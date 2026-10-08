---
version: alpha
name: Kawaii
description: "A pastel sticker sheet: bubblegum pink, lilac and mint grounds, one candy accent, 28px radii with pills everywhere, and drawn sparkle, heart and confetti stickers."
colors:
  primary: "#ff6fb2"
  primary-hover: "#ff86c1"
  on-primary: "#4a1738"
  primary-ink: "#ab1559"
  primary-ink-hover: "#8f104b"
  secondary: "#35c79a"
  tertiary: "#c9a6ff"
  accent-tint: "#fcdaec"
  neutral: "#fff2f9"
  surface: "#ffffff"
  surface-2: "#fbeef7"
  text: "#3b2743"
  text-muted: "#5f4a68"
  text-dim: "#634e6c"
  success: "#0d7a57"
  warning: "#946000"
  error: "#bd2d28"
  info: "#4f52c9"
  focus: "#7d5bd6"
  border: "#eadee8"
typography:
  display:
    fontFamily: Baloo 2
    fontSize: 2.8rem
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: "-0.005em"
  heading:
    fontFamily: Baloo 2
    fontSize: 1.28rem
    fontWeight: 600
    lineHeight: 1.2
  body:
    fontFamily: Nunito
    fontSize: 0.95rem
    fontWeight: 500
    lineHeight: 1.6
  label:
    fontFamily: JetBrains Mono
    fontSize: 0.72rem
    fontWeight: 500
    lineHeight: 1
    letterSpacing: "0.10em"
rounded:
  sm: 12px
  md: 18px
  lg: 28px
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
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: 14px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.pill}"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary-ink}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: 14px
  button-secondary-hover:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.primary-ink-hover}"
    rounded: "{rounded.pill}"
  button-danger:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.error}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
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
  card-body:
    textColor: "{colors.text-muted}"
    typography: "{typography.body}"
  card-media:
    backgroundColor: "{colors.secondary}"
    rounded: "{rounded.md}"
    height: 96px
  input:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 12px
  badge:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text-dim}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: 5px
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
  badge-info:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.info}"
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
  progress-bar:
    backgroundColor: "{colors.secondary}"
    rounded: "{rounded.pill}"
    height: 8px
  page:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.text}"
  spot-illustration:
    backgroundColor: "{colors.tertiary}"
    rounded: "{rounded.lg}"
    size: 96px
  divider:
    backgroundColor: "{colors.border}"
    height: 1px
  focus:
    textColor: "{colors.focus}"
---

# Kawaii

## Overview

Kawaii is a **pastel sticker sheet**. Four soft grounds — pink, lilac, mint and cream — carry a
single bubblegum action colour, and the shape language, not the hue, is what identifies the kit:
12/18/28px radii, pills on every chip, bar, toggle and avatar, soft plum-tinted shadows, and a
bouncy overshoot ease so controls pop instead of gliding. Type is a chunky rounded display
(Baloo 2) over a rounded soft body (Nunito), with a friendly mono for labels.

It exists because this library had three light, soft kits and none of them was *playful*.
`sakura` is a spring day — saturated blossom pink against living leaf green, drawn in measured,
elegant strokes. `city-pop` is an airbrushed 80s Tokyo sleeve, cream and coral and teal.
`glorious-morning` is first light — dawn gold on clear sky, energetic and open. All three are
*pretty*. Kawaii is the opposite register on purpose: it is **cute**, it wears stickers, and a
screen that reads as elegant is a screen where this kit has failed. The motifs make that
explicit — a four-point sparkle, a die-cut heart and a confetti field — where the other three
kits show a sun, a petal drift and a light ray.

## Colors

The pastels are grounds, not decorations. Pink `#fff2f9`/`#fbdcf0`, lilac `#eadffd` and mint
`#daf3e6` are the page wash, and **the palest stop is the one that binds**: `--surface` is pure
`#ffffff`, so every caption, hint and label is graded against white, not against the flattering
pink stop. Everything is inked in **deep plum** (`#3b2743`), never grey — a grey ink on a pastel
ground is exactly what makes a light theme read as corporate rather than cute.

There is **one candy accent**: bubblegum `#ff6fb2`. It is a fill and only a fill — as a small
label on white it is 2.57:1 — so accent-as-text ships separately as `#ab1559`, and that value is
graded *both* on every ground and on its own 16% `--accent-soft` tint composited over the
surface (the pastel-badge case that shipped unreadable in nine kits of this library). Because the
fill is a pastel, buttons take **dark** labels: `--text-invert` is a deep berry `#4a1738` at
5.55:1 on the bubblegum, where white would be 2.57:1 and vanish.

A pastel fill cannot carry a status, so `--ok`, `--warn`, `--danger` and `--info` are deepened
until each clears 4.5:1 on `--surface-2`, the ground badges and alerts actually sit on.

## Typography

**Baloo 2** is the display face: a chunky, bubbly rounded grotesque whose counters are round at
large sizes — it *is* sticker lettering. **Nunito** is the body: rounded, warm, and still legible
at 12–13px, which is where Quicksand's thin geometric strokes go spindly and Fredoka's wide
shapes cost a line. **JetBrains Mono** handles chips, labels and code; it is deliberately a
*friendly* monospace, because a technical mono would pull the small type back toward "dashboard".
Caps tracking is a modest `0.10em` — the chips are cute, not shouted.

## Layout

Spacing is comfortable and nothing is dense: 16px gutters, 24px between blocks, 18px card
padding. The defining layout fact is **roundness**: the smallest radius in the kit is 12px and
every interactive control is a pill. Radio and checkbox are explicitly rounded through the
`--check-*` capability, because native controls ignore `border-radius` and would otherwise ship
as the only square thing on the page — a visible break of the kit's one absolute rule.

## Elevation & Depth

Depth is **soft, wide and plum-tinted**: a pastel drop shadow, because a neutral-grey shadow on a
pastel page reads as grime. Two shadow steps plus a candy `--glow` (the pink lift under the
primary button) are all the depth the kit has. `--blur` is `none` — sticker paper is matte, and
frosted glass is `glass`'s territory. `--btn-shadow` reaches every button variant so all five
read as the same lifted sticker, and inputs take a soft `--input-inset` well so a field looks
pressed into the sheet.

## Shapes

The shape language is the identity. Corners are huge, pills are everywhere, and nothing is
chamfered. Three **drawn** motifs carry the genre's vocabulary: the four-point **sparkle** (a
concave star, which no gradient can make), the **die-cut heart** (a filled shape with a white
outline and a specular highlight), and the **confetti field** (dots, tiny stars and a tiny heart
tiled at unequal sizes). Each is an inline SVG in base64 — never hand-percent-encoded, which
double-encodes `#` and fails silently as a blank tile — and each carries its own base layer so no
tile shows only the kit's flat surface.

## Components

Buttons are bubblegum pills with deep-berry labels, or white pills with candy-pink labels; the
danger button keeps the white surface and takes a distinctly red text so "delete" never reads as
the action. Cards are white sticker paper on the pastel ground with a 2px plum-pink outline and a
28px radius; the elevated card sits on the pink inset tint. Media panels use a drawn pastel
sticker sheet rather than a generic accent ramp. Badges are pills: muted plum on the pink tint,
or candy-pink text on the composited accent tint. Links and eyebrows route through
`{colors.primary-ink}` so the fill is never used as a label.

## Do's and Don'ts

- **Do** keep the candy accent for action only, and route every label through `primary-ink`.
- **Do** give buttons **dark** labels. A pastel fill takes deep berry ink; white on `#ff6fb2` is
  2.57:1 and disappears.
- **Do** let the motifs be seen. They are drawn shapes on their own base layers, not sheens or
  washes that vanish at 168×72.
- **Don't** round anything less or square anything off. The pills and the huge radii are the kit
  — a 4px corner turns it back into a generic pastel theme.
- **Don't** reach for a second saturated colour or a third "look at me" accent. The pastels are
  grounds, `--accent-2` (mint) is structural only, and the one candy pink does all the persuading.
- **Don't** make it elegant. If a screen comes out tasteful and restrained, it is `sakura`,
  `city-pop` or `glorious-morning` — not this kit.