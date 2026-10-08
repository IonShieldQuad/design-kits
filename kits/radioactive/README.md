# Radioactive

**A containment site under CCTV.** Cold poured-concrete ground, clinical white wall plates, hazard
tape, and one toxic-green readout. Dangerous and institutional — a regulated facility, not a poster.

- Kit: `radioactive` · order `165` · mode `light`
- Fonts: Chakra Petch · Archivo · IBM Plex Mono
- Tags: `light` `industrial` `hazard` `technical` `clinical` `toxic`
- Source: original

## The mode decision — light, not dark

The brief allowed either **dark** (near-black with a glowing green) or **light-on-concrete** (grey with
black hazard stripes and a green readout). This is the light option, for three reasons:

1. **Hazard tape requires a mid ground.** The black band of a yellow/black 45° stripe disappears against
   near-black. The single most iconic device in the brief only works on concrete.
2. **"Institutional" is a property of concrete, not of a night sky.** A near-black field with a glowing
   green reads as a science-fiction title card — exactly the sci-fi poster the brief says to avoid. A
   poured-concrete hall with white instrument plates reads as a *regulated facility*.
3. **It is not a second rate for the library's many dark kits.** The glow the genre deserves is kept,
   but scoped (below), so the kit still has its one energised element.

The kit is still a **three-tier** surface stack (concrete floor → white plate → grey recessed well), which
is a light kit that exercises the `--text-on-surface*` and `--text-on-surface-2*` tokens rather than
inheriting one page-wide ink.

## The glow is a design decision

`--glow` is the kit's only luminescent device: a **tight** acid-green ring (1px ring, 9px core, 20px tail)
that the lab applies to the primary button and to keyboard focus. It marks **the one live element on a
screen** — the actionable control, the focused field, the active tab. A containment site is full of things
that are literally glowing, so the kit spends its glow budget on the element that is *energised* and
nowhere else. A soft bloom spread over the page would have made it a poster; a tight lamp keeps it a
facility. `--blur` is `none` throughout — no frosted glass sits on a poured floor.

## Key choices

- **Acid green is a FILL, never text.** `#86c81a` carries near-black ink at 9.18:1 (the hazard-signage
  convention — black on yellow-green) but is only 1.6:1 as a label on concrete, so `--accent-ink`
  (`#1d4a06`) exists for eyebrows, links, active tabs, badge labels and secondary buttons.
- **Amber never carries type.** `#e8860c` is the second accent and the hot warning tone, and it is a
  **fill only** — media panels, charts, hazard tape. It is not text on any ground (2.4:1 at best).
- **The concrete is a cold green-grey, not neutral and not beige** (`#c6cac3`). Neutral reads as office,
  warm as domestic; a facility is cold.
- **`--text-dim` is graded against the darkest aggregate pixel, not the average ground.** The floor is a
  drawn speckle, so its darkest grains (`~#bcc0b9`) are the binding ground for every dark ink — an
  average-ground solve would have cleared 5.4:1 and still failed 4.55:1 on the grains.
- **The native checkbox and radio are squared** with `--check-appearance: none` plus the `--check-*`
  tokens; a native control ignores `border-radius`, so a square kit that skips them renders the one shape
  it forbids.
- **Fields are milled into the concrete** (`--input-inset`), so inputs read as recessed rather than laid
  on the surface.
- **No chamfer** (`--cut: 0px`): `clip-path` would eat the `--glow` this kit needs.
- **The media panel is a contamination readout, not an accent ramp.** `--media-bg` is a drawn dark
  phosphor-green CCTV panel (scanlines, a waveform trace, a level readout, a camera reticle) at
  `--media-op: 1`, so a card's media strip reads as a monitor in a dark cell.

## Contrast — measured, not eyeballed

Graded with the WCAG relative-luminance formula against every ground the ink actually sits on: the
concrete floor's **darkest aggregate pixel** (`#bcc0b9`, the binding ground for dark ink on a light kit),
the floor average (`#c6cac3`), the solid `--bg-2` (`#c1c5be`), the clinical white plate (`#f2f4ef`) and
the recessed slab `--surface-2` (`#bfc3bc`). Translucent grounds are **composited** before grading.

| Ink | `--bg` grains `#bcc0b9` | floor `#c6cac3` | `--bg-2` | white plate | `--surface-2` | needs |
|---|---|---|---|---|---|---|
| `--text` `#12150f` | 9.98 | 11.09 | 10.53 | 16.64 | 10.31 | ≥7 |
| `--text-muted` `#3a4136` | 5.72 | 6.35 | 6.03 | 9.53 | 5.91 | ≥4.5 |
| `--text-dim` `#424a3f` | **4.98** | 5.54 | 5.26 | 8.31 | 5.15 | ≥4.55 |
| `--accent-ink` `#1d4a06` | 5.59 | 6.21 | 5.90 | 9.32 | 5.77 | ≥4.5 |
| `--ok` `#0d5230` | 5.02 | 5.58 | 5.29 | 8.37 | 5.18 | ≥4.5 |
| `--warn` `#6a3f04` | 4.89 | 5.43 | 5.16 | 8.15 | 5.05 | ≥4.5 |
| `--danger` `#8a160d` | 5.17 | 5.74 | 5.45 | 8.61 | 5.34 | ≥4.5 |
| `--info` `#17427e` | 5.37 | 5.97 | 5.67 | 8.96 | 5.55 | ≥4.5 |

- **`--text-invert` `#10130d` on `--accent` `#86c81a`: 9.18:1** (and 7.73:1 on the hover `#78b814`).
- **`--accent-ink` on its own 18% `--accent-soft` tint composited over the binding ground: 5.41:1** — the
  badge case, graded as a composite, not against the tint's declared value.
- **`--focus-ring` `#2c6a0e` on the binding ground: 3.58:1** (needs ≥3).

**Worst pair: `--text-dim` `#424a3f` on the darkest concrete aggregate `#bcc0b9` = 4.98:1** (needs
4.55). `--text-dim` is the token that fails most often; here it is solved against the darkest pixel of a
noisy texture rather than against an average colour, and the kit's own `verify-lab.cjs` run then samples
the real rendered pixels to confirm it.

## The three signature devices

Each does a **different** job and carries its own base layer, so no tile shows only the kit's flat
surface. Non-flatness is measured as the pixel standard deviation of the token painted as `background:`
on a 168×72 tile (`--surface-2` base), at device scale 2:

| Token | Job | What it is | σ (0-255) |
|---|---|---|---|
| `--radioactive-trefoil` | symbol | the IAEA trefoil, **drawn** inline SVG — three congruent annular sectors at 120° around a core, on a yellow placard disc | **58.03** |
| `--radioactive-hazard` | warning | drawn 45° yellow/black hazard tape (SVG pattern, crisp hard bands) | **71.36** |
| `--radioactive-spill` | atmosphere | a toxic puddle, **drawn** — blob + hot core + spatter + rising vapour over its own dark hall base | **43.46** |

Measured by the brief's method: each token painted as `background:` on a 168×72 box over the kit's
`--surface-2` (`#bfc3bc`) tile base, screenshotted in headless Chromium at device scale 2, and the
per-tile pixel standard deviation taken with PIL `ImageStat`. A flat chip reads near 0; all three clear
36, so none of them renders as an empty plate. (The hazard tile measured **36.04** on the first build —
its CSS stripe token had been rewritten into a smooth yellow→black ramp by the gallery's gradient
normaliser; drawing it as an SVG pattern fixed it to 71.36.)

All three are drawn as inline SVG. The trefoil and the spill need it because neither is expressible with
gradients — a wedge is exact geometry and a puddle is an organic blob with a highlight, not a tint. The
hatching is drawn because a CSS px-stop `repeating-linear-gradient` is rescaled into a smooth ramp by the
gallery's preview normaliser, which destroys the hard bands (verified: the first build rendered the tile
as a muddy yellow→black gradient). Base64 data URIs are used throughout (never hand-percent-encoded) so a
`#` cannot double-encode and fail silently.

## Trade-offs

- **The brightest thing on the page is a fill, not a label.** Acid green is the identity, but it is
  unusable as small text on concrete, so the "green text" a viewer expects is a much darker green
  (`--accent-ink #1d4a06`). That is honest to hazard signage and legible; it is deliberately not neon.
- **A noisy ground forces a near-black `--text-dim`.** Solving against the darkest aggregate grain means
  `--text-dim` sits close to `--text-muted`; the caption tier is quieter than in a flat-ground kit, but it
  passes everywhere. Reported rather than hidden.
- **`--border-w` is 1px.** The boldness lives in the tape and the trefoil, so the plates keep a fine cast
  joint; a 2px rule would fight the hazard device for attention.
- **`--radius-pill` is 2px, not `999px`.** An industrial kit's badge, avatar and toggle are stamped
  plates, not lozenges; the token keeps its name while the shape stays square. `--check-*` squares the
  native controls for the same reason.
- **The amber cannot be a text colour on any ground** (2.4:1 at best), so `--warn` as text is a dark amber
  (`#6a3f04`) and the *hot* amber survives only in fills, charts and the tape.

## When to use

Controlled, institutional danger: industrial and monitoring dashboards, safety and ops tooling, incident
and telemetry UIs, science and medical instrument panels, anything that wants to feel *contained* rather
than cosy. Avoid it for warm, social, editorial or nightlife surfaces — that is `city-pop`,
`summer-sunset`, `retro-anime` or `sakura`. For a dark control-room register instead of a daylight
one, use `inside-the-machine` or `cyberpunk`.
