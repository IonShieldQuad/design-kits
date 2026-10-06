# Cyber Angel

**Celestial-tech.** A pearl/ice light theme ground, one periwinkle-violet action colour,
ice-cyan as its companion, a whisper of lavender, and depth made of light instead of
shadow. Calm, airy, slightly otherworldly — the opposite of cyberpunk.

- Kit: `cyber-angel` · index `06` · order `60` · mode `light` · source `original`
- Fonts: Sora (display) · Inter (body) · JetBrains Mono (labels)
- Tags: `light`, `soft`, `cool`, `ethereal`

## Stance

Cyberpunk is a city at night, overclocked. Cyber Angel is the same intelligence, calm. So
the kit commits to three rules:

1. **Nothing dark.** The darkest ink is `#1a2147`; there is no black and no grey shadow.
2. **One action colour.** Periwinkle-violet `#5b5ce8` is the only thing that ever looks
   like a button. Ice-cyan `#7cc8f0` is a *gradient partner*, never an action.
3. **Depth is luminous.** Elevation is a wide, tinted halo. `--blur` is `none`: this kit's
   surfaces are crisp, and frost is explicitly the sibling `glass` kit's job.

## Key choices

- **The action colour is deeper than the brief's tint.** `#8fa8ff` (periwinkle) and
  `#a8e8ff` (ice) are kept, but as *ambience* tokens (`--angel-periwinkle`, `--angel-ice`,
  plus `--angel-halo`, `--angel-aurora`, `--angel-glow-soft`). Neither can carry white text
  (white on `#8fa8ff` is ~2.0:1), so promoting either to `--accent` would break the contract
  at the button. The action colour is `#5b5ce8`, which clears 5.1:1 against white.
- **Display tracking is positive.** `--tracking-display: .015em` against the usual
  `-0.02em`. It is what makes a big Sora heading read as airy rather than editorial-brutal.
- **Rounded, not bubbly.** 10 / 14 / 20px, `--cut: 0px`. Corners are soft but the geometry
  stays legible at thumbnail size.
- **Desaturated status colours.** `#0f7350` / `#8f5c00` / `#cc3350` / `#4553d6` are all
  darker than their default cousins so badge and alert text stays readable on a near-white
  ground.
- **Derived, not invented.** `--accent-soft`, `--angel-halo` and the shadow colours are
  expressed as `rgba()` over `--accent` / `--text`; the gradients in `--angel-aurora` are
  the accent → periwinkle → ice ramp. The only literals are the base palette.
- **`--accent-soft` is .08, not .14.** A thicker accent tint is prettier, but accent text
  sitting on it (`badge-accent`, the active nav pill, `code.inline`) measures 4.44:1 at
  `.10` and only clears 4.5:1 at `.08` or below. The tint is quietly reduced so the
  component passes.

## Contrast (WCAG 2.1)

`--bg` is a flat hex here, so the checks are simple. All ratios were computed against the
real composites, not eyeballed.

| Pair | Foreground | Background | Ratio | Target |
|---|---|---|---|---|
| body text | `--text` `#1a2147` | `--bg` `#f6f8ff` | **14.63:1** | ≥ 7:1 ✓ |
| secondary text | `--text-muted` `#646e96` | `--surface` `#ffffff` | **4.98:1** | ≥ 4.5:1 ✓ |
| button label | `--text-invert` `#ffffff` | `--accent` `#5b5ce8` | **5.07:1** | ≥ 4.5:1 ✓ |

Supplementary (not contract-mandated, checked so nothing looks broken):

| Pair | Ratio |
|---|---|
| `--text-muted` on `--surface-2` `#f1f4fd` | 4.53:1 |
| `--accent` text on `--accent-soft` over `--surface` | 4.56:1 |
| `--ok` / `--warn` / `--danger` / `--info` on `--surface-2` | 5.32 / 5.16 / 4.59 / 5.52:1 |
| white on `--accent-hover` `#4647cf` | 6.86:1 |
| `--text-dim` on `--surface` (tertiary, decorative only) | 2.95:1 — intentional |

## Linter

`npx -y -p @google/design.md designmd lint kits/cyber-angel/DESIGN.md` → **0 errors, 23
warnings**, all of them consciously kept:

| Count | Rule | Why it stays |
|---|---|---|
| 16 | `broken-ref` | `borderColor`, `boxShadow` and `backgroundImage` are not in the linter's component sub-token vocabulary (`backgroundColor`, `textColor`, `typography`, `rounded`, `padding`, `size`, `height`, `width`). They carry real spec value here — the hairline, the glow, the aurora gradient — so they stay rather than being deleted to quiet a warning. |
| 4 | `contrast-ratio` | False positives from un-composited alpha. Three compare `textColor` against a `transparent` / `rgba()` background the linter does not composite — it evaluates `rgba(91,92,232,.10)` as the accent itself, hence the giveaway `1.00:1`. Measured properly: secondary button **4.78:1** on `--bg` and **5.07:1** on `--surface`; ghost **4.70:1**; `badge-accent` and the active nav pill **4.56:1**. |
| 3 | `orphaned-tokens` | `periwinkle-soft`, `ice` and `lavender` are documented palette entries consumed by `--angel-halo` / `--angel-aurora` in `tokens.css`; no component references them because they are ambience, never text grounds. |

## Trade-offs and deviations

- **`--accent` is not the brief's literal swatch.** Documented above; it is the difference
  between a pretty tint and an accessible button.
- **`--blur: none`.** The contract requires the token; this kit sets it to `none` because
  crisp is the point. Cards then rely on `--shadow-1` + `--border` for separation.
- **White initials on the shared gradient avatar** (`.avatar` in `templates/lab.css` pins
  `--text-invert`) sit on the cyan end of `--angel-aurora` at roughly 2:1. That element is
  decorative and the lab's markup hardcodes the pairing; the token set cannot fix it without
  darkening `--accent-2` to the point where it is no longer ice-cyan. Flagged, accepted.
- **`--text-dim` fails 4.5:1 by design** — it is captions and placeholders only.

## When to use

Calm/wellness products, soft branding, hero sections, editorial intros, anything that wants
to feel serene and precise. Avoid for dense dashboards and anything that needs to feel loud.
