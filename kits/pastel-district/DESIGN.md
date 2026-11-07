---
version: alpha
name: Pastel District
description: A dreamy pink instrument panel — nine bokeh discs at 5% sitting behind hairline glass, on a deep plum ground, with one hairline of accent along the card's floor.
colors:
  primary: "#FF8FC4"
  primary-hover: "#FFA9D2"
  on-primary: "#2A0F1B"
  primary-soft: "rgba(255, 143, 196, 0.18)"
  secondary: "#6EE7B0"
  tertiary: "#FFB9DB"
  neutral: "#160C13"
  scene: "#43223B"
  scene-floor: "#12090F"
  surface: "#23141D"
  surface-2: "#1E121A"
  surface-flat: "#23141D"
  text: "#F8EFF3"
  text-muted: "#DCC5D0"
  text-dim: "#B79EAC"
  ok: "#6EE7B0"
  warn: "#FFC46B"
  danger: "#FF7086"
  info: "#C9A8FF"
  border: "rgba(255, 255, 255, 0.14)"
  border-strong: "rgba(255, 143, 196, 0.60)"

typography:
  display:
    fontFamily: "Chakra Petch"
    fontSize: "2.6rem"
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: "0.004em"
  h1:
    fontFamily: "Chakra Petch"
    fontSize: "1.7rem"
    fontWeight: 700
    lineHeight: 1.15
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
  sm: "4px"
  md: "6px"
  lg: "8px"
  pill: "999px"

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
  card-flat:
    backgroundColor: "{colors.surface-flat}"
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
    backgroundColor: "{colors.tertiary}"
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
  section-rule:
    backgroundColor: "{colors.border-strong}"
    height: "1px"
---

# Pastel District

**A dreamy pink instrument panel — bokeh light behind hairline glass.** Place 05 of the Li//OS
desk family, and the only warm-soft place in it. The grammar is the family's and is unchanged: a
1px frame, an opaque `{colors.surface}` face, a sheen band along its top edge, an occlusion band
along its floor, a 157° fall, a 5% tint of the accent, one drawn motif at 5%, and a hairline of
accent running along the card's bottom edge.

## Overview

Every other place in this family is a machined plate: a chamfer or a square corner, a lattice or
an engraving cut into the face, a cold hue. Pastel District is the same instrument with a different
**subject** — the object behind the glass is not a grid, it is nine discs of light that have gone
out of focus. Three decisions follow from that and nothing else does:

- **The card is a pane over a bloom, not a faceplate.** The nine discs sit *inside* the material,
  behind the tint and under the sheen, so they read as something behind the surface rather than a
  pattern printed on it. That is also why they are the only motif in the family that is not tiled:
  bokeh has no pitch to repeat at, so one stack of nine fills any box and every card gets its own
  constellation.
- **The frame stays one pixel.** A hairline is what makes a bloom look like it is behind
  something. A heavier border turns the glass into a lid.
- **The geometry is round and small.** `{rounded.sm}` / `{rounded.md}` / `{rounded.lg}` are 4 / 6 /
  8px — the desk's own `--rad: 6px`, stepped — with no `--clip` and no `--cut`. A chamfer is a
  cut, and nothing in this place is cut.

The one thing the kit does *not* add is a glow the desk does not have. Depth here is the desk's
own drop shadow; the light is the bloom already in the ground and in the nine discs, and the accent
appears as a 14px bloom at 30% only where the desk put it (a primary button).

## Colors

`{colors.primary}` is the place's `#FF8FC4` — the action colour, a primary button, a link, an
active nav item. It is a **light fill**, so `{colors.on-primary}` is the dark plum ink `#2A0F1B`
at 8.4:1, not white.

`{colors.tertiary}` is the same pink reserved for **text**: the desk already solved "accent as a
label" with its own `--accHi`, so small type takes `#FFB9DB` (7.6:1 on the pane) rather than the
fill colour. `{colors.primary-soft}` is an 18% tint of the accent, used for accent badges, the
active nav item and the secondary button's hover.

`{colors.secondary}` is the pale mint in the place's own scene, and it does the counterpoint's job:
the media plate, a chart series, the mint glint arriving in one corner. It is never an action
colour and it never carries small text on anything lighter than `{colors.surface-2}`.

`{colors.neutral}` is the ground. `{colors.scene}` is the plum field that sits over it and
`{colors.scene-floor}` is what the ground ramps to at its base — all three are the place's own
values and none of them is a preference.

The status ladder is **derived**, because the desk has one alert red and no ladder: mint
`{colors.ok}`, amber `{colors.warn}`, red `{colors.danger}`, pale violet `{colors.info}`. See the
note on `{colors.danger}` below — it is the one pair in this kit that needed judgement.

### Measured

Graded against the **composited** pane (the lightest pixel in a card's text band: 157° fall + 5%
tint + a bokeh disc, `#43313B`), against the lightest pixel of the ground (`#43223B`), and against
the nested tier's own composite (`rgb(41,25,35)`) — never against the declared
`{colors.surface}`:

| ink | on the pane (lit) | on the ground | on `surface-2` |
|---|---|---|---|
| `{colors.text}` `#F8EFF3` | **10.7:1** | 12.2:1 | 14.8:1 |
| `{colors.text-muted}` `#DCC5D0` | **7.4:1** | 8.5:1 | 10.3:1 |
| `{colors.text-dim}` `#B79EAC` | **4.9:1** | 5.6:1 | 6.8:1 |
| `{colors.tertiary}` `#FFB9DB` | 7.6:1 | 8.6:1 | 7.5:1 on the accent badge |

`{colors.on-primary}` on `{colors.primary}` is 8.4:1, and 10.0:1 on the hover fill.

## Typography

Chakra Petch for both voices and JetBrains Mono for labels — the family's pairing, shared by all
six places, because these are six rooms in one operating system and the type is the OS. Labels are
uppercase mono at `{typography.label}` with `.14em` tracking: an instrument that names its own
channels, not a poster.

The pairing costs a little softness. Chakra Petch is a squared technical face and a stricter
reading of "dreamy" would reach for something rounder; the family's argument is that the *place*
supplies the register and the OS supplies the voice, and a kit that changed the type would stop
being a room in the same building. Use the weight and the tracking for warmth, not a third family.

## Layout

The page is a lit surface, so the ground is never blank: two soft fields of the place's plum over a
120px technical grid, the nine discs at half their card alpha, and a ramp into
`{colors.scene-floor}` at the base. All of it is sized in **%**, never px — the gallery renders
`--bg` into a ~118px tile, and a px-anchored scene would show that tile its top edge only.

The cards sit on that field with the accent hairline along their floor, and the layout should leave
room under a card for it: the identity edge is at the very bottom inside the 9% occlusion band, and
a card with a negative margin or a clipped overflow loses it.

## Elevation & Depth

Depth is an **occlusion**, not a light. `--shadow-1` is the desk's `0 6px 16px rgba(0,0,0,.50)` and
`--shadow-2` its well shadow at `.55`; the card is already lit from behind, so the shadow's job is
to say the pane is in front of the bloom. `--glow` is the desk's own 14px accent bloom at 30%, and
it appears on a primary button only.

`--blur: none`. Every surface in this kit is opaque — the material's last layer is the face itself
— and a blurred opaque card is a repaint cost pretending to be glass. The translucency the kit has
is *inside* the material (the 5% tint over the discs), which no `backdrop-filter` can produce.

The sheen is the top 9% of the card and the occlusion its bottom 9%, both with the desk's own
stops. They are what make the pane read as a sheet with an edge rather than a rounded rectangle.

## Shapes

4 / 6 / 8px and a 999px pill, `--cut: 0px`, no `--clip`. The desk's `--rad` is 6px and the steps
are small on purpose: at a 16px chamfer the nine discs would be cropped by the diagonal and the
bloom would read as a badge. Native checkboxes and radios take `{rounded.sm}` (`--check-radius`),
because a squared control in this place is a different kit.

## Components

- **button-primary** — an opaque `{colors.primary}` plate with a `{colors.on-primary}` label and
  the `--glow` bloom. It is the only filled, opaque thing in the kit, and that is what keeps it
  separable from the mint `{colors.ok}` and the red `{colors.danger}`.
- **button-secondary** — transparent with a `{colors.tertiary}` label and a `{colors.border-strong}`
  hairline; hovering tints the plate with `{colors.primary-soft}`.
- **card** — the pane: sheen, occlusion, nine discs, identity edge, 5% tint, 157° fall, and the
  face. One token, `--pastel-district-pane`, because a fill plus a border is not this material.
- **card-elevated** — the nested tier on `{colors.surface-2}`: no discs and no identity edge, a
  shallow sheen and half the tint.
- **input** — `{colors.surface-2}` at `{rounded.md}`, `{colors.border}` hairline, `{colors.text}`
  ink. Focus takes the accent hairline and a 3px `{colors.primary-soft}` ring.
- **badge** — mono, uppercase, pill. `badge-accent` carries the pink tint and the accent ink; the
  four status badges carry a status hue on `{colors.surface-2}`.
- **avatar / chart-1..3 / media** — where the two accents are allowed to appear as colour rather
  than as chrome.

## Do's and Don'ts

**Do**

- Keep the nine discs at the alpha they ship with. They are baked at the desk's own 5%; raising
  them "until they show" turns light out of focus into a dotted fill.
- Grade any new ink against the composited pane — the lightest pixel under a disc, not `#23141D`.
- Keep the frame at 1px and the radius at 6px. The softness is in the light, not in the geometry.
- Let the identity edge have its pixel: nothing should sit flush against the bottom of a card.

**Don't**

- Don't set `--blur` to anything but `none`. It would blur an opaque surface and cost a compositor
  layer for no visible change.
- Don't add a glow. The bloom is already behind the glass; a second one makes the card a light
  source and the kit a neon theme.
- Don't use `{colors.primary}` as small text. It is legal on the pane (5.7:1) but it reads as a
  pressed button, and the desk's own `{colors.tertiary}` buys 7.6:1 for the same hue.
- Don't swap the ground for a light one and call it a variant: the pink is graded against a deep
  plum, and `{colors.text-dim}` on a white page is 2.9:1.
- Don't put `{colors.danger}` next to `{colors.primary}` in the same control group without a label.
  They are 21° apart in hue and the red is only separable because it is darker and more saturated.
- Don't tile the motif. Bokeh that repeats is a pattern.
