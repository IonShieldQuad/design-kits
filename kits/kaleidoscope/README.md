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

A follow-up legibility pass then fixed three defects a cold review found in that ground: small
text floating **on** the field competed with the facet edges; two Signature tiles read as holes
in the page; and the first (`--bg`) swatch vanished into the paper. All three are fixed at the
token level — a translucent **veil** over the field, a **wash plate** on the masthead, and a
**lit tile plate** under the dark motifs — with no change to the palette, the motifs or the
layout. The numbers are below.

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
| `--kaleidoscope-mandala` | DRAWN SVG: five 8-fold rosettes per 200px tile, half their facets unlit | **the field.** `--kaleidoscope-mandala-art` is the drawn field; this token is the signed *specimen* — the same field on a lit tile plate. The live page ground is `--kaleidoscope-ground` (the field over the aperture under `--kaleidoscope-veil`). |
| `--kaleidoscope-beam` | DRAWN SVG: hard-banded trapezoids, mirrored about the shaft axis | **light.** A shaft with a near-white core and chromatic flanks. Also the media panel (`--media-bg`). |
| `--kaleidoscope-fractal` | DRAWN SVG: a Sierpinski gasket mirrored into a diamond shard | **form.** A cut stone with real internal structure and hard edges — the shape language as an object. |
| `--kaleidoscope-star` | `repeating-conic-gradient`, 180° period | **the wheel.** The pure mirror device: nine wedges whose second half is the first half reflected. |

The three dark motifs (mandala, beam, fractal) each carry the same **lit tile plate** (a violet
radial) under their artwork. That is a legibility fix, not decoration: a tile that shares the
page's base reads as a hole cut in the page, and `--kaleidoscope-mandala` used to *be* `--bg`, so
its tile was literally the page. The plate is written out literally in each token rather than
shared through one `var()` — the lab generator classifies a signature token by looking for a
literal `gradient(`, and a value built only from `var()` references is misread as a box-shadow.

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
4. **A ground that refuses to compete.** The field is a *deep* indigo, and a translucent veil
   over it keeps its brightest pixel at approximately `#231c20` — because facets read as light
   through glass only if the ground never becomes a poster.

The type does the same job: three neutral faces (Sora / Inter / IBM Plex Mono) and no display
gimmick, so the geometry is the loudest thing on the page.

## Contrast — measured, never eyeballed

The ground is an **image layer under a translucent veil**, so the binding ground is a
**composite**, not a declared stop and not the art beneath it. Its brightest pixel was measured
off the rendered page (a 1280×1200 screenshot of `--bg` with no text, then per-pixel WCAG
luminance): the raw field peaks at `#332928`; `--kaleidoscope-veil` (`rgba(4,3,16,.34)`) brings
that composite down to **`#231c20`**. Every ink on the ground is graded against that composite.

| Pair | Ratio | Floor |
|---|---|---|
| `--text` on the deepest stop `#040310` | 18.70:1 | 7:1 |
| `--text` on the veiled field (brightest pixel) | 15.24:1 | 7:1 |
| `--text-muted` on `--surface` | 9.10:1 | 4.5:1 |
| `--text-muted` on the veiled field | 8.32:1 | 4.5:1 |
| `--text-dim` on the deepest stop `#040310` | 6.79:1 | 4.55:1 |
| `--text-dim` on `--surface` | 6.04:1 | 4.55:1 |
| `--text-dim` on the veiled field (brightest pixel) | 5.53:1 | 4.55:1 |
| `--text-dim` on the masthead (veil + wash) | 6.11:1 | 4.55:1 |
| **`--accent-ink` on `--accent-soft` over `--surface-2`** | **5.21:1** | **4.5:1 — the worst pair in the kit** |
| `--text-dim` on `--surface-2` | 5.26:1 | 4.55:1 |
| `--accent-ink` on `--surface` | 6.95:1 | 4.5:1 |
| `--accent-ink` on the veiled field | 6.36:1 | 4.5:1 |
| `--text-invert` on `--accent` (ruby) | 5.67:1 | 4.5:1 |
| `--text-invert` on `--accent-hover` | 6.91:1 | 4.5:1 |
| status on `--surface-2` (ok / warn / danger / info) | 7.48 / 7.05 / 5.64 / 6.79:1 | 4.5:1 |
| `--focus-ring` on the deepest stop | 6.14:1 | 3:1 |

**The worst pair is `--accent-ink` at 5.21:1, on the 15% ruby badge tint composited over
`--surface-2`** — a *translucent* ground, so it is graded as a composite (`#431f49`), never as the
raw tint. The next lowest is `--text-dim` on `--surface-2` at 5.26:1.

### The veil, and why it is a composite

The previous revision's headline claim was that the field's ceiling put `--text-dim` at 4.68:1 on
its brightest pixel — passing, but by 0.13. A cold review found the *number* was not the problem:
the problem was that small text on the field **competed with the facet edges**, whatever the peak
luminance said. So the field is now covered by `--kaleidoscope-veil` (`rgba(4,3,16,.34)`), a flat
translucent plate that is the top layer of `--bg`. It drops the peak (4.68:1 → **5.53:1**) *and*
the edge contrast together — measured mean |luminance gradient| fell 0.00049 → 0.00026, ~47%
calmer. The mirrored geometry still reads; it stops arguing with a caption.

Because the veil is translucent, every ground figure above is a **composite** — `--text-dim` is
graded against the veil over the field's brightest facet, not against the facet and not against a
solid. That is the trap the brief names, and it is why the veil's alpha is a stated number.

Two decisions still hold that ceiling exact:

- **No two facets overlap.** The rosettes are sized to *touch* (r=70; 2r=140 against a 141.4
  corner-to-centre distance), so no pixel ever carries two facet tints — the alpha budget is
  exactly one facet.
- **Half the facets are unlit.** Roughly every second facet is drawn near-black at 62%. Darkening
  is free — it can never push text under the floor — so the field buys its structure from shadow,
  and its lit facets stay low (12–15% of a jewel hue over the brightest aperture stop).

### The masthead wash is a plate, not a bloom

The old design's masthead carried a 15% ruby radial *bloom*. A bloom raises luminance, which is
exactly what a ground's ceiling cannot afford, so it was removed. `--wash` is now back as the
opposite object: a translucent dark **plate** (`linear-gradient(180deg, rgba(4,3,16,.58),
rgba(4,3,16,.34))`) laid over the veiled field. The eyebrow, the mono meta line and the swatch
labels sit on it, where `--text-dim` measures 6.11:1 against 5.53:1 on the bare veiled field.

It also fixes the first (`--bg`) swatch, which used to vanish: the swatch paints the *un-washed*
ground, so it now reads ~9.7× brighter in luminance than the washed masthead behind it. The
swatch was never the problem — the masthead and the swatch were simply the same value, and the
wash separates them.

### The surfaces are opaque; the veil carries everything else

The review's second item asked whether component surfaces let the pattern through. They do not.
`--surface` (`#15112e`) and `--surface-2` (`#221d42`) are opaque hexes, and the **computed**
background of `.card`, `.card-elevated`, `.input`, `.select`, `.textarea` and `.nav` is
`rgb(…)` at alpha 1 (`--blur: none`). The one element the lab paints with no background at all is
the `.tabs` underline row — its labels sit directly on the field, and the **veil** is what
protects them, exactly as it protects the tile captions, the block notes, the form hints and the
footer. `verify-lab.cjs` samples the rendered pixel behind that text, so this is asserted, not
assumed.

Two pairs *fail* and are the reason two tokens exist: white on ruby is **3.59:1** (hence the
near-black `--text-invert`) and ruby `#ff2d6f` as a small label is only ~4.1:1 over the lit
ground (hence `--accent-ink` `#ff6f9c`).

**No `--text-on-surface*` tokens are declared, and that is a deliberate call.** Those exist for a
*three-tier stack that inverts*. This kit's grounds — the veiled field, `--surface`, `--surface-2`
— are all dark, so a single text tier clears every one of them; the closest pair, `--text-dim` on
`--surface-2`, is 5.26:1. Adding overrides would be ceremony, not safety.

## Non-flatness — the tiles, measured

A tile that renders flat is this library's most-repeated defect, so each Signature tile was
screenshotted from the rendered lab at 2× (a 336×144 raster of the 168×72 chip) and graded by
grayscale standard deviation, with mean luminance as the separation measure. The page ground beside
the strip measures **0.30% mean luminance**:

| Motif | std-dev (168×72 lab tile) | mean luminance | vs page ground |
|---|---|---|---|
| `--kaleidoscope-mandala` | 27.93 | 8.33% | ~28× |
| `--kaleidoscope-beam` | 19.83 | 11.99% | ~40× |
| `--kaleidoscope-fractal` | 35.08 | 7.75% | ~26× |
| `--kaleidoscope-star` | 24.35 | 33.42% | ~111× |

None is flat (a flat plate would measure ~1). The fix this revision makes is in the last column:
before the lit tile plate, `--kaleidoscope-mandala` and `--kaleidoscope-beam` measured mean
luminance 1.68% and 2.97% — close enough to the 0.30% page ground that the tiles read as holes cut
in the page. The plate lifts each dark motif clear of the ground while its own artwork stays dark,
so the strip parses as four specimens. `--kaleidoscope-prism` is a *fill* and is not tiled.

## Key choices, and what they cost

- **The ground is drawn artwork, and it is veiled.** `--kaleidoscope-mandala-art` is a base64 SVG
  data URI, because a mirrored facet field with hard edges is geometry, not a gradient. The art is
  declared once and referenced by both the ground and the tile — derive, don't duplicate. Its
  *brightness* is then dialled by `--kaleidoscope-veil`, a translucent plate, rather than by
  redrawing the art: the veil is one number to tune, and it is graded as a composite.
- **`--surface-2` is lighter than `--surface`.** Nested panes *catch light* rather than sinking
  into a well: elevation is luminance, not distance. Cost: `--surface-2` is not usable as a
  deliberately dark inset. If you need one, use the darkest stop of the ground — the fill of the
  `facet-panel` component in `DESIGN.md`.
- **Surfaces are opaque, not translucent.** A glassy pane would be more on-theme, but it turns
  every contrast claim into a claim about a composite over a gradient. Opaque keeps every pair
  provable against a hex — the ground is the one deliberate composite, and it is measured.
- **The masthead's `--wash` is a dark plate, not a bloom.** A bloom raises luminance and would
  break the ground's ceiling; a dark plate lowers it and doubles as the thing that separates the
  first swatch from the paper. Cost: the masthead is a shade deeper than the page below it, which
  reads as a deliberate band rather than a seamless field.
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

`designmd lint` reports **0 errors, 0 warnings** (1 info: the token summary); `build.py` reports
the same single info line. `--kaleidoscope-*` tokens the lab cannot tile are described in prose
rather than declared as signature tiles, so nothing renders as an empty chip: the two `box-shadow`
depth tokens (`--kaleidoscope-facet-edge`, `--kaleidoscope-glint`), the `polygon()` clip
(`--kaleidoscope-facet-clip`), and the ground layers that are *plates* rather than motifs
(`--kaleidoscope-veil`, `--kaleidoscope-aperture`, `--kaleidoscope-ground`). The lab paints a
signature token only as a `background`, and a flat translucent plate as a tile is exactly the
"empty chip" that rule exists to prevent.

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
