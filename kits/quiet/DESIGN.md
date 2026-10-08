---
version: alpha
name: Quiet
description: Quiet dark app chrome — one soft indigo accent, small radii, generous space, no decoration.
colors:
  primary: "#5b7cfa"
  primary-hover: "#7390ff"
  primary-ink: "#7490fb"
  secondary: "#7d6ce8"
  tertiary: "#6b93e0"
  neutral: "#0b0e13"
  surface: "#12161f"
  surface-2: "#171c27"
  text: "#e8ecf3"
  text-muted: "#b9c2d0"
  success: "#5fbf8f"
  warning: "#e0b26b"
  error: "#ff8383"
typography:
  display:
    fontFamily: Inter
    fontSize: 2.6rem
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: "-0.02em"
  heading:
    fontFamily: Inter
    fontSize: 1.3rem
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: "-0.01em"
  body:
    fontFamily: Inter
    fontSize: 0.95rem
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: Inter
    fontSize: 0.78rem
    fontWeight: 500
    lineHeight: 1
    letterSpacing: "0.02em"
  data:
    fontFamily: 'ui-monospace, "Cascadia Mono", Consolas, monospace'
    fontSize: 0.8rem
    fontWeight: 400
    lineHeight: 1.5
    fontFeature: '"tnum"'
rounded:
  sm: 6px
  md: 8px
  lg: 12px
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
    textColor: "{colors.primary-ink}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: 16px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.primary-ink}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.primary}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: 16px
  button-secondary-hover:
    backgroundColor: "{colors.surface}"
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
    padding: 20px
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
    padding: 12px
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
  card-media:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.md}"
  card-media-2:
    backgroundColor: "{colors.secondary}"
    rounded: "{rounded.md}"
  alert-info:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.tertiary}"
    rounded: "{rounded.md}"
    padding: 12px
  alert-ok:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.success}"
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

Quiet is the app chrome you stop noticing. It came out of a small business landing page —
near-black indigo ground, one soft periwinkle accent, 10–16px radii, no gradients behind
content, no ornament — and it is the kit for the surfaces you spend hours in: settings panels,
dashboards that are mostly reading, editors, long forms.

The only material change from the source is type: raw `Segoe UI` is replaced with Inter, which
keeps the plainness and adds a consistent voice, plus a real monospace for numbers. Nothing else
about the kit is loud enough to need a change.

One sentence: *near-black indigo, one soft accent, small radii, and a lot of air.*

## Colors

- **Primary (#5b7cfa):** soft indigo. The only action colour. Hover is a lighter step of the
  same hue, not a different colour.
- **Secondary (#7d6ce8):** a related violet, one step around the wheel. It exists for
  gradients and media plates and never appears as a second call to action.
- **Tertiary (#6b93e0):** a muted blue for informational status — the least assertive of the
  accent family, which is what an "info" colour should be.
- **Neutral (#0b0e13):** the page ground. Near-black with a faint blue cast, deliberately not
  pure black — pure black makes the accent glow, and this kit does not glow.
- **Surface (#12161f) / surface-2 (#171c27):** the panel steps. Surface is the source's
  `--panel`; surface-2 is one visible lift for inputs and nested panels.
- **Text (#e8ecf3) / text-muted (#b9c2d0):** the two contrast-guaranteed text steps. Muted is
  unusually bright (10:1 on a panel) on purpose — this is the body colour for long text, not a
  caption grey.
- **Error (#ff8383):** the source's soft red, kept exactly.
- **Success (#5fbf8f) / warning (#e0b26b):** derived. The source only needed an error, so the
  other two statuses are mixed to sit at the same low saturation as `#ff8383` rather than
  arriving as saturated system colours.

`--text-dim: #8a93a3`, `--border: #2a3140` (the source's `--line`) and
`--border-strong: #3a4356` live in `tokens.css` but not in the `colors` map above: the
DESIGN.md component schema has no property that can reference a line colour, and a caption
asserts no contrast floor, so listing them would only produce orphan warnings.

## Typography

One family and one monospace. That is the whole system, and it is a feature.

- **Inter** — display, headings, body, labels. Sizes and weights do all the differentiation:
  2.6rem/700 display, 1.3rem/600 headings, 0.95rem/400 body at 1.6, 0.78rem/500 labels.
- **System monospace** (`ui-monospace`, Cascadia Mono, Consolas) — numbers, IDs, code. Tabular
  figures are on by default so columns of digits do not shimmer. No webfont is fetched for it;
  a tool that runs offline should not pay for a mono it already has.

Display tracking is `-0.02em` — tight enough to read as designed, not so tight that it becomes
a styling statement.

## Layout

A single centred column. Cards are a responsive grid that collapses to one column on a phone;
inputs are full-width inside their field. Vertical rhythm is generous (1.1–2.25rem between
blocks, 40px between sections) because the content of this kit is usually a form or a list, and
cramped forms are how "quiet" turns into "hostile".

Small radii are not the same as small spacing: keep the corners tight, keep the air large.

## Elevation & Depth

Almost none — and that is the design. `--glow: none` and `--blur: none` are hard zeros: nothing
in this kit emits light or frosts. Depth is one hairline (`--border`) plus a soft, tight
shadow (`--shadow-1: 0 1px 2px rgba(0,0,0,.4)`) for genuinely floating surfaces like menus, and
`--shadow-2` for modals. A card is a panel, not a raised object.

If a component needs to be noticed, it gets the accent, not a shadow.

## Shapes

Small and consistent: `--radius-sm: 6px`, `--radius-md: 8px`, `--radius-lg: 12px`, true pills
for badges and the toggle. `--cut: 0px` — this kit does not cut corners; the chamfer is another
kit's signature and mixing the two would make both arbitrary.

Card radius is the largest value in the system at 12px. There is no 20px+ "soft card" look
here, and no fully-round buttons.

## Components

- **button-primary** — a flat indigo plate with the page ink as the label. No glow, no
  gradient, no shadow.
- **button-primary-hover** — the lighter indigo. The button does not move; only its colour does.
- **button-secondary** — the ground as a plate with an indigo label and a hairline rim.
- **card** — a panel with a hairline and a 12px radius; `card-elevated` steps the fill up rather
  than adding shadow.
- **input** — `surface-2` fill, `--border` hairline, an indigo focus ring drawn as a soft halo
  (no hard 2px outline), matching the source.
- **badge** — a pill. Soft by default; `badge-accent` is the only one that carries the indigo.

## Do's and Don'ts

- **Do** use spacing for hierarchy. This kit has almost no other tool.
- **Do** keep one action colour; hover is a lighter step of the same hue.
- **Do** put numbers in the system monospace with tabular figures.
- **Do** let muted text stay bright when it is body copy. Dim is for captions only.
- **Don't** add a shadow to a card, a glow to a button, or a gradient behind content.
- **Don't** drop below 6px radius or go above 12px. The scale is intentionally narrow.
- **Don't** introduce a second accent family. Violet and blue are steps of the same idea.
