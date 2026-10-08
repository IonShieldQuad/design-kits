---
version: alpha
name: Radioactive
description: A containment site under CCTV — cold poured concrete, clinical white wall plates, hazard tape, and one toxic-green readout.
colors:
  primary: "#86c81a"
  primary-hover: "#78b814"
  primary-ink: "#1d4a06"
  secondary: "#e8860c"
  tertiary: "#17427e"
  neutral: "#c6cac3"
  surface: "#f2f4ef"
  surface-2: "#bfc3bc"
  text: "#12150f"
  text-muted: "#3a4136"
  text-dim: "#424a3f"
  invert: "#10130d"
  success: "#0d5230"
  warning: "#6a3f04"
  error: "#8a160d"
typography:
  display:
    fontFamily: Chakra Petch
    fontSize: 2.7rem
    fontWeight: 700
    lineHeight: 1.04
    letterSpacing: "-0.005em"
  heading:
    fontFamily: Chakra Petch
    fontSize: 1.3rem
    fontWeight: 600
    lineHeight: 1.2
  body:
    fontFamily: Archivo
    fontSize: 0.98rem
    fontWeight: 400
    lineHeight: 1.55
  label:
    fontFamily: IBM Plex Mono
    fontSize: 0.72rem
    fontWeight: 500
    lineHeight: 1
    letterSpacing: "0.16em"
  readout:
    fontFamily: IBM Plex Mono
    fontSize: 0.9rem
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: "0.04em"
rounded:
  sm: 2px
  md: 4px
  lg: 6px
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
    textColor: "{colors.invert}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: 16px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.invert}"
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
    textColor: "{colors.tertiary}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 14px
  alert-error:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.error}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 14px
  caption:
    textColor: "{colors.text-dim}"
    typography: "{typography.body}"
  table-header:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text-muted}"
    typography: "{typography.label}"
  link:
    textColor: "{colors.primary-ink}"
    typography: "{typography.body}"
---

# Radioactive

## Overview

A containment site under CCTV, photographed in daylight. The subject is a **building** — a decommissioned
reactor hall, a hazardous-materials store, a clean room with a spill in it — so the ground is poured
concrete and the working surfaces are the clinical white plates bolted onto it. The only things that
burn are the readouts: one toxic acid green for the live, actionable material, and one safety amber for
warnings and tape.

The kit is **light**, and that is the central decision. Hazard tape is meaningless on near-black — the
black band of a yellow/black diagonal vanishes — and "institutional" is a property of concrete in
daylight, not of a glowing poster. A dark green-on-black reading would have made a science-fiction
title card; a mid-grey concrete hall with yellow/black tape, white instrument plates and a green CRT
readout reads as a *regulated facility*. The glow that the genre does deserve is kept, but scoped to
the one element that is actually energised.

## Colors

Acid green `#86c81a` is the single action colour — the live lamp, the spill, the readout phosphor and
the "go" signal. It is a bright yellow-green on purpose: as a **fill** it is light enough to carry
near-black ink (`#10130d`, 9.18:1), which is the hazard-signage convention — black on yellow-green,
never white. As small **text** it cannot work on concrete (1.6:1), so the kit ships `--accent-ink`
(`#1d4a06`) for eyebrows, links, active tabs, badge labels and secondary buttons.

Safety amber `#e8860c` is the second accent and the hot warning tone. It belongs to *warning and data*
— media panels, charts, the hazard tape — and it is a **fill only**: it never carries a text label. The
third hue is an institutional telemetry blue `#17427e` for the `info` register, so a facility UI has its
CCTV/telemetry voice without inventing a third "look at me" colour.

The concrete `#c6cac3` is a cold green-grey, never neutral and never beige: a neutral grey would read as
office, and a warm grey as domestic. The clinical white `#f2f4ef` is the palest ground, and every ink is
graded against the **darkest aggregate pixel** of the floor (`~#bcc0b9`) and against the recessed slab
`#bfc3bc` — the two binding grounds. Because the kit is a three-tier stack (concrete → white plate →
grey well), text inside cards and inside insets ships separately as `--text-on-surface*` and
`--text-on-surface-2*` rather than inheriting one page-wide ink.

## Typography

Chakra Petch is the **display** face — a squared, technical signage letterform that reads as a stencilled
label on a control panel. It is not asked to set body copy. Archivo, a neutral institutional grotesque,
carries running text at reading size. IBM Plex Mono is the telemetry face: every readout, counter,
field label and code block is monospaced, because a facility's numbers are tabular. The `0.16em` tracking
on caps is what makes a small mono label read as machine output rather than as prose. Two families plus
a mono is the ceiling; nothing here is decorative.

## Layout

Spacing is firm rather than airy — `16px` gutters, `24px` between blocks — so the concrete shows between
the plates. Corners are `2px`–`6px`: machined, not rounded. Nothing is a pill; a badge is a stamped plate
at `2px` because the token must keep its name even when the shape is square.

## Elevation & Depth

Depth is **physical, not atmospheric**. `--blur` is `none`; there is no frosted glass on a poured floor.
Cards lift with a hard 1px lip plus a low, tight drop (`--shadow-1`/`--shadow-2`) so they read as plates
standing off the wall. The one luminous device is `--glow`: a **tight** acid-green ring with a short
bloom, applied by the lab to the primary button and to focus. It is deliberately scoped — it marks the
element that is *live* (the actionable control, the focused field, the active tab), and it is tight
enough to read as an energised indicator lamp rather than as neon atmosphere. Glow is a design decision
here: a containment site is full of things that are literally glowing, and this kit uses that fact to
give exactly one element on each screen its "on" state.

## Shapes

The kit's geometry lives in its three signature devices rather than its corners. The **trefoil**
(`--radioactive-trefoil`) is drawn inline SVG because it is exact geometry — three congruent annular
sectors at 120° around a core — and no stack of gradients can produce a wedge. The **hazard hatching**
(`--radioactive-hazard`) is drawn too — a 45° yellow/black tape pattern as inline SVG, giving crisp
hard bands where a CSS `repeating-linear-gradient` would be rescaled and blurred by the gallery's
preview normaliser. The **spill** (`--radioactive-spill`) is drawn too: a toxic puddle is a blob with a
hot core, spatter and rising vapour — structure, not a green gradient — and it carries its own dark hall
base so the tile reads as luminescence in a dark cell. Three motifs, three jobs: a symbol, a warning, an
atmosphere.

## Components

Primary buttons are acid-green fills with near-black labels — a pulled alarm cover; secondary buttons are
white plates with green labels; the danger button keeps the white plate and takes breach-red text. Cards
are the clinical-white plates; the elevated card recesses to the grey concrete slab (`--surface-2`).
Fields are milled *into* the concrete (`--input-inset`) and square, and the native checkbox and radio are
squared via the `--check-*` tokens (a native control ignores `border-radius`, so a square kit that skips
them renders the one shape it forbids). Progress and avatar fills are hard-banded two-tone acid — hazard
tape in green. Media panels are the CCTV readout, not an accent ramp.

## Do's and Don'ts

- **Do** keep green for the live/actionable layer and amber for warning and data. Two accents, two jobs.
- **Do** let the glow stay on the one energised element. Scattered over the page it becomes a poster.
- **Do** keep body copy on concrete or a white plate — never set text on the trefoil, the tape or a readout.
- **Don't** use the bright acid green as a text colour; it is a fill. Text green is `--accent-ink`.
- **Don't** put amber on a control label — it is a warning hue and a fill, and it never carries type.
- **Don't** round the corners or add glass. The facility is machined and cast, not soft.
