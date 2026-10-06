# Cyberpunk

**Neon on near-black — loud, glowing, still legible.**

Part of [design-kits](../../README.md). Index `04`, order `40`, mode `dark`, source `original`.

## Stance

This is the loud end of the library. A near-black ground with a violet cast, one hot magenta
action colour, and two secondaries — electric cyan for gradients and media, acid yellow for
hazard marks. It should be recognisable as a neon sign from across the room.

The kit refuses one thing that most "dark + neon" themes get wrong: it never lets glow stand
in for structure. Borderlines are magenta hairlines rather than greys, type is a clean
near-white, and status colours are deliberately pulled off the brand hues so a red "failed"
can never be read as a pink button.

## Key choices

- **Magenta is the only action colour** (`#ff2e88`). Cyan (`#22e0ff`) is the second accent and
  is used for gradients, media, bars and the focus ring; acid yellow (`#e8ff2e`, extra token
  `--cyberpunk-acid`) is reserved for hazard marks and a third chart series.
- **Dark type on neon.** White on `#ff2e88` is only ~3.5:1. Instead of dulling the magenta,
  `--text-invert` is near-black `#0b0713` — **5.7:1** on the accent, and it reads like ink on
  a lit sign. This is the kit's signature move.
- **Magenta hairlines.** `--border` is 30% magenta and `--border-strong` is 62% magenta, so
  panels sit on a lit grid instead of grey rules.
- **Bloom, not glass.** `--glow` (a 1px magenta ring plus two magenta shadows) is used on the
  primary button only; `--blur: none` keeps every edge hard.
- **Snap motion.** `--dur: .12s` with a fast-out `--ease` — this kit flicks, it does not glide.
- **Hard corners.** 3 / 4 / 6px radii, pills only on badges and avatars. `--cut: 10px` is
  exported for consumers who want a `clip-path` corner notch instead.

## Trade-offs

- **Status colours sit outside the neon set** (mint `#2fe6a0`, orange-amber `#ff9f1c`, true red
  `#ff3b30`, indigo `#7d8cff`). They are less "cyberpunk" in isolation, but they stay
  distinguishable from magenta/cyan/acid yellow, which matters more.
- **`--cut` is declared but the shared lab cannot apply it** — the lab renders `--radius-*`
  corners only. Downstream projects can use `--cut` with `clip-path`; the lab shows the hard
  3–6px corner. Deliberate: the token is exposed for real use, not faked in the preview.
- **Cards barely lift off the ground.** `--shadow-1` is near-black on near-black; on this kit
  elevation is signalled by the magenta hairline and `--shadow-2`'s cyan bloom instead.
- **Not for long-form reading.** 17.8:1 body text is comfortable, but the surrounding neon
  is designed to sit at the top of a page.

## Verification

Contrast (`docs/KIT-SPEC.md` targets): `--text` on `--bg` **17.9:1** (≥7) · `--text-muted` on
`--surface` **7.8:1** (≥4.5) · `--text-invert` on `--accent` **5.7:1** (≥4.5). All token
contract names present. Builds clean with `python tools/build.py`.

`designmd lint`: **0 errors**. The remaining warnings are `orphaned-tokens` only — `--ok`,
`--warn`, `--danger`, `--info`, `--focus-ring` and `--glow` are consumed by CSS status
surfaces, not by a front-matter component block. Kept deliberately.

## Use when

Games, music and media UI, launch screens, posters-that-happen-to-be-web, or a dashboard that
should feel like a cockpit. Not for medical, financial or long-form reading interfaces.
