---
version: alpha
name: Summer Sunset
description: A warm light kit — cream-to-blush sunset-sky ground, deep plum-brown type, and a coral to amber to violet ramp as the signature. Rounded, generous, friendly.
colors:
  primary: "#ff7a59"
  secondary: "#7b4bd8"
  tertiary: "#ffb347"
  neutral: "#fff8f1"
  bg-stop-1: "#fff8f1"
  bg-stop-2: "#ffe8da"
  bg-stop-3: "#ffddcb"
  bg-2: "#fff3e9"
  surface: "#fffdfa"
  surface-2: "#fff2e7"
  overlay: "rgba(43,29,47,0.45)"
  text: "#2b1d2f"
  text-muted: "#7a5a66"
  text-dim: "#806875"
  text-invert: "#2b1d2f"
  accent-hover: "#f9623c"
  accent-soft: "rgba(255,122,89,0.16)"
  ok: "#1f8a5b"
  warn: "#a86a12"
  danger: "#d64545"
  info: "#3f6fd8"
  border: "#f1d8c6"
  border-strong: "#e0b499"
  focus-ring: "#7b4bd8"
  ramp-coral: "#ff7a59"
  ramp-amber: "#ffb347"
  ramp-violet: "#7b4bd8"
typography:
  display:
    fontFamily: "Fraunces"
    fontSize: "2.75rem"
    fontWeight: 600
    lineHeight: 1.06
    letterSpacing: "-0.01em"
  heading:
    fontFamily: "Fraunces"
    fontSize: "1.3rem"
    fontWeight: 600
    lineHeight: 1.22
  body:
    fontFamily: "Inter"
    fontSize: "0.95rem"
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: "IBM Plex Mono"
    fontSize: "0.72rem"
    fontWeight: 500
    letterSpacing: "0.12em"
  code:
    fontFamily: "IBM Plex Mono"
    fontSize: "0.8rem"
    lineHeight: 1.6
rounded:
  sm: "10px"
  md: "14px"
  lg: "18px"
  pill: "999px"
spacing:
  xs: "0.4rem"
  sm: "0.75rem"
  md: "1.15rem"
  lg: "2.25rem"
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.text-invert}"
    borderColor: "{colors.primary}"
    borderRadius: "{rounded.md}"
    padding: "0.58rem 1rem"
    fontSize: "0.875rem"
    fontWeight: 600
  button-primary-hover:
    backgroundColor: "{colors.accent-hover}"
    textColor: "{colors.text-invert}"
    borderColor: "{colors.accent-hover}"
    borderRadius: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    borderColor: "{colors.border-strong}"
    borderRadius: "{rounded.md}"
    padding: "0.58rem 1rem"
    fontSize: "0.875rem"
  button-secondary-hover:
    backgroundColor: "{colors.accent-soft}"
    textColor: "{colors.accent-hover}"
    borderColor: "{colors.primary}"
    borderRadius: "{rounded.md}"
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    borderColor: "{colors.border}"
    borderRadius: "{rounded.lg}"
    padding: "1.35rem"
  card-elevated:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    borderColor: "{colors.border}"
    borderRadius: "{rounded.lg}"
    padding: "1.35rem"
  input:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text}"
    borderColor: "{colors.border}"
    borderRadius: "{rounded.md}"
    padding: "0.6rem 0.8rem"
    fontSize: "0.875rem"
  input-focus:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    borderColor: "{colors.primary}"
    borderRadius: "{rounded.md}"
  badge:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text-muted}"
    borderColor: "{colors.border}"
    borderRadius: "{rounded.pill}"
    padding: "0.2rem 0.6rem"
    fontFamily: "IBM Plex Mono"
    fontSize: "0.72rem"
    letterSpacing: "0.04em"
  badge-accent:
    backgroundColor: "{colors.accent-soft}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    borderRadius: "{rounded.pill}"
    fontSize: "0.72rem"
  badge-ok:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.ok}"
    borderColor: "{colors.ok}"
    borderRadius: "{rounded.pill}"
    fontSize: "0.72rem"
---

# Summer Sunset

The only warm light kit in the library. The ground is a cream-to-blush sunset-sky gradient,
the type is deep plum-brown (never orange), and the signature is a coral → amber → violet
ramp. Corners are 10–18px, padding is generous, and the display face is a soft serif.

## Overview

Most "warm" light themes make one mistake: they let the accent leak into the body copy and
the page turns orange, which is unreadable by paragraph three. This kit does the opposite.
The ground and the type are the *calm* end of a sunset — cream `#fff8f1` fading to blush
`#ffddcb`, with plum-brown text at 12.5:1 — and all of the heat lives in the coral action
colour, the `--accent-2` violet, and the media gradients.

Use it for landing pages, event and ticketing sites, consumer apps, food and travel
branding, onboarding, and anywhere a warm hello matters more than a serious tone. Avoid it
for dense data tooling and for anything that needs a cool, clinical voice — the warmth is
load-bearing, not decoration.

## Colors

| Role | Token | Value | Contrast |
|---|---|---|---|
| Ground | `--bg` | gradient, `#fff8f1` → `#ffddcb` | — |
| Ground (check stop) | — | `#ffddcb` | worst case for dark type |
| Card | `--surface` | `#fffdfa` | — |
| Body text | `--text` | `#2b1d2f` | **12.5:1** on `#ffddcb`, 15.1:1 on `#fff8f1` |
| Secondary text | `--text-muted` | `#7a5a66` | **5.9:1** on `--surface`, 4.7:1 on `#ffddcb` |
| Tertiary text | `--text-dim` | `#806875` | 3.6:1 on `--surface` |
| On-coral text | `--text-invert` | `#2b1d2f` | **6.2:1** on `--accent` |
| Action | `--accent` | `#ff7a59` | — |
| Cool accent | `--accent-2` | `#7b4bd8` | — |
| Ramp middle | `--summer-sunset-amber` | `#ffb347` | extra, off-contract |

**`--bg` is a gradient, and that is deliberate.** It is checked against its darkest stop,
`#ffddcb`, which is the worst case for dark type on light; every other stop scores higher.
`--bg-2` (`#fff3e9`) is a solid stand-in for exports and for tools that cannot read a
gradient token. Consequences of a gradient `--bg` are noted in the README.

**`--text-invert` is the same plum as `--text`.** White on coral is only ~2.6:1. Deep plum on
coral is 6.2:1 and looks like ink on a sunset postcard, so the kit uses dark-on-accent rather
than light-on-accent. This is the single most important decision in the palette.

**Body copy never goes orange.** Coral is for actions, links, tints and gradients. If a
paragraph is orange, the kit is being misused.

## Typography

- **Fraunces** (display) — a warm, slightly quirky serif for `h1`–`h3` and card titles. A
  serif, not a rounded sans, because it gives the kit editorial warmth instead of nursery
  softness, and it holds up on a gradient ground.
- **Inter** (body) — neutral and quiet so the serif can carry the personality.
- **IBM Plex Mono** (labels) — eyebrows, badges, table headers. Lighter and more humanist
  than JetBrains Mono, which suits the warmth.

Display is tight (`-0.01em`), labels are modestly tracked (`.12em`). No all-caps body copy.

## Layout

A 1040px measure with generous breathing room: 2.25rem between blocks, 1.35rem card padding,
1rem grid gaps, and a `0.4 / 0.75 / 1.15 / 2.25rem` spacing scale. Where the cyberpunk kit
tightens to look like a HUD, this one opens up to look like a good morning.

## Elevation & Depth

Shadows are warm and wide, never hard.

- `--shadow-1` — cards: a 28% brown drop, tinted to `#7a3f20` rather than pure black, so it
  reads as a late-afternoon shadow instead of a grey smudge.
- `--shadow-2` — elevated cards and popovers: a 42% brown drop plus a 1px inner white
  highlight, which is what makes a raised card feel like paper on paper.
- `--glow` — a 4px `rgba(255,122,89,.22)` ring on the primary button. A friendly halo, not a
  neon bloom; it should never be mistaken for the cyberpunk kit's.
- `--blur: none` — matte paper throughout.

## Shapes

Round. `--radius-sm: 10px`, `--radius-md: 14px`, `--radius-lg: 18px`, `--radius-pill: 999px`
for badges, avatars and toggles. `--cut: 0px` — this kit never notches a corner.

## Components

- **button-primary** — `{colors.primary}` coral fill, `{colors.text-invert}` plum type,
  14px radius, plus the soft `--glow` ring. Warm and tactile.
- **button-primary-hover** — `{colors.accent-hover}`, a deeper coral, so the button presses
  *into* the sunset rather than lifting out of it.
- **button-secondary** — `{colors.surface}` on a `{colors.border-strong}` sand border with
  coral type; hover fills with the 16% coral tint.
- **card** — `{colors.surface}` white-warm on a `{colors.border}` sand hairline at 18px, with
  a generously padded 1.35rem body. Elevated cards lean on `--shadow-2` rather than a colour
  step, because stepping up a warm ground too far turns it orange.
- **input** — `{colors.surface-2}` warm fill, sand hairline; focus swaps to a
  `{colors.primary}` border with a 3px `{colors.accent-soft}` ring, and the keyboard focus
  ring is `{colors.focus-ring}` violet, pulling the cool end of the ramp in.
- **badge** — sand hairline, `{colors.text-muted}` mono caps. `badge-accent` is the coral
  tint; status badges stay on the darker status hues so they remain legible on warm white.

## Do's and Don'ts

**Do**

- Keep the heat in accents, gradients and media. Ground and text stay calm.
- Use the full ramp across a page — coral for action, amber for the middle beat, violet for
  cool contrast and focus. `--summer-sunset-ramp` carries all three as one gradient.
- Let cards be white-warm (`{colors.surface}`) with sand hairlines; that is what separates
  this from a plain beige theme.
- Keep radii at 10px or above. Sharp corners fight the whole premise.

**Don't**

- Don't put white text on `--accent`; use `{colors.text-invert}` and keep the 6.2:1.
- Don't set body copy in coral, amber or violet. Ever.
- Don't use a pure-black shadow — a black drop on warm cream looks like dirt. The shadows are
  brown on purpose.
- Don't reach for this kit when the content is dense or clinical; that is what the cool kits
  are for.
