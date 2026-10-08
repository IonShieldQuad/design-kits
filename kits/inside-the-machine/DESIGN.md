---
version: alpha
name: Inside the Machine
description: Machined instrumentation — a graphite chassis with engraved panels, drawn carbon-fibre cloth, a punched vent plate and brushed steel, opaque steel hairlines, amber for action, green phosphor for readouts, and IBM Plex Mono carrying the interface.
colors:
  primary: "#ffb000"
  primary-hover: "#ffc233"
  primary-ink: "#0d0f11"
  secondary: "#4dff9e"
  tertiary: "#6c99b8"
  neutral: "#0d0f11"
  surface: "#16191d"
  surface-2: "#1b1f23"
  text: "#e9edef"
  text-muted: "#9aa4ad"
  success: "#4dff9e"
  warning: "#d99a2b"
  error: "#ff5147"
typography:
  display:
    fontFamily: IBM Plex Mono
    fontSize: 2.9rem
    fontWeight: 600
    lineHeight: 1.06
    letterSpacing: "-0.01em"
  heading:
    fontFamily: IBM Plex Mono
    fontSize: 1.3rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: "-0.005em"
  readout:
    fontFamily: IBM Plex Mono
    fontSize: 0.95rem
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: "0.01em"
  body:
    fontFamily: IBM Plex Sans
    fontSize: 0.95rem
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: IBM Plex Mono
    fontSize: 0.72rem
    fontWeight: 500
    lineHeight: 1
    letterSpacing: "0.12em"
rounded:
  sm: 2px
  md: 3px
  lg: 4px
  pill: 4px
spacing:
  xs: 4px
  sm: 8px
  md: 14px
  lg: 24px
  xl: 40px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.primary-ink}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: 14px 18px
    height: 38px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.primary-ink}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: 14px 18px
    height: 38px
  button-secondary-hover:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.primary-hover}"
    rounded: "{rounded.md}"
  button-ghost:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.text-muted}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: 14px 18px
  button-danger:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.error}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: 14px 18px
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
    backgroundColor: "{colors.neutral}"
    rounded: "{rounded.sm}"
    height: 96px
  card-media-2:
    backgroundColor: "{colors.secondary}"
    rounded: "{rounded.sm}"
    height: 96px
  input:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 12px
    height: 38px
  badge:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text-muted}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: 5px
  badge-accent:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.primary}"
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
    padding: 14px
  alert-ok:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.success}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 14px
  alert-warn:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.warning}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 14px
  alert-error:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.error}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 14px
  link:
    textColor: "{colors.primary}"
    typography: "{typography.body}"
---

## Overview

Inside the Machine is the *interior* of an instrument, not a product page about one. A graphite
chassis (#0d0f11) with panels milled into it, seams drawn as opaque 1px steel hairlines rather
than translucent white, and two phosphor lamps doing all the talking: **amber (#ffb000) acts,
green (#4dff9e) reports, red (#ff5147) faults.** Depth runs *inwards* — every panel is a recess
with a lit top lip and a shadowed bottom lip — so nothing floats above the chassis.

The same is true of the **controls**. A field is a milled *well*, a button is a beveled *plate*
seated in the panel, the native checkbox and radio are squared *sockets*, and the nav/tab/toggle
chrome takes the same recess-and-bevel language. The components are cut from the chassis, not laid
on it — a colour scheme alone left them reading as flat dark UI, which is exactly what this kit
exists not to be.

It is the one kit in this set where **mono is the interface, not a label font.** IBM Plex Mono
sets the headings, the eyebrows, the table headers, every badge, the metadata and every number;
IBM Plex Sans is the fallback voice, used only where the reader is reading sentences instead of
reading instruments. That inversion — and the warm amber-on-graphite ground — is what separates it from
Signal (navy HUD, Chakra Petch headings, cyan action) and Cyberpunk (near-black, magenta
action, neon bloom).

**The material is drawn, not tinted.** A palette this dark reads as a *colour scheme* until real
surfaces appear, so three textures are drawn (as base64 SVG data URIs, the one place a token may
hold artwork) and do three genuinely different jobs:

1. **A woven carbon-fibre cloth** — `--inside-the-machine-weave`. A 2/2 twill: continuous warp
   and weft tows whose over/under crossings step one column per row, so the sheen forms diagonal
   bands and it reads as interlace, not a beveled grid — under a **raked specular sweep** (a
   hard-stepped lit → flat → shadowed diagonal) so the light falls across the cloth at an angle.
   This is the kit's *surface*; it is milled into the media panel through `--media-bg`, the one
   place the lab shows a surface rather than a colour.
2. **A punched vent plate** — `--inside-the-machine-grille`. Each hole is a near-black well
   (r 3.15) inside a bright lit ring offset down 0.8px, so the lower lip catches the light. This is
   *structure*: the plate is perforated, not dotted.
3. **Brushed steel lit by a specular band** — `--inside-the-machine-steel`. Vertical striations
   over hard bands — a lit top rim, the bright specular band, a machine-mark line, a dark chamfer
   foot — with the grain in **two overlapping co-prime periods** and a **raked specular band** so
   it reads as metal rather than as a printed stripe. This is *light*.

Each tile is proved non-flat at 168×72 (pixel standard deviation in the README); the library's
most repeated defect is a motif tuned so subtly that its tile renders blank.

One sentence: *a machined instrument panel — amber for the one thing that acts, green phosphor
for everything it reports, over carbon cloth and brushed steel.*

## Colors

- **Primary (#ffb000):** amber. The single action colour. It fills the primary button, links,
  the focus ring's hue family, and the toggle's checked state — and nothing else. On this
  machine one lamp means "press it".
- **Primary-hover (#ffc233):** amber lifted one visible step. Never white, never a different
  hue — a lamp getting brighter, not changing colour.
- **Primary-ink (#0d0f11):** the chassis ink printed on the amber plate. Amber is a *fill*, so
  the label on it is graphite, not white.
- **Secondary (#4dff9e):** green phosphor. Readouts, media plates, progress, charts. The second
  accent, and the same green as `success` — see the note on shared lamps below.
- **Tertiary (#6c99b8):** steel blue. Data and telemetry only; it is a cool note that never
  competes with the two phosphor lamps.
- **Neutral (#0d0f11):** the graphite ground, and the base the carbon cloth is woven on.
- **Surface (#16191d) / surface-2 (#1b1f23):** the panel face and the recessed well. A two-step
  rise — small enough that a panel reads as *cut into* the chassis rather than laid on it.
- **Text (#e9edef) / text-muted (#9aa4ad):** the two contrast-guaranteed text steps, both cool
  graphite-adjacent greys rather than pure white, so lamps stay the brightest thing on screen.
- **Success (#4dff9e) / warning (#d99a2b) / error (#ff5147):** the lamps. Warning is amber
  *held one step down* from the action colour on purpose: a caution chip and a primary button
  are the same family, but a stamp is never as loud as a switch.

Deliberately not in the map above: `--text-dim: #828d95` (captions, placeholders, timestamps),
`--border: #2a2f35` / `--border-strong: #4a535c` (the steel seams), `--info: #6c99b8`, and
`--accent-soft: rgba(255,176,0,.13)`. The DESIGN.md component schema has no `borderColor`
property, and a translucent tint is not a colour — listing them would only produce orphan
warnings for values that are very much in use. Their exact values are in `tokens.css`.

**The material greys live in the artwork, not the palette.** The three drawn textures introduce
their own steel tones (a tow highlight `#99a5b2`, a steel specular `#f2f6f9`, a punched-plate lip
`#95a2b0`… — exact stops in `tokens.css`). They are the *shading of a drawn object*, not surfaces
a consumer paints with, so they are not palette tokens and not in the map above — the same way a
rose does not need its petal tint to be a theme colour. Every surface a consumer *does* paint
with is a palette colour, unchanged from before this kit grew a material.

## Typography

Two families, and the *mono is the primary one*:

- **IBM Plex Mono — display, headings, labels, controls, tables, numbers.** Engineered to be
  read at small sizes and in columns, which is what a readout is. It sets the h1 and section
  headings, every eyebrow, every badge, every table header, the swatch captions and the metadata.
  Caps labels and control captions are tracked `+0.12em` — a stamped plate, tighter than a HUD's
  `0.14em–0.18em`, because stamping compresses letters rather than spacing them out.
- **IBM Plex Sans — body copy only.** The *fallback voice*: paragraphs, card bodies, hint text.
  It is deliberately the same superfamily as the mono, so the two never look like two kits
  fighting; the sans simply means "this is a sentence, not a reading".
- **Readout (mono, `0.95rem`, `+0.01em`, weight 500):** the middle register — table cells,
  metrics, IDs, version strings. Slightly heavier and very slightly open, so a column of
  numerals lines up and reads as instrumentation.

There is no separate display face. The mono carries the largest type in the kit; that is the
position, not an omission.

**One honest seam.** The shared lab styles `.btn` with `font: inherit`, so the buttons rendered
in the lab draw their text in `--font-body`. The kit's own button style is still the mono label
(`{typography.label}` in `components:`), and the spec is what consumers copy; the mono is what
"buttons" means here. Nothing in the contract needs fixing for this — it is simply the one place
where the shared lab's own inheritance overrides a kit's declared component face, and it is
recorded rather than papered over.

## Layout

The shared column (`min(1040px, 100% - 2.5rem)`) over a chassis ground. Section boundaries are
1px steel seams with generous vertical padding; inside a panel the rhythm is tight (8–14px) so
readouts group by proximity rather than by boxing. Cards are an auto-fit grid that collapses to
one column on a phone.

Because the mono is wide, text blocks are kept narrower than a grotesque layout would need:
body copy caps around 62ch and control labels stay short. Dense material — tables, badge rows,
progress bars — is this kit's natural content, not its edge case.

Texture never sits under type. The carbon cloth (media panels) and the steel rail are painted on
boxes that carry no text; the page ground, masthead and every label sit on flat graphite or flat
panel tones, so the drawn material adds hardware without ever moving a contrast ratio. That is a
rule, not a coincidence: `--text-dim` clears 4.55:1 only against grounds at or below `#1b1f23`,
so a textured ground under type could not both be visible and be legible.

## Elevation & Depth

**Depth is engraved, not floating.** There is no soft outer drop shadow anywhere in this kit;
the lab's card gets its depth from `--shadow-1`, which is an inset stack — a 2px lit top lip
(`inset 0 2px 0 rgba(255,255,255,.10)`), a 2px shadowed bottom lip
(`inset 0 -2px 0 rgba(0,0,0,.62)`) and a short soft falloff into the well
(`inset 0 3px 9px -4px rgba(0,0,0,.48)`). The panel reads as a plate sitting *below* the chassis
surface. The lips are **2px**, not 1px, so a panel edge is cut with the same chamfer as a control
edge (`--machine-bevel`); a 1px lip disappeared at normal density and left the card reading flat.
`--shadow-2` deepens the recess (a brighter rim on a longer `16px` inner falloff);
`card-elevated` is therefore *more* cut-in, not more lifted — a milled well with light on its
rim, which is the correct reading of "elevated" on a machined face.

Inputs carry the same logic at the pixel scale: `--input-inset` (which *is* `--machine-recess`, so
a field, the nav channel, the tab row and the toggle track share one definition) drops a hard
shadow line and a 5px falloff from the inside top lip, lights a line at the inside bottom, and
rings all four edges with a dark inner wall. A field is a *hole in the panel* rather than a chip
laid on it — and it reads that way even though `--surface-2` is tonally a step *lighter* than the
card, because the recess, not the fill, is what carries it.

**Controls are plates with a hard chamfer.** `--btn-shadow` (which *is* `--machine-bevel`) is a 2px
lit top lip, a 3px shadowed bottom lip, lit/dark side lips, a hard zero-blur seat shadow, and a
last-layer 8% face lift. The face lift is what gives a **transparent** variant — secondary, ghost
and danger have no `--_bg` — a plate for the bevel to sit on; without it those controls are
outlines and read flat. On the amber plate the lift is invisible.

The lip alphas are deliberately above the "barely there" range (5%): at 5% a 1px highlight does
not survive a normal-density display, and a recess nobody can see is not a recess. The falloff
term is what sells it at viewing size — a 1px line alone reads as an outline.

`--glow` is reserved for controls that are *energised*, and it is **zero-blur**:
`0 0 0 1px rgba(255,176,0,.55)`, `0 0 0 3px rgba(255,176,0,.14)` and the shared bevel. It was once a
`14px` blurred halo; the blur was the last thing on the page reading as modern UI, so the lamp is
now an *anodised bezel* rather than a bloom — the machine reads as milled, not as glowing. It is
still the amber switch's alone; panels never wear it. `--blur: none`: machined metal is not frosted
glass, and translucent panels would undo the recess.

## Shapes

Small and hard: `--radius-sm: 2px`, `--radius-md: 3px`, `--radius-lg: 4px`. Nothing is
rounder than 4px, because a machined edge is a milled edge, not a soft one. `--cut: 0px` —
this kit does not chamfer; the seam does that job (Signal owns the corner cut, and reusing it
would blur the two kits together).

**The shape that matters here is not a radius — it is the drawn form.** A weave is a crossing of
tows, a grille is a punched hole, a rail is a lit chamfer; none of the three can be expressed as
a corner treatment, and all three are rectangular tiles repeated at their own size
(`--inside-the-machine-weave` at 24px, `--inside-the-machine-grille` at 12px). Radius stays 2–4px
so the *only* curves on screen are the punched holes and the woven sheen — the machine's own
geometry, not a soft UI.

The one deliberate contract bend: **`--radius-pill` is 4px, not 999px.** A badge on this
machine is a stamped rectangular plate; a lozenge would read as a pill-shaped tag from a
product UI. The token keeps its name for the contract. It also reaches the shared lab's own
switch, whose track and knob are drawn at `--radius-pill`: at 4px the toggle is a squared rocker —
the right answer here rather than an accident — and `kit.css` seats it as a milled track with a
beveled knob.

Native checkbox and radio **ignore** `border-radius`, so a kit that lives at 4px cannot leave a
perfectly round radio in place. `--check-appearance: none` plus the `--check-*` box tokens square
both. Unchecked is a small milled socket (`--surface-2` with a `--border-strong` rim); checked is
a lit amber plate — the lab paints the fill, so "on" is a *lamp*, which is this machine's own
vocabulary (at the cost of the tick glyph; see the README).

## Components

- **button-primary** — the amber plate: graphite label in the mono label style (`{typography.label}`),
  3px radius, and the only element in the kit that wears the lamp. Since the machining pass it
  wears the shared `--machine-bevel` too (folded into `--glow`), so its edge matches every other
  variant's. (The shared lab renders `.btn` with `font: inherit`, so the lab's own button text is
  drawn in the body face; see Typography.)
- **button-primary-hover** — the same plate with the lamp turned up (`#ffc233`). Still graphite
  ink; the hue never changes.
- **button-secondary / button-ghost / button-danger** — a panel plate with an amber, muted or
  fault-red label. They have no `--_bg` in the shared lab, so the 8% face lift inside
  `--machine-bevel` is what gives them a plate; the bevel then reads as a machined edge instead of
  three outlines. Secondary actions are recessed by tone, never filled with the accent.
- **checkbox / radio** — squared stamped sockets (`--check-appearance: none`). Unchecked is a milled
  well; checked is a lit amber plate. The radio, which Chromium draws as a circle, is the control
  that most needed this.
- **nav / tabs / toggle** — the shared lab draws these three with no shadow hook, so `kit.css`
  seats the nav bar and the tab row as `--machine-recess` channels, the current nav pill and
  current tab as `--machine-bevel` plates, and the toggle as a recessed track with a beveled knob.
- **card / card-elevated** — the milled panel and the deeper well. Both inset; both bounded by
  a steel seam; neither floats.
- **card-title** — mono, weight 600. Titles are labels you can read across the room.
- **card-media** — a milled blank of **woven carbon-fibre cloth**, not a colour swatch. The panel
  is drawn by `--media-bg: var(--inside-the-machine-weave)` and held at full strength with
  `--media-op: 1`; at the default `.85` the weave washed out to a grey tint. This is the kit's
  one surface rather than a colour, and the place the material is most legible — the lit corner of
  the raked sweep falling away to shadow is what sells it as cloth rather than as a printed tile.
- **input** — `surface-2` well, `--border` seam, amber focus with a soft `--accent-soft` halo,
  and `--input-inset` (= `--machine-recess`) so it reads as *recessed into* the panel — a hard
  shadowed top lip, a lit bottom lip and a dark inner wall. An input is a hole in the panel, so it
  is the *darker* of the two surface steps in spirit even though it is tonally one step up.
- **badge** — a 4px-cornered stamped plate; `badge-accent`, `badge-ok`, `badge-warn` and
  `badge-danger` recolour the label and leave the plate dark, so a status row reads as lamps,
  not as blocks of paint.
- **table-header** — mono, uppercase, `+0.12em`, dim: the engraved column legend.
- **alert-*** — a panel with a 3px lamp rule down the left edge (steel blue, green, dim amber,
  fault red).
- **link** — amber, underlined on hover; the same lamp as the action, because a link *is* an
  action.
- **The signature motifs** — `--inside-the-machine-weave` (woven carbon-fibre cloth, under a raked
  specular sweep), `--inside-the-machine-grille` (punched vent plate) and `--inside-the-machine-steel`
  (brushed steel rail with co-prime grain and a raked specular band). They render as 168×72 tiles
  on `--surface-2`; the weave additionally backs the media panel. They are material, not controls,
  and carry no text.

## Do's and Don'ts

- **Do** keep amber for the one thing that acts. Everything else on this machine reports.
- **Do** express depth with inset lips. If an element needs an outer shadow to be legible,
  it is the wrong element.
- **Do** draw seams as opaque steel (`#2a2f35`), not as translucent white. Engraving is
  subtractive.
- **Do** fake material with a drawn tile and a fixed size (`0 0 / 24px 24px repeat`), never
  with a stretched or smoothly-faded gradient. A weave that is scaled to fill smears; a metal
  ramp reads as fog.
- **Do** set facts, IDs and numerals in mono — and headings too. The mono is the interface.
- **Do** keep radii at 2–4px and let the corners stay hard.
- **Do** declare a control edge **once** (`--machine-bevel`) and compose it into `--glow`, so the
  amber switch and the secondary plate can never wear two different bevels.
- **Don't** put white text on amber; the amber plate takes graphite ink (`--primary-ink`).
- **Don't** powder a control with a blurred halo. The lamp is an *anodised bezel* — a hard ring —
  because a bloom reads as modern UI, not as a machined panel.
- **Don't** run a texture under type. Carbon cloth, the steel rail and the grille belong on
  media blanks and signature tiles; `--text-dim` needs a ground at or below `#1b1f23`.
- **Don't** dim the media panel below `--media-op: 1`. The weave is the point; a wash defeats it.
- **Don't** introduce a third lamp. Green reports, amber acts, red faults, and the steel blue
  is data — that is the whole instrument.
- **Don't** add a glow to a panel. Glow belongs to an energised control.
