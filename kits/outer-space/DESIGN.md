---
version: alpha
name: Outer Space
description: A deep blue-violet void shot through with a starfield, three nebula blooms and one warm starlight — vast, quiet, awe-struck.
colors:
  primary: "#ffe9b8"
  primary-hover: "#fff4d6"
  on-primary: "#0a0e22"
  primary-soft: "rgba(255, 233, 184, 0.14)"
  secondary: "#7fe3f0"
  tertiary: "#6b4bd6"
  neutral: "#070a18"
  nebula-1: "#6b4bd6"
  nebula-2: "#c2418f"
  nebula-3: "#4fd1e0"
  bg-stop-1: "#0b0f26"
  bg-stop-2: "#0a0e22"
  bg-stop-3: "#05070f"
  surface: "rgba(20, 26, 56, 0.55)"
  surface-2: "rgba(28, 36, 78, 0.66)"
  surface-solid: "#141a38"
  text: "#eef1fb"
  text-muted: "#bcc5e4"
  text-dim: "#b0badb"
  ok: "#5fe0a8"
  warn: "#ffb066"
  danger: "#ff6f86"
  info: "#8fb6ff"
typography:
  display:
    fontFamily: "Outfit"
    fontSize: "2.9rem"
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: "-0.015em"
  h1:
    fontFamily: "Outfit"
    fontSize: "1.7rem"
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "-0.015em"
  h2:
    fontFamily: "Outfit"
    fontSize: "1.3rem"
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: "-0.01em"
  body:
    fontFamily: "Inter"
    fontSize: "0.95rem"
    fontWeight: 400
    lineHeight: 1.6
  small:
    fontFamily: "Inter"
    fontSize: "0.8rem"
    fontWeight: 400
    lineHeight: 1.5
  button:
    fontFamily: "Inter"
    fontSize: "0.875rem"
    fontWeight: 500
    lineHeight: 1.2
  label:
    fontFamily: "IBM Plex Mono"
    fontSize: "0.72rem"
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: "0.14em"
rounded:
  sm: "8px"
  md: "14px"
  lg: "24px"
  pill: "999px"
spacing:
  xs: "4px"
  sm: "8px"
  md: "16px"
  lg: "28px"
  xl: "48px"
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: "0.58rem 1rem"
    height: "2.5rem"
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: "0.58rem 1rem"
  button-primary-lg:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: "0.78rem 1.35rem"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.secondary}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: "0.58rem 1rem"
  button-secondary-hover:
    backgroundColor: "{colors.primary-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: "0.58rem 1rem"
  button-ghost:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.text-muted}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: "0.58rem 1rem"
  button-danger:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.danger}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: "0.58rem 1rem"
  input:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: "0.6rem 0.72rem"
    height: "2.5rem"
  badge:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text-muted}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "0.2rem 0.55rem"
  badge-accent:
    backgroundColor: "{colors.primary-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "0.2rem 0.55rem"
  badge-ok:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.ok}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "0.2rem 0.55rem"
  badge-warn:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.warn}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "0.2rem 0.55rem"
  badge-danger:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.danger}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "0.2rem 0.55rem"
  badge-info:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.info}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "0.2rem 0.55rem"
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.lg}"
    padding: "1.15rem"
  card-elevated:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: "1.15rem"
  card-solid:
    backgroundColor: "{colors.surface-solid}"
    textColor: "{colors.text}"
    rounded: "{rounded.lg}"
    padding: "1.15rem"
  nav-item-active:
    backgroundColor: "{colors.primary-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.button}"
    rounded: "{rounded.sm}"
    padding: "0.4rem 0.75rem"
  caption:
    textColor: "{colors.text-dim}"
    typography: "{typography.small}"
  avatar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    size: "2.2rem"
  chart-1:
    backgroundColor: "{colors.secondary}"
    rounded: "{rounded.sm}"
  chart-2:
    backgroundColor: "{colors.tertiary}"
    rounded: "{rounded.sm}"
  chart-3:
    backgroundColor: "{colors.nebula-2}"
    rounded: "{rounded.sm}"
  page:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.text}"
  link:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.secondary}"
---

# Outer Space

## Overview

Outer Space is the kit for the *wonder* of space, not the menace of it. Every other dark kit in
this library is legible as an instrument: `carbon` is engineered, `cyberpunk` is loud, `signal` is
instrumental, `dark-glass` is sleek. This one is a vista. You do not operate it; you look out of it.

The ground is a deep blue-violet void — `{colors.bg-stop-1}` at the top falling to
`{colors.bg-stop-3}` 2600px down — carrying a starfield of 1–2.4px specks and five vast, off-centre
blooms: a warm gold star bloom at the top, violet (`{colors.nebula-1}`) at the top left, rose
(`{colors.nebula-2}`) at the right, a wide ice lane (`{colors.nebula-3}`) low centre, and a deep
violet floor bloom at the foot. Across the full page the ground's luminance runs from 0.0028 to
0.0444 — a **20.4x spread**. That range is the whole point: a flat field reads as
charcoal, and a viewer scrolling this page should feel distance.

The light comes from objects, not from the UI. Starlight gold (`{colors.primary}`) is the one action
colour; ice cyan (`{colors.secondary}`) is the cool register; the violet and rose exist only as
atmosphere you look *through*. Nothing here glows like a neon sign. It glows like a star.

One sentence: *starlight gold on a starfielded void, deep enough to fall into.*

## Colors

- **primary — `{colors.primary}`** starlight. The warm white-gold of a distant sun, and the single
  action colour of the kit: primary fills, focus rings, active nav, links. It is *light*, so the
  label on it is the void — `{colors.on-primary}` at 16.0:1, never white. This is the one decision
  that separates this kit from every other dark kit in the library, which all fill their primary
  button with a saturated neon and invert to white text.
- **primary-hover — `{colors.primary-hover}`** starlight at its brightest. The button gets *lighter*
  on hover, not darker: a star flares when you look at it. The ink stays `{colors.on-primary}`
  (17.4:1).
- **primary-soft — `{colors.primary-soft}`** a 14% starlight tint, derived not invented. Active nav
  chips, accent badges, inline code backgrounds, focus halos.
- **secondary — `{colors.secondary}`** ice cyan. The cool register: gradient partner, chart series,
  media, the avatar fill. It is the counterweight to the gold and it never carries a primary action.
- **tertiary — `{colors.tertiary}`** the violet of the top-left bloom, addressable a second time as
  `{colors.nebula-1}`. Terrible as a button, excellent as data and illustration: it is already in the
  page you are sitting on, so anything drawn in it looks continuous with the ground.
- **neutral — `{colors.neutral}`** the deepest stop of the void. The real ground is a layered
  gradient (see `--bg` in `tokens.css`); this is the flat stand-in for print, email and canvas.
- **The gradient stops ship as colours, deliberately.** `{colors.nebula-1}`, `{colors.nebula-2}`,
  `{colors.nebula-3}` and `{colors.bg-stop-1}` / `{colors.bg-stop-2}` / `{colors.bg-stop-3}` are the
  raw stops the ground is built from, so a project can rebuild the vista, sample a chart from it, or
  print a swatch without ever re-typing an `rgba()`. The gradients themselves live only in
  `tokens.css`.
- **Surfaces are translucent by design.** `{colors.surface}` is a 55% pane and `{colors.surface-2}`
  a 66% pane over that same ground; `{colors.surface-solid}` is the opaque fallback. Do not
  substitute a flat hex — the translucency is how the vista shows through the UI.
- **Status sits outside the starlight/ice pair.** Aurora `{colors.ok}`, solar amber `{colors.warn}`,
  rose-hot `{colors.danger}`, glacial `{colors.info}`. The amber is kept warm and saturated on
  purpose so it can never be read as the pale gold of an action.

## Typography

Two families and a mono, each with one job.

- **Outfit** is the display face: a wide, geometric grotesque with perfectly round counters that
  reads as *quiet* at 700 rather than shouty, which is exactly the register a vista wants. It is the
  on-the-nose choice for this subject the way a serif is for a newspaper, and it is a different
  skeleton from `carbon`'s Space Grotesk and `dark-glass`'s Sora — the three dark kits do not share a
  heading voice. Display is set tight at `-0.015em` so a large heading reads as one shape.
- **Inter** carries body and interface text at 0.95rem / 1.6. On a low-luminance ground generous
  leading matters more than on paper.
- **IBM Plex Mono** is labels, badges, table headers and code: uppercase, tracked
  `{typography.label.letterSpacing}` (0.14em). The wide tracking is the kit's "instrument voice",
  but at 0.14em rather than a HUD's 0.18em — this is a caption under a photograph, not a readout.

## Layout

The lab is a single column at `min(1040px, 100% - 2.5rem)`. The kit's own rhythm is spacious:
sections breathe at 2.25rem and panels are separated by 16–28px so the void reads *between* things,
which is the whole reason to use this kit over a solid dark page. Spacing runs `{spacing.xs}` to
`{spacing.xl}`, and the jump from `{spacing.lg}` to `{spacing.xl}` is large (28 → 48px) on purpose:
the top end is where the vista opens up.

Never full-bleed an opaque panel across the page. The ground must always be visible at the edges of
the viewport — that edge is where "space" happens.

## Elevation & Depth

Depth here is atmospheric, not architectural. Four things make it, in order of importance:

1. **The ground is layered, not a ramp.** It is four starfield tiles (1.1px, 0.9px, 1.3px and 2.4px
   specks on 137px, 89px, 211px and 373px tiles — deliberately coprime sizes, so the field never
   resolves into a visible grid) over five off-centre blooms over a five-stop ramp. `--bg-plain` is the same ground with the specks
   removed, for text-critical or print-adjacent use, and `--starfield` is the speck layers alone for
   overlaying a hero, a panel or a poster.
2. **Frost needs something to frost.** `templates/lab.css` applies `var(--blur)`
   (`blur(22px) saturate(140%)`) to every `.card`. A `backdrop-filter` over a smooth ramp is
   indistinguishable from flat paint — there is no high-frequency detail to smear. The starfield is
   what the glass frosts; the blooms are what `saturate()` lifts. Remove either and the panels
   flatten.
3. **Glow is the elevation.** `--glow` (`0 0 34px rgba(255,233,184,.30)`) is a soft starlight halo
   under the primary action. It is emitted light, never a drop shadow.
4. **Shadows are quiet.** `--shadow-1` and `--shadow-2` are deep blue-black, wide and soft, each
   carrying an `inset 0 1px 0` starlight lip along the top edge — that faint bright rim is what
   makes a panel read as a *pane* with a horizon rather than a hole punched in the page.

Edges are hairline and cool: `--border` is `rgba(178,198,255,.13)`, `--border-strong`
`rgba(190,208,255,.22)`, both at `--border-w: 1px`. A vista is bounded by light, so if a surface
needs more separation, add glow or shadow — never weight.

## Shapes

`{rounded.sm}` 8px, `{rounded.md}` 14px, `{rounded.lg}` 24px, pills at 999px, `--cut: 0px` — this
kit rounds; it does not cut. The panel radius is deliberately large: a viewport into something vast
should not have sharp corners, and a generous radius on a translucent pane reads as an aperture.
Nothing in this kit uses `clip-path`.

## Components

- **button-primary** — a starlight fill with the void as its label, carrying `--glow`. It is the only
  object on the page that emits.
- **button-primary-hover** — the star flares: the fill brightens to `{colors.primary-hover}` while
  the ink stays `{colors.on-primary}`.
- **button-secondary** — a translucent pane with an ice-cyan label and a cool hairline rim. The
  default "there is another option here" control, built to read as glass rather than as a stroke.
- **card / card-elevated** — the 55% and 66% panes, `{rounded.lg}`, `blur(22px)`; the second is
  denser rather than a second blur layer. **card-solid** is the opaque fallback.
- **input** — the denser `{colors.surface-2}` pane with a hairline rim; focus swaps the rim to
  starlight and adds a `{colors.primary-soft}` halo.
- **badge** — pill, mono, uppercase, translucent. `badge-accent` is the starlight-tinted variant.
- **avatar / chart-1 / chart-2 / chart-3** — where the cool register lives: ice cyan, nebula violet
  and nebula rose, i.e. the colours already in the ground.
- **nav-item-active** — a `{colors.primary-soft}` chip with starlight text: a small warm glow, not a
  filled pill.

## Do's and Don'ts

**Do**

- Let the ground show at the edges of every screen — the vista *is* the kit.
- Put starlight on exactly one thing per screen. One star, one action.
- Keep panels translucent and let the starfield frost through them.
- Verify any new text colour against the *brightest* pixel of the nebula, which is in the gold bloom
  near the top of the page — not against `{colors.neutral}`.
- Composite a translucent surface over the ground before claiming a contrast number for it.

**Don't**

- Don't fill a button with ice cyan, nebula violet or rose. Gold is the action; the rest is cosmos.
- Don't use white text on `{colors.primary}` — it is starlight, and `{colors.on-primary}` is the ink
  that clears 16:1 on it.
- Don't flatten `--bg` to a two-stop ramp. The frost and the saturate have nothing to work on and the
  whole kit turns into another dark blue page.
- Don't set `--blur` to `none`.
- Don't add a fourth "look at me" colour. There are two, plus one void, and that is the budget.
- Don't make it loud. Neon is a different library entry; this one is quiet, and the quietness is what
  makes it feel large.
