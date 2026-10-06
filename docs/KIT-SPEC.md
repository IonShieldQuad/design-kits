# Kit authoring contract (v1)

A kit is a **skin**, not a layout. You author the design language; the shared lab
(`templates/lab.html` + `templates/lab.css`) supplies the markup. If your kit needs custom
HTML to look good, the token set is underspecified — fix the tokens.

## Files a kit must contain

| File | Owner | Notes |
|---|---|---|
| `DESIGN.md` | you | Google DESIGN.md format. YAML front matter = normative values, body = rationale |
| `tokens.css` | you | `:root { ... }` defining the token contract below |
| `kit.json` | you | presentation metadata for the gallery (see below) |
| `README.md` | you | stance, key choices, trade-offs, when to use |
| `kit.css` | you, **optional** | the escape hatch — see below. Absent for most kits |
| `index.html` | generated | component lab — `python tools/build.py` |
| `tokens.json`, `tailwind.theme.json`, `theme.css` | generated | exports — `python tools/build.py` |

## Token contract — REQUIRED names

Define these exact names in `tokens.css`. The lab consumes them; a kit missing one still
renders (fallbacks) but is considered incomplete and `build.py` will warn.

```css
:root{
  /* surfaces */
  --bg:            /* page background — hex OR gradient */
  --bg-2:          /* secondary background / gradient stop */
  --surface:       /* cards, panels */
  --surface-2:     /* nested panels, inputs, subtle fills */
  --overlay:       /* modal scrim (rgba) */

  /* text */
  --text:          /* primary text */
  --text-muted:    /* secondary text */
  --text-dim:      /* tertiary text, placeholders, captions */
  --text-invert:   /* text on --accent */

  /* brand */
  --accent:        /* the single primary action colour */
  --accent-hover:  /* its hover state */
  --accent-2:      /* second accent — gradients, charts, media */
  --accent-soft:   /* low-alpha tint of --accent for backgrounds/rings (rgba) */

  /* status */
  --ok: --warn: --danger: --info:

  /* lines */
  --border:        /* default hairline colour (hex or rgba) */
  --border-strong: /* emphasised divider / input border colour */
  --border-w:      /* border width — 1px default; 2-3px for bold-line/retro/brutalist kits */
  --focus-ring:    /* keyboard focus outline colour */

  /* shape */
  --radius-sm: --radius-md: --radius-lg: --radius-pill:
  --cut:           /* corner-cut size if the kit uses clip-path corners, else 0px */

  /* type — full font stacks, always include a system fallback */
  --font-display: --font-body: --font-mono:
  --tracking-caps: --tracking-display:

  /* depth */
  --shadow-1: --shadow-2: --glow: --blur:

  /* motion */
  --dur: --ease:
}
```

Extras are allowed and ignored by the lab (e.g. `--neon-cyan`, `--hologlow`). Prefix them
with the kit slug if they could collide.

## Optional capabilities (declare to enable)

These are not required, but the shared lab honours them when present:

| Token | Effect |
|---|---|
| `--clip` | opt-in chamfer. Set `--cut: 12px` plus `--clip: polygon(var(--cut) 0, 100% 0, 100% calc(100% - var(--cut)), calc(100% - var(--cut)) 100%, 0 100%, 0 var(--cut))` and the lab applies `clip-path` to cards, buttons, inputs, badges, alerts, nav and code blocks. **Two caveats:** (1) `clip-path` also cuts the border along the diagonal, so a chamfered edge is borderless; (2) it clips `box-shadow` and `outline` too, so a glow, an emboss or a focus ring is eaten — re-express those as `filter: drop-shadow(...)`, which follows the clipped silhouette, and turn a clipped focus ring into a border-colour change. Both are documented limitations, not bugs. |
| `--accent-ink` | the accent colour for **text** (eyebrow, links, active nav/tab, secondary-button labels, inline code, badges) as opposed to fill. A colour that works as a button fill is frequently too light to read as a small label — dark-glass's accent is 3.8:1 as text, summer-sunset's orange needed darkening, and cyber-angel's cyan fill is 1.58:1 on light. Declare a text-safe member of the same family; falls back to `--accent`. |
| `--accent-ink-hover` | the hover step for accent text. Needed because `--accent-hover` is a *fill* hover and often too light to read; falls back to `--accent-ink`. |
| `--text-on-surface`, `--text-on-surface-muted` | text inside `.card`. Needed when `--surface` contrasts with `--bg` (light card on a dark canvas, or the reverse) — otherwise card text takes `--text` and goes unreadable. |
| `--text-on-surface-2`, `--text-on-surface-2-muted` | text inside inputs, badges, alerts and code blocks (everything on `--surface-2`). Needed when `--surface-2` is a dark inset sitting inside a light card, which is a three-tier surface stack. |

Three-tier stacks (dark canvas → light card → dark inset) are what these exist for; without
them the lab can only express one text colour per page.

## `kit.css` — the escape hatch (optional)

The token contract carries a design's *colours, type, shape and depth*. It cannot carry a
**construction**: a panel built from a white underlayer plus a clipped layer on top, a component
that needs its own pseudo-elements, bespoke patterning. When a kit genuinely needs that, it ships
`kit.css` beside `tokens.css` and the build links it into that kit's lab automatically.

Rules for `kit.css`:

1. It may only touch the shared lab's **component selectors** (`.card`, `.btn`, `.input`, …)
   using the kit's own tokens — no inventions the lab has no markup for.
2. It must never hardcode a colour. Go through `var(--token)` like everything else.
3. It must be small enough to explain in a paragraph, and the kit README must say what it does
   and why the tokens alone were insufficient.
4. It is per-kit. If two kits need the same construction, the *lab* or the contract is missing
   something — fix that instead of copying the stylesheet.

A worked example: a two-layer panel needs `position: relative` plus a `::before` offset underlay,
which no colour token can express:

```css
.card { position: relative; isolation: isolate; }
.card::before {
  content: ""; position: absolute; inset: 0; transform: translate(4px, 4px);
  background: var(--<kit>-canvas); clip-path: var(--clip); z-index: -1;
}
```

**The boundary:** bespoke vector artwork is not a theme. If a design's identity lives in custom
SVG geometry, that is a front-end, not a reusable kit — ship the SVG under `assets/` and let
`kit.css` place it, but do not claim the theme carries it. A kit is judged on whether it
*identifies* a design at 200×120, not on reproducing one screen pixel-for-pixel.

## A token can hold drawn artwork (when gradients genuinely cannot)

A *motif* is a different thing from bespoke artwork: it is part of the skin, and a token may
carry it as an inline SVG data URI. Reach for this when a form is organic and gradients keep
failing — a barbed vine built from `repeating-linear-gradient` reads as plaid, tartan or fencing
because a sprig needs a curve and a spur at an angle to the stem; a rose built from nested
radial rings reads as a bullseye, and no amount of uneven petal placement fixes it, because
rings have no petal *divisions*.

```css
--gothic-rose:
  /* drawn bloom: an asymmetric spiralling line reads as a rose where rings cannot */
  url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0…") center / 92px 92px no-repeat,
  radial-gradient(circle at 50% 46%, #6d0d15 0%, #2a060a 72%);
```

Rules that save real time:

1. **Use base64, not hand-percent-encoding.** A manually encoded URI is easy to double-encode
   (`#` → `%23` in the source, then `%` → `%25`), and it then fails *silently* — the tile renders
   blank with no console error in the tile, just a `net::ERR_INVALID_URL` request failure.
2. **A data URI contains a semicolon** (`…;base64,`), so any tooling that parses `tokens.css`
   with a naive `[^;]+` regex will truncate the value at `;base64` and produce a broken
   declaration. Parsers must track quote state and paren depth. (The reference `build.py`
   does; check yours.)
3. **Give it a base layer.** A drawn motif is usually line art, so pair it with a colour or
   gradient layer beneath, or the tile shows only the kit's flat surface.
4. **Don't wrap a data URI in `url()` for an HTML `src`** — `url(...)` is CSS syntax. That
   mistake looks exactly like a rendering bug and wastes a debugging cycle.
5. Scale it explicitly: `center / 92px 92px no-repeat` for a single mark, `0 0 / 74px 74px repeat`
   for a tiled field.

## kit.json

```json
{
  "name": "Quiet",
  "tagline": "Calm surfaces for tools you live in",
  "index": "03",
  "order": 30,
  "fonts_url": "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap",
  "fonts_label": "Inter",
  "mode": "dark",
  "source": "derived from simple-website-test",
  "tags": ["dark", "app", "minimal"]
}
```

- `order` — gallery sort key. Leave gaps (10, 20, 30…) so kits can be inserted later.
  The gallery number (`01`, `02`, …) is **derived** from this; a hand-written `index` field is
  ignored and reported as stale, so don't bother numbering by hand.
- `use_when` — optional one-liner for the generated picker table in `AGENTS.md`
  ("portfolio, product marketing for dev tools"). Falls back to `tagline`.
- `signature` — optional list of token names to render in the lab's **Signature** section.
  Default behaviour without it: every `--<slug>-*` token is treated as signature material.
  Declare it explicitly when your kit's bespoke tokens are named descriptively instead
  (e.g. `["--nebula-1", "--starfield", "--halo-star"]`). Unknown names are reported as warnings.
- `mode` — `dark` | `light`. Drives the gallery chip and is a filter facet.
- `fonts_url` — a single Google Fonts URL with every family/weight the kit uses. Empty
  string = system fonts only.
- `source` — where the palette came from. Be honest; "original" is fine.

## DESIGN.md rules

1. `version: alpha`, then `name:` and `description:`. Required.
2. `colors:` must define at least `primary`, `secondary`, `tertiary`, `neutral` — these are
   the spec's own names, not the CSS token names. Keep them mapped to the accent/surface
   family: `primary` = the action colour, `neutral` = the page ground.
3. **Hex colours are quoted strings.** `primary: "#00e5ff"`. Unquoted `#…` breaks YAML.
4. **Negative dimensions are quoted.** `letterSpacing: "-0.02em"`.
5. Sections, in this order, skipping any you don't need:
   Overview · Colors · Typography · Layout · Elevation & Depth · Shapes · Components ·
   Do's and Don'ts. Out-of-order sections produce linter warnings.
6. `components:` is where the kit earns its keep. Define at least `button-primary`,
   `button-primary-hover`, `button-secondary`, `card`, `input`, `badge`. Reference colours
   with `{colors.primary}` — never re-type a hex.
7. **Variants are siblings, not nested**: `button-primary-hover`, not `button-primary.hover`.
8. Typography sub-properties: only `fontFamily`, `fontSize`, `fontWeight`, `lineHeight`,
   `letterSpacing`, `fontFeature`, `fontVariation`. A typo is silently dropped.

## Quality bar

- **Contrast:** `--text` on `--bg` ≥ 7:1, `--text-muted` on `--surface` ≥ 4.5:1,
  `--text-invert` on `--accent` ≥ 4.5:1, and `--text-dim` ≥ 4.55:1 against `--bg` and
  `--surface`. **Carve-out:** when `--surface-2` deliberately *inverts* the kit (a dark well
  inside a light shell, or the reverse — cyber-angel's `#242424` panel), no single `--text-dim`
  can clear both families; the provable ceiling on the inverted ground is 3.31:1. In that case
  the paired `--text-on-surface-2*` tokens carry that tier, and the kit must state the ceiling
  in its README rather than lightening the ground. Run the linter; fix warnings.
- **One accent, one second accent.** A third "look at me" colour is how kits start looking
  like a rainbow. Status colours don't count toward this.
- **Typography comes from a real pairing**, not five fonts. Two families (display + body) and
  a mono is the usual maximum; a single family is also a valid answer.
- **The kit must be recognisable in a 200×120 thumbnail.** If you can't describe it in one
  sentence, it isn't a kit — it's a screenshot.
- **Never invent a value you can derive.** If a colour is a 12% tint of the accent, express
  it as `rgba(...)`/`color-mix()` — say so in the README.
- **Every signature token must be legible at 168×72 on the tile base (`--surface-2`).** This is
  the most-repeated failure in this library: an overlay tuned for subtlety over a mid-tone ground
  (a mist, a light ray, a sheen, a white wash) renders as an empty chip over a near-white or dark
  tile, so the kit's whole premise looks like nothing. Check the tiles, not just the page — and if
  the token is an overlay, give it enough presence (or a second layer) to survive on its own. Two
  motifs is plenty; a third weak one dilutes the two strong ones.

## Self-check before you call it done

```bash
cd H:/Work/design-kits
python tools/build.py                          # generates lab + gallery, lints every kit
npx -y -p @google/design.md designmd lint kits/<slug>/DESIGN.md
```

Both must be free of *errors*. Warnings you consciously keep should be noted in the kit's
README ("`contrast-ratio` warning on `badge` is intentional: it is decorative only").
