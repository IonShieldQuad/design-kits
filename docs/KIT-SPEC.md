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
  --border:        /* default 1px hairline (hex or rgba) */
  --border-strong: /* emphasised divider / input border */
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
  `--text-invert` on `--accent` ≥ 4.5:1. Run the linter; fix warnings.
- **One accent, one second accent.** A third "look at me" colour is how kits start looking
  like a rainbow. Status colours don't count toward this.
- **Typography comes from a real pairing**, not five fonts. Two families (display + body) and
  a mono is the usual maximum; a single family is also a valid answer.
- **The kit must be recognisable in a 200×120 thumbnail.** If you can't describe it in one
  sentence, it isn't a kit — it's a screenshot.
- **Never invent a value you can derive.** If a colour is a 12% tint of the accent, express
  it as `rgba(...)`/`color-mix()` — say so in the README.

## Self-check before you call it done

```bash
cd H:/Work/design-kits
python tools/build.py                          # generates lab + gallery, lints every kit
npx -y -p @google/design.md designmd lint kits/<slug>/DESIGN.md
```

Both must be free of *errors*. Warnings you consciously keep should be noted in the kit's
README ("`contrast-ratio` warning on `badge` is intentional: it is decorative only").
