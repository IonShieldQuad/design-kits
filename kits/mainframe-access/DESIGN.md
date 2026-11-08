---
version: alpha
name: Mainframe Access
description: A machine login rendered in phosphor green — a black plate lit by a green hairline, a green halo and green 3px scanlines, no fill on the face, the ground's own slower rows behind it, a projected holo pane, square corners, one hue, and a status ladder carried by saturation and material rather than by chroma.
colors:
  primary: "#5CF79B"
  primary-hover: "#85FAB5"
  on-primary: "#02120A"
  primary-soft: "rgba(92, 247, 155, 0.18)"
  secondary: "#FFC04D"
  tertiary: "#BCF7CE"
  neutral: "#020704"
  surface: "#000000"
  surface-2: "#071009"
  surface-solid: "#000000"
  text: "#C8EED4"
  text-muted: "#93CFA4"
  text-dim: "#77AB89"
  ok: "#BCF7CE"
  warn: "#FFC04D"
  danger: "#FF7070"
  info: "#9AD9FF"
  border: "rgba(92, 247, 155, 0.32)"
  border-strong: "rgba(92, 247, 155, 0.52)"
  grid: "#072A19"
  scan: "#FFFFFF"

typography:
  display:
    fontFamily: "Chakra Petch"
    fontSize: "2.7rem"
    fontWeight: 700
    lineHeight: 1.02
    letterSpacing: "0.004em"
  h1:
    fontFamily: "Chakra Petch"
    fontSize: "1.75rem"
    fontWeight: 700
    lineHeight: 1.12
    letterSpacing: "0.004em"
  h2:
    fontFamily: "Chakra Petch"
    fontSize: "1.3rem"
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: "0.01em"
  body:
    fontFamily: "Chakra Petch"
    fontSize: "0.95rem"
    fontWeight: 400
    lineHeight: 1.62
  small:
    fontFamily: "Chakra Petch"
    fontSize: "0.8rem"
    fontWeight: 400
    lineHeight: 1.5
  button:
    fontFamily: "Chakra Petch"
    fontSize: "0.875rem"
    fontWeight: 600
    lineHeight: 1.2
  label:
    fontFamily: "JetBrains Mono"
    fontSize: "0.75rem"
    fontWeight: 500
    letterSpacing: "0.14em"

rounded:
  sm: "0px"
  md: "0px"
  lg: "0px"
  pill: "2px"

spacing:
  xs: "4px"
  sm: "8px"
  md: "16px"
  lg: "28px"
  xl: "44px"

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
    padding: "0.58rem 1rem"
    typography: "{typography.button}"
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
    padding: "0.58rem 1rem"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.tertiary}"
    rounded: "{rounded.md}"
    padding: "0.58rem 1rem"
  button-secondary-hover:
    backgroundColor: "{colors.primary-soft}"
    textColor: "{colors.tertiary}"
    rounded: "{rounded.md}"
    padding: "0.58rem 1rem"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.text-muted}"
    rounded: "{rounded.md}"
    padding: "0.58rem 1rem"
  card:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.lg}"
    padding: "1.15rem"
  card-elevated:
    backgroundColor: "{colors.surface-2}"
    rounded: "{rounded.lg}"
    padding: "1.15rem"
  input:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text}"
    rounded: "{rounded.md}"
    padding: "0.6rem 0.72rem"
    height: "2.5rem"
  badge:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text-muted}"
    rounded: "{rounded.pill}"
    padding: "0.2rem 0.55rem"
    typography: "{typography.label}"
  badge-accent:
    backgroundColor: "{colors.primary-soft}"
    textColor: "{colors.tertiary}"
    rounded: "{rounded.pill}"
    padding: "0.2rem 0.55rem"
    typography: "{typography.label}"
  badge-ok:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.ok}"
    rounded: "{rounded.pill}"
  badge-warn:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.warn}"
    rounded: "{rounded.pill}"
  badge-danger:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.danger}"
    rounded: "{rounded.pill}"
  badge-info:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.info}"
    rounded: "{rounded.pill}"
  nav-item-active:
    backgroundColor: "{colors.primary-soft}"
    textColor: "{colors.tertiary}"
    rounded: "{rounded.sm}"
    padding: "0.4rem 0.75rem"
  caption:
    textColor: "{colors.text-dim}"
  avatar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.pill}"
    size: "2.2rem"
  chart-1:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.sm}"
  chart-2:
    backgroundColor: "{colors.secondary}"
    rounded: "{rounded.sm}"
  chart-3:
    backgroundColor: "{colors.info}"
    rounded: "{rounded.sm}"
  divider:
    backgroundColor: "{colors.border}"
    height: "1px"
---

# Mainframe Access

**Phosphor green on a black plate that emits.** A machine login drawn as one black rectangle with
a green hairline, a green halo and green scanlines at a 3px pitch: no fill on the face, a 30px
pale-green sheen at its crown, a green ramp rising off the floor and one accent line beneath it. The
same rows run behind it on the ground at twice the pitch, and again inside a projected holo pane.
Square to the pixel, one hue, and a status ladder carried by saturation and material rather than by
chroma. It is the only monochrome kit in the library.

Every colour and construction below was **re-measured on the running page** (`getComputedStyle` on
the settled desk), not read out of the prototype stylesheet: for this place the stylesheet is the
pre-script state, and its accent, ink ramp, hairline and card face all disagree with what renders.

## Overview

The register is a machine login: a room where the light comes from the screen and nothing else
emits — except the plate itself, which is the family's one exception.

- **The plate is the desk's `.card-in` background stack, in the order the running page paints it.**
  A 30px pale-green sheen at the crown over a green-to-black ramp over the green scanline over the
  identity edge over a `#000000` face. The desk's 5% accent tint is applied at `0`, so the plate has
  **no fill**: everything you see on it is a band, a ramp or a row.
- **The motif is green, and it is at a 3px pitch.** 1px rows in 5.5% of `rgb(92,255,140)` across the
  whole plate. On a black face a white row reads as a CRT; a phosphor-green row reads as this place.
  It is the same pitch as the holo pane's scanlines and twice the ground's density.
- **The green lives in the depth as well as the face.** The desk's card throws
  `drop-shadow(0 0 8px rgba(92,247,155,.16))`, holds an inset bloom
  `rgba(92,247,155,.05) 0 0 30px` and a pale top lip `rgba(200,255,215,.22) 0 1px 0 inset`. All
  three are re-expressed in `--shadow-1` (a `box-shadow` can hold the two insets; a `filter`
  cannot), which is why this is the family's emissive member and not another occlusion-only plate.
- **Two kinds of surface, both shipped.** A *card* is built out of the plate; a *pane* is projected
  onto it — a 13% veil, one accent bloom at its crown, CRT scanlines and four 24px corner marks.
  The media panel is the pane (`--mainframe-access-holo`), and it is what separates a desk skin
  from a coloured rectangle.
- **Nothing is rounded and nothing is cut.** No chamfer (`--cut: 0`, no `--clip`), no radius (0 /
  0 / 0, pill 2px). The green hairline and the green halo do the work a chamfer does in the sibling
  places: they separate a plate from its ground without a curve.
- **One hue.** Accent green is the only chroma in the interface; amber is the place's own second
  hue from its scene and appears only in warnings, chart stops and ramp ends. Everything else is
  value: black, green-alpha and the phosphor ladder.

## Colors

`{colors.primary}` is the place's `--acc`, `#5CF79B`, used as a fill and never as a small label.
`{colors.tertiary}` is the desk's `--accHi`, `#BCF7CE` — the same phosphor at the value where it can
be read as 12px type (10.42:1 on its own 18% tint, 13.25:1 on `--surface-2`). The desk's `--acc2`,
`#C2FF8F`, is the accent-text *hover* step (`--accent-ink-hover`) — the pale member of the family,
never a second accent. `{colors.on-primary}` is a near-black green, because a light fill needs a
dark ink: 13.93:1 on the accent, 14.94:1 on its hover step.

The hairline is the accent, not white. `{colors.border}` is `rgba(92,247,155,.32)` and
`{colors.border-strong}` is `rgba(92,247,155,.52)` — both measured off the running frame.

Inks are graded against the **composited** plate, not against the face colour:

| ground a glyph can occupy | composites to | `{colors.text}` | `{colors.text-muted}` | `{colors.text-dim}` |
|---|---|---|---|---|
| lightest band on a card (a scanline row inside the 30px green sheen) | `#161F19` | 13.37:1 | 9.41:1 | 6.41:1 |
| the face, between rows | `#000000` | 16.64:1 | 11.70:1 | 7.97:1 |
| the floor (5% accent ramp under a scanline row) | `#050E08` | 15.51:1 | 10.91:1 | 7.43:1 |
| `--surface-2`, where the `.hd` band is strongest | `#1A2D20` | 11.55:1 | 8.13:1 | 5.53:1 |
| 18% accent tint over `--surface-2` | `#1E432B` | 8.79:1 | 6.18:1 | 4.21:1 |
| page ground, lightest pixel (`{colors.grid}` at full) | `#072A19` | 12.28:1 | 8.64:1 | 5.89:1 |

No glyph sits on the accent tint: that composite is the `badge-accent` / active-nav fill, and its
label is `{colors.tertiary}` at **9.16:1** there — which is why `{colors.text-dim}` can drop to
4.21:1 there without anything becoming unreadable.

The pale-green sheen is what keeps the card text-safe: it tops out at `#131714` on its own and
`#161F19` where a scanline row crosses it, so the brightest band on the plate is still 13:1 for
`{colors.text}`. A white sheen at the family's 30% would have composited to `#626262` and taken the
body ink to 4.8:1.

`{colors.text-dim}` is the one ink lifted off the measurement. The desk's `#6A9B7A` reads 3.96:1 on
an 18% accent tint over the place's panel (`#163A23`), under the 4.55 floor, so it takes a single
step along its own hue to `{colors.text-dim}` `#77AB89` — 4.79:1 there, 6.41:1 on the plate's
lightest band, 7.97:1 on the face.

`{colors.secondary}` amber is the desk's own amber-terminal sibling for this place: it is the same
value as `--warn`, on purpose. A monochrome kit has no budget for a second decorative hue.

## Typography

Chakra Petch for display and body, JetBrains Mono for every label, badge, key and code value. The
pairing is shared by all six places in this family and is deliberately unchanged: the type *is* the
OS, so a later session should not "fix" it per place. Chakra Petch is squared technical signage;
JetBrains Mono is the channel-naming voice, uppercase at `{typography.label}` with
`{typography.label.letterSpacing}`.

## Layout

The page is a console, so the ground is structured, not blank: two soft `{colors.grid}` fields (80%
× 60% at 63%/38%, and 120% × 70% at 14%/96%), a 120px technical grid at 2.8%/2.4% white, and the
scanline at 6px. All of it is sized in percentages, so the scene survives being rendered into a
118px gallery tile rather than showing only its top edge. The card runs the same rows at **3px**, so
the plate is twice as dense as the page it floats on.

Vertical rhythm is `{spacing.lg}` between sections and `{spacing.xl}` for hero pacing. Panels are
square and butt up against each other; there is no overlap composition here, because two black
plates at the same value stack into one plate.

## Elevation & Depth

Depth is **emission**. `--shadow-1` is the desk's own card depth, re-expressed as one box-shadow:

```
0 0 8px rgba(92,247,155,.16)          the green halo (the desk's drop-shadow)
inset 0 0 30px rgba(92,247,155,.05)   the green bloom inside the plate
inset 0 1px 0 rgba(200,255,215,.22)   the pale top lip
```

`--shadow-2` keeps the halo and adds the family's `0 10px 26px rgba(0,0,0,.55)` well shadow for the
nested tier. The only other light on the page is `--glow` (`0 0 14px` at the accent's 32%), and only
`.btn-primary` uses it. One emitter per control is what keeps a terminal reading as a terminal — this
kit spends its one exception on the plate, not on every chip.

Inside a single plate the same idea runs at band scale: the crown carries a 30px pale-green sheen
(9% of `rgba(210,255,222)` fading to nothing) and the plate's own ramp runs 5% accent at the floor to
34% black at the top, so the surface is lit from below by its scan and sinks away at its crown. There
is no separate occlusion band and no 157° fall in this place — the ramp is both.

## Shapes

`{rounded.sm}` and `{rounded.md}` and `{rounded.lg}` are all `0px`; `{rounded.pill}` is `2px`, which
is the least that removes the burr from a 0.85rem badge without introducing a curve. `--cut: 0px`
and no `--clip`: there is no frame ring to derive, because the frame is the rectangle's own hairline.

## Components

- **button-primary** — an opaque `{colors.primary}` plate with a `{colors.on-primary}` label and
  `--glow`. It is the only filled, opaque control in the kit, which is how the action stays
  separable from `{colors.ok}`: the status is an outline chip with pale text, the action is a solid
  plate with dark text.
- **button-secondary** — transparent with `{colors.tertiary}` text and a 52% accent hairline; on
  hover it takes `{colors.primary-soft}` behind the same label (10.42:1 there).
- **card** — the plate: a 30px pale-green sheen, the green-to-black ramp, the green 3px scanline, the
  accent bottom edge at 75%, a `#000000` face, and the green halo from `--shadow-1`. No tint.
- **card-elevated** — `{colors.surface-2}` and `--shadow-2`: the nested tier — the desk's `.hd` band
  (10% pale green falling to 55% black) over the panel and a 2.5% accent tint, with no scanline.
- **input** — `{colors.surface-2}` with a recessed well (`inset 0 1px 0` black 55%, plus a 3.5%
  white inner keyline) and a `{colors.text}` value.
- **card-media** — the holo pane: four 24px corner marks at 70% accent, 1px scanlines at a 3px
  pitch, a crown bloom at 5.5% and a 13% veil, at `--media-op: 1`. The desk's animated 180px sweep
  is not expressible as a background token and is not shipped (see the README).
- **badge** — mono, uppercase, 2px; `badge-accent` is `{colors.tertiary}` on the accent tint, the
  status variants are outline chips in their own hue.
- **checkbox / radio** — a 1rem square: a `{colors.border-strong}` hairline on `{colors.surface-2}`
  when off, a solid `{colors.primary}` plate when on. The native control is drawn by the kit because
  a native radio paints a circle whatever the radius says.

## Do's and Don'ts

**Do**

- Grade any new ink against the composited plate. The face colour is not the ground a glyph sits on.
- Keep the scanline off the card. It belongs to the ground (6px, 3.5%) and the holo pane (3px, 3%) —
  the desk renders the card's at zero, and adding one makes the plate a texture instead of a plate.
- Keep `--blur: none`. Every surface here is opaque, and a blur on an opaque card is a repaint cost.
- Reach for the sheen, the hairline and the halo before reaching for a heavier border.
- Use the holo pane for any projected, "on-screen" surface. It is the second half of the desk and the
  only place a second construction is allowed.

**Don't**

- Don't add a radius, a chamfer or a `--clip`. The square plate is the kit's one absolute rule.
- Don't fill the face. A tint on a `#000000` plate reads as a lighter plate, not as a lit one; the
  green belongs in the halo and the hairline.
- Don't use `{colors.primary}` as small text — use `{colors.tertiary}`, which is the same phosphor
  at a readable value.
- Don't add a second decorative hue. Amber is a status colour here, and `{colors.secondary}` is
  the ceiling.
- Don't lighten the ground to make the plate "pop". The plate is black on a near-black ground and
  the hairline is the only thing separating them.
