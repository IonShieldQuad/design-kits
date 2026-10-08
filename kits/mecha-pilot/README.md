# Mecha Pilot

**The pilot's military HUD.** A dark olive board under a CRT scan line and a hard instrument
grid, a phosphor-green readout for the one thing that acts, a cyan channel for data — and three
drawn instruments: a targeting reticle, a range scale and caution tape. Green is nominal, amber is
caution, red is master caution. Nothing in it is smooth.

- Kit: `mecha-pilot` · order `150` · mode `dark`
- Fonts: Chakra Petch · Saira · Share Tech Mono
- Tags: `dark` `mecha` `hud` `military` `cockpit` `instrumentation`
- Source: original

## Stance

A cockpit is not a page. It is a dense, backlit board of readouts that a pilot glances at, so this
kit is **instrumentation first**: panels are flat plates, the depth is a hard offset (a plate
standing proud of the floor), and the identity comes from the instruments the panel is built from —
a reticle that means *target*, a scale that means *measured*, and a caution tape that means *careful*.
Every surface here is looked **at**; nothing is looked through.

The register is a **military flight/weapons HUD**: phosphor green is the light, and the palette is a
readout ladder rather than a brand. A green panel means the system is nominal, an amber legend means
caution, a red legend means master caution / weapon armed. The two loud hues that used to be
decoration are now the two cautions, and the whole panel reads green.

### Differentiated on purpose from two neighbours

| | `inside-the-machine` | `carbon` | **`mecha-pilot`** |
|---|---|---|---|
| Premise | industrial hardware **texture** | neon product page | **instrumentation** |
| Accent / 2nd | amber + green phosphor | neon cyan + violet | **phosphor green + calm cyan** |
| Depth | **engraved** inset seams | blurred drop + chamfer | **hard zero-blur offset** |
| Corners | 2–4px | **cut** (clip chamfer) | **square, no chamfer** |
| Type | mono-first | grotesque-first | **Chakra Petch display + readout mono** |
| Motifs | lamps, graticule | cut corner | **reticle · scale · caution tape** |

Mecha Pilot borrows none of these: there is no weave, no vent, no engraving, no neon and no chamfer.
Its differentiators are *a drawn reticle, a calibrated scale and a caution tape* — devices that only
exist on an instrument panel.

## Ground truth

| Token | Value | Note |
|---|---|---|
| `--bg` | scan-line + hard 32px grid over olive bands `#161b10`/`#10140a` | a CRT floor, banded and gridded, not faded |
| `--bg-2` | `#10140a` | solid stand-in for exports/masthead |
| `--surface` | `#1e2416` | the instrument plate (lightest ground) |
| `--surface-2` | `#141910` | recessed readout well, inputs, tile base |
| `--text` | `#e7f0dc` | 13.6:1 on `--surface` |
| `--text-muted` | `#a7b59b` | 7.4:1 on `--surface` |
| `--text-dim` | `#9baa8e` | 6.5:1 on `--surface` — the binding ground |
| `--text-invert` | `#10140a` | panel ink on the green lamp, 14.3:1 |
| `--accent` | `#4dff9e` | PHOSPHOR green — the readout and the only action colour (hue 147°) |
| `--accent-hover` | `#7dffb8` | the lamp one notch brighter |
| `--accent-2` | `#43d9e6` | DATA cyan — media, charts, telemetry |
| `--accent-soft` | `rgba(77,255,158,.16)` | derived: a 16% tint of `--accent` |
| `--accent-ink` | `#8fffc4` | the phosphor **as text** — 13.1:1 on `--surface` |
| `--ok` / `--warn` / `--danger` / `--info` | `#8bf24d` / `#ffb03a` / `#ff5147` / `#43d9e6` | the ladder: **nominal / caution / master caution / data** |
| `--border` / `--border-strong` | `#2c3524` / `#49543c` | bezel hairline / instrument rim |
| `--focus-ring` | `#8fffc4` | phosphor readout ring |
| `--radius-sm/md/lg/pill` | `0px` | an instrument bezel is square |
| `--cut` | `0px` | no chamfer — `carbon` owns that |
| `--shadow-1` / `--shadow-2` | `4px 4px 0` / `6px 6px 0` + 1px inset bezel | zero-blur offsets only |
| `--glow` | `0 0 0 1px / 3px / 5px` green rings | a **stepped** phosphor bloom, not a blur |
| `--blur` | `none` | a cockpit panel is not frosted glass |

## Derived, and why

- `--accent-soft: rgba(77,255,158,.16)` — a 16% tint of `--accent`, expressed as `rgba()` rather than
  re-typed as a hex, so it can never drift from the phosphor green.
- `--text-invert` **is** the ground (`#10140a`): the panel ink printed on the green lamp. `#4dff9e`
  is a fill, so white on it would be ~1.6:1; the panel ink clears 14.3:1.
- `--accent-ink: #8fffc4` — the fill green is legible as a *fill* but is the wrong tone for a small
  label; the ink is the same family lifted until it reads as text (13.1:1, and 8.6:1 on its own tint).
- **`--accent` vs `--ok` — the one real risk of a green kit, resolved by hue.** The action colour and
  the nominal lamp are both green, so they must be a *different* green or an action plate reads as a
  status lamp. `--accent` is a cool phosphor **mint** at hue **147°**; `--ok` is a yellow-leaning
  **"GO"** lamp at hue **90°** — a **57° hue gap**, backed by a lightness step. A nominal chip can
  never be mistaken for the action plate.
- `--warn: #ffb03a` is the classic annunciator **caution** amber (hue 36°) — the exact tone the kit's
  *action* used to own, now demoted to the caution rung. It is far enough (54°) from the `--ok` "GO"
  lamp to read as a separate lamp.
- `--danger: #ff5147` is **master caution** (hue 3°): it arrives as a legend and a lamp, never as a
  control.
- `--info` reuses `--accent-2` (data cyan): one channel, one meaning, both directions.
- `--text-dim: #9baa8e` is set by the *lightest* ground, `--surface #1e2416`, at 6.5:1 — solving it
  against an average ground is how dim captions end up failing on the one stop that matters.

## The three signature devices

Three motifs, three **different** jobs. Each is a background value, so the tiles paint rather than
merely apply. The kit stays inside the brief's two-to-three motif budget: no fourth tile, because a
military HUD's extra vocabulary (a stencil data strip, a hard grid) is carried by `--media-bg` and
`--bg` rather than by a fourth chip that would dilute these three.

- `--mecha-pilot-reticle` — **the symbol.** DRAWN inline SVG (base64): concentric rings with a dashed
  radial tick ring (a 6px stroke on a `1.5 6` dasharray), a gapped crosshair, four corner brackets, a
  top index triangle and a two-sided **range ladder** of descending hard ticks (the gunsight cue),
  over a scope face of hard concentric bands. A gradient cannot draw a ring with radial ticks; only
  vector can.
- `--mecha-pilot-scale` — **the measurement.** DRAWN inline SVG: a heading/range tape with hard minor
  ticks every 6px, taller major ticks every 30px, stencil numerals (`00 03 06 09 12`), end brackets and
  a bright index needle. A repeating gradient makes an even comb with no majors — that is a pattern,
  not a scale.
- `--mecha-pilot-hazard` — **the warning.** Pure repeating gradient: hard 45° **amber/olive** stripes
  under a 2px amber rule at both edges. Amber is the caution rung of the ladder, so this tile is the
  one place amber appears — and it is the highest-variance tile in the kit.

The CRT scan-line field and the hard instrument grid are deliberately **not** a fourth tile: they live
on the page floor (`--bg`) and on the media panel (`--media-bg`, which reads as a lit screen — scan
lines, a data grid, a sweep band and an opaque bar-code data strip along its foot), which is where a
screen belongs.

**Non-flatness, measured.** Each token was rendered as `background:` on a 168×72 box over
`--surface-2` in headless Chromium, screenshotted, and its per-tile pixel standard deviation taken
with PIL (luma, 0.2126/0.7152/0.0722). A flat plate scores ~0.

| Tile | std-dev (luma) | luma range | job |
|---|---|---|---|
| `--mecha-pilot-reticle` | **26.25** | 14–191 | the symbol |
| `--mecha-pilot-scale` | **34.23** | 15–235 | the measurement |
| `--mecha-pilot-hazard` | **86.34** | 13–186 | the warning |

No tile renders flat: the two drawn instruments carry their variance structurally, and the caution
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
3. **Gradients** — `--bg` is banded with px stops that share a position, plus a 1px CRT scan line and
   a **hard 32px instrument grid** (both black at low alpha, so they only darken); `--wash` is off
   (so the lab's default smooth radial bloom never appears); `--media-bg` is hard sweep bands over a
   scan-line field, a data grid and a bar-code strip; `--fill-bg` is a hard-stopped segmented lamp
   bar. There is no interpolated ramp anywhere.
4. **Scaled artwork** — every motif is vector line art drawn at the size it displays; nothing is
   upscaled, so nothing can blur. `--pixel-render: pixelated` is set so any raster a consumer adds
   stays hard-edged.
5. **Blur** — `--blur: none`; the lab's `backdrop-filter` resolves to `none`, and no kit rule adds one.

## Contrast (measured, not eyeballed)

Computed by script from the declared tokens; WCAG relative-luminance, graded against the ground each
ink actually sits on. The binding ground for a dark kit is the **brightest** one, here `--surface`
(`#1e2416`). `--accent-soft` composites are of the tint **over** that ground.

| Pair | on `--bg` top | on `--bg` low | on `--surface` | on `--surface-2` |
|---|---|---|---|---|
| `--text` | 14.93 | 15.89 | 13.57 | 15.21 |
| `--text-muted` | 8.12 | 8.63 | 7.37 | 8.27 |
| `--text-dim` | 7.12 | 7.58 | **6.47** | 7.26 |
| `--accent-ink` | 14.41 | 15.33 | 13.09 | 14.68 |
| `--accent-ink` on `--accent-soft` | 9.60 | 10.33 | **8.55** | 9.75 |
| `--ok` | 12.44 | 13.23 | 11.30 | 12.67 |
| `--warn` | 9.62 | 10.23 | 8.74 | 9.80 |
| `--danger` | 5.44 | 5.79 | **4.94** | 5.54 |
| `--info` | 10.27 | 10.92 | 9.33 | 10.46 |

Other required pairs: `--text-invert` on `--accent` **14.30:1** (≥4.5); `--focus-ring` on `--surface`
**13.09:1** (≥3); `--text-invert` on the fill's darker segment (`#3fbf6a`) **7.81:1** (the avatar
label sits on that fill).

**Worst pair: `--danger` `#ff5147` on `--surface` `#1e2416` = 4.94:1** — a master-caution legend
sitting inside a card. It clears the 4.5 bar with room; the tightest *text* tier is `--text-dim` at
6.47:1, well clear of 4.55.

## Trade-offs

- **Square, opaque, dense.** The kit has no radius, no translucency and no air. That is the register,
  and it makes it a poor fit for calm or editorial work — that is `quiet` or `zen-garden`.
- **A green kit has to solve green-vs-green.** The action colour and the nominal lamp are both green,
  separated by hue (147° vs 90°). It works, and it is the price of putting the status ladder and the
  action in the same colour family. If a brand owns a specific green, this kit will collide with it.
- **Amber survives as the caution, not as action.** The one amber object left is the caution tape and
  the `--warn` lamp. A project that wants *no* amber should use a different kit.
- **The glow is stepped, not blurred.** It reads as a lit lamp, but a very large control with the
  three-ring bloom can look graphic; keep it to one glowing element per view.
- **The reticle and scale are line art, not a layout.** A kit is judged at 200×120 and the tiles carry
  the identity; the kit does not reproduce a specific cockpit screen.
- `--pixel-render: pixelated` is declared for consumers who drop a raster in; the kit's own artwork is
  vector and unaffected.

## When to use

Military and flight HUD surfaces: sim/game UI, telemetry and mission consoles, weapon and sensor
dashboards, device and network dashboards, anything that should read as a green instrument panel with
a nominal/caution/critical ladder rather than a marketing page. Avoid it for long-form reading, calm
editorial, or light contexts.

## Files

`DESIGN.md` (normative values) · `tokens.css` (the contract) · `kit.json` (gallery metadata) ·
`index.html`, `tokens.json`, `tailwind.theme.json`, `theme.css` (generated by
`python tools/build.py --only mecha-pilot`).
