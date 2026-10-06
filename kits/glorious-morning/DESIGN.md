---
version: alpha
name: Glorious Morning
description: First light as UI — a clear-sky gradient ground that opens on a gold dawn band, a light-ray wash over it, and one sunrise-gold action colour with a clear sky blue as its cool counterweight.
colors:
  primary: "#f0a90c"
  primary-hover: "#d99400"
  primary-text: "#7d5200"
  primary-text-hover: "#5f3d00"
  on-primary: "#0f2136"
  secondary: "#3a9be0"
  tertiary: "#187a43"
  neutral: "#f3faff"
  bg-stop-1: "#eaf5ff"
  bg-stop-2: "#d6e9fc"
  bg-stop-3: "#ffecc6"
  bg-stop-4: "#ffdf9e"
  bg-stop-5: "#f9f0e1"
  bg-stop-6: "#f3faff"
  bg-2: "#f0f7ff"
  surface: "#fbfdff"
  surface-2: "#e9f2fd"
  overlay: "rgba(12,32,58,0.42)"
  text: "#0f2136"
  text-muted: "#3a4c64"
  text-dim: "#4d5d72"
  text-invert: "#0f2136"
  accent-soft: "rgba(240,169,12,0.16)"
  ok: "#187a43"
  warn: "#96631a"
  danger: "#c2352f"
  info: "#2f66c4"
  border: "rgba(26,58,102,0.14)"
  border-strong: "rgba(26,58,102,0.30)"
  focus-ring: "#1668bf"
  ramp-sky: "#8ecdf5"
  ramp-haze: "#bcdcf3"
  ramp-gold: "#f7b733"
  ramp-sun: "#f0a90c"
  leaf: "#38b26a"
typography:
  display:
    fontFamily: "Fraunces"
    fontSize: "2.75rem"
    fontWeight: 700
    lineHeight: 1.06
    letterSpacing: "-0.015em"
  heading:
    fontFamily: "Fraunces"
    fontSize: "1.3rem"
    fontWeight: 600
    lineHeight: 1.22
    letterSpacing: "-0.01em"
  body:
    fontFamily: "Nunito Sans"
    fontSize: "0.95rem"
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: "DM Mono"
    fontSize: "0.72rem"
    fontWeight: 400
    letterSpacing: "0.12em"
  code:
    fontFamily: "DM Mono"
    fontSize: "0.8rem"
    lineHeight: 1.6
rounded:
  sm: "8px"
  md: "12px"
  lg: "18px"
  pill: "999px"
spacing:
  xs: "0.4rem"
  sm: "0.75rem"
  md: "1rem"
  lg: "2.25rem"
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: "0.58rem 1rem"
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary-text}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: "0.58rem 1rem"
  button-secondary-hover:
    backgroundColor: "{colors.accent-soft}"
    textColor: "{colors.primary-text-hover}"
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
  input:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: "0.6rem 0.72rem"
  input-focus:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.md}"
  badge:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text-muted}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "0.2rem 0.55rem"
  badge-accent:
    backgroundColor: "{colors.accent-soft}"
    textColor: "{colors.primary-text}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
  badge-ok:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.ok}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
  badge-danger:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.danger}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
---

# Glorious Morning

First light, rebuilt as a working UI kit. The ground is a clear-sky gradient that opens on a
**gold dawn band inside the first screen**, a light-ray wash crosses it, and one
**sunrise-gold** action colour sits against a **clear sky blue** — with a deep cool ink doing
all the reading. Bright, awake, energetic; the opposite number to a rainy day.

## Overview

This kit is one of three in the library about a time of day, and the differentiator is *time
and energy*, not hue:

| Kit | Time | Feeling |
|---|---|---|
| `zen-garden` | overcast grey | quiet, static, restrained |
| `summer-sunset` | dusk | synthwave, nostalgic, warm-dark |
| **`glorious-morning`** | **first light** | **clear, awake, optimistic, energetic** |

Two rules carry it:

1. **The ground is air, not paper.** `--bg` is a very light *sky* tint — six stops of clear
   sky, warm haze, gold and settling air — never cream and never plain white. White would
   make it a document; cream would make it `summer-sunset`.
2. **The signature is the dawn itself.** A cool-sky-to-gold sunrise ramp, a light-ray wash, a
   low sun bloom in the top-left of the first screen and a dew sheen. All of it ships as
   `--glorious-morning-*` and is rendered in the lab's **Signature** section.

It is deliberately *not* the other two light kits it could be confused with:

- **Not `glass`.** Glass is pastel translucency — `--surface` is `rgba(255,255,255,.58)` and
  `--blur` is a load-bearing `blur(20px)`. Here `--blur: none`, `--surface` is an opaque crisp
  `#fbfdff`, and the only translucency in the kit is the faint hairline. Nothing is frosted.
- **Not `cyber-angel`.** Cyber-angel is a structural light shell: **black 1px rules**,
  **45° chamfers** (`--cut: 12px` + `--clip`), holo cyan. Here there are **no black rules**
  (`--border` is a 14% cool-navy hairline) and **no chamfers at all** (`--cut: 0px`, `--clip`
  is never declared). This kit has no geometry — it has light.

Use it for morning-fresh product launches, wellness and habit apps, education and children's
products, onboarding flows, and anything that should feel like a clear start. Do not use it for
night-time, dense data tooling, or anything that wants menace.

## Colors

| Role | Token | Value | Contrast |
|---|---|---|---|
| Ground | `--bg` | gradient `#eaf5ff` → `#f3faff` | — |
| Ground (check stop) | — | `#ffdf9e` (dawn band) | worst case for dark ink |
| Card | `--surface` | `#fbfdff` | — |
| Nested / input | `--surface-2` | `#e9f2fd` | — |
| Body ink | `--text` | `#0f2136` | **12.6:1** on the dawn band, 16.0:1 on `--surface` |
| Secondary ink | `--text-muted` | `#3a4c64` | **8.6:1** on `--surface` |
| Tertiary ink | `--text-dim` | `#4d5d72` | **5.2:1** on the dawn band, 6.6:1 on `--surface` |
| On-gold ink | `--text-invert` | `#0f2136` | **8.0:1** on `--accent` |
| Action (fill) | `--accent` | `#f0a90c` | sunrise gold |
| Action (**text**) | `--accent-ink` | `#7d5200` | **5.3:1** on the dawn band |
| Cool counterweight | `--accent-2` | `#3a9be0` | clear sky blue |
| Third (structure) | `--glorious-morning-leaf` | `#38b26a` | leaf green, decorative |
| Focus | `--focus-ring` | `#1668bf` | **4.3:1** on the dawn band |

**`--bg` is a gradient, and its stops are in PX.** The body's gradient box is the whole
document, so a `0–100%` ramp would smear these six stops over thousands of pixels: the first
screen would render a single flat pale plate and the dawn band — the entire point of the kit —
would sit far below the fold. With `0px … 760px` the full sequence lands in view at any page
length. `--bg-2: #f0f7ff` is the solid stand-in for exports and for tools that cannot parse a
gradient token.

**Contrast is checked against the *darkest* stop, `#ffdf9e` (the dawn band).** Of the six
stops it has the lowest luminance, so it is the worst case for dark ink; the other five all
score higher (13.1:1 to 15.4:1 for `--text`). This is the constraint that shapes the ink: the
dawn band is much darker than a white page, so `--text-dim` **cannot** be a pale grey —
`#4d5d72` is the lightest cool slate that still clears 4.55:1 there. Lightening the ink is the
wrong direction — a darker ink on a light ground is not the failure mode; a washed-out one is.

**Ink is deep COOL navy and `--text-invert` equals `--text`.** White on `#f0a90c` is about
1.9:1 — the sun is dark-on-gold, exactly as it is dark-on-orange in `summer-sunset`. Do not
"fix" this by lightening `--text-invert`.

**Gold is the classic `--accent-ink` trap, and this kit ships the fix.** `#f0a90c` is a
superb button fill (8.0:1 with ink on it) and an unreadable small label (1.9:1 on the ground).
So the kit declares a separate member of the same family for accent-as-text: `--accent-ink:
#7d5200` (5.3:1 on the dawn band, 6.7:1 on `--surface`), with `--accent-ink-hover: #674300`.
The eyebrow, links, active nav/tab, secondary-button labels, inline code and `badge-accent`
all use `--accent-ink`, never `--accent`.

**The gold is gold, not orange.** `#f0a90c` sits at hue 41°; `summer-sunset`'s action orange
`#ff7a1a` is at hue 25°. They are the same *warmth* and a visibly different colour.

**Status never borrows the brand hues.** `--ok` is a fresh leaf green `#187a43` (the third
colour, and readable at 4.8:1 on `--surface-2`), `--warn` is a deep ochre `#96631a` held well
away from the gold action, `--danger` is a true red `#c2352f`, `--info` is a deeper sky blue
`#2f66c4`. A failed state must never be mistakable for the gold primary.

**The gradients themselves are not in the `colors:` map above** — that block only accepts CSS
colours. The six ground stops ship as `bg-stop-1..6`, the sunrise ramp's four stops ship as
`ramp-sky / ramp-haze / ramp-gold / ramp-sun`, and the leaf ships as `leaf`. The live gradient
definitions are in `tokens.css` as `--glorious-morning-sunrise`, `--glorious-morning-ray`,
`--glorious-morning-sun` and `--glorious-morning-dew`.

## Typography

A three-face pairing chosen to sound like a good morning rather than a machine:

- **Fraunces** (display) — a warm humanist soft-serif with an optical-size axis. It reads like
  a hand-set greeting card: it is the one thing in the kit that is *human* rather than
  *celestial*, which is what keeps "first light" from turning into a weather report. Used for
  `h1`–`h3`, card titles and the wordmark.
- **Nunito Sans** (body) — a rounded humanist sans. Its open, slightly round terminals keep
  paragraphs friendly and daylight-bright; a neutral grotesque here would make the palette
  feel clinical.
- **DM Mono** (labels) — eyebrows, badges, table headers, timestamps, code. Quiet, low-contrast
  in texture, and warmer than the JetBrains/IBM Plex monos already in the library.

Display is barely tracked (`-0.015em`) because a soft serif wants only a whisper of
tightening; mono labels are wide (`.12em`). Body copy is never set in the display or mono face.

## Layout

The shared 1040px measure, 2.25rem between blocks and a `0.4 / 0.75 / 1 / 2.25rem` spacing
scale. Density is open but not sparse: the ground is doing work in the top third, so the
content below it wants air around it to stay legible against the sky.

## Elevation & Depth

Depth is light, and it is warm.

- `--shadow-1` — cards: a soft, wide, low-alpha cool-navy drop. It barely reads, which is
  right: the card is a *lift of air*, not an object.
- `--shadow-2` — elevated surfaces: the same, wider and slightly stronger.
- `--glow` — the primary button only: a warm gold halo beneath it, `0 10px 26px -10px
  rgba(240,169,12,.50)`. The gold button looks lit from underneath, like the sun arriving.
  It is deliberately the only warm shadow in the kit; `--glorious-morning-halo` is the same
  idea as a reusable extra.
- `--blur: none` — **this is the line between `glorious-morning` and `glass`.** Nothing is
  frosted. Air is transparent, not translucent.

## Shapes

Open and generous, never notched: `--radius-sm: 8px`, `--radius-md: 12px`, `--radius-lg: 18px`,
pills on badges, avatars and toggles. **`--cut: 0px` and `--clip` is never declared** — there
are no chamfers anywhere. Sharp geometry belongs to `cyber-angel` and `geometric-dimensions`;
this kit has no corners to cut because it has no edges, only hairlines.

## Components

Every component colour resolves to a `{colors.*}` token; nothing is re-typed.

- **button-primary** — `{colors.primary}` gold fill, `{colors.on-primary}` deep navy label,
  12px radius, plus the warm `--glow` halo. The one solid gold object on a screen: the sun.
- **button-primary-hover** — `{colors.primary-hover}` deeper gold, so the button presses down
  into the horizon instead of lifting out of it.
- **button-secondary** — `{colors.surface}` on a hairline with `{colors.primary-text}`
  (the readable bronze) type; hover fills with the 16% `{colors.accent-soft}` gold wash and
  steps the label to `{colors.primary-text-hover}`.
- **card** — `{colors.surface}` on a faint cool hairline at 18px with the soft `--shadow-1`.
  Elevated cards step to `{colors.surface-2}`. Because `--surface-2` stays light, card text
  needs no `--text-on-surface*` overrides — one ink family works on every surface here.
- **input** — `{colors.surface-2}` sky fill behind a 1px `{colors.border}` hairline; focus
  swaps to the gold border with a 3px `{colors.accent-soft}` ring, and the keyboard ring is
  `{colors.focus-ring}` sky blue so hover and focus never look alike.
- **badge** — hairline and `{colors.text-muted}` mono caps. `badge-accent` is the gold tint
  with `{colors.primary-text}` type; `badge-ok` and `badge-danger` use the status green and red.

## Do's and Don'ts

**Do**

- Keep the dawn band. `--glorious-morning-sunrise`, `--glorious-morning-sun`, the low
  `--glorious-morning-ray` wash and the masthead's `--accent-soft` bloom are the kit —
  drop them and it becomes a plain pale-blue theme.
- Use `--accent-ink` for every piece of gold text, and `--accent` only for fills.
- Keep `--border-w: 1px` and the hairline faint. Air, drawn once.
- Keep `--blur: none`. The moment panels frost over, this is `glass` with a sun in it.
- Let the gold live in buttons, the ramp and the sun. Prose stays in the cool navy ink.

**Don't**

- Don't put white text on `--accent`; use `{colors.on-primary}` and keep the 8.0:1.
- Don't set body copy in gold, leaf green or sky blue.
- Don't add chamfers. `--cut: 0px` is the point; there is no geometry in morning light.
- Don't lighten `--text-dim` to make the page feel airier — the dawn band is the binding
  constraint and `#4d5d72` is already at the floor there.
- Don't tint the status colours toward the brand — a gold "error" is invisible next to the
  gold primary.
