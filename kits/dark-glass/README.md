# Dark Glass

**Dark frosted glass.** A near-black ground carrying a violet/cyan mesh is seen through genuinely
translucent panels, edged with hairline *light* lines and separated by layered soft shadow. One
clear violet drives action; one cyan stays graphic. Nothing in the kit is opaque and nothing in the
kit is neon.

- Kit: `dark-glass` · order `75` · mode `dark` · source `original`
- Fonts: Sora (display) · Inter (body) · JetBrains Mono (labels)
- Tags: `dark`, `glass`, `soft`, `modern`

## Stance

Most "dark glassmorphism" fails in one of two ways: the panels are painted on (opacity 0.9, no
`backdrop-filter`), or the ground behind them is a smooth ramp with nothing to blur, so the frost is
invisible and the kit reads as flat charcoal with rounded corners.

This kit fixes both. Surfaces are `rgba(22,26,36,.55)` and `rgba(28,33,45,.68)`, and
`templates/lab.css` applies `var(--blur)` (`blur(20px) saturate(140%)`) to every `.card`, so the
ground is visible *through* the panels at all times.

## Key choices

- **The ground is a mesh, not a ramp — deliberately.** This is the one thing to understand about the
  kit. A `backdrop-filter` over a perfectly smooth gradient is indistinguishable from flat paint:
  there is no high-frequency detail for the blur to smear and no local colour difference for the
  `saturate()` to lift. The first build of this kit used a two-stop ramp and the frosted panels read
  as slightly-different-grey rectangles. `--bg` is therefore soft colour blobs — violet, cyan and
  deep purple — laid over a ramp with five close-spaced stops (`#0d0f1b` → `#070810`). **Six blobs,
  in three pairs:** the same three voices at y-positions 40 / 120 / 640, then again (a little quieter)
  at 1500 / 2050 / 2750, so the mesh carries down the whole document. The first version put all three
  near the top and everything below the fold photographed as flat black — the blobs have to follow the
  page, not just the masthead. **Do not simplify `--bg` to two stops, and do not drop the lower
  three.**
- **Blob geometry is in px, positions partly in %.** `radial-gradient(760px 620px at 14% 40px, …)`.
  The document is thousands of pixels tall; percentage-sized blobs (as the sibling `glass` kit uses
  for its stops) would smear the wash down the page and leave the viewport flat — and percentage
  *y*-positions would drift every time content is added. Fixed px radii and px y-positions keep the
  same mesh in view at any document length, and the two x-positions as % keep it responding to
  width.
- **Light borders, never dark ones.** `--border` is `rgba(255,255,255,.14)`. On a near-black ground a
  dark hairline is literally invisible, so the edge that reads is the *light* one. There is no ink
  border token anywhere in this kit. Depth is `--shadow-1` / `--shadow-2`: two black shadow layers
  each plus an `inset 0 1px 0 rgba(255,255,255,.10–.14)` top-edge highlight that makes a panel read
  as a pane rather than a hole.
- **`--text-invert` is dark, not white.** White on `#8b7cff` measures **3.27:1** — a fail. The kit
  therefore inverts the usual assumption: the primary button is luminous violet with a near-black
  label (`#0b0c14`, **5.97:1**). This is the single most important colour decision in the kit; if
  you "fix" it to white text you break it.
- **Two surface opacities, not two colours.** `--surface` 55%, `--surface-2` 68%, same navy hue.
  Elevation is opacity + shadow; hue is constant.
- **Status colours sit outside the brand pair.** Brand is violet (`#8b7cff`, hue 247°) and cyan
  (`#4fd8ff`, hue 193°). Status is green `#4fce8f` (150°), amber `#f5b942` (42°), pink-red
  `#ff6b81` (352°) and periwinkle `#6b9dff` (220°, kept 27° off the cyan so an "info" badge can
  never be read as brand cyan).
- **Derived, not invented.** `--accent-soft`, `--shadow-*`, `--dg-sheen` and `--dg-edge` are
  `rgba()` / `linear-gradient()` expressions, not new hues.
- **Sora** as the display face (rather than the sibling `glass` kit's Plus Jakarta Sans) — same
  humanist-geometric family, visibly different skeleton, so the two read as two kits in a thumbnail.

## Contrast — the compositing maths

The ground is a mesh and the surfaces are translucent, so a single flat hex proves nothing. Two
worst cases are used, and both are computed by `verify-dimensions.py` (scratch), which **parses
`tokens.css`** rather than hard-coding values:

- **Ground worst case** = the lightest pixel of the mesh. The sampler walks a 1440×2600 grid,
  evaluating each `radial-gradient` layer's alpha with the CSS model
  `a = α_peak · (1 − t / t_stop)` where `t` is the normalised elliptical distance, compositing
  back-to-front the way CSS paints (last layer over the ramp, first layer on top), with the
  **lightest ramp stop `#0d0f1b` used as the base everywhere** — a strict upper bound, since no
  real pixel sits on the lightest base *and* at the centre of every blob.
  Result: **`#1a3748`, L = 0.03419**, at (1264, 120) — the centre of the cyan wash.
- **Surface worst case** = the translucent panel composited over that pixel, per channel, on the
  sRGB values the browser actually blends:
  - `--surface` = `0.55 × rgb(22,26,36) + 0.45 × rgb(26,55,72)` = **`#182734`**
  - `--surface-2` = `0.68 × rgb(28,33,45) + 0.32 × rgb(26,55,72)` = **`#1b2836`**

### Required pairs

| Pair | Foreground | Background (worst case) | Ratio | Target |
|---|---|---|---|---|
| body text | `--text` `#eef2fb` | lightest mesh pixel `#1a3748` | **11.12:1** | ≥ 7:1 ✓ |
| secondary text | `--text-muted` `#b7c0d4` | composited `--surface` `#182734` | **8.34:1** | ≥ 4.5:1 ✓ |
| button label | `--text-invert` `#0b0c14` | `--accent` `#8b7cff` | **5.97:1** | ≥ 4.5:1 ✓ |
| caption/hint | `--text-dim` `#a0a9be` | lightest mesh pixel `#1a3748` | **5.29:1** | ≥ 4.55:1 ✓ |
| caption/hint | `--text-dim` `#a0a9be` | composited `--surface` `#182734` | **6.46:1** | ≥ 4.55:1 ✓ |
| caption/hint | `--text-dim` `#a0a9be` | composited `--surface-2` `#1b2836` | **6.35:1** | ≥ 4.55:1 ✓ |

`--text-dim` is the pair that usually fails on dark kits, so it was tuned against all three grounds
rather than only the panel: it sits at `5.29:1` on the *raw* ground, which is the binding case
because compositing a dark navy panel over the ground only *darkens* it and therefore only helps
light text.

### Supplementary

| Pair | Ratio |
|---|---|
| `--text` on composited `--surface` | 13.58:1 |
| `--text-muted` on the raw worst-case ground pixel | 6.83:1 |
| `--ok` / `--warn` / `--danger` / `--info` on composited `--surface-2` | 7.52 / 8.47 / 5.46 / 5.62:1 |
| `--accent` text on composited `--surface` | 4.66:1 |
| `--accent` text on the raw worst-case ground pixel | 3.82:1 — see trade-offs |
| `--accent` text on `--accent-soft` over `--surface` (active nav item) | 3.71:1 — see trade-offs |

## Trade-offs and deviations

- **`--accent` stays exactly the briefed `#8b7cff`.** It satisfies every required pair (dark label
  5.97:1) and is the value the brief named, so it was not "tuned for contrast" the way `glass` tuned
  its accent. The consequence is honest: violet *as text* on the darkest-lit part of the ground is
  **3.82:1**, below AA for body copy. The kit therefore treats `--accent` as a **fill, rail and
  indicator** colour — buttons, active nav chips, progress bars, the accent badge — and never relies
  on it for a paragraph. If a project needs accent-coloured link text on the bare ground, lighten
  `--accent` toward `#a091ff` (≈4.7:1 on the worst pixel) and accept a slightly pastel button fill.
- **`--bg` is a gradient, so the masthead loses its own wash.** `templates/lab.css` builds the
  masthead as `linear-gradient(180deg, var(--bg-2), var(--bg))`; feeding a gradient into a gradient
  stop is invalid CSS, so the whole `background` declaration is dropped and the masthead is
  transparent — the page mesh shows through instead. Visually correct (arguably better), but it is a
  consequence of a gradient `--bg`, documented here rather than left as a surprise.
- **The gallery preview will be flatter than the lab.** `tools/build.py` renders the gallery card as
  `background:{bg}` followed by its own `background-image`, which overrides a gradient `--bg`. The
  kit's colour survives only in the swatch bar there. The **lab page is the reference view.**
- **Nested glass is avoided.** Two translucent panels stacked composite to nearly opaque and the
  frost vanishes. `.card-elevated` uses the denser `--surface-2` rather than a second blur layer.
- **The mesh is a contrast liability if you make it prettier.** Raising `--dg-wash-1/2/3` past
  roughly `.30` pushes the lightest ground pixel past L ≈ 0.041 and `--text-dim` falls under 4.55:1.
  Re-run `verify-dimensions.py` after touching the washes.
- **`bg-stop-1/2/3` are unreferenced by components** (orphaned-token lint warnings, if the linter
  is run): they are the documented raw ramp stops consumed by `--bg`, and exist so a project can
  rebuild the mesh or emit a printed swatch without re-typing hexes.

## When to use

Dark dashboards and app shells, control panels, media tools, anything that should feel lit rather
than printed. Avoid where `backdrop-filter` is unavailable, on very old GPUs, for data-dense reading
(the glass reduces text contrast budget), and for print — use `--surface-solid`.

## Verify

```bash
python tools/build.py --no-export --no-lint     # lab html + contract check
python "C:/Users/Lily/AppData/Local/hermes/cache/scratch/verify-dimensions.py"   # contrast table
```
