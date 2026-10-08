# Pixel DMG

**Four shades of green.** A Game Boy DMG screen: a reflective monochrome LCD
behind a green polariser, where the whole design is carried by four greens and
a single pixel-art landscape — no smoothness anywhere.

- Kit: `pixel-dmg` · order `140` · mode `light`
- Fonts: Press Start 2P · Silkscreen · VT323
- Tags: `light` `retro` `pixel` `gameboy` `monochrome` `arcade`
- Source: original. Canonical four greens, extended one step at each end so
  WCAG-AA text can exist on a reflective LCD.
- Files: `tokens.css` · `DESIGN.md` · `kit.json` · `README.md`
  (no `kit.css` — the lab needed two tokens, not an override; see below)

## The four-shade problem (measured)

The DMG's canonical palette is four greens and nothing else:

| shade | hex | relative luminance |
|---|---|---|
| ink | `#0f380f` | 0.0296 |
| mid | `#306230` | 0.0958 |
| light-mid | `#8bac0f` | 0.3503 |
| LCD | `#9bbc0f` | 0.4297 |

Measured, the **best contrast any two of them can make is 6.02:1** — `#0f380f`
on `#9bbc0f`. Every other pair is worse. That is the problem in one number: the
contract asks for **7:1** of `--text` and **4.55:1** of `--text-dim`, and the
four shades cannot reach it. A reflective LCD also has no backlight above
`#9bbc0f` and no ink below `#0f380f`, so the kit resolves it by **extending the
ramp one step at each end** and documenting exactly what it added:

- **DEEP `#082608`** — `#0f380f` darkened to ~35% of its luminance; this is
  `--text` (7.43:1 on the darkest ground).
- **LIT `#a3c510 #b6d313 … #f6ff70`** — `#9bbc0f` lifted 8%–115%; the notional
  backlight ladder a reflective panel does not have, used for the artwork.

Everything else is one of the four shades, or a two-shade mix.

## The dim-text decision

`--text-dim` is `#1a481a`, **not** `#306230`. On the pale field a mid-green
scores 3.29:1 and fails the 4.55:1 floor: there is almost no luminance headroom
between "dark enough to pass" and the darkest ink. Dim text on a DMG is
therefore nearly as dark as body text. `#306230` is spent on rules and focus,
where 3.29:1 is a legal graphical-object contrast.

## The page ground is a pixel-art landscape, confined to the lit ladder

`--bg` is not a fill and not a gradient. It is a **160×90 SVG landscape** — a
bright sky, a stepped pixel sun, blocky clouds, a hard horizon slab and a
dithered ground — stretched to full width with `100% auto` (so the art pixels
stay square, ~8px on desktop) and `--pixel-render: pixelated` (so they stay
crisp). Below the band a hard-stop checkerboard carries the field to the foot.
The art is drawn **small and scaled up**, which is the only way to get genuinely
chunky pixels; drawing it at full size would render smooth.

**The artwork is deliberately confined to the lit ladder.** Contact-sheet
measurement showed why: the darkest tone anywhere in the ground is the canonical
LCD green `#9bbc0f` (L .4297 → `--text` 7.43:1), and even the next shade up,
`#8bac0f` (L .3503), would drop `--text` to 6.2:1 — under 7:1. So the landscape
uses `#9bbc0f` and lighter only, and the ink shades are reserved for components
and motifs. The measured consequence is a low-contrast, single-hue landscape
(that is exactly what a four-green reflective screen is); the horizon stays
legible because of the hard slab, not because of a strong value split. With more
light, light text would have to sit on a dark sky, and every ratio here would
break.

## Nothing is smooth — the five doors, closed

The kit was reworked so no smoothness enters by any of the five routes:

1. **Curves → 0.** Every `--radius-*` is `0px` (and `--cut: 0px`). The shared
   lab's `.toggle` track/knob, `.dot` and `.bar` rail bind to `--radius-pill`,
   so they square with the rest.
2. **Soft shadows → zero blur.** `--shadow-1/2` are `4px 4px 0 0` and
   `6px 6px 0 0` offset blocks. No blurred drop anywhere.
3. **Gradients → hard stops / dither.** `--bg` is art + a hard-stop checker;
   `--media-bg` is a hard-stop dither; the three motifs are hard-stop
   gradients; the masthead wash is removed (`--wash: transparent`), and the lab's
   two smooth `.bar`/`.avatar` fills are replaced with `--fill-bg` (a hard-stop
   dither).
4. **Scaled artwork → drawn small, scaled up.** The ground is a 160×90 SVG and
   the sprite a 7×6 grid, both scaled with `--pixel-render: pixelated`, and the
   sun is built from unit rects (a vector `<circle>` would render a smooth arc —
   measured and fixed).
5. **Blur / bloom → none.** `--blur: none`, no `backdrop-filter`, and the
   masthead's radial accent bloom is replaced by the ground itself.

## Contrast — measured, not eyeballed

Every ratio is computed from the rendered token values, graded against the
darkest ground each token can land on (the `#9bbc0f` field and horizon, L .4297,
and every artwork tone — all artwork tones are ≥ `#9bbc0f`, so this is the
floor).

| token | value | worst ground | ratio | target |
|---|---|---|---|---|
| `--text` | `#082608` | `#9bbc0f` | **7.43** | ≥ 7 |
| `--text-muted` | `#0f380f` | `#9bbc0f` | **6.02** | ≥ 4.5 |
| `--text-dim` | `#1a481a` | `#9bbc0f` | **4.83** | ≥ 4.55 |
| `--accent-ink` | `#0f380f` | `#9bbc0f` | **6.02** | ≥ 4.5 |
| `--text-invert` on `--accent` | `#b6d313` on `#0f380f` | — | **7.73** | ≥ 4.5 |
| `--text-invert` on `--accent-hover` | `#b6d313` on `#1c4f1c` | — | **5.64** | ≥ 4.5 |
| `--ok` | `#0f380f` | `#9bbc0f` | **6.02** | ≥ 4.5 |
| `--warn` | `#174117` | `#9bbc0f` | **5.32** | ≥ 4.5 |
| `--danger` | `#0a2a0a` | `#9bbc0f` | **7.11** | ≥ 4.5 |
| `--info` | `#1c4a1c` | `#9bbc0f` | **4.69** | ≥ 4.5 |
| `--focus-ring` | `#306230` | `#9bbc0f` | **3.29** | ≥ 3 |

The **worst required pair in the kit is `--info` at 4.69:1** on `--surface-2`;
the tightest text pair is `--text-dim` at 4.83:1. Both clear their targets.

## Status is distinguished by luminance, not hue

The DMG has no red and no green — one green at four depths. Status therefore
cannot be encoded in hue: `--danger` is the deepest green (7.11:1), `--ok` next
(6.02:1), `--warn` (5.32:1) and `--info` (4.69:1) lighter still, and the UI
always names a status with a word or an icon. Relying on four greens alone to
say "failed" versus "draft" would fail exactly the users a monochrome screen
already marginalises.

## The three signature motifs

Declared in `kit.json` so the lab renders them (tiles proof: standard deviation
of each 168×72 chip, over the `--surface-2` base):

| token | what it is | std-dev |
|---|---|---|
| `--pixel-dmg-dither` | 2px checkerboard (shading) | **71.4** |
| `--pixel-dmg-dotmatrix` | 1px LCD grid every 4px (screen) | **71.2** |
| `--pixel-dmg-sprite` | 7×6 pixel heart, inline SVG (icon) | **81.5** |

The ground artwork itself measures **std 84.2** over a 1280×760 render — it is a
landscape, not a flat plate.

## No `kit.css` — the lab needed two tokens instead

This kit was authored with a `kit.css`, and it no longer has one. Four smooth
remnants lived in the *shared* lab and no token reached them: the toggle track
was a literal `999px` pill, the toggle knob and status dot were `50%` circles,
and `.bar > i` / `.avatar` had hardcoded two-stop accent gradients.

Per the contract, that is a **missing token, not a per-kit override** — and it
was a live defect, not just a limitation: the pill and circles ignored
`--radius-pill`, so *any* kit declaring square corners still rendered a rounded
toggle and a round status dot. The lab was fixed (`--radius-pill` on the toggle
track/knob, the dot and the bar rail; `--fill-bg` for the two gradients) and the
`kit.css` was deleted. The kit now has no curve and no smooth blend anywhere,
using tokens alone — and every future square kit inherits the fix.

## Trade-offs

- **The palette is four shades plus a documented extension.** A purist DMG has
  no `#082608`; the contract's 7:1 made it necessary, and it is recorded rather
  than hidden.
- **The landscape is low-contrast by constraint.** It can only use greens that
  keep 7:1 under dark text, so it is a single-hue, high-key scene — the honest
  picture of a four-shade reflective screen.
- **Three pixel typefaces is one more than usual.** Each earns it: Press Start 2P
  is headline-only, Silkscreen is the readable grid, VT323 the narrow data face.
- **Hard offset shadows are structural.** They exist so depth never introduces
  anti-aliased grey — a fifth colour.
- **`--radius-pill` is `0px`.** A badge is a stamped tile, not a lozenge; the
  token keeps its name.

## When to use

Retro-computing and emulator pages, chiptune and game tools, playful portfolios,
8-bit microsites, and anything that should feel like a small green screen in your
hands. Avoid it for anything that must read as calm, clinical or contemporary —
that is `quiet`, `glass` or `glorious-morning`.
