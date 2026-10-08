---
version: alpha
name: Mecha Pilot
description: The pilot's military HUD — phosphor-green readouts, a targeting reticle, a range scale and caution tape on a dark olive board, with no smooth edge anywhere.
colors:
  primary: "#4dff9e"
  primary-hover: "#7dffb8"
  primary-ink: "#8fffc4"
  secondary: "#43d9e6"
  tertiary: "#ffb03a"
  neutral: "#10140a"
  surface: "#1e2416"
  surface-2: "#141910"
  text: "#e7f0dc"
  text-muted: "#a7b59b"
  success: "#8bf24d"
  error: "#ff5147"
  info: "#43d9e6"
typography:
  display:
    fontFamily: Chakra Petch
    fontSize: 2.9rem
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: "0.01em"
  heading:
    fontFamily: Chakra Petch
    fontSize: 1.3rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: "0.006em"
  body:
    fontFamily: Saira
    fontSize: 0.95rem
    fontWeight: 400
    lineHeight: 1.55
  label:
    fontFamily: Share Tech Mono
    fontSize: 0.75rem
    fontWeight: 400
    lineHeight: 1
    letterSpacing: "0.16em"
  readout:
    fontFamily: Chakra Petch
    fontSize: 1rem
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: "0.05em"
rounded:
  sm: 0px
  md: 0px
  lg: 0px
  pill: 0px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.neutral}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: 14px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.neutral}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary-ink}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: 14px
  button-secondary-hover:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.primary-ink}"
    rounded: "{rounded.md}"
  button-danger:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.error}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: 14px
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
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.md}"
    height: 96px
  card-media-2:
    backgroundColor: "{colors.secondary}"
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
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.primary-ink}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
  badge-success:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.success}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
  badge-warning:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.tertiary}"
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
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 14px
  alert-error:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.error}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 14px
  table-header:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text-muted}"
    typography: "{typography.label}"
  link:
    textColor: "{colors.primary-ink}"
    typography: "{typography.body}"
---

# Mecha Pilot

## Overview

The pilot's military flight/weapons HUD. Not the mecha — the cockpit: the small, dense, backlit board
the pilot actually reads at 0600. The ground is a dark olive under a CRT scan-line field and a hard
instrument grid; the panels are flat plates; and the whole language is **instrumentation** — a
phosphor-green readout lamp that means "nominal", an amber legend that means "caution", a red legend
that means "master caution", and the three devices a real panel is built from: a targeting reticle, a
calibrated range scale, and caution tape.

This kit sits deliberately between two neighbours and is defined by what it refuses to borrow.
`inside-the-machine` is industrial hardware **texture** — carbon weave, vents, engraved inset seams,
a mono that carries the interface — and its action colour is amber. Mecha Pilot has no texture and no
engraving: its depth is a hard **offset** (a plate standing proud of the floor), its readouts are
**lit** rather than milled, its action colour is phosphor **green**, and its identity lives in drawn
instruments rather than in the material. `carbon` is neon **cyan** on carbon black with **cut**
corners; here the second colour is a calm instrument cyan rather than neon, and there is **no
chamfer** — an instrument bezel is square, so every corner in the kit is a right angle.

Nothing in the kit is smooth. Every edge is orthogonal, every shadow is a zero-blur offset, every
gradient is hard-stopped, and the only "glow" is a phosphor bloom built from three concentric hard
rings, because it is a lit lamp and a lamp has a job.

## Colors

Phosphor green `#4dff9e` is the light: the readout that prints, the plate that acts, the one
saturated object on a green-black screen. It is a *cool* green — a mint leaning toward cyan, not a
plant green. Cyan `#43d9e6` is the data channel and belongs to telemetry, media, progress and focus —
technology, never action.

The **status ladder is military**, and it is the point of the palette. Green `#8bf24d` is *nominal*,
amber `#ffb03a` is *caution*, red `#ff5147` is *master caution*; cyan `#43d9e6` is *data*. The action
colour is **also green**, so the nominal lamp must be a *different* green: the action is a cool mint at
hue 147° and nominal is a yellow-leaning "GO" lamp at hue 90°, a 57° hue gap. An action plate can
therefore never be read as a status lamp. Amber and red never carry a primary action — they are the
two cautions.

The ground is a dark olive that never goes neutral-black and never goes blue: `#161b10` over
`#10140a`, a green-black with a khaki cast that reads as matte olive housing. Panels lift one step
(`#1e2416`) and readout wells sink to `#141910`. Because the CRT scan-line layer and the hard
instrument grid only ever *darken*, the lightest ground any type sits on is the plate itself, and that
is the ground every ratio below is graded against.

Green is a fill, so text-green ships separately: `--accent-ink` (`#8fffc4`) carries eyebrow, links,
active nav and badge labels, and clears 13.1:1 on the lightest ground and 8.6:1 on its own
`--accent-soft` tint composited over a panel.

## Typography

Three faces, three jobs. **Chakra Petch** is the display and the readout: squared, mechanical, drawn
for exactly this register. **Saira** is the body — a clean technical grotesque that stays readable in
a paragraph where Chakra Petch would turn into decoration. **Share Tech Mono** is the mono: every
kicker, table header, badge and metric is set in it, because on this panel anything that is a *fact*
is printed in the readout face.

Caps labels run `+0.16em`, wider than a stamped plate (`inside-the-machine` uses `.12em`) because
this is a HUD, not a machined case. Chakra Petch is display-only: below ~18px it becomes decoration,
so body copy is Saira at 400.

## Layout

Spacing is instrument-panel tight — `16px` gutters, `24px` between blocks — so readouts cluster the
way they do on a real board. There is no asymmetry and no airiness: an instrument panel is dense by
definition. Corners are `0px` everywhere, badges included; the geometry is orthogonal.

## Elevation & Depth

Depth is a **hard offset**, never a blur. A panel is a plate sitting `4px` (`--shadow-1`) or `6px`
(`--shadow-2`) proud of the floor, with a `1px` green bezel line inset into its edge. Reads sit
*into* the panel (`--input-inset`, a zero-blur milled well). The one place a bloom appears is
`--glow`, the lit readout: it is a phosphor halo **stepped into three concentric hard rings**
(1px / 3px / 5px) rather than a blurred one, so it stays non-smooth while still reading as "this
lamp is on". It is wired to the primary action and the focus ring only.

## Shapes

The kit's geometry lives in three drawn instruments rather than in its corners:

- `--mecha-pilot-reticle` — **the symbol**. Concentric rings with a dashed radial tick ring, a gapped
  crosshair, corner brackets, a top index and a two-sided range ladder of descending ticks, drawn as
  inline SVG. A gradient cannot make a ring with radial ticks; only vector can.
- `--mecha-pilot-scale` — **the measurement**. A heading/range tape with hard minor ticks, taller
  major ticks, stencil numerals, end brackets and a bright index needle, also drawn. A repeating
  gradient makes an even comb that has no majors, which is not a calibrated scale.
- `--mecha-pilot-hazard` — **the warning**. The instrument-panel caution tape: hard 45° amber/olive
  stripes under a 2px amber rule at both edges. This one is pure repeating gradient, and amber is the
  caution rung of the ladder, so it is the one place amber appears.

Three motifs, three different jobs. The CRT scan-line field and the hard instrument grid are *not* a
fourth tile — they are the page floor and the media panel, which is where a screen belongs.

## Components

Buttons are green plates with olive-black labels, or flat panels with green labels; every button
variant wears the same hard `2px 2px 0` key-offset, and only the primary one wears the lamp glow.
Cards are flat plates lifted off the floor; the elevated card is the readout well. Inputs sit milled
into the panel. Badges are hard squares carrying mono caps, with status badges on the chassis black —
green nominal, amber caution, red master caution. Media panels are a display: a dark green phosphor
screen with hard sweep bands, a scan-line field, a data grid and an opaque bar-code data strip, opaque
(`--media-op: 1`).

## Do's and Don'ts

- **Do** keep green for the readout and the action, and cyan for data. Two channels, two jobs.
- **Do** keep the ladder: green nominal, amber caution, red master caution. Amber and red never act.
- **Do** keep the nominal lamp (`--ok`, hue 90°) distinct from the action plate (`--accent`, hue
  147°); collapse them and an action reads as a status lamp.
- **Do** keep the corners square. The bezel is square; a rounded cockpit is not a cockpit.
- **Do** let the reticle, the scale and the caution tape do the identifying work — they are the kit.
- **Don't** add a third accent, a soft gradient, or a blurred shadow. Every one of those reopens a
  door this kit deliberately shut.
- **Don't** put a caution amber on a primary action; the green lamp is the only thing that acts.
- **Don't** blur the glow into a real halo. It is three hard rings on purpose.
