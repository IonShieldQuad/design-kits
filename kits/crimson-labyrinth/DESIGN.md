---
version: alpha
name: Crimson Labyrinth
description: Chamfered oxblood plates carrying a sheen, a bottom occlusion, one 268px engraved rose, a crimson identity edge and a 157° face fall — on a crimson-tinted black velvet ground. The status ladder is inverted so that red never means danger beside a red action.
colors:
  primary: "#FF4D5E"
  primary-hover: "#FF6E7C"
  on-primary: "#160406"
  primary-soft: "rgba(255, 77, 94, 0.12)"
  secondary: "#D9A85E"
  tertiary: "#FF8D99"
  neutral: "#090305"
  surface: "#140A0C"
  surface-2: "#13080C"
  text: "#F2E6E4"
  text-muted: "#CFB6B6"
  text-dim: "#BCA2A4"
  ok: "#9BC7A8"
  warn: "#D9B36B"
  danger: "#FF7A45"
  info: "#9E8CC7"
  border: "rgba(255, 255, 255, 0.14)"
  border-strong: "rgba(255, 77, 94, 0.6)"

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
    typography: "{typography.button}"
  button-secondary:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.tertiary}"
    rounded: "{rounded.md}"
    padding: "0.58rem 1rem"
    typography: "{typography.button}"
  button-secondary-hover:
    backgroundColor: "{colors.primary-soft}"
    textColor: "{colors.tertiary}"
    rounded: "{rounded.md}"
    padding: "0.58rem 1rem"
    typography: "{typography.button}"
  button-ghost:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.text-muted}"
    rounded: "{rounded.md}"
    padding: "0.58rem 1rem"
    typography: "{typography.button}"
  button-danger:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.danger}"
    rounded: "{rounded.md}"
    padding: "0.58rem 1rem"
    typography: "{typography.button}"
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
    padding: "0.2rem 0.55rem"
    typography: "{typography.label}"
  badge-warn:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.warn}"
    rounded: "{rounded.pill}"
    padding: "0.2rem 0.55rem"
    typography: "{typography.label}"
  badge-danger:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.danger}"
    rounded: "{rounded.pill}"
    padding: "0.2rem 0.55rem"
    typography: "{typography.label}"
  badge-info:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.info}"
    rounded: "{rounded.pill}"
    padding: "0.2rem 0.55rem"
    typography: "{typography.label}"
  nav-item-active:
    backgroundColor: "{colors.primary-soft}"
    textColor: "{colors.tertiary}"
    rounded: "{rounded.sm}"
    padding: "0.4rem 0.75rem"
  alert-danger:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.danger}"
    rounded: "{rounded.md}"
    padding: "0.6rem 0.72rem"
  alert-warn:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.warn}"
    rounded: "{rounded.md}"
    padding: "0.6rem 0.72rem"
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
    backgroundColor: "{colors.ok}"
    rounded: "{rounded.sm}"
  divider:
    backgroundColor: "{colors.border}"
    height: "1px"
  divider-strong:
    backgroundColor: "{colors.border-strong}"
    height: "1px"
---

# Crimson Labyrinth

**A gothic ritual console.** Not a dark page with a red accent: an instrument panel in a vampire's
chamber. The plate is near-black oxblood, its frame is a 1px crimson hairline cut by a 12px octagon,
its face carries one engraved rose at 268px, and the only light is a sheen along the top edge and a
crimson identity line along the bottom. It is a place in the `Li//OS` desk — the same construction
five sibling places wear, warmed to a colour, a motif and a metal of its own.

## Overview

Every token here comes from place 06 of the user's own desk prototype. The kit exists to port one
**material** faithfully and one **inversion** honestly.

The material is the desk's `.card-in`, unchanged, and its layer order *is* the light model: a sheen
(with its 1px specular lip) over a bottom occlusion band, over the rose plate, over the crimson
identity edge, over a 5% crimson tint, over a 157° face fall, over `{colors.surface}`. Move the tint
under the face and the plate disappears; put the fall under the face and there is no fall.

The inversion is the status ladder. Crimson is the action — the only thing that acts — so crimson
cannot also mean danger. `{colors.danger}` is a hot orange, `{colors.warn}` brass, `{colors.ok}` a
desaturated sage, `{colors.info}` a muted violet. Nothing in the ladder is crimson, which is exactly
what keeps a filled crimson button from reading as an error chip.

That inversion is also the difference between this kit and its `gothic` sibling. `gothic` is
editorial velvet: plum, ivory, a rose *bloom drawing on a stem*, soft 5–16px curves, a serif display
face. This kit is an instrument console: oxblood, a *line engraving* of a rose as the plate's own
material, a hard 12px octagon with a 1px frame, and the family's squared technical face. One is a
novel cover; the other is the machine a vampire keeps its records in.

## Colors

`{colors.primary}` is the place's `--acc`, exactly as the desk declares it: `#FF4D5E`, a crimson at
the light end of the oxblood family, used for the hairline that emphasises, the identity edge at the
foot of every plate, and the one filled action. It is mid-light, so it takes a very dark ink —
`{colors.on-primary}` is `#160406`, the place's own black-wine, not white: white on this crimson is
3.24:1 and would be the obvious mistake.

`{colors.tertiary}` is the same crimson re-tuned for **text** (the desk's `--accHi`): the fill colour
is 5.29:1 on the brightest band a card shows and the ink is 8.23:1 on the ground, which is why every
label, eyebrow, link and active-nav item uses the ink and every plate uses the fill. `{colors.secondary}`
is brass `#D9A85E`, the place's own second hue from its cathedral scene — a counterpoint in the media
ramp and charts, never a second action.

`{colors.neutral}` is the ground floor `#090305`. Over it sit two soft fields of the place's own
`--sceneA` (`#2B0A12` at 66%, softened so a field reads as a field and not as a blob), a 120px
technical grid at 2.8% / 2.4% white, the 560px rose at 0.0468 white, and a floor ramp into
`#050203`. The stops are not colour keys here because no component wears them — `--bg` is one
layered value; see `tokens.css`. The ground is quiet
on purpose: a busy page makes every plate read as texture inside texture.

## Typography

Chakra Petch for display and body, JetBrains Mono for labels — the family's pairing, shared by all
six places and deliberately not varied. These are places in one operating system and the type *is*
the OS: a squared technical face with a cut counter, which is what makes a ritual palette read as an
instrument rather than as a book cover. JetBrains Mono is the voice that labels the channels, at
`{typography.label}` (12px floor) and `0.14em`.

The cost is real: a squared sans cannot do the calligraphic, romantic line that `gothic` gets from
Cormorant. That is the trade this family makes everywhere — the ornament is in the plate, the type
stays the machine's.

## Layout

The plate is the layout unit. 12px octagons cut all four corners (the
desk's diagonal, not a four-corner bevel), the frame is exactly 1px, and the identity edge runs
along the bottom from 7% to 62% of the width — off-centre by design, because an instrument's label
is not a centred ribbon.

A page is a stack of plates on the ground with `{spacing.lg}` between sections; cards sit in an
auto-fit grid at a 230px minimum. The rose plate is pinned to a card's right side (100% 20%, 268px)
so it is cropped by the plate rather than centred in it — the engraving should feel like it was
struck for the plate, not placed on it.

## Elevation & Depth

There is almost no elevation. `--shadow-1` and `--shadow-2` are the desk's own
`0 6px 16px` / `0 10px 26px` black falloffs, but a chamfered box clips its own outer shadow, so on
this kit they read as the plate's edge and not as a lift. Depth is instead carried by three things
that cannot be clipped:

1. **the frame ring**, derived by `tools/build.py` from `--clip` — the clip shape with an inset copy
   punched out, so the diagonal keeps its 1px border where a painted border would be cut away;
2. **the sheen**, a 1px `rgba(255,255,255,.30)` lip that falls to nothing across the top 9%;
3. **the occlusion band**, black at 46% across the bottom 9%, which is what makes the plate look
   seated in the panel rather than floating.

`--blur: none`, always. Every surface is opaque, the desk forbids glass, and a blurred opaque card is
a repaint cost with no visual return.

## Shapes

`0px` radii, a `2px` pill (badges are cut tags, not lozenges), a `2px` checkbox, and `--cut: 16px` on
the two diagonal corners. `--focus-inset: 2px` paints the keyboard ring *inside* the silhouette,
because `clip-path` eats an outline along the chamfer; the same clipping is why the ring is a
`::before` ring rather than a border.

## Components

`button-primary` is a flat crimson plate with dark ink and the desk's `0 0 14px` crimson bloom.
`button-secondary` is a hairline ghost with the crimson ink label — it is a label, so it uses
`{colors.tertiary}`, not the fill. `card` is the full plate material; `card-elevated` drops to the
nested tier, which is the same oxblood at half the tint with no engraving, because a 268px rose on a
2.5rem control is clutter. `input` is that nested tier with a 1px hairline; `badge-accent` is a 12%
crimson tint under the crimson ink. `badge-danger` is the hot orange, never a red — see below.

## Do's and Don'ts

- **Do** keep the plate's layer order. Sheen, occlusion, rose, identity edge, tint, fall, face. It is
  the light model, not a list of decorations.
- **Do** let crimson be the only thing that acts, and let every state be a non-crimson hue. The
  ladder is inverted on purpose.
- **Do** keep the frame at 1px. Separation comes from the hairline, the sheen and the derived ring.
- **Do** leave the rose at 268px on a card and 560px on the ground, pinned right. It is one plate,
  not a pattern.
- **Don't** put white on the crimson fill. `#160406` is the ink; white is 3.24:1.
- **Don't** add rounding. The only curved thing in a plate is the engraving.
- **Don't** brighten the ground to make the rose read. The engraving is legitimately quiet; that is
  what makes it a plate rather than a wallpaper.
- **Don't** reuse crimson for danger, error or delete. That is the one failure this kit's whole
  status ladder exists to prevent.
- **Don't** ship this with a second display face. The type is the OS, and the OS is shared.
