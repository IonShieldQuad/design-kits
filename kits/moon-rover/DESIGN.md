---
version: alpha
name: Moon Rover
description: The lunar surface and the machine standing on it — grey-brown regolith under one unfiltered sun, a cast shadow with no penumbra, drawn dust, and a single dust-covered amber for action.
colors:
  primary: "#d9821c"
  primary-hover: "#eb9a33"
  primary-ink: "#191410"
  primary-text: "#5e2b03"
  primary-text-hover: "#4a2102"
  secondary: "#4a6a86"
  tertiary: "#26405a"
  neutral: "#ded9cd"
  ground-top: "#e6e2d7"
  ground-bottom: "#d2ccbf"
  surface: "#eeeae0"
  surface-2: "#c4beb0"
  text: "#1e1c17"
  text-muted: "#38332b"
  success: "#1f4a28"
  warning: "#553d04"
  error: "#7a2714"
typography:
  display:
    fontFamily: Saira Condensed
    fontSize: 2.9rem
    fontWeight: 700
    lineHeight: 1.06
    letterSpacing: "-0.005em"
  heading:
    fontFamily: Saira Condensed
    fontSize: 1.3rem
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: "0.002em"
  body:
    fontFamily: Saira
    fontSize: 0.95rem
    fontWeight: 400
    lineHeight: 1.58
  label:
    fontFamily: Fira Mono
    fontSize: 0.72rem
    fontWeight: 500
    lineHeight: 1
    letterSpacing: "0.12em"
  readout:
    fontFamily: Fira Mono
    fontSize: 0.9rem
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: "0.01em"
rounded:
  sm: 2px
  md: 3px
  lg: 5px
  pill: 3px
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
  ground-lower:
    backgroundColor: "{colors.ground-bottom}"
    textColor: "{colors.text}"
    typography: "{typography.body}"
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.lg}"
    padding: 20px
  card-media:
    backgroundColor: "{colors.secondary}"
    rounded: "{rounded.md}"
    height: 96px
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
  nav:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-muted}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
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

**This kit is the ground, not the sky.** It is the surface a mission is standing on: grey-brown
regolith (#e6e2d7 at the top of the page settling to #d2ccbf), a near-black warm ink, one
dust-covered amber for action, and a cold blue-grey that appears for exactly one reason — on the
Moon the shadow really *is* blue, because airless shadow is lit by earthshine and starlight and
nothing else. There is no violet, no neon, no glow, no starfield and no black in this palette. It
is a mineral register, and the material is granular.

**Two grades of one material.** Regolith is drawn, not sampled, and it ships in two grades because
one cannot do both of this kit's jobs:

- `--moon-rover-dust` — the **ground grade**. Sunlit chalk grains with every darkening element
  capped at 11% alpha, because type sits on it. Composited from the shipped artwork, the worst
  pixel — every darkening layer of the texture landing on the same spot, over the darkest `--bg`
  stop — still measures **7.53:1** for `{colors.text}` and **4.78:1** for `--text-dim`.
- `--moon-rover-grit` — the **material grade**. The same regolith with its micro-shadows kept:
  each grain has a lit facet and a real shaded facet and a hairline cast sliver. It is used only
  where no type can sit — the card media panel and the signature tiles.

That split is the kit's load-bearing decision. Regolith with honest micro-shadows is not a
background you can set 12px captions on; pretending otherwise is how a kit ships as "dusty
colours" with unreadable hints.

**The hard sun is a geometry, not a blur.** Every shadow is a **zero-blur offset plate** —
`--shadow-1`/`--shadow-2`, `--btn-shadow`, `--bar-shadow`, `--bar-item-shadow`, `--toggle-shadow`,
`--toggle-knob-shadow`, `--glow`. The media panel's shadow is a **caster and its projection**: a
low boulder field in the artwork, and that silhouette put through a shear matrix — so the shadow is
*longer than the object*, which is the one thing a drop shadow can never say — drawn translucent so
the grain of the ground still reads inside the darkness. (The first version of that panel used a
straight hard-stop gradient band: in a real 300×96 card it read as a stray dark overlay, because a
shadow with no caster, no contact line and no shape is a stripe.) `--blur` is `none`; an airless
body has no diffusion.

One sentence: *the lunar surface and the machine standing on it — grey-brown regolith under one
unfiltered sun, hard black shadow plates, drawn dust, and one dust-covered amber doing all the
acting.*

## Colors

- **Primary (#d9821c) — the dusty amber, and it is a FILL.** It fills the primary button, the
  checked controls, the progress bar and the avatar, and nothing else. It is the colour of hardware
  that has been out in the dust: saturated enough to act, dirty enough not to glow. As a label on
  this ground it measures **1.83:1** — a fill is not an ink.
- **Primary-hover (#eb9a33) — the dust is blown off it.** The plate comes *up* on press, which is
  both the physically honest move (a sunlit surface under a hand) and the legible one: its own
  label rises from 6.23:1 to **8.01:1**.
- **Primary-ink (#191410)** — dust-black printed *on* the amber plate. An amber fill takes dark
  ink, never white (white on #d9821c is ~2.2:1).
- **Primary-text (#5e2b03) / primary-text-hover (#4a2102)** — the amber *as text*: eyebrows, links,
  active nav and tab labels, secondary-button labels, inline code, `.table code`. A wet-rust brown
  of the same family: **6.22:1** on the deepest recess and **5.76:1** on its own 15% tint
  composited over that recess. This pair is why the palette works at all.
- **Secondary (#4a6a86) — shadow blue-grey.** The one cold colour in the kit and the reason the
  palette is not monochrome-warm. It is the shadow side of the media panel and the second stop of
  fills; it **never acts**. Its darker family members are `--info` (#26405a) and `--focus-ring`
  (#2e4a63).
- **Tertiary (#26405a) — telemetry blue.** Data and readouts, so an instrument never borrows the
  action colour. (It is `--info` in `tokens.css`.)
- **Neutral (#ded9cd)** — the ground's dominant stop and the solid stand-in, since `colors:` cannot
  hold a gradient (the linter errors on one). The two ramp stops ship as colours of their own:
  **ground-top (#e6e2d7)** and **ground-bottom (#d2ccbf)**, referenced by `page` and `ground-lower`.
- **Surface (#eeeae0) / surface-2 (#c4beb0)** — and note the *direction*, because it is the whole
  light model: a **card is a sunlit plate**, a shade **lighter** than the ground (#eeeae0 against a
  #d2ccbf lower ground), and an **inset is a scooped recess**, a shade **darker** (#c4beb0) — the
  same regolith with the sun taken off it. Neither is white paper, neither is a black well.
- **Text (#1e1c17) / text-muted (#38332b)** — the near-black warm ink and its second step.
- **Success (#1f4a28) / warning (#553d04) / error (#7a2714)** — deep mineral inks: a dark dusty
  green, a deep ochre and an oxide red. All three are solved on `--surface-2`, the **darkest**
  ground any of them is drawn on (a badge keeps its own recess background), not on the easy pale
  card. `--warn` is deliberately an ochre rather than a dimmed amber, so a caution never reads as
  the action.

Deliberately not in the map above: `--text-dim: #423d31` (captions, hints, table headers, the
binding pair in this kit), `--accent-ink-hover`, `--border: #a49c8a` / `--border-strong: #786f5d`
(the hard seams — the DESIGN.md component schema has no `borderColor` property),
`--accent-soft: rgba(217,130,28,.15)` (a translucent tint is not a colour), `--focus-ring`
(#2e4a63) and `--accent-2` as a fill. Listing any of them would only produce orphan warnings for
values that are very much in use. Exact values are in `tokens.css`.

## Typography

A **stamped-hardware voice**, in two families plus an instrument mono:

- **Saira Condensed — display.** A condensed technical grotesque. Hardware lettering *is* condensed
  and heavy, because it is stencilled onto a curved plate with a pantograph rather than set in a
  book; the condensed face is the closest honest analogue of a stamped data plate in the Google
  library. It sets the h1, section headings and card titles.
- **Saira — body.** The same superfamily at text width, so a plate's label and a plate's note share
  a hand rather than merely coexisting. This is the face a paragraph is read in.
- **Fira Mono — labels, eyebrows, badges, table headers, readouts.** A rover's data plate, not a
  HUD and not a terminal: mono is what an instrument prints in. The `readout` register (0.9rem,
  +0.01em) carries IDs, version strings and numerals so a column of figures lines up as
  instrumentation.
- Caps labels are tracked **+0.12em** — stamped and tracked, tighter than a HUD's 0.14–0.18em,
  because a pressed label is compressed into metal, not spaced out on glass.
- **Upright, always.** `--style-display: normal`: stencils do not lean. The contract names a font
  *family*, never its style, so `--style-display` is declared rather than left to a fallback.

There is no third face and nothing decorative: this kit's character is in the material, not in the
lettering.

## Layout

The shared column (`min(1040px, 100% - 2.5rem)`) over a dust-textured regolith ground. Section
boundaries are 2px machined seams; inside a panel the rhythm is tight (8–14px) so controls group by
proximity rather than by boxing. Cards are an auto-fit grid that collapses to one column on a phone.

Controls are 40px tall with 12px×20px button padding and 20px card padding. The spacing scale runs
4 · 8 · 16 · 28 · 44, and the gap between the ground band and the ground band below it is the 44px
step, so the page breathes the way a wide flat surface does.

## Elevation & Depth

**Depth is a plate of shadow, not a haze.** `--shadow-1` is `4px 4px 0 0 var(--moon-rover-shade)`
plus a one-pixel sunlit lip (`inset 1px 1px 0 rgba(255,253,246,.58)`); `--shadow-2` is the same at
`7px 7px`. The plate measures **2.2:1 against the ground** — a shadow you can see, not a hint. Both are zero-blur, because a shallow sun throws a plate of shadow and that plate has an
edge. There is no blurred drop shadow anywhere in this kit.

- **Every button variant** wears `--btn-shadow` (`3px 3px 0 0`), not just the primary: on a surface
  where everything is lit from one direction, everything casts.
- **The primary plate casts further** (`--glow`: `5px 5px`), because a raised plate on a sunlit
  surface throws a longer shadow than a flush one. `--glow` is reused as the hard plate rather than
  a halo — there is nothing to glow here.
- **Nav and tabs are milled into the ground** (`--bar-shadow`: `inset 0 2px 0`), and the current
  item is a plate riding in that channel (`--bar-item-shadow`).
- **Inputs are scooped** (`--input-inset`): the sunward inner wall of the scoop is in shadow
  (dark, top-left) and the wall opposite catches the light (lit, bottom-right). That is the same
  light model as the cast shadows, inverted — and it is why the recess reads as a hole rather than
  as a raised bevel.
- `--blur: none`. `card-elevated` uses `--surface-2` and `--shadow-2`, so it is *more* recessed,
  not more lifted.

## Shapes

Crisp plate geometry: `--radius-sm: 2px`, `--radius-md: 3px`, `--radius-lg: 5px`, and
**`--radius-pill: 3px`** — deliberately *not* a capsule. Nothing on a rover is rounded, so badges,
the toggle track, the switch knob, status dots and the avatar are all square-ish machined plates;
that single decision does more to distinguish this kit's silhouette than any colour.

`--cut: 0px` and **no `--clip`**: this kit wants its 2px frame on all four edges. A chamfer would
cut the border along the diagonal, eat the zero-blur cast shadows that *are* the kit, and force the
focus ring inward — three costs for a silhouette this palette does not want.

**Square native controls.** `--check-appearance: none` with a 2px rim (`--check-border`), a pale
plate (`--check-bg: #eeeae0`) and a filled amber square when checked (`--check-checked`). Native
checkboxes ignore `border-radius`, so without this a kit whose only shape rule is "square" would
render round radios.

## Components

- **button-primary** — the amber plate: dust-black label (`{colors.primary-ink}`) in the mono label
  style, 3px radius, 2px rim, and the longest hard shadow in the kit. It is a fill, never a text
  colour.
- **button-primary-hover** — the same plate with the dust blown off (`{colors.primary-hover}`),
  still dust-black. See Colors for why the fill brightens rather than darkens.
- **button-secondary / button-ghost / button-danger** — plates in the sunlit surface, the ground
  tone or open, taking wet-rust, muted-ink or oxide-red labels. Secondary actions are recessed or
  flush, never filled: only one thing in this kit is amber.
- **card / ground-lower / card-media** — the sunlit plate, the ground's lower stop, and the media
  panel. The media panel is where the kit paints a **surface** rather than a colour: a boulder field
  and its cast shadow, regolith at two scales, opaque (`--media-op: 1`).
- **card-title** — Saira Condensed at weight 650–700: a stencilled plate heading, read across a
  field.
- **input** — the scooped recess (`{colors.surface-2}`) with a 2px machined rim; on focus the rim
  takes the amber and the well takes a 3px `--accent-soft` halo.
- **badge / badge-accent / badge-ok / badge-warn / badge-danger** — 3px-radius stamped plates in the
  recess, with the amber tint carrying the accent label and the deep mineral inks carrying status.
  None of them is a capsule.
- **table-header** — mono, uppercase, +0.12em, muted: the engraved column legend.
- **nav / alert-\*** — a milled channel with a plate riding in it, and recessed frames with a 3px
  rule down the left edge (telemetry blue, dusty green, ochre, oxide red), one step wider than the
  kit's own 2px seam so the rule reads as a warning lamp.
- **link** — wet rust, underlined on hover: the same ink family as the action, because a link is an
  action even when it cannot be a fill.

## Do's and Don'ts

- **Do** keep the amber for fills. Set accent text in `{colors.primary-text}` (#5e2b03) — the fill
  is 1.83:1 as a label and no weight rescues it.
- **Do** use the ground grade of the texture anywhere type sits, and the material grade only where
  it does not. That split is the kit.
- **Do** express depth as a hard offset plate. If something needs a blur to be legible, it is the
  wrong element.
- **Do** keep radii at 2–5px, including badges. The 3px "pill" is a specification, not an oversight.
- **Do** let the shadow be longer than the object — that is what a low sun does.
- **Do** keep the blue-grey for shadow, telemetry and focus. It is the only cool note.
- **Don't** add a third saturated colour, a glow, a starfield, a violet, or anything that could be
  called cosmic. This is the ground, and the sky is out of frame.
- **Don't** put white on the amber plate. It takes dust-black (#191410).
- **Don't** blur anything: `--blur` is `none`, and a soft shadow would undo the entire premise.
- **Don't** lighten the ground to "calm it down". The inks are solved against the darkest stop and
  the texture's worst composite; raising the ground past #ded9cd starts costing margins that were
  paid for.
