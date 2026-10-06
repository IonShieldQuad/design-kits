---
version: alpha
name: Dark Glass
description: Dark frosted glass — translucent panels over a violet- and cyan-lit near-black mesh, hairline light edges, depth from layered soft shadow and a top-edge highlight.
colors:
  primary: "#8b7cff"
  primary-hover: "#a094ff"
  on-primary: "#0b0c14"
  primary-soft: "rgba(139, 124, 255, 0.16)"
  secondary: "#4fd8ff"
  tertiary: "#c3b8ff"
  neutral: "#0b0d16"
  surface: "rgba(22, 26, 36, 0.55)"
  surface-2: "rgba(28, 33, 45, 0.68)"
  surface-solid: "#161a24"
  text: "#eef2fb"
  text-muted: "#b7c0d4"
  text-dim: "#a0a9be"
  ok: "#4fce8f"
  warn: "#f5b942"
  danger: "#ff6b81"
  info: "#6b9dff"
  bg-stop-1: "#0d0f1b"
  bg-stop-2: "#090a13"
  bg-stop-3: "#070810"

typography:
  display:
    fontFamily: "Sora"
    fontSize: "2.6rem"
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: "-0.02em"
  h1:
    fontFamily: "Sora"
    fontSize: "1.7rem"
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "-0.015em"
  h2:
    fontFamily: "Sora"
    fontSize: "1.3rem"
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: "-0.01em"
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
  button:
    fontFamily: "Inter"
    fontSize: "0.875rem"
    fontWeight: 500
    lineHeight: 1.2
  label:
    fontFamily: "JetBrains Mono"
    fontSize: "0.72rem"
    fontWeight: 500
    letterSpacing: "0.12em"

rounded:
  sm: "10px"
  md: "16px"
  lg: "22px"
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
    textColor: "{colors.primary-hover}"
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
    textColor: "{colors.primary}"
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
    textColor: "{colors.primary}"
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
  page:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.text}"
---

# Dark Glass

## Overview

Dark Glass is the dark counterpart to the `glass` kit: the same structural idea — surfaces are
genuinely translucent and the ground is visible *through* them — pointed at a deep, luminous
dark instead of pastel light.

The ground is a near-black mesh: a violet wash at the top-left, a cyan wash at the top-right and
a wide deep-purple bloom low-centre — repeated at lower amplitude twice more down the page — laid
over a close-spaced ramp from `{colors.bg-stop-1}` to `{colors.bg-stop-3}`. Panels float on it at
55% and 68% opacity with hairline **light** edges
(`rgba(255,255,255,.14)`) and `backdrop-filter: blur(20px) saturate(140%)`. Nothing in the kit
uses a dark outline — on a near-black ground a dark border is invisible, so the edge that reads is
the light one.

Restraint is the point. There are exactly two brand hues — a clear violet (`{colors.primary}`)
and a cyan (`{colors.secondary}`) — and the cyan is graphic only: it appears in gradients, chart
bars, media and the avatar, never on a button. The single action colour is the violet.

## Colors

- **primary — `{colors.primary}`** clear violet. The one action colour: button fills, active nav,
  links, focus rings. It carries **dark** label text (`{colors.on-primary}`), not white — white on
  this violet measures 3.2:1 and would fail the contract, so the kit deliberately inverts the
  usual "white on the accent" assumption for a luminous mid-tone accent.
- **secondary — `{colors.secondary}`** cyan. Gradient partner and chart colour; it is also the
  wash in the top-right of the ground, so UI built on it looks continuous with the page.
- **tertiary — `{colors.tertiary}`** pale violet. A quiet third hue for data series and
  illustrations, one step lighter than the accent so it never competes with it.
- **neutral — `{colors.neutral}`** the solid stand-in for the page ground. The real ground is a
  mesh (see `--bg` in `tokens.css`), so when a surface genuinely cannot be a gradient or cannot be
  translucent — print, email, canvas — this is the colour to use.
- The three mesh stops are addressable: `{colors.bg-stop-1}`, `{colors.bg-stop-2}`,
  `{colors.bg-stop-3}`.
- **Surfaces are transparent by design:** `{colors.surface}` and `{colors.surface-2}` are `rgba()`
  ground. Never substitute a flat hex — the translucency *is* the kit. `{colors.surface-solid}` is
  the documented opaque fallback.
- Status colours sit outside the brand pair on purpose — green, amber, red and a brighter blue —
  so a "live" or "failed" badge can never be mistaken for the brand.

## Typography

Two families and a mono. **Sora** is the display face — geometric, wide counters, set tight
(`-0.02em`) so a large heading reads as one block rather than a row of letters. **Inter** carries
body and interface text at 0.95rem / 1.6; on a low-luminance ground generous leading matters more
than on paper. **JetBrains Mono** is labels only, uppercase, at
`{typography.label.letterSpacing}`.

Sora rather than the sibling `glass` kit's Plus Jakarta Sans is deliberate: same humanist-geometric
family of faces, visibly different skeleton, so a thumbnail of the two kits reads as two kits.

## Layout

Panels are the layout unit and the mesh is the canvas. Content sits on frosted cards, cards float
on the mesh, and the mesh should always be visible at the edges — a full-bleed opaque page destroys
the idea. Keep 16–28px between surfaces so the ground reads between them, and never stack two
frosted panels directly (nested translucency composites to mud; use `--surface-2`, the denser
panel, for the nested layer).

## Elevation & Depth

Three layers, distinguished by opacity and shadow rather than colour:

1. the mesh on `--bg`;
2. `{colors.surface}` at 55% with `backdrop-filter: blur(20px) saturate(140%)`;
3. `{colors.surface-2}` at 68% with the deeper `--shadow-2`.

Both steps add an `inset 0 1px 0 rgba(255,255,255,.10–.14)` highlight along the top edge — on a
dark ground that faint bright lip is what makes a panel read as a *pane* rather than a hole.

`--blur` is load-bearing: `templates/lab.css` applies `var(--blur)` to every `.card`, and a kit
that sets `--blur: none` gets no frost at all. The `saturate(140%)` matters as much as the blur —
it keeps the violet and cyan from going grey behind the glass.

**Frost needs something to frost.** A `backdrop-filter` over a perfectly smooth ramp is
indistinguishable from flat paint: there is no high-frequency detail for the blur to smear and no
tint gradient for the saturate to lift. That is exactly why `--bg` is a mesh of offset blobs on a
close-spaced ramp rather than a single slow gradient — the blobs guarantee there is structure behind
every panel, and the blur turns that structure into the soft luminous smear that reads as frosted
glass. The mesh **continues down the whole document** (six washes at px y-positions 40 / 120 / 640 /
1500 / 2050 / 2750, the lower ones at lower amplitude): a single top-of-page wash leaves everything
below the fold flat black, and every panel down there loses its frost. Do not "simplify" `--bg` to a
two-stop ramp; the frosted panels stop reading.

Edges are hairline **light** (`{colors.border}` at `rgba(255,255,255,.14)`), and exist only to catch
that light. There is no dark border token anywhere in this kit: on a near-black ground an ink
hairline is invisible. If a surface needs more separation, add shadow rather than a heavier line.

## Shapes

`{rounded.sm}` 10px, `{rounded.md}` 16px, `{rounded.lg}` 22px, pills at 999px, `--cut: 0px` — this
kit rounds; it does not cut. Radius is generous and consistent, so panels feel cut from the same
mould as the ground they float on.

## Components

- **button-primary** — `{colors.primary}` fill with a `{colors.on-primary}` label and a soft
  violet cast; hover lifts to `{colors.primary-hover}`.
- **button-secondary** — a translucent `{colors.surface}` pane with `{colors.primary}` text; the
  edge is the same hairline light line as a card, so it reads as glass, not as a stroked button.
- **card** — 55% panel, 1px light edge, `blur(20px) saturate(140%)`, `--shadow-1`.
- **card-elevated** — the 68% panel with `--shadow-2`; the extra opacity is what makes it feel
  lifted, not the shadow alone.
- **input** — the denser `{colors.surface-2}` panel as a fill; focus adds the accent rim and a soft
  `{colors.primary-soft}` ring.
- **badge** — pill, mono, uppercase, translucent; `badge-accent` is the violet-tinted variant.
- **avatar / chart-1** — the two places cyan is allowed: avatar fills and data series.

## Do's and Don'ts

**Do**

- Keep the mesh visible between panels — that is where the kit lives.
- Verify any new text colour against the *lightest* pixel of the mesh, not against `{colors.neutral}`.
- Reach for `--shadow-1` / `--shadow-2` (both carry the top-edge highlight) instead of adding borders.
- Composite translucent surfaces before claiming a contrast number.

**Don't**

- Don't set `--blur` to `none` or drop `backdrop-filter` — the kit becomes a flat dark page.
- Don't raise surface opacity above ~72%; frosted turns to painted.
- Don't put two frosted panels directly on top of each other.
- Don't put white text on `{colors.primary}` — it measures 3.2:1. Use `{colors.on-primary}`.
- Don't flatten `--bg` to a smooth two-stop ramp; a blur with nothing behind it is invisible.
- Don't use `{colors.secondary}` as a button fill — cyan is graphic, the violet is the action.
