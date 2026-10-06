# Zen Garden

**Peace and tranquility on a grey, rainy day: an overcast ground, wet-stone ink, one deep
moss sage and a rain blue.**

`12` · light · `Source Serif 4 · Inter · IBM Plex Mono` · source: original

## Stance

This is a **mood kit**, and the mood is restraint. The brief was one line — *"peace and
tranquility on a grey, rainy day"* — and almost everything in the token set follows from
translating that sentence rather than from picking pretty colours.

Three translations did the work:

- **Overcast, not sunny.** The ground is a cool, desaturated rainy-day grey (`#e8ecf0`).
  Explicitly *not* cream and *not* white. Cream would make the afternoon sunny; white would
  make it sterile. Every neutral step in the kit is cool, and keeping the whole ramp cool
  is what makes it read as weather rather than as a paper app.
- **Wet stone and moss.** Ink is a soft charcoal with a cool cast (`#2b3238`) — never pure
  black, which would be an edge, and this kit has no edges. The action colour is a deep
  moss sage; the second hue is a rain blue.
- **Quiet depth and generous air.** 1px hairlines, soft wide shadows at low opacity, 8–14px
  radii, a slower-than-default transition. Nothing snaps, nothing glows, nothing is square.

Use it for journaling, wellness and habit apps, calm reading interfaces, personal sites,
meditation and breathwork tools. **Not** for dashboards that must alarm, dense data
tooling, or marketing that must shout — the loudness budget is spent on legibility, and
nothing is left over for emphasis.

## The palette, and the role of each colour

| Token | Value | Role |
|---|---|---|
| `--bg` | `#e8ecf0` | **The overcast ground.** The single most important value in the kit. |
| `--bg-2` | `#eef2f6` | Mist lifted above the ground; the masthead's top stop. |
| `bg-stop-1/2/3` | `#eef2f6` / `#e8ecf0` / `#e2e8ee` | The three stops of the mist gradient (the gradient itself is `--zen-garden-mist`). |
| `--surface` | `#f2f5f8` | Cards — a lift of mist above the ground. |
| `--surface-2` | `#e6eaf0` | Nested panels and inputs — settled *below* the card. |
| `--text` | `#2b3238` | **Wet-stone charcoal**, cool cast. All body and display ink. |
| `--text-muted` | `#4d585f` | Secondary reading ink: card bodies, table cells. |
| `--text-dim` | `#565f69` | Captions, placeholders, table headers. |
| `--text-invert` | `#ffffff` | Ink on the action colour. |
| `--accent` | `#4a6658` | **Moss sage — the single action colour.** Buttons, links, active nav, focus tint. |
| `--accent-hover` | `#40594b` | The pressed step — one deeper, so a press settles instead of lighting up. |
| `--accent-2` | `#567694` | **Rain blue — the second hue.** Gradients, media plates, chart bars, avatars. Never text. |
| `--accent-soft` | `rgba(74,102,88,.10)` | 10% sage tint: focus halos, active nav, `badge-accent`, inline code. |
| `--ok` / `--warn` / `--danger` / `--info` | `#33714d` / `#8a6220` / `#a8453d` / `#43668e` | Status, held at the kit's low saturation so a status reads as a tint, not an alarm. |
| `--border` / `--border-strong` | `#cdd5dd` / `#aab6c2` | Hairline and emphasised line. |
| `--focus-ring` | `#3c6b93` | Deep rain-blue keyboard focus — deliberately *not* the sage action. |

The two accents are far apart in hue (a green and a blue) *and* in lightness, so they stay
distinguishable at a glance and at thumbnail size — and they are the only two hues in the
kit. `--accent-2` is a fill colour and measures under 4.5:1 on the ground by design; it is
never used for text.

## Derived, and why

- **`--bg` is solid, not a gradient.** A gradient `--bg` *silently voids* the shared lab's
  masthead background: `templates/lab.css` nests `--bg-2` and `--bg` inside a
  `linear-gradient(...)`, and a gradient nested in a gradient is invalid CSS, so the whole
  `background` shorthand is dropped — taking the accent wash with it. This kit wants that
  wash, so the mist ships as an extra (`--zen-garden-mist`) built from the three
  `bg-stop-*` stops, and `--bg` stays a colour. The stops are also the values in
  DESIGN.md's `colors:` map, because *a gradient is not a colour* and the linter errors on
  one there.
- **`--accent` was darkened from `#5f7d6a` to `#4a6658`.** This is the kit's one real
  correction and it was driven by numbers, not taste. At `#5f7d6a`, white on the sage
  measured **4.54:1** — a hair over the 4.5 floor — and sage used as a *link* colour on the
  overcast ground measured **3.82:1**, a genuine failure. The tempting fix is to lighten
  the ground; that is the wrong direction, because it pushes the kit toward cream and kills
  the rain. Darkening the accent instead lifts white-on-sage to **6.30:1** and
  sage-on-ground to **5.31:1** while leaving the colour unmistakably muted botanical.
- **`--accent-soft` is 10%, not 14%.** A heavier tint erodes the action colour's contrast
  *against its own tint*, and two lab components put moss text on that tint (active nav,
  `badge-accent`). At 10% the sage clears 4.5:1 on its tint over every ground; at 14% it
  does not.
- **`--text-invert` is pure white.** Sage is dark enough that white is both the highest
  contrast available and the right read (chalk on moss), unlike the library's other light
  kits where dark-on-accent wins.
- **`--accent-2` is `#567694`, not the brief's `#5b7d9c`.** At `#5b7d9c` white text on a
  moss-to-rain gradient (the avatar) measured 4.32:1. One step deeper fixes it and keeps it
  a rain blue.
- **`--border` and `--border-strong`** are two steps of the same cool grey as the ink:
  `#cdd5dd` for page hairlines, `#aab6c2` for input rims, which must read against
  `--surface-2` rather than against the ground.
- **`--glow` is a shadow, not a bloom.** `0 8px 22px -12px rgba(74,102,88,.50)` — a soft
  sage drop under the primary button. There is no coloured light in this kit.
- **`--blur: none`** — overcast is not glassy, and frosted glass would draw a hard,
  high-contrast edge around every surface, which is the opposite of the mood.

## Typography, and why it reads as tranquil

**Source Serif 4** (display) over **Inter** (body), with **IBM Plex Mono** for labels.

The serif is the tranquil voice: a *humanist* serif with open counters, calligraphic
stress and an unhurried, low-contrast rhythm. A serif at heading size reads as
contemplative — a garden journal, a temple inscription — rather than as a product
headline; that single choice does most of the "peace" work that colour cannot. Inter stays
plain so the serif is the only warm voice on the page, and IBM Plex Mono is a *humanist*
mono, softer than a JetBrains or a Share Tech terminal face, so labels stay legible without
becoming a machine voice.

There is a structural reason too: a serif over a sans body separates the two type levels
by **letterform** as well as by size. That is the kit's primary defence against a muted
palette sliding into grey mush — hierarchy survives even when the colour does not shout.

**Rejected alternative:** a single gentle gothic sans, *Zen Kaku Gothic New*, for display
and body. Two sans faces flatten the hierarchy exactly where this palette can least afford
it, and it would tie a mood kit to a regional aesthetic the brief never asked for.

## Trade-offs

- **Low chroma costs contrast, and the sage pays for it.** The accent had to be darkened
  well past the brief's example value to stay legible as a link. The kit is *deeper* than
  it first looks, and that is deliberate — the alternative was a washed-out button.
- **`--text-dim` at 5.4:1 on the darkest ground is nearly as legible as `--text-muted`.**
  That is intentional for a mood kit: greying secondary copy into nothing is what makes a
  calm interface feel *dim* rather than *quiet*. Differentiate with size and weight.
- **`--accent-2` is not text-safe** (3.95:1 on `--surface`). It is the price of a rain blue
  that stays rain blue; it is therefore scoped to fills — gradients, media, avatars, bars —
  and never to a label.
- **The ground carries almost no identity on its own.** `#e8ecf0` is a ~4% luminance
  shift from white with negligible chroma, so at thumbnail size the overcast grey reads as
  "near-white" — deliberately, because the brief's rainy-day grey is what makes full-size
  pages calm. It also means this kit's recognisability in a grid comes from its **one moss
  hue and its serif/rhythm**, not from its background. If you need the ground to assert
  itself, apply `--zen-garden-mist` (the rain gradient) rather than darkening `--bg`: a
  darker ground pushes the kit out of "overcast" and into "dim".
- **No elevation drama.** Floating surfaces (menus, toasts) have only `--shadow-2` and
  their hairline to work with. That reads as under-designed in a marketing context, which
  is why this kit is scoped to tools and reading, not landing pages.

## Deliberate deviations

- **`--bg` is a solid colour, the mist is an extra** — see above. This deviates from the
  library's gradient-ground kits (Summer Sunset) for a concrete rendering reason.
- **`--text-dim`, `--border`, `--border-strong` are in `tokens.css` *and* in the DESIGN.md
  `colors:` map.** They are included because they all carry documented numeric guarantees
  in this kit; there is no uncertainty about them to hide.
- **`tertiary` is a step of `primary`, not a third hue.** The schema asks for a `tertiary`;
  this kit's honest answer is that it has exactly two hues by design. Its `tertiary` is the
  pressed sage (`#40594b`).
- **`--cut: 0px`.** The chamfer belongs to Carbon and Signal. Mixing shape languages would
  make both arbitrary.

## Contrast

All ratios computed from `tokens.css` (WCAG 2.1 relative luminance). Full log:
`C:/Users/Lily/AppData/Local/hermes/cache/scratch/kit-verify-zen.md`.

| Pair | Ratio | Target |
|---|---|---|
| `--text` on `--bg` | 10.94:1 | ≥ 7 ✓ |
| `--text-muted` on `--surface` | 6.67:1 | ≥ 4.5 ✓ |
| `--text-invert` on `--accent` | 6.30:1 | ≥ 4.5 ✓ |
| `--text-dim` on `--bg` | 5.46:1 | ≥ 4.55 ✓ |
| `--text-dim` on `--surface` | 5.93:1 | ≥ 4.55 ✓ |
| `--text-dim` on `--surface-2` | 5.37:1 | ≥ 4.55 ✓ |

Supporting pairs the lab actually renders: `--accent` on `--bg` **5.31:1** (the `a` link
colour), `--accent` on `--accent-soft` over any ground ≥ **4.59:1** (active nav,
`badge-accent`), `--text-muted` on `--surface-2` **6.05:1**, and every status colour
≥ 4.52:1 on both panel surfaces.
