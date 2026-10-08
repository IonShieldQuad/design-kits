---
version: alpha
name: Chrome
description: Liquid chrome on black — a metallic four-stop ramp as the finish, magenta as the action, cyan as the cool tertiary, over hard 2px line work.
colors:
  primary: "#ff2e88"
  accent-ink: "#ff4796"
  secondary: "#c9d0da"
  tertiary: "#35e3ff"
  neutral: "#08090d"
  bg: "#08090d"
  bg-2: "#0e1118"
  surface: "#101319"
  surface-2: "#171b23"
  overlay: "rgba(3,4,7,0.78)"
  text: "#eef1f6"
  text-muted: "#a7b0bf"
  text-dim: "#8b94a4"
  text-invert: "#0b0d12"
  accent-hover: "#ff5aa3"
  accent-soft: "rgba(255,46,136,0.15)"
  ok: "#2fe6a0"
  warn: "#ffb347"
  danger: "#ff4d4d"
  info: "#35e3ff"
  border: "rgba(201,208,218,0.20)"
  border-strong: "rgba(201,208,218,0.46)"
  focus-ring: "#35e3ff"
  chrome-1: "#ffffff"
  chrome-2: "#c9d0da"
  chrome-3: "#7c8695"
  chrome-4: "#2b3038"
typography:
  display:
    fontFamily: "Orbitron"
    fontSize: "2.75rem"
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: "0.02em"
  heading:
    fontFamily: "Orbitron"
    fontSize: "1.3rem"
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: "0.02em"
  body:
    fontFamily: "Inter"
    fontSize: "0.95rem"
    fontWeight: 400
    lineHeight: 1.55
  label:
    fontFamily: "JetBrains Mono"
    fontSize: "0.72rem"
    fontWeight: 600
    letterSpacing: "0.20em"
  code:
    fontFamily: "JetBrains Mono"
    fontSize: "0.8rem"
    lineHeight: 1.6
rounded:
  sm: "2px"
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
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: "0.58rem 1rem"
  button-primary-hover:
    backgroundColor: "{colors.accent-hover}"
    textColor: "{colors.text-invert}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.secondary}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: "0.58rem 1rem"
  button-secondary-hover:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text}"
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
    backgroundColor: "{colors.surface-2}"
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
    textColor: "{colors.primary}"
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

# Chrome

Liquid chrome on black. Where the rest of the dark kits pick a single neon and glow, this one
is **metal**: a four-stop chrome ramp — specular white `#ffffff` → bright silver `#c9d0da` →
mid steel `#7c8695` → dark steel `#2b3038` — running across headings, rims and media. Magenta
`#ff2e88` is the action colour, cyan `#35e3ff` is the cool tertiary, and every surface is
outlined in hard 2px steel.

It is the **dark sibling of Summer Sunset**: same colour family (magenta + cyan over a
bold-line language, 2px lines, small radii), opposite ground — the light kit is a printed
poster, this one is polished metal in the dark.

## Overview

Two ideas carry the kit.

1. **A real metallic ramp, not a glow.** `--chrome-1..4` are exposed as extras and composed
   into `--chrome-gradient` (a 135° sweep that travels white → silver → steel → dark steel and
   back), `--chrome-sheen` (a 180° white-to-transparent top highlight for raised surfaces) and
   `--accent-2`, which is set to the bright-silver stop `#c9d0da`. Because the shared lab
   paints media, progress bars and avatars with `linear-gradient(--accent, --accent-2)`, that
   single choice turns every lab gradient into **magenta → chrome**, which is the whole
   signature in one line of CSS.
2. **Hard chrome line work.** `--border-w: 2px` and every panel/input/badge is outlined in
   20% silver (`--border`), hardened to 46% for the metal rim (`--border-strong`). Radii are
   2–6px — machined, not rounded.

Use it for developer tools, hardware and audio product pages, music and game UI, portfolios,
and dashboards that should feel like a machined panel. Do not use it for long-form reading or
anywhere a magenta error state could be confused with a magenta action — the kit keeps its
status colours deliberately off-brand to prevent exactly that.

## Colors

| Role | Token | Value | Contrast |
|---|---|---|---|
| Ground | `--bg` | `#08090d` | — |
| Raised ground | `--surface` / `--surface-2` | `#101319` / `#171b23` | — |
| Body text | `--text` | `#eef1f6` | **17.6:1** on `--bg` |
| Secondary text | `--text-muted` | `#a7b0bf` | **8.5:1** on `--surface` |
| Tertiary text | `--text-dim` | `#8b94a4` | **5.6:1** on `--surface-2`, 6.5:1 on `--bg` |
| On-magenta text | `--text-invert` | `#0b0d12` | **5.6:1** on `--accent` |
| Action | `--accent` | `#ff2e88` | magenta |
| Chrome / second accent | `--accent-2` | `#c9d0da` | bright silver |
| Tertiary | `--tertiary` | `#35e3ff` | cyan |
| Specular | `--chrome-1` | `#ffffff` | extra |
| Dark steel | `--chrome-4` | `#2b3038` | extra |

**The chrome ramp is a set of colours plus a gradient the DESIGN.md `colors:` block cannot
hold.** The four stops ship as `chrome-1..4`; the composed gradients (`--chrome-gradient`,
`--chrome-sheen`) live in `tokens.css` as extras and are meant to be applied to headings,
rails and raised surfaces with a `background` + `background-clip: text` or a `border-image`.

**Why `--accent-2` is silver, not cyan.** The brief calls for cyan as the second brand hue, but
`--accent-2` is the single token the shared lab feeds into its media, bar and avatar gradients.
Setting it to chrome silver is what makes those gradients read as **liquid chrome** and, just
as importantly, it keeps the kit from looking like the `cyberpunk` skin (which pairs the same
magenta with a cyan second accent). Cyan keeps a real job here — `--focus-ring`, `--info` and
the `--chrome-cyan` extra — without duplicating the neighbouring kit's signature.

**Why `--text-invert` is dark.** White on `#ff2e88` is only about 3.5:1. The kit keeps the
magenta and puts near-black type on it — **5.6:1**, like ink on a hot-pink enamel badge. Do not
"fix" this by lightening `--text-invert`.

**Status stays off-brand.** Magenta and cyan are both high-chroma and adjacent to obvious
status hues, so `--ok` is mint `#2fe6a0` (not cyan), `--warn` is amber `#ffb347` (not magenta),
`--danger` is a true red `#ff4d4d` (not a pink). The one deliberate overlap is `--info`, which
borrows the tertiary cyan: informational, never an action.

## Typography

Three faces, three jobs:

- **Orbitron** (display) — a wide geometric retro-future face. It is the chrome wordmark:
  `h1`–`h3`, card titles. Tracked out (`.02em`), never tracked in — the width is the point, and
  it is what makes a heading look machined.
- **Inter** (body) — everything you actually read. Neutral, so the display metal is the only
  loud thing on the page.
- **JetBrains Mono** (labels) — eyebrows, badges, table headers, timestamps, code. Uppercase at
  `.20em`; this is the instrument-panel voice and the widest tracking in the library's dark
  kits.

Display and mono are signposts, not prose — body copy is never Orbitron or JetBrains Mono.

## Layout

The shared 1040px measure, 1.75rem between blocks, 1rem grid gaps and a `0.35 / 0.6 / 1 /
1.75rem` scale. The rhythm is tight and even: chrome wants to look like a control panel, so
blocks do not breathe much and the 2px rules do the separating.

## Elevation & Depth

Depth is **rim-light**, not bloom.

- `--shadow-1` — cards: a near-black drop with a 1px inner white top-highlight. On a
  near-black ground the drop barely reads; the highlight is what makes a card feel like a
  polished plate.
- `--shadow-2` — elevated surfaces: a deeper drop plus a 1px silver ring, so a raised card
  picks up a chrome outline rather than a glow.
- `--glow` — the primary button only: a 1px magenta ring, a 1px inner **white specular
  highlight** and a tight magenta emanation. This is the rim-light: the button looks like
  polished metal catching a magenta light.
- `--blur: none` — hard metal, no frosted glass.

For the full liquid-chrome finish, apply `--chrome-gradient` to headings via
`background: var(--chrome-gradient); -webkit-background-clip: text; color: transparent;`
and lay `--chrome-sheen` over raised plates. The shared lab draws none of this for you; it is
documented so a project can.

## Shapes

Sharp and machined: `--radius-sm: 2px`, `--radius-md: 4px`, `--radius-lg: 6px`; pills only on
badges, avatars and toggles. `--cut: 0px` — nothing is notched; hard radii plus the 2px steel
rim are the entire shape language. Above 8px the corners stop reading as metal.

## Components

Every component colour resolves to a `{colors.*}` token; nothing is re-typed.

- **button-primary** — `{colors.primary}` magenta fill, `{colors.text-invert}` near-black
  label, 4px radius, plus the rim-light `--glow`. The only lit object on a screen.
- **button-primary-hover** — `{colors.accent-hover}`, a *lighter* magenta, so hover reads as
  brighter, like a metal surface catching more light.
- **button-secondary** — `{colors.surface}` plate, `{colors.secondary}` chrome-silver label and
  a 2px `{colors.border-strong}` steel rim. The "polished metal" button; hover steps up to
  `{colors.surface-2}` with `{colors.text}`.
- **card** — `{colors.surface}` on a 2px `{colors.border}` steel line at 6px, `--shadow-1`.
  Elevated cards step to `{colors.surface-2}` and pick up the chrome ring of `--shadow-2`.
- **input** — `{colors.surface-2}` fill behind a 2px `{colors.border}` rim; focus swaps the
  rim to `{colors.primary}` with a 3px `{colors.accent-soft}` ring, while the *keyboard* focus
  ring is `{colors.focus-ring}` cyan so hover and focus never look alike.
- **badge** — 2px `{colors.border}`, `{colors.text-muted}` mono caps at `.20em`. `badge-accent`
  is the magenta tint; `badge-ok` and `badge-danger` use the status mint and red.

## Do's and Don'ts

**Do**

- Reach for the chrome ramp for *finish*, and magenta for *action*. Metal is the surface; pink
  is the signal.
- Keep the 2px steel line work everywhere. It is what separates this from a plain dark theme.
- Keep radii at 2–6px. Chrome is machined; round corners soften it into something else.
- Put body copy on `--bg` or `--surface` in Inter. Let the metal and the magenta live in
  headings, rims and buttons.

**Don't**

- Don't put white text on `--accent`; use `{colors.text-invert}` and keep the 5.6:1.
- Don't set `--accent-2` back to cyan — that collapses the kit into the `cyberpunk` skin and
  loses the magenta → chrome gradients.
- Don't tint status colours toward the brand; a pink "error" disappears next to a pink button.
- Don't use `--glow` on more than the primary action, and don't apply `--blur` — this kit has
  no glass.
