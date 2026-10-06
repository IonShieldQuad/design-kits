---
version: alpha
name: Cyberpunk
description: Neon on near-black. Hot magenta drives every action, electric cyan and acid yellow carry gradients and hazards, and magenta hairlines make the grid itself glow.
colors:
  primary: "#ff2e88"
  secondary: "#22e0ff"
  tertiary: "#e8ff2e"
  neutral: "#08070d"
  bg: "#08070d"
  bg-2: "#0d0a14"
  surface: "#12101c"
  surface-2: "#1a1626"
  overlay: "rgba(4,3,9,0.74)"
  text: "#f3f0ff"
  text-muted: "#aaa2c8"
  text-dim: "#857e9f"
  text-invert: "#0b0713"
  accent-hover: "#ff5aa0"
  accent-soft: "rgba(255,46,136,0.14)"
  ok: "#2fe6a0"
  warn: "#ff9f1c"
  danger: "#ff3b30"
  info: "#7d8cff"
  border: "rgba(255,46,136,0.30)"
  border-strong: "rgba(255,46,136,0.62)"
  focus-ring: "#22e0ff"
  glow: "rgba(255,46,136,0.60)"
typography:
  display:
    fontFamily: "Oxanium"
    fontSize: "2.75rem"
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: "-0.01em"
  heading:
    fontFamily: "Oxanium"
    fontSize: "1.3rem"
    fontWeight: 650
    lineHeight: 1.2
  body:
    fontFamily: "Inter"
    fontSize: "0.95rem"
    fontWeight: 400
    lineHeight: 1.55
  label:
    fontFamily: "JetBrains Mono"
    fontSize: "0.72rem"
    fontWeight: 600
    letterSpacing: "0.18em"
  code:
    fontFamily: "JetBrains Mono"
    fontSize: "0.8rem"
    lineHeight: 1.6
rounded:
  sm: "3px"
  md: "4px"
  lg: "6px"
  pill: "999px"
spacing:
  xs: "0.35rem"
  sm: "0.6rem"
  md: "1rem"
  lg: "1.75rem"
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.text-invert}"
    borderColor: "{colors.primary}"
    borderRadius: "{rounded.md}"
    padding: "0.58rem 1rem"
    fontSize: "0.875rem"
    fontWeight: 550
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
    padding: "1.15rem"
  card-elevated:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text}"
    borderColor: "{colors.border-strong}"
    borderRadius: "{rounded.lg}"
    padding: "1.15rem"
  input:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text}"
    borderColor: "{colors.border}"
    borderRadius: "{rounded.md}"
    padding: "0.6rem 0.72rem"
    fontSize: "0.875rem"
  input-focus:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text}"
    borderColor: "{colors.primary}"
    borderRadius: "{rounded.md}"
  badge:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text-muted}"
    borderColor: "{colors.border}"
    borderRadius: "{rounded.pill}"
    padding: "0.2rem 0.55rem"
    fontFamily: "JetBrains Mono"
    fontSize: "0.72rem"
    letterSpacing: "0.04em"
  badge-accent:
    backgroundColor: "{colors.accent-soft}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    borderRadius: "{rounded.pill}"
    fontSize: "0.72rem"
  badge-danger:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.danger}"
    borderColor: "{colors.danger}"
    borderRadius: "{rounded.pill}"
    fontSize: "0.72rem"
---

# Cyberpunk

Neon on near-black, built to be loud without becoming unusable. One action colour — hot
magenta — plus two secondaries (electric cyan for gradients and media, acid yellow for
hazard marks). Magenta hairlines stand in for the usual grey ones, corners are 3–6px, and
the primary button carries a bloom shadow. Mono-forward labels give the kit its terminal
voice.

## Overview

This is the loud end of the library. A near-black ground with a violet cast (`#08070d`),
saturated neon on top, and no neutral greys anywhere in the line work: `--border` is
30% magenta and `--border-strong` is 62% magenta, so panels read as a lit grid.

It is meant for the top of a page — game and music UI, launch screens, posters that happen
to be web pages — and for dashboards that should feel like a cockpit rather than a settings
panel. Two rules keep it usable:

1. **Neon is for brand surfaces, never for body copy.** Body text is `#f3f0ff`, muted text
   is a desaturated lilac (`#aaa2c8`). Nothing long-form is ever magenta.
2. **Status colours never borrow the brand hues.** `--ok` is mint, `--warn` is orange-amber,
   `--danger` is true red, `--info` is indigo. See the note under Colors.

Use it when the interface should feel like a neon sign. Do not use it for long-form reading,
medical or financial data entry, or anywhere a magenta error state could be mistaken for a
magenta call-to-action.

## Colors

Five families, each with one job.

| Role | Token | Value | Contrast |
|---|---|---|---|
| Ground | `--bg` | `#08070d` | — |
| Raised ground | `--bg-2` / `--surface` | `#0d0a14` / `#12101c` | — |
| Body text | `--text` | `#f3f0ff` | **17.9:1** on `--bg` |
| Secondary text | `--text-muted` | `#aaa2c8` | **7.8:1** on `--surface` |
| Tertiary text | `--text-dim` | `#857e9f` | 4.6:1 on `--bg` |
| On-neon text | `--text-invert` | `#0b0713` | **5.7:1** on `--accent` |
| Action | `--accent` | `#ff2e88` | — |
| Second accent | `--accent-2` | `#22e0ff` | — |
| Acid | `--cyberpunk-acid` | `#e8ff2e` | extra, off-contract |

**Why `--text-invert` is dark.** White on hot magenta is only ~3.5:1, well under AA. Rather
than abandon the hue, the kit keeps `#ff2e88` and puts near-black type on it — 5.7:1, and it
reads like black ink on a neon sign. Do not "fix" this by lightening `--text-invert`.

**Why the status colours look off-brand.** Magenta (`#ff2e88`), cyan (`#22e0ff`) and acid
yellow (`#e8ff2e`) are all high-chroma and adjacent to the obvious status hues. So status
steps *away* from them: `--ok` `#2fe6a0` is mint not cyan, `--danger` `#ff3b30` is a true red
not a pink, `--warn` `#ff9f1c` is orange-amber not acid yellow, `--info` `#7d8cff` is indigo
not cyan. A failed state must never be mistakable for the brand.

## Typography

Two families and a mono, each with a narrow job:

- **Oxanium** (display) for `h1`–`h3`, card titles and the wordmark. A squarish techno face
  that reads at 2.75rem without looking like a sci-fi costume.
- **Inter** (body) for everything you actually read. Neutral on purpose — it is the calmer
  in the pairing.
- **JetBrains Mono** (labels) for eyebrows, badges, table headers, timestamps and code.
  Labels are uppercase at `.18em` tracking; this is where the terminal voice lives.

Display type is tight (`-0.01em`); mono labels are wide (`.18em`). Never set body copy in
Oxanium or JetBrains Mono — the display and mono faces are signposts, not prose.

## Layout

A single 1040px measure, 2.25rem between blocks, 1rem grid gap. The rhythm is deliberately
tight and even: this kit wants to look like a HUD, so block spacing does not breathe much.
Spacing scale: `0.35 / 0.6 / 1 / 1.75rem`.

## Elevation & Depth

Depth is light, not shadow — bloom and hairlines.

- `--shadow-1` — cards. A near-black drop with no spread; it barely reads on a near-black
  ground, which is deliberate.
- `--shadow-2` — elevated surfaces. Adds a 14% magenta ring and a wide cyan bloom.
- `--glow` — the primary button only: a 1px magenta ring plus two magenta shadows at
  decreasing alpha. This is the one place the kit is allowed to look lit from within.
- `--blur: none` — hard edges. No frosted glass, no softness.

## Shapes

Hard. `--radius-sm: 3px`, `--radius-md: 4px`, `--radius-lg: 6px`; pills only on badges and
avatars. `--cut: 10px` is exported for consumers who want a `clip-path` corner notch — the
shared lab draws the small radii instead, so a kit dropped into a real project gets either
the hard 3–6px corner or the 10px cut, never both on one box.

## Components

All component colour decisions resolve to `{colors.*}` tokens; nothing is re-typed.

- **button-primary** — `{colors.primary}` fill, `{colors.text-invert}` type, no border,
  plus `--glow`. The only lit element on a default screen.
- **button-primary-hover** — `{colors.accent-hover}`, a lighter magenta so hover reads as
  *brighter*, not darker — the neon metaphor, inverted from typical dark themes.
- **button-secondary** — `{colors.surface}` fill, `{colors.primary}` type, a 50% magenta
  border. Flat until hover, when it takes a 14% magenta wash.
- **card** — `{colors.surface}` on `{colors.border}`, 6px radius, `--shadow-1`. Elevated
  cards step up to `{colors.surface-2}` and pick up the bloom.
- **input** — `{colors.surface-2}` fill, `{colors.border}` hairline; focus swaps the border
  to `{colors.primary}` and lays a 3px `{colors.accent-soft}` ring, while the *keyboard*
  focus ring is `{colors.focus-ring}` cyan so hover and focus never look alike.
- **badge** — `{colors.surface-2}` on `{colors.border}`, uppercase mono at `.04em`.
  `badge-accent` uses the action tint; status badges use the status colours above.

## Do's and Don'ts

**Do**

- Reserve magenta for one thing per screen. If two elements are magenta, one of them is wrong.
- Put body copy on `--bg` or `--surface` and let the neon live in borders, glows and badges.
- Keep the cyan focus ring. It is the only signal that separates keyboard focus from hover.
- Keep radii at 3–6px. At 12px+ the kit stops reading as a cyberpunk skin.

**Don't**

- Don't put white text on `--accent`; use `--text-invert` (`#0b0713`) and keep the 5.7:1.
- Don't tint status colours toward the brand hues — a pink "error" is invisible next to a
  pink button.
- Don't use `--glow` on more than the primary action; bloom everywhere is bloom nowhere.
- Don't apply `--blur`; this kit has no glass.
