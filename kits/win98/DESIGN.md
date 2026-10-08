---
version: alpha
name: Windows 98
description: Windows 95/98 desktop chrome — a single grey plastic face, hard two-tone 3D bevels, one navy gradient title bar.
colors:
  primary: "#000080"
  primary-hover: "#0000a0"
  primary-ink: "#ffffff"
  secondary: "#008080"
  tertiary: "#0a4fa0"
  neutral: "#c0c0c0"
  surface: "#d4d0c8"
  surface-2: "#ffffff"
  text: "#000000"
  text-muted: "#333333"
  text-dim: "#3a3a3a"
  border: "#808080"
  border-strong: "#000000"
  success: "#008000"
  warning: "#6b6b00"
  error: "#800000"
  info: "#1c5fb0"
typography:
  display:
    fontFamily: Silkscreen
    fontSize: 2.9rem
    fontWeight: 700
    lineHeight: 1.06
    letterSpacing: "0.02em"
  heading:
    fontFamily: Silkscreen
    fontSize: 1.3rem
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "0.01em"
  body:
    fontFamily: Public Sans
    fontSize: 0.95rem
    fontWeight: 400
    lineHeight: 1.55
  label:
    fontFamily: VT323
    fontSize: 0.9rem
    fontWeight: 400
    lineHeight: 1
    letterSpacing: "0.06em"
  mono:
    fontFamily: VT323
    fontSize: 0.95rem
    fontWeight: 400
    lineHeight: 1.5
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
    rounded: "{rounded.sm}"
    padding: 12px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.primary-ink}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    padding: 12px
  button-secondary-hover:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.primary-hover}"
    rounded: "{rounded.sm}"
  button-danger:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.error}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    padding: 12px
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.sm}"
    padding: 18px
  card-elevated:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text}"
    rounded: "{rounded.sm}"
    padding: 18px
  card-title:
    textColor: "{colors.text}"
    typography: "{typography.heading}"
  card-media:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    height: 96px
  card-media-2:
    backgroundColor: "{colors.secondary}"
    rounded: "{rounded.sm}"
    height: 96px
  title-bar:
    backgroundColor: "{colors.tertiary}"
    textColor: "{colors.primary-ink}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    height: 24px
  input:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 10px
  badge:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text-muted}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    padding: 4px
  badge-accent:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.primary}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
  badge-success:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.success}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
  badge-warning:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.warning}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
  badge-info:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.info}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
  alert-info:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.info}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 14px
  alert-error:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.error}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 14px
  table-header:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text-dim}"
    typography: "{typography.label}"
  divider:
    backgroundColor: "{colors.border}"
    height: 2px
  divider-strong:
    backgroundColor: "{colors.border-strong}"
    height: 2px
  link:
    textColor: "{colors.primary}"
    typography: "{typography.body}"
  link-hover:
    textColor: "{colors.primary-hover}"
---

# Windows 98

## Overview

The last great desktop chrome before gradients learned to blur. This kit is built from
exactly three materials: one moulded grey plastic face (`#c0c0c0`), a hard two-tone 3D bevel
that raises or sinks every control, and a single navy gradient title bar for the thing that is
active. There is no soft light anywhere. A raised edge is a 1px white line against a 1px
near-black line — hard, adjacent, unblurred — which is what a 1998 UI actually drew and what
makes the whole thing still read as *physical* twenty-five years later.

The palette is the 16-colour VGA family the OS shipped with: control grey `#c0c0c0`, caption
navy `#000080`, and the teal `#008080` desktop a window sat on. Nothing has been invented where
a historical value existed; where a value had to move for legibility on the white well (the
olive "yellow", the alert red) it moved within its own family and the move is measured in the
README.

The register is deliberately plain-spoken. It is a skin for tools and nostalgia, not a poster —
grey chrome, black ink, and one blue bar that tells you where you are.

## Colors

Navy `#000080` is the single action colour: the primary button, the active nav item, links,
and the title bar. It is unusual among accents in that it is dark enough to be legible as a
*label* as well as a fill — 8.8:1 on the grey face and 16:1 on the white well — so
`--accent-ink` is the same navy rather than a separately darkened cousin. The hover step
(`#0000a0`) stays a navy on purpose: a brighter Windows blue like `#1084d0` is 2.2:1 against
grey and would disappear the moment it was used as text.

Teal `#008080` is the second accent and is a *ground*, not an action: it is the desktop, and it
reappears only in media plates, the second stop of a progress bar, and the charts. Neutral grey
`#c0c0c0` is the page itself.

The third surface is the important one. Fields, code, and every inset are pure white
`#ffffff` — a text field was a recess milled into the grey shell, and it was white. That is a
light-inside-light stack, so the `--text-on-surface-2*` tier is declared explicitly: inset text
is black and its muted tier is `#333333`, both measured against the well rather than inherited
from the page.

`tertiary` is not a third action colour: it is the *mid stop of the title-bar ramp*
(`#0a4fa0`, between the dark navy and the bright steel blue). It is recorded so the caption's
gradient ends are in the palette, and it is the one blue in the kit that still carries white ink
comfortably (7.9:1).

## Typography

Three faces, three jobs. **Silkscreen** is the bitmap caption face — it is what a window title
and a menu label should feel like, and it is unreadable in paragraphs, so it is confined to
display sizes and never to body copy. **Public Sans** is the body: a neutral UI grotesque that
stands in for MS Sans Serif, because a bitmap face at 15px body size is a legibility failure,
not authenticity. **VT323** is the terminal — metrics, table headers, silkscreen labels, code —
the DOS-VGA texture of a `dir` listing.

Small labels sit at `0.06em` tracking so they read as stamped chrome rather than as shrunken
prose. Nothing in the kit's own scale goes below `0.9rem` (~14.4px); UI chrome stays above the
legibility floor.

## Layout

Spacing is a tight 4/8/16/24/40 ladder — a 1998 dialog was dense, not airy, and the grey face
is at its best when controls crowd it the way a real toolbar did. Corners are **square**: every
radius token is `0`. A single rounded corner would break the illusion instantly, so badges are
squares too and the pill token is deliberately zero.

## Elevation & Depth

Depth is a *bevel*, never a shadow. `--shadow-1` and `--shadow-2` hold **inset** two-tone
constructions — white on the top-left, near-black on the bottom-right, with the classic
`#dfdfdf` / `#808080` inner step — so the generator applies a real 3D edge rather than painting
a soft drop. `--shadow-2` adds a *hard* 2px offset block (`2px 2px 0`) for floating dialogs,
because a 1998 popup cast a solid shadow, not a blur. Recessed fields get the inverse
construction through the opt-in `--input-inset`: grey-then-black on the top-left, white on the
bottom-right, the exact milled well a text field was.

`--blur` is `none`, always. Nothing here is glass. The name `--glow` is the contract's; its
value is ours — it carries the raised *navy* bevel the lab wires to the primary button, so the
action appears to catch the light rather than to emit any. No smooth surface survives: the
masthead wash (`--wash`) is the flat face colour, and the media panel is the 2px navy/grey
**dither** (`--media-bg` at full `--media-op`), the desktop wallpaper's own texture.

## Shapes

The kit's geometry is four tokens, each a different job. `--win98-titlebar` is the active
caption: dark navy sweeping to the bright steel blue with a 1px white gloss line along the top,
hard-banded rather than blended. `--win98-desktop` is the teal ground, dithered at 45° so the
tile is never a flat plate. `--win98-bevel-out` and `--win98-bevel-in` are the two directions of
the same bevel — a control cut proud of the face, and a field milled into it — drawn as literal
2px edges rather than as shadow tokens, so they can be dropped onto any element as a
`background`. Four is the ceiling; a fifth would dilute them.

## Components

Buttons are grey faces with a hard raised bevel or navy fills with a raised *navy* bevel; the
danger button keeps the grey and takes maroon text. Cards are the lighter `#d4d0c8` face — a
part sitting on the desktop — and the elevated card is the white well with a hard offset
shadow, a floating dialog. Inputs are white recesses with `--input-inset`. Badges are square
chips in VT323 caps. Alerts are white wells with a 3px coloured left edge, the one place a
status colour appears at full height. The table header is a white well with dim text, like a
column header row in an Explorer list view.

## Do's and Don'ts

- **Do** keep depth as hard two-tone bevels. If you find yourself reaching for `box-shadow`
  with a blur radius, you have left the kit.
- **Do** keep everything square. The geometry is the identity.
- **Do** let navy be the only action colour and teal be the only ground accent.
- **Don't** use a brighter Windows blue (`#1084d0`) as text — it is 2.2:1 on grey and vanishes.
- **Don't** add a third surface tone or a soft shadow; the kit has one face, one well, one bevel.
- **Don't** set Silkscreen or VT323 below the label size — bitmap faces disintegrate small.
