---
version: alpha
name: Sunset Boulevard
description: An instrument deck standing on a drawn city floor at midnight — violet hairline frame, 16px cut corners, an opaque indigo face carrying a perspective grid anchored to its own floor, and one amber sun in the scene.
colors:
  primary: "#B06CFF"
  primary-hover: "#C08BFF"
  on-primary: "#12081F"
  primary-soft: "rgba(176, 108, 255, 0.16)"
  secondary: "#FFB84D"
  tertiary: "#CFA4FF"
  neutral: "#0A0512"
  scene: "#231040"
  scene-floor: "#040208"
  surface: "#150C28"
  surface-2: "#120B1C"
  surface-solid: "#0F0819"
  text: "#F2EBFF"
  text-muted: "#C9B8E6"
  text-dim: "#AE9CCB"
  ok: "#45E0B0"
  warn: "#FFB84D"
  danger: "#FF5C7A"
  info: "#66D9FF"
  border: "rgba(255, 255, 255, 0.14)"
  border-strong: "rgba(176, 108, 255, 0.60)"

typography:
  display:
    fontFamily: "Chakra Petch"
    fontSize: "2.7rem"
    fontWeight: 700
    lineHeight: 1.04
    letterSpacing: "0.004em"
  h1:
    fontFamily: "Chakra Petch"
    fontSize: "1.75rem"
    fontWeight: 600
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
    fontWeight: 500
    lineHeight: 1.2
  label:
    fontFamily: "JetBrains Mono"
    fontSize: "0.72rem"
    fontWeight: 500
    letterSpacing: "0.14em"

rounded:
  sm: "0px"
  md: "0px"
  lg: "0px"
  pill: "2px"
  cut: "16px"

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
    backgroundColor: "{colors.tertiary}"
    rounded: "{rounded.sm}"
  chart-2:
    backgroundColor: "{colors.secondary}"
    rounded: "{rounded.sm}"
  chart-3:
    backgroundColor: "{colors.ok}"
    rounded: "{rounded.sm}"
  divider:
    backgroundColor: "{colors.border}"
    height: "1px"
---

# Sunset Boulevard

**An instrument deck on a city floor at midnight.** A violet-framed slab of opaque indigo, corners
cut at 18px, its face carrying a perspective grid that is anchored to its own bottom edge — the same
grid the page stands on, at twice the pitch and half the alpha. The only warm object in the kit is
the amber sun in the scene: `{colors.secondary}`, and never a wash behind text.

## Overview

This is one room of `Li//OS`, not a poster of a decade. The desk's grammar is fixed — a hairline
frame, an opaque face carrying a sheen band, a bottom occlusion band, a 157° face fall, a 5% accent
tint, one drawn texture, one accent hue — and what this place owns inside that grammar is the
**floor**.

- **The ground is a plane, not a backdrop.** Two soft fields of `{colors.scene}` over
  `{colors.neutral}`, a 120px technical grid, and the place's own perspective motif stretched across
  it, settling into `{colors.scene-floor}`. It recedes, so the page reads as somewhere rather than as
  a colour.
- **The card is a slab of that plane.** `{colors.surface}` is the desk's `.card-in` ported to tokens:
  sheen with a 1px specular lip, a bottom occlusion band, the same perspective grid at the card's own
  pitch with its horizon at 62% of the card's height, a 1px violet identity edge along the floor, a 5%
  tint, and a 157° fall. The grid lands on the card's floor, which is what makes the slab sit on the
  scene instead of floating in front of it.
- **The frame is cut, and it keeps its frame.** `--cut: 16px` with the family's `--clip`; because
  `clip-path` removes the border along the diagonal, `build.py` derives `--frame-ring` from that
  polygon and the 1px frame survives every edge.
- **One accent, one counterpoint.** Violet is the action. Amber is the scene's sun — it is also the
  warning status, and it is deliberately never a control.

## Colors

`{colors.primary}` `#B06CFF` is the place's own system violet: primary plates, links, active nav, the
focus ring, the identity edge along a card's floor. It is a **mid-light** fill, so `{colors.on-primary}`
`#12081F` carries its labels at 6.0:1 rather than white.

`{colors.tertiary}` `#CFA4FF` is the same violet re-tuned for **text** (the desk's `--accHi`): small
labels, eyebrows, links, badge labels and secondary-button labels route through it, because a fill
colour used as a label is the failure this split exists to prevent.

`{colors.secondary}` `#FFB84D` is the amber sun — the media plate, the second stop in charts and the
progress ramp's warm end. It is also `{colors.warn}`: amber in this kit is a **status colour and a
scene colour, not an action colour**. Nothing the user clicks is amber.

The status ladder is mint / amber / hot pink-red / sky. `{colors.danger}` `#FF5C7A` is deliberately a
warm pink-red so it separates cleanly from a violet action; the one pair that is not separable by hue
is `--warn` against `--accent-2`, because they are the same amber by design.

`{colors.neutral}` `#0A0512` is the floor. `{colors.surface}` `#150C28` is the deck's face, one full
step lighter so a card reads as lifted off the ground by value before it reads as lifted by anything
else.

## Typography

Chakra Petch for both display and body — a squared technical face, which is what an instrument deck
is lettered in — and JetBrains Mono for labels, keys and readouts. Labels are uppercase mono at
`{typography.label}` with `{typography.label.letterSpacing}`.

The pairing is **shared by every place in the family**, on purpose: these kits are rooms in one
operating system, and the type is the operating system. A later session should not "improve" it per
kit — change it in all of them or in none.

## Layout

The floor is percentage-sized, never px, so the scene lands the same in a 118px gallery tile as in a
full page. A 12-column feel with generous vertical rhythm (`{spacing.lg}` between sections,
`{spacing.xl}` for hero pacing). Cards are cut slabs with a 1px frame and a 9% sheen band: their
material is the face, and the grid inside them is anchored to the card's bottom edge, so a tall card
shows more floor and a short one shows the horizon.

Two scales do two jobs. The card's grid is the place's own pitch with its floor at 62% of the card's
height; the ground's is the same motif at half the alpha and twice the pitch. Equal weight would make
the page one busy field and every card read as texture inside texture.

## Elevation & Depth

Depth is **cast, not blurred**. Every surface here is opaque, so `--blur: none` — the desk forbids
glass and `backdrop-filter`, and a blurred opaque card is only a repaint cost. A card carries
`0 6px 16px rgba(0,0,0,.50)`; a nested or elevated one `0 10px 26px rgba(0,0,0,.55)`. `--glow` is the
desk's own bloom, `0 0 14px rgba(176,108,255,.32)`, and it is spent on the primary plate.

`clip-path` also clips a box-shadow, so a chamfered card's shadow stops at the silhouette. That is the
intended reading: the slab is cut out of the plane, not resting on top of it with a soft edge.

## Shapes

Cut, never rounded: `{rounded.sm}`/`{rounded.md}`/`{rounded.lg}` are 0, `--cut: 16px` taken on the
top-left and bottom-right corners (the desk's asymmetric chamfer), and
`--radius-pill` is `2px` so a pill-shaped badge still squares up. Native checkboxes and radios take
`--check-radius: 2px` for the same reason — a rounded control would be the one false note in the kit.
Because `clip-path` eats `outline` along the diagonal, keyboard focus is painted **inside** the
silhouette (`--focus-inset: 2px`) rather than outside it.

## Components

- **button-primary** — a solid `{colors.primary}` plate, `{colors.on-primary}` label, the desk's violet
  glow. The only filled, opaque thing on a page.
- **button-secondary** — transparent with a `{colors.border-strong}` hairline and a `{colors.tertiary}`
  label: an outlined plate on the floor, not a lit pane.
- **card** — the deck: sheen, occlusion, grid, identity edge, tint, fall, on `{colors.surface}`, 1px
  `{colors.border}` frame, cut corners.
- **card-elevated / input / badge / alert / code** — `{colors.surface-2}`, the nested tier: no texture,
  no identity edge, just a shallow sheen and half the tint on `{colors.surface-2}`. A 240px grid on a
  2.5rem control is clutter, not material.
- **badge** — mono, uppercase, 2px corners, cut; `badge-accent` takes the violet tint, the rest take a
  status hue with a tinted hairline.
- **avatar / progress** — the fill ramp: the accent at 25% into the accent itself.

## Do's and Don'ts

**Do**

- Keep the card's grid anchored to its bottom edge (62% height). It is the card's floor; floating it
  in the middle turns the deck into wallpaper.
- Use `{colors.tertiary}` for violet text and `{colors.primary}` for violet fills.
- Keep the frame at 1px. On a near-black ground a 2px line reads as printed, not as an instrument.
- Grade any new ink against the **composited** card (face + tint + fall + sheen), not against `{colors.neutral}`.

**Don't**

- Don't use the amber as an action colour. It is `{colors.warn}` as well as the sun; a clickable amber
  button is a button that reads as an error.
- Don't put the sun behind text, and don't turn it into a page-wide wash. It appears in the media
  plate and as the second stop of a chart, nowhere else.
- Don't round a corner, a chip or a checkbox.
- Don't set `--blur` — there is nothing here to see through.
- Don't add a third accent. Violet, amber and four status hues is already the room's whole palette.
