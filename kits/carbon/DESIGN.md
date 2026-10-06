---
version: alpha
name: Carbon
description: Deep-space technical UI — neon cyan on carbon black, cut corners, mono labels.
colors:
  primary: "#00e5ff"
  primary-hover: "#2ae9ff"
  primary-ink: "#04121a"
  secondary: "#7c4dff"
  tertiary: "#2f7bff"
  neutral: "#0b0c10"
  surface: "#13151c"
  surface-2: "#1a1e27"
  text: "#e6ebf2"
  text-muted: "#9aa6b4"
  success: "#3ddc97"
  warning: "#ffc46b"
  error: "#ff3d5e"
typography:
  display:
    fontFamily: Space Grotesk
    fontSize: 2.9rem
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: "-0.01em"
  heading:
    fontFamily: Space Grotesk
    fontSize: 1.3rem
    fontWeight: 650
    lineHeight: 1.2
    letterSpacing: "-0.005em"
  body:
    fontFamily: Inter
    fontSize: 0.95rem
    fontWeight: 400
    lineHeight: 1.55
  label:
    fontFamily: JetBrains Mono
    fontSize: 0.72rem
    fontWeight: 600
    lineHeight: 1
    letterSpacing: "0.08em"
  tech:
    fontFamily: Orbitron
    fontSize: 1rem
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: "0.06em"
rounded:
  none: 0px
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
  card-title:
    textColor: "{colors.text}"
    typography: "{typography.heading}"
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
  card-media:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.md}"
  card-media-2:
    backgroundColor: "{colors.secondary}"
    rounded: "{rounded.md}"
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
    backgroundColor: "{colors.surface}"
    textColor: "{colors.tertiary}"
    rounded: "{rounded.md}"
    padding: 12px
  alert-error:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.error}"
    rounded: "{rounded.md}"
    padding: 12px
  table-header:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-muted}"
    typography: "{typography.label}"
  link:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.primary}"
---

## Overview

Carbon is the technical end of the dark spectrum: a near-black board with neon cyan wiring.
It came out of the msubinarylily portfolio, where the page is a machine bay — grid rules,
a faceted plate, cut-corner plates, and mono labels that read as instrumentation rather than
prose. The surface is almost an absence of colour; the colour arrives as light.

The kit is for surfaces that want to look engineered: product marketing for developer tools,
a portfolio, a launch page for something with a launch button. It is **not** for reading
long text or for surfaces that must feel friendly.

One sentence: *neon cyan on carbon black, nothing round, everything cut.*

## Colors

The palette is monochrome-plus-light. There is one action colour and one atmosphere colour;
everything else is a step of the ground or a status.

- **Primary (#00e5ff):** neon cyan. Every action, every focus ring, every "this is live"
  moment. It is a *fill and a glow*, not a body-text colour — cyan text on a light surface is
  where this palette would fail, so the source keeps a separate readable ink for that case.
- **Secondary (#7c4dff):** neon violet. It exists for gradients and media (the holo wash),
  never for a second call to action.
- **Tertiary (#2f7bff):** the cold pole of the source's binary motif — a supporting blue used
  for informational status and rules.
- **Neutral (#0b0c10):** carbon. The ground the whole system sits on.
- **Surface (#13151c) / surface-2 (#1a1e27):** two lifts off the ground for cards and inputs.
- **Text (#e6ebf2) / text-muted (#9aa6b4):** the two contrast-guaranteed text steps. Muted
  clears 7:1 on the card surface.
- **Error (#ff3d5e):** the source's hot pole, promoted to the danger colour.

Three tokens are defined in `tokens.css` but intentionally absent from the `colors` map above,
because the DESIGN.md component schema has no property that can reference them (there is no
`borderColor`, and a tertiary caption has no contrast guarantee to assert):

- `--text-dim: #7c8795` — captions, placeholders, timestamps. `--text-muted` pulled toward
  the ground; exempt from the 4.5:1 floor in WCAG and treated as such here.
- `--border: #2a2f3a` — the default 1px hairline (`--line-dark`).
- `--border-strong: #3b424f` — input rims and emphasised dividers.

Status colours (`success`, `warning`, `error`) are signal, not brand. They never carry a
primary action.

## Typography

Four faces, each with one job, because the source already drew the line:

- **Space Grotesk** — display and headings. Geometric, slightly off-square, technical without
  being a gimmick.
- **Inter** — body. Everything you actually read.
- **JetBrains Mono** — labels, badges, table headers, code. Uppercase, tracked +0.08em. Mono
  is the kit's "instrument" voice: if a string is a fact rather than a sentence, it is mono.
- **Orbitron** — the wordmark face. It is exposed as `--font-tech` for the logotype and HUD
  labels only. It is deliberately *not* the display or the body font; Orbitron at paragraph
  size is unreadable, and the lab does not use it.

The display size is fluid (`clamp()`); the floor for mono labels is 12px.

## Layout

The lab is a single column at `min(1040px, 100% - 2.5rem)`. Carbon's own geometry is a
gap-driven grid (`clamp(1rem, 3vw, 2rem)`) that collapses to one column below 640px and opens
to two or three above 900px. Nothing here is bespoke to the kit — the shape language is what
carries it.

Density is medium: generous section padding (3.2–6rem) with tight internal rhythm, so the
page reads as a board with plated modules rather than a document.

## Elevation & Depth

Depth is light, not shadow. The signature elevation is `--glow`
(`0 0 14px rgba(0,229,255,.35)`) under the primary action and the focus ring — the surface
emits. Physical shadows (`--shadow-1`, `--shadow-2`) exist for menus and modals but are dark
and tight; they are never the primary way a thing reads as raised.

Blur is real: `--blur: blur(16px) saturate(1.35)` is the source header's glass, and the lab's
cards consume it.

## Shapes

**Nothing in this kit is round.**

- Radii are 0 across the scale, including `--radius-pill`. Badges and avatars are squares;
  the cut corner is the only corner treatment in the language.
- `--cut: 14px` is the corner size, `--cut-lg: 22px` for large plates, and
  `--clip-btn: 10px` for controls. The polygon is exposed as `--clip` / `--clip-lg` /
  `--clip-btn` so a project can apply it with one declaration:

  ```css
  .plate { clip-path: var(--clip); }
  .plate.btn { clip-path: var(--clip-btn); }
  ```

  The shared lab does not clip anything, so `--cut` is documented rather than automatic —
  apply it yourself. When you do, draw borders as two clipped layers (rim + inset surface),
  because `clip-path` cuts a 1px border off along the diagonal.

## Components

- **button-primary** — a solid cyan plate with the near-black ink label. It carries the glow.
  Mono, uppercase, min-height 44px in the source.
- **button-primary-hover** — the lighter cyan top stop of the source's gradient.
- **button-secondary** — carbon plate, cyan label, cyan-tinted rim. The default "there is
  another option here" button.
- **card / card-elevated** — square plates on `surface` and `surface-2`, separated by a
  hairline rather than a radius.
- **input** — `surface-2` fill, `--border` hairline, cyan focus ring plus `--accent-soft` halo.
- **badge** — mono, uppercase, square. `badge-accent` inverts to a carbon chip with a neon rim.

## Do's and Don'ts

- **Do** let cyan mean "act" or "live". One primary per screen.
- **Do** put facts in mono and sentences in Inter.
- **Do** apply `--clip` on plates and keep radii at 0. The cut *is* the brand.
- **Do** keep the board black. Colour is light on the board, not a wash across it.
- **Don't** use cyan for body copy on a light surface — use the darker readable ink instead.
- **Don't** introduce a third "look at me" colour. Violet is atmosphere; the poles are status.
- **Don't** round a corner. If a component needs a shape, cut it.
