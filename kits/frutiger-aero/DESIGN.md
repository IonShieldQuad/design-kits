---
version: alpha
name: Frutiger Aero
description: Sky-and-grass optimism — a sunlit meadow landscape (sky, low sun, three hazy ranges of green hills, mown grass) under translucent glass whose top edge carries a hard white specular band, with bubbles and water droplets on the signature tiles.
colors:
  primary: "#0d6db3"
  primary-hover: "#0b62a4"
  primary-ink: "#053c63"
  primary-ink-hover: "#04345a"
  on-primary: "#ffffff"
  secondary: "#2fa85e"
  tertiary: "#86cff2"
  neutral: "#a3ca7e"
  sky: "#a8d9f6"
  sky-2: "#c4e6fa"
  haze: "#e2efd8"
  hill-far: "#c3dbaa"
  hill-mid: "#b3d295"
  meadow: "#a3ca7e"
  meadow-foot: "#9fc67a"
  sun: "#fffcef"
  horizon-spec: "#fbfeff"
  surface: "rgba(255, 255, 255, 0.46)"
  surface-2: "rgba(255, 255, 255, 0.58)"
  surface-solid: "#a3ca7e"
  glass-band: "rgba(255, 255, 255, 0.95)"
  badge-tint: "rgba(13, 109, 179, 0.14)"
  overlay: "rgba(10, 38, 64, 0.44)"
  text: "#091f30"
  text-muted: "#1d3b52"
  text-dim: "#24425a"
  border: "rgba(38, 116, 168, 0.46)"
  border-strong: "rgba(10, 42, 72, 0.40)"
  fill-top: "#0f6aa8"
  fill-low: "#0b4f80"
  fill-foot: "#116b48"
  ok: "#094526"
  warn: "#583700"
  danger: "#7d1526"
  info: "#06406e"

typography:
  display:
    fontFamily: "Hind"
    fontSize: "2.6rem"
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: "-0.008em"
  h1:
    fontFamily: "Hind"
    fontSize: "1.7rem"
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "-0.008em"
  h2:
    fontFamily: "Hind"
    fontSize: "1.3rem"
    fontWeight: 600
    lineHeight: 1.2
  body:
    fontFamily: "Hind"
    fontSize: "0.95rem"
    fontWeight: 400
    lineHeight: 1.6
  small:
    fontFamily: "Hind"
    fontSize: "0.8rem"
    fontWeight: 400
    lineHeight: 1.5
  caption:
    fontFamily: "IBM Plex Mono"
    fontSize: "0.75rem"
    fontWeight: 400
    lineHeight: 1.4
  label:
    fontFamily: "IBM Plex Mono"
    fontSize: "0.75rem"
    fontWeight: 500
    letterSpacing: "0.13em"

rounded:
  sm: "10px"
  md: "16px"
  lg: "22px"
  pill: "999px"

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
  page-sky:
    backgroundColor: "{colors.sky}"
    textColor: "{colors.text}"
  page-sky-2:
    backgroundColor: "{colors.sky-2}"
    textColor: "{colors.text}"
  page-haze:
    backgroundColor: "{colors.haze}"
    textColor: "{colors.text}"
  page-hill-far:
    backgroundColor: "{colors.hill-far}"
    textColor: "{colors.text}"
  page-hill-mid:
    backgroundColor: "{colors.hill-mid}"
    textColor: "{colors.text}"
  page-meadow:
    backgroundColor: "{colors.meadow}"
    textColor: "{colors.text}"
  page-foot:
    backgroundColor: "{colors.meadow-foot}"
    textColor: "{colors.text}"
  page-sun:
    backgroundColor: "{colors.sun}"
    textColor: "{colors.text}"
  page-solid:
    backgroundColor: "{colors.surface-solid}"
    textColor: "{colors.text}"
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
    padding: "0.58rem 1rem"
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary-ink}"
    borderColor: "{colors.border}"
    rounded: "{rounded.md}"
    padding: "0.58rem 1rem"
  button-secondary-hover:
    backgroundColor: "{colors.glass-band}"
    textColor: "{colors.primary-ink-hover}"
    rounded: "{rounded.md}"
  button-ghost:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text-muted}"
    rounded: "{rounded.md}"
  button-danger:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.danger}"
    borderColor: "{colors.danger}"
    rounded: "{rounded.md}"
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    borderColor: "{colors.border}"
    rounded: "{rounded.lg}"
    padding: "1.15rem"
  card-elevated:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text}"
    rounded: "{rounded.lg}"
  card-specular:
    backgroundColor: "{colors.glass-band}"
    rounded: "{rounded.sm}"
    height: "13px"
  card-media:
    backgroundColor: "{colors.tertiary}"
    rounded: "{rounded.md}"
    height: "96px"
  horizon-specular-line:
    backgroundColor: "{colors.horizon-spec}"
    height: "2px"
  horizon-grass-foot:
    backgroundColor: "{colors.secondary}"
    height: "40px"
  input:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text}"
    borderColor: "{colors.border}"
    rounded: "{rounded.md}"
    padding: "0.6rem 0.72rem"
  input-focus:
    borderColor: "{colors.primary}"
    rounded: "{rounded.md}"
  divider:
    backgroundColor: "{colors.border}"
    height: "1px"
  input-rim:
    backgroundColor: "{colors.border-strong}"
    height: "1px"
  badge:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text-muted}"
    borderColor: "{colors.border}"
    rounded: "{rounded.pill}"
    padding: "0.2rem 0.55rem"
  badge-accent:
    backgroundColor: "{colors.badge-tint}"
    textColor: "{colors.primary-ink}"
    rounded: "{rounded.pill}"
  badge-ok:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.ok}"
    rounded: "{rounded.pill}"
  badge-warn:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.warn}"
    rounded: "{rounded.pill}"
  badge-danger:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.danger}"
    rounded: "{rounded.pill}"
  badge-info:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.info}"
    rounded: "{rounded.pill}"
  nav:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-muted}"
    borderColor: "{colors.border}"
    rounded: "{rounded.md}"
    padding: "0.4rem"
  nav-item-active:
    backgroundColor: "{colors.badge-tint}"
    textColor: "{colors.primary-ink}"
    rounded: "{rounded.sm}"
  alert:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text-muted}"
    borderColor: "{colors.primary}"
    rounded: "{rounded.md}"
    padding: "0.8rem 0.95rem"
  caption:
    textColor: "{colors.text-dim}"
    typography: "{typography.caption}"
  progress:
    backgroundColor: "{colors.fill-top}"
    height: "0.5rem"
    rounded: "{rounded.pill}"
  progress-foot:
    backgroundColor: "{colors.fill-foot}"
    rounded: "{rounded.pill}"
  avatar:
    backgroundColor: "{colors.fill-low}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.pill}"
    size: "2.2rem"
  modal-scrim:
    backgroundColor: "{colors.overlay}"
  link:
    textColor: "{colors.primary-ink}"
  focus-ring:
    backgroundColor: "{colors.primary-ink}"
    height: "2px"
---

# Frutiger Aero

## Overview

Frutiger Aero is the 2004–2013 consumer-tech register: sky above, green fields below, and
translucent glass over both. It is bright and friendly rather than severe — the ground is a
**place**, not a pattern.

The ground is a landscape, drawn as one inline SVG over a px-stopped ramp: a clear sky with a
low sun in the upper right, then **three ranges of rolling hills receding into their own haze**,
then the **mown meadow you are standing in**. Each range is painted, veiled in a pale haze, and
painted over by the next nearer one — that veil is the whole of aerial perspective, and it is
what makes the layers read as distance rather than as stripes. The nearest field carries broad
mown contour swaths and a fine blade grain, both of which fade out at the image's bottom edge so
the ground dissolves into the ramp instead of ending at a line.

Bubbles and water droplets did not go away when the ground became a field: they came off the
wallpaper and onto the **tiles**, where they are a motif rather than a background. A bubble field
behind type is wallpaper; a field with a horizon is the aesthetic's own name.

**This kit is the library's deliberate exception to its own non-smooth rule.** Every other kit is
required to shut five doors against smoothness — square corners, zero-blur shadows, hard-stopped
gradients, upscaled artwork, no blur. Frutiger Aero *is* smoothness. The one line that is not
negotiable is legibility, and that is the kit's trade: **gloss costs contrast headroom, and so
does a field.**

## Colors

- **neutral — `{colors.neutral}`** the meadow, and therefore the page ground. This is the value
  to hand to a medium that cannot take eleven gradient layers.
- **The ramp is addressable stop by stop**, far to near: `{colors.sky}`, `{colors.sky-2}`,
  `{colors.haze}`, `{colors.hill-far}`, `{colors.hill-mid}`, `{colors.meadow}`,
  `{colors.meadow-foot}`. The far range is the coolest and palest green; each nearer range is
  warmer and deeper, which is what aerial perspective means.
- **`{colors.sun}`** is the sun's core — cream, not gold. This is daylight, not dawn.
- **primary — `{colors.primary}`** azure. The one action colour, and deliberately deeper than the
  register's poster blue: a bright sky blue (`#2196f3`) gives a white label 3.10:1 and cannot
  carry text. `{colors.primary}` measures 5.45:1 with white.
- **primary-ink — `{colors.primary-ink}`** the accent as *text* (links, the eyebrow, active nav
  and tab, badge labels, secondary-button labels, inline code). The fill is only 2.49:1 as a small
  label on the grass (3.65:1 on a card), so text ships separately at 5.20:1.
- **secondary — `{colors.secondary}`** grass green. Gradients, media, the horizon. Never text.
- **tertiary — `{colors.tertiary}`** the sky at the top of the horizon panel.
- **Surfaces are transparent by design.** `{colors.surface}` is 46% white and
  `{colors.surface-2}` is 58% — never substitute a hex. The translucency *is* the kit, and
  `--blur` is applied on top of it. They are denser than a pale-ground glass kit would need
  because the ground beneath them is a mid-luminance field, not white.
- **Lines are cool and saturated.** `{colors.border}` is a mid-blue at 46% because a white
  hairline is invisible on a pale sky and twice invisible on grass, and because the same line has
  to read against both the field (L 0.43) and the glass (L 0.65–0.72).
- Everything is graded against the **darkest pixel of the drawn field**,
  `rgb(148,186,117)`, L 0.4270 — not against the palest ground, and not against a panel. The
  Forms row puts labels, hints and an invalid-field message straight on the grass with no panel
  behind them, and `.btn-danger` is a transparent control over the same ground.
- Status colours are therefore deep: `{colors.ok}` is a forest green, `{colors.danger}` a dark
  crimson. On a green ground a cheerful "success" green has nowhere light to go, and a readable
  chip beats a pretty one.

## Typography

**Hind** for display and body, **IBM Plex Mono** for captions and token labels.

The register's typeface is Frutiger — a commercial Linotype licence, and this repository is
public, so the kit ships a **Frutiger-adjacent free humanist sans** instead. Hind is humanist
with open apertures and an even colour, which is the part of Frutiger that carries the era's
feel; `"Frutiger"` appears in the stack as a **system fallback only**, never as a Google Fonts
request.

The register leans towards a light-to-regular display weight. The shared lab fixes display weight
at 700 for `.t-display` and `.masthead h1` and exposes no weight hook, so this kit's light display
voice is expressed where it can be: near-neutral tracking (`{typography.display.letterSpacing}`,
not a modern-SaaS `-0.02em`) and generous radii. Body copy is `{typography.body.fontSize}` / 1.6
— on a mid-tone ground, leading is what keeps paragraphs readable. Labels run in mono uppercase
at `{typography.label.letterSpacing}` and never below 12px.

## Layout

The ground is a scene and it should always be visible. The horizon sits **520–740px** down the
document: inside the first screen, below the masthead, so the first view a reader gets is sky,
sun, hills and a strip of meadow — never sky alone.

Panels float *on* the scene rather than covering it: keep 16–28px between surfaces so the field
shows between them, and never fill a page with an opaque surface. The meadow's mown swaths widen
and separate as they come toward the viewer, which is the only cue that says the ground is
receding; the grain lives in the near field and fades out by ~1300px so the rest of a long page
stays quiet behind type.

All ground stops are in **pixels**, not percentages: the body's gradient box is the whole
document, so a `0% → 100%` ramp smears the sky over several thousand pixels and the first
viewport reads as flat near-white. The drawn artwork is anchored at **82%** horizontally, not
50%, so a narrow viewport keeps the sun in frame instead of cropping to the centre.

## Elevation & Depth

Three translucent layers, distinguished by opacity and shadow rather than by colour:

1. **ground** — the drawn landscape on `--bg` (sky ramp, sun, cloud banks, three hazy ranges,
   mown meadow) plus sunlight lying on the field further down;
2. **`{colors.surface}`** — 46% white plus the 13px specular band, with
   `backdrop-filter: blur(16px) saturate(155%)`;
3. **`{colors.surface-2}`** — 58% white, a *soft* glass with no band, for everything nested:
   inputs, badges, alerts, code, the switch track, and the tile base the motifs are judged on.

The blur is **load-bearing** — `templates/lab.css` applies `var(--blur)` to every `.card`, and a
kit that sets `--blur: none` gets no frost at all.

**Why 46% and not 34%.** Over the previous pale ground a 34%-white panel stood about 0.11 above
its ground and read as glass. Over a meadow at L 0.50 the same 34% composites to L 0.612 — a
green-tinted pane only 0.11 above the grass, which reads as a stain rather than a surface. 46%
puts the card body at L 0.65–0.74 over the field: clearly a surface, still visibly green-tinted,
and still translucent enough that the hills and the mown bands pass under it. Above ~55% the
field stops reading through the glass at all, which is the failure in the other direction.
`{colors.surface-2}` is deliberately *denser* than `{colors.surface}` — nested surfaces should
be, and it is what makes an input read as a pane inside a pane.

**The band, and why it is 13px.** The specular band is the identity, and its lower edge is hard:
52% white at 12px straight to 2% at 13px. Measured over the darkest grass, that is a step from
L 0.821 to L 0.658 across one pixel — a lip, not a haze. On the material sample
(`.card-media` and the horizon token) the band is a hard-edged sweep across the **top third**
(22px, 23% of the 96px panel and 31% of the 72px tile), where nothing is ever typeset. On content
panels it is capped at 13px because the lab puts the first line of type 18px below a card's top
edge, so a percentage band's edge would land inside `.card-body` — a hard white line across a
paragraph.

`{colors.surface-2}` has no band at all, on purpose: the same token backs `.input`, `.badge`,
`.alert` and `pre.code`, and a hard edge inside a 41px field cuts straight through the text
inside it. `.card-elevated` therefore carries the denser nested glass and no band.

Shadows are soft and cast (`--shadow-1` / `--shadow-2`, each two cast layers plus an inset white
top highlight and a faint bottom bounce). `--glow` is the primary button's own lift: a cast
shadow plus an inner gloss.

## Shapes

`{rounded.sm}` 10px, `{rounded.md}` 16px, `{rounded.lg}` 22px, pills at 999px, `--cut: 0px`.
Generous and consistent — the panel and the landscape it floats on should feel cut from the same
mould. **No chamfer:** `--clip` is not declared, so `--frame-ring` is inert, and the kit's
geometry is curves only. Native check/radio keep the browser's own rendering with a
`--check-radius` of 6px, so a radio stays a circle while the box becomes a rounded square.

## Components

- **button-primary** — `{colors.primary}` with a white label, a cast shadow and an inner gloss;
  hover deepens to `{colors.primary-hover}` rather than brightening (a gloss darkens). Pressed, it
  travels 1px *down* as the bevel collapses.
- **button-secondary** — the glass itself as a control: 46% white, a `{colors.border}` rim,
  labelled in `{colors.primary-ink}`.
- **card** — 46% white, the 13px specular band, a `{colors.border}` rim, `--shadow-1`, and
  `{colors.text}` inside because the panel is lighter than the field behind it.
- **card-media** — the material sample: sky over grass with a hard specular line at the horizon,
  under a top-third gloss sweep. No text is ever set on it.
- **input** — soft glass at `{colors.surface-2}` with a recessed `--input-inset` and a bright
  lower bevel; focus switches the rim to `{colors.primary}` and adds a soft ring.
- **badge** — pill, mono, uppercase; `badge-accent` is the `{colors.badge-tint}` variant with a
  `{colors.primary-ink}` label (6.49:1 composited over a card, measured).
- **nav / nav-item-active** — a glass rail with a specular plate under the current item.
- **progress / avatar** — the hard-banded blue-to-green fill, gloss through the middle. The
  avatar's monogram is `{colors.on-primary}` and is the reason the fill is not brighter.
- **modal-scrim** — `{colors.overlay}`, a deep marine blue rather than neutral black.

## Do's and Don'ts

**Do**

- Let the sky, the hills and the meadow show between panels — the ground is half the kit.
- Keep the horizon inside the first screen. A page whose first viewport is all sky has lost the
  "grass" half of the name.
- Veil each range in haze before painting the nearer one over it. That veil is the landscape.
- Keep the specular band's lower edge hard. If it fades, the glass becomes fog.
- Grade any new ink against the **darkest field pixel** (`rgb(148,186,117)`, L 0.4270) and
  against the glass. A light kit with a scene binds on its darkest patch of grass, not on its
  palest sky.
- Keep the mown texture low-frequency: broad swaths, fading out below the fold. The field is a
  ground, not wallpaper.

**Don't**

- Don't put a repeating bubble field behind type — that is what this kit stopped doing. Bubbles
  and droplets belong on the tiles.
- Don't set `--blur: none` or drop `backdrop-filter` — the kit becomes a flat pastel page.
- Don't take the glass past ~55% white: frosted turns to painted, the field stops reading through
  the pane, and the specular band loses the headroom it needs to be seen.
- Don't put a white label on glass. White belongs on `{colors.primary}` and on the fill.
- Don't add a second light source. One sun, upper right, and the glass specular answers it.
- Don't use `{colors.primary}` as a large flat fill, and never as a text colour — that is what
  `{colors.primary-ink}` is for.
