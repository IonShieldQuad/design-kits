---
version: alpha
name: Signal
description: Deep-navy HUD — Chakra Petch headings, mono labels, cyan/blue action, mint and amber status.
colors:
  primary: "#37d7ff"
  primary-hover: "#5fe0ff"
  primary-ink: "#04121a"
  secondary: "#4a9dff"
  tertiary: "#8b6cff"
  neutral: "#05070d"
  surface: "#0c1426"
  surface-2: "#101b32"
  text: "#eaf3ff"
  text-muted: "#8ea3c4"
  success: "#43ffb4"
  warning: "#ffc46b"
  error: "#ff6b7a"
typography:
  display:
    fontFamily: Chakra Petch
    fontSize: 2.9rem
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: "0.01em"
  heading:
    fontFamily: Chakra Petch
    fontSize: 1.3rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: "0.01em"
  body:
    fontFamily: Inter
    fontSize: 0.95rem
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: JetBrains Mono
    fontSize: 0.72rem
    fontWeight: 600
    lineHeight: 1
    letterSpacing: "0.14em"
rounded:
  sm: 4px
  md: 6px
  lg: 10px
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

Signal is an instrument panel. It came out of a resume site that reads like a HUD: a deep-navy
ground with a fixed blue wash, faceted panels cut with a 16px chamfer, and mono labels doing
the work of a readout. It carries more colour than Carbon but stays calm about it — cyan and
blue are the brand, mint and amber are status, and nothing is saturated for its own sake.

Use it for dashboards, data-dense tools, consoles, and résumés — anywhere the reader is
scanning rather than reading. It is comfortable at small type and dense tables, which the
other two kits in this family are not.

One sentence: *a deep-navy HUD — brand cyan for action, mint and amber for status, mono for
anything that is a fact.*

## Colors

- **Primary (#37d7ff):** cyan. Actions, links, focus, live indicators, telemetry.
- **Secondary (#4a9dff):** blue. The second accent — gradients, media plates, chart series.
- **Tertiary (#8b6cff):** violet. Informational status; `--info` in `tokens.css` is the same
  violet, because the source palette has exactly one and it already means "network/system".
- **Neutral (#05070d):** the ground — near-black with a blue cast, not pure black.
- **Surface (#0c1426) / surface-2 (#101b32):** the navy panel steps. The source declares these
  as translucent navies (`rgba(12,20,38,.82)` and `rgba(16,27,50,.55)`) to be read over a
  gradient background; on a flat page those composite to almost exactly these opaque values,
  so the kit publishes the flattened colour and keeps the frosted look via `--blur`.
- **Text (#eaf3ff) / text-muted (#8ea3c4):** the two contrast-guaranteed text steps.
- **Success (#43ffb4) / warning (#ffc46b) / error (#ff6b7a):** status. Mint and amber are the
  source's own; the red is derived, because the source has no danger colour and a status
  system without one is incomplete.

`--text-dim: #7486a6` (the source's `--dim`), `--border: rgba(130,180,255,.16)` (the source's
`--line`) and `--border-strong: rgba(130,180,255,.34)` are defined in `tokens.css` but kept
out of the `colors` map above: the DESIGN.md component schema has no `borderColor` property
and a tertiary caption asserts no contrast floor, so listing them would only produce orphan
warnings for values that are very much in use.

## Typography

Three faces, tight roles:

- **Chakra Petch** — display and headings. Square-cut, slightly mechanical, which is why the
  panel furniture can stay plain without the whole thing looking generic.
- **Inter** — body at 1.6 line-height. Data-dense surfaces need the reading text to be calm.
- **JetBrains Mono** — every label, badge, table header, and number. Uppercase, tracked
  +0.14em. Mono is the kit's instrument voice.

Display and heading sizes are fluid in the source; the floor for mono labels is 11–12px.

## Layout

A `min(1040px, 100% - 2.5rem)` column, matching the source's `--maxw`. Sections are separated
by hairlines and generous vertical padding; inside a panel the rhythm is tight (8–16px) so
readouts group by proximity rather than by boxes. Cards are a responsive auto-fit grid that
collapses to one column on a phone.

Dense is the point: the lab's table, badge row and progress bars should read as the natural
content of this kit, not as an edge case.

## Elevation & Depth

Depth is a navy step plus a dark shadow — `--shadow-2: 0 18px 50px rgba(0,0,0,.28)` is the
source's own panel shadow, and it is unusually soft for a dark theme on purpose: panels float
on the navy rather than sitting in a hole in it.

`--glow` (`0 0 14px rgba(55,215,255,.4)`) is reserved for the active control — the source
lights its pressed language switch with exactly this. Panels carry `--blur: blur(10px)`, the
source topbar's glass, so a card over content still reads as a pane.

## Shapes

Small radii, held tight: `--radius-sm: 4px`, `--radius-md: 6px` (the source's single radius),
`--radius-lg: 10px`, and true pills for badges. Nothing is a large radius — 10px is the
ceiling, and only for panels.

The signature shape is a **corner cut**, not a radius: `--cut: 16px` drives
`--clip-corner`, the polygon the source applies to its panels and icon buttons:

```css
.panel { clip-path: var(--clip-corner); }   /* one 16px chamfer, bottom-right */
```

The lab does not clip anything, so this is opt-in. When applied, draw any border as two
clipped layers (rim + inset surface) — `clip-path` slices a normal border off along the
diagonal.

## Components

- **button-primary** — a solid cyan plate, near-black label, mono uppercase.
- **button-primary-hover** — cyan lifted one step; still an ink label, never white.
- **button-secondary** — navy plate with a cyan label. The default second action.
- **card / card-elevated** — navy panes, 10px radius, separated by a blue-tinted hairline.
- **input** — `surface-2` fill, `--border` hairline, cyan focus ring with a soft halo.
- **badge** — pill, mono, uppercase; `badge-accent`, `badge-success` and `badge-warning`
  recolor the label and leave the chip dark, so a row of status reads as lights, not blocks.
- **alert-*** — a navy pane with a 3px status rule down the left edge.

## Do's and Don'ts

- **Do** keep cyan for action and mint/amber for state. They never swap roles.
- **Do** set facts, IDs and numbers in mono; the sans is for sentences.
- **Do** use the corner cut on panels and keep radii at 6–10px. Both belong to the language.
- **Do** let panels float — soft shadow, navy step, hairline. Never a hard black shadow.
- **Don't** put white text on cyan. The ink colour exists because cyan is a fill, not a page.
- **Don't** add a fourth hue. Violet is informational; that is the whole quota.
- **Don't** desaturate to "calm it down" — the calm comes from spacing, not from grey.
