---
version: alpha
name: Retro Anime
description: 80s anime key art at dusk — indigo night, magenta neon, cyan tech, one striped sun.
colors:
  primary: "#ec4b8f"
  primary-hover: "#ff5fa2"
  primary-ink: "#1a0f2b"
  secondary: "#44a6d7"
  tertiary: "#ffb57b"
  neutral: "#19152b"
  surface: "#221a3a"
  surface-2: "#171129"
  text: "#f7ecff"
  text-muted: "#cbb8e4"
  success: "#45d6a4"
  warning: "#ffc46b"
  error: "#ff5f77"
typography:
  display:
    fontFamily: Audiowide
    fontSize: 2.9rem
    fontWeight: 400
    lineHeight: 1.06
    letterSpacing: "0.01em"
  heading:
    fontFamily: Rajdhani
    fontSize: 1.32rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: "0.005em"
  body:
    fontFamily: Rajdhani
    fontSize: 0.98rem
    fontWeight: 500
    lineHeight: 1.55
  label:
    fontFamily: Share Tech Mono
    fontSize: 0.72rem
    fontWeight: 400
    lineHeight: 1
    letterSpacing: "0.12em"
  tech:
    fontFamily: Audiowide
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: "0.06em"
rounded:
  sm: 3px
  md: 6px
  lg: 10px
  pill: 999px
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
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: 16px
  button-secondary-hover:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.primary-hover}"
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
    textColor: "{colors.primary}"
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
    textColor: "{colors.primary}"
    typography: "{typography.body}"
---

# Retro Anime

## Overview

Eighties anime key art, at the hour the neon comes on. A deep indigo night is the ground; the
sunset is a band across the top of the page; magenta is the one action colour and cyan is the
technology. The kit is built from five reference illustrations of the genre, and **every palette
value is the median sampled from those images** rather than an estimate — the sampled set is
`#19152b` indigo night · `#622c80` violet sky · `#bb4085` magenta · `#44a6d7` cyan neon ·
`#faa071`/`#ffb57b` gold horizon. Where a token had to move for contrast it was moved in the
accent's own family and recorded in `README.md`.

The register is warm nostalgia rendered in cold light: saturated, cinematic, unapologetically
neon, but with the flatness of a printed poster rather than the gloss of a dashboard. Type is
Audiowide for the wide 80s technical display, Rajdhani for the condensed humanist body, and
Share Tech Mono for machine labels.

## Colors

Magenta `#ec4b8f` is the primary action colour — the neon sign doing the persuading, and the
only saturated object most pages will contain. Cyan `#44a6d7` is the second accent and belongs
to *technology*, not to action: media panels, progress, focus, charts. Gold `#ffb57b` is the sun
and appears in the sky ramp, never as a control colour.

The night is `#19152b`, a violet-black rather than a neutral one — the references never contain a
grey, and a neutral black would flatten the warm/cool tension the whole genre depends on.

Because the fill magenta is only 5.2:1 against dark ink and far less as a label, text-magenta
ships separately: `--accent-ink` and `--accent-ink-hover` exist so eyebrow, links, active nav and
badge labels can be magenta family without failing contrast.

## Typography

Audiowide is deliberately the **display face only**. Its 1970s-technical, single-weight
letterforms are exactly the genre's title lettering, and they are unreadable in quantity — so
the body is Rajdhani, a condensed sans with the same engineering-drawing feel at reading size.
Share Tech Mono handles labels, metrics and code. The wide `0.12em` tracking on caps is what
makes small labels read as silkscreen rather than as body text.

## Layout

Spacing is comfortable rather than dense (`16px` gutters, `24px` between blocks) so the neon has
air around it. Corners are barely softened — `3px` to `10px` — because the references are
printed posters: geometry, not pillows. Nothing is a pill except badges.

## Elevation & Depth

Depth is **light**, not glass: `--blur: none` and panels stay flat, because a poster has no
frosted surfaces. Elevation comes from two devices instead — a magenta/base tint for nested
panels, and `--glow`, a cyan neon ring plus bloom, used sparingly on focused or active elements.
`--shadow-1`/`--shadow-2` are near-black indigo drops that read as night, not as grey.

## Shapes

The kit's geometry lives in its signature tokens rather than in its corners: the striped outrun
sun (`--retro-anime-sun`), the perspective floor grid (`--retro-anime-grid`), the px-stop sunset
ramp (`--retro-anime-sky`) and the chrome ramp (`--retro-anime-chrome`). Those four are the
genre's actual vocabulary — a sun with hard horizontal bars cutting through it, a grid running to
a vanishing point, and metal that reads as chrome because its ramp has a **dark band in the
middle**. The sun and the grid are drawn artwork (inline SVG) because neither is expressible with
repeating gradients: a bar pattern stripes the whole tile rather than the disc, and two straight
gradient families produce graph paper instead of depth. Four motifs is the ceiling — a fifth
dilutes the rest.

## Components

Buttons are magenta fills with indigo labels, or flat surfaces with magenta labels; the danger
button keeps the surface and takes vermilion text. Cards stay flat on the night with a hairline
violet border; the elevated card deepens to `--surface-2`. Inputs sit in the deepest well. Badges
are pills carrying mono caps. Media panels use the magenta and cyan ramps.

## Do's and Don'ts

- **Do** keep magenta for action and cyan for technology. Two accents, two jobs.
- **Do** let the sunset band live in the top viewport, then settle to night — a full-page gradient
  in `%` stops would show one flat colour and waste the whole idea.
- **Don't** put the gold on a control, and don't set body text over the sky band's gold stop.
- **Don't** add a third neon. The genre survives on magenta-vs-cyan; a third colour makes it a
  rainbow instead of a night.
- **Don't** round the corners further or add glass — the flatness is the poster.
