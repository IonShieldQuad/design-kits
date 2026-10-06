# Outer Space

**The wonder of space.** A deep blue-violet void carrying a starfield and five vast nebula blooms,
seen through translucent panes, with a single warm starlight as the action colour. Vast, quiet,
awe-struck — a vista, not an instrument.

- Kit: `outer-space` · order `90` · mode `dark` · source `original`
- Fonts: Outfit (display) · Inter (body) · IBM Plex Mono (labels)
- Tags: `dark`, `cosmic`, `glowing`, `spacious`

## Stance

Every other dark kit in this library is legible as an instrument. `carbon` is engineered, `cyberpunk`
is loud, `signal` is instrumental, `dark-glass` is sleek. This one is a viewpoint: you do not operate
it, you look out of it.

The brief was *"the wonders of space"*, and the word to design to is **wonder** — not menace, not
tech, not noise. That drove three decisions that are not decorative:

1. **Deep, not black.** The ground is a blue-violet void with **20.4x** of luminance spread across it
   (0.0028 → 0.0444), not a flat #000. Depth is what makes a page feel large.
2. **Starlight, not neon.** The light reads as emitted by distant objects — a warm white-gold
   (`#ffe9b8`) that is *lighter* than the page, an ice cyan for the cool register, and violet/rose
   that exist only as atmosphere. Nothing here is a glow-in-the-dark accent colour.
3. **Vast.** Big soft radial blooms, generous radii (8/14/24px), low-alpha hairline edges, and a
   starfield that gives the frosted panels something real to blur.

## Key choices

- **The accent is light, and the button label is the void.** `--accent` is `#ffe9b8` (starlight) and
  `--text-invert` is `#0a0e22` — **16.02:1**, and 17.44:1 on hover. White on this accent measures
  1.3:1. This is the single most distinctive thing about the kit: every other dark kit here fills its
  primary button with a saturated neon and inverts to white; this one emits. **Do not "fix"
  `--text-invert` to white.**
- **Hover gets brighter, not darker.** `--accent-hover` is `#fff4d6` — a star flares when you look at
  it. It is the one hover in the library that moves *up* in luminance.
- **`--bg` is layered, not a ramp — this is load-bearing.** `templates/lab.css` applies
  `var(--blur)` to every `.card`, and a `backdrop-filter` over a perfectly smooth gradient is
  indistinguishable from flat paint: there is no high-frequency detail to smear and no local colour
  gradient for `saturate()` to lift. So the ground is, top layer first:
  - **four starfield tiles** — 1.1px / 0.9px / 1.3px / 2.4px specks on **137×131px, 89×97px,
    211×197px and 373×331px** tiles, deliberately coprime sizes so the field never resolves into a
    visible grid; the 373px tile carries the few bright stars that give the field a sense of scale;
  - **five off-centre blooms** — violet `#6b4bd6` (top left, peak α .42), rose `#c2418f` (right,
    .25), ice `#4fd1e0` (low centre, .23), a warm gold star bloom (top, .16) and a deep violet floor
    bloom (bottom left, .21);
  - **a five-stop ramp** from `#0b0f26` to `#05070f`.

  The specks are what the glass frosts; the blooms are what the `saturate()` lifts. Remove either and
  the panels flatten into charcoal rectangles. `--bg-plain` is the same ground **without** the
  specks, for text-critical or print-adjacent use; `--starfield` is the speck layers alone, for
  overlaying a hero or a poster.
- **Bloom geometry is in px with % x-positions.** The document is thousands of pixels tall;
  percentage-sized blooms would smear the wash down the page and leave the viewport flat. Fixed px
  radii keep the same vista in view at any document length; the x positions stay in % so the
  composition responds to width.
- **Edges are hairline and cool.** `--border` is `rgba(178,198,255,.13)`, `--border-strong`
  `rgba(190,208,255,.22)`, both at `--border-w: 1px`. A vista is bounded by light, so separation
  comes from `--glow` and `--shadow-1/2` (each carrying an `inset 0 1px 0` starlight lip along the
  top edge), never from a heavier line.
- **Outfit, not Space Grotesk or Sora.** `carbon` already ships Space Grotesk as its display face and
  `dark-glass` ships Sora; Outfit is a third wide geometric grotesque with a visibly different
  skeleton, so the three dark kits do not share a heading voice. It is also the subject-appropriate
  face: wide, quiet, round-countered, and unsentimental at 700. Inter carries body, IBM Plex Mono
  carries labels at a wide-but-not-HUD 0.14em tracking.
- **Gold is the only action.** Ice cyan is the cool register (gradients, charts, avatars, media) and
  never fills a button. Violet and rose are ground only. That is the whole colour budget: two plus a
  void.
- **The accents were raised once, on evidence.** The first build's blooms (violet α .34) rendered
  correctly but read as a flat dark page at 200×120 — the vision check on a downscaled screenshot
  could not find the nebula. The blooms were raised ~25% (to α .42/.25/.23) and `--text-dim` lifted
  from `#aab4d6` to `#b0badb`, which buys back the contrast the brighter ground spends. Median ground
  luminance went 0.0099 → 0.0120 and the peak 0.0364 → 0.0445; the nebula and the star specks are now
  both visible at thumbnail scale, and every required pair still clears its target with margin.
- **Derived, not invented.** `--accent-soft` is a 14% tint of `--accent`; `--glow`, `--shadow-1/2`,
  `--halo-*` and `--vue` are `rgba()`/gradient expressions over the palette, not new hues.

## Palette and the role of each colour

| Token | Value | Role |
|---|---|---|
| `--bg-stop-1` | `#0b0f26` | lightest ramp stop — the top of the void (and the contrast bound) |
| `--bg-stop-2` | `#0a0e22` | mid ramp stop |
| `--bg-stop-3` | `#05070f` | deepest stop — the bottom of the page |
| `--nebula-1` | `#6b4bd6` | violet bloom, top left = DESIGN.md `tertiary` |
| `--nebula-2` | `#c2418f` | rose nebula, right |
| `--nebula-3` | `#4fd1e0` | ice lane, low centre |
| `--accent` | `#ffe9b8` | **starlight — the one action colour**: buttons, focus, active nav, links |
| `--accent-hover` | `#fff4d6` | the flare: brighter, never darker |
| `--accent-2` | `#7fe3f0` | **ice cyan — the cool register**: gradients, charts, media, avatars. Never a button |
| `--text` | `#eef1fb` | 9.85:1 on the brightest ground pixel |
| `--text-muted` | `#bcc5e4` | body-adjacent, labels, table cells |
| `--text-dim` | `#b0badb` | captions, hints, placeholders — tuned against the raw bright ground |
| `--text-invert` | `#0a0e22` | the void, as the label on starlight |
| `--ok` `--warn` `--danger` `--info` | `#5fe0a8` `#ffb066` `#ff6f86` `#8fb6ff` | aurora / solar amber / rose-hot / glacial, deliberately outside the brand pair |

## Contrast — how it was measured

`--bg` is a gradient and the surfaces are translucent, so a flat hex proves nothing. The numbers
below come from `scratch/verify-space.py`, which **parses `tokens.css`** — ramp stops, bloom
geometry, speck tile sizes and surface alphas — and then reconstructs the gradient the way CSS
paints it (first layer on top), sampling it on a 1440 × 2600 grid.

- **Worst-case ground pixel = `#40384e`, L = 0.04451, at (1008, 92)** — the top of the page, where
  the warm gold star bloom, the violet bloom and the lightest ramp stop `--bg-stop-1` (`#0b0f26`)
  overlap. **That stop is the ground bound used for every `--text-*` on `--bg` figure below.**
- Composites over that pixel, per channel: `--surface` (α .55) → **`#282742`**;
  `--surface-2` (α .66) → **`#282b4e`**.
- Ground spread across the sampled page: min 0.00219, median 0.01201, max 0.04451 — **20.4x**.

### Required pairs

| Pair | Foreground | Background | Ratio | Target |
|---|---|---|---|---|
| body text | `--text` `#eef1fb` | worst ground `#40384e` | **9.85:1** | ≥ 7:1 ✓ |
| secondary text | `--text-muted` `#bcc5e4` | composited `--surface` `#282742` | **8.37:1** | ≥ 4.5:1 ✓ |
| button label | `--text-invert` `#0a0e22` | `--accent` `#ffe9b8` | **16.02:1** | ≥ 4.5:1 ✓ |
| caption / hint | `--text-dim` `#b0badb` | worst ground `#40384e` | **5.76:1** | ≥ 4.55:1 ✓ |
| caption / hint | `--text-dim` `#b0badb` | composited `--surface` `#282742` | **7.44:1** | ≥ 4.55:1 ✓ |
| caption / hint | `--text-dim` `#b0badb` | composited `--surface-2` `#282b4e` | **7.06:1** | ≥ 4.55:1 ✓ |

`--text-dim` is the pair that usually fails on dark kits, so it was tuned against all three grounds
including the *raw* brightest ground pixel — the binding case here, since compositing a dark pane
over the ground only darkens it and therefore helps light text. It is clear at 5.76:1 with the whole
page's brightest pixel as its background.

### Supplementary

| Pair | Ratio |
|---|---|
| `--text` on composited `--surface` | 12.72:1 |
| `--text-muted` on the worst ground pixel | 6.48:1 |
| `--text-muted` on composited `--surface-2` | 7.94:1 |
| `--text-invert` on `--accent-hover` `#fff4d6` | 17.44:1 |
| `--accent` (starlight) as text on the worst ground pixel | 9.31:1 |
| `--accent-2` (ice) on composited `--surface` / on the worst ground | 9.67 / 7.49:1 |
| `--ok` / `--warn` / `--danger` / `--info` on composited `--surface-2` | 8.24 / 7.55 / 5.10 / 6.68:1 |

Unlike the other dark kits, accent-as-text is *not* a liability here: the accent is the palest colour
in the kit, so starlight link text is 9.31:1 on the brightest ground pixel. It is safe.

## Trade-offs and deviations

- **The star specks are excluded from the contrast bound, on purpose.** A 1–2.4px speck at peak α .75
  sitting under a glyph would locally measure ~1.3:1 against `--text-dim`. A speck is a decoration,
  not a ground: the four tiles cover well under 0.6% of the field and are excluded as a category —
  the bound is the lightest pixel of the *nebula ground*, which is what a text run actually sits on.
  If you find that uncomfortable, `--bg-plain` is the identical ground with the specks removed and
  passes the same numbers unchanged.
- **`--bg` is a gradient, so the masthead loses its own wash.** `templates/lab.css` builds the
  masthead as `linear-gradient(180deg, var(--bg-2), var(--bg))`; feeding a multi-layer value into a
  gradient stop is invalid, so that whole declaration is dropped and the masthead is transparent —
  the page vista simply shows through. Visually correct (arguably better than a separate wash), but
  it is a consequence of a gradient `--bg`, documented rather than left as a surprise.
- **The generated gallery preview is flatter than the lab.** `tools/build.py` renders the gallery card
  as `background:{bg}` followed by its own `background-image`, which *replaces* a gradient `--bg`
  with build.py's accent-soft wash. The kit's colour survives there mostly in the swatch bar. **The
  lab page is the reference view** — and a real render of it scales down to a legible 200×120:
  verified, it reads as a deep indigo/violet field with a visible nebula glow, scattered star specks
  and a pale gold action.
- **No generated exports yet.** This kit was authored and verified with
  `python tools/build.py --no-export --no-lint` (the documented self-check), so
  `tokens.json` / `tailwind.theme.json` / `theme.css` are produced by the next full `build.py` run.
- **Orphaned colour tokens, if the linter is run:** `--nebula-1/2/3`, `--bg-stop-1/2/3`, `--halo-*`,
  `--starfield`, `--bg-plain`, `--starlight`, `--starlight-bright`, `--ice-cyan`, `--glacial-blue`
  and `--vue` are the raw stops and layers the ground is built from, exposed deliberately so a
  project can rebuild the vista or print a swatch without re-typing an `rgba()`. DESIGN.md has no
  component property that can reference a gradient (and a gradient in `colors:` is a linter error),
  which is exactly why they ship as colours.
- **`--text-dim` is in DESIGN.md rather than excluded.** It clears 4.55:1 on every ground it sits on,
  so unlike `carbon`'s it needs no exemption.
- **Linter: 0 errors, 8 warnings — all deliberate.** `npx -p @google/design.md designmd lint` reports
  three `contrast-ratio` warnings on the components that use `{colors.primary-soft}` as a background
  (`button-secondary-hover`, `badge-accent`, `nav-item-active`) and five `orphaned-tokens` warnings
  (`nebula-1`, `nebula-3`, `bg-stop-1/2/3`).
  - The contrast warnings are **false positives**: the linter reads `rgba(255,233,184,0.14)` as an
    opaque `#ffe9b824` and compares it against itself (1.00:1). The real composite is a 14% gold tint
    over the ground or a pane, where starlight text measures 9.31:1 on the brightest ground pixel and
    12.72:1 on a card. `dark-glass` trips the identical rule for the identical reason.
  - The orphan warnings are the **gradient stops the kit is required to ship as colours**: DESIGN.md
    has no component property that can reference a gradient with per-layer background sizes, and a
    gradient in `colors:` is a linter error, so they exist as addressable stops with no component to
    point at them. `nebula-2` avoids the list only because it doubles as `chart-3`.

## When to use

Awe-led landing pages, hero sections, science and space products, astronomy and physics writing,
anything where the page should feel like a window rather than a document. It is at its best with one
large type-led hero and a lot of emptiness.

Avoid it for dense data tables and long-form reading (the low-luminance ground costs you contrast
budget), for print (use `--surface-solid` and `--bg-plain`), and anywhere the brief is "serious and
corporate" — this kit is unembarrassed about being beautiful.

## Verify

```bash
python tools/build.py --no-export --no-lint          # lab html + token-contract check
python "C:/Users/Lily/AppData/Local/hermes/cache/scratch/verify-space.py"   # parses tokens.css, prints the table
```

The second command re-derives every number in this README from `tokens.css`. Re-run it after touching
`--bg`, the blooms' alphas, the surface alphas or `--text-dim`.
