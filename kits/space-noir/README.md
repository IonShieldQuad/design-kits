# Space Noir

**A 90s space-noir jazz poster, a decade after the ink dried.** A warm charred-black ground, bone
type, one burnt-orange action, a muted deep teal counterpoint, film grain and a halftone screen —
flat, grainy, cinematic, and deliberately the *muted* half of the retro-anime pair.

- Kit: `space-noir` · order `175` · mode `dark`
- Fonts: Barlow Condensed · Barlow · Courier Prime
- Tags: `dark` `retro` `poster` `noir` `print` `cinematic`
- Source: **original**, from the era's design language. Design provenance: *'90s space-noir anime /
  jazz poster*. No character, ship, logotype, poster artwork or trade dress is reproduced — the kit is
  named for the genre, and every device in it (inked ground, film grain, halftone screen, interlocking
  discs, perforated film strip) is generic mid-century / jazz-poster print vocabulary.

## Stance

Most "retro anime" kits reach for saturation — neon, pastel, sunset. This one goes the other way: it
looks like a **printed poster that has been through a press and thirty years of light.** The palette
is deliberately desaturated, the ground is warm rather than neutral, and the material is *grain and
halftone* rather than a colour. It is the cinematic, adult register of the era — closer to a jazz
album cover than to a terminal or a HUD.

The one architectural commitment is that **the kit is print, not glass**: no blur, no bloom, no
`backdrop-filter`, and every shadow a hard zero-blur offset. Smoothness is shut out where it would be
visible, and the kit says so rather than faking it.

## Key choices

- **The ground is warm, not neutral.** `#221e1a → #121110` is a *brown-black* — printed stock ages
  warm, and a neutral `#0b0c10` would flatten the whole thing into a modern dark UI.
- **The action colour takes ink, not cream.** `#c06a30` with a near-black label (`#191210`, 4.7:1) is
  the jazz-album move and the stronger read; cream on the orange only reaches 3.6:1. Using `--text-invert`
  as ink is what makes the primary button look printed.
- **Enabling grain that only darkens.** The `--bg` grain is a drawn `feTurbulence` tile whose colour
  matrix maps luminance to *black* alpha, so the layer can only lower luminance. Every contrast pair is
  therefore graded against the ungrained ground and stays conservative — the image layer on `--bg`
  cannot quietly break a number.
- **The ground is printed stock, not a smooth ramp.** `--bg` stacks the drawn **halftone dot screen**
  over the film grain over the warm ink ramp, so the page itself shows the screened tooth of a press
  rather than a fading gradient. Both image layers are composed of near-black marks and only *darken*,
  which is why every ratio below is still solved against the lightest (ungrained, unscreened) ground.
- **The masthead wash is a screened shadow, not a bloom.** The lab's default is a radial
  `--accent-soft` glow; a noir masthead wants the opposite. `--wash` is a drawn screen of near-black
  dots, which only darkens, so the masthead's eyebrow and meta text are not put at risk.
- **Halftone is drawn, not simulated.** A repeating radial gradient fakes a dot screen as a smooth
  ramp; the brief calls this out by name. `--space-noir-halftone` is base64 SVG circles whose radii grow
  left to right — a real screened gradient.
- **`--accent-ink` exists** (`#e0904f`) because `#c06a30` is a fine *fill* but only ~4.7:1 as a small
  label, and less on its own tint. Eyebrow, links, active nav and badge/secondary labels route through it.
- **Courier Prime, not a techy mono.** The kit's small-print voice should read as a typewriter legend
  on a printed poster, not as a terminal.

## Contrast — measured, not eyeballed

WCAG ratios computed from the declared hexes; the *binding* ground for a dark kit is the **brightest**
stop. The brightest bg stop is `#221e1a`; `--surface-2` (`#151311`) and `--surface` (`#1e1a17`) are
slightly darker, so the worst case is always against `#221e1a`.

| Pair | Measured | Ground | Required | |
|---|---|---|---|---|
| `--text` `#ece4d6` | 13.11:1 | `#221e1a` (brightest bg) | 7.0 | ✅ |
| `--text-muted` `#bdb3a4` | 8.00:1 | `#221e1a` | 4.5 | ✅ |
| `--text-dim` `#9c9284` | **5.41:1** | `#221e1a` | 4.55 | ✅ |
| `--accent-ink` `#e0904f` | 6.52:1 | `#221e1a` | 4.5 | ✅ |
| `--accent-ink` on accent-soft over `--surface` | 5.61:1 | comp `#38271b` | 4.5 | ✅ |
| `--accent-ink` on accent-soft over `--surface-2` | 6.11:1 | comp `#302116` | 4.5 | ✅ |
| `--accent-ink` on accent-soft over `#221e1a` | 5.39:1 | comp `#3b2a1e` | 4.5 | ✅ |
| `--text-invert` `#191210` on `--accent` | 4.71:1 | `#c06a30` | 4.5 | ✅ |
| `--text-invert` on `--accent-hover` | 6.14:1 | `#d67f42` | 4.5 | ✅ |
| `--text-invert` on `--fill-bg` `#cc6f2e` | 5.18:1 | fill stop | 4.5 | ✅ |
| `--ok` `#8fae5f` | 6.61:1 | `#221e1a` | 4.5 | ✅ |
| `--warn` `#d9a441` | 7.36:1 | `#221e1a` | 4.5 | ✅ |
| `--danger` `#cb7266` | 4.84:1 | `#221e1a` | 4.5 | ✅ |
| `--info` `#5c9d97` | 5.30:1 | `#221e1a` | 4.5 | ✅ |
| `--focus-ring` `#e0934f` | 6.67:1 | `#221e1a` | 3.0 | ✅ |

**Worst pair:** `--text-invert` on `--accent` at **4.71:1** (ink label on the burnt-orange fill). The
worst *ground-bound* pair is `--text-dim` at **5.41:1** against `#221e1a` — both clear their floors.
`--accent-2` (teal `#2f6f68`) is a **media / fill** token and clears 3:1 for graphical objects, but it
is never used as text; `--info` (`#5c9d97`) exists as the readable teal for that.

## Signature motifs

Three, three different jobs, each proven non-flat and read cold (the drawn SVGs render on `--surface-2`,
the tile base):

1. **`--space-noir-halftone`** — the *material*. A drawn halftone screen whose cream dots grow left to
   right. Reads cold as a halftone dot screen, not a blur. Drawn (base64 SVG): a dot screen is not
   expressible with a repeating gradient without reading as a smooth ramp.
2. **`--space-noir-discs`** — the *poster geometry*. Two overlapping discs (orange + teal), cream-ringed,
   each with a centre dot, over a bold baseline rule. Reads cold as interlocking/overlapping discs — a
   poster device, deliberately generic, not a mark.
3. **`--space-noir-film`** — the *frame*. A perforated film strip: two rows of cream sprocket holes,
   hard frame dividers, a crisp cream edge. Reads cold as a film strip.

A fourth idea (a bold poster frame / corner bracket) was **cut**: it reused the film strip's edge device
and diluted the three that have distinct jobs. Three is the cap here.

## Trade-offs

- **The burnt orange is a mid tone, not a deep one.** A deeper burnt orange cannot carry a cream label
  at 4.5:1 in both its resting and hover states, so the kit takes the jazz-album route instead: a
  mid-orange field with an *ink* label. `--accent-2` (teal) is a fill/media token only and is never text.
- **Grain *and* halftone live on the ground; the media panel gets the fuller press.** `--bg` carries
  both the film grain and a halftone dot screen (the printed stock); the media panel layers that
  halftone over a muted orange→rust→teal press ramp. Both are drawn, and both ground image layers are
  darkening-only, so no contrast pair is risked by them (see above).
- **No `kit.css`.** The kit needed no construction the tokens could not carry — the hard offset, the
  screened wash, the recessed input and the halftone fields are all token values, which is the intended
  outcome.

## When to use

Cinematic, adult, poster-grade branding: music and film pages, album and event covers, editorial
features, portfolios that want a printed 90s glance rather than a neon night or a pastel morning.
Avoid it for anything that must feel bright, playful, clinical or trustworthy-at-9am — for the neon
half of the same decade, use `synthwave`; for the light, sweet half of the anime pair, use the shoujo
(pastel) kit.
