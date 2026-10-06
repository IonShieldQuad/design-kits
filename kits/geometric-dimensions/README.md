# Geometric Dimensions

**Bauhaus geometry with real dimensional depth.** Paper ground, near-black ink, 3px rules, square
corners, and depth expressed as a **hard offset shadow — `5px 5px 0` and `9px 9px 0` of solid ink,
zero blur**. Three primaries (red, blue, yellow) supply the geometric vocabulary; exactly one of
them drives action.

- Kit: `geometric-dimensions` · order `65` · mode `light` · source `original`
- Fonts: Archivo Black (display, via the Archivo family at wght 900) · Inter (body) · Space Mono (labels)
- Tags: `light`, `bold`, `geometric`, `retro`

## Stance

Neo-brutalist, but printable. Every surface is a sheet of board lying on a bone-coloured page and
lifted off it by a slab of ink offset down-right. No blur, no glow, no translucency, no rounded
corner — the kit's identity is a single mechanic: **the hard shadow is the elevation, and there is
nothing else softening it.** Delete `--shadow-1` and the whole thing collapses to a flat light
theme with thick borders.

## Which primary drives action

**Blue (`--accent` = `#2b4bd8`) drives every action.** It is the only one of the three primaries
that clears 4.5:1 with a white label — white on blue is **6.77:1**, white on red is **3.89:1** and
white on yellow is **1.88:1**. There is therefore only one candidate for a filled control, and the
brief's discipline falls out of the maths rather than being asserted.

- **Red (`--accent-2` = `#e8482f`)** — structural/graphic only: the media block, the second stop of
  the media gradient, a chart series. Ink-on-red is 4.83:1, so red *can* carry an ink label, but it
  never fills a button: at the same size it would read as a heavier control than the blue one.
- **Yellow (`--geo-yellow` = `#f2b21a`)** — graphic only: the highlight mark and printed label
  blocks. Ink-on-yellow is 9.99:1, which is exactly why the `highlight` component pairs yellow with
  `{colors.text}` and never with white.

## Key choices

- **Depth is a hard offset, full stop.** `--shadow-1: 5px 5px 0 var(--border)` and
  `--shadow-2: 9px 9px 0 var(--border)` — `blur 0`, `spread 0`, referencing the ink token so the
  shadow can never drift from the rules. `--blur: none`, so `templates/lab.css` applies no
  `backdrop-filter` to `.card`. The one place a hard offset needed re-wiring is the primary button:
  the shared lab sets `.btn-primary`'s `box-shadow` from `var(--glow)`, not `var(--shadow-1)`, so
  `--glow` is defined as `3px 3px 0 var(--border)` — a smaller slab of ink, not a glow.
- **`--border-w: 3px` and every rule is ink.** `--border` and `--border-strong` are both `#14110f`;
  there is no second line colour in the kit. A 1px hairline would turn the sheet into a blog.
- **Corners are hard.** `--radius-sm: 0`, `--radius-md`/`--radius-lg`: `2px`, and
  **`--radius-pill: 2px` on purpose** — badges and avatars read as small squares with a hint of
  print rounding, never as lozenges. `--cut: 0px`: cut corners are the sibling `carbon` kit's
  device, and reusing them here would blur two kits into one.
- **Archivo Black without synthetic bold.** The display face is Archivo Black — which is Archivo's
  900 cut. Google's CSS2 API is asked for the *Archivo* variable family pinned to `wght@900` rather
  than the `Archivo+Black` alias, so the `Archivo` family name is served and the shared lab's
  700/650/600 heading weights resolve to the true black face with **no browser-synthesised bold**.
  The stack leads with `"Archivo"` (the served family) and keeps `"Archivo Black"` as the
  next fallback.
- **Space Mono for labels**, not JetBrains Mono: a mechanical, typewriter-derived mono reads as
  printed data on a Bauhaus sheet, and it keeps the kit's type apart from `carbon`'s JetBrains Mono.
- **Status colours escape the primaries by value, not hue.** The brand *is* red/blue/yellow, so
  `--danger` is a darkened brick (`#b3261e`), `--warn` a burnt amber (`#8a5300`) and `--info` a
  deep steel (`#0f5c8c`), with `--ok` a forest green. A bright `#ff0000` danger would be
  indistinguishable from `--accent-2`.
- **Different from `carbon` by construction.** `carbon` is dark, square and neon and cuts its
  corners; this kit is light, printed, dimensional, and rounds nothing but a 2px print edge.
- **Derived, not invented.** `--accent-soft` is a 12% tint of the accent, the offsets are
  `--geo-offset-sm/-lg` aliases of the same ink slab, and every shadow references `var(--border)`.

## Contrast — verified on solids

Nothing in this kit is translucent, so every ratio is computed directly against the flat hexes in
`tokens.css`. No compositing is involved. (Run `verify-dimensions.py` to reproduce the table.)

### Required pairs

| Pair | Foreground | Background | Ratio | Target |
|---|---|---|---|---|
| body text | `--text` `#14110f` | `--bg` `#f4f1ea` | **16.67:1** | ≥ 7:1 ✓ |
| secondary text | `--text-muted` `#4e463f` | `--surface` `#fffdf7` | **9.09:1** | ≥ 4.5:1 ✓ |
| button label | `--text-invert` `#ffffff` | `--accent` `#2b4bd8` | **6.77:1** | ≥ 4.5:1 ✓ |
| caption/hint | `--text-dim` `#6b625a` | `--bg` `#f4f1ea` | **5.29:1** | ≥ 4.55:1 ✓ |
| caption/hint | `--text-dim` `#6b625a` | `--surface` `#fffdf7` | **5.87:1** | ≥ 4.55:1 ✓ |
| caption/hint | `--text-dim` `#6b625a` | `--surface-2` `#f0ebe0` | **5.02:1** | ≥ 4.55:1 ✓ |

`--text-dim` is the pair that usually fails on a light kit, and here it has to clear **three**
grounds. `--surface-2` (`#f0ebe0`) is the *darkest* of the three, and it is the binding case for
dim-on-light — the pale card stock `--surface` is trivially easy, the bone panel is not. 5.02:1
leaves about 10% headroom, so if you lighten `--surface-2` toward white, re-run the check.

### Supplementary

| Pair | Ratio |
|---|---|
| `--text` on `--surface` | 18.49:1 |
| `--text-muted` on `--bg` | 8.19:1 |
| `--accent` text on `--bg` (links, `.table code`) | 6.00:1 |
| `--ok` / `--warn` / `--danger` / `--info` on `--surface-2` | 5.50 / 5.32 / 5.50 / 6.03:1 |
| `--text-invert` `#ffffff` on `--accent-2` `#e8482f` | 3.89:1 — **never used**; why red is not an action colour |
| `--text` `#14110f` on `--tertiary` `#f2b21a` (the highlight mark) | 9.99:1 |

## Trade-offs and deviations

- **Two things in the shared lab are outside the token contract.** `lab.css` hard-codes
  `border: 1px solid` on `.btn` (the `--border-w` token is used by `.card`, `.input`, `.badge`,
  `section.block`, `.tabs`, `.nav` and `.table`, but **not** by buttons), so this kit's buttons keep
  a 1px ink rim while every card and input carries the 3px rule. It also hard-codes
  `border-radius: 999px` for the toggle switch (`.toggle input`), `50%` for `.dot`, and `999px` for
  the progress `.bar` — none of which read a token, so on this kit the toggle knob and the status
  dots stay circular and the progress bar stays a pill. Neither is fixable from `tokens.css`; a
  project using the kit directly should set the border width and the radii by hand on those
  selectors. Nothing else in the lab escapes the square treatment.
- **`--glow` is not a glow.** The name is the lab's slot for `.btn-primary`'s `box-shadow`; here it
  carries `3px 3px 0 var(--border)`, a hard ink offset. A reader who assumes `--glow` means a light
  bloom will be surprised — the alternative was a flat primary button, which would be a worse lie.
- **`--bg` is a flat paper colour, so the masthead shows its own wash.** Unlike a gradient-ground
  kit, `templates/lab.css`'s masthead `linear-gradient(180deg, var(--bg-2), var(--bg))` resolves
  normally here, and the masthead sits a shade warmer than the page body.
- **Display tracking is barely tightened.** Archivo Black is a very wide face; `-0.01em` is about as
  far as it can be pushed before the counters start to close at small sizes.
- **`--warn` and `--info` are unusual on purpose.** A burnt amber and a steel blue are less
  "friendly" than the usual amber/sky, but the alternative was status colours that read as the brand
  red and brand blue. If a project needs louder status colours, change the primaries, not the
  statuses.
- **No orphaned tokens**: every colour declared in `DESIGN.md` is referenced by at least one
  component, so the linter's `orphaned-tokens` warning should not fire (unlike `glass`, which keeps
  its raw ramp stops unreferenced).

## When to use

Editorial and campaign pages, posters-on-the-web, dev-tool marketing that wants to look printed
rather than lit, dashboards that should read as a control board (bold rules code the columns for
free). Avoid for dense data tables (3px rules plus a 9px offset is a lot of ink per row), for
long-form reading, and anywhere the brand is quiet — this kit is loud by design.

## Verify

```bash
python tools/build.py --no-export --no-lint     # lab html + contract check
python "C:/Users/Lily/AppData/Local/hermes/cache/scratch/verify-dimensions.py"   # contrast table
```
