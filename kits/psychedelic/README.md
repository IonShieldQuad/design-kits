# Psychedelic

**1960s acid poster — paper ground, five screen-print inks, fat groovy type.**

Part of [design-kits](../../README.md). Order `100`, mode `light`, source `original`.

## Stance

A 1960s acid poster rebuilt as a working UI kit. **The ground is paper** — a warm, uneven
off-white (`--bg` is an aged paper ramp, px stops, `#fbf7ea` → `#f1e7cc` → `#faf5e8`) — and
every colour is an *ink* laid on top of it. That is the period-correct construction (a screen
print begins with paper, not with a coloured page) and it is also the only construction that
lets five clashing inks coexist without the page becoming unreadable: a fully saturated ground
is a poster you cannot read past the headline.

Organic, warped and fluid — **not** geometric, **not** mirrored, **not** crisp. No chamfer
(`--cut: 0px`), no grid, no glass, no neon bloom. The liquidity comes from pooled radii
(8 / 14 / 22px), thick saturated outlines that are deliberately *off-key*, and four pattern
extras made from `repeating-radial-gradient`, `repeating-conic-gradient` and `radial-gradient`.

## Key choices

- **Paper ground, ink on top.** `--bg` is a px-stop paper ramp so the aged band lands inside
  the first screen instead of below it. Contrast is checked against its **darkest stop
  `#f1e7cc`** — the worst case for plum ink. `--bg-2: #f6efdb` is the solid stand-in for
  exports.
- **Five inks, three jobs.**
  - **Hot orange `#ff6a00` (`--accent`)** drives the **one primary action**. It is the only
    solid orange object on a screen.
  - **Deep purple `#5b1a8f` (`--accent-2`)** is the **cool counterweight**: media gradients,
    bars, avatars, and the focus ring.
  - **Acid green `#a8d400`, magenta `#e5198f`, yellow `#ffd21e` are graphic inks** — pattern
    extras, the ink ramp, and the printed edge. They never carry text: on paper that is
    1.4:1, 3.5:1 and 1.2:1. This is a deliberate deviation from the "one accent plus one
    second accent" quality bar — the brief asks for a clashing poster palette, and the extra
    hues are confined to graphics so that no component gains a second call to action.
- **Fill and text are different jobs.** `--accent-ink: #a83606` (5.33:1 on the worst stop)
  carries the eyebrow, links, secondary-button labels, active nav/tab, inline code and accent
  badges; `--accent-ink-hover: #8c2d03` is the text hover. `#ff6a00` is a great button
  (6.04:1 under plum) and an unreadable small label.
- **Dark plum ink on orange.** `--text-invert` equals `--text` (`#2a0a3e`): white on
  `#ff6a00` is ~2.4:1, plum on orange is 6.04:1 and reads like screen-print ink on a plate.
  Don't "fix" it by lightening `--text-invert`.
- **Thick, saturated, off-key outlines.** `--border-w: 2px` and the edge is its own ink
  (`#961478`, a magenta-purple half a step off both the magenta and the purple) rather than a
  neutral hairline. **2px, not 3px:** at 3px the lines of an input, a badge and a 22px corner
  start to collide, and the palette already carries the volume.
- **Soft pooled radii.** 8 / 14 / 22px + pills. The library's other printed kits are small
  and square-cornered; here the corners are pooled because the kit is organic, not geometric.
- **Printed misregistration, not light.** `--glow` is two hard offsets on the primary button
  (`2px 2px 0` magenta, `4px 4px 0` yellow) — two plates printed out of register.
  `--shadow-2` is a hard plum offset plus a magenta ink pool. `--blur: none`.
- **One ink tier.** All three surfaces stay paper (`#fdfaf0` card, `#f2e9d2` nested), so a
  single plum ink reads on every ground and the `--text-on-surface*` capability is **not**
  needed. Stated rather than used.

## Signature material (declared in `kit.json`)

| Token | What it is |
|---|---|
| `--psychedelic-swirl` | `repeating-radial-gradient` — pooled concentric ink bands, off-centre |
| `--psychedelic-burst` | `repeating-conic-gradient` — a sunburst of orange and magenta rays |
| `--psychedelic-wobble` | `repeating-radial-gradient` from far outside the box — warped banded stripes, not straight ones — over a pooled warm wash |
| `--psychedelic-blob` | two layered `radial-gradient`s — a pooled multi-ink wash |
| `--psychedelic-ramp` | the full five-ink sequence, orange → magenta → purple → acid |
| `--psychedelic-misreg` | the two-plate hard-offset shadow (magenta + yellow), applied |
| `--psychedelic-grain` | a two-pass `repeating-linear-gradient` crosshatch — the paper's printed weave |

The raw inks ship alongside as `--psychedelic-ink-acid / -magenta / -purple / -yellow /
-edge`, and `--psychedelic-ink-edge` is the off-key outline ink.

## Fonts, and why

- **Bowlby One** (display) — a heavy, bulbous, rounded display face: the fat Cooper-Black
  register of a hand-painted 1960s poster, in a single weight, so it reads as one loud painted
  word and cannot be over-applied.
- **DM Sans** (body) — clean, warm and neutral, so the display face is the only thing shouting.
- **Space Mono** (labels) — a wonky, period-adjacent mono for eyebrows, badges, table headers
  and code; deliberately not the library's JetBrains/Mono default.

The type contrast *is* the era: fat rounded display against a quiet grotesque.

## Trade-offs

- **Five inks against the "one accent + one second accent" bar.** Deliberate and briefed. The
  discipline is enforced by *role* instead of by count: exactly one action colour, exactly one
  counterweight, and the remaining three cannot be type, so they can never compete for
  attention with a control.
- **A gradient `--bg` invalidates the shared lab masthead's own `background` shorthand** (CSS
  forbids a gradient as a colour stop inside another gradient), so the masthead renders
  transparent and the paper ramp shows straight through — seamless. The side effect is that the
  masthead loses its local `--accent-soft` wash in the lab; orange still appears in the eyebrow,
  buttons, tints and badges.
- **Acid green and yellow are unusable as text.** Intentional — an acid-poster palette is
  mostly colour-as-pattern, not colour-as-language. Anything that needs to be read is plum.
- **`--accent-soft` is orange-only.** `rgba(255,106,0,.16)` backs badge and nav fills that sit
  under `--accent-ink`, so it must stay in the orange family; magenta and acid green arrive via
  the pattern extras instead.
- **Derived, not invented.** `--accent-soft` and the two `--glow` offsets are the inks at
  reduced alpha / full strength; nothing in `tokens.css` is a hand-tuned approximation of a
  palette colour.

## Verification

Contrast (`docs/KIT-SPEC.md` v1.1 targets; `--bg` checked against its darkest stop `#f1e7cc`):

| Pair | Ratio | Target |
|---|---|---|
| `--text` on `--bg` (worst stop) | **14.07:1** | ≥ 7 |
| `--text-muted` on `--surface` | **10.29:1** | ≥ 4.5 |
| `--text-invert` on `--accent` | **6.04:1** | ≥ 4.5 |
| `--text-invert` on `--accent-hover` | **4.95:1** | ≥ 4.5 |
| `--text-dim` on `--bg` / `--surface` / `--surface-2` | **6.08 / 7.17 / 6.19:1** | ≥ 4.55 |
| `--accent-ink` on `--bg` (worst) / `--surface` | **5.33 / 6.29:1** | ≥ 4.5 |
| `--accent-ink` on `--accent-soft` composited over ground / surface | **4.61 / 5.33:1** | ≥ 4.5 |
| `--focus-ring` on `--bg` (worst) | **8.57:1** | ≥ 3 |
| status inks on `--surface-2` (`ok` / `warn` / `danger` / `info`) | **5.11 / 5.14 / 5.33 / 5.09:1** | ≥ 4.5 |

All token contract names, including `--border-w`, are present. `python tools/build.py
--no-export --no-lint` reports `lab html OK` and **no** token-contract gaps.

The script that produced every ratio is
`C:/Users/Lily/AppData/Local/hermes/cache/scratch/kit-contrast-psychedelic.py`; the run log is
`C:/Users/Lily/AppData/Local/hermes/cache/scratch/kit-verify-psychedelic.md`.

Warnings retained on purpose (`designmd lint`: **0 errors**, 16 warnings). Fourteen are
`orphaned-tokens` — the raw inks, the four gradient stops, `bg-2`, `overlay`, `info`, the
border and focus colours are read by the shared lab straight from CSS, and **the gradients
themselves are not expressible in `colors:`** (the linter errors on one), so they ship as
stops and live in `tokens.css`. Two are `contrast-ratio`: `button-secondary-hover` and
`badge-accent` are read as ink-on-`#ff6a0029` because the linter does not composite a
translucent tint over a ground — both are tinted *surfaces* in the shared lab, not text
pairs, and composited over the page they are 4.61:1 (`--accent-ink` on `--accent-soft` over
the darkest paper stop) and 5.33:1 (over `--surface`).

## Use when

Gig and festival posters, album art and music brands, counterculture marketing, anything that
should look screen-printed. Not for dense data tooling or long-form reading.
