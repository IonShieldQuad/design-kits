---
version: alpha
name: City Pop
description: A Tokyo bay in daylight — cream sky, coral sun, ocean teal, airbrushed and airy.
colors:
  primary: "#d62f4b"
  primary-hover: "#d62f4b"
  primary-ink: "#a3203a"
  secondary: "#1f9aa8"
  tertiary: "#8a5a10"
  neutral: "#fff8f1"
  surface: "#ffffff"
  surface-2: "#f6efe9"
  text: "#2f2a40"
  text-muted: "#5d5670"
  success: "#19784f"
  warning: "#8a5a10"
  error: "#b3243a"
  info: "#2c68c4"
typography:
  display:
    fontFamily: Sora
    fontSize: 2.85rem
    fontWeight: 600
    lineHeight: 1.08
    letterSpacing: "-0.01em"
  heading:
    fontFamily: Sora
    fontSize: 1.3rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: "-0.005em"
  body:
    fontFamily: Manrope
    fontSize: 0.95rem
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: Space Mono
    fontSize: 0.72rem
    fontWeight: 400
    lineHeight: 1
    letterSpacing: "0.14em"
  tech:
    fontFamily: Space Mono
    fontSize: 0.9rem
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: "0.04em"
rounded:
  sm: 5px
  md: 10px
  lg: 16px
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
    textColor: "{colors.neutral}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: 16px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.neutral}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary-ink}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: 16px
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
    padding: 18px
  card-media:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.md}"
    height: 96px
  card-media-2:
    backgroundColor: "{colors.secondary}"
    rounded: "{rounded.md}"
    height: 96px
  input:
    backgroundColor: "{colors.surface}"
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
  alert-info:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.info}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 14px
  sun-bar:
    backgroundColor: "{colors.tertiary}"
    rounded: "{rounded.md}"
    height: 8px
  link:
    textColor: "{colors.primary-ink}"
    typography: "{typography.body}"
---

# City Pop

## Overview

City pop is the soft-rock and AOR sound that came out of Tokyo between the late seventies and the
mid eighties, and its sleeve art is a single recurring scene: **a bay, a skyline, and a sun sitting
on the water.** This kit is that scene in *daylight* — the hour the sleeve was photographed, not
the hour the neon comes on.

The ground is cream warming through a pale horizon into sky-blue, the action colour is the coral of
the sun on the bay, and ocean teal belongs to water, data and focus. Radii are soft (5/10/16px) and
the one glow is a lit ring rather than a bloom, because a printed sleeve has a sheen rather than a
light source. Type is Sora for the soft geometric display, Manrope for the humanist body, and Space
Mono for the space-age machine labels the era's credit blocks were full of.

The register is *airy and pastel*, and that is the distinction from the rest of the retro family:
`synthwave` is this decade at night (indigo, magenta, cyan neon), `summer-sunset` is this decade
as a saturated poster. City pop is the low-contrast, hairline, elegant one.

## Colors

Coral `#d83752` is the primary action colour. It is set darker than the daylight is bright so a
white label clears 4.5:1 on the fill — the pink of a sunset is a *fill*, and a fill has to carry
text. Because that same coral is under 4.5:1 as a small label on cream, text does not use it:
`primary-ink` (`#a3203a`) is the text-safe member of the family and carries eyebrows, links, active
navigation, badge labels and secondary buttons.

Ocean teal `#1f9aa8` is the second accent and it belongs to *water and to state*, not to action:
the sea, media plates, progress, focus rings, charts. The horizon gold `#8a5a10` is the sun; it
appears in the sky ramp and in a status chip, never as a control.

The grounds are **light and warm, never a neutral grey**. The whole palette is pulled toward warm
cream and salt-blue because those are what the scene is made of: the palest ground stop
(`#dceff3`) is the binding constraint on every ink, and the cream is not.

Every ratio is graded against the palest ground the ink can land on, and against coral's own 12%
tint composited over paper for the badge case — not against an average.

## Typography

Sora is the display face: a geometric with softened, slightly squared curves that reads as *product
of the eighties* without becoming the wide technical letterform the synthwave family uses. Manrope
carries the body — a humanist grotesque with a low, easy rhythm that suits long copy over a
coloured ground. Space Mono is the label and code face: its deliberately retro monospace is the
credit-block and tracklist type of the era, and the wide `0.14em` tracking on caps turns a small
label into a sleeve credit rather than body text.

## Layout

Spacing is comfortable (`16px` gutters, `24px` between blocks) so the colour has room. Corners are
soft and generous — `5px` to `16px`, pills for tags — because the sleeves are airbrushed with a
soft edge; there is no hard cut anywhere in the kit.

## Elevation & Depth

Depth is a **soft warm drop plus one lit ring**, and no blur: `--blur: none`, because a sleeve is
printed, not frosted. Numeric elevation (`--shadow-1`, `--shadow-2`) is warm ink at low alpha so it
reads as paper lifting off paper rather than as a grey shadow. The single energised object is
`--glow` — a teal ring with a coral lift — and it is applied only by the primary button and by
focused elements. The masthead wears a translucent warm wash (`--wash`) over the page's own
daylight, so the hero reads as a sky rather than as a flat plate.

## Shapes

The kit's geometry lives in its signature tokens, not in its corners: the **sky** (`--city-pop-sky`),
the **skyline** (`--city-pop-skyline`) and the **sea** (`--city-pop-sea`), which together are the
genre's one image. The sky and the sea are drawn artwork (inline SVG) rather than gradients: the sky
because a sun must read as a disc over a band of cloud and a plain ramp renders as fog, and the sea
because the sun's broken reflection column is real structure — a smooth ramp would read as a second
sky. The three motifs do three different jobs (atmosphere, silhouette, surface) and three is the
ceiling here; a fourth would dilute them.

The motifs are the *sleeve*, and they keep the sunset hour while the interface around them stays in
daylight — the album cover and the room it is played in. That contrast is deliberate.

## Components

Buttons are coral fills with cream labels, or white panels carrying coral-ink labels; the danger
button keeps the panel and takes a deep red. Cards are white paper with a warm hairline and a soft
drop; the elevated card steps to the warm inset. Inputs sit on white with the inset rim, so a field
reads as a form rather than a well. Badges are pills carrying mono caps. The media plate carries the
sleeve itself — the sky, skyline and bay as one drawn postcard via `--media-bg`, rather than a
generic accent ramp — and the sun-bar carries the gold.

## Do's and Don'ts

- **Do** keep coral for action and teal for water, data and focus. Two accents, two jobs.
- **Do** let the horizon live in the top viewport and settle to sky-blue below it — a full-page `%`
  gradient would show one flat colour and waste the whole idea.
- **Do** grade labels against the palest ground, not the average one. The blue stop binds, not the
  cream.
- **Don't** use the coral fill as a text colour; `primary-ink` exists because it does not pass.
- **Don't** let it drift to dusk. The moment the ground goes navy this kit becomes `synthwave`
  with the wrong palette — the daylight is the whole distinction.
