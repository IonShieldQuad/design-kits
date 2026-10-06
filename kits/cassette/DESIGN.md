---
version: alpha
name: Cassette
description: Warm 70s/80s hi-fi hardware — a beige plastic shell with a moulded sheen, brushed aluminium trim, chunky controls pressed into the panel, and exactly one amber LED that lights up.
colors:
  primary: "#e86f0a"
  primary-hover: "#fb8118"
  primary-ink: "#241708"
  primary-text: "#7a3600"
  primary-text-hover: "#632900"
  secondary: "#2f8e85"
  tertiary: "#274669"
  neutral: "#dcd1b6"
  ground-top: "#e2d8bf"
  ground-bottom: "#d3c6a6"
  surface: "#e9e0c9"
  surface-2: "#cabc9b"
  text: "#2b2115"
  text-muted: "#514327"
  success: "#18522a"
  warning: "#624502"
  error: "#8b1e0e"
typography:
  display:
    fontFamily: Overpass
    fontSize: 2.9rem
    fontWeight: 700
    lineHeight: 1.06
    letterSpacing: "-0.015em"
  heading:
    fontFamily: Overpass
    fontSize: 1.3rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: "-0.005em"
  body:
    fontFamily: Overpass
    fontSize: 0.95rem
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: Overpass Mono
    fontSize: 0.72rem
    fontWeight: 500
    lineHeight: 1
    letterSpacing: "0.1em"
  readout:
    fontFamily: Overpass Mono
    fontSize: 0.95rem
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: "0.01em"
rounded:
  sm: 4px
  md: 8px
  lg: 12px
  pill: 999px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 28px
  xl: 44px
components:
  page:
    backgroundColor: "{colors.ground-top}"
    textColor: "{colors.text}"
    typography: "{typography.body}"
  panel-well:
    backgroundColor: "{colors.ground-bottom}"
    textColor: "{colors.text}"
    rounded: "{rounded.lg}"
    padding: 20px
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.primary-ink}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: 12px 20px
    height: 40px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.primary-ink}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary-text}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: 12px 20px
    height: 40px
  button-secondary-hover:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.primary-text-hover}"
    rounded: "{rounded.md}"
  button-ghost:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.text-muted}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: 12px 20px
  button-danger:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.error}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: 12px 20px
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
    padding: 20px
  card-title:
    textColor: "{colors.text}"
    typography: "{typography.heading}"
  card-media:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.md}"
    height: 96px
  card-media-2:
    backgroundColor: "{colors.secondary}"
    rounded: "{rounded.md}"
    height: 96px
  input:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 12px
    height: 40px
  badge:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text-muted}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: 5px
  badge-accent:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.primary-text}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: 5px
  badge-ok:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.success}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: 5px
  badge-warn:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.warning}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: 5px
  badge-danger:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.error}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: 5px
  table-header:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-muted}"
    typography: "{typography.label}"
  alert-info:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.tertiary}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 16px
  alert-ok:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.success}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 16px
  alert-warn:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.warning}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 16px
  alert-error:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.error}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 16px
  link:
    textColor: "{colors.primary-text}"
    typography: "{typography.body}"
---

## Overview

**A theme built from a physical object, not a screen.** Cassette is the front panel of a 1970s
receiver, not a page about one. The ground is warm beige *plastic* — #e2d8bf at the top lip
settling to #d3c6a6 in the lower case, a mid-tone no paper kit in this set reaches — with a
moulded sheen across it, brushed aluminium for trim, and controls that are big enough to feel
like they have travel. "Chunky" is a real specification here: `--border-w: 2px` moulded seams,
radii from 4px to a full pill, and generous padding.

**Exactly one thing on this panel lights up.** The amber/orange LED (#e86f0a) fills the primary
button, the checked toggle, the progress bar and the media plate, and nothing else. It is a lamp
behind a beige bezel, so it is a *fill* — as small lettering on beige it measures 1.85:1 and is
invisible, which is why accent-as-text is a separate much darker burnt orange (`{colors.primary-text}`,
#7a3600). A real panel solves the same problem the same way: the lamp glows, the silkscreen is
painted in dark ink.

**The ink is warm brown, never grey.** A plastic panel's lettering is warm dark brown or black
(#2b2115); a neutral grey would read as a different material entirely. The ink is deliberately not
lightened to keep the page "soft" — a warm beige ground eats contrast fast, and the luxury of a
beige page is paid for by an unapologetically dark ink.

**Depth runs inwards.** Every surface is pressed into the shell: `--shadow-1` and `--shadow-2` are
inset stacks (lit top lip, shadowed bottom lip, short falloff into the well) and there is no soft
outer drop shadow in the kit at all. A control you press is a control that is *inset into a panel*.

One sentence: *the front panel of a 1970s receiver — beige plastic, brushed aluminium, chunky
controls pressed into the shell, and one amber LED doing all the acting.*

## Colors

- **Primary (#e86f0a):** the amber/orange LED. The single action colour: the primary button, the
  checked toggle, the progress bar, the media plate, the focus halo's family. It is a *fill*
  colour and earns its place by being the only saturated thing on the panel.
- **Primary-hover (#fb8118):** the lamp turned **up**. On a light kit the reflex is to darken on
  hover, but darkening #e86f0a drops the label to 4.1:1 — below AA on the state you are most
  likely to be looking at. Brightening raises it to 6.9:1 and is the physically honest move: an
  LED coming up, not a lamp changing colour.
- **Primary-ink (#241708):** the panel ink printed on the amber plate. Amber takes dark ink,
  never white — white on #e86f0a is ~2.4:1.
- **Primary-text (#7a3600) / primary-text-hover (#632900):** amber *as text* — eyebrows, links,
  active nav and tabs, secondary-button labels, inline code, `.table code`. 5.3:1 on the shell
  and 4.8:1 on the deepest inset, where the fill colour manages 1.85:1.
- **Secondary (#2f8e85):** meter teal — the one cool note in the kit, the tint of a lit tuning
  dial. It is the second stop of media plates and progress bars and nothing else. It never acts.
- **Tertiary (#274669):** petrol blue. Data and telemetry only, so a readout never borrows the
  action lamp.
- **Neutral (#dcd1b6):** the shell — the page ground's solid stand-in. `colors:` cannot hold a
  gradient (linter error), so the two ramp stops ship as colours of their own: **ground-top
  (#e2d8bf)** and **ground-bottom (#d3c6a6)**, referenced by the `page` and `panel-well`
  components.
- **Surface (#e9e0c9) / surface-2 (#cabc9b):** the sub-panel face and the inset bay. Note the
  direction: the *card* is a shade **lighter** than the shell (a plate catching the light) and the
  *inset* is a shade **darker** (the same plastic pressed deeper). Both are the same material —
  neither is white paper and neither is a dark well.
- **Text (#2b2115) / text-muted (#514327):** the two contrast-guaranteed steps of the warm brown
  ink.
- **Success (#18522a) / warning (#624502) / error (#8b1e0e):** the status inks — moulded green,
  dark ochre, record red. All three sit far below the amber in value, so a caution chip never
  reads as the action lamp, and all three are checked on `--surface-2` (the darkest ground any of
  them is drawn on) rather than on the easy pale one.

Deliberately not in the map above: `--text-dim: #5a4a2d` (captions, hints, table headers),
`--accent-ink-hover`, `--border: #b6a684` / `--border-strong: #8f7f5f` (the moulded seams),
`--accent-2`'s role as a fill, and `--accent-soft: rgba(232,111,10,.15)`. The DESIGN.md component
schema has no `borderColor` property, and a translucent tint is not a colour — listing them would
only produce orphan warnings for values that are very much in use. Their exact values are in
`tokens.css`.

## Typography

Two families, and they are the **same drawing at two widths**:

- **Overpass — display and body.** Derived from Highway Gothic, the American signage face: drawn
  to survive paint and stencils at small sizes on a physical panel. A mechanical/technical
  grotesque with a squarish, engineered set and an honest wide stance, which is what a front
  panel's lettering looks like. It sets the h1, the section headings, every sentence and every
  card body.
- **Overpass Mono — labels, eyebrows, badges, table headers, readouts.** The same skeleton at one
  width: a panel's silkscreen and its spec plate share a hand, so the label face and the body face
  being the same family is the point, not a shortcut.
- **Readout (mono, 0.95rem, +0.01em, weight 500)** — the middle register: table cells, IDs,
  version strings and numerals, very slightly opened so a column of figures lines up as
  instrumentation.
- Caps labels are tracked **+0.1em** (`--tracking-caps`): stamped, compressed, tighter than a
  HUD's 0.14em–0.18em, because a moulded label is pressed into the plastic rather than spaced out
  on glass.

There is no third face, no retro script and nothing that reads as 1950s diner signage: the kit is
1970s *industrial*, and a script would turn a receiver into a jukebox.

**One honest seam.** The shared lab styles `.btn` with `font: inherit`, so buttons drawn in the lab
take their text from `--font-body`. The kit's declared button face is still the mono
(`{typography.label}` in `components:`), and the spec is what consumers copy. Nothing in the
contract needs fixing for this — it is recorded rather than papered over.

## Layout

The shared column (`min(1040px, 100% - 2.5rem)`) over a shell ground. Section boundaries are 2px
moulded seams with generous vertical padding; inside a panel the rhythm stays tight (8–14px) so
controls group by proximity rather than by boxing. Cards are an auto-fit grid that collapses to one
column on a phone.

Controls are deliberately roomy: 40px control height, 12px×20px button padding, 20px card padding.
A panel that feels like it has travel needs the space to be wrong about nothing — a chunky control
cramped into a dense layout reads as a bug, not as a texture.

## Elevation & Depth

**Depth is engraved, not floating.** `--shadow-1` and `--shadow-2` are inset stacks: a lit top lip
(`inset 0 1px 0 rgba(255,252,240,.55)`), a shadowed bottom lip (`inset 0 -2px 0 rgba(94,74,44,.20)`)
and a short soft falloff into the well (`inset 0 3px 8px -4px rgba(72,55,30,.42)`). `card-elevated`
uses `--surface-2` and `--shadow-2`, so it is *more* pressed in, not more lifted: a deeper bay in
the same shell.

The lip alphas are deliberately above the "barely there" 5% range. At 5% a 1px highlight does not
survive a normal-density display, and a bevel nobody can see is not a bevel — on beige, where the
ground itself is mid-tone, the falloff term is what sells the recess.

The one place the kit leaves the panel is `--glow`: the shared lab wires `.btn-primary`'s
`box-shadow` to `--glow` rather than to a shadow token, so `--glow` is the amber lamp's halo —
a warm bleed onto the shell plus an inner gloss on the plate. It is applied to the energised
control only. Panels never wear it. `--blur: none`: moulded plastic is not frosted glass, and a
blurred panel would undo the entire premise.

## Shapes

Chunky and moulded: `--radius-sm: 4px`, `--radius-md: 8px`, `--radius-lg: 12px`, and
**`--radius-pill: 999px`** — a full pill, because a hardware tag and a toggle on this panel are
round-ended. That is the largest radius in the set (geometric-dimensions rounds nothing at 0–2px;
inside-the-machine caps at 4px) and it is what makes a button here read as soft moulded plastic
rather than card stock or milled metal.

`--cut: 0px` — this panel is moulded, so it has no chamfer. Corner cuts belong to the kits that
cut their aluminum.

## Components

- **button-primary** — the amber plate: panel ink in the mono label style (`{typography.label}`),
  8px radius, 2px moulded rim, and the only element in the kit allowed to glow. It is the LED.
- **button-primary-hover** — the same plate with the lamp turned **up** (#fb8118), still panel ink.
  See Colors for why hover brightens rather than darkens.
- **button-secondary / button-ghost / button-danger** — sub-panel or open plates with burnt-orange,
  muted-brown or record-red labels. Secondary actions are pressed into the panel, never filled:
  only one thing on this panel lights up.
- **card / card-elevated / panel-well** — the sub-panel face, the deeper inset bay, and the shell
  tone. All three are inset; none floats.
- **card-title** — Overpass at weight 600. Titles are labels you can read across a room.
- **card-media** — the only full-saturation block in the kit: the amber LED as a plate, with
  `card-media-2` in meter teal.
- **input** — the inset bay (`{colors.surface-2}`) with a 2px moulded rim; on focus the rim takes
  the amber and the well takes a 3px `--accent-soft` halo, so an input lights up like a control.
- **badge** — a full pill in the inset bay; `badge-accent`, `badge-ok`, `badge-warn` and
  `badge-danger` recolour the label and leave the plate as the shell, so a status row reads as
  silkscreen, not as blocks of paint.
- **table-header** — mono, uppercase, +0.1em, muted: the engraved column legend.
- **alert-*** — a sub-panel with a 3px rule down the left edge (petrol, green, dark ochre, record
  red), one step wider than the panel's own 2px seam so the rule reads as a lamp.
- **link** — burnt orange, underlined on hover: the same ink family as the action, because a link
  is an action even when it is not a lamp.

## Do's and Don'ts

- **Do** keep the amber for the one thing that lights up. Everything else on the panel is printed.
- **Do** set amber text in `{colors.primary-text}` (#7a3600), never the LED fill. The fill is
  1.85:1 as small lettering and no amount of weight rescues it.
- **Do** express depth with inset lips. If an element needs an outer shadow to be legible, it is
  the wrong element.
- **Do** keep the ink warm and dark. A grey or lightened ink turns beige plastic into manila paper.
- **Do** leave the controls roomy — 40px tall, 8px radius, 2px rims. Chunk is a measurement.
- **Do** brighten the primary button on hover. The lamp comes up; it never changes hue.
- **Don't** introduce a second saturated action colour. Teal is media, not action.
- **Don't** put white text on the amber plate. It takes panel ink (#241708).
- **Don't** frost anything. `--blur` is `none`; this is moulded plastic, not glass.
- **Don't** put the LED glow on a panel. Glow belongs to an energised control.
