# Mecha Pilot

**The pilot's instrument panel.** Gunmetal under a CRT scan line, an amber readout lamp for the one
thing that acts, a cyan channel for data, a warning red — and three drawn instruments: a targeting
reticle, a range scale and hazard tape. Nothing in it is smooth.

- Kit: `mecha-pilot` · order `150` · mode `dark`
- Fonts: Chakra Petch · Saira · Share Tech Mono
- Tags: `dark` `mecha` `hud` `cockpit` `technical` `instrumentation`
- Source: original

## Stance

A cockpit is not a page. It is a dense, backlit board of readouts that a pilot glances at, so this
kit is **instrumentation first**: panels are flat plates, the depth is a hard offset (a plate
standing proud of the floor), and the identity comes from the instruments the panel is built from —
a reticle that means *target*, a scale that means *measured*, and a hazard tape that means *careful*.
Every surface here is looked **at**; nothing is looked through.

### Differentiated on purpose from two neighbours

| | `inside-the-machine` | `carbon` | **`mecha-pilot`** |
|---|---|---|---|
| Premise | industrial hardware **texture** | neon product page | **instrumentation** |
| Accent / 2nd | amber + green phosphor | neon cyan + violet | **amber + calm cyan** |
| Depth | **engraved** inset seams | blurred drop + chamfer | **hard zero-blur offset** |
| Corners | 2–4px | **cut** (clip chamfer) | **square, no chamfer** |
| Type | mono-first | grotesque-first | **Chakra Petch display + readout mono** |
| Motifs | lamps, graticule | cut corner | **reticle · scale · hazard tape** |

Mecha Pilot borrows none of these: there is no weave, no vent, no engraving, no neon and no chamfer.
Its differentiators are *a drawn reticle, a calibrated scale and a warning tape* — devices that only
exist on an instrument panel.

## Ground truth

| Token | Value | Note |
|---|---|---|
| `--bg` | scan-line field over hard gunmetal bands `#10151b`/`#0d1116` | a CRT floor, banded not faded |
| `--bg-2` | `#0d1116` | solid stand-in for exports/masthead |
| `--surface` | `#171d24` | the instrument plate (lightest ground) |
| `--surface-2` | `#111720` | recessed readout well, inputs, tile base |
| `--text` | `#e8eef5` | 14.5:1 on `--surface` |
| `--text-muted` | `#9aa6b3` | 6.9:1 on `--surface` |
| `--text-dim` | `#93a0ae` | 6.4:1 on `--surface` — the binding ground |
| `--text-invert` | `#0d1116` | panel ink on the amber lamp, 10.0:1 |
| `--accent` | `#ffab2b` | READOUT amber — the only action colour |
| `--accent-hover` | `#ffbc4d` | the lamp one notch brighter |
| `--accent-2` | `#3fd0e6` | DATA cyan — media, charts, telemetry |
| `--accent-soft` | `rgba(255,171,43,.16)` | derived: a 16% tint of `--accent` |
| `--accent-ink` | `#ffc061` | the amber **as text** — 10.5:1 on `--surface` |
| `--ok` / `--warn` / `--danger` / `--info` | `#4ee08a` / `#ffd24a` / `#ff5a4d` / `#3fd0e6` | annunciator lamps, one job each |
| `--border` / `--border-strong` | `#2b3540` / `#48535f` | bezel hairline / instrument rim |
| `--focus-ring` | `#ffc061` | amber readout ring |
| `--radius-sm/md/lg/pill` | `0px` | an instrument bezel is square |
| `--cut` | `0px` | no chamfer — `carbon` owns that |
| `--shadow-1` / `--shadow-2` | `4px 4px 0` / `6px 6px 0` + 1px inset bezel | zero-blur offsets only |
| `--glow` | `0 0 0 1px / 3px / 5px` amber rings | a **stepped** phosphor bloom, not a blur |
| `--blur` | `none` | a cockpit panel is not frosted glass |

## Derived, and why

- `--accent-soft: rgba(255,171,43,.16)` — a 16% tint of `--accent`, expressed as `rgba()` rather than
  re-typed as a hex, so it can never drift from the amber.
- `--text-invert` **is** the ground (`#0d1116`): the panel ink printed on the amber lamp. `#ffab2b`
  is a fill, so white on it would be ~1.9:1; the panel ink clears 10.0:1.
- `--accent-ink: #ffc061` — the fill amber is legible as a *fill* but is the wrong tone for a small
  label; the ink is the same family lifted until it reads as text (10.5:1, and 7.6:1 on its own tint).
- `--warn: #ffd24a` is a **yellower** caution than the amber readout on purpose: a caution chip must
  never be mistaken for the action plate. The two adjacent lamps are the classic caution/warning pair.
- `--ok` / `--info` reuse the green and cyan of the annunciator: one lamp, one meaning, both directions.
- `--text-dim: #93a0ae` is set by the *lightest* ground, `--surface #171d24`, at 6.4:1 — solving it
  against an average ground is how dim captions end up failing on the one stop that matters.

## The three signature devices

Three motifs, three **different** jobs. Each is a background value, so the tiles paint rather than
merely apply.

- `--mecha-pilot-reticle` — **the symbol.** DRAWN inline SVG (base64): concentric rings with a dashed
  radial tick ring (a 6px stroke on a `1.5 6` dasharray), a gapped crosshair, four corner brackets and
  a top index triangle, over a scope face of hard concentric bands. A gradient cannot draw a ring with
  radial ticks; only vector can.
- `--mecha-pilot-scale` — **the measurement.** DRAWN inline SVG: a heading/range tape with hard minor
  ticks every 6px, taller major ticks every 30px, mono numerals, end brackets and a bright index
  needle. A repeating gradient makes an even comb with no majors — that is a pattern, not a scale.
- `--mecha-pilot-hazard` — **the warning.** Pure repeating gradient: hard 45° amber/black stripes
  under a 2px amber rule at both edges. It is the instrument-panel hazard tape.

The CRT scan-line field is deliberately **not** a fourth tile: it lives on the page floor (`--bg`) and
on the media panel (`--media-bg`, which reads as a lit screen — scan lines, a data grid and a sweep
band), which is where a screen belongs.

**Non-flatness, measured.** Each token was rendered as `background:` on a 168×72 box over
`--surface-2` in headless Chromium, screenshotted, and its per-tile pixel standard deviation taken
with PIL (luma, 0.2126/0.7152/0.0722). A flat plate scores ~0.

| Tile | std-dev (luma) | luma range | job |
|---|---|---|---|
| `--mecha-pilot-reticle` | **22.50** | 15–184 | the symbol |
| `--mecha-pilot-scale` | **30.10** | 19–210 | the measurement |
| `--mecha-pilot-hazard` | **82.41** | 14–180 | the warning |

No tile renders flat: the two drawn instruments carry their variance structurally, and the hazard
tape is the highest-variance tile in the kit.

## Nothing smooth — all five doors shut

1. **Curves** — every `--radius-*` is `0px`, and `--check-appearance: none` with a `--check-bg` box
   squares the native checkbox and radio (which ignore `border-radius`, so a "0px" kit would otherwise
   still render round ones).
2. **Soft shadows** — `--shadow-1`/`--shadow-2` are zero-blur offsets (`4px 4px 0`, `6px 6px 0`), and
   `--btn-shadow` gives *every* button variant the same `2px 2px 0` key-offset. The only bloom in the
   kit, `--glow`, is a phosphor halo **stepped into three concentric hard rings** — no blur radius at
   all — because it is a lit lamp and the register permits a lit lamp; the "glow" and the "no soft
   shadow" rule are reconciled rather than one of them ignored.
3. **Gradients** — `--bg` is banded with px stops that share a position, plus a 1px CRT scan line;
   `--wash` is off (so the lab's default smooth radial bloom never appears); `--media-bg` is hard
   sweep bands over a scan-line field and a data grid; `--fill-bg` is a hard-stopped segmented lamp
   bar. There is no interpolated ramp anywhere.
4. **Scaled artwork** — every motif is vector line art drawn at the size it displays; nothing is
   upscaled, so nothing can blur. `--pixel-render: pixelated` is set so any raster a consumer adds
   stays hard-edged.
5. **Blur** — `--blur: none`; the lab's `backdrop-filter` resolves to `none`, and no kit rule adds one.

## Contrast (measured, not eyeballed)

Computed by script from the declared tokens; WCAG relative-luminance, graded against the ground each
ink actually sits on. The binding ground for a dark kit is the **brightest** one, here `--surface`
(`#171d24`). `--accent-soft` composites are of the tint **over** that ground.

| Pair | on `--bg` top | on `--bg` low | on `--surface` | on `--surface-2` |
|---|---|---|---|---|
| `--text` | 15.70 | 16.21 | 14.53 | 15.40 |
| `--text-muted` | 7.40 | 7.65 | 6.85 | 7.26 |
| `--text-dim` | 6.88 | 7.11 | **6.37** | 6.75 |
| `--accent-ink` | 11.32 | 11.69 | 10.48 | 11.11 |
| `--accent-ink` on `--accent-soft` | 8.36 | 8.69 | **7.58** | 8.14 |
| `--ok` | 10.79 | 11.14 | 9.98 | 10.58 |
| `--warn` | 12.72 | 13.14 | 11.77 | 12.48 |
| `--danger` | 5.96 | 6.15 | **5.51** | 5.84 |
| `--info` | 9.93 | 10.26 | 9.19 | 9.75 |

Other required pairs: `--text-invert` on `--accent` **10.02:1** (≥4.5); `--focus-ring` on `--surface`
**10.48:1** (≥3).

**Worst pair: `--danger` `#ff5a4d` on `--surface` `#171d24` = 5.51:1** — a danger badge sitting inside
a card. It clears the 4.5 bar with room; the whole table is comfortably above target, and the tightest
*text* tier is `--text-dim` at 6.37:1, well clear of 4.55.

## Trade-offs

- **Square, opaque, dense.** The kit has no radius, no translucency and no air. That is the register,
  and it makes it a poor fit for calm or editorial work — that is `quiet` or `zen-garden`.
- **Amber is warm and loud.** It is the fastest way to make the one action findable on a dark panel,
  but it collides with any brand that already owns orange, and it means the caution lamp had to be
  pushed yellower to stay distinct.
- **The glow is stepped, not blurred.** It reads as a lit lamp, but a very large control with the
  three-ring bloom can look graphic; keep it to one glowing element per view.
- **The reticle and scale are line art, not a layout.** A kit is judged at 200×120 and the tiles carry
  the identity; the kit does not reproduce a specific cockpit screen.
- `--pixel-render: pixelated` is declared for consumers who drop a raster in; the kit's own artwork is
  vector and unaffected.

## When to use

Cockpit and HUD surfaces: sim/game UI, telemetry and mission consoles, device and network
dashboards, anything that should read as an instrument panel rather than a marketing page. Avoid it
for long-form reading, calm editorial, or light contexts.

## Files

`DESIGN.md` (normative values) · `tokens.css` (the contract) · `kit.json` (gallery metadata) ·
`index.html`, `tokens.json`, `tailwind.theme.json`, `theme.css` (generated by
`python tools/build.py --only mecha-pilot`).
