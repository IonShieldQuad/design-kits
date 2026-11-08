# Crimson Labyrinth

**A gothic ritual console — crimson hairlines and an engraved rose on black velvet.** Not a dark
page with a red accent: an instrument panel in a vampire's chamber. Near-black oxblood plates, a 1px
crimson frame cut by a 12px octagon, one engraved rose struck into the plate's face, a sheen along
the top edge and a crimson identity line along the bottom. One accent, one brass counterpoint, and a
status ladder that deliberately does not use the accent.

- Kit: `crimson-labyrinth` · order `220` · mode `dark`
- Fonts: Chakra Petch · JetBrains Mono
- Tags: `dark` `gothic` `ornate` `ritual` `romantic`
- Source: **derived** from the user's own `bespoke-desktop` Li//OS desk — `prototypes/v9-lilythium`,
  place 06. Palette, panel construction and drawn motif are the prototype's tokens, not inventions.

## Stance

This is a **place**, not a mood. `Li//OS` is one desktop whose fifteen locations are variants of a
single instrument-panel grammar: a hairline frame, an opaque face carrying a sheen band, a bottom
occlusion band, a 157° face fall, a 5% accent tint and one drawn texture; one accent hue per place;
one signature motif. Crimson Labyrinth is the place where the OS goes ritual: crimson on oxblood, a
rose engraved into the metal. The grammar is shared with five siblings and is not up for
interpretation — what belongs to this place is its colour, its metal, its motif and its one
inversion (the status ladder).

## Lineage

| place | kit | order | accent | face | ground | shape | motif |
|---|---|---|---|---|---|---|---|
| 01 | `azure-technologies` | 205 | `#4FD8FF` | `#0A0F16` | `#05080D` | chamfer 16 | hex lattice |
| 02 | `mainframe-access` | 210 | `#54E08A` | `#04100A` | `#020704` | square | scanlines |
| 05 | `pastel-district` | 215 | `#FF8FC4` | `#23141D` | `#160C13` | round 6 | bokeh |
| **06** | **`crimson-labyrinth`** | **220** | **`#FF4D5E`** | **`#140A0C`** | **`#090305`** | **octagon 12** | **engraved rose** |
| 07 | `sunset-boulevard` | 225 | `#B06CFF` | `#150C28` | `#0A0512` | chamfer 18 | perspective grid |
| 08 | `viridian-fields` | 230 | `#147A57` | `#0C1410` | `#0A1512` | round 5 | engraved fern |

**The axis that separates this place from its five siblings is colour temperature and what the
ornament *is*.** It is the family's only warm place: every other one is cool (cyan, phosphor green,
blue-violet, violet) or candy (pink, sage). And it is one of the two places whose motif is *engraved
line art on metal* rather than a field — the rose is struck into the plate, not projected behind it.

**Against the `gothic` kit (order 120), which is the neighbour a reader will actually compare it
to:** `gothic` is editorial velvet — plum ground, ivory type, a wine accent, a *rose bloom drawn on a
thorned stem* as a decorative mark, soft 5–16px curves, a true pill, and Cormorant Garamond carrying
the romance. This kit is the machine, not the book: oxblood and crimson, an *engraving of a rose as
the card's own material* (not a sticker on it), a hard 12px octagon with a 1px frame, 0px radii, and
the family's squared technical face. One is a novel cover on velvet; the other is the console a
vampire keeps its records in. They share a register, not a construction — and `gothic` keeps red as
danger while this kit cannot (below).

## What the material is

`--surface` is not a fill: it is `--crimson-labyrinth-pane`, the desk's own `.card-in`, pasted
unchanged. The layer order **is** the light model:

1. **sheen** — white 30% across the first 1px (the specular lip), 17% on the next, .048 fading out by
   34% of a 9%-tall band at the top. This is light arriving from above;
2. **occlusion** — black 46% → 13.8% → 0 across the bottom 9%. This is the plate seated in the
   panel, and it is what stops a flat rectangle reading as a sticker;
3. **the rose plate** — one 268px engraving, pinned to the right side at 20% down (see *The motif*);
4. **the identity edge** — the accent hairline along the bottom, from 7% to 62% of the width, at 55%;
5. **the tint** — 5% crimson over everything;
6. **the face fall** — 157°: white 12% at the start, nothing at 44%, black 24% at 78%, black 52% at
   the end. A plate lit from one corner;
7. **the face** — `#140A0C`.

Move the tint under the face and the rose vanishes; move the fall under the face and there is no
fall; put the texture under the tint and it is invisible. The order is the whole design.

`--surface-2` — inputs, badges, alerts, code, `card-elevated` — is the **nested** tier: a shallow
sheen, half the tint, the place's own `--panel` `#13080C`. It drops the rose and the identity edge on
purpose, because a 268px engraving on a 2.5rem control is clutter rather than material.

`--blur: none` on every surface. They are opaque, the desk forbids glass, and a blurred opaque card
is a repaint cost with no visual return.

## The motif

One engraving, two plates, neither tiled. Both lines are pasted **verbatim** from
`docs/lilythium/textures.css`; do not redraw, re-encode, re-pitch or re-alpha them.

| token | what it is | pitch and placement | alpha |
|---|---|---|---|
| `--crimson-labyrinth-tex` | the card plate: the whole engraving | `268px auto`, `100% 20%`, `no-repeat` | 0.085 white |
| `--crimson-labyrinth-tex-ground` | the ground plate: the same engraving, larger | `560px auto`, `100% 78%`, `no-repeat` | 0.0468 white |

The alpha is baked into each SVG because the desk applied its `--txA` as a pseudo-element `opacity`,
which a background layer cannot do; the folded values are the desk's own and were verified at
gallery-tile size. Two scales, two jobs: the ground plate is larger and half the density, so the page
has a quiet bloom at its lower right and a card still reads as a plate with an engraving on it. Equal
weight makes the whole page one busy field.

**Read the plates in the lab as plates, not as patterns.** A 168×72 signature tile shows a *window*
onto a 268px plate pinned at 100%/20% — i.e. the sparse top-right of the engraving — so the `tex`
tile looks nearly empty even though the card (where the plate is composed for) is unmistakable. That
is a property of a non-tiling plate rendered as a swatch, and it is the same for every place in this
family. The `field` tile, which is the ground, shows the engraving properly because the ground plate
sits lower and wider.

## Key choices

- **The status ladder is inverted, and that is the kit's one structural decision.** Crimson is the
  action here, so crimson cannot also mean danger: a red danger chip next to a crimson primary
  button makes every button on the page read as an error. `--danger` is therefore the place's hot
  orange `#FF7A45`, `--warn` its brass `#D9B36B`, `--ok` a desaturated sage `#9BC7A8` and `--info` a
  muted violet `#9E8CC7`. No member of the ladder is crimson, which is what keeps state and action
  separable by hue at a glance.
- **`--accent-ink` is the desk's `--accHi`, and it is not the fill.** `#FF4D5E` is a mid-light
  crimson: 5.34:1 on the brightest band of a card, 8.23:1 on the ground. That is enough for a fill
  and a hairline, not enough for 12px text, so labels use `#FF8D99` (8.23:1 on the ground, 5.34:1 on
  a card's lightest band).
- **`--text-invert` is very dark ink, not white.** The accent is mid-light, so the button plate takes
  `#160406` at 6.14:1; white on `#FF4D5E` would be 3.24:1.
- **The ink is warm bone, not the desk's cool grey.** The desk's root ink (`#E9F0F6` / `#B2BFCA` /
  `#93A1AE`) is a cool blue-white, which on a warm oxblood ground reads faintly cyan. The three inks
  here are the same lightness family, shifted warm, and are graded against the composited pane.
- **`--border` is the desk's white 14% hairline; `--border-strong` is the place's `--accLine`
  (`rgba(255,77,94,.6)`).** So the *frame* of a plate is white hairline and the *emphasis* is
  crimson — the crimson a reader sees on a card is the identity edge and the buttons, not the frame.
  This is faithful to the desk and it is worth knowing before "fixing" it.
- **No `--frame-ring`.** `tools/build.py` derives it from `--clip`; authoring one would double-draw
  the frame and fight the derivation. The derived ring is what keeps the 1px border along the two
  diagonals that `clip-path` would otherwise cut away.
- **`--focus-inset: 2px`.** A clipped box loses `outline` along the chamfer, so the keyboard ring is
  painted inside the silhouette instead.

## Derived, and why

- `--crimson-labyrinth-scene-a: rgba(43,10,18,.66)` — the place's `--sceneA` `#2B0A12` at 66%, so
  the ground's two fields read as fields and not as two blobs of solid maroon.
- `--accent-soft: rgba(255,77,94,.12)` — a 12% tint of `--accent`, written as `rgba()` because it is
  derivable and must stay in sync. **12% is set by arithmetic, not taste**: an accent badge label on
  the brightest band a card shows measures 4.44:1 at 16%, 4.56:1 at 14% (0.01 short of the 4.55 bar)
  and 4.67:1 at 12%. The tint was moved down until the worst composite cleared.
- `--text-dim: #BCA2A4` — the previous candidate `#B39A9C` measured 4.50:1 on that same band; this is
  the value that clears 4.55 with headroom (4.96:1).
- `--fill-bg` — `rgba(255,77,94,.25)` → `#FF4D5E`, the accent's own 25% tint ramping into the fill.
- `--wash` — the masthead is a wash over the ground, never a surface: crimson 14% blooming down from
  the top, with brass 7% off the right shoulder as candlelight. Both stops are palette colours.

## Contrast (computed, not eyeballed)

Measured from `tokens.css` against the **composited** grounds the kit actually paints — a card's
brightest band is `rgb(68,52,54)` (sheen .048 + the fall's white .12 at 0° + the 5% tint over
`#140A0C`), `--surface-2` is `rgb(42,25,29)`, the lit ground is `rgb(38,15,20)`, the masthead wash
composites to `rgb(79,33,35)`. Translucent plates are composited before grading.

| Pair | Ratio | Target | |
|---|---|---|---|
| `--text` on `--bg` (lit / dark) | **14.87** / **16.94**:1 | ≥ 7 | ✓ |
| `--text` on a card's bright band | **9.66**:1 | ≥ 7 | ✓ |
| `--text` on `--surface-2` | **13.71**:1 | ≥ 7 | ✓ |
| `--text-muted` on `--surface-2` / card band / wash | **8.78** / **6.18** / **7.00**:1 | ≥ 4.5 | ✓ |
| `--text-dim` on `--bg` / wash / card band / `--surface-2` | **7.64** / **5.61** / **4.96** / **7.04**:1 | ≥ 4.55 | ✓ |
| `--text-invert` on `--accent` / `--accent-hover` | **6.14** / **7.37**:1 | ≥ 4.5 | ✓ |
| `--accent-ink` on `--bg` / card band / wash | **8.23** / **5.34** / **6.05**:1 | ≥ 4.5 | ✓ |
| `--accent-ink` on an accent badge (`--surface-2` plate / card band) | **6.49** / **4.67**:1 | ≥ 4.5 | ✓ |
| `--danger` on `--surface-2` / card band / ground | **6.47** / **4.56** / **7.02**:1 | ≥ 4.5 | ✓ |
| `--warn` on `--surface-2` / card band | **8.45** / **5.96**:1 | ≥ 4.5 | ✓ |
| `--ok` on `--surface-2` / card band | **8.86** / **6.25**:1 | ≥ 4.5 | ✓ |
| `--info` on `--surface-2` (the only place it is text) | **5.60**:1 | ≥ 4.5 | ✓ |
| `--focus-ring` on the ground / card band | **8.23** / **5.34**:1 | ≥ 3 | ✓ |

**Tightest real pair:** `--danger` on a card's brightest band, 4.56:1 (target 4.5). A hot orange is
the only non-crimson red this palette can afford: purer reds lose too much luminance to clear the
bar on a plate that lightens toward its corner. **Not graded:** `--info` on a card's bright band
(3.95:1) — violet is never body text on a plate; it is a badge label on `--surface-2` (5.60:1) and a
3px alert rule. `--border` and `--border-strong` sit at 1.44:1 and 5.02:1 by design: hairlines that
never carry meaning alone.

## Trade-offs

- **Inverting the ladder costs the obvious red.** "Delete" is an orange here. That is the price of
  crimson being the action, and it is the right price: a red danger beside a crimson button is a
  page where every action looks like a fault. The kit pays it once, in `--danger`, and states it.
- **A 1px white frame is a quiet frame.** The desk's hairline is white at 14%, 1.44:1 on the face:
  present, never assertive. It is the reason the crimson identity edge exists — the colour has to
  arrive somewhere on a resting card, and it arrives at the bottom, off-centre.
- **A chamfer clips its own shadows.** `--shadow-1` / `--shadow-2` are the desk's values and they are
  real, but a clipped box clips its outer falloff too, so on this kit they read as the plate's edge
  rather than as a lift. Depth comes from the derived frame ring, the sheen and the occlusion band.
  Restoring a visible drop shadow would need `filter: drop-shadow()` — a construction, not a token,
  and this family ships no `kit.css`.
- **The roses are quiet.** White at 8.5% on `#140A0C` is a watermark, not an illustration; on a
  photo-quality screen you read the engraving at arm's length, and it disappears on a laptop in
  daylight. That subtlety is the desk's own and was not raised to make it "show" — an engraving that
  shouts is a print, not a plate.
- **The shared type pairing buys one OS and costs one voice.** Chakra Petch on all six places is what
  makes them read as the same machine — and it means this kit cannot have the calligraphic romance
  `gothic` gets from Cormorant Garamond. The ornament has to live in the plate instead. Do not "fix"
  the shared pair; it is the family's contract.

## When to use

Dark romance, gothic editorial, nightlife and music, witchy or vampire branding, and game UI that
should feel **ritual rather than tactical** — a menu that behaves like an altar. It is a poor fit for
anything that must look safe, clinical or corporate, and it is a poor fit for dense dashboards: the
plate is composed for a few large objects, not a wall of small ones.

Reach for a sibling when:

- you want **velvet and a serif**, soft curves and a drawing of a rose rather than an engraving of
  one → `gothic`;
- you want the same chamfer but **cool and luminous** — a projected screen rather than a metal plate
  → `photonic`, or place 01 `azure-technologies`;
- you want **restraint without warmth** — a machine that reports rather than a room that broods →
  place 02 `mainframe-access`.

## Linter warnings kept deliberately

`python tools/build.py --only crimson-labyrinth --no-export` reports three identical findings and one
summary line; there are **no errors**.

- `contrast-ratio: textColor (#ff8d99) on backgroundColor (#ff4d5e1f) 1.47:1` ×3 — on `badge-accent`,
  `button-secondary-hover` and `nav-item-active`. The linter grades the ink against
  `primary-soft` **as if it were an opaque colour**, which it is not: it is a 12% tint. Composited
  over the surfaces those three components actually sit on, the pair is **6.49:1** (badge on
  `--surface-2`), **6.30:1** (hover plate on a card's mid band) and **4.67:1** on a card's brightest
  band. All three clear 4.5:1; the 1.47:1 number is an artifact of grading a translucent tint as a
  solid. `tools/verify-lab.cjs` — which samples the real rendered pixels — passes those elements.
- `token-summary: 18 colors, 7 typography scales, 4 rounding levels, 5 spacing tokens, 25 components`
  — an inventory line, not a defect.

Nothing else is suppressed: every colour key in `DESIGN.md` is referenced by a component (the two
ground stops are described in prose instead of being declared orphans), and every other
`contrast-ratio` pair the linter can compute passes.

## Files

`DESIGN.md` (normative values) · `tokens.css` (the contract) · `kit.json` (gallery metadata) ·
`index.html`, `DESIGN.html` (generated by `python tools/build.py --only crimson-labyrinth`).
