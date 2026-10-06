---
version: alpha
name: Cyber Angel
description: A light shell with dark wells — 1px black rules and 45° chamfers on #D9D9D9 panels, the Figma file's holo cyan as the one action colour, and its dark Panel #242424 for everything inset.
colors:
  primary: "#15b9ff"
  primary-hover: "#4fcbff"
  on-primary: "#313131"
  secondary: "#89dcff"
  tertiary: "#005e85"
  neutral: "#d9d9d9"
  neutral-2: "#e0e0e0"
  canvas: "#2e2f30"
  surface: "#e0e0e0"
  surface-2: "#242424"
  text: "#292929"
  text-muted: "#444444"
  text-dim: "#5c5c5c"
  text-invert: "#313131"
  on-surface: "#292929"
  on-surface-muted: "#444444"
  on-surface-2: "#89dcff"
  on-surface-2-muted: "#7fbfda"
  border: "#000000"
  border-strong: "#000000"
  accent-soft: "rgba(21, 185, 255, 0.14)"
  ok: "#5fe3a1"
  warn: "#ffc46b"
  danger: "#b32017"
  danger-panel: "#ff948f"
  info: "#89dcff"

typography:
  display:
    fontFamily: "Syncopate"
    fontSize: "2.6rem"
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: "0.02em"
  h1:
    fontFamily: "Syncopate"
    fontSize: "1.7rem"
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "0.02em"
  h2:
    fontFamily: "Syncopate"
    fontSize: "1.3rem"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "0.02em"
  h3:
    fontFamily: "Syncopate"
    fontSize: "1.05rem"
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: "0.02em"
  body:
    fontFamily: "Montserrat"
    fontSize: "0.95rem"
    fontWeight: 400
    lineHeight: 1.6
  small:
    fontFamily: "Montserrat"
    fontSize: "0.8rem"
    fontWeight: 400
    lineHeight: 1.5
  input:
    fontFamily: "Nova Flat"
    fontSize: "0.875rem"
    fontWeight: 400
    lineHeight: 1.4
  label:
    fontFamily: "Nova Flat"
    fontSize: "0.72rem"
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: "0.09em"

rounded:
  sm: "2px"
  md: "3px"
  lg: "4px"
  pill: "2px"

spacing:
  xs: "4px"
  sm: "8px"
  md: "16px"
  lg: "28px"
  xl: "44px"

components:
  page:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.text}"
  surface:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
  hero:
    backgroundColor: "{colors.neutral-2}"
    textColor: "{colors.text}"
    typography: "{typography.display}"
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.lg}"
    padding: "1.15rem"
  card-body:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface-muted}"
    typography: "{typography.body}"
  card-elevated:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.on-surface-2}"
    rounded: "{rounded.lg}"
    padding: "1.15rem"
  card-elevated-body:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.on-surface-2-muted}"
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
    padding: "0.58rem 1rem"
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
    padding: "0.58rem 1rem"
  button-secondary:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.tertiary}"
    rounded: "{rounded.md}"
    padding: "0.58rem 1rem"
  button-secondary-hover:
    backgroundColor: "{colors.neutral-2}"
    textColor: "{colors.tertiary}"
    rounded: "{rounded.md}"
    padding: "0.58rem 1rem"
  button-ghost:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.text-muted}"
    rounded: "{rounded.md}"
    padding: "0.58rem 1rem"
  button-ghost-hover:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.on-surface-2}"
    rounded: "{rounded.md}"
    padding: "0.58rem 1rem"
  button-danger:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.danger}"
    rounded: "{rounded.md}"
    padding: "0.58rem 1rem"
  input:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.on-surface-2}"
    typography: "{typography.input}"
    rounded: "{rounded.md}"
    padding: "0.6rem 0.72rem"
  input-placeholder:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.on-surface-2-muted}"
  badge:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.on-surface-2-muted}"
    rounded: "{rounded.pill}"
    padding: "0.2rem 0.55rem"
  badge-accent:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.tertiary}"
    rounded: "{rounded.pill}"
    padding: "0.2rem 0.55rem"
  badge-ok:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.ok}"
    rounded: "{rounded.pill}"
    padding: "0.2rem 0.55rem"
  badge-warn:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.warn}"
    rounded: "{rounded.pill}"
    padding: "0.2rem 0.55rem"
  badge-danger:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.danger-panel}"
    rounded: "{rounded.pill}"
    padding: "0.2rem 0.55rem"
  badge-info:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.info}"
    rounded: "{rounded.pill}"
    padding: "0.2rem 0.55rem"
  nav-item-active:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.tertiary}"
    rounded: "{rounded.sm}"
  link:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.tertiary}"
  table-header:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.text-dim}"
  table-rule:
    backgroundColor: "{colors.border-strong}"
    height: "1px"
  divider:
    backgroundColor: "{colors.border}"
    height: "1px"
  focus-ring:
    backgroundColor: "{colors.tertiary}"
    height: "2px"
  tint-surface:
    backgroundColor: "{colors.accent-soft}"
  scrim:
    backgroundColor: "{colors.canvas}"
  alert:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.on-surface-2-muted}"
    rounded: "{rounded.md}"
    padding: "0.8rem 0.95rem"
  alert-strong:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.on-surface-2}"
  alert-danger:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.danger-panel}"
  toggle-track:
    backgroundColor: "{colors.surface-2}"
    height: "1.3rem"
  toggle-knob:
    backgroundColor: "{colors.text-invert}"
    size: "0.95rem"
  avatar:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.pill}"
    size: "2.2rem"
  chart-series-1:
    backgroundColor: "{colors.primary}"
  chart-series-2:
    backgroundColor: "{colors.secondary}"
  chart-series-3:
    backgroundColor: "{colors.tertiary}"
---

# Cyber Angel

## Overview

Cyber Angel is the angel of the singularity as it was actually drawn: a light shell with
dark wells. The page and its panels are light grey — `{colors.neutral}` under
`{colors.surface}` — and everything inset into them (inputs, badges, alerts, code, elevated
cards) is the design's dark Panel, `{colors.surface-2}`. The two are held together by pure
black rules at 1px, `{colors.border}`, and by a 12px 45° chamfer on opposite corners that
cuts the corner off every card, button, input, nav and badge in the kit.

The single action colour is the file's holo cyan, `{colors.primary}`, with its own light tone
`{colors.secondary}` as the gradient partner and `{colors.tertiary}` as the deep ink used
wherever accent-coloured *text* has to sit on a light ground. Warmth is not part of this
design and is not faked: the optimism here is lit, forward-leaning holo blue, not a sunset.

Use it for bright, confident, technological work — product launches, AI and vision pages,
tools that want to look like an instrument panel rather than a terminal. Do **not** use it
where surfaces must be soft, translucent or pastel: that is `glass`, and its opposite is
`carbon`.

## Colors

Every value below is a token from the Figma frame (*Marketplace-Cyber-Angel → UI Kit →
Cyber Angel*) or a documented derivation from one; `README.md` lists the raw Figma names
next to each.

- **primary — `{colors.primary}`** the file's *Outline* holo cyan. It is a **fill**, not an
  ink: it carries dark label text (`{colors.on-primary}`, the file's *On Holo Dark*, 5.8:1)
  and it glows, because the file ships cyan halos at radius 2 / 4 / 8. Where cyan has to be
  legible *as text* on a light ground the kit uses `{colors.tertiary}` instead — a deeper cut
  of the same hue (5.1:1) — because no single cyan can serve both polarities: 1.6:1 as text on
  the light ground, 5.8:1 as a fill under dark ink, and the two cannot be one value.
- **secondary — `{colors.secondary}`** the file's *Primary* / *On Panel* light holo. It is
  the gradient partner (media plates, progress bars, the avatar), the `info` status, and the
  rim colour on a focused input.
- **tertiary — `{colors.tertiary}`** deep holo cyan: links, the active nav pill, the eyebrow,
  secondary-button labels, inline code. This is the one accent value that is *ink* on a light
  surface.
- **neutral — `{colors.neutral}`** the file's *Background 2*: the page. `{colors.neutral-2}`
  (its *Surface*) is the lit stop the masthead ramps into, so the header is brighter than the
  page rather than darker.
- **`{colors.surface}` / `{colors.surface-2}`** are the two grounds that make this kit: light
  panels, dark wells. They are opposite polarities on purpose, and they are why the kit owns
  **four** text tokens instead of one.
- **`{colors.canvas}`** is the file's *Background*, the dark canvas these components were
  drawn on. It survives as the modal scrim, not as the page: a light reading of this file
  means the canvas yields to the panels.
- **`{colors.border}` and `{colors.border-strong}`** both resolve to the file's single border
  colour, `#000000`. The file uses one black rule everywhere; splitting it into two greys
  would soften the thing that makes the design read as a UI kit.
- Status: `{colors.ok}`, `{colors.warn}`, `{colors.danger}`, `{colors.info}`. The file colours
  its semantics for the **dark panel** (*On Panel Error* `{colors.danger-panel}`), which no
  light ground can carry, so red exists twice: `{colors.danger}` is *Holo Error* `#ff554a`
  deepened for the light ground (a Delete button, an invalid-field hint), and
  `{colors.danger-panel}` is the file's own on-panel red for the wells (7.3:1). `ok` and
  `warn` only ever appear on the wells, so they are tuned to the panel.
- The file's **disabled** pair (`#606060` Disabled Dark, `#FFFFFF` Disabled Light) is held for
  the disabled state and recorded here rather than in the token list: `#606060` on
  `{colors.neutral}` is 4.45:1 — an honest disabled tone, deliberately below the body-text
  floor.

## Typography

Three families, and the voice belongs to the first: **Syncopate** for every heading — wide,
squared, cap-set, counters knocked out of the letterforms. It is the reason this kit does not
look like every other light theme, and it is set **open**, not tight:
`{typography.display.letterSpacing}` is a positive `0.02em`, the opposite of the usual
editorial display setting and exactly what the design does.

The file's own ladder is 42 / 32 / 16 for Syncopate headers, 24 / 18 / 12 for Nova Flat
subheads and inputs, and 14 / 12 / 10 for Montserrat body. The sizes declared above are the
ones the shared lab actually renders; keep the file's ladder in mind when sizing new work.

**Nova Flat** takes the third slot — subheads, form and UI chrome (labels, badges,
placeholders, captions). It is not literally monospaced and the design never asks for a mono:
what it asks for is a flat, technical detail voice, and Nova Flat is it. **Montserrat** carries
body copy at 0.95rem / 1.6. Buttons are Syncopate in the file, on a 24 / 16 / 12 ladder — the
lab's `.btn` inherits the body face, so set them explicitly in your own build.

## Layout

Borders do the structure. 1px black rules separate every section, frame every card and outline
every input and badge, so a page built with this kit reads as a stack of ruled panes rather
than a set of floating surfaces. Keep `spacing.md` (16px) as the floor between two surfaces and
`spacing.lg` (28px) between groups.

The chamfer means a shape never has four square corners, so give the diagonal room: do not butt
two clipped shapes together on the cut edge, and do not put a rounded child inside a chamfered
parent.

## Elevation & Depth

The file's depth is an **emboss plus a holo halo**, and both are reproduced:

- `--shadow-1` — resting cards: drop `2px 4px 4px rgba(0,0,0,.25)` plus an inner light
  `inset 1px 1px 2px rgba(205,205,205,.25)`, the file's `#CDCDCD40` emboss.
- `--shadow-2` — elevated cards: the same pair at `4px 8px 8px / .30`.
- `--glow` — the primary button and only the primary button: the file's cyan halo stack,
  `#15B9FF40` at radius 2 and 8.
- `--blur: blur(2px)` — the file's background-blur radius is 2, and that is all the frost this
  kit gets. It is texture, not glassmorphism.

`clip-path` clips an element's box-shadow and outline along with its pixels, so on the
chamfered buttons and cards the halo and the outer drop are re-expressed as `drop-shadow()`
filters, which follow the clipped silhouette. The inner emboss needs no such treatment — it is
painted inside the shape.

## Shapes

Two systems, one language. Radii are 2 / 3 / 4px (`{rounded.sm}` / `{rounded.md}` /
`{rounded.lg}`) — the file rounds 2-4px at most — and `{rounded.pill}` is **2px**, because this
kit has no pills: a badge is a chamfered tag and the avatar is a clipped chip.

The signature is `--cut: 12px` plus the `--clip` polygon, a 45° chamfer on opposite corners
(top-left and bottom-right). `--cut` is the single knob: raise it for a more brutal silhouette,
set the polygon to `none` to opt out.

One caveat, by construction: **`clip-path` cuts the border along the diagonal**. The chamfered
edge is borderless — a 45° black rule cannot follow a 45° cut twice. That is a known limitation
of the technique, not a bug, and the straight edges still carry the rule.

The file's brand glyph is a diagonal slash; `--cyber-angel-slash` in `tokens.css` exposes it as a
repeatable 45° hatch for hero art, dividers and print, alongside `--cyber-angel-holo` (the fill
ramp), `--cyber-angel-halo` (the halo as a radial wash) and `--cyber-angel-halo-ink` (`#15B9FF40`,
which is also the drop-shadow under the primary button).

## Components

- **button-primary** — `{colors.primary}` holo fill with `{colors.on-primary}` ink, 3px radius,
  a 12px chamfer and the cyan halo. Hover brightens to `{colors.primary-hover}` (the file's
  halo light) rather than darkening: the label is dark ink, so a lighter fill means *more*
  contrast, not less (7.0:1).
- **button-secondary** — transparent, a black rim and a `{colors.tertiary}` label; hover fills
  with the 14% `{colors.accent-soft}` tint. It reads as a pane of the page inside a heavy frame.
- **card** — `{colors.surface}` inside a 1px `{colors.border}` rule with the emboss. Hover the
  ghost button inside it and you meet the other ground: `card-elevated` steps the fill to
  `{colors.surface-2}`, the dark Panel, and swaps its ink to `{colors.on-surface-2}`.
- **input** — the dark Panel with a black rim and `{colors.on-surface-2}` ink (10.2:1); the
  placeholder drops to `{colors.on-surface-2-muted}` (7.7:1). Focus swaps the rim to the holo
  light `{colors.secondary}` — a ring would be clipped away by the chamfer.
- **badge** — a chamfered tag, 2px radius, Nova Flat, uppercase, on the dark Panel:
  `{colors.on-surface-2-muted}` by default, the status inks for the variants, and
  `{colors.danger-panel}` where a danger badge needs the panel's own red.
- **avatar / media / progress** — any gradient runs `{colors.primary}` → `{colors.secondary}`,
  holo fill to holo light, with `{colors.on-primary}` ink on top (8.5:1 at the light end).

## Do's and Don'ts

**Do**

- Keep the two polarities honest: light shell (`{colors.surface}`), dark wells
  (`{colors.surface-2}`). Every ink choice in this kit follows from which of the two it sits on.
- Use `{colors.tertiary}` wherever accent text meets a light ground, and the
  `{colors.on-surface-2}` pair on the wells.
- Let the black rule and the chamfer do the work — they are the identity at thumbnail size.
- Keep the holo halo for the primary action only; a page of glows is a page of noise.

**Don't**

- Don't use `{colors.primary}` as a text colour on a light ground (1.6:1), and don't put
  `{colors.text}` on `{colors.surface-2}` — the wells have their own ink pair.
- Don't round anything above 4px, and don't reintroduce pills.
- Don't put `{colors.warn}` or `{colors.ok}` on a light ground; they are panel colours.
- Don't put a gradient in `colors:` — the holo ramp lives in `tokens.css` (`--cyber-angel-holo`), and
  the file's two gradient stops are shipped as `{colors.primary}` and `{colors.secondary}`.
