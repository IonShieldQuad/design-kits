"""Minimal markdown -> HTML for the generated DESIGN.html view.

Why this exists: GitHub Pages runs Jekyll, which REWRITES every .md file that carries front
matter into .html — so a link to `kits/<slug>/DESIGN.md` 404s on the live site even though the
file is in the repo. Two fixes, both applied: a `.nojekyll` marker so Pages serves files
verbatim, and this renderer so the link lands on something readable instead of a raw dump.

Deliberately small: it covers exactly what the kit specs use — front matter, ATX headings,
pipe tables, fenced code, bullet lists, paragraphs, and inline bold/code/italic/link.
"""
import html
import re


def _inline(s: str) -> str:
    s = html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])", r"<em>\1</em>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
    return s


def md_to_html(text: str) -> str:
    lines = text.split("\n")
    out, i = [], 0

    # ---- front matter: the normative values, kept verbatim but labelled
    if lines and lines[0].strip() == "---":
        end = next((n for n in range(1, len(lines)) if lines[n].strip() == "---"), None)
        if end:
            fm = "\n".join(lines[1:end])
            out.append(
                '<section class="spec-fm"><h2>Front matter &mdash; the normative values</h2>'
                "<p class=\"spec-note\">This block is the machine-readable half of the spec: "
                "another agent can read these token names and values directly.</p>"
                f"<pre><code>{html.escape(fm)}</code></pre></section>"
            )
            i = end + 1

    buf_para: list[str] = []

    def flush():
        if buf_para:
            out.append("<p>" + _inline(" ".join(buf_para)) + "</p>")
            buf_para.clear()

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith("```"):                       # fenced code
            flush()
            i += 1
            code = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code.append(lines[i]); i += 1
            out.append("<pre><code>" + html.escape("\n".join(code)) + "</code></pre>")
            i += 1
            continue

        if re.match(r"^\s*\|.*\|\s*$", line):              # pipe table
            flush()
            rows = []
            while i < len(lines) and re.match(r"^\s*\|.*\|\s*$", lines[i]):
                rows.append(lines[i].strip()); i += 1
            cells = lambda r: [c.strip() for c in r.strip("|").split("|")]
            body = rows[1:] if len(rows) > 1 and re.match(r"^[\s|:-]+$", rows[1]) else rows
            head = cells(rows[0]) if body is not rows else []
            t = ["<table>"]
            if head:
                t.append("<thead><tr>" + "".join(f"<th>{_inline(c)}</th>" for c in head) + "</tr></thead>")
            t.append("<tbody>")
            for r in body:
                t.append("<tr>" + "".join(f"<td>{_inline(c)}</td>" for c in cells(r)) + "</tr>")
            t.append("</tbody></table>")
            out.append("".join(t))
            continue

        m = re.match(r"^(#{1,6})\s+(.*)$", stripped)          # heading
        if m:
            flush()
            lvl = min(6, len(m.group(1)) + 1)                # the page owns <h1>
            aid = re.sub(r"[^a-z0-9]+", "-", m.group(2).lower()).strip("-")
            out.append(f'<h{lvl} id="{aid}">{_inline(m.group(2))}</h{lvl}>')
            i += 1
            continue

        if re.match(r"^\s*[-*]\s+", line):                   # bullet list
            flush()
            items = []
            while i < len(lines) and re.match(r"^\s*[-*]\s+", lines[i]):
                item = re.sub(r"^\s*[-*]\s+", "", lines[i])
                i += 1
                while i < len(lines) and lines[i].startswith("  ") and lines[i].strip():
                    item += " " + lines[i].strip(); i += 1
                items.append(f"<li>{_inline(item)}</li>")
            out.append("<ul>" + "".join(items) + "</ul>")
            continue

        if not stripped:
            flush(); i += 1; continue

        buf_para.append(stripped); i += 1

    flush()
    return "\n".join(out)
