# Retro Anime

**Eighties anime key art, at the hour the neon comes on.** Indigo night as the ground, the
sunset as a band across the top of the page, magenta for action, cyan for technology, and one
striped sun.

- Kit: `retro-anime` · order `125` · mode `dark`
- Fonts: Audiowide · Rajdhani · Share Tech Mono
- Tags: `dark` `retro` `anime` `neon` `synthwave` `city-pop`
- Source: five reference illustrations supplied by the user (city-pop / 80s-anime / outrun sunset
  key art)

## Sampling — the palette is measured, not estimated

Each reference was opened at full resolution and mined with a script that converts to HSV, keeps
the strongly-saturated and luminous pixels (the neon), and takes the **median colour within each
hue band**. That produces a per-image palette; the kit uses the median *across* the five.

| Image | violet | magenta | cyan | gold | dark ground | sun peak |
|---|---|---|---|---|---|---|
| cyborg on the beach | `#632c7c` | `#a44078` | `#44a6be` | `#f69f71` | `#1e1526` | `#fed58a` |
| neon seaside café | `#6d3aca` | `#d456ca` | `#0dbcf9` | — | `#0b092b` | — |
| sailor-fuku at dusk | `#5f2580` | `#af4385` | `#4ca4c6` | `#faa071` | `#191532` | `#ffad7b` |
| mecha and schoolgirl | `#59157f` | `#c5378c` | `#4ab3d7` | `#fba175` | `#21162d` | `#ffb583` |
| "Synthetic Dawn" poster | `#623aa7` | `#bb376d` | `#43a1e0` | `#fbb26c` | `#100d20` | `#ffbb77` |
| **kit value** | sky `#622c80` | `#ec4b8f` (driven) | `#44a6d7` | `#ffb57b` | night `#19152b` | — |

Five independent images converge on the same bands, which is why the palette is trustworthy:
violet ≈ `#622c80`, magenta ≈ `#bb4085`, cyan ≈ `#44a6d7`, gold ≈ `#faa071`–`#ffb57b`, and a
near-black that is **violet** (`#19152b`), never neutral grey.

## Key choices

- **The night is violet, not black.** Every reference's darkest mass is an indigo-violet. A
  neutral `#0b0c10` would have killed the warm/cool tension the genre runs on.
- **Magenta is action, cyan is technology.** The references give cyan to *machines* — eyes, suit
  circuitry, screens, grid — and magenta to *atmosphere and signage*. The kit keeps that
  assignment, which is why the focus ring is cyan rather than magenta.
- **Gold never becomes a control.** `#ffb57b` is the sun. It appears in `--retro-anime-sky` and
  in `--warn`, and nowhere that asks the user to click.
- **`--accent-ink` exists** (`#ff9cc4`) because `#ec4b8f` is 5.2:1 as a *fill* label but only
  ~2.9:1 as a small label on the night. Eyebrow, links, active nav and badge labels route
  through it.
- **`--text-dim` is `#c2b2df`, not a mid-lavender.** Measured against *every* ground including
  the sky band's brightest stop: the first attempt hit 4.40:1 on `#622c80` and was lifted.
- **No glass, no blur, no chamfer.** A poster is flat and printed; `--blur: none`, `--cut: 0px`.
  Depth comes from neon glow and near-black indigo drops.
- **The sunset is px stops**, so the band lands inside the first viewport and the page settles to
  night below it. `%` stops over a 3000px document would have shown one flat colour.
- **The page's horizon stop is a *dark* warm brown** (`#6e3520`), not the sampled gold. Gold at
  `#ffb57b` under body text fails badly; a dark warm stop still reads as a horizon band between
  the violet sky and the night, and every contrast pair survives it (verified, not assumed).
- **Corners are 3–10px, not round.** Printed geometry, softened at the edge only.

## The four signature devices

These are the genre's actual vocabulary, all built from sampled stops:

- `--retro-anime-sky` — the sunset ramp: violet → magenta → gold at the horizon, px stops.
- `--retro-anime-sun` — **the outrun sun, drawn**: a gold-to-magenta disc with hard horizontal
  bars cut across its *lower half only*, widening as they descend. This had to be drawn (inline
  SVG): a `repeating-linear-gradient` stripes the whole tile, not the disc, so it read as
  "scanlines over a rectangle" rather than as a sun.
- `--retro-anime-grid` — **the perspective floor, drawn**: verticals converging on a vanishing
  point with a bright horizon line, and horizontals whose spacing widens toward the viewer. Two
  repeating gradients give parallel graph paper, which is why the first attempt read as flat.
- `--retro-anime-chrome` — the metal from the references' armour and crystalline wings. It reads
  as chrome because the ramp is **hard-banded with a dark band in the middle**; smooth stops read
  as fog.

A fifth motif (horizontal haze bands) was cut: it reused the sun's bar pattern in another colour,
so the two tiles competed instead of forming a system. Four is the ceiling.

## Trade-offs

- **The page cannot be the poster.** A UI cannot put body text on a saturated sunset, so the
  bright gold lives in the signature tokens and the sky band, and the working ground stays night.
- **Audiowide is single-weight.** It is display-only by design; headings use Rajdhani 600 rather
  than asking a 400-only face to pretend it has weight.
- **`--accent-2` is a media/fill token, not a label.** It clears 3:1 (WCAG 1.4.11, graphical
  objects) everywhere but not 4.5:1 on the violet band, and it is never used as text.
- **Two accents is the ceiling.** The genre tempts a third neon; that turns the night into a
  rainbow and loses the magenta-vs-cyan vibration.

## When to use

Night-time nostalgia with a heartbeat: music, media, streaming and game pages, event or album
branding, portfolios that want cinema rather than minimalism. Avoid it for anything that must
feel calm, clinical, trustworthy-at-9am or light — that is `quiet`, `glass` or `glorious-morning`.
For the same decade in daylight, use `summer-sunset`; for hardware rather than atmosphere, `cassette`.
