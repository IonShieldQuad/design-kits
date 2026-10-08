---
version: alpha
name: Retro Anime
description: A light, high-key pastel kit with cel-shaded depth — cream ground, navy ink, a deep rose action and sky-blue structure, and four drawn celestial motifs.
colors:
  primary: "#c53a68"
  primary-hover: "#b2335e"
  primary-ink: "#ae2a5e"
  primary-ink-hover: "#94214f"
  secondary: "#3f7fd0"
  tertiary: "#a87d2a"
  neutral: "#fdf7ee"
  surface: "#fffdf8"
  surface-2: "#f5eef4"
  text: "#1e2749"
  text-muted: "#414c72"
  text-dim: "#49547b"
  text-invert: "#fff8f0"
  accent-tint: "#eed5e0"
  night: "#1b2350"
  success: "#1f7a5a"
  warning: "#8f6410"
  error: "#bd3a22"
  info: "#2b6fb5"
typography:
  display:
    fontFamily: Shippori Mincho
    fontSize: 2.7rem
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: "0em"
  heading:
    fontFamily: Shippori Mincho
    fontSize: 1.3rem
    fontWeight: 600
    lineHeight: 1.25
  body:
    fontFamily: Nunito Sans
    fontSize: 0.95rem
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: IBM Plex Mono
    fontSize: 0.72rem
    fontWeight: 400
    lineHeight: 1
    letterSpacing: "0.16em"
rounded:
  sm: 5px
  md: 9px
  lg: 14px
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
    textColor: "{colors.primary-ink-hover}"
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
    backgroundColor: "{colors.night}"
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
    backgroundColor: "{colors.accent-tint}"
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
    textColor: "{colors.warning}"
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
    textColor: "{colors.text-dim}"
    typography: "{typography.label}"
  link:
    textColor: "{colors.primary-ink}"
    typography: "{typography.body}"
  rule:
    backgroundColor: "{colors.tertiary}"
    height: 2px
---

# Retro Anime

## Overview

Nineties shoujo magical-girl anime, as a design language: a high-key pastel key art, a
crescent moon and a field of stars, ribbons and sparkle, and a gold trim — all drawn in the flat
cel-shaded fills of the era. The register is the *title card and the transformation sequence*:
romantic, celestial and unapologetically decorative, but built so a real page stays legible.

The ground is a warm **cream/ivory that cools toward a pale night-sky lavender**, never pure
white — the page is a night sky that has not gone dark. Deep **navy** is the ink, a **blush
rose** and a **sky blue** are the two working accents, and a flat cel-animation **gold** is the
trim. Every motif is generic celestial vocabulary (a face-free crescent, a four-point sparkle, a
ribbon bow, a starfield); none is a specific series, character, costume or logo.

Depth is **cel shading**, not shadow: flat fills with one hard second tone, hard-edged zero-blur
offsets, and crisp 2px outlines. There is no soft drop shadow and no bloom in the kit.

## Colors

The **rose** `#c53a68` is the single action colour — the ribbon the whole kit is drawn in. It is
deep on purpose: a pastel blush is only ~2.6:1 as a label and cannot carry a cream label as a
fill, so the *tint* blush lives in `--accent-soft` and the motif tiles, while the working action
is this deeper rose.

The **sky blue** `#3f7fd0` is the second accent and belongs to *structure and the night*, not to
action: media, progress, focus, charts. The **gold** `#a87d2a` is trim — a flat cel ochre, not a
metal — and appears as a rule, the knot of the ribbon, and the lit star of the media scene.

The page ground is **cream** `#fdf7ee` cooling to lavender `#eef4fb`; the card is warm ivory
`#fffdf8`. No grey appears anywhere in the kit — a grey on a cream page reads as an office
document, and the whole premise here is a night sky.

Because the rose fill cannot be a label, text-rose ships separately: `--accent-ink` `#ae2a5e`
(and `--accent-ink-hover` `#94214f`) carry the eyebrow, links, active nav, the secondary-button
label and badge labels.

## Typography

**Shippori Mincho** leads the display stack: a Japanese Mincho serif, which is the elegant,
slightly retro letterform of a 90s title card and a voice no other kit in the library uses. It is
a *display* face only — set a long paragraph in it and the page becomes a poster, so the body is
**Nunito Sans**, a clean humanist sans that stays readable down to 12px. **IBM Plex Mono** is the
light machine voice for chips, table headers and code. The wide `0.16em` tracking on caps is what
makes a small label read as a title-card credit line rather than as body text.

## Layout

Spacing is comfortable (`16px` gutters, `24px` between blocks) so the celestial motifs have room.
Corners are softened, never round and never square — `5px`/`9px`/`14px` — because an animation cel
is a soft-edged frame; a pill is reserved for badges and avatars only. Nothing is chamfered: cel
shading cuts nothing.

## Elevation & Depth

Depth is **cel shading**. Every elevation is a hard-edged, zero-blur offset in a cool navy-shadow
tone — the **cel plate** (`4px 4px 0`, `6px 6px 0`) — never a blurred drop. Fills are two-tone
with a hard break: the crescent is split by a straight lit/shadow edge through a clip, the ribbon
loops carry a fold line, and the night skies are two hard bands. `--blur` is `none`: a cel is
opaque film, not frosted glass. The one "lit" object is the primary button, whose `--glow` is not
a bloom but a hard rose ring stacked on the same cel offset.

## Shapes

The kit's geometry lives in four **drawn** signature tokens rather than in its corners: the
the crescent moon (`--retro-anime-moon`), the shoujo sparkle (`--retro-anime-sparkle`), the ribbon bow (`--retro-anime-ribbon`) and the starfield (`--retro-anime-starfield`). Each is inline SVG (base64)
because a crescent, a concave four-point star, a swallowtail ribbon and a banded night sky are
geometry no gradient family produces — a radial ring reads as a bullseye and a lone spiral as a
rosette. The media panel takes the same night sky at full width as the card's one big celestial
moment, and the masthead wash is two soft pastel lights (a blush and the sky) over the page's own
ground.

## Components

Buttons are rose fills with a **cream** label, or flat ivory surfaces with a rose label; the
danger button keeps the surface and takes a true vermilion red, held a clear 29° of hue off the
rose so a destructive action never reads as the accent. Every button is the same cel plate
(`--btn-shadow`) except the primary, which also wears the hard rose ring. Cards sit flat on the
ground with a crisp 2px navy outline and the cel offset; the elevated card deepens to
`--surface-2`. Inputs are the blush inset with a hard 2px top press. Badges are pills carrying
mono caps, the accent badge on the rose tint. Media panels are the night: a navy field with a
crescent and a sparkle field.

## Do's and Don'ts

- **Do** keep the ink navy and the action rose. Two accents, two jobs.
- **Do** express depth as a hard offset or a hard two-tone fill, never as a blur.
- **Don't** lighten the rose to a pastel for the button fill — a pastel fill cannot carry a cream
  label, and the tint is what `--accent-soft` is for.
- **Don't** put the gold behind small text; it is trim, and `--warn` is the inked status.
- **Don't** round past `14px` or pill a control — that is `kawaii`, not this kit.
