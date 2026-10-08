# Kawaii

**A pastel sticker sheet.** Bubblegum pink, lilac, mint and cream grounds; one candy accent; and a
shape language that is the real identity — huge radii, pills on everything, soft plum shadows, a
bouncy overshoot ease, and drawn sparkles, hearts and confetti.

- Kit: `kawaii` · order `160` · mode `light`
- Fonts: Baloo 2 · Nunito · JetBrains Mono
- Tags: `light` `pastel` `playful` `cute` `rounded` `sticker`
- Source: original

## What this kit is not

The library already had three light, soft kits, and none of them is *playful*:

| kit | register | signature |
|---|---|---|
| `sakura` | spring, elegant | saturated blossom pink vs living leaf green, a measured petal drift, 10–20px radii |
| `city-pop` | 80s Tokyo pastel, elegant | airbrushed cream/coral/teal sleeve art, 5–16px radii |
| `glorious-morning` | first light, energetic | dawn gold on clear sky, a soft-serif display, 8–18px radii |
| **`kawaii`** | **sticker-cute, playful** | **pink/lilac/mint pastels, 12–28px radii + pills, a bubbly rounded display, sparkles and hearts** |

Kawaii is *sweet*, not *pretty*. It is the only light kit here that rounds to 28px, the only one
whose controls are pills, and the only one whose motifs are stickers rather than natural
phenomena. If a screen built with it reads as tasteful and restrained, the kit has failed and you
wanted one of the three above.

## Contrast — measured, not eyeballed

Pastel grounds make `--text-dim` the hard token, and the binding ground is the **palest** one.
Here that is `--surface` at pure `#ffffff`, so every caption, hint and label was proved against
white — not against the pink stop that flatters the numbers. Every value was computed by a script
that composites translucent tints before grading (the `--accent-soft` badge case).

| pair | ground | measured | target |
|---|---|---|---|
| `--text` `#3b2743` | `--surface` `#ffffff` | **13.49:1** | ≥ 7 |
| `--text` | worst `--bg` stop `#eadffd` (lilac) | 10.58:1 | ≥ 7 |
| `--text-muted` `#5f4a68` | `--surface` | 7.88:1 | ≥ 4.5 |
| `--text-muted` | `--surface-2` `#fbeef7` | 7.00:1 | ≥ 4.5 |
| `--text-muted` | worst `--bg` stop `#eadffd` | 6.18:1 | ≥ 4.5 |
| `--text-dim` `#634e6c` | `--surface` | 7.40:1 | ≥ 4.55 |
| `--text-dim` | `--surface-2` | 6.58:1 | ≥ 4.55 |
| `--text-dim` | worst `--bg` stop `#eadffd` | 5.81:1 | ≥ 4.55 |
| `--accent-ink` `#ab1559` | `--surface` solid | 7.04:1 | ≥ 4.5 |
| `--accent-ink` | `--surface-2` solid | 6.26:1 | ≥ 4.5 |
| `--accent-ink` | own 16% tint over `--surface` (composited `#ffe8f3`) | 6.06:1 | ≥ 4.5 |
| `--accent-ink` | own tint over `--surface-2` (composited `#fcdaec`) | 5.49:1 | ≥ 4.5 |
| `--accent-ink` | own tint over worst `--bg` stop (composited `#edcdf1`) | **4.90:1** | ≥ 4.5 |
| `--text-invert` `#4a1738` on `--accent` `#ff6fb2` | — | 5.55:1 | ≥ 4.5 |
| `--text-invert` on `--accent-hover` `#ff86c1` | — | 6.41:1 | ≥ 4.5 |
| `--ok` `#0d7a57` | `--surface-2` | 4.74:1 | ≥ 4.5 |
| `--warn` `#946000` | `--surface-2` | 4.75:1 | ≥ 4.5 |
| `--danger` `#bd2d28` | `--surface-2` | 5.23:1 | ≥ 4.5 |
| `--info` `#4f52c9` | `--surface-2` | 5.52:1 | ≥ 4.5 |
| `--focus-ring` `#7d5bd6` | worst ground `#eadffd` | 3.80:1 | ≥ 3 |

**Worst pair in the table: `--accent-ink` on its own `--accent-soft` tint composited over the
lilac `--bg` stop — 4.90:1** (target 4.5), measured on `#edcdf1`. The badge the lab actually
renders sits on `--surface-2`, where the same composite is 5.49:1. The lowest *text* pair is
`--text-dim` on the same lilac stop at 5.81:1. `verify-lab.cjs` composites the real DOM stack and
reports 0 contrast errors.

Two consequences worth stating:

- **The fill is pastel, so the label is dark.** `--text-invert` is a deep berry `#4a1738`, not
  white. White on bubblegum `#ff6fb2` is 2.57:1 and would vanish; the dark-berry label is 5.55:1.
- **`--accent-soft` is a 16% tint of the accent, not a hand-picked pink** — written
  `rgba(255,111,178,.16)` so it can only ever be the accent. The `accent-tint` colour in
  `DESIGN.md` (`#fcdaec`) is its documented **composite over `--surface-2`**, which is the colour a
  badge actually shows.

## The three signature motifs

Each does a different job, and each carries its own base layer so no tile is a flat plate. All
three are **drawn** inline SVG (base64) — a concave four-point star, a rounded die-cut heart and a
dashed sticker border are geometry no gradient family produces.

Non-flatness was measured the way the brief asks: each token rendered as `background:` on a
168×72 box, screenshotted in headless Chromium, then per-tile pixel standard deviation read with
PIL.

| token | job | std-dev (R / G / B) | max channel | grey |
|---|---|---|---|---|
| `--kawaii-sparkle` | the "pop" mark — a drawn four-point star burst | 22.93 / **39.78** / 15.56 | 39.78 | 28.63 |
| `--kawaii-heart` | the affection mark — a die-cut sticker heart | 20.57 / **45.75** / 20.90 | 45.75 | 27.35 |
| `--kawaii-confetti` | the field — a tiled scatter of dots and tiny stars | **25.66** / 23.92 / 15.90 | 25.66 | 19.56 |

None is a flat plate (a flat tile measures ≈ 0). For reference, the kit's own `--bg` swatch — the
pastel ground itself, which is deliberately pale — measures 25.28 (max channel) / 22.31 (grey) at
92×41, so even the *ground* carries visible structure.

- `--kawaii-sparkle` — **the mark.** A four-point star burst, two satellite stars, a candy core
  and pastel dots, over a pink→lilac base with a soft white halo. Tuned against PIL std-dev: the
  first pale-base attempt measured 30.5 and washed out at tile size; this measures 39.8 and reads.
- `--kawaii-heart` — **the affection mark.** A rounded die-cut sticker heart (candy fill, white
  outline, specular highlight) plus a mini mint heart and a mini lilac heart, over a mint→cream
  base. A different *symbol* and a different *construction* from the sparkle: a filled shape with
  an outline, where the sparkle is points and lines.
- `--kawaii-confetti` — **the field.** A tiled scatter of dots, tiny four-point stars and a tiny
  heart at unequal sizes and colours, on its own cream ground. Texture you tile *behind* something
  rather than a mark you place — the third job.

A fourth candidate — a scalloped border strip — was cut: it reused the confetti's dot vocabulary
at another scale, so the two tiles competed instead of forming a system. Three is right here.

## Key choices

- **Roundness is the identity, not the colour.** Many kits are pastel; the differentiator is 28px
  corners and pills on every control. Checkbox and radio are rounded through the `--check-*`
  capability (`--check-appearance: none` plus a round box), because native controls ignore
  `border-radius` and would otherwise be the only square thing on the page. The **checked state is
  a filled candy box with no glyph** — the shape cue is the container, the state is the fill.
- **A bouncy ease.** `cubic-bezier(.34,1.56,.64,1)` overshoots, so controls pop. The other light
  kits glide; this one hops.
- **Dark ink on a pastel fill.** Stated above; it is the single most likely thing to get wrong when
  hand-editing this kit.
- **Plum-tinted shadows.** A neutral-grey shadow on a pastel page reads as grime.
- **The grounds were deepened once, on measurement.** The first pale ground measured ≈ flat as a
  92×40 swatch and read as "near-white" — the kit's whole premise was invisible in every preview
  strip. The shipped stops are visibly pastel and, because deeper grounds *raise* ink contrast,
  every pair still clears its target with margin.
- **`--media-bg` is the kit's own material**, not the default accent ramp: a pastel sticker sheet
  with a dashed white die-cut border, sparkles and a heart. `--media-op: 1` lifts the default `.85`
  dim, because a dimmed pastel is just a grey.
- **No `kit.css`.** Everything is a token — colours, radii, three drawn motifs, a shadow, a fill
  ramp, and the opt-in surfaces the lab honours. No construction was needed.

## Trade-offs

- **A pastel page cannot be vivid.** The saturated moments are the bubblegum button and the motif
  tiles; the working ground stays pale so body copy survives. There is no large colour moment on
  the page, by design.
- **`--accent-2` (mint `#35c79a`) is structural only** — media, progress, avatar, charts. It is
  2.15:1 on white and 1.91:1 on `--surface-2`, so it is never used as a label; the dark mint that
  does read (`--ok` `#0d7a57`) is a separate status token.
- **`--text-dim` at 5.81:1** is the tightest text pair; it clears 4.55 with margin but is the first
  thing to re-check if a ground stop ever deepens.
- **The checked control is colour-only.** The `--check-*` capability fills the box; there is no
  check glyph, because the spec's documented behaviour for a custom box is a filled state. If a
  glyph is required, that is a `kit.css` job and was deliberately not taken.
- **Three motifs is the ceiling.** The genre tempts a fourth sticker shape; that dilutes the
  sparkle and the heart, which are the two that identify the kit.

## When to use

Playful consumer and creator products: kids' and hobby apps, chat and community surfaces,
sticker/emoji tooling, achievement and reward UI, and marketing or landing pages that should feel
*fun* rather than premium. Avoid it for anything that must read as calm, clinical, trustworthy or
elegant — that is `quiet`, `glass`, `sakura`, `city-pop` or `glorious-morning`.