---
version: alpha
name: Space Program
description: Mission control — a near-white engineering drawing sheet with a rimmed border and a module grid, white plates bolted onto it, one agency blue that acts, and a console of drawn telemetry — a checklist, a block number and a lamp cluster. The room the mission is run from, not the sky it flies through.
colors:
  primary: "#12539f"
  primary-hover: "#0d3f80"
  primary-ink: "#0e3f8f"
  secondary: "#2b6fc4"
  tertiary: "#8f5404"
  neutral: "#fbfcfe"
  surface: "#ffffff"
  surface-2: "#e9eef5"
  text: "#0d1b2a"
  text-muted: "#4a5768"
  text-dim: "#55627a"
  invert: "#ffffff"
  success: "#10703a"
  warning: "#8f5404"
  error: "#b81b12"
  info: "#17427e"
typography:
  display:
    fontFamily: Big Shoulders Display
    fontSize: 2.8rem
    fontWeight: 700
    lineHeight: 1.02
    letterSpacing: "0.005em"
  heading:
    fontFamily: Big Shoulders Display
    fontSize: 1.32rem
    fontWeight: 600
    lineHeight: 1.18
  body:
    fontFamily: IBM Plex Sans
    fontSize: 0.95rem
    fontWeight: 400
    lineHeight: 1.55
  label:
    fontFamily: Overpass Mono
    fontSize: 0.75rem
    fontWeight: 600
    lineHeight: 1
    letterSpacing: "0.14em"
  readout:
    fontFamily: Overpass Mono
    fontSize: 0.9rem
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: "0.03em"
rounded:
  sm: 2px
  md: 3px
  lg: 4px
  pill: 2px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.invert}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: 14px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.invert}"
    rounded: "{rounded.md}"
  button-primary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.invert}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary-ink}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: 14px
  button-secondary-hover:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.primary-ink}"
    rounded: "{rounded.md}"
  button-danger:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.error}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
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
    padding: 10px
  badge:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text-muted}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: 4px
  badge-accent:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.primary-ink}"
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
  badge-danger:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.error}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
  status-caution:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.tertiary}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
  lamp-go:
    backgroundColor: "{colors.success}"
    rounded: "{rounded.sm}"
    size: 24px
  lamp-caution:
    backgroundColor: "{colors.tertiary}"
    rounded: "{rounded.sm}"
    size: 24px
  lamp-abort:
    backgroundColor: "{colors.error}"
    rounded: "{rounded.sm}"
    size: 24px
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
---

# Space Program

## Overview

Mission control: the room the mission is run from. Not the sky — `outer-space` owns the sky — and not
the pilot's weapons HUD, which is `mecha-pilot`. This is the *program*: an engineering drawing sheet,
white plates bolted onto it, and the paperwork a mission is actually flown by. A checklist, a block
number, a lamp cluster, a plotted trace.

The register is **documentation**, and the ground is **white on purpose**. `--surface` is pure white
(the wall plates), `--surface-2` is a pale cool well (fields, badges, readouts), and `--bg` is a
near-white drawing sheet with a rimmed border 14px in from the page edge, a 48px module grid and a
fine 8px drafting grid. Depth is a *hard cast edge*, not a shadow: a card is a plate standing two
pixels proud of the sheet. Ink is deep and institutional — the dark of a printed form, never a
blue-grey haze.

One colour acts. Agency blue `#12539f` is the only thing on the page that means "do this"; the signal
ladder — GO green, CAUTION amber, ABORT red — carries *state* and never an action. The second accent,
`#2b6fc4`, is the plotter pen: the same family one step brighter, for charts, second series and the
traced line. Nothing glows. Nothing is blurred. A control room clicks rather than fades.

### Deliberately not its neighbours

| | `outer-space` | `mecha-pilot` | `radioactive` | **`space-program`** |
|---|---|---|---|---|
| Mode | dark | dark | light | **light, white-dominant** |
| Premise | the vista | the pilot's HUD | the containment site | **the program office / console room** |
| Action colour | starlight gold | phosphor green | acid green | **agency blue** |
| Ground | starfield void | olive CRT | green-grey concrete | **white drawing sheet + module grid** |
| Motifs | nebulae, starfield | reticle, range scale, caution tape | trefoil, hazard tape, spill | **checklist, block number, lamp cluster** |
| Depth | blurred glow + glass | zero-blur offset | soft institutional drop | **zero-blur cast plate, no glow at all** |

## Colors

Agency blue `#12539f` is the action: the primary key, the focus ring, the active tab, and the ink of
every link and label that means "go here". Its text-safe member ships separately as `--accent-ink`
(`#0e3f8f`, 8.47:1 on the pale well and 6.69:1 even on its own 13% tint composited over it) because a
fill that carries a white label is not automatically a fill that reads as an 11px legend.

The second accent, `#2b6fc4`, is the **plotter pen** — the same family one step brighter. It belongs
to charts, second data series and the traced line in the media panel. It is never an action, and it is
deliberately not a third hue: a console room has one blue, and adding a teal "because technology"
would make this kit a different, noisier one.

The signal ladder is **clarity colouring** — colour for legibility, not decoration. GO `#10703a`
(5.30:1), CAUTION `#8f5404` (5.24:1), ABORT `#b81b12` (5.57:1) are each the brightest value their hue
can take and still carry a badge *label* on the pale well. The lamp **glass** in the drawn motifs is
the same hue one step brighter (`#16a34a`, `#e08a0c`, `#d02014`) — which is how a real lamp works:
bright glass, dark legend. That split is the whole of the kit's relationship to status colour.

The ground is white and the plate is white; they are told apart by a cast edge and a 1px joint line,
not by tint. Because a near-white kit is graded the *other way round* from a dark one, every ink is
solved against the **darkest** ground that carries type — `--surface-2` and the module-grid
intersection — and never against white. See the table in `README.md`; the numbers there are
worst-case.

## Typography

Three faces, three jobs. **Big Shoulders Display** is the display: a condensed, sign-painter's
grotesque with an engineeering-signage gait, used for headings and card titles only. **IBM Plex Sans**
is the body — a utilitarian text face designed for technical documentation, and the reason a paragraph
of this kit stays a paragraph. **Overpass Mono** is the readout: every kicker, legend, badge, table
header, caption and metric is set in it, because on this page anything that is a *fact* is printed in
the telemetry face. Overpass comes from highway signage, so it holds up at 12px in caps.

Caps labels run `+0.14em` — stencilled, but narrower than a HUD (`mecha-pilot` uses `.16em`), because
this is a formed legend on a plate rather than a glow on a screen.

## Layout

Spacing is documentation-tight and completely regular: `16px` gutters, `24px` between blocks, and a
background that draws the *sheet* rather than decorating it — a rimmed border, a 48px module grid and
an 8px drafting grid, all hard-edged. Panels align to the module grid and to each other; there is no
asymmetry and no airiness, because a form is laid out by a draughtsman. Corners are machined, 2–4px,
not rounded and not chamfered (`carbon` owns the cut corner).

## Elevation & Depth

Depth is a **cast edge**, never a shadow. A card is a white plate standing 2px proud of the sheet on
two hard rules (`--shadow-1`); an elevated card is 4px (`--shadow-2`). Fields are **milled into** the
plate rather than laid on it (`--input-inset`), the navigation is a **milled console channel**
(`--bar-shadow`) with the current item riding in it as a plate (`--bar-item-shadow`), and the switch is
a seated track with a machined knob (`--toggle-shadow`, `--toggle-knob-shadow`).

Controls are **analog keys**. A button rests on a cast edge with a top inner highlight
(`--btn-shadow`), and on press that edge **collapses into an inset well**
(`--btn-shadow-active`) — the control visibly travels into the panel. `--dur` is 80ms and `--ease` is
`linear`, so the transition snaps instead of easing: it clicks. Nothing in the kit is blurred:
`--blur: none`, and there is not a single radial gradient in the file.

## Shapes

The kit's geometry is three drawn devices, each doing a different job — the procedure, the identity,
the state:

- `--space-program-checklist` — **the procedure**. A blocky flight-checklist strip: a filled header
  bar, three ruled columns, three *ticked* square boxes and one open box, with value leaders struck
  down the right. A repeating gradient makes an even rule pattern; it cannot make a tick inside a box.
- `--space-program-blocknumber` — **the identity**. A drawing title block: a heavy frame, a hatched
  revision cell, a dark binding edge, and a stencil numeral (`04`) drawn as exact geometry with its
  stencil breaks, plus a legend rule beneath it.
- `--space-program-lamps` — **the state**. A console lamp cluster: four square lamps in dark bezels
  with a bright glass, a hard specular band and a leader rule, seated in a milled channel —
  GO · CAUTION · ABORT · OFF.

The plotted trace and the graduation strip are **not** a fourth tile: they live on the card media
panel (`--media-bg`, a plotter output with a drafting grid, a two-pen trace and a numbered
graduation), which is where a plot belongs.

## Components

Buttons are agency-blue keys with white labels or white plates with blue labels; **every** variant
wears the same cast edge and the same collapsed pressed state, so the whole control layer is one
physical object. Cards are white plates on a cast edge; the elevated card is the pale well. Inputs
are milled, with a square native checkbox drawn as a checklist box (`--check-appearance: none`,
`--check-radius: 0px`). Badges are stamped plates carrying mono caps: on the pale well for the neutral
one, on the sheet for the signal ones. Media panels are plotter output, opaque. Progress and the avatar
are a **segmented console channel** (`--fill-bg`), hard-stopped, with both segments dark enough for the
white label.

## Do's and Don'ts

- **Do** keep the ground white and the plates whiter. This kit's whole premise is that a console room
  is a bright room.
- **Do** keep exactly one action colour. Blue acts; green, amber and red only report.
- **Do** keep the ladder legible: a status colour is used at the brightest value that still clears
  4.5:1 as a label, and lamp *glass* is brighter than lamp *legend*.
- **Do** keep every control a physical key — cast edge at rest, inset well when pressed, 80ms linear.
- **Do** let the checklist, the block number and the lamp cluster do the identifying work.
- **Don't** add a glow, a blur or a soft shadow. There is no bloom in this kit; `--glow` is a
  machined rim on the primary key, not a halo.
- **Don't** round anything above 4px or chamfer a corner — `carbon` owns the cut corner.
- **Don't** put a starfield, a nebula or a spacecraft in it. That is `outer-space`, and it is the sky;
  this is the room.
