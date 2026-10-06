---
version: alpha
name: Geometric Dimensions
description: Bauhaus geometry on a paper ground — 3px ink rules, hard square corners, and depth expressed as a hard offset shadow with zero blur.
colors:
  primary: "#2b4bd8"
  primary-hover: "#1f39b3"
  on-primary: "#ffffff"
  secondary: "#e8482f"
  tertiary: "#f2b21a"
  neutral: "#f4f1ea"
  surface: "#fffdf7"
  surface-2: "#f0ebe0"
  text: "#14110f"
  text-muted: "#4e463f"
  text-dim: "#6b625a"
  ok: "#1b6b3a"
  warn: "#8a5300"
  danger: "#b3261e"
  info: "#0f5c8c"

typography:
  display:
    fontFamily: "Archivo"
    fontSize: "2.6rem"
    fontWeight: 900
    lineHeight: 1.02
    letterSpacing: "-0.01em"
  h1:
    fontFamily: "Archivo"
    fontSize: "1.7rem"
    fontWeight: 900
    lineHeight: 1.1
    letterSpacing: "-0.01em"
  h2:
    fontFamily: "Archivo"
    fontSize: "1.3rem"
    fontWeight: 900
    lineHeight: 1.15
  h3:
    fontFamily: "Archivo"
    fontSize: "1.05rem"
    fontWeight: 900
    lineHeight: 1.2
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
    fontWeight: 600
    lineHeight: 1.2
  label:
    fontFamily: "Space Mono"
    fontSize: "0.72rem"
    fontWeight: 700
    letterSpacing: "0.1em"

rounded:
  sm: "0px"
  md: "2px"
  lg: "2px"
  pill: "2px"

spacing:
  xs: "4px"
  sm: "8px"
  md: "16px"
  lg: "28px"
  xl: "44px"

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
    padding: "0.58rem 1rem"
    typography: "{typography.button}"
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
    padding: "0.58rem 1rem"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.md}"
    padding: "0.58rem 1rem"
    typography: "{typography.button}"
  card:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.lg}"
    padding: "1.15rem"
  card-elevated:
    backgroundColor: "{colors.surface-2}"
    rounded: "{rounded.lg}"
    padding: "1.15rem"
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.md}"
    padding: "0.6rem 0.72rem"
    height: "2.5rem"
  input-focus:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.md}"
  badge:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text-muted}"
    rounded: "{rounded.pill}"
    padding: "0.2rem 0.55rem"
    typography: "{typography.label}"
  badge-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.pill}"
    padding: "0.2rem 0.55rem"
    typography: "{typography.label}"
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
  caption:
    textColor: "{colors.text-dim}"
  media-block:
    backgroundColor: "{colors.secondary}"
    rounded: "{rounded.md}"
    height: "96px"
  highlight:
    backgroundColor: "{colors.tertiary}"
    textColor: "{colors.text}"
    rounded: "{rounded.sm}"
    padding: "0.2rem 0.55rem"
  page:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.text}"
---

# Geometric Dimensions

## Overview

A printed Bauhaus sheet. The ground is paper (`{colors.neutral}`), the ink is near-black
(`{colors.text}`), every rule is 3px of that ink, and every corner is square. Nothing glows, nothing
is frosted, nothing floats.

The name is the whole idea: **depth is a hard offset shadow, not a blur.** A card is lifted off the
page by 5px of solid ink to its bottom-right; the elevated card by 9px. There is no blurred shadow
anywhere in the kit — the moment a soft shadow appears, this becomes a generic light theme instead
of a sheet of printed board. That hard offset is what "dimensions" means here, and it is the single
thing to preserve.

## Colors

Three primaries do the graphic work, and the discipline is that **exactly one of them drives
action**:

- **primary — `{colors.primary}` (blue) drives every action.** Buttons, links, the focus ring, the
  active nav chip, the progress bar. It is the only one of the three primaries that clears 4.5:1
  against a white label (6.77:1), so it is the only candidate for a filled control.
- **secondary — `{colors.secondary}` (red) is structural only.** Media fills, chart series, the
  second stop of the media gradient, a single graphic block. It never fills a button: white on red
  measures 3.89:1 and a black label would read as a different, heavier control than the blue one.
- **tertiary — `{colors.tertiary}` (yellow) is graphic only.** The highlight mark, a printed label
  block, a chart series. It is the loudest value in the kit and is therefore used in the smallest
  areas.
- **neutral — `{colors.neutral}`** the paper ground. `{colors.surface}` is card stock (a shade
  lighter than the ground) and `{colors.surface-2}` is the bone tone for nested panels, inputs and
  badge fills.
- **Status colours stay off the primaries.** The brand is red/blue/yellow, so a status colour cannot
  escape those hue families entirely — the escape is *value*, not hue: forest green `{colors.ok}`,
  burnt amber `{colors.warn}`, brick `{colors.danger}` and steel `{colors.info}` are all darkened
  and desaturated so a "failed" badge is never the brand red and a "draft" badge is never the brand
  yellow. Keep them that way; a bright `#ff0000` danger would collide with `{colors.secondary}`.
- **Borders are ink and are not a colour decision.** `#14110f` is the only rule colour in the kit
  (see `--border` in `tokens.css`); the 3px weight, not the hue, is the design statement.

## Typography

**Archivo** at 900 for display — the Archivo Black cut: a heavy geometric grotesque with flat
terminals and a near-monolinear skeleton, which is what a Bauhaus sheet wants in a headline. It is
served at a single weight (900) on purpose: the shared lab asks headings for 600–700, and a
single-weight family pinned at 900 resolves those requests to the true black face with **no
synthetic bold**. **Inter** carries body and interface text; **Space Mono** — a mechanical,
typewriter-derived mono — is labels only, uppercase, at `{typography.label.letterSpacing}`.

Body copy is 0.95rem / 1.6 with generous leading: on a bright paper ground the risk is text
vibrating against the surface, so the kit opens the leading rather than the tracking. Display
tracking is barely tightened (`-0.01em`) — a black face needs almost none.

## Layout

The sheet is the layout unit. Content sits inside ink-ruled blocks on the paper ground, and blocks
are separated by 3px rules and by *visible offsets*: a 28px gutter is preferred over a hairline,
because the hard shadow needs room to land. Everything is left-aligned to a hard edge; nothing is
centred except a genuine empty state.

Keep surfaces flat against each other — this kit has no translucency and no overlays except the
modal scrim (`rgba(20,17,15,.55)`), which is a flat veil rather than a blur.

## Elevation & Depth

Two steps, both hard offsets in solid ink:

1. **`--shadow-1` = `5px 5px 0 var(--border)`** — the default card and the primary button's resting
   shadow.
2. **`--shadow-2` = `9px 9px 0 var(--border)`** — the elevated card.

Both are `spread 0 / blur 0` — literally the box painted again, offset. **No blurred shadow may
appear anywhere in this kit**, and no soft `box-shadow` ring: the input's focus state is an accent
border plus the offset, not a glow. `--blur` is `none` and `templates/lab.css` therefore applies no
`backdrop-filter` — there is nothing frosted here.

The primary button carries a smaller 3px offset through `--glow`, because the shared lab wires
`.btn-primary`'s `box-shadow` to `--glow` rather than to `--shadow-1`; a filled control that sat
perfectly flat against the page would break the rule that everything in this kit is a lifted object.

## Shapes

`{rounded.sm}` 0px, `{rounded.md}` 2px, `{rounded.lg}` 2px, `{rounded.pill}` **2px**, `--cut: 0px`.
Hard corners are the point. The pill token is deliberately 2px rather than 999px: badges and
avatars read as small squares with a hint of print rounding, never as lozenges. Cut corners (the
`--cut` clip-path family) belong to the sibling `carbon` kit, which is dark, square and neon; this
kit is light, printed and dimensional, and uses a hard offset instead of a cut.

## Components

- **button-primary** — `{colors.primary}` fill, `{colors.on-primary}` label, 2px corner, and a 3px
  hard ink offset that reads as the button resting on the sheet. Hover deepens to
  `{colors.primary-hover}` and the offset is unchanged.
- **button-secondary** — card-stock fill with ink text and a 3px ink rule; the same hard offset.
  It must not become a translucent or ghosted button — glass is not in this kit's vocabulary.
- **card** — `{colors.surface}` with a 3px ink border, 2px corner and the 5px hard offset.
- **card-elevated** — `{colors.surface-2}` with the 9px offset; the extra distance *is* the
  elevation, there is no shadow softening to lean on.
- **input** — card-stock fill, 3px ink rim, square-ish corner; the focus state swaps the rim to
  `{colors.primary}` and keeps the offset.
- **badge** — square-ish (2px), mono, uppercase, bone fill; `badge-primary` is the blue-filled
  variant that is allowed because it is an *action* marker, not a status one.
- **media-block** — `{colors.secondary}` (red), the one place the second primary fills area.

## Do's and Don'ts

**Do**

- Keep the offset shadow hard: `Npx Npx 0` of `{colors.text}`. It is the kit's signature.
- Use `{colors.primary}` for anything the user is meant to click or submit. Nothing else.
- Keep rules at 3px. A 1px hairline turns a Bauhaus sheet into a blog.
- Let red and yellow be large *graphic* shapes and small *text* colours — never a filled control.

**Don't**

- Don't introduce a blurred `box-shadow`, a glow, or a `backdrop-filter`. Any of the three breaks
  the kit's identity.
- Don't round a corner. Not a card, not a pill, not an avatar.
- Don't put white text on `{colors.secondary}` (3.89:1) or on `{colors.tertiary}` — the red and the
  yellow take ink-coloured text or no text at all.
- Don't use red or yellow as an action colour; if two of the three primaries start acting, the kit
  reads as decoration rather than hierarchy.
