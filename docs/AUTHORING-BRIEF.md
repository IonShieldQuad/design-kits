# Authoring brief — read this first

You are working in **`H:\Work\design-kits`**, a reusable UI theme-kit library (Windows host;
your shell is git-bash, so use POSIX syntax, and pass `C:/…`-style paths to native tools).
Each kit is a portable design-token set consumed by **one shared component lab**, and the
library is published at <https://ionshieldquad.github.io/design-kits/>.

Read, in this order:

1. this file — your contract and workflow;
2. `docs/KIT-SPEC.md` — the authoring contract (required tokens, optional capabilities);
3. `kits/retro-anime/` — the most recent full kit; copy its level of rigour and file shape;
4. `templates/lab.css` — what the shared lab actually consumes.

## The one architectural rule

**A kit is a skin, not a layout.** `templates/lab.html` and `templates/lab.css` are shared and
must **not** be edited. Every visual difference must come from your tokens. If you think you need
custom HTML, the token set is underspecified — fix the tokens.

## Files you author

Inside `kits/<slug>/` only. Touch nothing else in the repo.

| File | Required | Notes |
|---|---|---|
| `tokens.css` | yes | `:root { … }` defining the contract |
| `DESIGN.md` | yes | Google DESIGN.md format |
| `kit.json` | yes | gallery metadata |
| `README.md` | yes | stance, choices, trade-offs, when to use |
| `kit.css` | **no** | the escape hatch — read the `kit.css` section of `KIT-SPEC.md` first. Prefer tokens: a shadow, a radius, a dither and a gradient are all tokens. Only a *stacked construction* (a panel built from two offset plates) needs `kit.css`. |

`index.html`, `DESIGN.html`, `tokens.json`, `theme.css`, `tailwind.theme.json` are **generated**.

## Commands

```bash
# generate YOUR lab (and your spec page)
cd /h/Work/design-kits && python tools/build.py --only <slug> --no-export --no-lint

# render it in a real headless browser and assert on computed styles
cd /h/Work/design-kits && KIT_SHOTS="$LOCALAPPDATA/Temp/<slug>-shots" node tools/verify-lab.cjs <slug>
```

`verify-lab.cjs` must end with `PASS  <slug>`. It reads computed styles, so it catches tokens that
silently fall back, and it samples the real rendered pixel behind text to grade contrast.

**You MUST pass `--only <slug>`.** A bare `python tools/build.py` rewrites the shared gallery,
manifest and picker tables, which other authors are running concurrently — that races and is
forbidden here.

**Write all four files before your first build.** A build pass reads *every* kit directory, so if
another author is mid-write a sibling can be briefly unreadable and the pass will fail. If that
happens, wait a few seconds and retry — do not "fix" another kit.

**Do NOT** run git commands, commit, or edit anything outside `kits/<slug>/`.

## Contrast — measure, never eyeball

Write a small Python script (`python`, not `python3`: PIL 12.3.0 + numpy 2.4.6 are installed) and
report the numbers. Grade the **rendered** value, and grade against the ground the ink actually
sits on:

- `--text` ≥ **7:1** on every solid ground (`--surface`, `--surface-2`, every `--bg` gradient stop)
- `--text-muted` ≥ **4.5:1** everywhere
- `--text-dim` ≥ **4.55:1** on **every** ground including `--surface-2` and every `--bg` stop —
  this is the token that fails most often (it backs every caption, hint and label)
- `--accent-ink` ≥ **4.5:1** on every ground **and on its own `--accent-soft` tint composited over
  the surface** (a badge sits on a ~12–18% tint of the accent; grade the composite, not the tint)
- `--text-invert` on `--accent` ≥ **4.5:1** (use the label colour you actually declare — cream is
  not white, and the difference decides pass/fail)
- `--ok` / `--warn` / `--danger` / `--info` ≥ **4.5:1** on the ground they are used on
- `--focus-ring` ≥ **3:1**

For a **light** kit the binding ground is the **palest** stop; for a **dark** kit it is the
brightest. Solving `--text-dim` against an average ground is how it ends up at 4.4:1 on the one
stop that matters.

Never use the `--accent` fill as a text colour: declare `--accent-ink` (and `--accent-ink-hover`).
Five kits in this library shipped with unreadable accent-as-text because they skipped it.

## Signature motifs — the single most repeated failure

Extras named `--<slug>-*` (or listed in `kit.json`'s `signature`) render in a **Signature** strip
as ~168×72 tiles on `--surface-2`. Rules:

- **Check the tiles, not the page.** A motif tuned for subtlety is invisible there. A tile that
  renders flat is the number-one defect in this library.
- **Cap at two or three motifs** (four only in an unusually rich genre), each doing a *different*
  job. Two motifs using the same device are redundant and will be cut.
- **Structure beats gradient.** A droplet is a highlight plus a colour, not a flat tint. Chrome is
  hard bands with a crisp dark band in the middle, not a light-to-dark blur. A prism disperses into
  ordered hard bands. A dithered field is `repeating-conic-gradient(a 0 25%, b 0 50%)` with
  `background-size: 2px 2px`.
- **A token may hold DRAWN ARTWORK** when a form is organic or physical (a curve, a frond, a
  mechanism, a perspective, a glyph). Use an inline SVG data URL, **base64**:
  `url("data:image/svg+xml;base64,…") 0 0 / 74px 74px repeat, <a base layer>`.
  Never hand-percent-encode — a double-encoded `#` fails *silently* as a blank tile (base64 avoids
  the whole class). Worked examples: `kits/gothic/tokens.css`, `kits/retro-anime/tokens.css`,
  `kits/pixel-dmg/tokens.css`.
- Give drawn artwork a base layer and scale it explicitly (`center / 92px 92px no-repeat` for a
  mark, `0 0 / 74px 74px repeat` for a field).
- A **box-shadow** value is applied to a small bevel by the generator rather than painted, so a
  halo/glow token is legitimate.
- Prove each tile is not a flat plate: render the token as `background:` on a 168×72 box,
  screenshot it, and print the per-tile pixel standard deviation (PIL). Report the numbers.

## Opt-in capabilities the lab honours

`--accent-ink`/`--accent-ink-hover` · `--text-on-surface(-muted)` · `--text-on-surface-2(-muted)`
· `--clip` + `--cut` (chamfer; note `clip-path` also cuts borders and clips shadows) ·
`--input-inset` (recessed fields) · `--media-bg` / `--media-op` (the card media panel; the default
is a generic two-stop accent ramp — use this for your texture) · `--wash` (replaces the masthead's
radial bloom) · `--fill-bg` (progress + avatar fills) · `--btn-shadow` (applied to *every* button
variant) · `--pixel-render` (`image-rendering`, for pixel/low-res art) · `--check-appearance`,
`--check-bg`, `--check-border`, `--check-checked` (square the native checkbox/radio — they ignore
`border-radius`).

`--bg` accepts any background layer list: a hex, a gradient (use **px** stops, not `%`, so the
band lands inside the first viewport), or an **image** with its own size/position. An image layer
on `--bg` raises arbitrary pixels' luminance, so if you use one, verify contrast against its
lightest and darkest regions or keep it clear of type.

## Non-smooth kits (pixel art, 8-bit, 90s chrome, cockpit)

Smoothness enters through five doors; shut all five and say how in your report:

1. curves → every `--radius-*` is `0px` (and square the checkbox/radio with the `--check-*` tokens)
2. soft shadows → **zero-blur offset** shadows only; never a blurred drop shadow
3. gradients → hard stops (two stops at one position) or a dither; a smoothly fading `--bg` is the
   biggest giveaway
4. scaled artwork → **draw small and scale up** (`--pixel-render: pixelated` + a ~160×100 asset)
5. blur → `--blur: none`, no `backdrop-filter`

## Typography and legibility

Two families plus a mono is the usual maximum; a single family is a valid answer. All faces must
come from Google Fonts, and `kit.json`'s `fonts_url` must cover **every weight you use**. UI chrome
(kickers, chips, nav labels, meta lines) is **≥ 12px** — small grey-on-dark labels are the
recurring complaint in review.

## `DESIGN.md` rules

YAML front matter (`colors` as **hex only** — the linter *errors* on gradients there; `typography`;
`rounded`; `spacing`; `components`), then body sections in exactly this order: `## Overview`,
`## Colors`, `## Typography`, `## Layout`, `## Elevation & Depth`, `## Shapes`, `## Components`,
`## Do's and Don'ts`.

Component sub-keys are whitelisted to `backgroundColor`, `textColor`, `typography`, `rounded`,
`padding`, `size`, `height`, `width` — anything else (`boxShadow`, `borderColor`, `backgroundImage`,
`fontWeight`) warns and is dropped from the exports, so describe those in prose. Reference every
palette colour from at least one component, or document the accepted orphaned-token warning.
`textColor` must be the colour that actually renders: if a button's label comes from `--accent-ink`,
declare `primary-ink`, not `primary`.

## `kit.json`

```json
{ "name": "…", "tagline": "…", "signature": ["--slug-a", "--slug-b"],
  "order": 000, "fonts_url": "https://fonts.googleapis.com/css2?…", "fonts_label": "A · B · C",
  "mode": "light|dark", "source": "original", "tags": ["…"], "use_when": "…" }
```

Tags: include the mode plus 3–6 descriptive, lowercase, hyphenated tags.

## Report back

1. the files you wrote;
2. your contrast table's **worst pair** with its measured number and the ground it was measured on;
3. the `verify-lab.cjs` PASS line;
4. each signature motif, and its measured non-flatness (std-dev);
5. anything you could not express with tokens — say so honestly rather than faking it.

Do not claim a number you did not measure.
