---
version: alpha
name: Tropical Breeze
description: A warm coastal afternoon — sand and sea-foam ground, sea turquoise, palm green, one coral pop.
colors:
  primary: "#cc3f26"
  primary-hover: "#b33620"
  primary-ink: "#a8291a"
  primary-ink-hover: "#8c2013"
  secondary: "#0fae9e"
  tertiary: "#257043"
  neutral: "#f6f3e6"
  surface: "#fffdf7"
  surface-2: "#f2efe1"
  text: "#16342c"
  text-muted: "#3d5a50"
  text-dim: "#4f6b60"
  text-invert: "#fffaf0"
  success: "#257043"
  warning: "#8a5a10"
  error: "#b3243a"
  info: "#1f6f9e"
  accent-tint: "#f8e4dc"
typography:
  display:
    fontFamily: Baloo 2
    fontSize: 2.9rem
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: "-0.01em"
  heading:
    fontFamily: Baloo 2
    fontSize: 1.32rem
    fontWeight: 650
    lineHeight: 1.2
    letterSpacing: "-0.005em"
  body:
    fontFamily: Nunito
    fontSize: 0.98rem
    fontWeight: 400
    lineHeight: 1.55
  label:
    fontFamily: DM Mono
    fontSize: 0.72rem
    fontWeight: 400
    lineHeight: 1
    letterSpacing: "0.13em"
  code:
    fontFamily: DM Mono
    fontSize: 0.84rem
    fontWeight: 400
    lineHeight: 1.6
rounded:
  sm: 8px
  md: 14px
  lg: 22px
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
    typography: "{typography.body}"
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
    backgroundColor: "{colors.secondary}"
    rounded: "{rounded.md}"
    height: 96px
  input:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 10px
  hint:
    textColor: "{colors.text-dim}"
    typography: "{typography.label}"
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
  badge-error:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.error}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
  badge-info:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.info}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
  frond-mark:
    backgroundColor: "{colors.tertiary}"
    rounded: "{rounded.md}"
    height: 68px
    width: 68px
  table-header:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text-dim}"
    typography: "{typography.label}"
  alert-info:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text-muted}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 14px
  alert-error:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text-muted}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 14px
  link:
    textColor: "{colors.primary-ink}"
    typography: "{typography.body}"
---

# Tropical Breeze

## Overview

Mid-afternoon on a coast: dry sand underfoot, the sea in front of it, a palm leaning in from the
corner, one low sun. This is a **warm, playful holiday**, not a minimal spa — the page is allowed
to be cheerful, rounded and saturated, and it is built so it never becomes a rainbow or a neon sign.

The ground is the scene itself. `--bg` is a px-stopped gradient that cools to sea-foam at the top
of the page and warms to sand at the foot of it, so the first viewport is sky-coloured and the
bottom of a long page is beach. Cards are clean warm paper, insets are pale dry sand.

Three structural hues sit under one accent. **Sea turquoise** (`#0fae9e`) owns water, data, media
and progress. **Palm green** (`#257043`) owns the kit's plant life — the frond motif and the success
tier. **Coral** (`#cc3f26`) is the single action colour and the only saturated object a page will
contain. There is no grey anywhere: greys belong to `zen-garden`, and crimson belongs to `city-pop`.

## Colors

Coral `#cc3f26` is the primary: a warm, orange-leaning tomato — a hibiscus, deliberately a hue
away from city-pop's crimson (`#d62f4b`). It is graded as a **fill**, which is why it sits darker
than the day is bright: a cream label (`--text-invert` `#fffaf0`) clears 4.69:1 on it, but coral as
a small label is only ~4.8:1 and worse on its own tint, so text-coral ships separately as
`--accent-ink` `#a8291a` (6.08:1 at worst on a solid ground, 5.10:1 on its own 13% tint).

Turquoise `#0fae9e` is the second accent and belongs to the sea and to state — media panels,
progress, focus, charts. It is bright by design and is **never used as text**: `--info` `#1f6f9e`
carries the text-safe blue. Palm green `#257043` is the third structural hue and doubles as
`--ok`, so success is not an afterthought bolted onto the palette — it is the frond's own colour.

The ink is a deep palm-shadow green `#16342c`, not a neutral charcoal: a neutral would pull the
page straight back toward the restrained register this kit is not. The warm sand `#f6f3e6` is the
neutral ground; `--surface-2` `#f2efe1` is the dry-sand inset that badges, inputs and code sit in.

Status colours are held off the brand hues so a status reads as a signal rather than as decoration:
ochre `#8a5a10`, a deep berry `#b3243a`, and the shallow-sea blue `#1f6f9e`.

## Typography

Baloo 2 is the display face — a warm, rounded, slightly chunky letterform that carries the holiday
without tipping into novelty script. Nunito is the body: it shares Baloo 2's rounded terminals, so
the page reads as one voice at two weights, and it stays legible in quantity. DM Mono takes labels,
metrics and code, spaced `0.13em` in caps so a small label reads as a painted beach sign.

One caveat encoded here: Baloo 2's rounded weights are generous, so display tracking is held at
`-0.01em` and never tighter — over-tightening a rounded face closes its counters and it stops
looking friendly.

## Layout

Spacing is airy (`16px` gutters, `24px` between blocks) — the brief is a breeze, so nothing is
packed. The whole page is soft: radii run `8px`–`22px`, with one pill reserved for badges. Nothing
is notched and nothing is sharp; the shore is all curves.

## Elevation & Depth

Depth is **open air, not glass**: `--blur` stays `none` and panels are flat paper, because a beach
afternoon has no frosted surfaces. Lift comes from two soft, wide, low-opacity shadows in the ink's
own green, plus `--glow` — the one energised object on a page, a turquoise rim with the coral's own
warm bloom beneath it, so a primary button reads as lit by the low sun. The shadows are soft on
purpose; this is a smooth kit, not a pixel or 90s-chrome one.

## Shapes

The kit's geometry lives in three drawn signature tokens rather than in its corners.

**The frond** (`--tropical-breeze-frond`) is the mark: a swept rachis with leaflets fanned off it
at an angle, shortening toward the tip. It is drawn as inline SVG because a frond *is* a curve with
leaflets — no repeating gradient produces one, and a stripe pattern renders as a fern print.

**The waves** (`--tropical-breeze-wave`) are the field: three rolling crests at different amplitudes,
each with a foam lip offset above it, over the sea's own gradient. They tile seamlessly — every
path starts and ends on the same y with a matched slope — which is what lets it work as a repeating
texture rather than a single mark.

**The parasol** (`--tropical-breeze-parasol`) is the emblem: a top-down beach umbrella, eight wedges
alternating coral and cream around a turquoise hub. It is drawn because a disc divided into wedges
is a division of *angle*, and no gradient produces that. It is also the one place the coral and the
turquoise meet.

A fourth motif (a sand-grain dither) was considered and cut: the beach grain is already carried by
`--media-bg`, and a fourth tile would only dilute the three.

## Components

Buttons run coral fills with cream labels, or flat paper with coral-ink labels; the danger button
keeps the paper and takes berry text. Cards stay flat on the sand with a warm hairline border; the
elevated card settles into the dry-sand inset. Inputs sit in that same inset, which is also where
badges, code and alerts live — so `--text-on-surface-2*` and the badge inks are all graded against
`#f2efe1`. The media panel is not a colour at all: `--media-bg` replaces the lab's generic accent
ramp with the beach itself — sky, a low soft sun on the water, crests and dry sand.

The accent badge is the one component whose ground is translucent: its background is a 13% coral
tint over the surface it sits on, so `accent-tint` in the palette above is that composite as it
renders on warm paper (`#f8e4dc`), and `--accent-ink` is graded against the composite, not the tint.

## Do's and Don'ts

- **Do** keep coral for action and turquoise for sea/state. Two accents, two jobs.
- **Do** let the ground walk from sea-foam to sand down the page — a `%` ramp shows one flat colour
  and wastes the whole idea.
- **Do** hold `--blur: none`. This is open air; the moment a panel frosts, it becomes a different kit.
- **Don't** use `--accent-2` turquoise as text — it is a fill and a watermark, not an ink; `--info`
  is the text-safe blue.
- **Don't** set the coral on the coral tint. The badge case is graded (`--accent-ink` on the
  composite), and coral-on-coral-tint is not.
- **Don't** add a third accent hue or a grey. Four hues is the whole coast; a grey is a different beach.
