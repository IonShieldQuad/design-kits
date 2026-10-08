# Retro Anime

**Nineties shoujo magical-girl anime, as a design language.** A cream/ivory sky cooling toward
lavender, deep navy ink, a blush rose for action and a sky blue for structure, and a flat
cel-animation gold as the trim — with a crescent moon, a shoujo sparkle, a ribbon bow and a
starfield drawn in the flat cel-shaded fills of the era.

- Kit: `retro-anime` · order `170` · mode `light`
- Fonts: Shippori Mincho · Nunito Sans · IBM Plex Mono
- Tags: `light` `retro` `anime` `shoujo` `celestial` `pastel`
- Source: **original** — "90s shoujo magical-girl anime" as *design provenance*, not a franchise

## Provenance (this repo is public)

The register is an **era's design language** — cel shading, high-key pastel key art, celestial
iconography, gold trim — and the kit is named by genre, not by any series. Every motif is generic
vocabulary anyone may draw: a **face-free crescent moon**, a **four-point sparkle** (concave
geometry, not a five-point star), a **ribbon bow** and a **starfield**. There is no character's
face, no title logotype and no recognisable costume anywhere in it.

## What this kit is not

Two kits in this library are the obvious places for `retro-anime` to drift, and it is built to
avoid both:

| kit | register | signature | how `retro-anime` differs |
|---|---|---|---|
| `kawaii` | sticker-cute, **playful** | pink/lilac/mint pastels, 12–28px radii, pills on every control, a bouncy overshoot ease, confetti/hearts | retro-anime is **romantic and celestial**: 5–14px radii, pills on badges only, a calm ease, an elegant Mincho display, navy ink — and its motifs are **cel-shaded** (hard two-tone fills and crisp outlines), not stickers |
| `tropical-breeze` | pastel **beach** | sand/sea/turquoise, coral action, a palm frond, a parasol | retro-anime is a **night sky in daylight**: navy, rose and sky-blue; a crescent, sparkles and a ribbon. No warm terra, no plant life, no sun-on-water |
| `city-pop` | 80s **Tokyo daylight** | airbrushed cream/coral/teal sleeve art, 5–16px radii | city-pop is *airbrushed and smooth* (soft blur, a printed sleeve); retro-anime is *flat and cel* — a hard second tone, zero-blur offsets, a hard creased ribbon |

It is also the library's **only celestial** kit — nothing else owns a moon, a starfield and a
night sky as its signature.

## Contrast — measured, not eyeballed

A light kit's binding ground is the **palest** one, so every ink was graded against `--surface`
(`#fffdf8`, pure `#ffffff` never appears) **and** every `--bg` stop, and the accent badge was
graded against its own `--accent-soft` tint **composited** over each ground. Script-computed; the
masthead wash is included, which is why the wash itself had to be dialled back (see below).

| pair | ground | measured | target |
|---|---|---|---|
| `--text` `#1e2749` | `--surface` `#fffdf8` | **14.33:1** | ≥ 7 |
| `--text` | worst `--bg` stop | 12.87:1 | ≥ 7 |
| `--text-muted` `#414c72` | `--surface` | 8.26:1 | ≥ 4.5 |
| `--text-muted` | `--surface-2` `#f5eef4` | 7.36:1 | ≥ 4.5 |
| `--text-dim` `#49547b` | `--surface` | 7.28:1 | ≥ 4.55 |
| `--text-dim` | `--surface-2` | 6.49:1 | ≥ 4.55 |
| `--text-dim` | worst `--bg` stop | 6.54:1 | ≥ 4.55 |
| `--accent-ink` `#ae2a5e` | `--surface` solid | 6.27:1 | ≥ 4.5 |
| `--accent-ink` | `--surface-2` solid | 5.59:1 | ≥ 4.5 |
| `--accent-ink` | own 14% tint over `--surface` (composited `#fbebf1`) | 5.15:1 | ≥ 4.5 |
| `--accent-ink` | own 14% tint over `--surface-2` (composited `#eed5e0`) | **4.63:1** | ≥ 4.5 |
| `--accent-ink` | own 14% tint over the worst `--bg` stop | 4.66:1 | ≥ 4.5 |
| `--accent-ink` | worst masthead-wash composite | 4.70:1 | ≥ 4.5 |
| `--text-invert` `#fff8f0` on `--accent` `#c53a68` | — | 4.77:1 | ≥ 4.5 |
| `--text-invert` on `--accent-hover` `#b2335e` | — | 5.65:1 | ≥ 4.5 |
| `--ok` `#1f7a5a` | `--surface-2` | 4.62:1 | ≥ 4.5 |
| `--warn` `#8f6410` | `--surface-2` | 4.61:1 | ≥ 4.5 |
| `--danger` `#bd3a22` | `--surface-2` | 4.86:1 | ≥ 4.5 |
| `--info` `#2b6fb5` | `--surface-2` | 4.55:1 | ≥ 4.5 |
| `--focus-ring` `#2f6fc0` | worst ground `--surface-2` | 4.43:1 | ≥ 3 |

**Worst pair in the table: `--accent-ink` on its own `--accent-soft` tint composited over
`--surface-2` — 4.63:1** (target 4.5), on `#eed5e0`. That is the composite the accent badge
actually renders, and the node the whole kit is closest to the floor at. `verify-lab.cjs`
composites the real DOM stack and reports **0 contrast errors**.

Two consequences worth stating:

- **The fill is deep, the tint is pale.** `#c53a68` is the *action* rose; the *blush* is only the
  14% `--accent-soft` tint and the motif tiles. A pastel-pink button would be ~2.6:1 as a label and
  could not carry the cream `--text-invert` — so the rose is deep and the label is cream.
- **`--accent-soft` is a tint of the accent, not a hand-picked pink** — written
  `rgba(197,58,104,.14)` so it can only ever be the rose.

## The four signature motifs

Each does a **different job** — emblem, glint, object, field — and each carries its own base layer
so no tile is a flat plate. All four are **drawn** inline SVG (base64 — never hand-percent-encoded,
which double-encodes `#` and fails silently as a blank tile). Non-flatness was measured the way the
brief asks: each token rendered as `background:` on a **168×72** box, screenshotted in headless
Chromium, per-tile pixel standard deviation read with PIL.

| token | job | std-dev (max ch) | grey |
|---|---|---|---|
| `--retro-anime-moon` | the **emblem** — a face-free crescent, hard cel two-tone | **38.56** | 34.99 |
| `--retro-anime-sparkle` | the **glint** — a concave four-point shoujo sparkle burst | **44.09** | 36.68 |
| `--retro-anime-ribbon` | the **object** — a bow with a hard crease and swallowtail tails | **66.85** | 57.78 |
| `--retro-anime-starfield` | the **field** — a tileable four-point star scatter | **52.14** | 47.67 |

None is a flat plate (a flat tile measures ≈ 0). Each was also **looked at cold**, with no label:
the crescent, the sparkle, the bow and the starfield were each identified correctly by a fresh
observer, and each tile's non-flatness was read from the real render rather than assumed.

- **The crescent was redrawn twice.** The first version (an outer circle minus an offset circle,
  `fill-rule: evenodd`) rendered as a **fat blob / annulus** at tile size — the bite never read.
  The shipped version is **two arcs meeting at two horn tips** (an outer arc bulging left, an inner
  arc carving the bite), which reads as a crescent at 62px. Its lit/shadow split is a *hard straight
  edge* applied through a clip — i.e. cel shading, not a second offset shape (a first attempt with
  an offset gold crescent read as a **stray duplicate outline** and was cut).
- **The sparkle was strengthened twice, on measurement.** The first blush-on-blush version
  measured **26.8** max-channel and read washed out at tile size; deepening the field and adding a
  rose outline lifted it to 40.7, and the shipped version — a *saturated* blush field with ink
  outlines, a white outer star and a gold inner star — measures **44.1** and carries real punch.
  The lesson is the brief's: a motif tuned for subtlety over a pale ground renders as an empty
  chip, so the sparkle's field is the one place the kit is deliberately saturated.
- **The ribbon carries the cel crease.** Each loop is split by a straight **fold line** (the lower
  leaf one tone darker), with a hard specular on the upper leaf — a fold, not a blur. A first
  version laid the dark tone as a generic inner shadow and read as a flat, crease-less bow.
- **Four is the ceiling.** The genre tempts a fifth shape (a wand, wings, a heart locket); a fifth
  tile only dilutes the four that identify the kit.

## Key choices

- **Cel shading is the depth cue, and it is enforced everywhere.** Depth is a hard **zero-blur**
  offset (the *cel plate*: `4px 4px 0` / `6px 6px 0` in a cool navy-shadow tone), a **two-tone
  fill** with a hard break, and crisp **2px navy outlines**. `--blur: none` and there is no soft
  drop shadow in the kit; `--glow` is a hard rose ring stacked on the same offset, not a bloom.
- **Rose is action, sky is structure.** The rose `#c53a68` is the only fill that acts (buttons,
  toggle, check); the sky `#3f7fd0` owns media, progress, focus and charts, and is *never a label*
  (3.6:1). The gold `#a87d2a` is trim only — a rule, the ribbon knot, the lit star.
- **The ink is navy, never grey.** A grey on a cream page reads as an office document; the whole
  premise is a night sky, so `--text` is `#1e2749`.
- **The danger red is held off the rose by hue, not by hope.** A first cut at `#c0392f` sat only
  24° from the rose and read as a second accent; the shipped `--danger` `#bd3a22` is a vermilion
  **29°** away, so a destructive action never reads as the action colour (and it clears 4.86:1).
- **The masthead wash was dialled back on measurement.** At the first `rgba(197,58,104,.12)` /
  `rgba(63,127,208,.14)` the composited ground dropped `--accent-ink` to **4.11:1**; shipped at
  `.07` / `.08` it holds **4.70:1** and still reads as a blush-plus-sky glow.
- **The media panel is the night.** `--media-bg` is a drawn navy sky — a hard cel cloud band, a
  crescent and a starfield — at `--media-op: 1`, so the light page gets one big celestial moment.
- **`--fill-bg` is navy** (progress + avatar), so cream initials clear 12:1 and the progress bar
  reads as a night bar on a cream page.
- **No `kit.css`.** Everything is a token — colours, radii, four drawn motifs, the cel offsets on
  every bar and button, the recessed input, the fill, the night media, the wash. No construction
  needed one.

## Trade-offs

- **The rose cannot be pastel.** A blush pink strong enough to look "shoujo" is only ~2.6:1 as a
  label and cannot carry a cream label as a fill, so the working action is a deep rose and the
  blush lives in the tint and the motif tiles. That is the whole fill-vs-label split in one line.
- **`--accent-2` (sky `#3f7fd0`) is structural only** — media, progress, avatar, charts. It is
  3.6:1 at worst, so it is never used as a small label; the inked sky that does read (`--info`
  `#2b6fb5`) is a separate status token.
- **Gold is trim, not ink.** `#a87d2a` clears 3:1 as a graphical object (a rule, a star) on every
  light ground, but it is **not** a text colour — the inked status gold is `--warn` `#8f6410`.
- **Four motifs is the ceiling in this genre.** A fifth (a wand, wings, a heart locket) dilutes the
  four that identify the kit; the library's own `kawaii` cut a fourth for the same reason.
- **The media panel's scene is described in prose, not in a component key.** DESIGN.md's component
  sub-keys are whitelisted and `backgroundImage` is not among them, so `card-media` declares the
  night navy as its `backgroundColor` and the drawn crescent-and-starfield panel is documented in
  the overview and the `--media-bg` comment instead. No capability was missing — this is a
  documented limit of the spec's component keys, not of the token contract.
- **Nothing was left unexpressed.** The kit needed no `kit.css` and no lab change; every effect,
  including the four motifs and the cel offsets on the nav and toggle, is a token.

## When to use

Retro-romantic and magical: fan and fandom pages, game and visual-novel UI, zine and event
branding, seasonal or character-themed promo, and anything that should feel like a 90s shoujo
title card. It is a **light, decorative** kit — reach for it when the page should feel *romantic
and celestial*, not calm or clinical.

Avoid it for anything that must read as sober, trustworthy or clinical — that is `quiet`, `carbon`
or `glass`. For pastel that is **playful** rather than romantic, use `kawaii`; for pastel that is
**coastal**, use `tropical-breeze`; for the same nostalgia as **neon night**, use `synthwave`.
