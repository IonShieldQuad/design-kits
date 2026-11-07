---
version: alpha
name: Mainframe Access
description: A machine login rendered in phosphor green — a 4px scanline glass plate on a near-black ground, square corners, one hue, and a status ladder carried by value rather than by chroma.
colors:
  primary: "#54E08A"
  primary-hover: "#7FEFA9"
  on-primary: "#02120A"
  primary-soft: "rgba(84, 224, 138, 0.18)"
  secondary: "#FFC04D"
  tertiary: "#93F2B8"
  neutral: "#020704"
  surface: "#081A10"
  surface-2: "#071009"
  surface-solid: "#04100A"
  text: "#E6F7EA"
  text-muted: "#AECBB8"
  text-dim: "#A8C5B2"
  ok: "#93F2B8"
  warn: "#FFC04D"
  danger: "#FF6464"
  info: "#9AD9FF"
  border: "rgba(255, 255, 255, 0.14)"
  border-strong: "rgba(84, 224, 138, 0.60)"
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

**Phosphor-green terminal glass on a black grid.** A plate you look *into*: a 4px scanline at 5%
white lying over a 5% accent tint, a 1px specular lip along its top, a 46% occlusion band along
its floor, and a 157° fall between them. Square to the pixel, one hue, and a status ladder that is
almost entirely value rather than chroma. It is the only monochrome kit in the library.

## Overview

The register is a machine login: a room where the light comes from the screen and nothing else
emits. Every decision below follows from that one constraint.

- **The plate is the desk's `.card-in`, unchanged.** Sheen (with its 1px specular lip) over
  occlusion over texture over identity edge over tint over fall over the face. The order is the
  light model, not a stacking accident: a texture under the tint is invisible at 100% zoom, a fall
  under the face is not a fall.
- **The scanline is above the tint, at the desk's own pitch.** 1px row every 4px, 5% white — 25
  rows across a 100px card. Above the tint it is the brightest mark on the plate; below it, it is
  1px of white inside a green wash and disappears.
- **Two scales, deliberately different jobs.** The card runs 4px rows; the ground runs the same
  rows at 8px and 2.75%. Equal weight would make the page one busy field and every card read as
  texture inside texture.
- **Nothing is rounded and nothing is cut.** No chamfer (`--cut: 0`, no `--clip`), no radius (0 /
  0 / 0, pill 2px). The family's frame, sheen and occlusion do the work that a chamfer does in
  the sibling places: they separate a plate from its ground without a curve.
- **One hue.** Accent green is the only chroma in the interface; amber is the place's own second
  hue from its scene and appears only in warnings, chart stops and ramp ends. Everything else is
  value: black, white-alpha and the phosphor ladder.

## Colors

`{colors.primary}` is the place's `--acc`, `#54E08A`, used as a fill and never as a small label.
`{colors.tertiary}` is the desk's `--accHi`, `#93F2B8` — the same phosphor at the value where it
can be read as 12px type (13.14:1 on the mid plate, 8.74:1 on its own 18% tint). `{colors.on-primary}`
is a near-black green, because a light fill needs a dark ink: 11.35:1 on the accent, 13.55:1 on
its hover step.

Inks are graded against the **composited** plate, not against the face colour:

| band on a card | composites to | `{colors.text}` | `{colors.text-muted}` | `{colors.text-dim}` |
|---|---|---|---|---|
| lightest band a glyph can occupy (12% fall + 5% tint + scanline row + 4.8% sheen tail) | `#394940` | 8.56:1 | 5.46:1 | 5.13:1 |
| mid plate | `#0B1C13` | 15.84:1 | 10.11:1 | — |
| floor (52% fall + 46% occlusion) | `#09150F` | 16.70:1 | 10.66:1 | — |
| `--surface-2` (panel + 2.5% tint + 6% sheen) | `#18231B` | 14.54:1 | 9.28:1 | 8.71:1 |
| page ground, lightest pixel (`{colors.grid}` at full) | `#072A19` | 13.92:1 | 8.89:1 | 8.34:1 |

The 1px specular lip at the very top of a plate composites to `#6E7973` (18.2% luminance) and takes
`{colors.text}` down to 4.06:1 — it is a 1px highlight, no glyph sits in it, and it is the price of
the sheen the whole family shares.

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
scanline at 8px. All of it is sized in percentages, so the scene survives being rendered into a
118px gallery tile rather than showing only its top edge.

Vertical rhythm is `{spacing.lg}` between sections and `{spacing.xl}` for hero pacing. Panels are
square and butt up against each other; there is no overlap composition here, because two opaque
plates at the same value stack into one plate.

## Elevation & Depth

Depth is **occlusion, not glow**. `--shadow-1` is the desk's own `0 6px 16px rgba(0,0,0,.50)` and
`--shadow-2` its `0 10px 26px rgba(0,0,0,.55)`; the only light a component throws is `--glow`
(`0 0 14px` at the accent's 34%), and only `.btn-primary` uses it. One emitter per page is what
keeps a terminal reading as a terminal.

Inside a single plate, the same idea runs at 1px scale: the top 9% carries the sheen (30% white on
its first pixel, 4.8% by 34%), the bottom 9% carries the occlusion (46% black on its first pixel,
13.8% by 38%). Those two bands are what make a flat fill read as glass over a panel.

## Shapes

`{rounded.sm}` and `{rounded.md}` and `{rounded.lg}` are all `0px`; `{rounded.pill}` is `2px`, which
is the least that removes the burr from a 0.85rem badge without introducing a curve. `--cut: 0px`
and no `--clip`: there is no frame ring to derive, because the frame is the rectangle's own hairline.

## Components

- **button-primary** — an opaque `{colors.primary}` plate with a `{colors.on-primary}` label and
  `--glow`. It is the only filled, opaque control in the kit, which is exactly how the action stays
  separable from `{colors.ok}`: the status is an outline chip with pale text, the action is a solid
  plate with dark text.
- **button-secondary** — transparent with `{colors.tertiary}` text and a 45% accent hairline; on
  hover it takes `{colors.primary-soft}` behind the same label (8.74:1 there).
- **card** — the plate: sheen, occlusion, 4px scanline, accent bottom edge, 5% tint, 157° fall.
- **card-elevated** — `{colors.surface-2}` and `--shadow-2`: the nested tier, no scanline.
- **input** — `{colors.surface-2}` with a recessed well (`inset 0 1px 0` black 55%, plus a 3.5%
  white inner keyline) and a `{colors.text}` value.
- **badge** — mono, uppercase, 2px; `badge-accent` is `{colors.tertiary}` on the accent tint, the
  status variants are outline chips in their own hue.
- **checkbox / radio** — a 1rem square: a `{colors.border-strong}` hairline on `{colors.surface-2}`
  when off, a solid `{colors.primary}` plate when on. The native control is drawn by the kit because
  a native radio paints a circle whatever the radius says.

## Do's and Don'ts

**Do**

- Grade any new ink against the composited plate. The face colour is not the ground a glyph sits on.
- Keep the scanline at 4px on components and 8px on the ground. The two pitches are what stop the
  page and the cards from fighting.
- Keep `--blur: none`. Every surface here is opaque, and a blur on an opaque card is a repaint cost.
- Reach for the sheen and the occlusion bands before reaching for a heavier border.

**Don't**

- Don't add a radius, a chamfer or a `--clip`. The square plate is the kit's one absolute rule.
- Don't use `{colors.primary}` as small text — use `{colors.tertiary}`, which is the same phosphor
  at a readable value.
- Don't add a second decorative hue. Amber is a status colour here, and `{colors.secondary}` is
  the ceiling.
- Don't lighten the ground to make the plate "pop". The plate is a 5% tint held above black; a
  lighter floor removes the only contrast it has.
