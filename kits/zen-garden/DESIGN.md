---
version: alpha
name: Zen Garden
description: Peace and tranquility on a grey, rainy day — an overcast ground, wet-stone charcoal ink, one deep moss-sage action colour and a rain-blue second accent.
colors:
  primary: "#4a6658"
  primary-hover: "#40594b"
  secondary: "#567694"
  tertiary: "#40594b"
  neutral: "#e8ecf0"
  bg-stop-1: "#eef2f6"
  bg-stop-2: "#e8ecf0"
  bg-stop-3: "#e2e8ee"
  bg-2: "#eef2f6"
  surface: "#f2f5f8"
  surface-2: "#e6eaf0"
  overlay: "rgba(43,50,56,0.42)"
  text: "#2b3238"
  text-muted: "#4d585f"
  text-dim: "#565f69"
  text-invert: "#ffffff"
  accent-soft: "rgba(74,102,88,0.10)"
  ok: "#33714d"
  warn: "#8a6220"
  danger: "#a8453d"
  info: "#43668e"
  border: "#cdd5dd"
  border-strong: "#aab6c2"
  focus-ring: "#3c6b93"
typography:
  display:
    fontFamily: "Source Serif 4"
    fontSize: "2.9rem"
    fontWeight: 600
    lineHeight: 1.12
    letterSpacing: "-0.012em"
  heading:
    fontFamily: "Source Serif 4"
    fontSize: "1.3rem"
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: "-0.006em"
  body:
    fontFamily: "Inter"
    fontSize: "0.95rem"
    fontWeight: 400
    lineHeight: 1.62
  label:
    fontFamily: "IBM Plex Mono"
    fontSize: "0.72rem"
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: "0.08em"
rounded:
  sm: "8px"
  md: "10px"
  lg: "14px"
  pill: "999px"
spacing:
  xs: "0.35rem"
  sm: "0.65rem"
  md: "1.15rem"
  lg: "2.25rem"
  xl: "3.5rem"
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.text-invert}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: "0.58rem 1rem"
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.text-invert}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: "0.58rem 1rem"
  button-secondary-hover:
    backgroundColor: "{colors.accent-soft}"
    textColor: "{colors.primary-hover}"
    rounded: "{rounded.md}"
  button-ghost:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-muted}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
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
  card-title:
    textColor: "{colors.text}"
    typography: "{typography.heading}"
  input:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: "0.6rem 0.72rem"
  badge:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text-muted}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "0.2rem 0.55rem"
  badge-accent:
    backgroundColor: "{colors.accent-soft}"
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
  nav:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-muted}"
    rounded: "{rounded.md}"
    padding: "0.4rem"
  nav-active:
    backgroundColor: "{colors.accent-soft}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
  alert-info:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.info}"
    rounded: "{rounded.md}"
    padding: "0.8rem 0.95rem"
  alert-danger:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.danger}"
    rounded: "{rounded.md}"
    padding: "0.8rem 0.95rem"
  link:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.primary}"
---

## Overview

Zen Garden is a **mood kit**: peace and tranquility on a grey, rainy day. It is a light
theme, and its ground is not white and not cream — it is a cool, slightly desaturated
rainy-day grey, because cream would make the afternoon sunny and white would make it
sterile. Everything else follows from that one decision.

Three rules carry the mood:

1. **Overcast, not sunny.** A cool grey ground (`#e8ecf0`) with mist (`#eef2f6`) above it
   and rain (`#e2e8ee`) below. No warm tint anywhere in the neutrals.
2. **Wet stone and moss.** Ink is a soft charcoal with a cool cast (`#2b3238`) — never
   pure black, which would be an edge. The single action colour is a deep moss sage
   (`#4a6658`); the one second hue is a rain-blue (`#567694`).
3. **Quiet depth and generous air.** 1px hairlines, soft wide shadows at low opacity,
   gentle 8–14px radii, a slower-than-usual transition. Nothing snaps, nothing glows,
   nothing is square.

Use it for journaling, wellness and habit apps, calm reading interfaces, personal sites,
meditation or breathwork tools — anywhere the interface should get out of the way. Do
**not** use it for dashboards that need to alarm, dense data tooling, or marketing that
must shout; this kit has deliberately spent its loudness budget on legibility and nothing
is left over for emphasis.

One sentence: *wet stone, moss sage and rain blue on an overcast afternoon.*

## Colors

The palette is a grey ground plus exactly two hues. There is no third "look at me"
colour, and it took a numeric pass to get the sage right.

| Role | Token | Value | Contrast |
|---|---|---|---|
| Overcast ground | `--bg` | `#e8ecf0` | — |
| Mist / ground lift | `--bg-2` | `#eef2f6` | — |
| Ground stops (for mist) | `bg-stop-1/2/3` | `#eef2f6` / `#e8ecf0` / `#e2e8ee` | — |
| Card | `--surface` | `#f2f5f8` | — |
| Nested panel / input | `--surface-2` | `#e6eaf0` | — |
| Body ink | `--text` | `#2b3238` | **10.94:1** on `--bg` |
| Secondary ink | `--text-muted` | `#4d585f` | **6.67:1** on `--surface` |
| Tertiary ink | `--text-dim` | `#565f69` | **5.37:1** on the darkest ground |
| Ink on the action | `--text-invert` | `#ffffff` | **6.30:1** on `--accent` |
| Action (moss sage) | `--accent` | `#4a6658` | **5.31:1** as a link on `--bg` |
| Second accent (rain blue) | `--accent-2` | `#567694` | fill only, never text |
| Focus | `--focus-ring` | `#3c6b93` | deep rain blue |
| Hairline | `--border` | `#cdd5dd` | — |
| Emphasised line | `--border-strong` | `#aab6c2` | — |

**Primary (`#4a6658`)** is the whole action vocabulary: primary buttons, links, inline
code, focus tint, active nav. It is a *deep* moss, not a mint — see below.

**Secondary (`#567694`)** is the rain-blue. It exists for gradients, media plates, chart
bars and avatars — the moss-to-rain wash on `--card-media` and the progress bar is the
one place the two accents meet. It is a fill, never body text, and never a second call to
action.

**Tertiary (`#40594b`)** is the pressed step of primary, not a third hue. The DESIGN.md
schema asks for a `tertiary`, and this kit's honest answer is that it has exactly two
hues by design — so `tertiary` is the same colour family as `primary`, one step deeper.
Adding a real third colour here would be the failure this kit is built to avoid.

**Neutral (`#e8ecf0`)** is the overcast ground. It is the single most important value in
the kit; if you warm it, the rain stops.

**The sage was darkened on purpose.** The starting point was a lighter `#5f7d6a`. At that
value, white on the sage measured **4.54:1** — a hair above the 4.5 floor — and, worse,
sage used as a link colour on the overcast ground measured **3.82:1**, a real failure.
Lightening the ground to fix it is the wrong move; it would push the kit toward cream.
Darkening the accent to `#4a6658` lifts white-on-sage to 6.30:1 and sage-on-ground to
5.31:1 while keeping the kit unmistakably "muted botanical". Do not lighten it back.

**`--accent-soft` is a 10% tint, not 14%.** Tinting the action colour's own background
more heavily erodes the action colour's contrast against it; at 10% (
`rgba(74,102,88,.10)`) the sage still clears 4.5:1 on its own tint over any ground, which
is what active nav and `badge-accent` depend on. Every tint in the kit is expressed as
`rgba(...)` of `--accent` rather than as a new hand-picked hex, so it can never drift.

**The mist gradient is not in this `colors:` map.** A gradient is not a colour and the
linter errors on one. Its three stops ship as `bg-stop-1/2/3` (`#eef2f6` / `#e8ecf0` /
`#e2e8ee`), and the live gradient is `--zen-garden-mist` in `tokens.css`.

**Status colours bracket the brand hues rather than borrow them.** `ok` is a leaf green
(`#33714d`) deliberately *more* saturated than the moss action; `warn` is ochre
(`#8a6220`); `danger` is clay (`#a8453d`); `info` is a deeper rain blue (`#43668e`) than
`--accent-2`, so an info alert never reads as a decorative gradient stop. A failed state
must never be mistakable for the calm action.

## Typography

Three faces, each with one job. The display face is the mood; the others stay quiet.

- **Source Serif 4** (display) — headings, the wordmark, card titles, the lab's `h1`.
  A **humanist** serif: open counters, calligraphic stress, and a low-contrast,
  unhurried rhythm. A serif reads as *contemplative* here — a garden journal or a temple
  inscription rather than a product headline — and, practically, it gives the kit real
  hierarchy: a serif over a sans body separates the two levels by letterform, not only by
  size, which is exactly the defence against a muted palette sliding into grey mush.
- **Inter** (body) — everything you actually read. Neutral on purpose, so the serif is
  the only warm voice on the page.
- **IBM Plex Mono** (labels) — eyebrows, badges, table headers, code. A *humanist* mono,
  softer than the library's JetBrains/Share Tech terminals, so labels stay legible without
  turning into a machine voice.

The alternative considered was a single gentle gothic sans — **Zen Kaku Gothic New** — for
display and body. It was rejected: two sans faces flatten the hierarchy exactly where this
palette can least afford it, and it would tie the kit to a Japanese aesthetic the brief
never asked for. This kit is a *mood*, not a region.

Display is only lightly tightened (`-0.012em` — a serif does not want more). Mono labels
are tracked to `0.08em`, half the library's shout, because nothing here should be loud.

## Layout

The shared lab measure — `min(1040px, calc(100% - 2.5rem))` — with a
`0.35 / 0.65 / 1.15 / 2.25 / 3.5rem` spacing scale. Density is **loose**: block padding,
card padding and the gap scale all sit a notch above the library's defaults, because air
is the mood. Generous space is what makes a thin hairline and a low-alpha shadow read as
*calm* instead of as *timid*.

## Elevation & Depth

Depth is weather, not architecture. Nothing lifts off the page; surfaces settle into air
that is a little darker underneath.

- `--shadow-1` — cards: a 1px contact shadow plus a wide `26px` drop at `-14px` spread and
  22% of the stone ink. Large radius, low opacity, barely there.
- `--shadow-2` — elevated surfaces: the same idea, wider (`52px`) and softer, so an
  elevated card reads as *further from the ground*, not as more raised.
- `--glow` — the primary button only, and it is **a shadow, not a bloom**: a sage-tinted
  `0 8px 22px -12px rgba(74,102,88,.50)`. There is no coloured light in this kit. If it
  ever looks like a glow, it is too strong.
- `--blur: none` — overcast is not glassy, and frosted glass would put a hard, high-
  contrast edge around every surface.

## Shapes

Gentle and continuous: `--radius-sm: 8px`, `--radius-md: 10px`, `--radius-lg: 14px`, and
`999px` pills for badges, avatars, toggles and progress bars. `--cut: 0px` — nothing is
notched, ever; a chamfer is a decision, and this kit's decision is that there are no
decisions.

The band is deliberate. Below 8px the corners start to read as crisp and technical, which
fights the mood; above 14px every plate becomes a lozenge and the interface stops being
able to hold a grid. 8–14px is the calm register.

## Components

Every colour resolves to a `{colors.*}` token; nothing is re-typed. Shadows, hairlines and
gradients live in the prose here and in `tokens.css`, because the component schema has no
property to express them.

- **button-primary** — a solid `{colors.primary}` moss plate with `{colors.text-invert}`,
  10px radius, the soft sage `--glow` beneath. It is the only solid saturated object on a
  screen, which is what makes the muted palette still have a clear focal point.
- **button-primary-hover** — `{colors.primary-hover}`, one step *deeper*. A calm
  interface presses down rather than lighting up.
- **button-secondary** — `{colors.surface}` with a moss label and a moss-tinted rim
  (`color-mix` 45%); hover fills with the 10% `{colors.accent-soft}` wash.
- **button-ghost** — `{colors.text-muted}` with no rim at all; the quietest control.
- **card / card-elevated** — `{colors.surface}` and `{colors.surface-2}` at 14px,
  separated by a 1px `{colors.border}` hairline and `--shadow-1`, never by a hard edge.
- **input** — `{colors.surface-2}` settled *below* the card it sits in, ringed with
  `{colors.border-strong}` rather than the page hairline, so a field reads as a recess and
  not as a floating box. Focus swaps to the moss border with a `{colors.accent-soft}`
  halo; the keyboard ring is `{colors.focus-ring}` deep blue so hover and focus never
  look alike.
- **badge** — `{colors.text-muted}` mono caps in a pill on `{colors.surface-2}`.
  `badge-accent` is the 10% sage tint with a moss label; `badge-ok` / `badge-warn` /
  `badge-danger` use the status greens, ochre and clay.
- **nav / nav-active** — a `{colors.surface}` pill bar; the current item takes
  `{colors.accent-soft}` with a moss label, the calmest possible "you are here".

## Do's and Don'ts

**Do**

- Keep the ground cool. Every neutral step — `--bg`, `--bg-2`, `--surface`, `--surface-2`
  — is blue-grey, and keeping the whole ramp cool is what makes the kit read as weather
  rather than as a paper app.
- Let the moss mean "act" and the rain-blue mean "atmosphere". One primary per screen.
- Keep hairlines at 1px and radii inside 8–14px. The restraint *is* the design.
- Spend the space. Loose padding and slow transitions are doing as much work here as the
  colours are.
- Reach for `--zen-garden-mist` (or the three `bg-stop-*` stops) when a surface needs
  weather behind it, and keep `--bg` itself solid so the shared lab's masthead wash keeps
  working.

**Don't**

- Don't warm the neutrals. An off-white or a cream ground turns this into a generic light
  theme and the rain stops falling.
- Don't lighten `--accent` back toward `#5f7d6a`. It fails as a link colour on this ground
  (3.82:1). Darken for failures; never lighten the ground.
- Don't tint `--accent` backgrounds above 10%. `--accent-soft` is load-bearing: active nav
  and `badge-accent` put moss text on it, and a heavier tint drops them under 4.5:1.
- Don't introduce a third hue, and don't use `--accent-2` as body text — it is a fill
  colour and measures under 4.5:1 on the ground.
- Don't add a glow, a hard shadow or a 2px border. Leave the surfaces soft.
- Don't put pure black on the page. `--text` is stone, not ink-black.
