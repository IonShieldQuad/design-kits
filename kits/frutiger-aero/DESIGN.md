---
version: alpha
name: Frutiger Aero
description: Sky-and-grass optimism — a sky-blue-to-white ground with a green foot, seen through translucent glass whose top edge carries a hard white specular band, with bubbles and water droplets in the air.
colors:
  primary: "#0d6db3"
  primary-hover: "#0b62a4"
  primary-ink: "#0a5590"
  primary-ink-hover: "#084d84"
  on-primary: "#ffffff"
  secondary: "#2fa85e"
  tertiary: "#86cff2"
  neutral: "#eef9ff"
  sky: "#b4e0fb"
  sky-2: "#c3e7fc"
  air: "#eef9ff"
  grass: "#cdecce"
  grass-2: "#bfe8b2"
  grass-deep: "#a4db7c"
  horizon-spec: "#fbfeff"
  surface: "rgba(255, 255, 255, 0.34)"
  surface-2: "rgba(255, 255, 255, 0.44)"
  surface-solid: "#eef9ff"
  glass-band: "rgba(255, 255, 255, 0.95)"
  badge-tint: "rgba(13, 109, 179, 0.14)"
  overlay: "rgba(10, 38, 64, 0.44)"
  text: "#10334f"
  text-muted: "#2c4a66"
  text-dim: "#3a5872"
  border: "rgba(84, 152, 206, 0.42)"
  border-strong: "rgba(16, 58, 94, 0.32)"
  fill-top: "#0f6aa8"
  fill-low: "#0b4f80"
  fill-foot: "#116b48"
  ok: "#0f6b3d"
  warn: "#7d4d00"
  danger: "#b0203c"
  info: "#0b5f9e"

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
  page-air:
    backgroundColor: "{colors.air}"
    textColor: "{colors.text}"
  page-grass:
    backgroundColor: "{colors.grass}"
    textColor: "{colors.text}"
  page-grass-foot:
    backgroundColor: "{colors.grass-2}"
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
    backgroundColor: "{colors.grass-deep}"
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

Frutiger Aero is the 2004–2013 consumer-tech register: sky above, grass below, and
translucent glass over both, with bubbles and water droplets in the air. It is bright and
friendly rather than severe — the ground is a real gradient scene, the panels are genuinely
see-through, and the light comes from a single source at the upper left.

**This kit is the library's deliberate exception to its own non-smooth rule.** Every other
kit here is required to shut five doors against smoothness — square corners, zero-blur
shadows, hard-stopped gradients, upscaled artwork, no blur. Frutiger Aero *is* smoothness:
the gradients ramp, the shadows are soft and cast, `--blur` is real and load-bearing on
every card, and there is a light bloom in the masthead. The one line that is not negotiable
is legibility, and that is the kit's trade: **gloss costs contrast headroom.** A specular
band lifts the luminance of a panel's top edge; a bright blue sky is a mid-luminance
ground; a white label on a glossy control is the pair that fails first. Every ink here is
solved against the darkest ground stop, and the working is in `README.md`.

What makes it read as *glass* rather than as *fog* is one structural decision: the specular
band has a **hard lower edge**. A soft blur with no highlight is fog; a blurred panel with a
crisp white band across its top is glass. The band is deliberate and pre-loadable
(`{colors.glass-band}` over `{colors.surface}`), and it is capped at 13px on content panels
— see *Elevation & Depth*. Measured on the rendered card, the band is a strip ~20 units
whiter in red than the body below it, ending in a hard cut of ~15 units across a single
pixel.

## Colors

- **primary — `{colors.primary}`** azure. The one action colour, and it is deliberately
  deeper than the register's poster blue: a bright sky blue (`#2196f3`) gives a white
  label 3.10:1 and cannot carry text. `{colors.primary}` measures 5.45:1.
- **primary-ink — `{colors.primary-ink}`** the accent as *text* (links, the eyebrow, active
  nav and tab, badge labels, secondary-button labels, inline code, table code). The fill
  colour is only 3.89:1 as a small label on the sky, so text ships separately at 5.52:1.
- **secondary — `{colors.secondary}`** grass green. Gradients, media, charts and the green
  end of the ramp. It is never a text colour.
- **tertiary — `{colors.tertiary}`** the sky at the top of the horizon panel, and the solid
  stand-in for the media surface.
- **neutral — `{colors.neutral}`** the ground's white middle, and the colour to use when a
  surface genuinely cannot be translucent (print, email, canvas). See also
  `{colors.surface-solid}`.
- The ramp is addressable stop by stop: `{colors.sky}`, `{colors.sky-2}`, `{colors.air}`,
  `{colors.grass}`, `{colors.grass-2}`, with `{colors.grass-deep}` for the deepest green and
  `{colors.horizon-spec}` for the specular line at the horizon.
- **Surfaces are transparent by design.** `{colors.surface}` and `{colors.surface-2}` are
  `rgba()` white. Never substitute a hex — the translucency *is* the kit, and `--blur` is
  applied on top of it.
- **Lines are cool, not white.** `{colors.border}` is a soft sky-blue hairline, because a
  white hairline is invisible on this ground. The bright edge of a pane is a separate job
  and is done inside the shadow (`{colors.glass-band}`-adjacent insets), not by the border.
- Status colours (`{colors.ok}`, `{colors.warn}`, `{colors.danger}`, `{colors.info}`) are
  all solved against the **page ground**, not just against a white card: the Forms row sets
  labels and hints straight on the sky with no panel behind them.
- `{colors.fill-top}`, `{colors.fill-low}` and `{colors.fill-foot}` are the progress/avatar
  fill. They exist as separate values because `.avatar` typesets a white monogram on them:
  the upper band is capped at 10% white over `{colors.fill-top}` (4.71:1) and the lower at
  14% over `{colors.fill-low}` (5.99:1). A brighter, prettier band fails the avatar.

## Typography

**Hind** for display and body, **IBM Plex Mono** for captions and token labels.

The register's typeface is Frutiger — a commercial Linotype licence, and this repository is
public, so the kit ships a **Frutiger-adjacent free humanist sans** instead. Hind is
humanist with open apertures and an even colour, which is the part of Frutiger that carries
the era's feel; `"Frutiger"` appears in the stack as a **system fallback only**, never as a
Google Fonts request.

The register leans towards a light-to-regular display weight. The shared lab fixes display
weight at 700 for `.t-display` and `.masthead h1` and exposes no weight hook, so this kit's
light display voice is expressed where it can be: near-neutral tracking
(`{typography.display.letterSpacing}`, not a modern-SaaS `-0.02em`) and generous radii.
Body copy is `{typography.body.fontSize}` / 1.6 — on a saturated ground, leading is what
keeps paragraphs readable. Labels run in mono uppercase at
`{typography.label.letterSpacing}` and never below 12px.

## Layout

The ground is a scene, and it should always be visible: the sky at the top of a page, white
through the middle, the green register at the foot. Panels float *on* it rather than
covering it — keep 16–28px between surfaces so the sky shows between them, and never fill a
page with an opaque surface.

The full ground walk is expressed in **pixel** stops (380/760/1150/1950/2550/3300px), not
percentages: the body's gradient box is the whole document, so a `0% → 100%` ramp smears the
sky over several thousand pixels and the first viewport reads as flat near-white.

## Elevation & Depth

Three translucent layers, distinguished by opacity and shadow rather than by colour:

1. **ground** — the gradient scene on `--bg`, plus a drawn bubble field;
2. **`{colors.surface}`** — 34% white plus the specular band, with
   `backdrop-filter: blur(16px) saturate(155%)`;
3. **`{colors.surface-2}`** — 44% white, a *soft* glass with no band, for everything
   nested: inputs, badges, alerts, code, the switch track, the tile base.

The blur is **load-bearing** — `templates/lab.css` applies `var(--blur)` to every `.card`,
and a kit that sets `--blur: none` gets no frost at all.

**Why 34% and not 46%.** The first build of this kit used 46% white *plus* a
`brightness(1.04)` term in `--blur`, and the band came back invisible: measured on the
rendered card, the panel composited to L 0.989 and the band's plateau to L 0.991 — a step of
0.002. A specular highlight needs headroom above the surface it sits on, and a near-white
panel has none. The `brightness()` term was removed and the base brought down, which is why
the bloom now lives only in `--bg` and `--wash`, where it lightens the ground *before* the
glass is composited over it. `{colors.surface-2}` is deliberately *denser* than
`{colors.surface}` — nested surfaces should be, and it is what makes an input read as a pane
inside a pane.

One consequence of the shared lab worth knowing:
`.card-elevated` reads `--surface-2`, not `--surface`, so the raised card in the Cards row
carries the denser nested glass and **no** specular band. Giving both card tiers the band
would mean putting one on `--surface-2`, which also backs `.input`, `.badge`, `.alert` and
`pre.code` — where a hard edge at 46% of a 41px field cuts through the text inside it. The
band therefore appears on the base card, the nav, the masthead lip and the media panel, and
the raised panel is the smooth-glass one.

**The band, and why it is 13px.** The specular band is the identity, and it has a hard lower
edge: 52% white at 12px straight to 2% at 13px. On the material sample — `.card-media` and
the horizon token — the band is a hard-edged sweep across the **top third** (22px, which is
23% of the 96px panel and 31% of the 72px tile), where nothing is ever typeset. On content
panels it is capped at 13px, and that is measured rather than timid: the lab puts the first
line of type 18px below a card's top edge and around 17px below a nav item's, so a
percentage band's edge lands inside `.card-body` on the Cards row — a hard white line across
a paragraph. The kit keeps the hard edge and moves the edge, rather than softening the edge.

`{colors.surface-2}` has no band at all, on purpose: the same token backs `.input`, `.badge`,
`.alert` and `pre.code`, and a hard edge inside a 41px field cuts straight through the text
inside it.

Shadows are soft and cast (`--shadow-1` / `--shadow-2`, each two cast layers plus an inset
white top highlight and a faint bottom bounce). `--glow` is the primary button's own lift: a
cast shadow plus an inner gloss.

## Shapes

`{rounded.sm}` 10px, `{rounded.md}` 16px, `{rounded.lg}` 22px, pills at 999px, `--cut: 0px`.
Generous and consistent — the panel and the ground it floats on should feel cut from the
same mould. **No chamfer:** `--clip` is not declared, so `--frame-ring` is inert, and the
kit's geometry is curves only. Native check/radio keep the browser's own rendering with a
`--check-radius` of 6px, so a radio stays a circle while the box becomes a rounded square.

## Components

- **button-primary** — `{colors.primary}` with a white label, a cast shadow and an inner
  gloss; hover deepens to `{colors.primary-hover}` rather than brightening (a gloss
  darkens). Pressed, it travels 1px *down* as the bevel collapses.
- **button-secondary** — the glass itself as a control: 34% white with the same specular
  band and a `{colors.border}` rim, labelled in `{colors.primary-ink}`.
- **card** — 34% white, the 13px specular band, a `{colors.border}` rim, `--shadow-1`, and
  `{colors.text}` inside because the panel is lighter than the sky behind it.
- **card-media** — the material sample: sky over grass with a hard specular line at the
  horizon, under a top-third gloss sweep. No text is ever set on it.
- **input** — soft glass at `{colors.surface-2}` with a recessed `--input-inset` and a bright
  lower bevel; focus switches the rim to `{colors.primary}` and adds a soft ring.
- **badge** — pill, mono, uppercase; `badge-accent` is the `{colors.badge-tint}` variant with
  a `{colors.primary-ink}` label (5.33:1 composited, measured).
- **nav / nav-item-active** — a glass rail with a specular plate under the current item.
- **progress / avatar** — the hard-banded blue-to-green fill, gloss through the middle.
  The avatar's monogram is `{colors.on-primary}` and is the reason the fill is not brighter.
- **modal-scrim** — `{colors.overlay}`, a deep marine blue rather than neutral black.

## Do's and Don'ts

**Do**

- Let the sky and the grass show between panels — the ground is half the kit.
- Keep the specular band's lower edge hard. If it fades, the glass becomes fog.
- Grade any new ink against the **darkest** ground stop (`{colors.sky}`) and against the
  gloss band at full alpha. A light kit binds on its most saturated ground, not its palest.
- Put vivid, saturated blue where nothing is typeset: media panels, the drawn motifs, the
  progress fill. The ink stays dark.

**Don't**

- Don't set `--blur: none` or drop `backdrop-filter` — the kit becomes a flat pastel page.
- Don't raise surface opacity much above 50%: frosted turns to painted, the sky stops
  reading through the panel, and the specular band loses the headroom it needs to be seen.
- Don't put a white label on glass. White belongs on `{colors.primary}` and on the fill.
- Don't add a second light source. One highlight per sphere, upper left, always.
- Don't use `{colors.primary}` as a large flat fill, and never as a text colour — that is
  what `{colors.primary-ink}` is for.
