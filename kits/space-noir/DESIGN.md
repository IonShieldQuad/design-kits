---
version: alpha
name: Space Noir
description: 90s space-noir jazz poster — an inked ground, film grain, a halftone screen and one burnt-orange action.
colors:
  primary: "#c06a30"
  primary-hover: "#d67f42"
  primary-ink: "#e0904f"
  primary-ink-hover: "#eda468"
  secondary: "#2f6f68"
  tertiary: "#d9a441"
  neutral: "#1a1714"
  surface: "#1e1a17"
  surface-2: "#151311"
  text: "#ece4d6"
  text-muted: "#bdb3a4"
  text-dim: "#9c9284"
  ink: "#191210"
  success: "#8fae5f"
  error: "#cb7266"
  info: "#5c9d97"
typography:
  display:
    fontFamily: Barlow Condensed
    fontSize: 2.9rem
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: "0.005em"
  heading:
    fontFamily: Barlow Condensed
    fontSize: 1.32rem
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: "0.01em"
  body:
    fontFamily: Barlow
    fontSize: 0.98rem
    fontWeight: 400
    lineHeight: 1.55
  label:
    fontFamily: Courier Prime
    fontSize: 0.72rem
    fontWeight: 400
    lineHeight: 1
    letterSpacing: "0.14em"
rounded:
  sm: 2px
  md: 4px
  lg: 8px
  pill: 999px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
components:
  page:
    backgroundColor: "{colors.neutral}"
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 16px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary-ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 16px
  button-secondary-hover:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.primary-ink-hover}"
    rounded: "{rounded.md}"
  button-danger:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.error}"
    typography: "{typography.body}"
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
  caption:
    textColor: "{colors.text-dim}"
    typography: "{typography.label}"
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
  badge-warning:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.tertiary}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
  badge-danger:
    backgroundColor: "{colors.surface-2}"
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

# Space Noir

## Overview

Nineteen-nineties space-noir as a printed jazz poster, a decade after the ink dried. The register is
**muted, grainy and cinematic**: a warm charred-black ground, bone/cream type, a single burnt-orange
action, a muted deep teal as the cool counterpoint and a dusty red for alerts. Nothing in the kit is
saturated and nothing glows — the whole surface should look like a poster that has been through a
press, an envelope and thirty years of ultraviolet.

This is **design provenance, not a franchise.** The kit is named for the genre, not a show, and the
material here — an inked ground with film grain, a halftone dot screen, interlocking discs as poster
geometry, a perforated film strip — is the period's generic print vocabulary. No character, ship,
logotype, poster artwork or trade dress is reproduced anywhere in it.

Two ideas do the work. First, **the kit is print, not glass**: depth is a hard zero-blur offset (a
plate sitting proud of its ground), an edge is a crisp rule, and there is no blur, bloom or frosted
surface anywhere. Second, **grain and halftone are the material, not a colour**: the ground carries a
drawn film-grain tile, a drawn halftone screen sits in the media panel and in a signature tile, and
the masthead's highlight is a screened shadow rather than the lab's default radial bloom.

## Colors

Burnt orange `#c06a30` is the one action colour, and it takes **ink** as its label — an orange field
carrying near-black type (`#191210`) is the jazz-album move, and it is also the strongest contrast the
kit owns. Deep teal `#2f6f68` is the cool counterpoint and belongs to *media and data*, never to
action: media panels, charts, the `info` alert. Aged amber `#d9a441` is the kit's one warm tertiary —
it is the same tone as the warning rung, which is deliberate: in a three-colour poster, the caution
and the warm accent share a hue. Dusty red `#cb7266` is the alert colour, printed and faded so it
reads as a warning without ever being mistaken for the orange action.

The ground is a warm charred black (`#221e1a` at the top, settling to `#121110`) — a *brown* cast, not
a neutral grey and never `#000`, because the references are printed on stock that has aged warm. The
type is bone/cream `#ece4d6`, the paper's own colour, not white.

Because the orange is an excellent *fill* but only 4.7:1 as a small label, the readable member ships
separately: `--accent-ink` `#e0904f` carries every READ word — eyebrows, links, active nav, badge and
secondary-button labels — and is graded against each ground and against the accent's own 16% tint
composited over it.

## Typography

Barlow Condensed is the **display face only**: a heavy condensed grotesque whose width is the poster
punchline, used at 600–800 for headings, titles and the type scale. Barlow is the sturdy body face —
the same superfamily, a wider cut, legible in quantity — so the two voices contrast by *width* rather
than by a second temperament, which is exactly how a poster sets a shout against its standfirst.
Courier Prime is the mono: a typewriter face for swatches, labels, table headers and metrics, chosen
because the kit's small-print voice is a **print** artifact, not a terminal readout. Caps labels run
at `0.14em`, a screened poster legend rather than a UI chip.

## Layout

Spacing is poster-generous (`16px` gutters, `24px` between blocks) so the ink has air. Corners are
barely softened (`2px`–`8px`) — a printed panel is a rectangle, and the only true pill is the badge.
Every panel edge is a hairline cream rule; the "frame" in this kit is a crisp edge plus a hard
zero-blur offset, never a soft shadow.

## Elevation & Depth

Depth is **hard-edged and flat**, the way ink sits on paper. `--blur` is `none` and no panel carries a
`backdrop-filter`. Elevation is a zero-blur offset: `--shadow-1`/`--shadow-2` are dark squares pushed
3px/6px down-right under a panel, ringed by a faint cream hairline, and `--glow` — the primary
button's chrome — is a crisp ink ring plus a hard orange offset, not a bloom. Grain supplies the only
"texture": a drawn `feTurbulence` tile in `--bg` and `--media-bg` that only *darkens*, so every
contrast pair is solved against the ungrained ground and stays conservative.

## Shapes

The geometry lives in three signature tokens, each with a different job. `--space-noir-halftone` is the
**material** — a drawn dot screen whose dots grow left to right, the screened gradient of a 90s print,
expressed as base64 SVG because a radial gradient fakes a halftone as a smooth ramp. `--space-noir-discs`
is the **poster geometry** — two overlapping discs, orange and teal, cream-ringed with centre dots over
a bold baseline rule, drawn and generic, a poster device rather than a mark or a logo. `--space-noir-film`
is the **frame** — a perforated film band with two rows of sprocket holes and hard frame dividers,
joining the print material to the film material. Three motifs, three jobs; a fourth would dilute them.

## Components

Buttons are burnt-orange fills with ink labels, or flat surface plates with lifted-orange labels; the
danger button keeps the surface and takes dusty-red text. Cards stay flat on the ink with a cream
hairline; the elevated card deepens to `--surface-2` and gains the larger hard offset. Inputs sit in
the deepest well, recessed by a zero-blur inset. Badges are pills carrying Courier Prime caps, sitting
on `--surface-2`. Media panels are the one place the kit shows a *surface* rather than a colour: a
halftone screen and grain over a muted orange→rust→teal press ramp, opaque.

## Do's and Don'ts

- **Do** keep burnt orange for action and deep teal for media and data. Two accents, two jobs.
- **Do** let the grain and the halftone carry the texture — they are the kit, not decoration.
- **Do** use ink (`--text-invert`) on the orange fill; cream on orange fails, and ink is the poster.
- **Don't** add a third saturated colour. The palette survives on one warm action and one cool
  counterpoint; a third makes it a rainbow instead of a poster.
- **Don't** round the corners further, add a blurred shadow, or introduce glass — the flatness *is*
  the print.
- **Don't** brighten the teal into neon. It is a counterpoint, not a light source.
