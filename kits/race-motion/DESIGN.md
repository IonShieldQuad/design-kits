---
version: alpha
name: Race Motion
description: Motorsport as broadcast — asphalt under kerbs and a chequered flag, set in a big italic.
colors:
  primary: "#d40a00"
  primary-hover: "#e10600"
  primary-ink: "#ff7a6d"
  secondary: "#e9eef3"
  tertiary: "#ffd23f"
  neutral: "#0d0f12"
  surface: "#1b1e24"
  surface-2: "#262a31"
  text: "#f3f6f9"
  text-muted: "#bcc3cc"
  text-invert: "#ffffff"
  success: "#3ddc84"
  error: "#ff6256"
typography:
  display:
    fontFamily: Saira
    fontSize: 3rem
    fontWeight: 800
    lineHeight: 1.02
    letterSpacing: "-0.01em"
  heading:
    fontFamily: Saira
    fontSize: 1.32rem
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "-0.005em"
  body:
    fontFamily: Inter
    fontSize: 0.95rem
    fontWeight: 400
    lineHeight: 1.55
  label:
    fontFamily: JetBrains Mono
    fontSize: 0.72rem
    fontWeight: 500
    lineHeight: 1
    letterSpacing: "0.16em"
  timing:
    fontFamily: JetBrains Mono
    fontSize: 0.82rem
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: "0.02em"
rounded:
  sm: 0px
  md: 2px
  lg: 3px
  pill: 3px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
components:
  page:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.text}"
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.text-invert}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: 16px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.text-invert}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary-ink}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: 16px
  button-secondary-hover:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.primary-ink}"
    rounded: "{rounded.md}"
  button-ghost:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-muted}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: 16px
  button-danger:
    backgroundColor: "{colors.surface}"
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
    rounded: "{rounded.lg}"
    padding: 18px
  card-title:
    textColor: "{colors.text}"
    typography: "{typography.heading}"
  card-media:
    backgroundColor: "{colors.secondary}"
    rounded: "{rounded.md}"
    height: 96px
  card-media-2:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.md}"
    height: 96px
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
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.primary-ink}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
  badge-success:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.success}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
  badge-caution:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.tertiary}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
  alert-error:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.error}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 14px
  link:
    textColor: "{colors.primary-ink}"
    typography: "{typography.body}"
---

# Race Motion

## Overview

The energy of a race broadcast, not a car brand. A marque's site is a white room with a red
accent; this is the other thing — tarmac at dusk, under lights, with a kerb at the edge of the
frame and a chequered flag across it. Racing red is the single action colour, bodywork white is
the second accent, and one signal yellow is kept for cautions alone.

The register is **asphalt** (the brief's dark option) rather than bodywork white. Three reasons:
a white ground with black type and a red accent is what every car marque already looks like; the
white halves of a kerb and a chequer disappear on a white page, so the two motifs this kit is
built on only work on a dark one; and a broadcast is lit from the top of the frame, which is what
`--bg` models. The mode is therefore `dark`.

The kit's geometry is a **speed cut** — the two leading (right) corners of every plate are
removed by `clip-path`, so cards, buttons, inputs and badges all lean forward. That chamfer plus
a heavy *italic* display face is what makes the kit identifiable at 200×120.

## Colors

Racing red `#d40a00` is the one action colour: primary buttons, focus, the live state. Its fill
is only 3.55:1 as a small label, so text-red ships separately as `primary-ink` `#ff7a6d` — every
link, eyebrow, active tab, badge label and inline code goes through it. Bodywork white `#e9eef3`
is the second accent (livery stripes, media fills); it is not a control colour.

The ground is `#26292f` at the top of the frame settling to `#0d0f12` at the bottom — asphalt,
never a neutral grey-black, and warm enough at the far end (`#33100e` in the slipstream) to read
as brake glow. `neutral` `#0d0f12` is that darkest stop.

Signal yellow `#ffd23f` is `tertiary`, and it does exactly **one** job: caution. It appears in
`--warn`, in `badge-caution`, and nowhere that asks the user to click or to act. Status colours
stay off the brand red: `success` is a green flag, `error` is a light coral-red tier deliberately
distinct from the deep fill so a "failed" badge is never mistaken for the accent.

## Typography

Three faces, three jobs. **Saira** is the display face and it is set **italic** — the register is
a broadcast graphic, and a broadcast graphic leans forward. Saira was chosen over Chakra Petch
(no italic exists) and over Archivo (italic exists, but a neutral grotesque) because its slightly
squared, technical italic is the sports-graphics voice; the italic itself is declared in `kit.css`
because the token contract carries a font *family*, never a font *style*. **Inter** is the body,
because it stays legible in quantity where a display face does not. **JetBrains Mono** is the
timing tower: labels, metrics and code, set wide (`0.16em`) in caps so small labels read as
graphics rather than as body text.

## Layout

Comfortable density — `16px` gutters, `24px` between blocks — so the loud surfaces have air.
Corners are effectively square: `0px` to `3px`, with the diagonal carried by the `12px` speed cut
instead of by a radius. Nothing is a pill; badges are chamfered tags. UI chrome (kickers, chips,
nav labels, meta lines) stays at or above 12px.

## Elevation & Depth

Flat, like a broadcast overlay: `--blur: none`, no `backdrop-filter`. Depth is a tight dark drop
(`0 3px 14px` / `0 12px 34px`) plus a red charge glow on the primary action. One honest caveat:
the kit opts into `--clip`, and `clip-path` clips `box-shadow`, so on a clipped plate those drops
read as *subtle* rather than absent — the chamfer and the hard bands carry most of the depth.
That is a documented limitation of the chamfer, not a bug, and it suits a flat overlay.

## Shapes

The kit's geometry lives in three signature tokens rather than in its corners:

- `--race-motion-chequer` — a **true two-tone chequered flag**: `repeating-conic-gradient` lays a
  2×2 block and `background-size` sets its period, so each square is exactly 12px. Hard-edged and
  crisp; it is deliberately sized in `rem` because the build's swatch normaliser rewrites any
  `NNpx` gradient inside a single paren pair into smooth `%` stops, which would melt the checker
  into a conic swirl.
- `--race-motion-kerb` — hard-banded red and white at −52°, never a smooth ramp (both stops share
  a position at every seam). The track edge.
- `--race-motion-slipstream` — speed lines: white and red streaks at 102° over a dark asphalt
  ground with a bright convergence where the car has just passed. This is what `--media-bg`
  paints, so a media panel shows motion rather than the lab's default flat accent ramp.

Three motifs, three jobs: identity (the flag), limit (the kerb), motion (the slipstream).

## Components

Primary buttons are red plates with a pure-white label (not a cream — the difference is the
4.97:1 pass). Secondary buttons are flat surfaces with red text through `primary-ink`. Cards sit
on `--surface` with a 2px steel rule, the elevated card deepens to `--surface-2`, and inputs are
milled by an inset shadow. Badges are chamfered tags carrying mono caps; the caution badge is the
kit's only yellow. Media panels use the slipstream.

## Do's and Don'ts

- **Do** keep red for action and white for structure; two accents, two jobs.
- **Do** let the speed cut do the diagonal work — a radius on top of a chamfer fights it.
- **Do** keep the signal yellow on cautions only. It is not a second brand colour.
- **Don't** put the red fill behind small text; use `primary-ink`.
- **Don't** add a blurred shadow, a glass panel or a third accent — this register is flat, loud
  and precise, and a bloom turns a broadcast into a dashboard.
