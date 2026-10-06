---
version: alpha
name: Kaleidoscope
description: Mirrored jewel facets on a deep indigo aperture — one ruby facet acts, sapphire answers it cool, and the other three are structure. The discipline is symmetry, not restraint.
colors:
  primary: "#ff2d6f"
  secondary: "#5b86ff"
  tertiary: "#19dda0"
  neutral: "#050410"
  accent-hover: "#ff5b8f"
  accent-soft: "rgba(255,45,111,0.15)"
  facet-ruby: "#ff2d6f"
  facet-sapphire: "#5b86ff"
  facet-emerald: "#19dda0"
  facet-amber: "#ffb020"
  facet-violet: "#a678ff"
  bg: "#0a0719"
  bg-deep: "#050410"
  surface: "#15112e"
  surface-2: "#221d42"
  overlay: "rgba(5,4,16,0.78)"
  text: "#f6f3ff"
  text-muted: "#b9b2dd"
  text-dim: "#9590b8"
  text-invert: "#08040d"
  ok: "#35c98e"
  warn: "#e0a13a"
  danger: "#ff6b4a"
  info: "#8aa6ff"
  border: "rgba(170,150,255,0.24)"
  border-strong: "rgba(186,170,255,0.44)"
  focus-ring: "#5b86ff"
typography:
  display:
    fontFamily: "Sora"
    fontSize: "2.75rem"
    fontWeight: 700
    lineHeight: 1.06
    letterSpacing: "-0.02em"
  heading:
    fontFamily: "Sora"
    fontSize: "1.3rem"
    fontWeight: 600
    lineHeight: 1.2
  body:
    fontFamily: "Inter"
    fontSize: "0.95rem"
    fontWeight: 400
    lineHeight: 1.55
  label:
    fontFamily: "IBM Plex Mono"
    fontSize: "0.72rem"
    fontWeight: 500
    letterSpacing: "0.15em"
  code:
    fontFamily: "IBM Plex Mono"
    fontSize: "0.8rem"
    lineHeight: 1.6
rounded:
  sm: "3px"
  md: "5px"
  lg: "7px"
  pill: "6px"
spacing:
  xs: "0.35rem"
  sm: "0.6rem"
  md: "1rem"
  lg: "1.75rem"
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.text-invert}"
    rounded: "{rounded.md}"
    padding: "0.58rem 1rem"
    typography: "{typography.body}"
    height: "2.4rem"
  button-primary-hover:
    backgroundColor: "{colors.accent-hover}"
    textColor: "{colors.text-invert}"
    rounded: "{rounded.md}"
    padding: "0.58rem 1rem"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    rounded: "{rounded.md}"
    padding: "0.58rem 1rem"
    typography: "{typography.body}"
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.lg}"
    padding: "1.15rem"
  card-elevated:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text}"
    rounded: "{rounded.lg}"
    padding: "1.15rem"
  input:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text}"
    rounded: "{rounded.md}"
    padding: "0.6rem 0.72rem"
    height: "2.5rem"
  input-focus:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text}"
    rounded: "{rounded.md}"
    height: "2.5rem"
  badge:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text-muted}"
    rounded: "{rounded.pill}"
    padding: "0.2rem 0.55rem"
    typography: "{typography.label}"
  badge-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.text-invert}"
    rounded: "{rounded.pill}"
    padding: "0.2rem 0.55rem"
    typography: "{typography.label}"
  badge-ok:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.ok}"
    rounded: "{rounded.pill}"
    padding: "0.2rem 0.55rem"
    typography: "{typography.label}"
  badge-warn:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.warn}"
    rounded: "{rounded.pill}"
    padding: "0.2rem 0.55rem"
    typography: "{typography.label}"
  badge-danger:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.danger}"
    rounded: "{rounded.pill}"
    padding: "0.2rem 0.55rem"
    typography: "{typography.label}"
  badge-info:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.info}"
    rounded: "{rounded.pill}"
    padding: "0.2rem 0.55rem"
    typography: "{typography.label}"
  chart-series-1:
    backgroundColor: "{colors.facet-ruby}"
    rounded: "{rounded.sm}"
    width: "12px"
    height: "12px"
  chart-series-2:
    backgroundColor: "{colors.facet-emerald}"
    rounded: "{rounded.sm}"
    width: "12px"
    height: "12px"
  chart-series-3:
    backgroundColor: "{colors.facet-amber}"
    rounded: "{rounded.sm}"
    width: "12px"
    height: "12px"
  chart-series-4:
    backgroundColor: "{colors.facet-violet}"
    rounded: "{rounded.sm}"
    width: "12px"
    height: "12px"
  chart-series-5:
    backgroundColor: "{colors.facet-sapphire}"
    rounded: "{rounded.sm}"
    width: "12px"
    height: "12px"
  divider:
    backgroundColor: "{colors.border}"
    height: "1px"
    width: "100%"
  divider-strong:
    backgroundColor: "{colors.border-strong}"
    height: "1px"
    width: "100%"
  overlay-scrim:
    backgroundColor: "{colors.overlay}"
    width: "100%"
    height: "100%"
  focus-indicator:
    backgroundColor: "{colors.focus-ring}"
    height: "2px"
    width: "100%"
  input-ring:
    backgroundColor: "{colors.accent-soft}"
    height: "3px"
    width: "100%"
  facet-panel:
    backgroundColor: "{colors.bg-deep}"
    textColor: "{colors.text}"
    rounded: "{rounded.sm}"
    padding: "1.15rem"
  media-block:
    backgroundColor: "{colors.secondary}"
    rounded: "{rounded.md}"
    height: "96px"
  caption:
    textColor: "{colors.text-dim}"
  page:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.text}"
  page-deep:
    backgroundColor: "{colors.bg}"
    textColor: "{colors.text}"
---

# Kaleidoscope

## Overview

Every other kit in this library obeys *one accent plus one second accent*. This one does not,
and that is the argument the kit exists to make. **Symmetry replaces restraint.** A kaleidoscope
is multi-hue by construction — the image inside it is a riot of jewel colour — and it still
reads as one object, because everything in it is *mirrored*. The discipline moved out of the
palette and into the geometry: every pattern here is built from a mirrored pair of angles
(0°/180°, 60°/120°, or a conic sequence that repeats its own first half back), and every corner
is a cut rather than a curve. A rainbow is undisciplined; a kaleidoscope is a rainbow that has
been folded. That fold is the whole kit.

So there are five jewel facets — ruby, amber, emerald, sapphire, violet — and **exactly one
of them is allowed to act**: ruby (`{colors.primary}`) fills the single primary control on a
screen, and sapphire (`{colors.secondary}`) is its cool counterweight, carrying gradients, media
and chart series. Amber, emerald and violet are structure and graphic: pattern stops, a lit edge,
a prism ramp. They never fill a button and they are never text. The eye can hold five hues
because only two of them are asking for anything.

The ground is near-neutral: a very deep indigo aperture (`{colors.bg-deep}` at its darkest),
light entering from above it, falling to near-black. It has to be near-neutral, or the facets
stop reading as light through glass and start reading as more colour on colour. Nothing in this
kit is soft: no blurred shadow, no frost, no organic curve.

Use it where the page *is* the artefact — launch pages, game and music UI, a portfolio or
gallery that should feel crafted rather than merely dark. Do not use it for long-form reading
or dense data entry: five hues is a lot of signal for a form.

**It is not `cyberpunk`** (one neon accent on black, 3–6px corners, magenta hairlines) and it is
not `carbon` (cyan/violet, square). This kit is *pink-red ruby*, *cut at two opposite corners*,
*multi-hue*, and *mirrored*. If the facets were reduced to one hue it would become a darker
carbon with a chamfer.

## Colors

Five facets, three jobs.

| Role | Token | Value | Job |
|---|---|---|---|
| Ruby | `{colors.facet-ruby}` = `{colors.primary}` | `#ff2d6f` | **the one facet that acts** — primary button, links, focus-adjacent states |
| Sapphire | `{colors.facet-sapphire}` = `{colors.secondary}` | `#5b86ff` | cool counterweight — media gradient, progress, focus ring |
| Emerald | `{colors.facet-emerald}` = `{colors.tertiary}` | `#19dda0` | graphic — pattern stop, chart series 2 |
| Amber | `{colors.facet-amber}` | `#ffb020` | graphic — pattern stop, the spark at the centre |
| Violet | `{colors.facet-violet}` | `#a678ff` | graphic — pattern stop, the lit facet edge |

Neutral ground and text:

| Role | Token | Value | Contrast |
|---|---|---|---|
| Ground (darkest stop) | `--bg` | `#050410` | — |
| Ground (base) | `{colors.bg}` | `#0a0719` | — |
| Card pane | `{colors.surface}` | `#15112e` | — |
| Lit pane | `{colors.surface-2}` | `#221d42` | — |
| Body text | `{colors.text}` | `#f6f3ff` | **18.60:1** on the darkest stop |
| Secondary text | `{colors.text-muted}` | `#b9b2dd` | **9.10:1** on `{colors.surface}` |
| Tertiary text | `{colors.text-dim}` | `#9590b8` | **6.75:1** on the ground, **6.04:1** on `{colors.surface}` |
| Ink on a facet | `{colors.text-invert}` | `#08040d` | **5.67:1** on ruby, **6.91:1** on its hover |
| Ruby as *text* | `--accent-ink` `#ff6f9c` | — | **7.76:1** on the ground, **6.95:1** on `{colors.surface}` |

Three things are worth stating plainly.

**Who acts.** Ruby only. `--accent` is `#ff2d6f`; it is the single filled control on a screen.
Sapphire is `--accent-2` and is the *cool counterweight* — it never fills an action, it fills
media. Emerald, amber and violet are not in the brand pair at all: they appear in patterns
(`--kaleidoscope-star`, `--kaleidoscope-rose-window`, `--kaleidoscope-shard`,
`--kaleidoscope-prism`), in chart series and in a lit edge. If you ever find yourself reaching
for amber to fill a button, the kit has failed — that is the fifth "look at me" colour arriving.

**Why the ink is near-black.** White on ruby is 3.59:1, well under AA. Rather than lighten the
facet (which would make it a pale pink and cost the kit its jewel value), the label is
near-black `{colors.text-invert}`: 5.67:1, and it reads like ink on a lit stone. Do not "fix"
this by lightening `{colors.text-invert}`.

**Ruby as text is a different, lighter member of the same family.** `#ff2d6f` is a fine *fill*
and only 4.14:1 as a small label over the masthead's ruby wash. `--accent-ink` `#ff6f9c` is the
same hue, lighter, and clears 4.5:1 everywhere it is used — links, the eyebrow, inline code,
active nav, secondary-button labels.

**Status colours sit off the facets by value, not by hue.** The palette owns every hue family
already, so escaping by hue is impossible; the escape is chroma and value. `{colors.ok}` is a
sea-jade *duller and deeper* than the emerald facet, `{colors.warn}` a burnt gold duller than
amber, `{colors.info}` a pale sapphire lighter than the sapphire facet, and `{colors.danger}` is
deliberately pushed to **orange-red vermilion** so that a destructive state is never mistakable
for the ruby action colour. Keep those four relationships.

**Borders are facet edges, not grey rules.** `--border` is 24% of a lavender violet
(`rgba(170,150,255,.24)`), `--border-strong` 44%. On a near-black ground a neutral grey hairline
reads as a fence; a violet one reads as the edge of a pane.

## Typography

One geometric sans, one neutral, one mono. **The geometry is the star; the type does not
compete** — so there is no display face with a gimmick in it, and no more than two weights of
anything.

- **Sora** (display) for `h1`–`h3`, card titles and the wordmark. A crisp geometric sans with
  flat terminals and a tight, almost mechanical counter set — geometric enough to sit beside a
  cut corner without arguing with it.
- **Inter** (body) for everything read. Deliberately plain: it is the one neutral voice on a
  page of five hues.
- **IBM Plex Mono** (labels) for eyebrows, badges, table headers, timestamps and code —
  uppercase at `{typography.label.letterSpacing}` `.15em`.

Display tracking is tight (`-0.02em`) because a geometric face opens up at large sizes; mono
labels are wide. Never set body copy in Sora or in the mono — they are signposts, not prose.

## Layout

One 1040px measure, 2.25rem between blocks, 1rem grid gap, spacing scale
`0.35 / 0.6 / 1 / 1.75rem`. The rhythm is even and quiet on purpose: the page is already
busy with facets and cut corners, and a layout that also jumped around would be noise. Faceted
content wants *regular* framing — that regularity is what makes the mirrored patterns read as
deliberate rather than scattered.

## Elevation & Depth

Depth is **light through the material**, not shadow on top of it. Two consequences, and the
first one is a trap:

1. **`clip-path` eats `box-shadow` and `outline`.** This kit opts into `--clip` (below), and the
   shared lab applies it to cards, buttons, inputs, badges, alerts, nav and code blocks. Every
   *outer* drop shadow on those elements is clipped away — including a focus ring and any
   outside glow. This is a documented limitation of the chamfer capability, not a bug. So the
   kit leads its depth with **insets**, which are painted inside the box and survive the cut.
2. Therefore `--shadow-1` and `--shadow-2` are *inset facet edges first*, with an outer bloom
   appended for consumers who do not clip the element. `--shadow-2`'s bloom is not re-typed — it
   is `var(--kaleidoscope-glint)`, and **`--glow` is literally `var(--kaleidoscope-facet-edge)`**,
   so the primary button's lit rim and the surface bloom are the same two materials the lab
   renders in its Signature section. Derive, don't duplicate. `--shadow-1` stays nearly flat,
   because on a clipped card only its inset edge lands.
3. `--blur` is `none`. There is no frosted glass here: the surfaces are opaque, so the contrast
   of every pair is provable against a hex rather than a composite.

## Shapes

Everything is cut.

- `{rounded.sm}` 3px, `{rounded.md}` 5px, `{rounded.lg}` 7px — the measured corners.
- `{rounded.pill}` **6px**. A 999px pill cannot survive a chamfer: the diagonal would slice
  across the rounded end and produce a notched lozenge. Badges and avatars are chamfered chips
  in this kit, on purpose.
- **`--clip` (declared)** — the chamfer, two *opposite* corners cut at `--cut: 10px`. This is
  the kit's baseline shape and the lab applies it for us. Its cost is that the two diagonal
  edges are borderless (the border is cut with the shape) — at 10px that is a thin bright sliver
  of missing hairline, and it is what makes the shape read as a cut stone rather than a box.
- **`--kaleidoscope-facet-clip` (declared, more aggressive)** — an eight-point cut: *all four*
  corners at `--kaleidoscope-cut-lg: 22px`. This one is not what the shared lab applies; it is
  exported for hero panels, media frames and modal shells, and applied explicitly with
  `clip-path: var(--kaleidoscope-facet-clip)`. Two shapes, one language: 10px on two corners for
  controls, 22px on four for surfaces.

Because of the clip, the visible geometry is the *intersection* of the small radii with the cut
polygon — sharp, crystalline, never soft.

## Components

Every colour decision below resolves to a `{colors.*}` token; nothing is re-typed. Border
colours, shadows and clip-paths are deliberately not listed per component — they live in
`tokens.css` (see the note in Do's and Don'ts).

- **button-primary** — `{colors.primary}` ruby fill, `{colors.text-invert}` ink, 5px corner,
  chamfered, and the inset lit edge (`--glow`). The **only** lit, filled control on a screen.
- **button-primary-hover** — `{colors.accent-hover}`, a *brighter* ruby, not a darker one: a
  facet catching more light. The label stays `{colors.text-invert}` at 6.9:1.
- **button-secondary** — `{colors.surface}` pane with a `{colors.primary}` ruby label and a ruby
  hairline. Flat until hover, when it takes a 15% ruby wash — the same facet, barely lit.
  *That hover state is prose, not a component entry:* DESIGN.md cannot express "label on a
  translucent tint" without the linter comparing the label to the raw, uncomposited tint colour,
  which reports a contrast failure that does not exist on screen (the tint sits over the page
  ground, where `--accent-ink` measures 6.88:1). The state is specified in `tokens.css`
  (`--accent-soft`) and in this sentence.
- **card** — `{colors.surface}`, chamfered, `--shadow-1` (which on a clipped card is the inset
  top edge). **Card text is `{colors.text}`** on a dark pane; no `--text-on-surface*` override is
  needed because all three grounds are dark.
- **card-elevated** — `{colors.surface-2}`, the *lighter* pane. Elevation here is luminance, not
  distance: a nested pane catches more light.
- **input** — `{colors.surface-2}` fill, chamfered, `{colors.text}` value text. Focus changes the
  border to ruby and lays a 3px `{colors.accent-soft}` ring; the *keyboard* focus ring is
  sapphire (`--focus-ring`) so hover, focus and action are three different colours — and note
  that a clipped element cannot show an outside outline, so keep the border-colour change.
- **badge** — `{colors.surface-2}` chip, `{colors.text-muted}` mono uppercase label, 6px
  "pill". Variants: `badge-primary` (ruby, an *action* marker), `badge-ok` / `badge-warn` /
  `badge-danger` / `badge-info` (status, on the lit pane).
- **facet-panel** — `{colors.bg-deep}` ground inside a lighter page: the dark inset of the
  stack, carried by `--kaleidoscope-facet-clip` at 22px.
- **chart-series-1…5** — the five facets as data ink, in role order (ruby, emerald, amber,
  violet, sapphire). This is the one place all five are permitted in one view, because a chart
  is a graphic and not a hierarchy.
- **media-block** — `{colors.secondary}` sapphire; the one place the counterweight fills area.
  Real media uses `--kaleidoscope-prism` (ruby → amber → emerald → sapphire → violet).
- **divider** / **divider-strong** — the hairline and the emphasised rule, as `{colors.border}`
  and `{colors.border-strong}` fills. DESIGN.md has no `borderColor` property, so the line
  colours are declared here as 1px fills instead — the honest way to keep them referenced.
- **overlay-scrim** — `{colors.overlay}`, the modal veil.
- **focus-indicator** / **input-ring** — the two rings, as fills: the 2px sapphire keyboard ring
  (`{colors.focus-ring}`) and the 3px `{colors.accent-soft}` halo the focused input lays down.
- **page** / **page-deep** — the ground, and its darkest stop.

## Do's and Don'ts

**Do**

- Let ruby be the *single* filled control on a screen. One facet acts; four are structure.
- Keep every pattern mirrored. Patterns ship as `--kaleidoscope-*` tokens; the conic fan repeats
  its own first half, the shard lattice pairs 60° with 120°, the rose window is radial. If you
  add a pattern, add a mirror.
- Keep the insets. `--shadow-1`/`--shadow-2`/`--glow` are inset-only for a reason: the clip eats
  everything outside the silhouette.
- Use `--kaleidoscope-facet-clip` (22px, four corners) for hero panels and `--clip` (10px, two
  corners) for controls. Never mix both on one element.
- Keep `--text-invert` near-black and `--accent-ink` lighter than `--accent`. They are two
  different weights of the same decision.

**Don't**

- Don't fill a control with amber, emerald or violet, and don't set text in them. They are
  graphics. A second filled control turns the kit into a rainbow.
- Don't put white on `{colors.primary}` (3.6:1) or on any facet.
- Don't soften anything: no blurred shadow, no `--blur`, no border radius above 7px, no
  organic curve. Softening one corner makes the rest of the kit look like an accident.
- Don't rely on an outer glow or a focus outline on a clipped element — it will not render.
  Use a border-colour change instead.
- Don't list `boxShadow`, `borderColor` or `backdropFilter` in a component here: DESIGN.md
  accepts only background/text/typography/rounded/padding/size/height/width, and anything else
  is silently dropped by the exports. Those values live in `tokens.css` and in this prose.
