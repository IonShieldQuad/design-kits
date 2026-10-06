---
version: alpha
name: Inside the Machine
description: Machined instrumentation — a graphite chassis with engraved panels, opaque steel hairlines, amber for action, green phosphor for readouts, and IBM Plex Mono carrying the interface.
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
    backgroundColor: "{colors.primary}"
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

It is the one kit in this set where **mono is the interface, not a label font.** IBM Plex Mono
sets the headings, the eyebrows, the table headers, every badge, the metadata and every number;
IBM Plex Sans is the fallback voice, used only where the reader is reading sentences instead of
reading instruments. That inversion — and the warm amber-on-graphite ground — is what separates it from
Signal (navy HUD, Chakra Petch headings, cyan action) and Cyberpunk (near-black, magenta
action, neon bloom).

One sentence: *a machined instrument panel — amber for the one thing that acts, green phosphor
for everything it reports.*

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
- **Neutral (#0d0f11):** the graphite ground.
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

## Elevation & Depth

**Depth is engraved, not floating.** There is no soft outer drop shadow anywhere in this kit;
the lab's card gets its depth from `--shadow-1`, which is an inset stack — a lit top lip
(`inset 0 1px 0 rgba(255,255,255,.10)`), a shadowed bottom lip
(`inset 0 -1px 0 rgba(0,0,0,.60)`) and a short soft falloff into the well
(`inset 0 2px 6px -3px rgba(0,0,0,.45)`). The panel reads as a plate sitting *below* the chassis
surface. `--shadow-2` deepens the recess (a brighter rim on a longer `14px` inner falloff);
`card-elevated` is therefore *more* cut-in, not more lifted — a milled well with light on its
rim, which is the correct reading of "elevated" on a machined face.

The lip alphas are deliberately above the "barely there" range (5%): at 5% a 1px highlight does
not survive a normal-density display, and a recess nobody can see is not a recess. The falloff
term is what sells it at viewing size — a 1px line alone reads as an outline.

`--glow` is reserved for controls that are *energised*: `0 0 0 1px rgba(255,176,0,.45)` plus a
short `14px` halo. It is a lamp, not a shadow — panels never wear it. `--blur: none`: machined
metal is not frosted glass, and translucent panels would undo the recess.

## Shapes

Small and hard: `--radius-sm: 2px`, `--radius-md: 3px`, `--radius-lg: 4px`. Nothing is
rounder than 4px, because a machined edge is a milled edge, not a soft one. `--cut: 0px` —
this kit does not chamfer; the seam does that job (Signal owns the corner cut, and reusing it
would blur the two kits together).

The one deliberate contract bend: **`--radius-pill` is 4px, not 999px.** A badge on this
machine is a stamped rectangular plate; a lozenge would read as a pill-shaped tag from a
product UI. The token keeps its name for the contract, and the switch control in the shared
lab keeps its own hard-coded round rocker — a switch is allowed to be a switch.

## Components

- **button-primary** — the amber plate: graphite label in the mono label style (`{typography.label}`),
  3px radius, the only element in the kit allowed to glow. (The shared lab renders `.btn` with
  `font: inherit`, so the lab's own button text is drawn in the body face; see Typography.)
- **button-primary-hover** — the same plate with the lamp turned up (`#ffc233`). Still graphite
  ink; the hue never changes.
- **button-secondary / button-ghost / button-danger** — a panel-face plate with an amber,
  muted or fault-red label. Secondary actions are recessed, never filled.
- **card / card-elevated** — the milled panel and the deeper well. Both inset; both bounded by
  a steel seam; neither floats.
- **card-title** — mono, weight 600. Titles are labels you can read across the room.
- **input** — `surface-2` well, `--border` seam, amber focus with a soft `--accent-soft` halo.
  An input is a hole in the panel, so it is the *darker* of the two surface steps in spirit
  even though it is tonally one step up.
- **badge** — a 4px-cornered stamped plate; `badge-accent`, `badge-ok`, `badge-warn` and
  `badge-danger` recolour the label and leave the plate dark, so a status row reads as lamps,
  not as blocks of paint.
- **table-header** — mono, uppercase, `+0.12em`, dim: the engraved column legend.
- **alert-*** — a panel with a 3px lamp rule down the left edge (steel blue, green, dim amber,
  fault red).
- **link** — amber, underlined on hover; the same lamp as the action, because a link *is* an
  action.

## Do's and Don'ts

- **Do** keep amber for the one thing that acts. Everything else on this machine reports.
- **Do** express depth with inset lips. If an element needs an outer shadow to be legible,
  it is the wrong element.
- **Do** draw seams as opaque steel (`#2a2f35`), not as translucent white. Engraving is
  subtractive.
- **Do** set facts, IDs and numerals in mono — and headings too. The mono is the interface.
- **Do** keep radii at 2–4px and let the corners stay hard.
- **Don't** put white text on amber; the amber plate takes graphite ink (`--primary-ink`).
- **Don't** introduce a third lamp. Green reports, amber acts, red faults, and the steel blue
  is data — that is the whole instrument.
- **Don't** add a glow to a panel. Glow belongs to an energised control.
