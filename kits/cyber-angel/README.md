# Cyber Angel

**The angel of the singularity, as drawn.** Derived from the user's Figma file
**Marketplace-Cyber-Angel → page "UI Kit" → frame "Cyber Angel"** — not from a verbal brief.

A light shell with dark wells. `#D9D9D9` page, `#E0E0E0` panels, 1px **pure black** rules, and
a 12px 45° **chamfer** cutting opposite corners off every card, button, input, nav and badge.
Anything inset — inputs, badges, alerts, code, elevated cards — is the file's dark **Panel
`#242424`** carrying its **"On Panel" holo cyan**. Type is Syncopate (cap-set, wide-tracked),
Nova Flat and Montserrat.

- Kit: `cyber-angel` · order `60` · mode `light`
- Source: the Figma frame above (was "original" — the kit is now a derivation)
- Fonts: Syncopate · Nova Flat · Montserrat
- Tags: `light` `sharp` `bold` `holo` `geometric`
- Signature: the chamfer, the black rule, and the holo cyan fill / deep holo ink split

## Derivation — Figma token → kit token

Every value below is a token from that frame, or a documented derivation from one (nothing was
invented; nothing was eyeballed).

| Figma token | Kit token | Value |
|---|---|---|
| Background 2 | `--bg` | `#d9d9d9` |
| Surface | `--bg-2`, `--surface` | `#e0e0e0` |
| Panel | `--surface-2` | `#242424` |
| Background | `--overlay` `rgba(46,47,48,.62)`, `--cyber-angel-canvas` | `#2e2f30` |
| On Surface | `--text`, `--text-on-surface` | `#292929` |
| On Holo Dark | `--text-invert` / `{colors.on-primary}` | `#313131` |
| On Panel | `--accent-2`, `--info`, `--text-on-surface-2` | `#89dcff` |
| Outline | `--accent` | `#15b9ff` |
| Primary | (the same holo family as On Panel) | `#89dcff` |
| Border | `--border`, `--border-strong` | `#000000` |
| Disabled Dark / Light | recorded in `DESIGN.md` prose (deliberately not a checked token) | `#606060` / `#ffffff` |
| Holo Border Error | `--danger` (deepened for the light ground) | `#b32017` |
| On Panel Error | `--cyber-angel-danger-panel` | `#ff948f` |
| Holo Error | (source of `--danger`) | `#ff554a` |
| halo `#15B9FF40` @ r2/4/8 | `--glow` + `--cyber-angel-halo-ink`; `--cyber-angel-halo` as a wash | cyan halo |
| inner `#CDCDCD40` + drop `#00000040` | `--shadow-1`, `--shadow-2` | emboss + offset drop |
| background-blur radius 2 | `--blur` | `blur(2px)` |
| 45° cut, opposite corners | `--cut: 12px` + `--clip` | the signature |
| diagonal slash glyph | `--cyber-angel-slash` | 45° hatch |
| Syncopate / Nova Flat / Montserrat | `--font-display` / `--font-mono` / `--font-body` | — |

**Derived, not invented** (each one is a documented operation on a Figma value):

- `--text-muted #444444` — the midpoint of *On Surface* `#292929` and *Disabled Dark* `#606060`.
  That is exactly the secondary-text tier the file never names.
- `--text-dim #5c5c5c` — *Disabled Dark* `#606060` deepened one step so captions clear the
  4.55:1 floor on the page ground.
- `--accent-hover #4fcbff` — the midpoint of *Outline* `#15b9ff` and *On Panel* `#89dcff`.
  Hover **brightens** here (unusual for a light kit) because the label is dark ink: a lighter
  fill means *more* contrast with it, 5.83 → 7.01:1.
- `--accent-soft rgba(21,185,255,.14)` — a 14% tint of the accent, expressed as `rgba()`.
- `--text-on-surface-2-muted #7fbfda` — *On Panel* `#89dcff` desaturated toward the panel: same
  hue, one tier dimmer (10.2 → 7.7:1), for placeholders and secondary copy on the wells.
- `--cyber-angel-holo-ink #005e85` — the deep cut of the holo hue, the only accent value that is
  **ink** on a light surface (see the split below).
- Status `--ok #5fe3a1` and `--warn #ffc46b` — the file ships no success/warning colour, so the
  kit picks two that live only on the dark wells. Amber is deliberately browner than the file's
  reds so a warning can never read as an error, and mint sits next to the holo cyan rather than
  introducing a new brand hue.

## The two-tier ink system (the thing this file actually demands)

The frame has **two polarities**: light surfaces (`#E0E0E0`, ink *On Surface* `#292929`) and dark
panels (`#242424`, ink *On Panel* `#89dcff`). The kit therefore declares four text tokens, not
one — and this is not a shortcut, it is arithmetic:

```
one ink for --bg #d9d9d9 AND --surface-2 #242424 : best possible = 3.31:1 (grey #747474)
                                                   the floor is 4.55:1 → impossible
```

The same holds for the accent: `#15b9ff` is a **holo fill** (1.58:1 as text on the light ground,
5.83:1 as a fill under dark ink). No single cyan serves both roles, so the kit splits them —
`--accent` fills, `--cyber-angel-holo-ink` writes. In the frame, cyan on a light surface is likewise an
*outline or a fill*, never body text.

**`--text-dim` on `--surface-2` is therefore delegated, not skipped.** `--text-dim` meets the
4.55:1 floor on every ground it actually sits on (`--bg` 4.74, `--surface` 5.07); the design's
dark well is served by the contract's paired tokens — `--text-on-surface-2` (10.16:1) and
`--text-on-surface-2-muted` (7.66:1) — with `--text-dim` itself at 2.32:1 there, which is the
proof that one value cannot do both jobs.

## Contrast — measured, not eyeballed

Computed by a script that parses `tokens.css` (no hand-typed hexes) and composites every
`rgba()` tint over the ground it lands on.

| Contract pair | Foreground | Ground | Ratio | Target |
|---|---|---|---|---|
| body ink | `--text` `#292929` | `--bg` `#d9d9d9` | **10.31:1** | ≥ 7:1 ✓ |
| secondary ink | `--text-muted` `#444444` | `--surface` `#e0e0e0` | **7.38:1** | ≥ 4.5:1 ✓ |
| button label | `--text-invert` `#313131` | `--accent` `#15b9ff` | **5.83:1** | ≥ 4.5:1 ✓ |
| captions / hints | `--text-dim` `#5c5c5c` | `--bg` `#d9d9d9` | **4.74:1** | ≥ 4.55:1 ✓ |
| captions / hints | `--text-dim` `#5c5c5c` | `--surface` `#e0e0e0` | **5.07:1** | ≥ 4.55:1 ✓ |
| well inks (delegation) | `--text-on-surface-2` `#89dcff` | `--surface-2` `#242424` | **10.16:1** | ≥ 4.55:1 ✓ |
| well inks (delegation) | `--text-on-surface-2-muted` `#7fbfda` | `--surface-2` `#242424` | **7.66:1** | ≥ 4.55:1 ✓ |

Everything else the lab renders:

| Pair | Ratio |
|---|---|
| `--text` on `--surface` / masthead stop `--bg-2` | 11.02 / 11.02:1 |
| `--text-muted` on `--bg` | 6.90:1 |
| `--text-invert` on `--accent-hover` / `--accent-2` (avatar ramp) | 7.01 / 8.51:1 |
| `--cyber-angel-holo-ink` on `--bg` / `--surface` | 5.06 / 5.41:1 |
| `--cyber-angel-holo-ink` on the 14% `--accent-soft` tint over bg / surface | 4.66 / 4.95:1 |
| `--danger` on `--bg` / `--surface` (Delete button, invalid hint) | 4.74 / 5.07:1 |
| `--cyber-angel-danger-panel` on `--surface-2` (danger badge) | 7.31:1 |
| `--ok` / `--warn` / `--info` on `--surface-2` | 9.60 / 9.88 / 10.16:1 |
| `--focus-ring` on `--bg` (non-text UI needs 3:1) | 5.06:1 |
| `--accent-2` on `--surface-2` (focused input rim) | 10.16:1 |

The kit's previous build failed the annotation tier at **2.78:1**; the dim tier here is 4.74:1
and it was **not** bought by lightening the ground.

## The compatibility block in `tokens.css`

`tokens.css` ends with a four-part, colour-only block (`§1`–`§4`). It exists because the shared
lab was built for kits with **one** ink per polarity. Read it as a shim, not as styling:

- **§1 HALO INK** — eight lab consumers paint `var(--accent)` as *text* on a light ground
  (links, eyebrow, secondary button, accent badge, active nav, active tab, table `code`, inline
  code). `#15b9ff` is 1.58:1 there, so they take `--cyber-angel-holo-ink` instead. The accent itself
  stays a holo fill.
- **§2 DARK WELLS** — the tiers the lab still paints on the dark Panel from a light-ground ink:
  `pre.code` (and its `.dim` spans), the elevated card's title/body, the `:hover` states of nav,
  table rows and the ghost button, and the toggle knob. Plus the danger tier: the lab uses one
  `--danger` for both a Delete button on the light ground *and* a badge on the dark panel, so the
  badge/alert/invalid-rim take `--cyber-angel-danger-panel`.
- **§3 CHAMFER KEEPER** — `clip-path` clips an element's `box-shadow` and `outline` along with
  its pixels. The file's holo halo and emboss drop are therefore re-expressed as `drop-shadow()`
  filters, which follow the clipped silhouette, and the input's focus ring (a box-shadow the
  chamfer would eat) becomes a holo border.
- **§4 CAP-SET DISPLAY** — Syncopate is set uppercase in the frame. The lab leaves
  `text-transform` alone, so the display face is set cap here.

**Delete a line the day the lab stops needing it.** §1 and the danger half of §2 are about the
accent being a fill and red existing in two tiers — those are permanent facts of this design. §2's
well tiers and §3 are things the lab can absorb: it already wires `--text-on-surface-2` into
inputs, badges and alerts, and the remaining consumers (`pre.code`, `card-elevated`, the hover
states, the toggle knob) are the same one-line change. Nothing in the block is layout.

## Signature tiles

Every extra in `tokens.css` is named `--cyber-angel-*`, because the lab's **Signature** section
renders any token whose name starts with the kit slug — alphabetically, up to eight, each painted
into a chip. All eight here are **paintable** (the fill ramp `--cyber-angel-holo`, the halo wash
`--cyber-angel-halo`, the halo ink `#15B9FF40`, the deep holo inks, the brand slash
`--cyber-angel-slash`, the canvas, the panel red). The file's non-paintable effects — the emboss
drop and the halo stack — are carried by `--shadow-1` / `--shadow-2` / `--glow` rather than
duplicated as extras that would render as empty chips.

## Chamfers — the known limitation

`clip-path` cuts the border along the diagonal, so a chamfered edge is **borderless**: a 45° black
rule cannot follow a 45° cut twice. The straight edges still carry the rule and the shape reads as
chamfered at thumbnail size. This is a documented property of the technique, not a bug.

Related, and also by construction: the transition between a light panel and a dark well happens
across a black rule, so no two polarities are ever asked to blend.

## Linter & build

```
npx -y -p @google/design.md designmd lint kits/cyber-angel/DESIGN.md
  → 0 errors, 0 warnings   (one token-summary info: 26 colours, 8 type scales, 39 components)

python tools/build.py --no-export --no-lint
  ▸ cyber-angel  (Cyber Angel)
    · optional: --clip, --text-on-surface, --text-on-surface-muted,
                --text-on-surface-2, --text-on-surface-2-muted
    ✓ lab html                      (no "token contract gaps")

node tools/verify-lab.cjs cyber-angel      (headless Chromium, 1280×900 + 390×844)
  → PASS — 0 errors, 0 warnings, 0 console errors
    0 missing tokens, 0 fallback tokens, no horizontal overflow
    fonts loaded: Syncopate (1 face), Nova Flat (1 face), Montserrat (3 faces)
    computed: body bg rgb(217,217,217), card bg rgb(224,224,224), accent #15b9ff
```

0 component sub-tokens outside the whitelist (`backgroundColor`, `textColor`, `typography`,
`rounded`, `padding`, `size`, `height`, `width`) — the shadows, borders, chamfer and halo ramps
live in `tokens.css` and in prose, and no gradient appears in `colors:`.

## Trade-offs and deviations

- **`--bg-2` is `#E0E0E0`, not the file's `#2E2F30`.** `--bg-2` is the masthead's top gradient
  stop. Putting the dark canvas there drags the tagline down the ramp to ~5.4:1 and the
  caption/meta tier to ~2.5:1 — the exact washed-out annotation failure this kit was rebuilt to
  fix. `#E0E0E0` (the file's *Surface*) makes the header lit from above instead, and the dark
  canvas survives as the modal scrim (`--overlay`) and as `--cyber-angel-canvas`.
- **Two reds, two inks.** Documented above: the file colours semantics for the dark panel and no
  light ground can carry `#ff948f`. Splitting red is the honest translation.
- **Nova Flat is not monospaced.** It sits in the contract's `--font-mono` slot because that slot
  is the lab's *UI-chrome* voice (labels, badges, placeholders, captions) and Nova Flat is the
  file's input/subhead face. The fallback chain stays monospace, so code degrades sanely if the
  webfont never arrives. Montserrat takes body; Syncopate takes display.
- **Syncopate's uppercase is set in `tokens.css`, not `DESIGN.md`.** `textTransform` is not in the
  linter's typography vocabulary (it would be dropped by the exports with a `broken-ref` warning),
  and it is a property of how this face is set rather than a token.
- **The disabled state keeps the file's values** (`#606060` / `#ffffff`) but does not assign them
  to a contrast-checked component: `#606060` on `#d9d9d9` is 4.45:1, an honest disabled tone that
  is deliberately below the body-text floor. Disabled text is the one thing that *should* look
  unavailable.
- **`--border` and `--border-strong` are the same black** because the file has exactly one border
  colour. A softer second grey would have been an invention, and it would have softened the rule
  that carries the design.

## When to use

Bright, confident, technological work: product launches, AI and vision pages, instruments and
dashboards that want to look engineered, brand pages that want light without pastel. Avoid it
where surfaces must be soft, translucent or quiet — that is `glass` for frost and `carbon` for
night.
