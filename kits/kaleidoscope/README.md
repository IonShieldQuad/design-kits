# Kaleidoscope

**A full-bleed mirrored kaleidoscope. Symmetry instead of restraint.**

A dark kit that is deliberately multi-hue — ruby, amber, emerald, sapphire and violet — and
stays coherent because *every pattern in it is mirrored*. The library's usual rule ("one accent,
one second accent") is suspended here on purpose; the discipline moved from the palette into the
geometry. `docs/KIT-SPEC.md` says a third "look at me" colour is how kits start looking like a
rainbow. That is true, and this kit answers it rather than ignoring it: five hues are survivable
only because exactly two of them have a job and the rest are folded into patterns.

This revision answered a review that found the kit *insufficiently itself*: strong facets, but a
background that was still a dark card on a dark page. The ground is now a drawn mirrored field,
and two new forms — a beam of light and a fractal shard — do jobs the old pattern set did not.

## The argument, in one paragraph

A kaleidoscope is a radial object. Its colour is not restrained; its *form* is. So the kit takes
the colour as given (five facets) and puts all the discipline in the mirror: an eight-fold
mandala field that tiles seamlessly and is under every surface, a conic fan that repeats its own
first half back, a beam of light symmetric about its own axis, a fractal shard split down its
spine, and a chamfer that cuts opposite corners rather than rounding them. Any pattern added to
this kit should be able to answer "where is your mirror?" If it can't, it belongs to a different
kit.

## The motifs, and what each one does

Four tokens are declared in `kit.json` `signature`, so the lab renders each as a 168×72 tile.
They are not four variations on one idea — each has a distinct job:

| Token | Device | Job |
|---|---|---|
| `--kaleidoscope-mandala` | DRAWN SVG: five 8-fold rosettes per 200px tile, half their facets unlit | **the ground.** It is what `--bg` is made of — a full-bleed field, not a card on a page. |
| `--kaleidoscope-beam` | DRAWN SVG: hard-banded trapezoids, mirrored about the shaft axis | **light.** A shaft with a near-white core and chromatic flanks. Also the media panel (`--media-bg`). |
| `--kaleidoscope-fractal` | DRAWN SVG: a Sierpinski gasket mirrored into a diamond shard | **form.** A cut stone with real internal structure and hard edges — the shape language as an object. |
| `--kaleidoscope-star` | `repeating-conic-gradient`, 180° period | **the wheel.** The pure mirror device: nine wedges whose second half is the first half reflected. |

`--kaleidoscope-prism` is a fifth pattern and deliberately **not** a tile. It is a *fill* —
`--media-bg` and `--fill-bg` are made of it — and a strip of ordered colour bands sitting beside
the beam would be the same device twice, which is exactly the redundancy the brief cuts. The two
depth tokens are not tiled for a mechanical reason: `--kaleidoscope-facet-edge` (the lit inset
edge, and `--glow`) and `--kaleidoscope-glint` (the outer bloom, used by `--shadow-2`) are
`box-shadow` values, and the lab paints a signature token only as a `background`. They are
documented in `DESIGN.md` instead of padded into the strip.

**Why the ground got a motif and the old two patterns lost theirs.** The previous set carried
`--kaleidoscope-shard` (a repeating line lattice) and `--kaleidoscope-rose-window` (concentric
rings). Both were *fields* that did the ground's job while the ground itself was a plain
gradient. The mandala now does that job far better — it is drawn, mirrored, and faceted — and the
fractal does the geometry as an *object*. Keeping all four would have been exactly the dilution
the brief warns about.

## Roles — which facet does what

| Facet | Token | Job |
|---|---|---|
| **Ruby** `#ff2d6f` | `--accent` | **The one facet that acts.** The single filled primary control on a screen, plus its hover, plus ruby hairlines. |
| **Sapphire** `#5b86ff` | `--accent-2` | **Cool counterweight.** Media gradient (`--accent` → `--accent-2`), progress bars, avatars, the focus ring. Never fills an action. |
| Emerald `#19dda0` | `--kaleidoscope-emerald` | structure / graphic: mandala facet, prism band, chart series. |
| Amber `#ffb020` | `--kaleidoscope-amber` | structure / graphic: mandala facet, the bright core of a beam's flanks, the middle of the prism ramp. |
| Violet `#a678ff` | `--kaleidoscope-violet` | structure / graphic: mandala facet, the outer rib of the beam, hairline tint. |

Emerald, amber and violet **never fill a control and are never used as text**. That constraint is
the whole reason five hues do not become a mess: two facets ask for attention, three are material.

## How symmetry keeps it from being a mess

Four mechanisms, all checkable in `tokens.css`:

1. **Every pattern is mirrored.** `--kaleidoscope-mandala` is a set of eight-fold rosettes whose
   unlit facets mirror to unlit facets; `--kaleidoscope-beam` is symmetric about its own axis;
   `--kaleidoscope-fractal` is split down a vertical spine; `--kaleidoscope-star` is a
   `repeating-conic-gradient` whose period is 180°, so the second half of every turn is the first
   half reflected; `--kaleidoscope-prism` repeats ruby and sapphire in its own ramp.
2. **Only two facets have roles.** Fills are ruby; media is sapphire. A screen with two filled
   controls is a bug, not a variation.
3. **One geometry.** Two cuts, no curves: `--clip` (10px, two opposite corners) for controls and
   `--kaleidoscope-facet-clip` (22px, all four corners) for surfaces. Never both on one element.
4. **A ground that refuses to compete.** The field is a *deep* indigo — its brightest pixel is
   approximately `#332928` — because facets read as light through glass only if the ground never
   becomes a poster.

The type does the same job: three neutral faces (Sora / Inter / IBM Plex Mono) and no display
gimmick, so the geometry is the loudest thing on the page.

## Contrast — measured, never eyeballed

The ground is now an **image layer**, so the binding ground is not a declared stop. It is the
brightest pixel the field actually paints, measured off the rendered page (a 1280×1400 screenshot
of `--bg` with no text, then per-pixel WCAG luminance). That pixel is ≈ `#332928`.

| Pair | Ratio | Floor |
|---|---|---|
| `--text` on the deepest stop `#040310` | 18.70:1 | 7:1 |
| `--text` on the field's brightest pixel | 12.89:1 | 7:1 |
| `--text-muted` on `--surface` | 9.10:1 | 4.5:1 |
| `--text-muted` on the field's brightest pixel | 7.04:1 | 4.5:1 |
| `--text-dim` on the deepest stop `#040310` | 6.79:1 | 4.55:1 |
| `--text-dim` on `--surface` | 6.04:1 | 4.55:1 |
| `--text-dim` on `--surface-2` | 5.26:1 | 4.55:1 |
| **`--text-dim` on the field's brightest pixel** | **4.68:1** | **4.55:1 — the worst pair in the kit** |
| `--accent-ink` on the field's brightest pixel | 5.38:1 | 4.5:1 |
| `--accent-ink` on `--surface` | 6.95:1 | 4.5:1 |
| `--text-invert` on `--accent` (ruby) | 5.67:1 | 4.5:1 |
| `--text-invert` on `--accent-hover` | 6.91:1 | 4.5:1 |
| status badges on `--surface-2` (ok / warn / danger / info) | 7.48 / 7.05 / 5.64 / 6.79:1 | 4.5:1 |
| `--focus-ring` on the deepest stop | 6.14:1 | 3:1 |

**The worst pair is `--text-dim` at 4.68:1, on the field's brightest pixel** — the caption/hint
tier, on the one image layer that lifts arbitrary pixels. Two decisions hold it there:

- **No two facets overlap.** The rosettes are sized to *touch* (r=70; 2r=140 against a 141.4
  corner-to-centre distance), so no pixel ever carries two facet tints. The alpha budget is
  exactly one facet, which makes the ceiling exact rather than approximate.
- **Half the facets are unlit.** Roughly every second facet is drawn near-black at 62%. Darkening
  is free — it can never push text under the floor — so the field buys its internal structure
  from shadow, and its lit facets stay low (12–15% of a jewel hue over the brightest aperture
  stop).

**The masthead's ruby bloom was removed (`--wash: none`).** The star of the old design was a 15%
ruby radial bloom on the masthead; stacked on the field it puts `--text-dim` at 4.5:1 before any
facet joins it. The field *is* the masthead's material now, so the bloom is gone. This is the
honest version of "an image on `--bg` binds against its lightest region".

Two pairs *fail* and are the reason two tokens exist: white on ruby is **3.59:1** (hence the
near-black `--text-invert`) and ruby `#ff2d6f` as a small label is only ~4.1:1 over the lit
ground (hence `--accent-ink` `#ff6f9c`).

**No `--text-on-surface*` tokens are declared, and that is a deliberate call.** Those exist for a
*three-tier stack that inverts*. This kit's grounds — the field, `--surface`, `--surface-2` — are
all dark, so a single text tier clears every one of them; the closest pair, `--text-dim` on
`--surface-2`, is 5.26:1. Adding overrides would be ceremony, not safety.

## Non-flatness — the tiles, measured

A tile that renders flat is this library's most-repeated defect, so each motif was rasterised as
a `background` on a 168×72 box on `--surface-2` at 2× and graded by grayscale standard deviation:

| Motif | std-dev (lab tile) | std-dev (token drawn directly) |
|---|---|---|
| `--kaleidoscope-mandala` | 13.23 | 10.05 |
| `--kaleidoscope-beam` | 29.52 | 29.23 |
| `--kaleidoscope-fractal` | 32.60 | 32.29 |
| `--kaleidoscope-star` | 28.61 | 16.81 |
| `--kaleidoscope-prism` *(supporting fill, not tiled)* | 31.13 | 21.82 |

The mandala is the lowest by design: it is the one motif with a hard contrast ceiling, so its
variance is squeezed into a narrow luminance band. Even so it is not flat — its facets, unlit
facets and dark seams produce a std-dev of 10–13, and it is a *field*, so its job is texture
rather than a hero graphic.

## Key choices, and what they cost

- **The ground is drawn artwork.** `--kaleidoscope-mandala` is a base64 SVG data URI, because a
  mirrored facet field with hard edges is geometry, not a gradient. The art is declared once as
  `--kaleidoscope-mandala-art` and `--bg` and the tile both reference it — derive, don't
  duplicate.
- **`--surface-2` is lighter than `--surface`.** Nested panes *catch light* rather than sinking
  into a well: elevation is luminance, not distance. Cost: `--surface-2` is not usable as a
  deliberately dark inset. If you need one, use the darkest stop of the ground — the fill of the
  `facet-panel` component in `DESIGN.md`.
- **Surfaces are opaque, not translucent.** A glassy pane would be more on-theme, but it turns
  every contrast claim into a claim about a composite over a gradient. Opaque keeps every pair
  provable against a hex — the ground is the single computed composite, and it is measured.
- **The chamfer costs the border along the diagonal,** and it **eats outer shadows and
  outlines.** Everything the lab clips loses any outward `box-shadow`, including a focus ring. So
  `--shadow-1`, `--shadow-2` and `--glow` are **inset-first**, `--kaleidoscope-glint` is the
  outer bloom for elements you choose *not* to clip, and keyboard focus is carried by the
  sapphire border colour rather than an outside outline.
- **`--radius-pill` is 6px, not 999px.** A 999px pill cannot survive a chamfer. Badges and
  avatars are chamfered chips here.
- **`--accent-ink` is declared, and it is not `--accent`.** Different weights of one decision.
- **`--fill-bg` is `--kaleidoscope-prism`.** Progress bars and avatars disperse into ordered hard
  bands instead of a smooth accent→accent-2 fade — the hard-bands rule, applied to a component.
- **`--media-bg` is the beam over the prism.** The card media panel shows a shaft of light
  dispersing, which is the kit's own thesis rather than a generic two-stop ramp.
- **Status colours are off the facets by value.** Every hue family is taken, so `--ok`, `--warn`,
  `--danger` and `--info` are *duller and deeper* than the facet they resemble, and `--danger` is
  pushed to orange-red vermilion so a destructive state can never be read as the ruby action.

## Lint

`designmd lint` reports **0 errors, 0 warnings** (1 info: the token summary). `--kaleidoscope-*`
tokens that the lab cannot tile (the two `box-shadow` depth tokens and the `polygon()` clip) are
described in prose rather than declared as signature tiles, so nothing renders as an empty chip.

## When to use it

Launch pages, game and music UI, portfolio and gallery surfaces, anything that should read as
*crafted* rather than merely dark. Do not use it for long-form reading, dense data entry, or any
form where five hues is more signal than the content deserves.

## Files

- `DESIGN.md` — normative values and rationale
- `tokens.css` — the skin (contract v1, plus the facet set and the drawn motifs)
- `kit.json` — gallery metadata
- `index.html` — generated component lab (`python tools/build.py --only kaleidoscope`)
- `tokens.json`, `tailwind.theme.json`, `theme.css` — generated exports

No `kit.css`: every change here is expressible as a token — a drawn motif is a token, and the
field, the beam and the shard all live in `tokens.css`.
