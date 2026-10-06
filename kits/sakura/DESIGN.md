---
version: alpha
name: Sakura
description: A spring day — saturated blossom pink against fresh leaf green on a light tinted ground, with deep plum ink and a hint of bounce.
colors:
  primary: "#c8325f"
  primary-hover: "#b02651"
  secondary: "#2e8339"
  tertiary: "#a81d4c"
  neutral: "#f9eef3"
  bg-stop-sky: "#f1f6fb"
  bg-stop-petal: "#fdf1f6"
  bg-stop-leaf: "#f3f8ee"
  bg-stop-warm: "#fdf3f6"
  bg-stop-end: "#f9eef3"
  bg-2: "#fdf3f7"
  surface: "#fffbfd"
  surface-2: "#f8eef3"
  overlay: "rgba(58,36,56,0.38)"
  text: "#3a2438"
  text-muted: "#5e4557"
  text-dim: "#6d5165"
  text-invert: "#ffffff"
  accent-soft: "rgba(200,50,95,0.10)"
  accent-ink: "#a81d4c"
  accent-ink-hover: "#8d1540"
  ok: "#177040"
  warn: "#8f5c00"
  danger: "#b3261e"
  info: "#2b6aa8"
  border: "#ecd6e0"
  border-strong: "#d9b9c8"
  focus-ring: "#2f8340"
typography:
  display:
    fontFamily: "Zen Kaku Gothic New"
    fontSize: "2.9rem"
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: "-0.01em"
  heading:
    fontFamily: "Zen Kaku Gothic New"
    fontSize: "1.3rem"
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: "-0.006em"
  body:
    fontFamily: "Karla"
    fontSize: "0.95rem"
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: "IBM Plex Mono"
    fontSize: "0.72rem"
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: "0.12em"
rounded:
  sm: "10px"
  md: "14px"
  lg: "20px"
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
    textColor: "{colors.accent-ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: "0.58rem 1rem"
  button-secondary-hover:
    backgroundColor: "{colors.accent-soft}"
    textColor: "{colors.accent-ink-hover}"
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
    textColor: "{colors.accent-ink}"
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
    textColor: "{colors.accent-ink}"
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
    textColor: "{colors.accent-ink}"
---

## Overview

**Not a quiet petal-drift — a spring day.** Sakura is the season rendered as an interface:
blossom pink against fresh leaf green, light and cheerful, with **more colour than pastel**.
Two colours carry the whole kit, and both are held at visible saturation. The failure mode
this kit is built to avoid has two directions, and it avoids both:

- Go **too pale** and it dissolves into generic pastel — a soft wash of near-white with a
  faint tint. That is what the library's `glass` kit already is, and Sakura is deliberately
  not it.
- Add **too much pink** and it becomes a nursery: one sugary hue repeated until the page
  reads as a baby-shower invitation.

The escape from both is the same move: **pink against living green**. Pink alone is a cliché;
pink beside a fresh leaf is the season. Green is therefore not a swatch colour — it is a
working counterweight that appears in real UI (the focus ring, the media/avatar/progress
gradients, the light half of the spring ramp, the scatter, and every status that means "go").
The two hues are married in one ramp: blossom → **cream** → leaf. The cream midpoint is what
makes them read as a single gradient rather than as two accents that happen to meet.

Three decisions follow from that, and each is load-bearing:

1. **Pink drives action.** Sakura *is* the blossom, so the one saturated object on a screen
   is the blossom: the primary button, the toggle, the checkbox, the tint behind active nav.
   Pink as a **fill** is the identity; a kit whose primary action is green would be a
   different season wearing this name.
2. **The ink is deep plum, never pink.** Pink body text on a pink ground is the second
   failure mode, so the reading ink is a warm plum-black (`#3a2438`). And because a pink
   that works as a button *fill* is far too light to read as a small *label*, text-pink
   ships separately as `--accent-ink`, a much deeper rose.
3. **The ground is a real gradient, not white.** A clean light base with a faint warm–cool
   shift — cool sky at the top of the first screen, warm petal below it, a leaf tint lower
   down — so the page is tinted like a room with a window open, never sterile white and
   never grey (grey is `zen-garden`, and grey is a wet day).

Depth is airy but explicitly **not glassy**: soft layered shadows and no frosted
translucency at all (`--blur: none`). Frost is `glass`'s material; here depth is a lift, not
a pane.

One sentence: *blossom pink and fresh leaf green on a light tinted spring ground.*

## Colors

Two hues, one ink, one light ground. Both hues are **saturated**, and the way they stay
legible is by deepening the ink — never by lightening the ground.

| Role | Token | Value | Contrast |
|---|---|---|---|
| Ground (gradient) | `--bg` | sky→petal→leaf stops | proved on the darkest stop |
| Ground, cool stop | `bg-stop-sky` | `#f1f6fb` | — |
| Ground, petal stop | `bg-stop-petal` | `#fdf1f6` | — |
| Ground, leaf stop | `bg-stop-leaf` | `#f3f8ee` | — |
| Ground, mid stop | `bg-stop-warm` | `#fdf3f6` | — |
| Ground, darkest stop | `bg-stop-end` | `#f9eef3` | the value all maths used |
| Ground lift / export stand-in | `--bg-2` | `#fdf3f7` | — |
| Card | `--surface` | `#fffbfd` | — |
| Nested panel / input | `--surface-2` | `#f8eef3` | — |
| Body ink (plum) | `--text` | `#3a2438` | **12.5:1** on the darkest ground |
| Secondary ink | `--text-muted` | `#5e4557` | **8.3:1** on `--surface` |
| Tertiary ink | `--text-dim` | `#6d5165` | **6.2:1** on the darkest ground, **6.8:1** on `--surface` |
| Ink on the action | `--text-invert` | `#ffffff` | **5.2:1** on `--accent` |
| Action (blossom pink) | `--accent` | `#c8325f` | **5.2:1** as a fill with white type |
| Pink **as text** | `--accent-ink` | `#a81d4c` | **6.3:1** on the darkest ground |
| Counterweight (leaf green) | `--accent-2` | `#2e8339` | fill only; white on it **4.7:1** |
| Blossom tint | `--accent-soft` | `rgba(200,50,95,.10)` | deep rose on it **5.5:1** |
| Focus | `--focus-ring` | `#2f8340` | fresh green, never the pink action |
| Hairline | `--border` | `#ecd6e0` | — |
| Emphasised line | `--border-strong` | `#d9b9c8` | — |

**Primary (`#c8325f`) is the blossom, and it is the action colour.** A pink that has to
carry white type cannot be a pastel — `#c8325f` is saturated but *deep*, which is exactly the
register the brief asked for ("more colour than pastel"): it has the chroma of a blossom and
the weight of a pressed petal. Lighten it and the button fails; the answer is never to
lighten the ground.

**Secondary (`#2e8339`) is the fresh leaf, and it is the differentiation.** Pink alone is
the cliché; the green is what makes the page a spring day rather than a nursery. It is
deliberately **chromatic**, not the desaturated moss `zen-garden` uses — a living leaf next
to a blossom, not a grey sage next to rain. It appears in the focus ring, the media plate,
the avatar and the progress bar (all as the second stop of a pink→green wash), and in the
light half of `--sakura-ramp`. It is a fill and a motif colour; body text is plum, and
green-as-text is never asked to carry a paragraph.

**Tertiary (`#a81d4c`) is pink-as-text, not a third hue.** The schema wants a `tertiary`,
and this kit's honest answer is that it has two hues by design. Its `tertiary` is
`--accent-ink`: the deep rose that links, eyebrows, active nav and secondary-button labels
actually use. It exists because **the fill pink measures only 2.7:1 as a small label on the
ground** — a real failure, and the reason `--accent-ink` is a declared capability rather
than a nice-to-have.

**Neutral (`#f9eef3`) is the darkest stop of the spring ground.** It is the value chosen for
every contrast calculation, so the numbers above hold at the *worst* point a viewer can
scroll to, not at the flattering light one. Warm it further and it stops being a spring
ground; cool it and it becomes `zen-garden`'s overcast.

**The ground is a gradient, and its stops live in `colors:` as colours.** A gradient is not
a colour and the linter errors on one, so the five stops ship as `bg-stop-*` and the live
gradient is `--bg` in `tokens.css`. The stops are in **px**, not percent: the body's
gradient box is the whole document height, so a 0–100% ramp smears a 5% tint across
thousands of pixels and the viewport reads flat white. Fixed-length stops keep the same wash
in view at any page length.

**Status colours bracket the brand pair rather than borrow it.** `ok` is a **deeper emerald**
(`#177040`) — green, but a more emerald green than the fresh leaf, so "success" is never
mistakable for "the counterweight". `warn` is pollen ochre, `danger` is a brick red chosen to
sit clearly away from the pink (a crimson would have collided with the blossom), and `info`
is the cool **sky** from the top of the ground, inked. Each clears 4.5:1 on both panel
surfaces.

**Every tint is derived.** `--accent-soft` is a 10% `rgba()` of `--accent` and the media and
avatar washes are the `--accent`→`--accent-2` pair — no hand-picked blends that could drift.

## Typography

Three faces, each with one job.

- **Zen Kaku Gothic New** (display) — headings, the wordmark, card titles. A
  Japanese-designed humanist gothic with light, open letterforms: it gives the airy cheer
  of the season (light weights, generous counters, no heaviness) and it ties the type to
  the same place the blossom comes from, so the kit's origin reads through letterform as
  well as colour.
- **Karla** (body) — everything you actually read. A clean grotesque with slightly warm,
  unfussy shapes; neutral enough that the display face stays the only voice with a spring
  in it.
- **IBM Plex Mono** (labels) — eyebrows, badges, table headers, code. A humanist mono, so a
  label stays legible without turning into a machine voice.

Display is tightened only a touch (`-0.01em` — a gothic does not want more than that), and
mono labels are tracked to `0.12em`: open and light, in keeping with a bright day, but still
short of a shout.

## Layout

The shared lab measure — `min(1040px, calc(100% - 2.5rem))` — with a
`0.35 / 0.65 / 1.15 / 2.25 / 3.5rem` spacing scale. Density is **comfortable**: enough air
that the ground's warm–cool shift is visible between the plates, but tighter than a mood
kit's, because a spring day is awake rather than contemplative. Cards, panels and fields all
sit on `--radius-lg` / `--radius-md`, and the block rule is the 1px petal hairline.

## Elevation & Depth

Airy, soft, and **not frosted**. Where `glass` puts a translucent pane on a pastel ground,
Sakura lifts an opaque warm-white card off a tinted one.

- `--shadow-1` — cards: a small contact shadow plus a wide, low-opacity plum drop
  (`rgba(58,36,56,.20)` at `26px`). Plum, never black: a black shadow on a warm ground reads
  as dirt.
- `--shadow-2` — elevated surfaces: the same idea wider and softer, so a raised card reads
  as further from the ground rather than as more raised.
- `--glow` — the primary button only, and it is a **blossom shadow, not a bloom**: a pink
  `0 10px 22px -10px rgba(200,50,95,.42)`. If it ever looks like light, it is too strong.
- `--blur: none` — an airy spring page is not a pane of frosted glass. This is the single
  cleanest line between Sakura and `glass`.

## Shapes

Gently rounded throughout: `--radius-sm: 10px`, `--radius-md: 14px`, `--radius-lg: 20px`,
and `999px` pills for badges, avatars, toggles and the progress bar. A blossom has no
corners, so the scale sits one step softer than the library default. `--cut: 0px` — nothing
is chamfered; a cut corner is an industrial signal and this kit is neither.

## Components

Every colour resolves to a `{colors.*}` token. Shadows, hairlines and gradients live in the
prose here and in `tokens.css`, because the component schema has no property for them.

- **button-primary** — a solid `{colors.primary}` blossom plate with `{colors.text-invert}`,
  a 14px radius and the pink `--glow` beneath. It is the one saturated object on a screen,
  which is what gives a bright palette a clear focal point.
- **button-primary-hover** — `{colors.primary-hover}`, one step **deeper**. The blossom
  bruises; it does not glow.
- **button-secondary** — `{colors.surface}` with an `{colors.accent-ink}` label and a
  rose-tinted rim (`color-mix` 45%); hover fills with the 10% `{colors.accent-soft}` wash.
  The label is the *deep* rose, never the fill pink.
- **button-ghost** — `{colors.text-muted}` with no rim; the quietest control.
- **card / card-elevated** — `{colors.surface}` and `{colors.surface-2}` at 20px, separated
  by the 1px `{colors.border}` petal hairline and `--shadow-1`, never a hard edge.
- **input** — `{colors.surface-2}` settled *below* the card, with a `{colors.border-strong}`
  rim so the field reads as a recess and not a floating box. Focus swaps to the pink border
  with an `{colors.accent-soft}` halo; the keyboard ring is `{colors.focus-ring}` **green**,
  so focus and hover can never be confused — and so the leaf is genuinely in the UI.
- **badge** — `{colors.text-muted}` mono caps in a pill on `{colors.surface-2}`.
  `badge-accent` is the 10% blossom tint with an `{colors.accent-ink}` label;
  `badge-ok` / `badge-warn` / `badge-danger` use the emerald, ochre and brick.
- **nav / nav-active** — a `{colors.surface}` pill bar; the current item takes
  `{colors.accent-soft}` with a deep-rose label, the calmest possible "you are here".
- **link** — `{colors.accent-ink}` on the ground. Never `{colors.primary}`: the fill pink is
  a 2.7:1 label and would be a real accessibility failure.

## Do's and Don'ts

**Do**

- Keep the ground `--bg`'s gradient and its px stops. The warm–cool shift is the kit's
  weather; flattening it to one hex makes the page read as white paper.
- Let pink **fill** and pink **label** be two different values. `{colors.primary}` for
  surfaces you click; `{colors.accent-ink}` for anything that is text.
- Use the leaf green in real UI — focus, gradients, bars — not only in swatches. Green in
  one chip is decoration; green at the focus ring is a season.
- Reach for `--sakura-ramp` when two accents must meet, and let the **cream** midpoint do
  the work of joining them.
- Spend the space. Comfortable padding is what keeps a saturated palette from feeling loud.

**Don't**

- Don't lighten `--accent` toward pastel to "soften" the kit. That is `glass`, and it also
  drops white-on-pink under 4.5:1. Deepen the ink instead; never lighten the ground.
- Don't use `{colors.primary}` as a text colour. It measures 2.7:1 on the ground. Small
  labels are `{colors.accent-ink}`.
- Don't put pink body text on the pink ground. The ink is `{colors.text}` (plum) —
  `{colors.tertiary}` is for labels and links only, at label sizes.
- Don't add a third "look at me" hue. Pink plus leaf green is the whole palette; the cream in
  the ramp is a midpoint, not a member.
- Don't introduce frosted translucency or a coloured glow. Soft opaque shadows only.
- Don't let the scatter or the blossom motif become a wallpaper. `--sakura-petal` and
  `--sakura-blossom` are accents for a plate, a masthead or a hero — never a page-long fill.
