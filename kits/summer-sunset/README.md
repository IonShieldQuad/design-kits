# Summer Sunset

**80s synthwave poster — sunset sky, bold lines, orange · cyan · magenta.**

Part of [design-kits](../../README.md). Index `05`, order `50`, mode `light`, source `original`.

## Stance

A risograph sunset poster rebuilt as a working UI kit. A warm sunset-sky gradient ground,
**bold 2px aubergine outlines** on every surface, and three neon colours with three jobs:
orange `#ff7a1a` sets, cyan `#06a9c4` cools, magenta `#ff2ea6` bleeds through the ramp and
the ground's middle band. Ink is deep aubergine `#2a1136` — never orange — so the poster is
still readable at paragraph length.

It is a **light** kit: the neon is the light source, the paper is the ground.

## Key choices

- **Bold graphic lines.** `--border-w: 2px`, every panel/input/button/badge outlined in
  `rgba(42,17,54,.26)`, hardened to `.60` for emphatic rules. The line work is drawn, not
  implied — this is the kit's identity.
- **A gradient ground.** `--bg` is `linear-gradient(180deg, #fff5ec, #ffe3ca 40%, #ffd1de 74%,
  #eedaf5)` — peach → apricot → **magenta band** → violet haze. `--bg-2: #fff0e2` is the solid
  stand-in for exports.
- **Orange is the action, and nothing else is.** `--accent: #ff7a1a`. It fills the primary
  button, inks the links in the shared lab, and is the sun disc. It is never body copy.
- **Cyan is the cool counterweight.** `--accent-2: #06a9c4` drives the media/bar/avatar
  gradients; the keyboard focus ring is a deep cyan `#077184`, so focus is never mistakable
  for the orange hover.
- **Magenta is the third colour.** `--summer-sunset-magenta: #ff2ea6`, carried by the ramp
  (`--summer-sunset-ramp`) and by the ground's middle band. Emphasis, never a second CTA.
- **Dark ink on orange.** White on `#ff7a1a` is ~2.4:1, so `--text-invert` is the same
  aubergine as the body ink — **6.5:1** on the accent. Screen-print ink on a warm poster.
- **Hard-offset shadows, not bloom.** `--glow` is `3px 3px 0` aubergine — a printed sticker
  shadow. The one soft halo (`--summer-sunset-halo`) lives in the extras.
- **Small printed radii.** 4 / 6 / 8px, `--cut: 0px`. No notches, no big rounds.

## Fonts, and why

- **Audiowide** (display) — the canonical 80s synth/arcade wide letterform. It reads as a
  poster headline at `h1` size without becoming a costumed sci-fi face, and it is a single
  weight, so it cannot be over-used.
- **Inter** (body) — neutral, so the retro display face is the only thing shouting.
- **Share Tech Mono** (labels) — a narrow, analogue-feeling terminal mono. Chosen over
  JetBrains Mono to keep the kit's voice distinct from the other technical kits in the set.

## Trade-offs

- **A gradient `--bg` invalidates the lab masthead's own `background` shorthand** (CSS does
  not allow a gradient as a colour stop inside another gradient), so the masthead renders
  transparent and the page gradient shows straight through — seamless. A side effect: the
  masthead loses its local orange accent wash in the shared lab; orange still appears in the
  eyebrow, buttons, tints and banners. Deliberate — the full sky is worth more than a wash,
  and it is what makes the kit read at thumbnail size.
- **`--text-invert` equals `--text`.** Unusual on paper, correct in practice: the only way to
  keep AA on an orange accent without whitening the type. Don't "fix" it.
- **Orange links on the warm ground are low-contrast** (orange `#ff7a1a` on the cream stop is
  ~2.4:1). This is inherent to a saturated light-accent kit in the shared lab, where links are
  always `--accent`. The kit's *text* colours all clear their targets; for long-form links in a
  real project, underline them or use `--focus-ring`/`--info` ink.
- **Magenta is an extra, not a contract token.** It appears in the ramp, the ground and the
  sun extras; it does not drive a component, which is exactly what keeps it from becoming a
  second action colour.

## Verification

Contrast (`docs/KIT-SPEC.md` v1.1 targets; `--bg` checked against its darkest stop `#ffd1de`,
the magenta band):

| Pair | Ratio | Target |
|---|---|---|
| `--text` on `--bg` (worst stop) | **12.52:1** | ≥ 7 |
| `--text-muted` on `--surface` | **8.38:1** | ≥ 4.5 |
| `--text-invert` on `--accent` | **6.54:1** | ≥ 4.5 |
| `--text-dim` on `--bg` (worst), `--surface`, `--surface-2` | **4.96 / 6.51 / 5.96:1** | ≥ 4.55 |

All token contract names, including `--border-w`, are present. `python tools/build.py
--no-export --no-lint` reports `lab html OK` and **no** token-contract gaps.

`designmd lint`: **0 errors**. Warnings retained on purpose: `orphaned-tokens` on the status
colours, `--focus-ring` and the gradient-stop colours (the shared lab reads those straight from
CSS, and the `--bg` **gradient itself is not expressible in the DESIGN.md `colors:` block** —
the stops ship as `bg-stop-1..4` and the ramp stops as `ramp-peach/orange/magenta/violet`,
with the gradients defined in `tokens.css`); and three `contrast-ratio` warnings
(`button-secondary`, `button-secondary-hover`, `badge-accent`) where the linter reads accent-on-
tint as text. Those three mirror the shared lab exactly — the secondary button and the accent
badge are tinted surfaces, not body copy — so they are decorative pairs, not text pairs.

## Use when

Launch pages, game and music UI, event and ticketing sites, retro-branded consumer apps —
anything that should feel like a poster. Not for dense data tooling or long-form reading.
