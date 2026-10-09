---
version: alpha
name: Holographic
description: An iridescent foil theme for dark interfaces — hue-shifting charcoal plates carrying hard-banded prismatic surfaces, a stamped foil material, a prism split and a rainbow iris, with a hard chromatic-aberration edge on every control, over one blue action and a violet counterpoint.
colors:
  primary: "#54adff"
  primary-hover: "#6fbcff"
  primary-ink: "#6ec0ff"
  primary-ink-hover: "#8ed0ff"
  secondary: "#b64ce8"
  tertiary: "#48cfe0"
  neutral: "#212a38"
  surface: "#252633"
  surface-2: "#16171f"
  text: "#edeff7"
  text-muted: "#bcc1cf"
  text-dim: "#aeb5c7"
  ink: "#0d0e14"
  success: "#46e0a0"
  warning: "#ffc46b"
  error: "#ff7585"
typography:
  display:
    fontFamily: Gruppo
    fontSize: 2.9rem
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: "0.01em"
  heading:
    fontFamily: Gruppo
    fontSize: 1.3rem
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: "0.02em"
  body:
    fontFamily: Space Grotesk
    fontSize: 0.98rem
    fontWeight: 400
    lineHeight: 1.55
  label:
    fontFamily: Space Mono
    fontSize: 0.75rem
    fontWeight: 400
    lineHeight: 1
    letterSpacing: "0.18em"
rounded:
  sm: 3px
  md: 7px
  lg: 13px
  pill: 999px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
components:
  page:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.text}"
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 16px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary-ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 16px
  button-secondary-hover:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.primary-ink-hover}"
    rounded: "{rounded.md}"
  button-danger:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.error}"
    typography: "{typography.body}"
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
    padding: 18px
  card-title:
    textColor: "{colors.text}"
    typography: "{typography.heading}"
  card-body:
    textColor: "{colors.text-muted}"
    typography: "{typography.body}"
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
    padding: 10px
  caption:
    textColor: "{colors.text-dim}"
    typography: "{typography.label}"
  badge:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text-muted}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: 4px
  badge-accent:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.primary-ink}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
  badge-success:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.success}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
  badge-warning:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.warning}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
  badge-danger:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.error}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
  alert-info:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.tertiary}"
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

# Holographic

## Overview

Iridescence as a *material*: dark, hue-shifting charcoal foil plates carrying surfaces
that shift hue across their width as hard prismatic bands. The register is **optical,
cool and technical** — the reference is a shelf of gradient-stroked shapes and a rainbow
iris, and the kit reads like a sheet of holographic foil catching light rather than like a
colour scheme. One blue action (`#54adff`), one violet counterpoint (`#b64ce8`), and a
drawn foil that supplies every other hue.

Crucially, the iridescence is in the **working parts**, not only in three decorative
chips: every button carries a hard **chromatic-aberration edge** (three solid, zero-blur
offset plates in violet, magenta and teal), every field is a prismatic-lip recess, the
bars and the switch carry milled prismatic edges, the fills are hard prismatic bands, and
the panels themselves shift hue as foil bands. A kit that names itself holographic and
quarantines its rainbow into a tile has not behaved holographically; this one does.

This is a **derived kit**. The provenance is a Figma file (fileKey
`4tEWhmZzpqWsjjwJrqS8lg`, node `4:2`, "Glowy stuff"): a dark charcoal canvas of
gradient-stroked badge shapes, a rainbow camera-aperture pinwheel and a "Cool Sci-fi
thing" label set in Gruppo at `#54adff`. The palette, the aperture geometry and the
type come from that file. What does *not*: the file renders as soft neon **glow**, and
a soft glow is exactly what the holographic register must not be. Every glow in the
reference is re-expressed here as **hard-banded diffraction** — crisp bands, crisp
edges, zero blur. The kit is named by genre; no logo or trade dress is reproduced.

## Colors

Blue `#54adff` is the single action colour — the reference's own label blue — and it
takes **ink** as its label (`#0d0e14`, 8.07:1), which is the strongest contrast the kit
owns. Violet `#b64ce8` is the counterpoint and belongs to *media and data*: media
panels, the second chart series, never to a primary action. The cyan `#48cfe0`
(tertiary) carries the info rung, deliberately a step apart from the blue action so the
two never read as the same signal.

The rainbow lives in the **material**, not in a third accent — that is the whole
discipline of this kit. The palette is two accents; the drawn foil, the prism
and the iris supply the rest of the spectrum as material, and the same foil feeds
the card media panel.

The ground is three **hue-shifting charcoal plates** — a violet-cast top (`#33304a`),
a blue-cast mid (`#212a38`) and the deep base (`#16171f`) — laid as hard bands, so the
page ground itself shifts hue like foil catching light rather than fading. **Panels
(`--surface`) are banded the same way** — violet-, blue-, plum- and teal-cast bands at
near-constant luminance — so a card shifts hue like foil while staying a stable ground for
type (every band is deliberately darker than the plate, so the plate still binds the
contrast table). Because the ground is variable, the binding ground for every contrast pair
is the **brightest plate** (`#33304a`), and the masthead's prismatic wash is graded as a
composite (`#384263`), never against the raw ink. Hairlines are tinted toward the foil
(violet on the default rule, blue on emphasis). Type is a cool near-white `#edeff7`, the
foil's specular highlight rather than pure white.

The blue is an excellent *fill* and only 6.40:1 as a small label on the brightest plate,
so the readable member ships separately: `--accent-ink` `#6ec0ff` carries every READ word
(eyebrow, links, active nav, accent and secondary-button labels) and clears 4.86:1 even
on its own 16% tint composited over the brightest plate.

## Typography

Gruppo is the **display face** and it is the reference's own — a geometric, rounded,
technical face that reads like a foil label or a security print, used at 400 only (it
ships one weight). Space Grotesk is the body face: a wider technical grotesque, so the
two voices contrast by *width* rather than by temperament, exactly how a technical label
sets a spec against its standfirst. Space Mono is the small-print voice for swatches,
labels, table headers and metrics — a security-print legend, not a terminal. Caps labels
run at `0.18em`, a printed legend rather than a UI chip.

## Layout

Spacing is airy (`16px` gutters, `24px` between blocks) so the bands have room to read.
Corners are the reference's rounded badge geometry, kept small (`3px`/`7px`/`13px`) — a
prismatic plate is a plate, and the only true pill is the badge. There is no chamfer
(`--cut: 0px`): the kit's geometry is the band and the aperture, not a diagonal.

## Elevation & Depth

Depth is **hard-edged and flat**. `--blur` is `none` and no panel carries a
`backdrop-filter`. Elevation is a **zero-blur offset**: `--shadow-1`/`--shadow-2` are
dark plates pushed down-right under a panel, each ringed by a faint violet prismatic
hairline (the elevated card adds a violet refraction band beyond its offset), and every
button's edge is `--btn-shadow` — three solid, zero-blur offset plates in **violet
`#b64ce8`, magenta `#ff5fd0` and teal `#3ee0c8`**, i.e. chromatic aberration as chrome.
The primary button's `--glow` is that same prismatic stack under a crisp ink ring, not a
bloom. There is no blur, no feather and no rainbow glow anywhere in this kit, despite the
source material being nothing but glow: the foil, the prism fan and the iris are the
"light". The prismatic edges sit *outside* the text box, so they add hue without ever
touching the ground an ink is graded against.

## Shapes

The geometry lives in three signature tokens, each with a different job.
`--holographic-diffraction` is the **material** — a **stamped foil**, drawn as base64 SVG:
19 abrupt bands (silver, blue, cyan, violet, magenta, gold, teal) with crisp dark lands and
silver specular highlights, vertical so it tiles seamlessly and reused as the card media
panel. It is drawn rather than faded because a stamped sheet is a material with hard edges,
and because drawing it lets the band count be high enough that the banding is unmistakable
at 168×72. `--holographic-prism` is the **geometry** — a beam entering a triangle and
leaving as an ordered fan of hard bands, drawn as base64 SVG because a linear gradient
cannot fan from a point. `--holographic-aperture` is the **glyph** — the reference's
eight-bladed rainbow iris, a camera aperture that is also a spectrum wheel, drawn because
an aperture is arcs at angles a gradient cannot fake. Three motifs, three jobs; a fourth
would dilute them.

## Components

Buttons are blue fills with ink labels, or flat surface plates with lifted-blue labels;
the danger button keeps the surface and takes the coral-red text. Every variant carries the
same hard **chromatic-aberration edge** — violet, magenta and teal zero-blur offset plates
stacked down-right, so the control itself is iridescent; the primary button swaps that for
its own `--glow` prismatic stack under an ink ring, and the disabled button drops the edge
so it reads inert. Cards sit on the banded panel with a violet prismatic hairline; the
elevated card deepens and gains a violet refraction band beyond its offset. Inputs sit in
the deepest well, recessed by a prismatic-lip zero-blur inset, and the native controls are
reskinned through `--check-*` (a `--surface-2` well, a violet hairline, an accent-blue
checked fill) so they sit in the kit's palette rather than the browser's light defaults.
Nav and tabs are a
milled channel with prismatic inner lips, the active item wearing the prismatic offset; the
switch has a prismatic-lipped track and a violet/blue-edged knob. Badges are pills carrying
Space Mono caps on `--surface-2`. Progress and avatar fills are four hard prismatic bands.
Media panels are where the kit shows the *material*: `--media-bg` is the drawn foil sheet
itself — abrupt silver/blue/pink/gold bands with crisp dark lands, opaque.

## Do's and Don'ts

- **Do** keep blue for action and violet for media and data. Two accents, two jobs; the
  rainbow belongs to the material (the foil, the prism, the iris) and to the control edges.
- **Do** use ink (`--text-invert`) on the blue fill; near-white on blue fails, and ink on
  a bright prismatic plate is the foil move.
- **Do** keep every ramp **hard-stopped** and every edge **zero-blur**. A smooth two-stop
  gradient, or a feathered rainbow glow, is the one thing that turns this kit back into a
  generic neon theme.
- **Don't** add a blurred shadow, a bloom, or a `backdrop-filter` — the crispness *is* the
  material. The prismatic button edge is three *solid* plates, not a gradient.
- **Don't** use a prismatic hue as a **text** colour or introduce a third accent fill. The
  spectrum may live in the material, the fills and the hard edges of chrome — never on a
  glyph, and never as a new "look at me" action colour.
- **Don't** grade contrast against an average ground: a prismatic ground is variable, so
  measure against the brightest plate, the lightest panel band and the wash composite.
