#!/usr/bin/env python3
"""
design-kits build.

Discovers every kit under kits/, then:
  1. generates kits/<slug>/index.html from templates/lab.html  (the component lab)
  2. exports tokens.json / tailwind.theme.json / theme.css via @google/design.md
  3. lints each DESIGN.md and reports contrast findings
  4. regenerates the gallery (root index.html) and manifest.json

Adding a kit = create kits/<slug>/ with DESIGN.md + tokens.css + kit.json + README.md,
then run this. Nothing to register by hand.

Usage:
  python tools/build.py                 # generate everything
  python tools/build.py --no-export     # skip npx exports (fast)
  python tools/build.py --no-lint       # skip the DESIGN.md linter
  python tools/build.py --check         # verify generated files are up to date (CI)

Zero third-party dependencies. Requires npx only for (2) and (3).
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KITS_DIR = ROOT / "kits"
TPL = ROOT / "templates"

# Token contract v1 — see docs/KIT-SPEC.md. Missing names are a warning, not an error.
REQUIRED_TOKENS = [
    "--bg", "--bg-2", "--surface", "--surface-2", "--overlay",
    "--text", "--text-muted", "--text-dim", "--text-invert",
    "--accent", "--accent-hover", "--accent-2", "--accent-soft",
    "--ok", "--warn", "--danger", "--info",
    "--border", "--border-strong", "--focus-ring", "--border-w",
    "--radius-sm", "--radius-md", "--radius-lg", "--radius-pill", "--cut",
    "--font-display", "--font-body", "--font-mono", "--tracking-caps",
    "--shadow-1", "--shadow-2", "--glow", "--blur",
    "--dur", "--ease",
]

SWATCH_TOKENS = [
    ("--bg", "bg"), ("--surface", "surface"), ("--border", "border"),
    ("--accent", "accent"), ("--accent-2", "accent 2"), ("--ok", "ok"),
    ("--warn", "warn"), ("--danger", "danger"),
]

# Optional capabilities: a kit may declare these and the lab will honour them. Never a "gap".
#   --clip                  opt-in chamfer (clip-path); also cuts the border along the diagonal
#   --text-on-surface*      text inside .card (when --surface contrasts with --bg)
#   --text-on-surface-2*    text inside inputs/badges/alerts (when --surface-2 contrasts)
OPTIONAL_TOKENS = [
    # text accessibility
    "--accent-ink", "--accent-ink-hover", "--text-on-surface", "--text-on-surface-muted",
    "--text-on-surface-2", "--text-on-surface-2-muted",
    # shape / construction
    "--clip", "--input-inset", "--btn-shadow",
    "--check-appearance", "--check-bg", "--check-border", "--check-checked",
    # surfaces the lab would otherwise hardcode
    "--media-bg", "--media-op", "--wash", "--fill-bg",
    # rendering
    "--pixel-render",
]

OK = "\033[92m✓\033[0m"
WARN = "\033[93m!\033[0m"
ERR = "\033[91m✗\033[0m"


# --------------------------------------------------------------------------- io
def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_if_changed(path: Path, content: str, check: bool) -> bool:
    """Write content; in check mode only report. Returns True if the file is/was current."""
    old = read(path) if path.exists() else None
    if check:
        return old == content
    if old != content:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    return True


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]


def short_value(v: str) -> str:
    """Swatch caption. A raw gradient string wraps into a 200px-tall cell and wrecks the row."""
    v = " ".join(v.split())
    if "gradient(" in v:
        return "gradient"
    if v.startswith(("rgba(", "rgb(", "hsla(")):
        try:
            fn = v[: v.index("(") + 1]
            inner = v[v.index("(") + 1: v.rindex(")")]
            return fn + ",".join(x.strip() for x in inner.split(",")) + ")"
        except ValueError:
            return v[:22]
    return v if len(v) <= 22 else v[:21] + "…"


def normalize_gradient(v: str) -> str:
    """Make a gradient readable inside a small chip.

    A gradient whose stops are in px (which kits use so the band lands in the first screen)
    clamps inside a 40px swatch or a 72px tile and reads as a flat colour. Rescale such
    gradients to evenly spaced percentages for preview purposes only. Only applied when the
    value has no nested parentheses, so `rgba()` stops are left untouched.
    """
    if "gradient(" not in v or not re.search(r"\d+px", v) or v.count("(") != 1:
        return v
    i, j = v.index("("), v.rindex(")")
    head, inner, tail = v[: i + 1], v[i + 1: j], v[j:]
    parts = [p.strip() for p in inner.split(",") if p.strip()]
    leading: list[str] = []
    while parts and not re.match(r"^(#|rgb|hsl|oklch|lab|color\()", parts[0]):
        leading.append(parts.pop(0))
    if len(parts) < 2:
        return v
    stops = []
    for n, p in enumerate(parts):
        colour = re.match(r"^(#\S+|rgba?\([^)]*\)|hsla?\([^)]*\)|\S+)", p).group(1)
        stops.append(f"{colour} {100 * n / (len(parts) - 1):.0f}%")
    return head + ", ".join(leading + stops) + tail


def swatch_label(v: str) -> str:
    """Caption with a break opportunity after each comma.

    'rgba(255,255,255,.58)' in an 82px mono cell has no space to wrap at, so the browser
    would either overflow or (with overflow-wrap:anywhere) split the number mid-digit.
    <wbr> gives it a legal break point instead.
    """
    s = short_value(v)
    if "," not in s:
        return html.escape(s)
    return "<wbr>,".join(html.escape(p) for p in s.split(","))


def is_translucent(v: str) -> bool:
    """True when the swatch needs a checkerboard under it or it disappears into the page."""
    v = v.strip().lower()
    if "gradient(" in v:
        return True  # gradients often start/end translucent; the checker costs nothing
    if v.startswith("rgba("):
        try:
            return float(v[v.rindex(",") + 1: v.rindex(")")].strip()) < 0.98
        except ValueError:
            return True
    return v in ("transparent", "none")


# ------------------------------------------------------------------ css parsing
COMMENT_RE = re.compile(r"/\*.*?\*/", re.S)
VAR_RE = re.compile(r"(--[a-zA-Z0-9_-]+)\s*:\s*")


def _read_value(body: str, start: int) -> tuple[str, int]:
    """Read a custom-property value from `start` until its terminating `;`.

    A naive `[^;]+` is wrong: values legitimately contain semicolons inside quotes or parens
    (any `data:` URI does — `data:image/svg+xml;base64,...`). Track paren depth and quotes, and
    stop only at a `;` at depth 0 outside quotes.
    """
    depth, quote, i = 0, "", start
    while i < len(body):
        c = body[i]
        if quote:
            if c == "\\":
                i += 2
                continue
            if c == quote:
                quote = ""
        elif c in "\"'":
            quote = c
        elif c in "([":
            depth += 1
        elif c in ")]":
            depth -= 1
        elif c == ";" and depth == 0:
            return body[start:i], i + 1
        i += 1
    return body[start:], len(body)


def parse_css_vars(css: str) -> dict[str, str]:
    """Flat { --name: value } map. Later definitions win (last :root block)."""
    body = COMMENT_RE.sub("", css)
    out: dict[str, str] = {}
    pos = 0
    while True:
        m = VAR_RE.search(body, pos)
        if not m:
            break
        value, end = _read_value(body, m.end())
        out[m.group(1)] = " ".join(value.split())
        pos = end
    return out


# ------------------------------------------------------------- design.md parse
def split_front_matter(md: str) -> tuple[str, str]:
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", md, re.S)
    if not m:
        return "", md
    return m.group(1), m.group(2)


def fm_scalar(fm: str, key: str) -> str | None:
    m = re.search(rf"^{re.escape(key)}\s*:\s*(.+?)\s*$", fm, re.M)
    if not m:
        return None
    return m.group(1).strip().strip('"').strip("'")


def fm_block(fm: str, key: str) -> dict[str, str]:
    """Collect `key:` followed by an indented scalar map (colors:, rounded:, spacing:)."""
    lines = fm.splitlines()
    out: dict[str, str] = {}
    i = 0
    while i < len(lines):
        if re.match(rf"^{re.escape(key)}\s*:\s*$", lines[i]):
            i += 1
            while i < len(lines):
                line = lines[i]
                if not line.strip():
                    i += 1
                    continue
                if not line.startswith((" ", "\t")):
                    break
                m = re.match(r"^\s+([A-Za-z0-9_.-]+)\s*:\s*(.+?)\s*$", line)
                if m:
                    out[m.group(1)] = m.group(2).strip().strip('"').strip("'")
                i += 1
            break
        i += 1
    return out


def fm_typography_families(fm: str) -> list[str]:
    """Pull fontFamily values out of the typography block, de-duplicated, in order."""
    lines = fm.splitlines()
    fams: list[str] = []
    inside = False
    for line in lines:
        if re.match(r"^typography\s*:\s*$", line):
            inside = True
            continue
        if inside:
            if line and not line.startswith((" ", "\t")):
                break
            m = re.match(r"^\s+fontFamily\s*:\s*(.+?)\s*$", line)
            if m:
                fam = m.group(1).strip().strip('"').strip("'")
                if fam and fam not in fams:
                    fams.append(fam)
    return fams


# ------------------------------------------------------------------ kit loading
class Kit:
    def __init__(self, path: Path):
        self.dir = path
        self.slug = path.name
        self.seq: int | None = None  # gallery position, assigned after sorting
        self.optional_used: list[str] = []
        self.design_path = path / "DESIGN.md"
        self.tokens_path = path / "tokens.css"
        self.meta_path = path / "kit.json"
        self.problems: list[str] = []
        self.warnings: list[str] = []

        if not self.design_path.exists():
            self.problems.append("missing DESIGN.md")
            self.design = ""
        else:
            self.design = read(self.design_path)
        self.fm, self.body = split_front_matter(self.design)

        if not self.tokens_path.exists():
            self.problems.append("missing tokens.css")
            self.tokens = ""
        else:
            self.tokens = read(self.tokens_path)

        self.meta: dict = json.loads(read(self.meta_path)) if self.meta_path.exists() else {}
        if not self.meta_path.exists():
            self.warnings.append("missing kit.json (gallery falls back to defaults)")

        self.vars = parse_css_vars(self.tokens)

    # -- derived presentation values -----------------------------------------
    @property
    def name(self) -> str:
        return self.meta.get("name") or fm_scalar(self.fm, "name") or self.slug.title()

    @property
    def tagline(self) -> str:
        return self.meta.get("tagline") or fm_scalar(self.fm, "description") or ""

    @property
    def description(self) -> str:
        return fm_scalar(self.fm, "description") or self.tagline

    @property
    def index_label(self) -> str:
        """Derived from gallery position (order), not hand-maintained — inserting a kit must not
        require renumbering every other kit.json."""
        if self.seq is not None:
            return f"{self.seq:02d}"
        return str(self.meta.get("index") or "—")

    @property
    def order(self) -> int:
        try:
            return int(self.meta.get("order", 999))
        except (TypeError, ValueError):
            return 999

    @property
    def mode(self) -> str:
        return (self.meta.get("mode") or "dark").lower()

    @property
    def tags(self) -> list[str]:
        tags = list(self.meta.get("tags") or [])
        if self.mode not in tags:
            tags.insert(0, self.mode)
        return tags

    @property
    def fonts_url(self) -> str:
        return self.meta.get("fonts_url") or ""

    @property
    def fonts_label(self) -> str:
        if self.meta.get("fonts_label"):
            return self.meta["fonts_label"]
        fams = fm_typography_families(self.fm)
        return " · ".join(fams[:3]) if fams else "system fonts"

    @property
    def radius_label(self) -> str:
        r = fm_block(self.fm, "rounded")
        if r:
            parts = [r[k] for k in ("sm", "md", "lg") if k in r]
            if parts:
                return " / ".join(parts)
        return ", ".join(
            self.vars.get(k, "") for k in ("--radius-sm", "--radius-md") if self.vars.get(k)
        ) or "—"

    @property
    def swatch_pairs(self) -> list[tuple[str, str]]:
        """[(label, css value)] for the masthead + gallery strip."""
        out: list[tuple[str, str]] = []
        for tok, label in SWATCH_TOKENS:
            val = self.vars.get(tok)
            if val and val.lower() not in ("transparent", "none"):
                out.append((label, val))
        return out

    def check_tokens(self) -> None:
        missing = [t for t in REQUIRED_TOKENS if t not in self.vars]
        if missing:
            self.warnings.append("token contract gaps: " + ", ".join(missing))
        self.optional_used = [t for t in OPTIONAL_TOKENS if t in self.vars]

    # -- generated output ----------------------------------------------------
    def signature_section(self) -> str:
        """Render the kit's own slug-prefixed extra tokens.

        Convention: any token named `--<slug>-*` is the kit's signature material (a bespoke
        gradient, ramp, pattern or halo). Without this section those exist in tokens.css and
        appear nowhere in the lab — which is how a kit can be internally complete and still
        read as generic.
        """
        prefix = f"--{self.slug}-"
        declared = self.meta.get("signature")
        if isinstance(declared, list) and declared:
            # explicit declaration wins: an author may reasonably name material descriptively
            # (--nebula-1) rather than slug-prefixing it (--outer-space-nebula-1)
            extras = [(k, self.vars[k]) for k in declared if k in self.vars]
            missing = [k for k in declared if k not in self.vars]
            if missing:
                self.warnings.append("kit.json signature names unknown tokens: " + ", ".join(missing))
        else:
            extras = sorted((k, v) for k, v in self.vars.items() if k.startswith(prefix))
        extras = extras[:8]
        if not extras:
            return ""
        tiles = "".join(sig_tile(k, v) for k, v in extras)
        return (
            '  <section class="block">\n'
            '    <div class="block-head"><h2>Signature</h2>'
            '<span class="note">this kit\'s own extra tokens, rendered</span></div>\n'
            f'    <div class="tiles">{tiles}</div>\n'
            '  </section>\n'
        )

    def lab_html(self) -> str:
        tpl = read(TPL / "lab.html")
        swatches = "".join(
            f'<div class="swatch" title="{html.escape(v, quote=True)}">'
            f'<i><b style="background:{html.escape(normalize_gradient(v), quote=True)}"></b></i>'
            f'<span>{swatch_label(v)}</span>'
            f'<span>{html.escape(l)}</span></div>'
            for l, v in self.swatch_pairs
        )
        rep = {
            "{{SLUG}}": self.slug,
            "{{NAME}}": html.escape(self.name),
            "{{TAGLINE}}": html.escape(self.tagline),
            "{{DESCRIPTION}}": html.escape(self.description, quote=True),
            "{{INDEX}}": html.escape(self.index_label),
            "{{FONT_LINK}}": self.fonts_url,
            "{{FONTS_LABEL}}": html.escape(self.fonts_label),
            "{{RADIUS_LABEL}}": html.escape(self.radius_label),
            "{{SWATCHES}}": swatches,
            "{{SIGNATURE}}": self.signature_section(),
            # a kit that needs an actual CONSTRUCTION rather than a colour ships kit.css
            # (layered panels, bespoke patterning). Absent by default — the whole point of the
            # token contract is that most kits never need one.
            "{{KIT_CSS}}": ('<link rel="stylesheet" href="kit.css">'
                            if (self.dir / "kit.css").exists() else ""),
        }
        for k, v in rep.items():
            tpl = tpl.replace(k, v)
        return tpl

    def gallery_card(self) -> str:
        bg = self.vars.get("--bg", "#0b0d12")
        fg = self.vars.get("--text", "#e9edf5")
        surf = self.vars.get("--surface", "transparent")
        strip = "".join(
            f'<i style="background:{html.escape(normalize_gradient(v), quote=True)}"></i>' for _, v in self.swatch_pairs[:6]
        )
        chips = "".join(
            f'<span class="g-tag{" mode-" + self.mode if t == self.mode else ""}">{html.escape(t)}</span>'
            for t in self.tags[:4]
        )
        font_chip = f'<span class="g-tag">{html.escape(self.fonts_label.split(" · ")[0])}</span>'
        # A radial accent wash over the kit's own ground makes the preview readable at a glance.
        preview_bg = (
            f"background:{html.escape(bg, quote=True)};"
            f"background-image:radial-gradient(120% 130% at 18% 0%,"
            f"{html.escape(self.vars.get('--accent-soft', 'transparent'), quote=True)} 0%,transparent 60%),"
            f"linear-gradient(180deg,{html.escape(surf, quote=True)} 0%,transparent 100%);"
        )
        return f"""    <article class="g-card" data-tags="{html.escape(' '.join(self.tags))}">
      <div class="g-preview" style="{preview_bg}color:{html.escape(fg, quote=True)}">
        <span class="aa" style="font-family:{html.escape(self.vars.get('--font-display', 'inherit'), quote=True)}">Aa</span>
        <span class="swatchbar">{strip}</span>
      </div>
      <div class="g-body">
        <div class="g-title"><span class="num">{html.escape(self.index_label)}</span><h3>{html.escape(self.name)}</h3></div>
        <p class="g-tagline">{html.escape(self.tagline)}</p>
        <p class="g-desc">{html.escape(self.description)}</p>
        <div class="g-meta">{chips}{font_chip}</div>
        <div class="g-links">
          <a class="primary" href="kits/{self.slug}/index.html">Open lab →</a>
          <span class="spacer"></span>
          <a class="quiet" href="kits/{self.slug}/DESIGN.md">DESIGN.md</a>
          <a class="quiet" href="kits/{self.slug}/tokens.css">tokens.css</a>
        </div>
      </div>
    </article>"""

    def manifest_entry(self) -> dict:
        return {
            "slug": self.slug,
            "name": self.name,
            "tagline": self.tagline,
            "description": self.description,
            "index": self.index_label,
            "order": self.order,
            "mode": self.mode,
            "tags": self.tags,
            "fonts": self.fonts_label,
            "source": self.meta.get("source", ""),
            "colors": {k: v for k, v in (fm_block(self.fm, "colors")).items()},
            "files": {
                "design": f"kits/{self.slug}/DESIGN.md",
                "tokens": f"kits/{self.slug}/tokens.css",
                "lab": f"kits/{self.slug}/index.html",
                "readme": f"kits/{self.slug}/README.md",
            },
            "warnings": self.warnings,
        }


# --------------------------------------------------------------- generated docs
def sig_tile(name: str, value: str) -> str:
    """One Signature tile.

    An extra token is not always a background: `--summer-sunset-halo` is a box-shadow and
    `--chrome-sheen` is a gradient overlay. Painting a shadow value as `background` renders
    nothing at all, which is how a kit's proudest token ends up looking like an empty chip.
    So: backgrounds get painted, everything else gets APPLIED to a small bevel on the kit's
    own surface.
    """
    v = value.strip()
    looks_like_bg = bool(
        "gradient(" in v or v.startswith("url(")
        or re.match(r"^(#|rgb|hsl|oklch|lab|color\()", v)
    )
    inner = (
        f'<b style="background:{html.escape(normalize_gradient(v), quote=True)}"></b>' if looks_like_bg
        else f'<b class="fx" style="box-shadow:{html.escape(v, quote=True)}"></b>'
    )
    return (
        f'<figure class="tile" title="{html.escape(name)}: {html.escape(v, quote=True)}">'
        f'<span class="chip">{inner}</span>'
        f'<figcaption>{html.escape(name[2:])}</figcaption></figure>'
    )


def picker_table(kits: list) -> str:
    """The agent-facing picker table. Generated so it cannot drift from the kits."""
    rows = [
        "| Kit | Tone | Use when |",
        "|---|---|---|",
    ]
    for k in kits:
        tone = " · ".join(k.tags)
        use = " ".join((k.meta.get("use_when") or k.tagline).split())
        rows.append(f"| [`{k.slug}`](kits/{k.slug}/DESIGN.md) | {tone} | {use} |")
    return "\n".join(rows)


def inject_block(path: Path, marker: str, block: str, check: bool) -> bool:
    """Replace the region between <!-- BEGIN marker --> and <!-- END marker -->.
    No markers in the file = nothing to do (silently skipped)."""
    if not path.exists():
        return True
    text = read(path)
    begin, end = f"<!-- BEGIN {marker} -->", f"<!-- END {marker} -->"
    if begin not in text or end not in text:
        return True
    new = re.sub(re.escape(begin) + r".*?" + re.escape(end),
                 begin + "\n" + block + "\n" + end, text, flags=re.S)
    return write_if_changed(path, new, check)


# ------------------------------------------------------------------ npx bridge
def npx_design(*args: str, stdin_text: str | None = None) -> tuple[int, str]:
    """Run @google/design.md through npx. Returns (exit_code, stdout)."""
    exe = shutil.which("npx") or shutil.which("npx.cmd")
    if not exe:
        return 127, "npx not found on PATH"
    cmd = [exe, "-y", "-p", "@google/design.md", "designmd", *args]
    try:
        p = subprocess.run(
            cmd, input=stdin_text, capture_output=True, text=True, timeout=180,
            cwd=str(ROOT), shell=False,
        )
    except subprocess.TimeoutExpired:
        return 124, "timed out after 180s"
    return p.returncode, (p.stdout or "") + (p.stderr or "")


def export_all(kit: Kit) -> list[str]:
    log: list[str] = []
    jobs = [
        (["export", "--format", "dtcg", str(kit.design_path)], "tokens.json"),
        (["export", "--format", "json-tailwind", str(kit.design_path)], "tailwind.theme.json"),
        (["export", "--format", "css-tailwind", str(kit.design_path)], "theme.css"),
    ]
    for args, out_name in jobs:
        code, out = npx_design(*args)
        if code != 0 or not out.strip():
            log.append(f"{WARN} export {out_name} failed (exit {code}): {out.strip()[:160]}")
            continue
        (kit.dir / out_name).write_text(out.strip() + "\n", encoding="utf-8")
    return log


def lint_kit(kit: Kit) -> list[str]:
    code, out = npx_design("lint", "--format", "json", str(kit.design_path))
    findings: list[str] = []
    if code == 127:
        return [f"{WARN} linter unavailable ({out.strip()})"]
    payload = None
    try:
        payload = json.loads(out)
    except json.JSONDecodeError:
        m = re.search(r"\{.*\}", out, re.S)
        if m:
            try:
                payload = json.loads(m.group(0))
            except json.JSONDecodeError:
                payload = None
    if payload is None:
        if code != 0:
            return [f"{ERR} lint failed (exit {code}): {out.strip()[:200]}"]
        return []
    items = payload.get("findings") or payload.get("results") or []
    for f in items:
        sev = (f.get("severity") or "").lower()
        rid = f.get("rule") or f.get("ruleId") or "?"
        msg = f.get("message") or ""
        mark = ERR if sev in ("error", "fatal") else WARN
        findings.append(f"{mark} {rid}: {msg}")
    if code != 0 and not items:
        findings.append(f"{ERR} lint exit {code}: {out.strip()[:200]}")
    return findings


# ------------------------------------------------------------------------ main
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="verify generated files are current")
    ap.add_argument("--no-export", action="store_true", help="skip npx token exports")
    ap.add_argument("--no-lint", action="store_true", help="skip the DESIGN.md linter")
    ap.add_argument("--only", action="append", metavar="SLUG",
                    help="build just these kits (repeatable). Skips the shared gallery, manifest "
                         "and picker tables, so parallel kit authors cannot race on them.")
    args = ap.parse_args()

    if not KITS_DIR.exists():
        print(f"{ERR} no kits/ directory at {KITS_DIR}")
        return 2

    kits = sorted(
        (Kit(p) for p in KITS_DIR.iterdir() if p.is_dir() and not p.name.startswith(("_", "."))),
        key=lambda k: (k.order, k.slug),
    )
    if not kits:
        print(f"{WARN} no kits found yet — add kits/<slug>/ with DESIGN.md + tokens.css")

    # gallery position is derived, so inserting a kit never means renumbering the rest
    for i, k in enumerate(kits, 1):
        k.seq = i
        declared = str(k.meta.get("index") or "").strip()
        if declared and declared.lstrip("0") != str(i).lstrip("0"):
            k.warnings.append(
                f"kit.json index {declared!r} is stale — the gallery number is derived "
                f"from order (now {i:02d}); the field is ignored"
            )

    if args.only:
        known = {k.slug for k in kits}
        unknown = [s for s in args.only if s not in known]
        if unknown:
            print(f"{ERR} no such kit(s): {', '.join(unknown)}")
            return 2
    todo = [k for k in kits if not args.only or k.slug in args.only]

    stale: list[str] = []
    lint_errors = 0

    for kit in todo:
        kit.check_tokens()
        print(f"\n▸ {kit.slug}  ({kit.name})")
        for p in kit.problems:
            print(f"  {ERR} {p}")
        for w in kit.warnings:
            mark = ERR if w.startswith("token contract") else WARN
            print(f"  {mark} {w}")
        if kit.optional_used:
            print(f"  · optional: {', '.join(kit.optional_used)}")

        if write_if_changed(kit.dir / "index.html", kit.lab_html(), args.check):
            print(f"  {OK} lab html")
        else:
            stale.append(f"kits/{kit.slug}/index.html")
            print(f"  {ERR} lab html stale")

        if not args.no_export and not args.check:
            for line in export_all(kit):
                print(f"  {line}")
            exported = [n for n in ("tokens.json", "tailwind.theme.json", "theme.css") if (kit.dir / n).exists()]
            if exported:
                print(f"  {OK} exports: {', '.join(exported)}")

        if not args.no_lint and not args.check:
            findings = lint_kit(kit)
            if not findings:
                print(f"  {OK} DESIGN.md lint clean")
            for line in findings:
                print(f"  {line}")
                if line.startswith(ERR):
                    lint_errors += 1

    if args.only:
        print(f"\n{OK} built {len(todo)} kit(s) only — the shared gallery, manifest and picker "
              f"tables are left to the aggregating run")
        return 1 if lint_errors else 0

    # ---------------------------------------------------------------- gallery
    font_links = "\n".join(
        f'<link href="{k.fonts_url}" rel="stylesheet">' for k in kits if k.fonts_url
    )
    cards = "\n".join(k.gallery_card() for k in kits) or (
        '    <p class="g-desc">No kits yet. Add <code>kits/&lt;slug&gt;/</code> '
        "with DESIGN.md + tokens.css and re-run <code>python tools/build.py</code>.</p>"
    )
    # filter chips are derived from the tags actually in use — a hardcoded list silently rots
    # as kits are added (it did: the first chip set only covered the first seven kits).
    # A tag used by a single kit is noise once the library grows, so require >= 2, and cap the row.
    tag_counts: dict[str, int] = {}
    for k in kits:
        for t in k.tags:
            tag_counts[t] = tag_counts.get(t, 0) + 1
    ordered_tags = sorted(tag_counts, key=lambda t: (-tag_counts[t], t))
    shown = [t for t in ordered_tags if tag_counts[t] >= 2][:14]
    if len(shown) < 4:  # tiny libraries: show what there is
        shown = ordered_tags[:8]
    chips = ['<button class="g-chip" data-filter="all" aria-pressed="true">all</button>']
    chips += [
        f'<button class="g-chip" data-filter="{html.escape(t, quote=True)}" aria-pressed="false">'
        f'{html.escape(t)} {tag_counts[t]}</button>'
        for t in shown
    ]
    filters = "\n".join("    " + c for c in chips)

    gallery = read(TPL / "gallery.html")
    gallery = (
        gallery.replace("{{FONT_LINKS}}", font_links)
        .replace("{{CARDS}}", cards)
        .replace("{{FILTERS}}", filters)
        .replace("{{KIT_COUNT}}", str(len(kits)))
        .replace("{{TOKEN_COUNT}}", str(len(REQUIRED_TOKENS)))
    )
    if write_if_changed(ROOT / "index.html", gallery, args.check):
        print(f"\n{OK} gallery index.html ({len(kits)} kits)")
    else:
        stale.append("index.html")
        print(f"\n{ERR} gallery index.html is stale")

    manifest = {
        "generated_by": "tools/build.py",
        "contract_version": 1,
        "kit_count": len(kits),
        "required_tokens": REQUIRED_TOKENS,
        "kits": [k.manifest_entry() for k in kits],
    }
    manifest_text = json.dumps(manifest, indent=2, ensure_ascii=False) + "\n"
    if write_if_changed(ROOT / "manifest.json", manifest_text, args.check):
        print(f"{OK} manifest.json")
    else:
        stale.append("manifest.json")
        print(f"{ERR} manifest.json is stale")

    # the agent-facing picker table is generated too, so "hand it to another AI agent"
    # cannot go stale the moment a kit is added
    table = picker_table(kits)
    for doc in ("AGENTS.md", "README.md"):
        if inject_block(ROOT / doc, "KITS", table, args.check):
            print(f"{OK} {doc} kit table")
        else:
            stale.append(doc)
            print(f"{ERR} {doc} kit table is stale")

    print(f"\nmanifest digest {sha(manifest_text)} · kits {len(kits)}")
    if args.check and stale:
        print(f"{ERR} stale generated files: {', '.join(stale)} — run: python tools/build.py")
        return 1
    if lint_errors:
        print(f"{ERR} {lint_errors} lint error(s) — fix before shipping")
        return 1
    print(f"{OK} done")
    return 0


if __name__ == "__main__":
    sys.exit(main())
