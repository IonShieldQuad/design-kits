---
version: alpha
name: Mecha Pilot
description: The pilot's instrument panel — amber readouts, a targeting reticle, a range scale and hazard tape on gunmetal, with no smooth edge anywhere.
colors:
  primary: "#ffab2b"
  primary-hover: "#ffbc4d"
  primary-ink: "#ffc061"
  secondary: "#3fd0e6"
  tertiary: "#ffd24a"
  neutral: "#0d1116"
  surface: "#171d24"
  surface-2: "#111720"
  text: "#e8eef5"
  text-muted: "#9aa6b3"
  success: "#4ee08a"
  error: "#ff5a4d"
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
    textColor: "{colors.secondary}"
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

The pilot's instrument panel. Not the mecha — the cockpit: the small, dense, backlit board the
pilot actually reads at 0600. The ground is gunmetal under a CRT scan-line field; the panels are
flat plates; and the whole language is **instrumentation** — an amber readout lamp that means
"act", a cyan channel that means "data", a warning red, and the three devices a real panel is
built from: a targeting reticle, a calibrated range scale, and hazard tape.

This kit sits deliberately between two neighbours and is defined by what it refuses to borrow.
`inside-the-machine` is industrial hardware **texture** — carbon weave, vents, engraved inset
seams, a mono that carries the interface. Mecha Pilot has no texture and no engraving: its depth
is a hard **offset** (a plate standing proud of the floor), its readouts are **lit** rather than
milled, and its identity lives in drawn instruments rather than in the material. `carbon` is neon
**cyan** on carbon black with **cut** corners; here the action colour is amber, the data colour is
a calm instrument cyan rather than neon, and there is **no chamfer** — an instrument bezel is
square, so every corner in the kit is a right angle.

Nothing in the kit is smooth. Every edge is orthogonal, every shadow is a zero-blur offset, every
gradient is hard-stopped, and the only "glow" is a phosphor bloom built from three concentric hard
rings, because it is a lit lamp and a lamp has a job.

## Colors

Amber `#ffab2b` is the readout: the lamp that prints, the plate that acts, the one saturated
object on a screen. Cyan `#3fd0e6` is the data channel and belongs to telemetry, media, progress
and focus — technology, never action. Red `#ff5a4d` is the warning, and it arrives as tape and as
an annunciator, not as a control.

The four status lamps are the annunciator strip of an aircraft panel — green nominal, yellow
caution, red warning, cyan data — and they never carry a primary action. The yellow caution lamp
is deliberately *yellower* than the amber readout so a caution chip can never be mistaken for the
action.

The ground is a gunmetal that never goes neutral-black and never goes blue: `#10151b` over
`#0d1116`, a warm-cool graphite that reads as painted metal. Panels lift one step (`#171d24`) and
readout wells sink to `#111720`. Because the CRT scan-line layer only ever *darkens*, the lightest
pixel the page can show is the plate itself, and that is the ground every ratio below is graded
against.

Amber is a fill, so text-amber ships separately: `--accent-ink` (`#ffc061`) carries eyebrow,
links, active nav and badge labels, and clears 10.5:1 on the lightest ground and 7.6:1 on its own
`--accent-soft` tint composited over a panel.

## Typography

Three faces, three jobs. **Chakra Petch** is the display and the readout: squared, mechanical,
drawn for exactly this register. **Saira** is the body — a clean technical grotesque that stays
readable in a paragraph where Chakra Petch would turn into decoration. **Share Tech Mono** is the
mono: every kicker, table header, badge and metric is set in it, because on this panel anything
that is a *fact* is printed in the readout face.

Caps labels run `+0.16em`, wider than a stamped plate (`inside-the-machine` uses `.12em`) because
this is a HUD, not a machined case. Chakra Petch is display-only: below ~18px it becomes
decoration, so body copy is Saira at 400.

## Layout

Spacing is instrument-panel tight — `16px` gutters, `24px` between blocks — so readouts cluster the
way they do on a real board. There is no asymmetry and no airiness: an instrument panel is dense
by definition. Corners are `0px` everywhere, badges included; the geometry is orthogonal.

## Elevation & Depth

Depth is a **hard offset**, never a blur. A panel is a plate sitting `4px` (`--shadow-1`) or `6px`
(`--shadow-2`) proud of the floor, with a `1px` amber bezel line inset into its edge. Reads sit
*into* the panel (`--input-inset`, a zero-blur milled well). The one place a bloom appears is
`--glow`, the lit readout: it is a phosphor halo **stepped into three concentric hard rings**
(1px / 3px / 5px) rather than a blurred one, so it stays non-smooth while still reading as "this
lamp is on". It is wired to the primary action and the focus ring only.

## Shapes

The kit's geometry lives in three drawn instruments rather than in its corners:

- `--mecha-pilot-reticle` — **the symbol**. Concentric rings with a dashed radial tick ring, a
  gapped crosshair, corner brackets and a top index, drawn as inline SVG. A gradient cannot make a
  ring with radial ticks; only vector can.
- `--mecha-pilot-scale` — **the measurement**. A heading/range tape with hard minor ticks, taller
  major ticks, numerals, end brackets and a bright index needle, also drawn. A repeating gradient
  makes an even comb that has no majors, which is not a calibrated scale.
- `--mecha-pilot-hazard` — **the warning**. The instrument-panel hazard tape: hard 45° amber/black
  stripes under a 2px amber rule at both edges. This one is pure repeating gradient.

Three motifs, three different jobs. The CRT scan-line field is *not* a fourth tile — it is the
page floor and the media panel, which is where a screen belongs.

## Components

Buttons are amber plates with gunmetal labels, or flat panels with amber labels; every button
variant wears the same hard `2px 2px 0` key-offset, and only the primary one wears the lamp glow.
Cards are flat plates lifted off the floor; the elevated card is the readout well. Inputs sit
milled into the panel. Badges are hard squares carrying mono caps, with status badges on the
chassis black. Media panels are a display: a dark amber phosphor screen with hard sweep bands and
a scan-line field, opaque (`--media-op: 1`).

## Do's and Don'ts

- **Do** keep amber for action and cyan for data. Two accents, two jobs.
- **Do** keep the corners square. The bezel is square; a rounded cockpit is not a cockpit.
- **Do** let the reticle, the scale and the hazard tape do the identifying work — they are the kit.
- **Don't** add a third accent, a soft gradient, or a blurred shadow. Every one of those reopens a
  door this kit deliberately shut.
- **Don't** put the caution yellow on a primary action; the amber lamp is the only thing that acts.
- **Don't** blur the glow into a real halo. It is three hard rings on purpose.
