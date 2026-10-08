---
version: alpha
name: Psychedelic
description: A 1960s acid poster printed on paper — a warped banded plate, five clashing screen-print inks, thick off-key outlines and a fat rounded display face.
colors:
  primary: "#ff6a00"
  secondary: "#5b1a8f"
  tertiary: "#e5198f"
  neutral: "#f6ecd8"
  ink-acid: "#a8d400"
  ink-yellow: "#ffd21e"
  ink-edge: "#961478"
  bg-stop-1: "#fdfaf1"
  bg-stop-2: "#f8f1e0"
  bg-stop-3: "#f6ecd8"
  bg-stop-4: "#fbf6e9"
  bg-2: "#f8f1e0"
  surface: "#fefcf4"
  surface-2: "#f4ecd9"
  overlay: "rgba(42,10,62,0.55)"
  text: "#2a0a3e"
  text-muted: "#5c2570"
  text-dim: "#6d457e"
  text-invert: "#2a0a3e"
  accent-ink: "#943005"
  accent-ink-hover: "#8c2d03"
  accent-hover: "#e85d00"
  accent-soft: "rgba(255,106,0,0.16)"
  ok: "#0d6f4c"
  warn: "#8a5500"
  danger: "#b81f24"
  info: "#2a63a3"
  border: "rgba(150,20,120,0.46)"
  border-strong: "rgba(150,20,120,0.78)"
  focus-ring: "#5b1a8f"
typography:
  display:
    fontFamily: "Bowlby One"
    fontSize: "2.75rem"
    fontWeight: 400
    lineHeight: 1.06
    letterSpacing: "0.01em"
  heading:
    fontFamily: "Bowlby One"
    fontSize: "1.3rem"
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: "0.01em"
  body:
    fontFamily: "DM Sans"
    fontSize: "0.95rem"
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: "Space Mono"
    fontSize: "0.72rem"
    fontWeight: 400
    letterSpacing: "0.14em"
  code:
    fontFamily: "Space Mono"
    fontSize: "0.8rem"
    lineHeight: 1.6
rounded:
  sm: "8px"
  md: "14px"
  lg: "22px"
  pill: "999px"
spacing:
  xs: "0.4rem"
  sm: "0.75rem"
  md: "1rem"
  lg: "2.25rem"
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.text-invert}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: "0.58rem 1rem"
    height: "2.6rem"
  button-primary-hover:
    backgroundColor: "{colors.accent-hover}"
    textColor: "{colors.text-invert}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.accent-ink}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: "0.58rem 1rem"
  button-secondary-hover:
    backgroundColor: "{colors.accent-soft}"
    textColor: "{colors.accent-ink-hover}"
    rounded: "{rounded.md}"
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.lg}"
    padding: "1.15rem"
  card-elevated:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text}"
    rounded: "{rounded.lg}"
  input:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: "0.6rem 0.72rem"
    height: "2.5rem"
  input-focus:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.md}"
  badge:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text-muted}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "0.2rem 0.55rem"
  badge-accent:
    backgroundColor: "{colors.accent-soft}"
    textColor: "{colors.accent-ink}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
  badge-ok:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.ok}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
  badge-warn:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.warn}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
  badge-danger:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.danger}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
---

# Psychedelic

A 1960s acid poster, rebuilt as a working UI kit. **The ground is a paper plate, and the
page is the poster**: a hard-banded ripple of overprinted screen tints, then a 3px halftone
grain, then warm off-white paper. Every colour is an *ink* laid on top — acid green, hot
orange, magenta, deep purple and a sparing yellow. The period-correct construction is the
reason the kit works at all: a screen print starts with paper, and a fully saturated page is
a poster nobody can read past a headline.

## Overview

Three things carry the era, and none of them is a smooth gradient:

1. **The page is the poster.** `--bg` is a layered plate, not a flat beige: a 3px
   `repeating-conic-gradient` **halftone grain**, over `--psychedelic-warp` — a
   `repeating-radial-gradient` ripple whose bands are **hard-stopped** (two stops at one
   position, zero gap), centred off the plate's top-left so the bands land as warped arcs —
   over a px-stop aged-paper ramp (`#fdfaf1` → `#f6ecd8` → `#fbf6e9`). Yellow and acid green
   **carry the field at strength**; magenta, orange and purple arrive as **thin overprint
   rings** in the paper gaps. That split is not decoration — it is the only way a light
   plate can hold five inks *and* keep plum type legible; see Colors.
2. **Clashing saturated inks, five of them, with three jobs.** Hot orange
   `#ff6a00` (`--accent`) drives the **one** primary action. Deep purple `#5b1a8f`
   (`--accent-2`) is the **cool counterweight** — media gradients, bars, the focus ring,
   the cool end of every ramp. Acid green `#a8d400`, magenta `#e5198f` and yellow
   `#ffd21e` are **graphic** inks: they live in the ground field, the patterns and the
   printed edge. Acid green (1.4:1 on paper) and yellow (1.2:1) never carry text; magenta
   is 3.5:1 as type so it does not either.
3. **Organic and warped, never geometric.** No chamfer (`--cut: 0px`), no grid, no mirror.
   The liquid comes from generous pooled radii (8 / 14 / 22px), thick saturated outlines
   that are deliberately *off-key*, and three pattern extras: a **warp** (the banded
   ground ripple), a **halftone** (a 3px dot screen) and a **burst** (the full-strength
   five-ink sunburst that lives in the graphics, never under type).

The shadows are printed, not lit: the primary button carries the whole poster behind it as
two hard offsets, magenta then yellow (`--glow: 2px 2px 0 #e5198f, 4px 4px 0 #ffd21e`) — two
plates printed out of register. That misregistration, not a neon bloom, is the kit's depth.

It is a **light** kit: mode `light`, one deep plum ink `#2a0a3e`, and the printed plate is
the ground.

## Colors

The plate supplies the colour, the inks sit on it, and the inks are graded against the
**darkest band the ground can produce** (the purple overprint ring over `#f6ecd8`, the
palest paper stop), not against an average.

| Role | Token | Value | Contrast |
|---|---|---|---|
| Plate (palest stop) | `--bg` | `#fdfaf1` | — |
| Plate (darkest stop) | `--bg` | `#f6ecd8` | worst case for plum ink |
| Card | `--surface` | `#fefcf4` | — |
| Nested / input | `--surface-2` | `#f4ecd9` | — |
| Body ink | `--text` | `#2a0a3e` | **14.78:1** on the plate stop; **11.13:1** worst band |
| Secondary ink | `--text-muted` | `#5c2570` | **10.46:1** on `--surface`; 6.90:1 worst band |
| Tertiary ink | `--text-dim` | `#6d457e` | **6.39 / 6.37:1** on plate / surface-2; 4.81:1 worst band |
| On-orange ink | `--text-invert` | `#2a0a3e` | **6.04:1** on `--accent`, 4.95:1 on hover |
| Action | `--accent` | `#ff6a00` | hot orange |
| Action as text | `--accent-ink` | `#943005` | **6.67:1** on plate; **4.70:1** on its own tint over the worst band |
| Cool counterweight | `--accent-2` | `#5b1a8f` | deep purple |
| Graphic ink | `--psychedelic-ink-acid` | `#a8d400` | 1.4:1 — graphic only |
| Graphic ink | `--psychedelic-ink-magenta` | `#e5198f` | 3.5:1 — graphic only |
| Graphic ink | `--psychedelic-ink-yellow` | `#ffd21e` | 1.2:1 — sparingly, graphic only |
| Printed edge | `--psychedelic-ink-edge` | `#961478` | off-key outline ink |
| Focus | `--focus-ring` | `#5b1a8f` | **6.78:1** worst ground |

**The inks are laid as screen tints, and the tint level is a contrast decision.** On a light
plate the deep inks can only be printed at a few percent before they sink plum type below
4.5:1 — so **yellow (70%) and acid green (36%) carry the field at strength**, while
**magenta (12%), orange (18%) and purple (10%) sit as thin overprint rings**. The
full-strength clash is the graphics' job: the `--psychedelic-burst`, the `--media-bg`
panel and the masthead `--wash`. The readings above are the *composited* colour of each
band over the palest paper stop, and the tint levels were solved against the worst of them.

**`--bg` is a layered plate, checked band by band.** The darkest thing the plate can make is
a purple overprint ring over the `#f6ecd8` stop; the palest is a bare `#fdfaf1` stop. Every
value in the table is measured on the unluckiest band the relevant ink can land on.
`--bg-2: #f8f1e0` is the solid paper stand-in for exports.

**The pattern gradients are not in the `colors:` map above** — that block accepts CSS
colours only, and the linter errors on a gradient there. The raw inks ship as colours
(`ink-acid`, `ink-yellow`, `ink-edge`, plus `primary`/`secondary`/`tertiary` for
orange/purple/magenta) and the gradients themselves live in `tokens.css` as
`--psychedelic-warp`, `--psychedelic-halftone` and `--psychedelic-burst`.

**Ink is deep plum, and `--text-invert` equals `--text`.** White on `#ff6a00` is about
2.4:1. Plum on orange is 6.0:1 and reads exactly like screen-print ink on a warm plate, so
the kit puts dark ink on the accent rather than light. Do not "fix" this by lightening
`--text-invert` — the poster's ink block is a dark plate.

**Fill and text are different jobs, so orange has two tokens.** `#ff6a00` fills the primary
button (6.04:1 under plum) and is unreadable as a small label. The eyebrow, links,
secondary-button labels, active nav/tab, inline code and accent badges therefore read
`--accent-ink` `#943005` (6.67:1 on the plate, 5.70:1 on the purple ring, 4.70:1 even on
its own 16% tint composited over the worst band) with `--accent-ink-hover` `#8c2d03` for the
hover step — because `--accent-hover` `#e85d00` is a *fill* step and too light to read as
type. The bolder ground pushed this ink one shade deeper than the first cut of the kit; it
is still unmistakably burnt orange.

**Status never borrows a brand ink.** `--ok` `#0d6f4c` forest green (never the acid green),
`--warn` `#8a5500` brown-amber (never the orange action or the yellow), `--danger` `#b81f24`
true red (never the magenta), `--info` `#2a63a3` blue (the palette's one cold hue that is not
a brand ink). A failed state must never be mistakable for the orange primary.

## Typography

A three-face pairing where the contrast between the faces *is* the era:

- **Bowlby One** (display) — a heavy, bulbous, rounded display face: the fat Cooper-Black
  register of a hand-painted 1960s poster, in a single weight, so it reads as one loud
  painted word and can never be over-applied. `h1`–`h3`, card titles, the wordmark. Set at
  weight 400 — its only weight — and never tracked negative; the face is already wide.
- **DM Sans** (body) — a clean geometric-humanist sans, warm enough for paper and neutral
  enough that the display face is the only thing shouting. Body copy is never set in
  Bowlby One or Space Mono.
- **Space Mono** (labels) — eyebrows, badges, table headers, timestamps, code. A wonky,
  period-adjacent mono that is not the library's JetBrains/Mono default.

Display is barely tracked (`.01em`); mono labels are wide (`.14em`).

## Layout

The shared 1040px measure, 2.25rem between blocks, and a `0.4 / 0.75 / 1 / 2.25rem`
spacing scale. Density is medium: a poster needs air around the ink, so blocks breathe and
the 2px outlines have room to read as printed frames rather than as borders. The warped
ground is a *plate* under that text, so its bands are sized in px (58 / 74 / 96 / 140 /
152 / 174px, a ~205px repeat) to land inside the first viewport rather than below it — and
small enough that the motif also reads inside a 168×72 Signature tile.

## Elevation & Depth

Depth is print, not light.

- `--shadow-1` — cards: a barely-there plum drop plus a purple pool, wide and low-alpha.
  The 2px line is what makes a card a card; the shadow only lifts it off the paper.
- `--shadow-2` — elevated surfaces: a **hard 4px/4px offset** in 14% plum plus a wider
  **magenta pool**. The hard offset is the press registration cue, the pool is ink bleed.
- `--glow` — the primary button only: **two hard offsets**, `2px 2px 0` magenta and
  `4px 4px 0` yellow. The button is printed from three plates and two of them are out of
  register; that is the kit's signature depth, and it is a shadow, not a bloom.
- `--blur: none` — matte paper, no glass anywhere.

## Shapes

Soft, pooled and rounded on the components — the opposite of the library's crisp printed
kits: `--radius-sm: 8px`, `--radius-md: 14px`, `--radius-lg: 22px`, pills on badges,
avatars and toggles. `--cut: 0px`: a chamfer is a straight geometric cut and geometry is
exactly what this kit is not. Where a sharper kit uses a notch, this one uses a pooled
corner.

The *ground* carries the shape language instead of the corners. It is a **warp, not a
grid**: `--psychedelic-warp` is concentric bands struck from a centre off the plate's
top-left, so every edge arrives as an arc and no two bands are parallel; the halftone grain
is a 3px dot screen, the imperceptibly small unit of print; and `--psychedelic-burst` is a
conic ray wheel — the one place the kit's geometry is radial rather than linear. Corners
round, the field warps: the two together are why the skin reads as hand-printed rather than
as a tidy UI on cream.

## Components

Every component colour resolves to a `{colors.*}` token; nothing is re-typed.

- **button-primary** — `{colors.primary}` orange fill, `{colors.text-invert}` plum label,
  14px radius, and the two-plate misregistration `--glow` (magenta + yellow hard offsets).
  The one solid orange object on a screen.
- **button-primary-hover** — `{colors.accent-hover}`, a deeper orange: the button presses
  into the ink, it does not lift out of it. `{colors.text-invert}` still clears 4.95:1.
- **button-secondary** — `{colors.surface}` paper on a saturated `{colors.border-strong}`
  edge with `{colors.accent-ink}` type; hover washes in the 16% `{colors.accent-soft}` and
  steps the label to `{colors.accent-ink-hover}`.
- **card** — `{colors.surface}` paper behind a 2px `{colors.border}` off-key edge at 22px.
  Elevated cards step to `{colors.surface-2}` and pick up the hard-offset `--shadow-2`.
- **input** — `{colors.surface-2}` deeper paper behind a 2px `{colors.border}` edge; focus
  swaps the border to `{colors.primary}` with a 3px `{colors.accent-soft}` ring, while the
  keyboard focus ring is `{colors.focus-ring}` deep purple so focus never looks like hover.
- **badge** — 2px `{colors.border}`, `{colors.text-muted}` mono caps;
  **badge-accent** is the orange tint under `{colors.accent-ink}`; **badge-ok/warn/danger**
  use the status inks.

## Do's and Don'ts

**Do**

- Keep the ground a **plate**: paper, hard-banded ink tints, a halftone grain. Ink on paper
  is the kit; a saturated `--bg` destroys the readability that lets five inks coexist.
- Keep every plate band **hard-stopped**. Two stops at one position, never a ramp — a
  smoothly fading ground is a colour wash, and this kit is a screen print.
- Use the pattern extras where a surface wants texture: `--psychedelic-burst` for a media
  panel or a hero field, `--psychedelic-warp` for a banded band of ground,
  `--psychedelic-halftone` as the printed dot screen. Full-strength inks go in the
  **graphics**, never under type.
- Keep `--border-w: 2px` and the off-key `--psychedelic-ink-edge` family. A neutral grey
  hairline turns this into a plain cream theme.
- Keep the display face single-weight and large. Bowlby One at 12px is mud.

**Don't**

- Don't put text on acid green, yellow or magenta. They are graphic inks: 1.4:1, 1.2:1 and
  3.5:1 on paper.
- Don't raise a dark ink's tint on the plate without re-measuring: magenta, orange and
  purple are capped at ring strength (12 / 18 / 10%) precisely so `--accent-ink` and
  `--text-dim` survive on the worst band.
- Don't use `#ff6a00` as type; use `{colors.accent-ink}`.
- Don't add a second orange or a second purple. One action colour, one counterweight.
- Don't add glass, blur, or a neon bloom. The depth is printed misregistration.
- Don't square the corners or add a chamfer — that is the geometric kit's language, not
  this one.
