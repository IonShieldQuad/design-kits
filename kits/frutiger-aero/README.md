# Frutiger Aero

**Sky-and-grass optimism, in glass.** A sky-blue-to-white ground with a green register at the
foot, seen through genuinely translucent panels whose top edge carries a **hard-edged white
specular band** — with drawn bubbles and water droplets in the air. Light, friendly, clean;
never corporate grey.

- Kit: `frutiger-aero` · order `200` · mode `light` · source `original`
- Fonts: Hind (display + body) · IBM Plex Mono (captions, labels)
- Tags: `light`, `glossy`, `translucent`, `2000s`, `sky`, `friendly`
- Signature: `--frutiger-aero-bubble`, `--frutiger-aero-droplet`, `--frutiger-aero-horizon`
- No `kit.css` — everything here is a token, including the drawn artwork.

## Stance

This kit is **the library's deliberate exception to its own non-smooth rule.** Every other kit
is required to shut five doors against smoothness — square corners, zero-blur shadows,
hard-stopped gradients, upscaled artwork, no blur. Frutiger Aero *is* smoothness: gradients
ramp, shadows are soft and cast, `--blur` is real and load-bearing on every card, and the
masthead carries a bloom. Softening this kit is not restraint, it is failure.

The one line that is not negotiable is legibility, and it is where the whole design is
constrained: **gloss costs contrast headroom.** See *The trade* below — it is the reason the
ground's most saturated stop is `#b4e0fb` and the specular band is 13px rather than a third of
the panel.

## What makes it glass rather than fog

One structural decision carries the material: **the specular band's lower edge is hard.**
`rgba(255,255,255,.52)` at 12px drops straight to `rgba(255,255,255,.02)` at 13px. A soft blur
with no highlight is fog; a blurred panel carrying a crisp white band across its top is glass.

Measured on the rendered card (deviceScaleFactor 4, sampled across the panel's full width):

| | rendered RGB | luminance |
|---|---|---|
| card rim (1px) | 177, 212, 236 | 0.60 |
| band, top | 250, 253, 254 | 0.988 |
| band, at the cut (12px) | 239, 250, 254 | 0.949 |
| just below the cut (13.5px) | 229, 247, 254 | 0.925 |
| card body (15px down) | 224, 246, 254 | 0.902 |

So the band is a strip **~20 units whiter in red** than the body below it, and the cut is a
step of **~15 units across a single pixel**. It is a lip, not a haze.

## Key choices

- **The band is 13px on content panels and a hard-edged top third on the material sample.**
  Measured, not timid: the shared lab puts the first line of type 18px below a card's top edge
  and ~17px below a nav item's, so a *percentage* band's edge lands inside `.card-body` on the
  Cards row — a hard white line across a paragraph. So the band keeps its hard edge and moves
  its edge instead: 13px on `--surface` (cards, nav), and the full top third on
  `.card-media`/the horizon token and the masthead lip (a 22px band, i.e. 23% of the 96px media
  panel and 31% of the 72px tile), where nothing is ever typeset. A specular band's height is
  set by the light source, not by the box, which is why it is px rather than a percentage.
  `--surface-2` has **no** band at all, because the same token backs `.input`, `.badge`,
  `.alert` and `pre.code` — a hard edge inside a 41px field cuts through the text in it.
- **The glass base is 34% white, and that is a measured correction.** The first build used 46%
  plus a `brightness(1.04)` in `--blur`, and the band came back **invisible**: the panel
  composited to L 0.989 and the band's plateau to L 0.991 — a step of **0.002**. A specular
  highlight needs headroom above the surface it sits on, and a near-white panel has none. The
  `brightness()` term is gone and the base came down; the bloom now lives in `--bg` and
  `--wash`, where it lightens the ground *before* the glass is composited over it (so it can
  only ever *raise* the luminance under card text, which keeps the contrast table conservative).
- **`--blur` is real and load-bearing:** `blur(16px) saturate(155%)`. `templates/lab.css`
  applies `var(--blur)` to every `.card`; set it to `none` and this kit is a flat pastel page.
- **A cool rim, not a white one.** `--border` is `rgba(84,152,206,.42)`. A white hairline is
  invisible on a sky (that is `glass`'s documented compromise); a soft blue line reads as the
  edge of a pane on both the sky and the glass, so section rules still exist on this page. The
  *bright* edge of a pane is a separate job and lives inside `--shadow-1` as an inset white
  line.
- **One action colour, one counterweight, no third.** Azure for action; grass green for
  gradients, media, charts and the green end of the ramp. The green is never text.
- **`--accent-ink` ships separately.** `--accent` is 3.89:1 as a small label on the sky, so
  every link, eyebrow, active nav/tab, badge label and secondary-button label uses
  `--accent-ink` at 5.52:1.
- **Saturated blue lives where nothing is typeset** — `.card-media`, the drawn motifs, and the
  progress/avatar fill under a *measured* white label. The ink stays dark; the sky stays pale
  enough to carry it.
- **Derived, not invented:** `--accent-soft` is a 14% tint of `--accent`; `--fill-bg`,
  `--gloss`, `--glow` and both shadows are `rgba()`/`linear-gradient()` expressions of the
  declared palette, not new hues.
- **No chamfer.** `--clip` is not declared, so `--frame-ring` is inert here. Generous radii
  only: 10 / 16 / 22px.

## Trade-offs and deviations

- **The ground's most saturated stop is capped by contrast, not by taste.** `--text-dim` is
  the token that fails first under gloss, and it must clear 4.55:1 on *every* ground the lab
  can put it on — for this kit that is the page ground itself (the Forms row sets labels and
  hints straight on the sky, with no panel behind them). Solving it backwards fixes a ceiling:
  the darkest ground stop may not go below **L 0.6998**, and the darkest *interpolated* point
  along the ramp measures exactly the same 0.6998, so the ramp never dips below its own first
  stop. `--frutiger-aero-sky` (`#b4e0fb`) is therefore the *bright* end of the sky, not the
  poster-vivid mid-blue the register would use. The vivid blues moved to the fills, the media
  panel, the motifs and the progress bar, where no text sits.
- **`--accent` is `#0d6db3`, not a register-true sky blue.** `#2196f3` gives a white label
  **3.10:1** — a lovely fill and an unusable button. `#0d6db3` measures 5.45:1 with white. A
  gloss is a fill, and on a light kit a fill has to carry a label.
- **The progress/avatar fill's gloss is capped at 10% white.** `.avatar` typesets a white
  monogram (`.avatar { color: var(--text-invert) }`), so the fill has to keep white ≥ 4.5:1
  across *all* of its bands: 10% white over `#0f6aa8` = **4.71:1**, 14% over `#0b4f80` =
  **5.99:1**, 14% over the green foot `#116b48` = **4.77:1**. A brighter, prettier gloss band
  measured **2.13:1** and was rejected. This is the trade in one token.
- **`.card-elevated` carries no band** — the shared lab reads `--surface-2` for
  `.card-elevated`, not `--surface`, so the raised panel in the Cards row is the *denser nested
  glass* (smooth, banded only by its top-edge highlight and its shadow). Shown honestly rather
  than worked around: giving both card tiers the band would mean putting one on `--surface-2`,
  which would band every input, badge, alert and code block. The band appears on the base card,
  the nav, the masthead lip and the media panel.
- **`--check-appearance` is deliberately not declared.** The contract gives one switch that
  squares both the checkbox *and* the radio, and the checked state is a filled box. Squaring
  the radio to get a square checkbox trades a correct control for an incorrect one, so the kit
  takes the browser's own rendering (with `accent-color` = the azure) and sets only
  `--check-radius: 6px`.
- **`--btn-shadow` is insets only.** Four of the five button variants (`.btn-secondary`,
  `.btn-ghost`, `.btn-danger`, `.btn-link`) are *transparent*, and a cast shadow on a
  transparent box is a grey blob with no plate under it. The bevel is therefore inner light on
  all variants; the cast shadow lives on `--glow` (the primary button) and on the panels.
- **The masthead's band is 36px and the sweep is diagonal.** A horizontal gloss band across the
  masthead would have to cross the `h1` (type starts at 40px), so the masthead lip is a 36px
  specular at the very top and the *sweep* is a 103deg diagonal — the one place a gradient's
  angle is doing structural work rather than decoration.
- **Two independent visual passes failed to see the card's band, and both were wrong.** At 50%
  scale and even in a 4× crop, an unprimed look reported "no bright band, no hard edge" on a
  panel where the pixel profile above is unambiguous. A specular band on an already-pale panel
  is a *quiet* feature; the brief's rule that an independent look is reliable for presence but
  unreliable for colour, thickness and hard-vs-smooth banding held here, and the measurement
  decided it. It is left quiet on purpose: the loud version (a top-third band on a content card)
  puts a white line through `.card-body`, which was measured, not assumed.
- **The gallery preview will look softer than the lab.** The kit's ground is a gradient, so
  `tools/build.py` skips its synthetic wash and paints the kit's own `--bg` (bubbles and all) —
  but the preview is 118px tall, so only the first stop of the ramp is in view. **The lab page
  is the reference view.**
- **The bubble field on the ground only ever *raises* luminance.** It is drawn in white strokes
  and white fills (168px tile), so it cannot darken type. Restated against the measurement: of
  725,920 gutter pixels down the whole 3490px page, exactly **208 are darker than the ramp's
  first stop** — one single row (y=425), the 1px full-width hairline under the masthead, on
  which nothing is typeset. Every other ground pixel is at or above `#b4e0fb`. That is what
  makes the contrast table provable.
- **`--text-dim` is a dark slate, not a light grey.** On a saturated ground the caption tier has
  to be dark to survive; the hierarchy is carried by `--text` (13.06:1 on the gloss band) /
  `--text-muted` (7.42:1 on a card) / `--text-dim` (6.00:1) rather than by lightness alone.

## How it differs from its nearest neighbours

| Kit | Same as | Different |
|---|---|---|
| `glass` | light, translucent, `--blur` load-bearing, one accent | `glass` is *restrained pastel* — a rose/lilac/mint/sky ramp, saturation held down, **no specular band at all** (its sheen is a soft 135deg wash), hairline **white** edges, and a periwinkle-indigo accent. Frutiger Aero is a **scene** (sky over grass), its glass carries a **hard-edged** specular band, its rim is a cool blue line, its second colour is a grass green, and it draws bubbles and droplets. `glass` is quiet; this is optimistic. |
| `dark-glass` | the same material | it is the *dark* pole: a near-black ground with light ink, light hairline rims, a violet/cyan mesh, and no specular band. Here the ground is light, the ink is dark, the rim is cool, the band is hard, and there are motifs. Different polarity, different rim logic, different motifs. |
| `chrome` | gloss | chrome is **reflective metal on black**: a brushed-metal ramp *as* the surface, magenta/cyan, hard 2px line work, and smoothness deliberately shut (zero-blur shadows). This is **transmissive** glass on a sky — you see the ground through it — with a soft cast shadow and a real blur. |
| `holographic` | surface-as-identity | holographic is **diffraction**: hard-banded prismatic iridescence on charcoal, with its five smoothness doors deliberately shut. Here smoothness is the point, the material is refraction rather than diffraction, and the ground is daylight rather than dark. |
| `tropical-breeze` | light, optimistic, blue + green, three structural hues | it is **paper, not glass**: cards are clean warm paper, `--blur: none` ("open air, not glass"), coral is the single action colour, and its motifs are a frond, a wave and a parasol. Frutiger Aero is translucent, blurred, azure, and its motifs are a sphere, a teardrop and a horizon. The mood overlaps; the **material** does not. |
| `kawaii` | light, generous radii, playful | kawaii is a **sticker sheet**: pastel pink/lilac/mint, `--blur: none` (its own comment reads *"glass owns that"* — this kit is the one it means), a bouncy overshoot ease and drawn sparkles/hearts/confetti. Frutiger Aero rounds generously too, but its register is clean consumer tech rather than sticker-cute, and its third dimension is the material. |

## The trade: gloss costs contrast headroom

Three specific places where the register and readability pull against each other, and what was
chosen:

1. **A bright sky ground vs. dark ink.** Every ink here is graded against the *darkest* ground
   stop. A light kit binds on its most saturated ground, not its palest one — the palest ground
   is the easy case for dark ink. The saturation ceiling (`#b4e0fb`, L 0.6998) is set by
   `--text-dim`, which backs every caption, hint, placeholder and swatch label.
2. **A glossy fill vs. a white label.** Capped at 10% white over `#0f6aa8` for the avatar
   (4.71:1); a 38% band measured 2.13:1.
3. **The specular band vs. a line of text.** Capped at 13px, so the hard edge never crosses a
   glyph; the unconstrained top-third band lives only where nothing is typeset. And the base
   itself is capped at 34% white, because a panelless whiter than that leaves the band
   invisible (measured: a 0.002 step at 46% + `brightness(1.04)`).

## Contrast — the compositing maths

The ground is a gradient, panels are translucent, and the specular band is the palest thing on
the page, so a single flat hex proves nothing. Two worst cases bound everything:

- **Ground worst case = the darkest (most saturated) stop of the ramp**, `#b4e0fb`
  **L = 0.6998**. Every bloom and the bubble field only raise luminance, and the darkest
  *interpolated* point along the ramp measures 0.6998 too; the only darker pixels on the page
  are 1px hairlines that carry no type (measured: 208 of 725,920 sampled gutter pixels).
- **Palest case = the gloss band at full alpha over the palest stop**, i.e. effectively white,
  L = 1.0. Nothing in this kit is light-coloured text except `--text-invert`, which only ever
  sits on `--accent` and on the progress/avatar fill.

### Required pairs

| Pair | Foreground | Ground (worst case) | Ratio | Target |
|---|---|---|---|---|
| body text | `--text` `#10334f` | darkest stop `#b4e0fb` | **9.32:1** | ≥ 7:1 ✓ |
| secondary text | `--text-muted` `#2c4a66` | darkest stop `#b4e0fb` | **6.58:1** | ≥ 4.5:1 ✓ |
| tertiary text | `--text-dim` `#3a5872` | darkest stop `#b4e0fb` | **5.32:1** | ≥ 4.55:1 ✓ |
| button label | `--text-invert` `#ffffff` | `--accent` `#0d6db3` | **5.45:1** | ≥ 4.5:1 ✓ |
| accent as text | `--accent-ink` `#0a5590` | darkest stop `#b4e0fb` | **5.52:1** | ≥ 4.5:1 ✓ |
| accent as text on a badge | `--accent-ink` `#0a5590` | `--accent-soft` 14% over `--surface-2` `#c6e1f4` | **5.70:1** | ≥ 4.5:1 ✓ |
| accent as text on a card | `--accent-ink` `#0a5590` | `--accent-soft` 14% over `--surface` `#b3d9f2` | **5.20:1** | ≥ 4.5:1 ✓ |
| status | `--ok` `#0f6b3d` | darkest stop `#b4e0fb` | **4.70:1** | ≥ 4.5:1 ✓ |
| status | `--warn` `#7d4d00` | darkest stop `#b4e0fb` | **5.11:1** | ≥ 4.5:1 ✓ |
| status | `--danger` `#b0203c` | darkest stop `#b4e0fb` | **4.81:1** | ≥ 4.5:1 ✓ |
| status | `--info` `#0b5f9e` | darkest stop `#b4e0fb` | **4.77:1** | ≥ 4.5:1 ✓ |
| focus ring | `--focus-ring` `#0a5590` | darkest stop `#b4e0fb` | **5.52:1** | ≥ 3:1 ✓ |

**Worst pair in the kit: `--ok` `#0f6b3d` on the darkest ground stop `#b4e0fb` at 4.70:1**
(target 4.5:1). It is a status colour used as badge text; the tighter a status colour gets, the
more the green has to be pulled towards the forest floor.

### Composited (glass and tint) pairs — graded, not assumed

All against the darker of the two card grounds, i.e. a 34%-white `--surface` over the darkest
stop (`#ceebfc`), or a 44%-white `--surface-2` over it (`#daf0fd`):

| Pair | Ground | Ratio |
|---|---|---|
| `--text` on a card, below the band (`#d1ecfc`) | 10.64:1 |
| `--text-muted` on a card (`#ceebfc`) | 7.42:1 |
| `--text-dim` on a card (`#ceebfc`) | 6.00:1 |
| `--text-dim` on a card below the band (`#d1ecfc`) | 6.07:1 |
| `--text-dim` on `--surface-2`, its darkest end (`#daf0fd`) | 6.34:1 |
| `--text-muted` on `--surface-2` | 7.84:1 |
| `--text-invert` on the upper `--fill-bg` band (10% white over `#0f6aa8`) | 4.71:1 |
| `--text-invert` on the lower `--fill-bg` band (14% white over `#0b4f80`) | 5.99:1 |
| `--text-invert` on the green foot (14% white over `#116b48`) | 4.77:1 |

`templates/lab.css` also passes each *rendered* text box through `verify-lab.cjs`, which samples
the real pixel behind the text and re-composites any alpha — that run is clean (below).

## Signature motifs

Three, each doing a different job, each drawn as base64 inline SVG (a sphere and a teardrop are
organic forms; nested radial rings read as a bullseye, so gradients cannot do them).

Non-flatness is measured on the **rendered** 168×72 tile, per channel, in the lab:

| Token | Job | Drawn | Measured (σ, per channel) | Luma range |
|---|---|---|---|---|
| `--frutiger-aero-bubble` | a **sphere** — rim, body gradient, one hard-edged specular | 3 bubbles at 56/36/24px over a sky base | **20.3 / 11.7 / 5.6** | 0.320–1.000 |
| `--frutiger-aero-droplet` | a **teardrop** — different silhouette, lit differently (caustic pooled low in the bulb) | 3 droplets at 48/28/22px over a grass base | **23.4 / 12.9 / 22.4** | 0.335–0.989 |
| `--frutiger-aero-horizon` | a **plane** — sky over grass with a hard specular line *on* the horizon, under a hard-edged band | 3 CSS layers, two hard stops | **22.0 / 10.3 / 45.8** | 0.570–0.986 |

For scale: a flat plate of the tile base measures σ < 1. All three are 20–46 units of
per-channel deviation, so every tile survives the "empty chip" failure on its own.

The bubble's rim is deliberately **split**: bright on the lit (upper-left) arc, weightier and
darker through the lower-right. A uniform outline reads as a sticker — the first draft had one,
and it was rejected on sight at 4× magnification. Each sphere carries exactly one light source
(upper left) with a hard-edged core inside a soft halo; the lower-right second highlight of the
first draft was cut for the same reason.

## Verification

From the repo root:

```bash
python tools/build.py --only frutiger-aero --no-export --no-lint
KIT_SHOTS="$LOCALAPPDATA/Temp/frutiger-aero-shots" node tools/verify-lab.cjs frutiger-aero
```

Result: **`PASS  frutiger-aero`** — 0 errors, 0 missing tokens, 0 console errors, no contrast
failures (the harness reads computed styles, samples the real pixel behind each text box, and
composites the translucent stack). `verdict.json` is in `$KIT_SHOTS`.

Everything numeric in this file was measured, not asserted: the static table comes from a
Python compositing script, the band and tile figures come from pixel profiles of the rendered
lab at deviceScaleFactor 1 and 4, and the ink pairs are re-checked independently by
`verify-lab.cjs`.

`npx -y -p @google/design.md designmd lint kits/frutiger-aero/DESIGN.md` → **0 errors, 10
warnings + 1 info**, all documented below.

## Linter

The `@google/design.md` component vocabulary whitelists `backgroundColor`, `textColor`,
`typography`, `rounded`, `padding`, `size`, `height`, `width`. Measured findings, not a
description:

| Count | Rule | Why it stays |
|---|---|---|
| 8 | `broken-ref` — `'borderColor' is not a recognized component sub-token` | The rim is the substance of this kit: a white hairline is invisible on a sky, which is why every pane's edge is a blue line. `borderColor` is not in the vocabulary, so the eight uses are recorded as warnings and the rim is written up in prose under *Colors* and *Elevation & Depth*. |
| 2 | `contrast-ratio` **false positive** — `textColor #0a5590 on backgroundColor #0d6db324` reports 1.42:1 | `badge-accent` and `nav-item-active`. The linter compares the ink to the un-composited 14% tint, so it effectively measures the ink against itself. Composited over a surface the pair measures **5.70:1** (badge) and **5.20:1** (on a card). |
| 1 | `token-summary` (info) | 33 colours, 7 type scales, 4 radii, 5 spacing tokens, 39 components. |

Zero **errors**, and **no `orphaned-tokens`** — every declared colour is referenced from at least
one component.

## When to use

Consumer software and device-adjacent marketing, playful dashboards and onboarding, media and
lifestyle products, game launchers, anything that should feel bright, glossy and friendly rather
than severe. It is a **light** kit: do not use it for dark-mode shells or dense data work that
wants a neutral ground. Avoid it for print (use `--frutiger-aero-solid` /
`--frutiger-aero-air`), and anywhere `backdrop-filter` is unavailable — without the frost this
is a pale pastel page with bubbles on it.

## What the lab could not express

Honest list, per the brief's report-back rule — none of it was worked around by editing the lab:

- **A display *weight* hook.** The register leans towards a light-to-regular display weight, and
  the shared lab sets `font-weight: 700` on `.t-display` and `.masthead h1` with no token to
  change it (`--style-display` covers `font-style` only). The kit therefore expresses its light
  display voice through a near-neutral tracking value and generous radii instead. A
  `--weight-display` (or `--light-display`) hook would fix it for every kit whose register is
  lighter than its headings currently render.
- **A per-variant button shadow.** `--btn-shadow` reaches every variant at once, so a kit whose
  secondary/ghost/danger variants are transparent cannot give its *filled* variants a cast
  shadow without floating a grey blob under the transparent ones. `--glow` happens to cover
  `.btn-primary` only, which is why the primary button's cast shadow lives there and every other
  variant gets an inset bevel.
- **A separate specular token for `.card-elevated`.** The lab reads `--surface-2` for it, and
  `--surface-2` also backs every input, badge, alert and code block — so one token cannot carry
  a hard-edged band on the raised panel without banding all of those too.

## IP

**No Microsoft trade dress.** There is no Windows logo, no window chrome copied from a
screenshot, and no Vista/7 branding or UI text anywhere in this kit. The vocabulary is generic
optics — glass, a specular band, a bubble, a droplet, a horizon — and the kit is named by the
aesthetic's established *community* name, not a product name.

**The typeface is not Frutiger.** The real Frutiger is a commercial Linotype licence and this
repository is public, so the kit ships **Hind**, a Frutiger-adjacent free humanist sans, with
`"Frutiger"` present only as a *system fallback string* inside the font stack — never as a
Google Fonts request.
