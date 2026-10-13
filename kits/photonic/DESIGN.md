---
version: alpha
name: Photonic
description: Transparent film lit at the rim — panes you see through, a glowing hue-coded edge that bleeds inward and dies at the centre, a drawn honeycomb light-field, and one spectrum that lives in the material.
colors:
  primary: "#15b9ff"
  primary-hover: "#4acaff"
  on-primary: "#061019"
  primary-soft: "rgba(21, 185, 255, 0.16)"
  secondary: "#b64ce8"
  tertiary: "#8fe3ff"
  neutral: "#05070d"
  surface: "rgba(3, 6, 13, 0.62)"
  surface-2: "rgba(2, 4, 9, 0.78)"
  surface-solid: "#09121c"
  text: "#e8f3fa"
  text-muted: "#a9b8c4"
  text-dim: "#8e9dab"
  ok: "#15ffab"
  warn: "#ffa23a"
  danger: "#ff554a"
  info: "#6c8cf5"
  border: "rgba(21, 185, 255, 0.42)"
  border-strong: "rgba(21, 185, 255, 0.72)"
  bg-stop-1: "#060910"
  bg-stop-2: "#05070d"
  bg-stop-3: "#04050a"
  weave: "#7ee7ff"

typography:
  display:
    fontFamily: "Genos"
    fontSize: "2.7rem"
    fontWeight: 600
    lineHeight: 1.04
    letterSpacing: "0.004em"
  h1:
    fontFamily: "Genos"
    fontSize: "1.75rem"
    fontWeight: 600
    lineHeight: 1.12
    letterSpacing: "0.004em"
  h2:
    fontFamily: "Genos"
    fontSize: "1.3rem"
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: "0.01em"
  body:
    fontFamily: "Rubik"
    fontSize: "0.95rem"
    fontWeight: 400
    lineHeight: 1.62
  small:
    fontFamily: "Rubik"
    fontSize: "0.8rem"
    fontWeight: 400
    lineHeight: 1.5
  button:
    fontFamily: "Rubik"
    fontSize: "0.875rem"
    fontWeight: 500
    lineHeight: 1.2
  label:
    fontFamily: "Azeret Mono"
    fontSize: "0.72rem"
    fontWeight: 500
    letterSpacing: "0.18em"

rounded:
  sm: "8px"
  md: "14px"
  lg: "26px"
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
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
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
  card-solid:
    backgroundColor: "{colors.surface-solid}"
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
    backgroundColor: "{colors.secondary}"
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

# Photonic

**Transparent film, lit at the rim.** Not a dark card with a coloured border: a pane you can see
through, whose only light source is its own edge. The rim is a saturated hue, the hue bleeds inward
and dies at the centre, the pane darkens whatever is behind it by 62%, and everything sits on a
drawn honeycomb light-field at a 14px pitch. There is one spectrum (the reference's conic disc) and
it lives in the material — a progress fill, an avatar, a media panel — never as a third accent.

## Overview

A hologram is an optical object before it is a UI style: light leaves an edge, passes through a
film, and what you see is the *combination* of that film with whatever is behind it. This kit is
built from that sentence, and every decision below follows from it.

- **The back layer is a screen.** A tablet display: a flare along its top edge, 32px display rows,
  the honeycomb emitter lattice, a backlight blooming down from the top and a vignette at the rim.
  It is the light source, and it is part of the theme rather than a neutral backdrop.
- **The front layers float off it.** `{colors.surface}` is the *pane material*, not a fill: the woven
  lattice (a 14px pitch) + the rim light (dark through the middle, cyan arriving at the edge, violet
  rising in one corner) + a 56% blue film. 44% of the screen still shows through every pane; the film
  over the kit's lightest ground pixel lands at `#0f3046`, over a white page at `#657b8a`. A pane's
  value is *derived*, and the soft occluding halo in `--shadow-1` is what lifts it off the display.
- **The field is inside the weave, never on its own.** `{colors.surface-2}` — inputs, alerts, badges,
  progress tracks, code blocks — carries the same two layers as a card, at about half the strength and
  at three times the cell size, so a small control shows one cell edge rather than a pattern.
- **The material is saturated; the ground is not.** The reference's tiles are vivid — hue at full
  saturation on a thin rim, bleeding inward — and a neutral film on a near-black ground renders as
  dead grey. So the colour is spent where it belongs (rims, blooms, the card's own weave, the
  spectrum) and the ground's lattice is pitched at 3× the cell size with a third of the contrast.
- **The rim is the emitter.** `{colors.border}` at `rgba(21,185,255,.42)` plus the inward bleed and
  outward bloom of `--shadow-1` — the reference's measured `inset 2px 4px 10px 4px` and
  `0 0 8px 4px`.
- **The lattice is drawn.** A honeycomb at a 14px pitch (the reference's own measurement), drawn as
  base64 SVG and tiled — here it doubles as the screen's emitter matrix rather than sitting behind
  the page as decoration.
- **Hue codes function, not decoration.** Cyan is the action, violet the counterpoint, and the
  reference's other two tiles — mint, coral — become the status ladder.

## Colors

`{colors.primary}` is the reference's system cyan, taken from the file's own label glow, at the
saturation the reference drew it (its rims are 100% saturation — the kit does not soften them). It is
the only action colour: primary buttons, links, active nav, the focus ring. `{colors.secondary}` violet
is the counterpoint, confined to media, charts and the spectrum. `{colors.tertiary}` is the same
cyan family re-tuned for **text** — the fill colour is 8.5:1 on a pane but only as a large label,
so small type uses the lighter member.

The status ladder is the reference's remaining tile hues: `{colors.ok}` is its mint, `{colors.danger}`
its coral, `{colors.warn}` and `{colors.info}` are stops sampled out of its conic disc.

`{colors.neutral}` is the ground. It is not a preference: it is the floor the film was graded
against, and the lightest pixel any viewer can scroll to is `#122535` (three washes overlapping).

## Typography

Genos for display — a squared technical face that reads as signage rather than as a HUD readout —
Rubik for body text, Azeret Mono for labels, keys and metadata. Labels are uppercase mono at
`{typography.label}` (12px floor) with `{typography.label.letterSpacing}`, the register of an
instrument that names its own channels rather than a poster.

The reference's own label face is Gruppo; the `holographic` kit already carries it from this same
node, so it is deliberately not doubled here. The reference's heading face (Nova Flat) belongs to
`cyber-angel`.

## Layout

The page is a display, so the ground is never blank: the screen's rows, lattice, backlight and
vignette carry the top of the document and stay anchored in px as it scrolls. A 12-column feel with
generous vertical rhythm (`{spacing.lg}` between sections, `{spacing.xl}` for
hero pacing). Panes can overlap — a translucent surface over another pane is the one composition
this kit affords and no other dark kit does — but never more than one level deep, because two 62%
films stack to 86% and the second one stops reading as film at all.

The weave is pitched in px, not %, so the field's scale is constant from the masthead to the footer
of a long document.

The colour field inside a card **decays with distance from the nearest border** rather than from the
centre: deep cyan arrives from the top and bottom, deep violet from the left and right, each reaching
about 40–46% into the box and falling to nothing. A corner, being nearest two borders, is therefore the
brightest point of a card and the middle is its quietest — the same model the reference's tiles use.

## Elevation & Depth

Depth is **emitted, then occluded**. `--shadow-1` is four parts: the inward hue bleed (`inset 2px 4px
10px 4px` at 34%) and the outward bloom (`0 0 14px 2px` at 45%) from the reference — its own measured
rim glow is 45–50%, so the bloom is *bright*, not wide — plus a lit top edge, light from the screen
arriving under the pane, and a wide, soft *occluding* halo beneath it. That halo is
the one thing the reference could not teach: there the panels were drawn on a flat canvas and needed
no separation, while here a pane floats in front of a lit display and collapses into a bordered card
without it. `--shadow-2` deepens both for a surface that must float off another pane.

`--blur` at `blur(10px) saturate(112%)` is load-bearing: a 54% film over an emissive ground is
see-through by design, and the blur is what keeps the screen's own lattice from reading through the
text on top of it. Remove it and the pane stays transparent but stops being legible.

## Shapes

`{rounded.sm}` 8px (the reference's own panel radius), `{rounded.md}` 14px, `{rounded.lg}` 26px for
panes, pills at 999px, `--cut: 0px`. A hologram has no mitered corners — this kit rounds, and it
rounds generously, the way the reference's 180px tile carries an 18% corner radius.

## Components

- **button-primary** — a solid `{colors.primary}` plate with a `{colors.on-primary}` label and the
  full `--glow` bloom. It is the one filled, opaque thing in the kit, which is exactly how it stays
  distinguishable from the status hues it sits beside.
- **button-secondary** — `{colors.surface}` film with cyan text and the `--btn-shadow` rim: a lit
  pane, not a stroked button.
- **card** — the film, a 1px rim, `--shadow-1`, `--blur`. Its value is derived from the ground.
- **card-elevated** — the denser film with `--shadow-2`; the extra opacity is what lifts it.
- **input** — a shallow lens recess: `--input-inset` is a dark well with a lit lip, so a field looks
  machined into the pane rather than printed on it.
- **badge** — mono, uppercase, pill; `badge-accent` carries the cyan tint, the others take a status
  hue with a tinted rim.
- **avatar / chart-1..3** — where the spectrum and the counterpoint are allowed.

## Do's and Don'ts

**Do**

- Keep the ground. A pane's value comes from what is behind it — that is the kit, not a detail.
- Grade any new text colour against the **composited** pane (film over the lightest ground pixel).
- Reach for the rim and the bloom before reaching for a heavier border.
- Keep the weave at a 14px pitch. Finer and it reads as noise; coarser and it reads as wallpaper.

**Don't**

- Don't set `--blur` to `none`. Without it the film stops hiding what is behind it.
- Don't flatten a card onto `{colors.surface-2}` or a solid fill; `{colors.surface}` *is* the material.
- Don't shrink the ground's cells back to the card's pitch — the two scales are what keep the page and
  the panes from fighting.
- Don't swap `--bg` for a light ground: `--text-muted` falls to 3.07:1 on a white page.
- Don't stack more than one translucent pane.
- Don't use `{colors.secondary}` (violet) as an action colour or as small text — it is 4.7:1 on a
  pane and belongs to media and charts.
- Don't add a third accent. The four reference hues are one action, one counterpoint and two status
  colours; a fifth hue makes a hologram look like a dashboard.
- Don't put the weave behind text at a higher amplitude than the token ships — it is a field, not a
  pattern.
