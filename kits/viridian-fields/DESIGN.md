---
version: alpha
name: Viridian Fields
description: A matte botanical console — a deep absorbed emerald as the only filled thing, one engraved fern struck at 248px in a card's bottom-right, a 1px frame and a 157° face fall. No bloom, no scanlines, no glow wash.
colors:
  primary: "#147A57"
  primary-hover: "#116B4C"
  on-primary: "#EAF6F0"
  primary-soft: "rgba(20, 122, 87, 0.22)"
  secondary: "#7FA9C8"
  tertiary: "#5BCBA0"
  neutral: "#0A1512"
  surface: "#0C1914"
  surface-2: "#1D2E29"
  text: "#EAF6F0"
  text-muted: "#B7CCC1"
  text-dim: "#A2B9AD"
  ok: "#6FCF97"
  warn: "#D9B36B"
  danger: "#EE7A70"
  info: "#7FA9B8"
  border: "rgba(255, 255, 255, 0.14)"
  border-strong: "rgba(20, 122, 87, 0.60)"
  bg-stop-1: "#16382B"
  bg-stop-2: "#0A1512"
  bg-stop-3: "#050B08"
  fern: "#FFFFFF"

typography:
  display:
    fontFamily: "Chakra Petch"
    fontSize: "2.7rem"
    fontWeight: 600
    lineHeight: 1.06
    letterSpacing: "0.004em"
  h1:
    fontFamily: "Chakra Petch"
    fontSize: "1.7rem"
    fontWeight: 600
    lineHeight: 1.14
    letterSpacing: "0.004em"
  h2:
    fontFamily: "Chakra Petch"
    fontSize: "1.28rem"
    fontWeight: 500
    lineHeight: 1.22
    letterSpacing: "0.008em"
  body:
    fontFamily: "Chakra Petch"
    fontSize: "0.95rem"
    fontWeight: 400
    lineHeight: 1.64
  small:
    fontFamily: "Chakra Petch"
    fontSize: "0.8rem"
    fontWeight: 400
    lineHeight: 1.52
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
  sm: "3px"
  md: "5px"
  lg: "7px"
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
  button-danger:
    backgroundColor: "transparent"
    textColor: "{colors.danger}"
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
  tab-item-active:
    backgroundColor: "transparent"
    textColor: "{colors.tertiary}"
    rounded: "0px"
  alert:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text}"
    rounded: "{rounded.md}"
    padding: "0.8rem 0.95rem"
  alert-danger:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text}"
    rounded: "{rounded.md}"
  code-block:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text}"
    rounded: "{rounded.md}"
    padding: "0.85rem 1rem"
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
    backgroundColor: "{colors.tertiary}"
    rounded: "{rounded.sm}"
  divider:
    backgroundColor: "{colors.border}"
    height: "1px"
---

# Viridian Fields

**A matte botanical console.** Deep emerald is the action, an engraved fern is the material, and
nothing on the page emits light. This is the one place in the Li//OS desk family that is *absorbed*
rather than *lit*: the accent is a dark green fill, the ink on it is the lightest thing in the kit,
and the only glow is the place's own 14px emerald at 26%, on the primary button.

## Overview

Every other dark kit in this library answers "how does it glow?" This one answers "what does a
surface look like when it has stopped reflecting?" Four decisions carry it:

- **The accent is dark, and it inverts the ink.** `{colors.primary}` is the place's own `--acc`,
  a deep emerald that is *darker* than the text around it. So ink on it is light
  (`{colors.on-primary}`) and the accent used as a label is its pale member `{colors.tertiary}`
  — the fill itself is 3.4:1 on a pane and cannot be a small label. Five of the six places in this
  family do the opposite; here it is deliberate and the numbers are in the README.
- **The material is a plate, not a gradient.** `{colors.surface}` is the desk's own `.card-in`:
  a sheen band with a 1px specular lip, a bottom occlusion band, the engraved fern, an emerald
  identity edge along the floor, a 5% tint, a 157° face fall, and the face. The fern is drawn once
  at 248px and pinned to the bottom-right — it is an engraving on a plate, not a pattern.
- **The frame is 1px and nothing behind it moves.** The page ground is two soft fields of
  `{colors.bg-stop-1}` over a 120px technical ruling, one 520px fern struck near the floor, and a
  ground-to-floor ramp. Large-celled and quiet, so the card's plate is legible as a plate.
- **Depth is occlusion.** `--shadow-1` and `--shadow-2` are black drops; `--blur: none` because
  every surface is opaque. Nothing in this kit is glass, and a blurred opaque card only costs a
  repaint.

## Colors

`{colors.primary}` is the desk's `--acc` (#147A57): a matte, absorbed emerald with 0.15 relative
luminance. It fills the primary button, the progress ramp and the avatar — the only opaque fills in
the kit. `{colors.tertiary}` (#5BCBA0, the desk's `--accHi`) is the same hue re-tuned for **text**:
eyebrows, links, active nav, secondary-button labels, `badge-accent`. It measures 9.0:1 on the flat
pane, 6.4:1 on a card's lit end and 5.9:1 over the brightest point of the scene field.

`{colors.secondary}` (#7FA9C8) is the place's own pale sky — the second hue, for gradients, media,
charts and the avatar's far stop. It is a fill colour and is never a label.

The status ladder is derived from the place, and the pair that needed care is `{colors.ok}` against
the accent: both are green, so `{colors.ok}` is held clearly lighter and mintier — 0.50 relative
luminance against the accent's 0.15, 2.8:1 apart — and a state chip is separated from the action by
*material* as well: a badge is an outlined chip, the action is an opaque plate.

`{colors.neutral}` is the floor the whole kit was graded against, and `{colors.bg-stop-1}` is the
lightest field on the page — the scene's own `--sceneA`. `{colors.fern}` documents the plate's
stroke colour (white, at the 9% the desk baked into its alpha); it is a drawn asset, not a tint.

## Typography

Chakra Petch for display and body, JetBrains Mono for labels, keys and metadata — the family's
fixed pairing, shared by all six places, because the type *is* the OS. Display weights stay at 500–600:
this register is printed on a plate rather than shouted off one, and a 700 weight at display size is
the quickest way to make a matte kit read as a loud one.

Labels are uppercase mono at `{typography.label}` (12px floor) with `{typography.label.letterSpacing}`
— the desk's instrument voice, narrow enough to sit inside a 3px chip radius.

## Layout

The page is a plate laid on a field: generous vertical rhythm (`{spacing.lg}` between sections,
`{spacing.xl}` for hero pacing), 1px rules, and a card radius of 5px so a plate reads as cut rather
than moulded. Nothing overlaps; the kit's depth comes from the drop under a plate, not from stacking
translucent layers.

The signature plate is anchored to the card's **bottom-right corner** (the desk's own
`right -42px bottom 10%`), so a card's engraving always reads as a mark struck into that corner
rather than as a centred illustration. On the ground the same engraving appears once at 520px near
the floor of the page — one plate, at roughly half the card's alpha. It does not repeat.

## Elevation & Depth

Two shadows, both black, both short: `0 6px 16px rgba(0,0,0,.50)` for a resting plate and
`0 10px 26px rgba(0,0,0,.55)` for one that floats. The single emanation is
`0 0 14px rgba(46,156,116,.26)` — the place's own glow, at the desk's own width, on the primary
button. Widening that blur, or lifting its alpha, is what would turn this kit into Mainframe Access.

## Shapes

`{rounded.sm}` 3px, `{rounded.md}` 5px, `{rounded.lg}` 7px, `{rounded.pill}` 999px. `--cut: 0px`
and no `--clip`: this place rounds, it does not chamfer. Buttons take the 5px radius, chips and small
controls 3px, and the native checkbox is squared to 3px with `--check-radius` so the shape language
holds on controls the browser draws itself.

## Components

- **Buttons.** The primary is an opaque emerald plate with a light label and the faint emerald glow;
  its hover goes *deeper* (#116B4C), because raising the fill's luminance drops the light label
  toward 3.9:1. Secondary and danger buttons are transparent with an accent-hairline rim and their
  colour in the label. The press travels *down* (`--btn-press: 0px` against a −1px hover) so the key
  seats into the plate — the only motion in the kit, linear and .18s.
- **Cards.** `{colors.surface}` is the plate material; `card-elevated` drops to `{colors.surface-2}`
  — the nested tier, which drops the engraving and the identity edge and keeps a shallow sheen plus
  half the tint.
- **Inputs.** A shallow recess with a lit lower lip (`--input-inset`), a rim of
  `{colors.border-strong}` — the desk's accent hairline at 60% — and `{colors.surface-2}` as its
  field.
- **Badges.** Pills at `{rounded.pill}` with a mono label; `badge-accent` sits on a 22% emerald tint
  under the pale ink. Status badges keep the chip's own surface and take only their dot and border
  from the status hue.
- **Navigation.** A milled channel (`--bar-shadow`) with the current item on an emerald tint, in
  `{colors.tertiary}`.

## Do's and Don'ts

- **Do** treat the emerald as a fill and its pale member as the label. Writing `--accent` as text is
  the mistake this kit's ink pair exists to prevent.
- **Do** keep the glow at 14px / 26%. It is the place's own value and its restraint is the identity.
- **Do** let the fern sit in the bottom-right of a plate and leave it alone. It is drawn at 248px
  with its alpha baked in; re-tinting or tiling it makes it a pattern.
- **Don't** lighten the ground to add contrast. The scene field is the lightest ground the kit was
  graded against, and every number in the README assumes it.
- **Don't** use `{colors.secondary}` for text, and don't introduce a third "look at me" hue — the
  status ladder is the only other colour family the kit carries.
- **Don't** add glass, backdrop blur or a coloured rim glow. All three are the opposite register.
