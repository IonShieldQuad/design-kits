---
version: alpha
name: Summer Sunset
description: An 80s synthwave sunset poster as UI — a warm sunset-sky gradient ground, bold 2px aubergine outlines, and orange, cyan and magenta over the top.
colors:
  primary: "#ff7a1a"
  primary-ink: "#8f3b00"
  secondary: "#06a9c4"
  tertiary: "#ff2ea6"
  neutral: "#fff5ec"
  bg-stop-1: "#fff5ec"
  bg-stop-2: "#ffe3ca"
  bg-stop-3: "#ffd1de"
  bg-stop-4: "#eedaf5"
  bg-2: "#fff0e2"
  surface: "#fffaf5"
  surface-2: "#ffeede"
  overlay: "rgba(42,17,54,0.55)"
  text: "#2a1136"
  text-muted: "#6d3a5e"
  text-dim: "#75506a"
  text-invert: "#2a1136"
  accent-hover: "#ef6a06"
  accent-soft: "rgba(255,122,26,0.16)"
  ok: "#1a7d52"
  warn: "#a86a12"
  danger: "#c8353f"
  info: "#3a6fd8"
  border: "rgba(42,17,54,0.26)"
  border-strong: "rgba(42,17,54,0.60)"
  focus-ring: "#077184"
  ramp-peach: "#ffb37a"
  ramp-orange: "#ff7a1a"
  ramp-magenta: "#ff2ea6"
  ramp-violet: "#7b2ff7"
  sun-core: "#ffd93b"
typography:
  display:
    fontFamily: "Audiowide"
    fontSize: "2.75rem"
    fontWeight: 400
    lineHeight: 1.08
    letterSpacing: "0.01em"
  heading:
    fontFamily: "Audiowide"
    fontSize: "1.3rem"
    fontWeight: 400
    lineHeight: 1.22
    letterSpacing: "0.01em"
  body:
    fontFamily: "Inter"
    fontSize: "0.95rem"
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: "Share Tech Mono"
    fontSize: "0.72rem"
    fontWeight: 400
    letterSpacing: "0.16em"
  code:
    fontFamily: "Share Tech Mono"
    fontSize: "0.8rem"
    lineHeight: 1.6
rounded:
  sm: "4px"
  md: "6px"
  lg: "8px"
  pill: "999px"
spacing:
  xs: "0.4rem"
  sm: "0.75rem"
  md: "1rem"
  lg: "2.25rem"
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.text-invert}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: "0.58rem 1rem"
  button-primary-hover:
    backgroundColor: "{colors.accent-hover}"
    textColor: "{colors.text-invert}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary-ink}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: "0.58rem 1rem"
  button-secondary-hover:
    backgroundColor: "{colors.accent-soft}"
    textColor: "{colors.primary-ink}"
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
    textColor: "{colors.primary-ink}"
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

# Summer Sunset

An 80s synthwave sunset poster, rebuilt as a working UI kit. A warm sunset-sky gradient
for the ground, **bold 2px aubergine outlines** on every surface, and the three neon
colours doing exactly three jobs: orange sets, cyan cools, magenta bleeds through the ramp.
Ink is deep aubergine — never orange — so the poster stays readable at paragraph length.

## Overview

The reference is a risograph concert poster, not a beach theme. Two things carry it:

1. **Bold graphic lines.** `--border-w: 2px` and every panel, input, button and badged
   chip is outlined in near-ink aubergine `rgba(42,17,54,.26)` — hardened to `.60` for the
   emphatic rule. Nothing is a faint grey hairline; the line work is drawn, not implied.
2. **A gradient sky.** `--bg` is one continuous sunset: peach `#fff5ec` → apricot
   `#ffe3ca` → **magenta band** `#ffd1de` → violet haze `#eedaf5`. It runs warm top to
   bottom, exactly like the poster it is imitating.

All the colour sits in the lines, the buttons and the gradients; the ground and the prose
stay calm. It is a **light** kit on purpose: mode `light`, ink `#2a1136`, and the neon is
the light source, not the page.

Three colours, three jobs:

- **Orange `#ff7a1a`** (`--accent`) — the single action colour. Primary buttons, links in
  the shared lab, the sun disc.
- **Cyan `#06a9c4`** (`--accent-2`) — the cool counterweight. Gradients and media, and the
  deep-cyan `#077184` focus ring. It is the only cold thing on the page and it needs to stay
  rare.
- **Magenta `#ff2ea6`** (`tertiary`, and the `--summer-sunset-magenta` extra) — the third
  brand colour. It lives in the ground's middle band and in the ramp; it is emphasis, never a
  second call to action.

Use it for launch pages, game and music UI, event and ticketing sites, retro-branded
consumer apps, anything that should feel like a poster. Do not use it for dense data
tooling or long-form reading — the gradient ground and the neon lines want to be seen, not
read past.

## Colors

| Role | Token | Value | Contrast |
|---|---|---|---|
| Ground | `--bg` | gradient `#fff5ec` → `#eedaf5` | — |
| Ground (check stop) | — | `#ffd1de` (magenta band) | worst case for dark ink |
| Card | `--surface` | `#fffaf5` | — |
| Body ink | `--text` | `#2a1136` | **12.5:1** on the worst stop |
| Secondary ink | `--text-muted` | `#6d3a5e` | **8.4:1** on `--surface` |
| Tertiary ink | `--text-dim` | `#75506a` | **5.0:1** on the worst stop, 6.0:1 on `--surface-2` |
| On-orange ink | `--text-invert` | `#2a1136` | **6.5:1** on `--accent` |
| Action | `--accent` | `#ff7a1a` | orange |
| Cool accent | `--accent-2` | `#06a9c4` | cyan |
| Third colour | `--summer-sunset-magenta` | `#ff2ea6` | magenta (extra) |
| Focus | `--focus-ring` | `#077184` | deep cyan, 4.2:1 on the worst stop |

**`--bg` is a gradient, checked against its darkest stop.** `#ffd1de` (the magenta band) is
the worst case for dark ink; every other stop scores higher. `--bg-2: #fff0e2` is the solid
stand-in for exports and for tools that cannot parse a gradient token.

**The gradients themselves are not in the `colors:` map above** — that block only accepts
CSS colours. The four ground stops ship as `bg-stop-1..4`, and the sunset ramp ships as
`ramp-peach / ramp-orange / ramp-magenta / ramp-violet`, with the live gradient definitions
in `tokens.css` (`--summer-sunset-ramp`, `--summer-sunset-sun`, `--summer-sunset-sunband`,
`--summer-sunset-grid`).

**Ink is deep aubergine, and `--text-invert` equals `--text`.** White on `#ff7a1a` is about
2.4:1. Deep aubergine on orange is 6.5:1 and reads like screen-print ink on a warm poster,
so the kit uses dark-on-accent rather than light-on-accent. Do not "fix" this by lightening
`--text-invert`.

**Status never borrows the brand hues.** `--ok` is forest green `#1a7d52` (not cyan), `--warn`
is amber-brown `#a86a12` (not the orange action), `--danger` is a true red `#c8353f` (not the
magenta band), `--info` is indigo `#3a6fd8`. A failed state must never be mistakable for the
orange primary.

## Typography

A three-face pairing that is deliberately retro rather than neutral:

- **Audiowide** (display) — the classic wide 80s synth/arcade letterform. It is the poster
  headline: `h1`–`h3`, card titles, the wordmark. It is set at weight 400 (its only weight)
  and is never tracked negative, because the face is already wide.
- **Inter** (body) — everything you actually read. Neutral on purpose, so the retro display
  face is the only thing shouting.
- **Share Tech Mono** (labels) — eyebrows, badges, table headers, timestamps, code. A narrow
  terminal mono with a period voice; it is a different, more analogue mono than the library's
  JetBrains/Mono families, which suits the poster.

Display is essentially untracked (`.01em`); mono labels are wide (`.16em`). Body copy is
never set in Audiowide or Share Tech Mono.

## Layout

The shared 1040px measure, 2.25rem between blocks and a `0.4 / 0.75 / 1 / 2.25rem` spacing
scale. Density is medium — the poster wants air around the sun, so blocks breathe and the
outlines have room to read as a frame.

## Elevation & Depth

Depth is print, not light.

- `--shadow-1` — cards: a soft, warm aubergine drop, wide and low-alpha. It barely reads,
  which is the point: the 2px line is what makes a card a card.
- `--shadow-2` — elevated surfaces: a **hard 4px/4px offset** in 14% aubergine plus a wider
  drop. The hard offset is the risograph "registration" cue.
- `--glow` — the primary button only: a **hard `3px 3px 0` aubergine offset**, like a printed
  drop shadow on a sticker. It is a shadow, not a neon bloom — the kit's glow lives in the
  extras as `--summer-sunset-halo`, a soft orange halo for deliberately lit media.
- `--blur: none` — screen-print, matte, no glass.

## Shapes

Small and printed: `--radius-sm: 4px`, `--radius-md: 6px`, `--radius-lg: 8px`, pills only on
badges, avatars and toggles. `--cut: 0px` — nothing is notched; the bold outline does all the
graphic work. At 12px+ the corners start fighting the line language.

## Components

Every component colour resolves to a `{colors.*}` token; nothing is re-typed.

- **button-primary** — `{colors.primary}` orange fill, `{colors.text-invert}` aubergine
  label, 6px radius, plus the hard `--glow` offset. The one solid orange object on a screen.
- **button-primary-hover** — `{colors.accent-hover}`, a deeper orange, so the button presses
  down into the sunset instead of lifting out of it.
- **button-secondary** — `{colors.surface}` on a `{colors.border-strong}` aubergine line with
  orange type; hover fills with the 16% `{colors.accent-soft}` wash.
- **card** — `{colors.surface}` warm-white on a 2px `{colors.border}` aubergine outline at 8px.
  Elevated cards step to `{colors.surface-2}` and pick up the hard-offset `--shadow-2`.
- **input** — `{colors.surface-2}` warm fill behind a 2px `{colors.border}` line; focus swaps
  to the orange border with a 3px `{colors.accent-soft}` ring, and the keyboard focus ring is
  `{colors.focus-ring}` deep cyan so hover and focus never look alike.
- **badge** — 2px `{colors.border}`, `{colors.text-muted}` mono caps. `badge-accent` is the
  orange tint; `badge-ok` and `badge-danger` use the status greens and reds.

## Do's and Don'ts

**Do**

- Keep the lines bold. `--border-w: 2px` is the kit's whole personality — drop it to 1px and
  the poster becomes a plain light theme.
- Use the full sunset ramp across a page: orange for action, magenta for emphasis bands,
  violet for the cool end and for focus. `--summer-sunset-ramp` carries all four stops.
- Put body copy on `--surface` or the light end of the ground and let the neon live in lines,
  buttons and gradients.
- Keep radii at 8px or below. Round corners fight the print-poster language.

**Don't**

- Don't put white text on `--accent`; use `{colors.text-invert}` and keep the 6.5:1.
- Don't make body copy orange, cyan or magenta. Ever.
- Don't tint the status colours toward the brand — a magenta "error" is invisible next to the
  magenta band.
- Don't add a neon bloom shadow. The warmth is print, not light; `--glow` is a hard offset.
