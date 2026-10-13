# Photonic

**Transparent film, lit at the rim.** A hologram is an optical object before it is a style: light
leaves an edge, passes through a film, and what you see is the film *combined with* whatever is
behind it. So the panes here are 62% dark film you can see through, the rim is the emitter, the hue
bleeds inward and dies at the centre, and the ground is a drawn honeycomb light-field at a 14px
pitch. One spectrum, in the material.

- Kit: `photonic` · order `185` · mode `dark`
- Fonts: Genos · Rubik · Azeret Mono
- Tags: `dark` `sci-fi` `holographic` `translucent` `luminous` `hud`
- Source: **derived** from the user's Figma reference, fileKey `4tEWhmZzpqWsjjwJrqS8lg`,
  node `4:2` (`"Glowy stuff"`) — the same node the `holographic` kit was taken from. IP: the kit is
  named by genre; no logo or trade dress is reproduced. Hues are the reference's own four tiles.

## Stance

`holographic` (same node) kept the reference's **geometry** and threw its **light** away: foil,
hard-banded diffraction, zero-blur offsets, `--blur: none`. This kit is the other half of the same
file — the light, kept and made usable. The value is in what the reference actually *rendered*:

| measured on the reference | value | where it lands here |
|---|---|---|
| the tile's fill | `#979a9a` at 30% in **multiply** over the canvas (ground × 0.88) | `--surface` — a dark film that darkens whatever is behind it, hue preserved |
| the rim | 1–3px saturated hue, constant around the perimeter (hue varies < 3° all the way round) | `--border` at 42%, `--border-w: 1px` |
| the inward bleed | `inset 2px 4px 10px 4px` at 25–50% | `--shadow-1` first layer |
| the outward bloom | `0 0 8px 4px` at 50% | `--shadow-1` second layer |
| the surface behind it | a honeycomb weave, **14 CSS px** lattice, ~1px edges sitting 10–12 levels below the cell fill | `--photonic-weave-img`: a drawn base64 SVG tiled at 42 × 24.25px, `--bg` + `--media-bg` |
| the disc | a 12-stop conic spectrum, darker at the centre, vivid at the rim | `--photonic-spectrum` (11 stops, sampled clockwise off node `10:2`) |

The screen is built as a display is: a flare along its top edge, 32px **display rows**, the emitter
lattice, a backlight blooming down from the top, a vignette at the rim and a 4% raster grain. The
vignette sits *above* the lattice and the backlight above both, so the weave dims toward the rim and
washes out where the light is strongest — a uniformly-lit lattice is the one thing that makes a
"screen" read as wallpaper. The rows are 32px on purpose: a 3px scanline grille beats against the
14px lattice and moirés on scaled displays.

The lattice is the reference's own material (a 14px woven honeycomb, measured off its exports)
doubling as the emitter matrix. It is deliberately not an LCD/shadow-mask grid: this is a projection
surface inside a fiction, not a photograph of hardware.

Multiply is not reachable from a token, so the film is expressed the way it *behaves* on a dark
ground — a black-alpha pane that darkens the ground by 62% and keeps its hue — which is the same
arithmetic over the grounds this kit is valid on.

**One weave, deliberately inverted.** On the reference the weave is dark dividers on a mid-gray
canvas. The same weave on a near-black ground would be invisible, so here it is drawn as *lit* edges
(`#7ee7ff` at 11%, 0.9px). The structure is the reference's; the polarity is what a dark ground
requires.

## The backdrop contract

**This is the one kit in the library whose surfaces are derived rather than declared, so the ground
is part of the theme.** `--surface` is 62% film: the pane is `ground × 0.38 + film`, never a fixed
colour. Measured, with the film composited channel-by-channel in sRGB:

| ground behind the pane | pane composites to | `--text` | `--text-muted` |
|---|---|---|---|
| the kit's own lightest pixel `#183b50` (screen backlight + three washes) | `#132a38` | 13.2:1 | 7.3:1 |
| the kit's darkest pixel `#030408` | `#0a1218` | 16.8:1 | 9.3:1 |
| mid-gray (the reference's own canvas `#414141`) | `#252c31` | 12.6:1 | 7.0:1 |
| a light photo-ish gray `#c9d2da` | `#606b73` | 4.8:1 | **2.7:1** |
| a white page `#f2f5f8` | `#727a80` | **3.9:1** | **2.1:1** |

Solving for the crossing point: `--text` still clears 7:1 over a plain ground as light as `#999999`,
`--text-muted` 4.5:1 up to `#848484`, and `--text-dim` 4.55:1 up to `#535353`. A light *ground* is not
the failure — a light ground *behind a pane* is, because the film turns it milky while the ink stays put. Three consequences, all intentional:

1. **Never replace `--bg`.** It ships with the kit because it is the floor the film was graded
   against. Propping these panes over a page you did not control is the failure this table predicts.
2. **`--blur` is not decoration.** `blur(10px) saturate(112%)` is what stops high-frequency content
   behind a pane from reading straight through its text. Set it to `none` and the film is still
   transparent — it just stops being legible.
3. **Two panes never stack.** 54% over 54% is 79%, at which point the second layer is a painted
   panel with a hologram's rim drawn on it.

If a project genuinely needs a light ground, that is a different kit (see `glass`), not an override.

## Key choices

- **Cyan is the action, and it is the only filled thing.** `--accent` is the reference's system
  cyan; primary buttons are opaque plates. Every other control is a lit pane. That is also how the
  action stays separable from `--ok` (the reference's mint): the difference is material, not hue —
  a solid plate versus an outline chip — so a 40° hue gap is not being asked to carry the whole job.
- **Four reference hues, two accents.** The reference's tiles are four hue families. Here cyan is
  the action, violet the counterpoint, and mint/coral become the status ladder. Status colours don't
  count toward the two-accent budget, so the palette is honest.
- **`--accent-ink` exists because the fill fails as text.** `#15b9ff` is 8.5:1 on a pane but reads as
  a fill; small labels use `#8fe3ff` (13.1:1).
- **Radii follow the reference's own numbers** — r8 on its flat panel, ~18% on the 180px tile — so
  chips are 8px and panes are 26px. A hologram has no mitered corners.
- **Fonts deliberately differ from the sibling kit.** The reference's label face is Gruppo, which
  `holographic` already carries from this node; Genos/Rubik/Azeret Mono keep the two kits
  distinguishable in the gallery's font column as well as on the page.

## Trade-offs

- **Derived surfaces cost predictability.** Against the sibling kits, a fixed `--surface` colour is
  easier to reason about. Here the pane changes when the ground does — which is the point, and also
  the thing to check first when a text colour looks wrong on a new page.
- **The weave is drawn, not generated.** It is 3.6KB of base64 in `tokens.css` (declared once as
  `--photonic-weave-img` and referenced by `--bg`, `--media-bg` and the signature tile, so it is not
  duplicated). A gradient cannot make a hexagon: this is the case `docs/KIT-SPEC.md` covers under
  drawn artwork, and it carries a base layer so the tile is never an empty chip.
- **`--media-op: 1`.** The media panel is a lit region of the screen, not a bright ramp; the default
  0.85 would grey it out.
- **The rim is 1px and the bloom is small.** The edge is the emitter, so it does not need a wide halo
  to be seen — the wide halo was tried and it flattened every control into the same neon blur.
- **The `--photonic-screen` signature tile is a dark chip, on purpose.** A display is dark; its
  presence at 168×72 comes from the lattice, the rows and the flare along its top edge, not from a
  bright fill. Its two siblings (`--photonic-bloom`, `--photonic-spectrum`) carry the colour.
- **No `kit.css`.** The construction the reference uses (multiply film) was reachable by expressing
  its behaviour over a dark ground, so the kit stays inside the token contract.

## When to use

Projected and in-world interfaces: sci-fi, space and hardware product pages, HUD and telemetry
overlays, ambient status displays, AI/vision marketing — anywhere the interface should look lit from
its own edges rather than printed, **on a dark ground you control**.

Not: dense data dashboards (`signal`), a military instrument ladder (`mecha-pilot`), or a page whose
background is the client's own light content (`glass`, `dark-glass`).

## Linter warnings kept deliberately

`python tools/build.py` reports, and this kit keeps:

- `contrast-ratio: #8fe3ff on #15b9ff29 = 1.55:1` (three times: `badge-accent`, `button-secondary-hover`,
  `nav-item-active`). The linter grades the accent tint's **declared** rgba instead of compositing it.
  Composited over the pane, `--accent-ink` measures **7.6:1** here, and `tools/verify-lab.cjs` — which
  composites the real DOM stack — passes the kit.
- `orphaned-tokens`: `neutral`, `border-strong`, `bg-stop-1..3`, `weave` are defined but not referenced
  by a component. They document the ground ramp and the drawn lattice's stroke colour; `--border-strong`
  is the input-focus rim and `{colors.neutral}` is the page ground the backdrop contract is graded against.

## Files

Authored: `DESIGN.md`, `tokens.css`, `kit.json`, `README.md`. Generated by `python tools/build.py`:
`index.html` (component lab), `tokens.json`, `theme.css`, `tailwind.theme.json`. Do not hand-edit the
generated set.
