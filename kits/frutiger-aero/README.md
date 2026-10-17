# Frutiger Aero

**Sky-and-grass optimism, in glass — over a place, not a pattern.** A sunlit meadow: clear
sky ramping to the masthead, a low sun in the upper right, three ranges of rolling green hills
receding into their own haze, and the mown field you are standing in. The panels float on it as
translucent glass whose top edge carries a **hard-edged white specular band**. Bubbles and water
droplets live on the **tiles**, not on the wallpaper.

- Kit: `frutiger-aero` · order `200` · mode `light` · source `original`
- Fonts: Hind (display + body) · IBM Plex Mono (captions, labels)
- Tags: `light`, `glossy`, `translucent`, `2000s`, `meadow`, `friendly`
- Signature: `--frutiger-aero-bubble`, `--frutiger-aero-droplet`, `--frutiger-aero-horizon`
- No `kit.css` — everything here is a token, including the drawn landscape.

## Stance

This kit is **the library's deliberate exception to its own non-smooth rule.** Every other kit is
required to shut five doors against smoothness — square corners, zero-blur shadows, hard-stopped
gradients, upscaled artwork, no blur. Frutiger Aero *is* smoothness: gradients ramp, shadows are
soft and cast, `--blur` is real and load-bearing on every card, and the masthead carries a bloom.

The line that is not negotiable is legibility — and it is where the whole design is constrained.
**Gloss costs contrast headroom, and so does a field.** A green meadow is a mid-luminance ground,
not a near-white one: compared with the pale-ground values this kit used to ship, its body ink now
sits **59% lower in relative luminance**, `--text-dim` 45% lower and the status colours 45–60%
lower, and its glass is 12 points denser. A "success" green had to become a forest green to be
readable on grass. Every number below was measured off the rendered page.

## The ground is a scene

`--bg` is nine layers, top-down:

| # | Layer | What it does |
|---|---|---|
| 1 | sun core, 104px | the light source: a small hot cream core at **82% / 250px** |
| 2 | sun bloom, 520×430 | the wide low glow that lifts the upper-right sky |
| 3–5 | three cloud banks | flattened white ellipses — something has to be *in* the sky |
| 6 | **drawn landscape** (one base64 SVG, 1280×760, anchored `82% 570px`) | sky left transparent; three ranges, each veiled before the nearer one is painted over it; mown contours and blade grain in the near field |
| 7–8 | two broad daylight pools | sunlight lying on the meadow at y≈1900 and y≈3000, at 0.18–0.20 alpha |
| 9 | the ramp | px-stopped sky → haze → far → mid → meadow, **and the fallback**: without the artwork this is still a horizon, not a bubble field |

**Aerial perspective is the whole trick.** Each range is painted, then covered by a pale haze
veil that is strongest at its foot, then the nearer range is painted over the veil. What survives
is a band of haze between every two crests — cool and pale at the top of each range, warm and
deep at the foot. Measured across one row of the meadow (y=900), the green runs
`rgb(154,192,121)` on the left flank to `rgb(173,204,136)` on the sunlit right: **one light source,
upper right**, and every range is cool on its left and warm on its right.

**The mown field.** Eight contour swaths (15→45px wide, 0.04–0.11 alpha, alternating light and
dark) whose spacing widens toward the viewer, plus ~420 scattered blade strokes at 0.07–0.19
alpha. Both live inside a mask that fades to zero at the image's bottom edge, so the texture
*dissolves* into the ramp at ~1300px instead of stopping at a line. It is deliberately faint:
broad swaths, no high-frequency pattern, nothing that competes with a paragraph.

**Why the horizon is at 570px.** The masthead is 476–499px tall depending on whether Hind has
loaded. At 570 the first viewport shows a clear band of sky under the masthead rule, then the
whole landscape — far, mid and near crests plus meadow with visible mowing — before the fold at
900px. The first build of this pass put the artwork at 520 and the crest read as *tangent* to the
masthead rule: two competing horizontals 40px apart. 570 is the measured fix.

**Why `82%` and not `50%`.** The artwork is 1280px wide, so on a wide viewport its position is
immaterial. Below 1280 it matters: anchored at 82% the image stays on the sun, and the sun stays
in frame at 390px instead of being cropped away with the centre.

**Why px stops.** The body's gradient box is the whole document (~3,560px). A `0% → 100%` ramp
smears the sky over several thousand pixels and the first viewport reads as flat near-white. Every
stop is in px so the sky-to-field walk happens inside the first screen and the meadow holds its
colour for the 2,500px below it.

## Key choices

- **The specular band's lower edge is hard.** `rgba(255,255,255,.52)` at 12px drops straight to
  `.02` at 13px. Measured on the rendered card at deviceScaleFactor 4, down a column through the
  top edge:

  | | rendered RGB | luminance |
  |---|---|---|
  | field behind the card | 160, 198, 124 | 0.496 |
  | band, y+1.5px | 255, 255, 254 | 0.999 |
  | band, at the cut (y+13px) | 222, 240, 206 | 0.821 |
  | just below the cut (y+14px) | 197, 229, 168 | 0.714 |
  | card body, y+22px | 197, 229, 168 | 0.713 |

  So the cut is a step of **0.107 in luminance across about three-quarters of a CSS pixel**, and
  the panel's body sits **0.218 above the field** behind it. A soft blur with no highlight is fog;
  a blurred panel carrying a crisp white band is glass.
- **The band is 13px, not "the top third".** The shared lab puts the first line of type 18px below
  a card's top edge and ~17px below a nav item's, so a *percentage* band's edge lands inside
  `.card-body` on the Cards row — a hard white line across a paragraph. The band keeps its hard
  edge and moves its edge instead. The unconstrained top-third band lives only on `.card-media`,
  the `--frutiger-aero-horizon` token and the masthead lip, where nothing is ever typeset.
- **The glass got denser: 34% → 46%, and 44% → 58% for the nested tier.** Over the previous pale
  ground 34% was enough. Over a meadow at L 0.50 a 34% pane composites to L 0.61 — 0.11 above the
  grass, which reads as a *stain*, not a surface. 46% puts the card body at L 0.652 (worst case,
  over the darkest grass) and 0.714 where it actually sits, which is 0.22 above the field. Above
  ~55% the field stops reading through the glass at all. `--surface-2` stays denser on purpose:
  it is the pane inside the pane, and it is also the base the signature tiles are judged on.
- **`--blur` is real and load-bearing:** `blur(16px) saturate(155%)`. `templates/lab.css` applies
  `var(--blur)` to every `.card`; set it to `none` and this kit is a flat pastel page.
- **A cool rim, and now a deeper one.** `--border` is `rgba(38,116,168,.46)`. A white hairline was
  invisible on the pale sky; on grass it would be invisible twice over. A saturated mid-blue reads
  as the edge of a pane against *both* grounds it has to work on — the field at L 0.43 and the
  glass at L 0.65–0.72.
- **The masthead wash now fades to zero at its bottom edge.** Its last stop used to be `.20`
  white at 100%, which on a pale ground read as a soft edge and on grass drew a hard horizontal
  seam across the landscape — at exactly the height where the eye is looking for a horizon. The
  wash fades out, and a warm sun bloom aligned to the pixel with `--bg`'s sun (82% / 250px) sits
  on top of the gloss sweep so the disk cannot be cut off by the masthead box.
- **One action colour, one counterweight.** Azure for action; grass green for gradients, media,
  charts and the far ranges. The green is never text.
- **`--accent-ink` ships separately, and it matters more now.** `--accent` is **2.49:1** as a small
  label on the grass (3.65:1 on a card), so every link, eyebrow, active nav/tab, badge label and
  secondary-button label uses `--accent-ink` at 5.20:1.
- **Derived, not invented:** `--accent-soft` is a 14% tint of `--accent`; `--fill-bg`, `--gloss`,
  `--glow` and both shadows are `rgba()`/`linear-gradient()` expressions of the declared palette.
- **No chamfer.** `--clip` is not declared, so `--frame-ring` is inert here. Generous radii only:
  10 / 16 / 22px.

## How it differs from its nearest neighbours

Three kits in this library are also light, optimistic and green-ish. The difference is not the
palette; it is what the ground *is*.

| Kit | Its ground | How this kit differs |
|---|---|---|
| `glorious-morning` | **First light.** A clear sky with a gold dawn band and a light-ray wash, sunrise gold as the action colour, and nothing frosted (`--blur: none`). | That is a moment — dawn, radiant, and flat by design. This is a **place**: a field with a horizon, seen through glass that actually blurs. Its sun is a low white-cream daylight sun, not a gold dawn; its accent is azure, not sunrise gold; and its depth comes from haze between ranges, not from light rays. |
| `tropical-breeze` | **A warm coastal afternoon.** Sand, sea-foam and palm green in a flat warm ramp, coral as the single action colour, cards of clean warm paper (`--blur: none`). | That is a *palette* on paper; this is a *scene* under glass. Tropical breeze has no horizon, no distance and no mown texture — its green is palm, warm and yellow-leaning. This kit's green is meadow, cooler, and structured into three hazy ranges you can see the depth of. |
| `zen-garden` | **Stillness.** Wet stone, moss sage and rain blue in a three-stop grey ramp; muted, minimal, `--radius` 8/10/14px. | Zen garden is quiet and *indoor*: a misted stone surface with no sky, no light source and no perspective. This kit is outdoors, midday, saturated and sunny — and deliberately glossy where zen-garden is matte. If zen-garden is a rainy courtyard, this is a field in July. |
| `glass` | light, translucent, `--blur` load-bearing | `glass` is restrained pastel over a flat rose/lilac/mint/sky ramp with **no specular band at all**. This kit's ground is a landscape and its glass carries a hard-edged band. |
| `dark-glass` | the same material, dark pole | near-black ground, light ink, no specular band. Different polarity, different rim logic, different motifs. |

## Contrast — measured, not asserted

The ground is a drawn scene with a sun bloom over it and glass over that, so no single flat hex
proves anything. Three bounds are measured:

- **The darkest field pixel: `rgb(148,186,117)`, L 0.4270.** Sampled from the rendered page across
  769,824 gutter pixels (two 108px strips × the full 3,564px document). That pixel is a *shade
  of a mown swath* — the 1st percentile is L 0.4527 and the median is L 0.5034 — but a
  caption can land on one, so it is the number the whole table is solved against.
- **The darkest *declared* ramp stop: `#9fc67a`, L 0.4916** (the page foot). The drawn scene is
  12% darker than the stop the ramp itself declares, which is exactly why grading against the
  declared stops alone would have been wrong.
- **The sky under the masthead: `rgb(197,228,240)` at its most saturated down to `rgb(237,247,253)`
  in the wash's hotspot.** That is the easy case for dark ink — `--text` measures 12.58:1 and
  15.46:1 across it — and it is where the h1, the eyebrow and the swatch captions sit.

### Required pairs — graded against the darkest field pixel

| Pair | Foreground | On `rgb(148,186,117)` | Target |
|---|---|---|---|
| body text | `--text` `#091f30` | **7.63:1** | ≥ 7:1 ✓ |
| secondary text | `--text-muted` `#1d3b52` | **5.30:1** | ≥ 4.5:1 ✓ |
| tertiary text | `--text-dim` `#24425a` | **4.77:1** | ≥ 4.55:1 ✓ |
| accent as text | `--accent-ink` `#053c63` | **5.20:1** | ≥ 4.5:1 ✓ |
| status ok | `--ok` `#094526` | **5.05:1** | ≥ 4.5:1 ✓ |
| status warn | `--warn` `#583700` | **4.86:1** | ≥ 4.5:1 ✓ |
| status danger | `--danger` `#7d1526` | **4.75:1** | ≥ 4.5:1 ✓ |
| status info | `--info` `#06406e` | **4.85:1** | ≥ 4.5:1 ✓ |
| focus ring | `#053c63` | **5.20:1** | ≥ 3:1 ✓ |
| button label | `--text-invert` `#ffffff` | on `--accent` `#0d6db3` → **5.45:1** | ≥ 4.5:1 ✓ |

**Worst pair in the kit: `--danger` `#7d1526` on the darkest field pixel at 4.75:1** (target
4.5:1). It is `.btn-danger`'s label and the invalid-field hint, both of which sit on bare grass
with no panel behind them.

### Composited pairs — glass over grass, tints over glass

`--surface` (46% white) over the darkest field pixel composites to `#c5dab4` (L 0.652);
`--surface-2` (58%) to `#d2e2c5` (L 0.722). Both are graded against that composite, not against
white:

| Pair | On a card | On `--surface-2` |
|---|---|---|
| `--text` | 11.23:1 | 12.34:1 |
| `--text-muted` | 7.80:1 | 8.57:1 |
| `--text-dim` | 7.02:1 | 7.71:1 |
| `--accent-ink` | 7.66:1 | 8.42:1 |
| `--ok` | 7.43:1 | 8.16:1 |
| `--warn` | 7.16:1 | 7.87:1 |
| `--danger` | 7.00:1 | 7.69:1 |

Badge and secondary-button labels sit on a **14% accent tint composited over the glass**, not on
the tint's declared value: `--accent-ink` on `accent-soft`/`--surface` = **6.49:1**, on
`accent-soft`/`--surface-2` = **7.07:1**.

The avatar's white monogram is the reason the progress fill is not brighter: 10% white over
`#0f6aa8` = **4.72:1**, 14% over `#0b4f80` = **6.01:1**, 14% over the green foot `#116b48` =
**4.79:1**.

`verify-lab.cjs` re-checks this independently by sampling the real pixel behind each rendered text
box; its tightest sampled pair is `.btn-secondary` at **5.57:1**.

## Signature motifs

Three, each doing a different job, each drawn as base64 inline SVG (a sphere and a teardrop are
organic forms; nested radial rings read as a bullseye, so gradients cannot do them). They are
unchanged by the ground rework — that is the point of moving them off the wallpaper.

Non-flatness is measured on the **rendered** 168×72 tile at 1×, per channel:

| Token | Job | Drawn | σ R/G/B | Luma range |
|---|---|---|---|---|
| `--frutiger-aero-bubble` | a **sphere** — rim, body gradient, one hard-edged specular | 3 bubbles at 56/36/24px over a sky base | **17.7 / 9.8 / 4.5** | 0.320–1.000 |
| `--frutiger-aero-droplet` | a **teardrop** — different silhouette, caustic pooled low in the bulb | 3 droplets at 48/28/22px over a grass base | **23.1 / 11.9 / 20.6** | 0.332–0.989 |
| `--frutiger-aero-horizon` | a **plane** — sky over grass with a hard specular line *on* the horizon | 3 CSS layers, two hard stops | **25.4 / 10.4 / 51.3** | 0.575–0.998 |

For scale, the same box painted with the tile base alone measures σ **0.4**. All three are 17–51
units of per-channel deviation, so every tile survives the "empty chip" failure on its own.

The bubble's rim is deliberately **split**: bright on the lit (upper-left) arc, weightier and
darker through the lower-right. A uniform outline reads as a sticker. Each sphere carries exactly
one light source, and the droplet is lit differently again — the light rims its upper-left and the
caustic pools low in the bulb, where a droplet actually concentrates it.

## Trade-offs and deviations

- **The inks are deeper than a pale-ground kit would need, and that is the cost of the field.**
  `--text` went `#10334f` → `#091f30`, `--text-dim` `#3a5872` → `#24425a`, `--ok` `#0f6b3d` →
  `#094526`, `--danger` `#b0203c` → `#7d1526`. The hierarchy is carried by `--text` /
  `--text-muted` / `--text-dim` (0.013 / 0.040 / 0.050 in relative luminance) plus weight, rather
  than by lightness alone — on a mid-tone ground there is far less room to spread three tiers.
- **`--ok` is a forest green, not a "success" green.** On grass, a cheerful green is invisible by
  definition. The chip that can be read wins.
- **The glass is denser than glass purists would like.** 46% white is a real cost to the
  "you can see the scene through it" effect; at 34% the panel read as a tint on the field rather
  than a surface above it, which is the worse failure at this ground luminance.
- **The mown texture is faint on purpose.** It reads as mowing at 1×, not as a pattern: eight
  broad swaths and a grain far below text contrast. Making it louder made the field compete with
  the content, which is exactly what a ground must never do.
- **`.card-elevated` carries no band** — the shared lab reads `--surface-2` for it, and a band on
  `--surface-2` would band every input, badge, alert and code block. Shown honestly rather than
  worked around.
- **`--check-appearance` is deliberately not declared.** The contract gives one switch that
  squares the checkbox *and* the radio; squaring the radio to get a square checkbox trades a
  correct control for an incorrect one. The kit takes the browser's own rendering with
  `accent-color` = the azure and sets only `--check-radius: 6px`.
- **`--btn-shadow` is insets only.** Four of the five button variants are transparent, and a cast
  shadow on a transparent box is a grey blob with no plate under it. The bevel is inner light on
  all variants; the cast shadow lives on `--glow` and on the panels.
- **The gallery preview will show sky, not the landscape.** `tools/build.py` paints `--bg` into a
  118px-tall preview box, and the artwork is anchored at `570px` for a 3,564px document, so the
  chip shows the top of the sky ramp and the sun's upper glow only. **The lab page is the
  reference view** — the preview is a colour chip, and no single-layer token can be both a page
  ground and a thumbnail.
- **Two independent visual passes were wrong about this kit before, and the numbers settled it.**
  An unprimed look reported "no bright band, no hard edge" on a panel whose pixel profile is
  unambiguous, and later saw "soft flat bands" where the render measures a 0.107 luminance step.
  Presence-of-a-place, though, is exactly what a look *can* answer. Three independent readings of
  the page agreed the ground reads as **sky → haze → rolling hills**, and a 1:1 crop of the field
  shows the mown swaths; the swaths are the first thing to fade in a whole-page view scaled down to
  thumbnail size, which is the price of keeping a ground quiet.

## Verification

From the repo root:

```bash
python tools/build.py --only frutiger-aero --no-export --no-lint
KIT_SHOTS="$LOCALAPPDATA/Temp/frutiger-aero-shots" node tools/verify-lab.cjs frutiger-aero
```

Result: **`PASS  frutiger-aero`** — 0 errors, 0 warnings, 0 missing tokens, 0 console errors, no
contrast failures (the harness reads computed styles, samples the real pixel behind each text box,
and composites the translucent stack). `verdict.json` is in `$KIT_SHOTS`.

`npx -y -p @google/design.md designmd lint kits/frutiger-aero/DESIGN.md` → **0 errors, 10 warnings
+ 1 info**, documented below.

## Linter

| Count | Rule | Why it stays |
|---|---|---|
| 8 | `broken-ref` — `'borderColor' is not a recognized component sub-token` | The rim is the substance of this kit: a white hairline is invisible on a sky and twice invisible on grass, which is why every pane's edge is a blue line. `borderColor` is not in the vocabulary, so the eight uses are recorded as warnings and the rim is written up in prose under *Colors* and *Elevation & Depth*. |
| 2 | `contrast-ratio` **false positive** — `#053c63` on `#0d6db324` reports 2.10:1 | `badge-accent` and `nav-item-active`. The linter compares the ink to the un-composited 14% tint, so it effectively measures the ink against itself. Composited over a card the pair measures **6.49:1**; over `--surface-2`, **7.07:1**. |
| 1 | `token-summary` (info) | 35 colours, 7 type scales, 4 radii, 5 spacing tokens, 42 components. |

Zero **errors**, and **no `orphaned-tokens`** — every declared colour is referenced from at least
one component.

## When to use

Consumer software and device-adjacent marketing, playful dashboards and onboarding, media and
lifestyle products, game launchers — anything that should feel bright, glossy and friendly rather
than severe, and anything that wants to feel *outdoors*.

It is a **light** kit: do not use it for dark-mode shells or dense data work that wants a neutral
ground, and do not use it behind long-form text if the panels can be made opaque — the field is
the point, so a page that hides it wastes the kit. For print, email or canvas, use
`--frutiger-aero-meadow` (the opaque ground) rather than the layered `--bg`. Avoid it anywhere
`backdrop-filter` is unavailable: without the frost this is a pale green page with glass drawn on
it.

## What the lab could not express

Honest list, per the brief's report-back rule — none of it was worked around by editing the lab:

- **A per-variant button shadow.** `--btn-shadow` reaches every variant at once, so a kit whose
  secondary/ghost/danger variants are transparent cannot give its *filled* variants a cast shadow
  without floating a grey blob under the transparent ones. `--glow` covers `.btn-primary` only,
  which is why the primary button's cast shadow lives there and every other variant gets an inset
  bevel.
- **A separate specular token for `.card-elevated`.** The lab reads `--surface-2` for it, and
  `--surface-2` also backs every input, badge, alert and code block — one token cannot carry a
  hard-edged band on the raised panel without banding all of those too.
- **A display *weight* hook now exists, and this kit leaves it unset.** `--weight-display` was
  added after an earlier report from this kit, so the original gap is closed and the entry is kept
  here only for the record. The ground rework did not touch the display voice: 700 is what the
  panel proportions, tracking and the specular band were solved against, and changing it would be
  a different piece of work with its own measurements. Stated as a scope decision, not a
  limitation — and not claimed as a finding.
- **No hook for `background-attachment` / per-section grounds.** The scene is one image layer
  sized in px, which is what makes the horizon land at a fixed height — but there is no way to
  give, say, the footer a different part of the same landscape.

## IP

**No Microsoft trade dress.** There is no Windows logo, no window chrome copied from a
screenshot, and no Vista/7 branding or UI text anywhere in this kit. The vocabulary is generic
optics and generic landscape — glass, a specular band, a bubble, a droplet, a horizon, a mown
field — and the kit is named by the aesthetic's established *community* name, not a product name.

**The typeface is not Frutiger.** The real Frutiger is a commercial Linotype licence and this
repository is public, so the kit ships **Hind**, a Frutiger-adjacent free humanist sans, with
`"Frutiger"` present only as a *system fallback string* inside the font stack — never as a Google
Fonts request.
