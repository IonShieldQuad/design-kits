---
version: alpha
name: Cyber Angel
description: A celestial-tech light kit — pearl and ice ground, one periwinkle glow, airy display type and soft rounded geometry.
colors:
  primary: "#5b5ce8"
  primary-hover: "#4647cf"
  primary-border: "#b9bcf7"
  on-primary: "#ffffff"
  secondary: "#7cc8f0"
  tertiary: "#c9c2ff"
  neutral: "#f6f8ff"
  neutral-2: "#eef2fb"
  surface: "#ffffff"
  surface-2: "#f1f4fd"
  text: "#1a2147"
  text-muted: "#646e96"
  text-dim: "#636c92"
  border: "#dce3f7"
  border-strong: "#c3cdec"
  ok: "#0f7350"
  warn: "#8f5c00"
  danger: "#cc3350"
  info: "#4553d6"
  periwinkle-soft: "#8fa8ff"
  ice: "#a8e8ff"
  lavender: "#c9c2ff"

typography:
  display:
    fontFamily: "Sora"
    fontSize: "2.6rem"
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: "0.015em"
  h1:
    fontFamily: "Sora"
    fontSize: "1.7rem"
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "0.01em"
  h2:
    fontFamily: "Sora"
    fontSize: "1.3rem"
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: "0.01em"
  body:
    fontFamily: "Inter"
    fontSize: "0.95rem"
    fontWeight: 400
    lineHeight: 1.6
  small:
    fontFamily: "Inter"
    fontSize: "0.8rem"
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: "JetBrains Mono"
    fontSize: "0.72rem"
    fontWeight: 500
    letterSpacing: "0.18em"

rounded:
  sm: "10px"
  md: "14px"
  lg: "20px"
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
    fontWeight: 550
    boxShadow: "0 10px 26px rgba(91,92,232,0.30)"
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
    boxShadow: "0 14px 32px rgba(91,92,232,0.36)"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary-border}"
    rounded: "{rounded.md}"
    padding: "0.58rem 1rem"
  button-secondary-hover:
    backgroundColor: "{colors.neutral-2}"
    textColor: "{colors.primary-hover}"
    borderColor: "{colors.primary-border}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.text-muted}"
    rounded: "{rounded.md}"
  card:
    backgroundColor: "{colors.surface}"
    borderColor: "{colors.border}"
    rounded: "{rounded.lg}"
    padding: "1.15rem"
    boxShadow: "0 6px 22px rgba(58,70,150,0.10)"
  card-elevated:
    backgroundColor: "{colors.surface}"
    borderColor: "{colors.border}"
    rounded: "{rounded.lg}"
    boxShadow: "0 18px 46px rgba(58,70,150,0.16)"
  input:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text}"
    borderColor: "{colors.border-strong}"
    rounded: "{rounded.md}"
    padding: "0.6rem 0.72rem"
  input-focus:
    borderColor: "{colors.primary}"
    boxShadow: "0 0 0 3px rgba(91,92,232,0.14)"
  badge:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text-muted}"
    borderColor: "{colors.border}"
    rounded: "{rounded.pill}"
    padding: "0.2rem 0.55rem"
  badge-accent:
    backgroundColor: "rgba(91,92,232,0.10)"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary-border}"
    rounded: "{rounded.pill}"
  nav-item-active:
    backgroundColor: "rgba(91,92,232,0.10)"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
  alert-info:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text-muted}"
    borderColor: "{colors.info}"
    rounded: "{rounded.md}"
  page:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.text}"
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
  media-gradient:
    backgroundImage: "linear-gradient(135deg, {colors.primary} 0%, {colors.secondary} 100%)"
    rounded: "{rounded.md}"
---

# Cyber Angel

## Overview

Cyber Angel is what cyberpunk looks like after it forgives you. The ground is pearl
(`{colors.neutral}`) cooling into ice (`{colors.neutral-2}`); the only real colour is a
periwinkle-violet (`{colors.primary}`) with an ice-cyan companion (`{colors.secondary}`)
for gradients and media. Depth is *light*, not shadow: elevation reads as a soft coloured
halo rather than a grey drop. Nothing in the kit is black, nothing is saturated, and
nothing shouts.

The mood is calm and slightly otherworldly — a small chapel rendered in glass and
moonlight rather than a neon street. Use it when the product should feel serene, precise
and a little transcendent: wellness, quiet SaaS, hero sections, editorial intros. Do **not**
use it for dense dashboards (too much air) or anything that needs to feel fast and loud.

## Colors

- **primary — `{colors.primary}`** periwinkle-violet. The single action colour. It is
  deliberately deeper than the brief's tint swatch (`{colors.periwinkle-soft}`): a light
  lavender cannot carry white label text, so the *action* colour is the deep cut and the
  light tint is demoted to ambience.
- **secondary — `{colors.secondary}`** ice-cyan. Never a button; always a gradient partner,
  chart colour or media wash.
- **tertiary — `{colors.tertiary}`** lavender whisper. Hairline highlights and the softest
  gradient stop only.
- **neutral — `{colors.neutral}`** pearl page ground, with `{colors.neutral-2}` as the
  second stop under the masthead.
- **`{colors.periwinkle-soft}` / `{colors.ice}`** are exposed as `--angel-periwinkle` and
  `--angel-ice`. They are glow colours: use them at low alpha, never as a text ground.
- Status colours are deliberately desaturated to survive on white: `{colors.ok}`,
  `{colors.warn}`, `{colors.danger}`, `{colors.info}`.

One accent, one companion. If a third "look at me" colour appears, the kit has stopped
being Cyber Angel.

## Typography

Sora (geometric humanist display) over Inter (body) over JetBrains Mono (labels). Display
type is **opened up, not tightened** — `{typography.display.letterSpacing}` is positive, the
opposite of the usual editorial display setting, and it is what makes a heading feel airy
instead of heavy. Weight tops out at 700; there is no 900 in this kit.

Mono labels run at `{typography.label.letterSpacing}` tracking: they read as small engraved
captions. Body copy sits at 0.95rem / 1.6 — generous leading, because the ground is bright
and tight leading on bright ground feels cramped.

## Layout

Air is a material here. The lab's default spacing is already loose; lean further. Group
related controls, then leave a full 44px (`spacing.xl`) between groups. Cards are roomy
(`1.15rem` inner padding) and the grid should never be dense enough that two surfaces touch.

## Elevation & Depth

Two shadow steps, both tinted indigo rather than black:

- `--shadow-1` — resting cards: `0 6px 22px rgba(58,70,150,.10)`.
- `--shadow-2` — elevated cards and overlays: `0 18px 46px rgba(58,70,150,.16)`.
- `--glow` — the primary button and only the primary button: `0 10px 26px rgba(91,92,232,.30)`.

`--blur` is `none` on purpose. This kit's surfaces are crisp; the frosted look belongs to
the sibling `glass` kit and mixing them produces mud. Where a surface needs to feel
luminous, add a large soft halo (`--angel-glow-soft`) rather than a second shadow.

## Shapes

Soft, rounded, never bubbly: `{rounded.sm}` 10px, `{rounded.md}` 14px for interactive
elements, `{rounded.lg}` 20px for cards, pills at 999px. `--cut` is `0px` — no chamfers, no
machined corners; the geometry is meant to feel grown rather than milled.

## Components

- **button-primary** — `{colors.primary}` on `{colors.on-primary}`, 14px radius, carrying
  `--glow`. Hover deepens to `{colors.primary-hover}`; it never brightens (brightening a
  button on a bright ground makes it vanish).
- **button-secondary** — transparent with a `{colors.primary-border}` hairline and accent
  text; hover fills with the soft accent tint.
- **card** — white on pearl with a `{colors.border}` hairline and `--shadow-1`. The
  elevation tells you it is a card far more than any border does.
- **input** — `{colors.surface-2}` fill with a `{colors.border-strong}` border; focus swaps
  the border to `{colors.primary}` and adds a 3px soft ring.
- **badge** — pill, mono, uppercase, `{colors.surface-2}` fill. `badge-accent` is the
  tinted variant for status the user should notice.

## Do's and Don'ts

**Do**

- Let brightness do the work: `{colors.surface}` on `{colors.neutral}` plus a soft shadow is
  the whole depth system.
- Keep white text on the accent only — the accent is tuned so `{colors.on-primary}` clears
  4.5:1.
- Use `{colors.secondary}` for gradient partners and data, and stop there.

**Don't**

- Don't put text on `{colors.periwinkle-soft}` or `{colors.ice}` — they are glow colours.
- Don't add a second shadow *and* a border *and* a fill to one surface; pick two.
- Don't tighten display tracking or push weight past 700 — it tips into generic tech.
- Don't mix in `--blur`; frosted surfaces break the crisp/ethereal split with `glass`.
