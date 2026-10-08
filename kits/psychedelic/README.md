# Psychedelic

**1960s acid poster — a warped banded plate, five screen-print inks, fat groovy type.**

Part of [design-kits](../../README.md). Order `100`, mode `light`, source `original`.

## Stance

A 1960s acid poster rebuilt as a working UI kit. **The ground is a paper plate, and the page
is the poster**: `--bg` is a 3px halftone grain over a hard-banded ripple of overprinted
screen tints over a warm off-white paper ramp (`#fdfaf1` → `#f6ecd8` → `#fbf6e9`). Every
colour is an *ink* laid on that plate. That is the period-correct construction (a screen
print begins with paper, not with a coloured page) and it is also the only construction that
lets five clashing inks coexist without the page becoming unreadable: a fully saturated
ground is a poster you cannot read past the headline.

Organic, warped and fluid — **not** geometric, **not** mirrored, **not** crisp. No chamfer
(`--cut: 0px`), no grid, no glass, no neon bloom. The liquidity comes from pooled radii
(8 / 14 / 22px), thick saturated outlines that are deliberately *off-key*, and three pattern
motifs: a **warp** (the banded ground ripple), a **halftone** (a 3px dot screen) and a
**burst** (the full-strength five-ink sunburst).

## Key choices

- **The page is the poster, and every plate band is hard-stopped.** `--bg` stacks three
  layers: a `repeating-conic-gradient` halftone grain at 3px, `--psychedelic-warp` (a
  `repeating-radial-gradient` ripple centred at `16% 4%`, so its edges arrive as warped
  arcs), and a px-stop aged-paper ramp. Every band edge is two stops at one position — a
  ramp here would be a colour wash, not a screen print. Stops are in **px** so a band lands
  inside the first viewport instead of 2000px down.
- **The inks are laid as screen tints, and the tint level is a measured contrast decision.**
  On a light plate the deep inks sink plum type fast, so:
  - **Yellow (70%) and acid green (36%) carry the field at strength** — the two light inks.
  - **Magenta (12%), orange (18%) and purple (10%) sit as thin overprint rings** in the paper
    gaps, where they read as colour without dropping the plate below `--text-dim`'s floor.
  - The **full-strength clash is the graphics' job**: `--psychedelic-burst`, the `--media-bg`
    card panel and the masthead `--wash`. Five inks at strength never sit under type.
- **The bolder ground pushed `--accent-ink` one shade deeper**, to `#943005`. `#ff6a00` is a
  great button and an unreadable small label; the burnt-orange text ink has to clear 4.5:1
  on the darkest band the plate can make *and* on its own 16% tint composited over it. The
  first cut of this kit used `#a83606` on a flat ground; the plate now needs `#943005`, which
  is 6.67:1 on the plate and 4.70:1 on the composite.
- **Five inks, three jobs.** The swatch row shows more cells than five because it also lists the
  paper, the border and the status colours — the *inks* are five, and the copy counts those.
  - **Hot orange `#ff6a00` (`--accent`)** drives the **one primary action**. It is the only
    solid orange object on a screen.
  - **Deep purple `#5b1a8f` (`--accent-2`)** is the **cool counterweight**: media gradients,
    bars, avatars, and the focus ring.
  - **Acid green `#a8d400`, magenta `#e5198f`, yellow `#ffd21e` are graphic inks** — the
    ground field, the patterns, and the printed edge. They never carry text: on paper that is
    1.4:1, 3.5:1 and 1.2:1. This is a deliberate deviation from the "one accent plus one
    second accent" quality bar — the brief asks for a clashing poster palette, and the extra
    hues are confined to graphics so that no component gains a second call to action.
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
- **One ink tier.** All three surfaces stay paper (`#fefcf4` card, `#f4ecd9` nested), so a
  single plum ink reads on every ground and the `--text-on-surface*` capability is **not**
  needed. Stated rather than used.

## Signature material (declared in `kit.json`)

Three motifs, three jobs — atmosphere, texture, structure.

| Token | Job | What it is |
|---|---|---|
| `--psychedelic-warp` | **atmosphere** | `repeating-radial-gradient` — the ground ripple: yellow and acid bands at strength with magenta / orange / purple overprint rings in the gaps. Hard stops, warped arcs. |
| `--psychedelic-halftone` | **texture** | `repeating-conic-gradient` — a 3px magenta/yellow dot screen. The print idiom for texture, not a noise field. |
| `--psychedelic-burst` | **structure** | `repeating-conic-gradient` — a five-ink ray wheel with paper between the rays: the full-strength clash, confined to graphics (media panel, tile). |

The raw inks ship alongside as `--psychedelic-ink-acid / -magenta / -purple / -yellow /
-edge`, and `--psychedelic-ink-edge` is the off-key outline ink. The previous cut declared
seven slug extras, most of them the same device re-tuned; those are gone. Three motifs with
three distinct jobs is the point — a fourth dilutes them, and a motif capped at two or three
is the brief.

## Fonts, and why

- **Bowlby One** (display) — a heavy, bulbous, rounded display face: the fat Cooper-Black
  register of a hand-painted 1960s poster, in a single weight, so it reads as one loud painted
  word and cannot be over-applied.
- **DM Sans** (body) — clean, warm and neutral, so the display face is the only thing shouting.
- **Space Mono** (labels) — a wonky, period-adjacent mono for eyebrows, badges, table headers
  and code; deliberately not the library's JetBrains/Mono default.

The type contrast *is* the era: fat rounded display against a quiet grotesque.

## Trade-offs

- **The plate cannot flood with ink.** A light kit with plum type caps the deep inks at ring
  strength (magenta 12%, orange 18%, purple 10%); the poster's *volume* therefore comes from
  the two light inks at strength plus the graphics, not from a saturated page. That is the
  honest reading of "screen print on paper", and it is the constraint that keeps the page
  legible.
- **Designing the ground moved a text ink.** `--accent-ink` went `#a83606 → #943005` so the
  burnt-orange label survives the ink rings; the tint levels were solved against that value,
  not the other way round.
- **A layered `--bg` invalidates the shared lab masthead's own `background` shorthand** (CSS
  forbids a gradient as a colour stop inside another gradient), so the kit declares `--wash`
  — a pale hard-banded ray fan — to give the masthead a printed header instead of the lab's
  smooth radial bloom.
- **Acid green and yellow are unusable as text.** Intentional — an acid-poster palette is
  mostly colour-as-pattern, not colour-as-language. Anything that needs to be read is plum.
- **`--accent-soft` is orange-only.** `rgba(255,106,0,.16)` backs badge and nav fills that sit
  under `--accent-ink`, so it must stay in the orange family; magenta and acid green arrive via
  the ground field and the pattern extras instead.
- **Derived, not invented.** Every plate tint is its ink at reduced alpha, composited over the
  plate and measured; nothing in `tokens.css` is a hand-tuned approximation of a palette colour.

## Verification

Contrast is graded against the **darkest band the plate can make** (`warp acid on #f6ecd8`),
not an average. The model computes every paper stop × every warp band × the halftone grain ×
every `--wash` ray, plus the opaque surfaces and the `--accent-soft` composites.

| Pair | Ratio | Target |
|---|---|---|
| `--text` on the plate stop / worst band | **14.78 / 11.13:1** | ≥ 7 |
| `--text-muted` on `--surface` / worst band | **10.46 / 6.90:1** | ≥ 4.5 |
| `--text-dim` on plate / `--surface-2` / worst band | **6.39 / 6.37 / 4.81:1** | ≥ 4.55 |
| `--text-invert` on `--accent` / `--accent-hover` | **6.04 / 4.95:1** | ≥ 4.5 |
| `--accent-ink` on plate / `--surface` | **6.67 / 7.62:1** | ≥ 4.5 |
| `--accent-ink` on `--accent-soft` over the worst band | **4.70:1** | ≥ 4.5 |
| `--accent-ink-hover` on `--accent-soft` over the worst band | **5.07:1** | ≥ 4.5 |
| `--focus-ring` on the worst ground | **6.78:1** | ≥ 3 |
| status inks on `--surface-2` (`ok` / `warn` / `danger` / `info`) | **5.26 / 5.28 / 5.48 / 5.23:1** | ≥ 4.5 |

**Worst pair:** `--accent-ink` on `--accent-soft` composited over `warp purple + halftone on
#f6ecd8` = **4.70:1** (target 4.5).

All token contract names, including `--border-w`, are present. `python tools/build.py
--only psychedelic --no-export --no-lint` reports `lab html OK` and **no** token-contract gaps.

The script that produced every ratio is
`C:/Users/Lily/AppData/Local/hermes/cache/scratch/kit-contrast-psychedelic.py`; its run log is
`C:/Users/Lily/AppData/Local/hermes/cache/scratch/kit-verify-psychedelic.md`.

**Signature-tile non-flatness.** Each motif was rendered as `background:` on a 168×72 box over
the kit's `--surface-2` (what the lab's Signature strip does), screenshotted at dpr 2
(336×144) and scored by per-pixel luminance std-dev — `0` is the flat plate that is this
library's most-repeated defect. Measured with
`C:/Users/Lily/AppData/Local/hermes/cache/scratch/psy-tiles.cjs`:

| Motif | sd(luminance) | sd(red channel) | distinct colours |
|---|---|---|---|
| `--psychedelic-warp` | 0.0591 | 14.40 | 5 |
| `--psychedelic-halftone` | 0.2227 | 10.23 | 2 |
| `--psychedelic-burst` | 0.2731 | 39.16 | 7 |

The warp is the one worth watching: at its first tuning the band period (360px) was wider than
the tile, so the tile rendered as one flat yellow field (sd-red 3.39). It was tightened to a
~205px repeat so the tile now shows the yellow field, the magenta ring, the acid band and the
orange ring — five colours, four hard edges.

Warnings retained on purpose (`designmd lint`: **0 errors**, orphaned-token + tint warnings).
`orphaned-tokens` — the raw inks, the four paper stops, `bg-2`, `overlay`, `info`, the border
and focus colours are read by the shared lab straight from CSS, and **the motifs are not
expressible in `colors:`** (the linter errors on a gradient), so they ship as stops and live in
`tokens.css`. `contrast-ratio` on `button-secondary-hover` and `badge-accent` — the linter reads
them as ink-on-`#ff6a0029` without compositing the translucent tint over the plate; composited,
they are 4.70:1 (the worst pair above).

## Use when

Gig and festival posters, album art and music brands, counterculture marketing, anything that
should look screen-printed. Not for dense data tooling or long-form reading.
