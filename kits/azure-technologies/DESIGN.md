---
version: alpha
name: Azure Technologies
description: The reference place of the Li//OS desk family — a cold orbital instrument console of cyan hairlines on a near-black blue ground, a hexagon lattice in the card material, and 16px chamfers.
colors:
  primary: "#4FD8FF"
  primary-hover: "#7FE4FF"
  primary-ink: "#04121A"
  primary-text: "#8BE8FF"
  secondary: "#7E8CFF"
  tertiary: "#0B2233"
  neutral: "#05080D"
  surface: "#0A0F16"
  surface-2: "#0A0F15"
  text: "#E8F2F8"
  text-muted: "#B7C7D3"
  text-dim: "#9AADBC"
  success: "#4EE6B0"
  warning: "#FFC04D"
  error: "#FF6377"
  info: "#A98BFF"
typography:
  display:
    fontFamily: Chakra Petch
    fontSize: 2.9rem
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: "0.004em"
  heading:
    fontFamily: Chakra Petch
    fontSize: 1.3rem
    fontWeight: 650
    lineHeight: 1.2
    letterSpacing: "0.004em"
  body:
    fontFamily: Chakra Petch
    fontSize: 0.95rem
    fontWeight: 400
    lineHeight: 1.55
  label:
    fontFamily: JetBrains Mono
    fontSize: 0.75rem
    fontWeight: 600
    lineHeight: 1
    letterSpacing: "0.14em"
  mono:
    fontFamily: JetBrains Mono
    fontSize: 0.8rem
    fontWeight: 400
    lineHeight: 1.6
rounded:
  none: 0px
  sm: 0px
  md: 0px
  lg: 0px
  pill: 2px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.primary-ink}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: 16px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.primary-ink}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.primary-text}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: 16px
  button-secondary-hover:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary-text}"
    rounded: "{rounded.md}"
  button-danger:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.error}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: 16px
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.lg}"
    padding: 18px
  card-elevated:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
  card-title:
    textColor: "{colors.text}"
    typography: "{typography.heading}"
  card-body:
    textColor: "{colors.text-muted}"
    typography: "{typography.body}"
  card-media:
    backgroundColor: "{colors.tertiary}"
    rounded: "{rounded.md}"
  input:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 10px
  badge:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text-muted}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: 4px
  badge-accent:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.primary-text}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
  badge-success:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.success}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
  badge-warning:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.warning}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
  badge-danger:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.error}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
  alert-info:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.info}"
    rounded: "{rounded.md}"
    padding: 12px
  alert-error:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.error}"
    rounded: "{rounded.md}"
    padding: 12px
  nav:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-muted}"
    rounded: "{rounded.md}"
    padding: 8px
  nav-item-active:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.primary-text}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
  table-header:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-dim}"
    typography: "{typography.label}"
  link:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.primary-text}"
---

## Overview

Azure Technologies is place 01 of the Li//OS desk — the reference instance of a family of
fifteen instrument-panel places, six of which are ported here. It is a cold orbital console:
a near-black blue ground, cyan hairlines at 1px, an opaque card face carrying a 36 x 20.7846
hexagon lattice at 9%, a 16px chamfer on every plate, and no rounding anywhere.

The desk's grammar is what makes it one family rather than six skins: a hairline frame, an
opaque face with a sheen band across its top 9%, a bottom occlusion band, a 157° face fall, a
5% accent tint and one drawn texture at 5–9%. This kit is that grammar with the fewest
modifications, which is exactly why it is the baseline: a sibling place changes its hue, its
motif or its corner treatment and keeps everything else, so this is the file to copy and the
file to diff against.

Two cues carry the register, both measurable. Depth is *light on a plate*, not elevation: the
only elevation tokens in the file are the desk's own `0 6px 16px rgba(0,0,0,.50)` and its
`0 10px 26px rgba(0,0,0,.55)`, and neither is visible on a clipped card — separation comes
from the 1px frame and the sheen lip. And nothing is soft: `--blur: none`, `--ease: linear`,
`--radius-*: 0px`.

## Colors

Six values were copied from the place's own token block and nothing was invented:

- **Primary (#4FD8FF)** — `--acc`. The action colour, the hairline colour, the identity edge
  along the bottom of every card, at 55% on that edge and 60% on `--border-strong`. It is a
  light fill (L≈0.58), so primary labels are `#04121A` rather than white: 11.4:1.
- **Primary-hover (#7FE4FF)** — one step lighter, the hover fill only.
- **Primary-text (#8BE8FF)** — `--accHi`, the desk's own answer to "accent as text": the
  eyebrow, links, active nav, secondary-button labels and badges. `--accent-ink-hover` is
  `#B0F1FF`.
- **Secondary (#7E8CFF)** — the violet the place's own space scene carries. It is the second
  accent, and it is used in gradient stops, charts and the media plate. Never a second call to
  action.
- **Tertiary (#0B2233)** — `--sceneA`, the two bloom fields in the ground and the media plate's
  light. It is a *light source* value, not a UI fill.
- **Neutral (#05080D)** — `--ground`, the page floor, ramping to `--sceneB #030609`.
- **Surface (#0A0F16) / surface-2 (#0A0F15)** — `--face` and `--panel`. The card is the face
  plus the material's five translucent layers; the nested tier is the panel plus a 6% sheen
  and a 4% tint.
- **Text (#E8F2F8) / text-muted (#B7C7D3) / text-dim (#9AADBC)** — the three ink steps, graded
  against the composited pane rather than against a solid (table in `README.md`).
- **Success / warning / error / info** — mint, amber, red and violet off the place's scene,
  `#4EE6B0` / `#FFC04D` / `#FF6377` / `#A98BFF`. Cyan stays the action; mint is 26° away and
  is separated by material as well as hue.

Three values are defined in `tokens.css` and absent from the map above because the DESIGN.md
component schema has no property that can carry them:

- `--border: rgba(255,255,255,.14)` — the frame hairline. It is white at 14%, not accent:
  a page of cyan frames reads as a wireframe, a page of white hairlines with one cyan edge per
  plate reads as an instrument.
- `--accent-soft: rgba(79,216,255,.16)` — nav selection, inline code, secondary hover.
- `--overlay: rgba(3,6,9,.72)` — modal scrim, derived from `--sceneB`.

## Typography

The family ships exactly two faces and shares them across all six places, deliberately: these
are places inside one operating system, and the type *is* the OS. Changing it per kit would
break the one thing that makes the set a set.

- **Chakra Petch** — display and body. Squared, technical, slightly condensed; it holds a
  2.9rem heading and a 0.95rem paragraph without either looking borrowed from the other.
  `--tracking-display: .004em` — this face is drawn tight and positive tracking opens it,
  where a neutral grotesque would need negative.
- **JetBrains Mono** — labels, badges, table headers, code, the eyebrow. Uppercase at
  `--tracking-caps: .14em`. If a string is a fact rather than a sentence, it is mono.

Display weight is 700, headings 650, body 400. Label floor is 12px, asserted by the harness.

## Layout

A single column at `min(1040px, 100% - 2.5rem)`; cards in an auto-fit grid at a 230px minimum,
collapsing to one column below ~640px. Density is medium-tight: 2.25rem section padding with
0.65–1rem internal gaps, so the page reads as plated modules on a board rather than a document.

The ground is deliberately *large-celled*: a 120px technical grid and the motif at 144 x 83.14
(twice the card's pitch). The components carry the motif at 36 x 20.7846 and 5.5%. Two scales,
two jobs — an equal-weight ground and card makes the whole page one busy field and every card
reads as texture inside texture.

Every scene size is a percentage, never a px: the gallery renders `--bg` into a ~118px tile and
a px-anchored radial shows it the top edge of the page instead of the scene.

## Elevation & Depth

There is no elevation model, only a light model, and it is the layer order inside
`--azure-technologies-pane`:

```
sheen (1px specular lip)  >  occlusion  >  texture  >  identity edge  >  tint  >  face fall  >  face
```

Why that order and not another:

- **Sheen above everything.** It is light arriving on the plate; nothing on the plate tints it.
- **Occlusion above the texture.** The bottom 9% of a card goes out of the light, so the
  lattice must dim there. Occlusion under the texture leaves a full-strength lattice in the
  dark band, which reads as a rendering fault.
- **Texture above the tint.** A 9% lattice under a 5% cyan tint is invisible; the tint is a
  wash on the face and the lattice is drawn on the wash.
- **Tint above the fall.** The fall is the face's own shading; the tint is the place's colour
  sitting on that face, so it takes the shading rather than replacing it.
- **The identity edge above the face and below the occlusion.** 1px of `--accLine` at 55%
  along the bottom, from 7% to 96% of the width — the one place a plate is allowed to be
  brighter than its frame.

`--shadow-1` and `--shadow-2` are the desk's drop-shadows as `box-shadow`, but a clipped plate
drops its shadow along the silhouette, so on cards they are effectively absent. That is the
documented cost of the chamfer, and the frame ring is what replaces them: the 1px ring derived
from `--clip` follows the diagonal, so a chamfered card keeps a closed outline. Glow exists
exactly once — `--glow: 0 0 14px rgba(79,216,255,.34)` on the primary action.

## Shapes

**Nothing in this kit is round.** Radii are 0 across the scale, `--radius-pill` is 2px (not 0,
so a badge's fill does not clip its own glyphs), `--check-radius` is 2px and
`--check-appearance: none` squares the native checkbox, because a native control ignores
`border-radius` and would otherwise render as the only circle on the page.

One chamfer, everywhere: `--cut: 16px` with

```css
--clip: polygon(var(--cut) 0, 100% 0, 100% calc(100% - var(--cut)),
                calc(100% - var(--cut)) 100%, 0 100%, 0 var(--cut));
```

The clip applies to cards, buttons, inputs, badges, alerts, nav and code blocks. Two
consequences, both documented rather than worked around: the border is cut along the diagonal
(fixed by the generated `--frame-ring`), and `outline` is cut too (`--focus-inset: 2px` paints
the keyboard ring inside the silhouette).

## Components

- **button-primary** — the only filled control in the kit. `#4FD8FF` plate, `#04121A` label,
  700 mono label at `.14em`, the 16px chamfer, and the desk's glow. One per screen.
- **button-primary-hover** — `#7FE4FF`; the label stays dark ink.
- **button-secondary** — no fill of its own, `--accent-ink` label, rim at
  `color-mix(in srgb, var(--accent) 45%, transparent)`. Its hover takes `--accent-soft`.
- **card** — the pane material: opaque `#0A0F16` face, lattice, sheen, occlusion, tint, and the
  cyan identity edge. The 1px frame is the ring, not a border.
- **card-elevated** — `--surface-2`: no lattice, no identity edge, 6% sheen and 4% tint. On a
  2.5rem control the card's material is clutter.
- **card-media** — the place plate: the lattice at card pitch over the scene's bloom on the
  face, at `opacity: 1`. Not the default accent→accent-2 ramp, which would read as a marketing
  banner in a console.
- **input** — `--surface-2` fill, 1px `--border`, chamfered; focus is the accent border plus
  the inset ring.
- **badge** — mono, uppercase, 2px radius, chamfered. `badge-accent` is `--accent-ink` on
  `--accent-soft`.
- **nav** — the pane material, so the bar is the same plate as the cards; the current item is
  `--accent-soft` with `--accent-ink`.

## Do's and Don'ts

- **Do** keep the frame at 1px. Separation in this kit is a hairline plus a sheen lip; a 2px
  ink line on near-black is what makes an instrument panel look printed.
- **Do** keep cyan for action and hairlines. It is a light colour — use `--accent-ink` for
  text and `--text-invert` on cyan fills.
- **Do** let the motif carry the surface. The lattice is 5.5% on the card and 2.75% on the
  ground on purpose; raising either makes the page one busy field.
- **Do** keep the chamfer at 16px. It is the family's shape; a sibling place changes hue or
  motif, not this.
- **Don't** add a second filled button, a gradient banner, or a blurred card. Every surface
  here is opaque and the desk forbids glass.
- **Don't** lighten `--text-dim` to make a caption pop. It is graded against the composited
  pane; the table in `README.md` is the argument.
- **Don't** use the violet for an action. It exists because the place's scene has a violet in
  it, not because the kit needs a second button.
