---
version: alpha
name: Glass
description: Frosted, translucent panels over a soft pastel gradient — restrained glassmorphism with layered depth instead of borders.
colors:
  primary: "#4550e8"
  accent-ink: "#2a36e5"
  primary-hover: "#3944d6"
  primary-border: "#a9b0fa"
  on-primary: "#ffffff"
  secondary: "#b39dff"
  tertiary: "#7fe0c4"
  neutral: "#eef1f8"
  rose: "#ffd9e8"
  lilac: "#dcd6ff"
  mint: "#d3f5ea"
  sky: "#d6ecff"
  surface: "rgba(255, 255, 255, 0.58)"
  surface-2: "rgba(255, 255, 255, 0.65)"
  surface-solid: "#f3f5fb"
  text: "#1c2033"
  text-muted: "#454b63"
  text-dim: "#585e76"
  border: "rgba(255, 255, 255, 0.70)"
  border-strong: "rgba(28, 32, 51, 0.14)"
  ok: "#0f7350"
  warn: "#8f5c00"
  danger: "#c4354f"
  info: "#4550e8"

typography:
  display:
    fontFamily: "Plus Jakarta Sans"
    fontSize: "2.6rem"
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: "-0.02em"
  h1:
    fontFamily: "Plus Jakarta Sans"
    fontSize: "1.7rem"
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "-0.015em"
  h2:
    fontFamily: "Plus Jakarta Sans"
    fontSize: "1.3rem"
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: "-0.01em"
  body:
    fontFamily: "Plus Jakarta Sans"
    fontSize: "0.95rem"
    fontWeight: 400
    lineHeight: 1.6
  small:
    fontFamily: "Plus Jakarta Sans"
    fontSize: "0.8rem"
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: "JetBrains Mono"
    fontSize: "0.72rem"
    fontWeight: 500
    letterSpacing: "0.14em"

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
    boxShadow: "0 10px 26px rgba(69,80,232,0.28)"
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
    boxShadow: "0 14px 32px rgba(69,80,232,0.34)"
  button-secondary:
    backgroundColor: "rgba(255, 255, 255, 0.45)"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary-border}"
    rounded: "{rounded.md}"
    padding: "0.58rem 1rem"
  button-secondary-hover:
    backgroundColor: "rgba(255, 255, 255, 0.70)"
    textColor: "{colors.primary-hover}"
    borderColor: "{colors.primary-border}"
  card:
    backgroundColor: "{colors.surface}"
    borderColor: "{colors.border}"
    rounded: "{rounded.lg}"
    padding: "1.15rem"
    boxShadow: "0 10px 30px rgba(31,38,88,0.14), 0 2px 6px rgba(31,38,88,0.06)"
    backdropFilter: "blur(20px) saturate(180%)"
  card-elevated:
    backgroundColor: "{colors.surface-2}"
    borderColor: "{colors.border}"
    rounded: "{rounded.lg}"
    boxShadow: "0 26px 60px rgba(31,38,88,0.20), 0 6px 18px rgba(31,38,88,0.08)"
    backdropFilter: "blur(20px) saturate(180%)"
  input:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text}"
    borderColor: "{colors.border-strong}"
    rounded: "{rounded.md}"
    padding: "0.6rem 0.72rem"
  input-focus:
    borderColor: "{colors.primary}"
    boxShadow: "0 0 0 3px rgba(69,80,232,0.14)"
  badge:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text-muted}"
    borderColor: "{colors.border}"
    rounded: "{rounded.pill}"
    padding: "0.2rem 0.55rem"
  badge-accent:
    backgroundColor: "rgba(69,80,232,0.12)"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary-border}"
    rounded: "{rounded.pill}"
  nav-item-active:
    backgroundColor: "rgba(69,80,232,0.12)"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
  page:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.text}"
  badge-ok:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.ok}"
    rounded: "{rounded.pill}"
  badge-info:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.info}"
    rounded: "{rounded.pill}"
  badge-warn:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.warn}"
    rounded: "{rounded.pill}"
  badge-danger:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.danger}"
    rounded: "{rounded.pill}"
  alert-info:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text-muted}"
    borderColor: "{colors.info}"
    rounded: "{rounded.md}"
  media-gradient:
    backgroundImage: "linear-gradient(135deg, {colors.primary} 0%, {colors.secondary} 100%)"
    rounded: "{rounded.md}"
---

# Glass

## Overview

Glass is glassmorphism with the volume turned down. The ground is a soft pastel ramp —
rose, lilac, mint and sky over a light base — and everything above it is a frosted white
panel you can see through. There is no flat colour anywhere: surfaces are translucent,
edges are hairline light, and depth comes from stacked soft shadows plus a one-pixel
highlight on the top edge.

Restraint is the whole point. The pastels are washes, not statements; the ink is deep
(`{colors.text}`) so text stays legible over any stop of the ramp; and the only saturated
thing in the kit is the periwinkle-indigo action colour (`{colors.primary}`).

Because surfaces are translucent, "the background" is never one value. Every contrast
claim in `README.md` is made against the **lightest** gradient stop and against the **composited** surface (white at 58% over that stop) — the two worst cases.

## Colors

- **primary — `{colors.primary}`** periwinkle-indigo. Tuned one step deeper than the
  reference swatch so white label text clears 4.5:1 on a bright kit where the button sits
  on a pastel ground rather than on white.
- **secondary — `{colors.secondary}`** lilac. Gradient partner and chart colour; it is the
  mid-stop of the ground, so UI built on it looks continuous with the page.
- **tertiary — `{colors.tertiary}`** mint. Available for success-adjacent accents and data
  series; it is the one cool green on the ramp.
- **neutral — `{colors.neutral}`** the light base the whole gradient settles onto, and the
  colour to use when a surface genuinely cannot be translucent (print, email, canvas).
- The four ramp stops are addressable: `{colors.rose}`, `{colors.lilac}`, `{colors.mint}`,
  `{colors.sky}`.
- **Surfaces are transparent by design:** `{colors.surface}` and `{colors.surface-2}` are
  `rgba()` white. Never substitute a hex — the translucency *is* the kit.
- Status colours (`{colors.ok}`, `{colors.warn}`, `{colors.danger}`, `{colors.info}`) are
  darkened so badge text stays readable once it is composited over the ramp.

## Typography

A single family, Plus Jakarta Sans, for both display and body, with JetBrains Mono for
labels. Using one humanist geometric across the whole kit is deliberate: the ground is busy
with colour, so the type stays quiet. Display sizes are set **tight** (`-0.02em`) — the
inverse of the sibling `cyber-angel` kit, whose headings are opened up.

Labels run at `{typography.label.letterSpacing}` in mono uppercase. Body copy is 0.95rem /
1.6; on a busy pastel ground, generous leading is what keeps paragraphs readable.

## Layout

Panels are the layout unit. Content sits on frosted cards, cards sit on the ramp, and the
ramp should always be visible at the edges — a full-bleed opaque page defeats the entire
idea. Keep 16–28px between surfaces so the ground reads between them.

## Elevation & Depth

Three layers, all translucent, distinguished by opacity and shadow rather than by colour:

1. ground — the gradient on `--bg`;
2. `{colors.surface}` at 58% white with `backdrop-filter: blur(20px) saturate(180%)`;
3. `{colors.surface-2}` at 65% white with the deeper `--shadow-2`.

The blur is **load-bearing**: `templates/lab.css` applies `var(--blur)` to `.card`, and a
kit that sets `--blur: none` gets no frost at all. Saturing the backdrop (180%) is what
keeps the pastels from turning to milk behind the glass.

Borders are hairline light (`{colors.border}`) and exist only as an edge highlight.
`{colors.border-strong}` is the one exception — a faint ink hairline for emphasised rules,
because a second *white* line has no visible difference against a pastel ground. If a
surface needs more definition, add shadow rather than another border.

## Shapes

`{rounded.sm}` 10px, `{rounded.md}` 14px, `{rounded.lg}` 20px, pills at 999px, `--cut: 0px`.
Radius is generous but consistent — the frosted panel and the ground it floats on should
feel cut from the same mould.

## Components

- **button-primary** — `{colors.primary}` with white label and a soft indigo cast; hover
  deepens to `{colors.primary-hover}`.
- **button-secondary** — translucent white (45%) with a `{colors.primary-border}` hairline;
  it reads as a pane of glass with accent text.
- **card** — 58% white, 1px light edge, `blur(20px) saturate(180%)`, `--shadow-1`.
- **card-elevated** — 65% white and `--shadow-2`; the extra opacity is what makes it feel
  lifted, not the shadow alone.
- **input** — 65% white fill with a `{colors.border-strong}` hairline; focus adds the
  accent border and a soft ring.
- **badge** — pill, mono, uppercase, translucent fill; `badge-accent` for the tinted
  variant.

## Do's and Don'ts

**Do**

- Keep the ground visible between panels — that is where the kit lives.
- Verify any new text colour against the *lightest* ramp stop and the composited surface.
- Use `--shadow-1` / `--shadow-2` (they carry a top-edge highlight) instead of adding
  borders for depth.

**Don't**

- Don't set `--blur` to `none` or drop `backdrop-filter` — the kit becomes a flat pastel
  page and loses its identity.
- Don't raise surface opacity above ~70%: frosted turns to painted.
- Don't put two translucent panels directly on top of each other; nested glass muddies.
- Don't use `{colors.primary}` as a large flat fill — it is an action colour on a pastel
  ground, not a background.