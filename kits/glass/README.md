# Glass

**Restrained glassmorphism.** A soft pastel gradient ground (rose / lilac / mint / sky)
seen through genuinely translucent white panels, with hairline light edges and layered soft
shadows instead of borders. Subtle colours, deep ink, one periwinkle-indigo action colour.

- Kit: `glass` · index `07` · order `70` · mode `light` · source `original`
- Fonts: Plus Jakarta Sans (display + body) · JetBrains Mono (labels)
- Tags: `light`, `soft`, `modern`, `glass`

## Stance

Most "glassmorphism" fails because the glass is decoration: a solid card with a blurry
picture behind it. Here the glass is structural — surfaces are `rgba(255,255,255,.58)`,
`templates/lab.css` applies `var(--blur)` (`blur(20px) saturate(180%)`) to every `.card`,
and the ground is visible *through* the panels at all times. The pastels are washes, not
statements; the only saturated element in the kit is the action colour.

## Key choices

- **`--blur` is real and load-bearing.** `blur(20px) saturate(180%)`. The saturate boost
  matters twice over: a plain blur turns pastel ground into grey milk behind the panel, and
  over a smooth gradient the saturate is the *visible* part of the effect — there is no
  high-frequency detail behind a lab card for a blur to smear. The frost reads because the
  backdrop is tinted and the panel floats, not because pixels are smeared.
- **Light borders, not dark ones.** `--border` is `rgba(255,255,255,.70)` — an edge
  *highlight*, and the brief's hairline light border. Structure comes from `--shadow-1` /
  `--shadow-2`, two shadow layers each plus an `inset 0 1px 0` top highlight: a 58%-white
  panel over a pastel ground sits only a few percent away from it in luminance, so the
  shadow is what defines a card. `--border-strong` is the exception — a faint ink hairline
  (`rgba(28,32,51,.14)`), because a second *white* line has no visible difference on a
  pastel ground and the emphasised rule needs to read.
- **Two surface opacities, not two colours.** `--surface` = 58% white, `--surface-2` = 65%
  white. Elevation is opacity + shadow; hue is constant.
- **The action colour is deeper than the reference swatch.** The brief's `#5b6bff` renders
  white label text at 4.21:1 — under AA. `--accent` is `#4550e8`, which measures 5.89:1
  against white and 4.70:1 against its own tint over a glass panel (a nearly-white panel
  makes that second number the tight one). Everything else in the brief is literal.
- **One family.** Plus Jakarta Sans for display *and* body; the ground is colourful, so the
  type is not. Display tracking is tight (`-0.02em`) — the deliberate inverse of the
  sibling `cyber-angel` kit, which opens its headings up.
- **Derived, not invented.** `--accent-soft`, `--shadow-*`, `--glass-sheen` and
  `--glass-edge` are `rgba()`/`linear-gradient()` expressions, not new hues.

## Contrast — the compositing maths

The ground is a gradient and surfaces are translucent, so a single flat hex proves nothing.
Two worst cases are used:

- **Ground worst case** = the *lightest* ramp stop. Of `#ffd9e8`, `#dcd6ff`, `#d3f5ea`,
  `#d6ecff`, `#eef1f8`, the highest relative luminance is `#eef1f8` (the base the ramp
  settles onto) at **L = 0.8787**.
- **Surface worst case** = white at α = .58 over that stop, composited per channel on the
  sRGB values the browser is blending: `0.58×255 + 0.42×(238, 241, 248)` → `#f8f9fc`,
  **L = 0.9479**. Because compositing only *lightens* the stop, the composited surface is
  the harder case for dark text, and it bounds every other stop and every lower-opacity
  overlay.

### Required pairs

| Pair | Foreground | Background (worst case) | Ratio | Target |
|---|---|---|---|---|
| body text | `--text` `#1c2033` | lightest stop `#eef1f8` | **14.25:1** | ≥ 7:1 ✓ |
| secondary text | `--text-muted` `#454b63` | composited `--surface` `#f8f9fc` | **8.18:1** | ≥ 4.5:1 ✓ |
| button label | `--text-invert` `#ffffff` | `--accent` `#4550e8` | **5.89:1** | ≥ 4.5:1 ✓ |

The two required dark-text pairs are comfortable because the ramp is pastel, not saturated:
even the *finish* colour `#eef1f8` is 88% luminance, and a 58% white panel over it is
lighter still. The tight pair in this kit is not one of the three — it is accent text on the
accent tint (4.71:1), which is why `--accent` had to go deeper than the brief's swatch.

### Supplementary

| Pair | Ratio |
|---|---|
| `--text` on composited `--surface` | 15.31:1 |
| `--text-muted` on the raw worst-case stop (no panel behind it) | 7.61:1 |
| `--accent` text on `--accent-soft` over composited `--surface` | 4.71:1 |
| `--ok` / `--warn` / `--danger` / `--info` on composited `--surface-2` | 5.61 / 5.44 / 5.07 / 5.65:1 |
| `--text-dim` on composited `--surface` (captions, decorative) | 4.26:1 — intentional |

Note on `saturate(180%)`: it is applied to the backdrop *before* the panel is composited,
and it darkens a near-white stop at most marginally, so the composited figure above remains
a valid upper bound on lightness.

## Linter

`npx -y -p @google/design.md designmd lint kits/glass/DESIGN.md` → **0 errors, 24
warnings**, all of them consciously kept:

| Count | Rule | Why it stays |
|---|---|---|
| 17 | `broken-ref` | `borderColor`, `boxShadow`, `backdropFilter` and `backgroundImage` are not in the linter's component sub-token vocabulary (`backgroundColor`, `textColor`, `typography`, `rounded`, `padding`, `size`, `height`, `width`). For this kit they are the substance of the spec — the hairline light edge, the two-layer shadows and the load-bearing `blur(20px) saturate(180%)` — so they stay. |
| 2 | `contrast-ratio` | False positives from un-composited alpha. Both compare accent `textColor` against `rgba(69,80,232,.12)` without compositing it, so the linter ends up comparing the colour to itself — hence the giveaway `1.00:1`. Composited properly over a glass panel: **4.71:1**. |
| 5 | `orphaned-tokens` | `rose`, `lilac`, `mint`, `sky` and `surface-solid` are the documented ramp stops and the opaque fallback. They are consumed by `--bg` and by anything that needs a solid equivalent (print, email); no component references them directly because components sit *on* the ramp. |

## Trade-offs and deviations

- **`--accent` is `#4550e8`, not the brief's `#5b6bff`.** `#5b6bff` gives white-on-accent
  4.21:1 and would fail the contract at the button; on glass it is worse still, because
  accent text on the accent tint over a nearly-white panel is the *tightest* pair in the
  kit. `#4550e8` measures 5.89:1 on white and 4.70:1 on its own tint, and still reads as
  the intended periwinkle-indigo.
- **`--bg` is a gradient, so the masthead loses its own wash.** `templates/lab.css` builds
  the masthead as `linear-gradient(180deg, var(--bg-2), var(--bg))`; feeding a gradient into
  a gradient stop is invalid CSS, so that declaration is dropped and the masthead is
  transparent — the page gradient shows through instead. The result is visually correct
  (and arguably better) but it is a known consequence of a gradient `--bg`, not an accident.
- **The gallery preview will look paler than the lab.** `tools/build.py` renders the
  gallery card as `background:{bg}` followed by its own `background-image`, which overrides
  a gradient `--bg`. The kit's colour survives only in the swatch bar there. The **lab page
  is the reference view.**
- **Borders are white.** On a bright ground a white hairline is nearly invisible over the
  lightest stops. That is intentional (depth via shadow, per the brief), but the consequence
  is real: this kit relies on `--shadow-1` to define a card, and `section.block`'s
  `border-top` rule — which the shared lab draws with `--border` — is a whisper rather than
  a line. `--border-strong` is therefore a faint **ink** hairline so the emphasised rules
  (table headers, the fallback button edge) still read. Removing `--shadow-1` would flatten
  the kit completely.
- **`--bg` uses pixel gradient stops, not percentages.** The body's gradient box is the whole
  document, so a `0% → 100%` ramp smears the four pastels over several thousand pixels and
  the viewport renders as flat near-white — the first build did exactly that and it was
  invisible at the top of the page. Fixed-length stops keep the same wash in view at any page
  length; the ramp still settles on `#eef1f8`, so the worst-case stop used for the contrast
  maths is unchanged.
- **`--text-dim` sits under 4.5:1** — captions and placeholders only, never body copy.
- **Nested glass is avoided.** Two translucent panels stacked composite to nearly opaque,
  which reads as flat. The lab's `.card-elevated` uses the higher-opacity surface rather
  than a second blur layer.

## When to use

Modern SaaS marketing and app shells, overlays, hero cards, dashboards that need to feel
light rather than dense, anything where the brand wants pastel colour without shouting.
Avoid for data-dense tables on white paper, print (use `{colors.neutral}` and
`{colors.surface-solid}`), and anywhere `backdrop-filter` is unavailable.
