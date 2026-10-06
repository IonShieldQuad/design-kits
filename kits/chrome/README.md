# Chrome

**Liquid chrome on black — a metallic ramp, magenta action, cyan tertiary.**

Part of [design-kits](../../README.md). Index `08`, order `55`, mode `dark`, source `original`.

## Stance

Where the other dark kits pick one neon and glow, this one is **metal**. A four-stop chrome
ramp — specular white `#ffffff` → bright silver `#c9d0da` → mid steel `#7c8695` → dark steel
`#2b3038` — supplies the finish; magenta `#ff2e88` supplies the action; cyan `#35e3ff` is the
cool tertiary. Everything is outlined in hard 2px steel, radii are 2–6px, and the primary
button carries a rim-light rather than a bloom.

It is the **dark sibling of Summer Sunset** — same colour family (magenta + cyan over a
bold-line, small-radius language), opposite ground. Summer Sunset is a printed poster in
daylight; Chrome is polished metal in the dark.

## Key choices

- **A real metallic ramp, not a glow.** `--chrome-1..4` are exposed as extras and composed into
  `--chrome-gradient` (a 135° sweep white → silver → steel → dark steel → back) and
  `--chrome-sheen` (a 180° top highlight). The composed gradients live in `tokens.css` because
  the DESIGN.md `colors:` block only accepts plain colours; the four stops ship as
  `chrome-1..4`.
- **`--accent-2` is chrome silver `#c9d0da`.** The shared lab paints media, bars and avatars
  with `linear-gradient(--accent, --accent-2)`, so this single choice turns every lab gradient
  into **magenta → chrome**. It is the kit's signature in one line.
- **Magenta is the only action colour.** `--accent: #ff2e88`; hover lightens to `#ff5aa3`, so
  hover reads as *brighter metal*, not darker.
- **Cyan keeps a real job.** `--focus-ring` and `--info` are cyan `#35e3ff`, and `--chrome-cyan`
  exposes it for charts — without duplicating the neighbouring kit's signature (see below).
- **Hard 2px line work.** `--border-w: 2px`, `--border` is 20% silver, `--border-strong` 46%.
  The rim *is* the brand.
- **Dark ink on magenta.** White on `#ff2e88` is ~3.5:1, so `--text-invert` is near-black
  `#0b0d12` — **5.6:1** on the accent. Ink on a hot-pink enamel badge.
- **Sharp radii.** 2 / 4 / 6px, `--cut: 0px`. Machined, not rounded.

## Fonts, and why

- **Orbitron** (display) — a wide geometric retro-future face, tracked out to `.02em`. Width
  reads as machined metal, and it holds at both `h1` and card-title sizes.
- **Inter** (body) — neutral, so the display metal is the only loud thing on the page.
- **JetBrains Mono** (labels) — the instrument-panel voice, uppercase at `.20em` tracking,
  the widest label tracking among the dark kits.

## Trade-offs

- **`--accent-2` had to be silver, not cyan.** The brief names cyan as the second brand hue,
  but `--accent-2` is the one token the shared lab feeds into its media/bar/avatar gradients.
  Setting it to cyan would have produced *exactly* the `cyberpunk` kit's magenta → cyan
  gradients and made the two skins near-identical in the lab. Silver keeps the gradients
  metallic and keeps the kits distinct; cyan is honoured as the tertiary (`--focus-ring`,
  `--info`, `--chrome-cyan`). This is the single most important decision in the kit.
- **`--text-invert` is near-black.** Unusual on paper, correct in practice: the only way to
  keep AA on a magenta accent without whitening the type. Don't "fix" it.
- **The chrome gradient is prose + extras, not a `colors:` entry.** Gradients cannot go in the
  DESIGN.md `colors` block; the four stops do, and the composed gradients stay in `tokens.css`
  and in the Elevation & Depth prose.
- **`--info` shares the tertiary cyan.** The one deliberate brand/status overlap; `--info` is
  informational, never an action, so it cannot be mistaken for a button.

## How `chrome` stays distinct

- **vs `cyberpunk`:** cyberpunk is a *single-magenta* poster — magenta hairlines, cyan second
  accent, a soft neon bloom, `--border-w: 1px`, violet-black ground. Chrome is the opposite: a
  cooler, harder, **multi-stop metallic finish** with magenta → **silver** gradients (never
  magenta → cyan), steel-silver line work rather than magenta hairlines, a rim-light instead of
  a bloom, and `--border-w: 2px`. Same colour family, different material — the lab gradients do
  not match, which is what makes them read as two kits.
- **vs `summer-sunset`:** it is the deliberate **dark sibling** — same magenta/cyan family,
  same 2px bold-line and small-radius language — but with an inverted ground (near-black vs
  sunset gradient) and a chrome ramp that Summer Sunset does not have. Orange, the light kit's
  action colour, does not appear in Chrome at all.

## Verification

Contrast (`docs/KIT-SPEC.md` v1.1 targets; solid near-black grounds):

| Pair | Ratio | Target |
|---|---|---|
| `--text` on `--bg` | **17.58:1** | ≥ 7 |
| `--text-muted` on `--surface` | **8.51:1** | ≥ 4.5 |
| `--text-invert` on `--accent` | **5.55:1** | ≥ 4.5 |
| `--text-dim` on `--bg`, `--surface`, `--surface-2` | **6.51 / 6.08 / 5.64:1** | ≥ 4.55 |

All token contract names, including `--border-w`, are present. `python tools/build.py
--no-export --no-lint` reports `lab html OK` and **no** token-contract gaps.

`designmd lint`: **0 errors**. Warnings retained on purpose: `orphaned-tokens` on the status
colours, `--focus-ring`, the surfaces and the chrome/extra stops (the shared lab reads those
straight from CSS, and the composed `--chrome-gradient` / `--chrome-sheen` cannot live in the
DESIGN.md `colors:` block, which only accepts plain colours — the four stops ship as
`chrome-1..4`); and one `contrast-ratio` warning on `badge-accent`, where the linter reads
accent-on-tint as text. It mirrors the shared lab exactly — the accent badge is a tinted
surface — so it is a decorative pair, not a text pair.

## Use when

Developer tools, hardware and audio product pages, music and game UI, portfolios, and
dashboards that should feel like a machined panel. Not for long-form reading, and not where a
magenta error state could be confused with a magenta action.
