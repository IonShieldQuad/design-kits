---
version: alpha
name: Pixel DMG
description: The Game Boy DMG — a reflective monochrome LCD carrying four shades of green, dithered into a whole interface.
colors:
  primary: "#0f380f"
  primary-hover: "#1c4f1c"
  primary-ink: "#b6d313"
  secondary: "#8bac0f"
  tertiary: "#306230"
  neutral: "#9bbc0f"
  surface: "#b4d212"
  surface-2: "#9bbc0f"
  text: "#082608"
  text-muted: "#0f380f"
  text-dim: "#1a481a"
  success: "#0f380f"
  warning: "#174117"
  error: "#0a2a0a"
  info: "#1c4a1c"
typography:
  display:
    fontFamily: Press Start 2P
    fontSize: 2.4rem
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: "0.01em"
  heading:
    fontFamily: Silkscreen
    fontSize: 1.2rem
    fontWeight: 700
    lineHeight: 1.3
  body:
    fontFamily: Silkscreen
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: VT323
    fontSize: 1.05rem
    fontWeight: 400
    lineHeight: 1
    letterSpacing: "0.1em"
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
    textColor: "{colors.text}"
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
  card-media-2:
    backgroundColor: "{colors.tertiary}"
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
    textColor: "{colors.primary}"
    typography: "{typography.body}"
---

# Pixel DMG

## Overview

The Game Boy DMG, at four shades of green. A reflective monochrome LCD behind a
green polariser is the entire world of this kit: a pale lit field, a handful of
dark inks, and **nothing else** — no second hue, no saturation to spend, no
gradient that is not a hard-stop dither or a ramp between two of the four
shades. Every decision a designer normally makes with colour has to be made with
*distance in luminance* instead.

The kit is built on the machine's canonical palette — `#0f380f` ink, `#306230`
mid, `#8bac0f` light-mid, `#9bbc0f` LCD — and is honest about where that palette
had to be extended. The darkest canonical shade reaches only **6.02:1** on the
lightest, below the 7:1 the contract asks of body text; a reflective LCD has no
backlight above `#9bbc0f`. So the kit derives one deeper ink and a *lit ladder*
above the field, records both, and uses nothing else.

Nothing in the kit is smooth. Radii are `0px`, every shadow is a zero-blur
offset block, every gradient is a hard-stop dither, artwork is drawn small and
scaled up with `--pixel-render`, and the page ground is a **pixel-art
landscape** rather than a fading fill.

## Colors

`#0f380f` is the action colour — the machine's own ink, used as a **fill** for
the primary button, the toggle and the progress bar. It is dark enough to carry
the lit LCD green `#b6d313` at 7.73:1, so accent-as-text and accent-as-fill are
the same value; only a hover step (`#082808`) was needed.

The ground is the LCD, drawn as a pixel landscape: a bright `#d4f41d` sky, a
stepped pixel sun, blocky `#b6d313` clouds, a hard `#9bbc0f` horizon slab, and a
dithered `#9bbc0f`/`#aed011` ground that continues to the foot of the page. The
landscape is confined to the **lit ladder** on purpose: even the canonical
light-mid `#8bac0f` (L .3503) drops `--text` to 6.2:1, so no ink shade is ever
allowed under type. `--surface` (`#b4d212`) is one lift above the field — a card
catching the room light — and `--surface-2` (`#9bbc0f`) is the inset.

The subtlety that governs everything is `--text-dim`. On a pale field a
mid-green is fatal: `#306230` scores 3.29:1 and fails the 4.55:1 floor. Dim text
must be **dark** — `#1a481a` (4.83:1 minimum) — and `#306230` is spent on rules
and focus instead, never on type.

## Typography

Three pixel faces, three jobs. **Press Start 2P** is the 8×8 arcade headline
face, used only where a title should shout — it is square and enormously wide,
so it is never set as body. **Silkscreen** (a 5×5 grid) carries body and
headings. **VT323** is the narrow terminal face for data, labels and code, where
it stays legible small. `--tracking-caps` is `0.1em`; display tracking stays
positive (`.01em`) because the pixel faces are already wide.

## Layout

Spacing is comfortable (`16px` gutters, `24px` blocks) so the chunky frames have
air. The shape language is absolute: **every corner is a right angle**. There is
no radius at all (`--radius-*: 0px`) and no chamfer (`--cut: 0px`), because
pixels are 90 degrees and any curve betrays the medium. Borders are `2px` and
**opaque** — a pixel frame is a solid rule, not a translucent hairline.

## Elevation & Depth

Depth is a **hard offset block**, never a blur: `--shadow-1` and `--shadow-2`
are `4px`/`6px` solid drops with zero blur radius, because a blurred shadow
would introduce anti-aliased grey — a fifth colour — into a four-shade palette.
The primary button wears a chunky pixel bevel (`--glow`, `inset` highlights top
and bottom) rather than a bloom, fields get a hard inset (`--input-inset`), and
the media panel is a hard-stop dither (`--media-bg`) at full opacity
(`--media-op: 1`) rather than the lab's smooth two-stop default. `--blur` is
`none`, and the masthead paints nothing over the ground (`--wash: transparent`).

## Shapes

The kit's geometry lives in its **pixel-art ground** and its three signature
motifs. The ground (`--bg`) is a 160×90 SVG — sky, dither, stepped sun, clouds,
horizon, dithered ground — stretched to full width so its pixels stay square,
with `--pixel-render: pixelated` keeping them crisp; a hard-stop checkerboard
carries the field below. The motifs, all from the four shades: the **dither**
(`--pixel-dmg-dither`, a 2px checkerboard — the machine's own trick for faking a
shade), the **dot-matrix** (`--pixel-dmg-dotmatrix`, a 1px rule every 4px on both
axes, the LCD's grain), and the **sprite** (`--pixel-dmg-sprite`, a pixel heart
drawn as an inline SVG, because a glyph is not a gradient). Each does a different
job — scene, shading, icon.

## Components

Buttons are ink fills with lit-green labels, or flat surfaces with ink labels;
the danger button keeps the surface and takes the deepest green. Cards are the
lifted `--surface` with a 2px mid-green frame and a hard drop; the elevated card
drops to `--surface-2`. Inputs sit in the deepest well with a hard inset shadow.
Badges are square stamped tiles in mono caps. Status is a **depth of green**
(danger deepest, info lightest) and is always labelled.

## Do's and Don'ts

- **Do** make every distinction a change in luminance. Hue is not available.
- **Do** keep dim text dark (`#1a481a`); a mid-green on the pale field fails.
- **Do** name status in words or an icon — never lean on green-vs-green alone.
- **Don't** add a fifth green, or any second hue; four shades is the whole point.
- **Don't** blur anything or round a corner; both betray the medium.
- **Don't** set Press Start 2P as body text — it is a headline face only.
