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
| the tile's fill | `#979a9a` at 30% in **multiply** over the canvas (ground × 0.88) | the film inside `--photonic-pane` — a blue-tinted 56% pane, so the ground still shows through it |
| the rim | 1–3px saturated hue, constant around the perimeter (hue varies < 3° all the way round) | `--border` at 58%, `--border-w: 1px` |
| the inward bleed | `inset 2px 4px 10px 4px` at 25–50% | `--shadow-1` first layer, at 34% |
| the outward bloom | `0 0 8px 4px` at 50% | `--shadow-1` second layer, at 45% |
| the surface behind it | a honeycomb weave, **14 CSS px** lattice, ~1px edges sitting 10–12 levels below the cell fill | `--photonic-weave-img`: the card's own material, drawn as base64 SVG |
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
ground: a blue-tinted pane at 56%, which darkens the ground and keeps its hue — the same arithmetic
over the grounds this kit is valid on. It is blue rather than neutral because the reference's tiles
are *saturated*: a neutral film on a near-black ground renders as dead grey, and the kit's colour is
supposed to look like light through glass, not like a dark box.

**The field decays with distance from the nearest border — it is not a radial.** Four edge gradients:
deep cyan arriving from the top and bottom, deep violet from the left and right, each reaching ~40–46%
into the box and falling to nothing. Intensity is therefore highest *against a border* and the middle
is the quietest part of a card; and because it follows distance-to-border rather than
distance-to-centre, a corner (nearest two borders) is the brightest point — the reference's own
behaviour. Text lives in the 12–20% band, which is the brightest ink ground in a card, so the alphas
are set where `--text-dim` still clears its floor *there*: a bright accent cyan at 0.26 in that band
measured 3.3:1, which is why the field is built from deep hues (a saturated mid-blue at 0.32, a deep
violet at 0.20) rather than the bright ones.

**The material, and where it lives.** A card is not a fill. `--surface` is `--photonic-pane`: the
woven lattice + that field + the film — one value, because a wash on its own is a printing fault and
only becomes material once the weave is over it. `--surface-2` — the nested tier worn by inputs,
alerts, badges, progress tracks and code blocks — carries the same two layers at roughly half the
strength and at three times the cell size (42px, so a 40px control shows one cell edge and reads as
detail rather than pattern). The ground is deliberately the *opposite* of the card: a
lattice at 3× the cell size (42px) carrying a third of the contrast, so the page stays a quiet surface
and the ground never reads as texture inside a card — the card's own weave is pitched at 14px and
drawn stronger than the ground's, which is what keeps the two from fighting.

**One weave, deliberately inverted.** On the reference the weave is dark dividers on a mid-gray
canvas. The same weave on a near-black ground would be invisible, so here it is drawn as *lit* edges
(`#7ee7ff` at 11%, 0.9px). The structure is the reference's; the polarity is what a dark ground
requires.

## The backdrop contract

**This is the one kit in the library whose surfaces are derived rather than declared, so the ground
is part of the theme.** `--surface` is a 56% film: the pane is `ground × 0.44 + film`, never a fixed
colour. Measured, with the film and its in-card gradient composited channel-by-channel in sRGB:

| ground behind the pane | pane composites to | `--text` | `--text-muted` |
|---|---|---|---|
| the kit's own lightest pixel `#18394e` (screen backlight + three washes) | `#19294d` | 12.7:1 | 7.9:1 (dim 6.4:1) |
| the kit's darkest pixel `#030408` | `#131a39` | 15.1:1 | 9.3:1 (dim 7.6:1) |
| mid-gray (the reference's own canvas `#414141`) | `#242c49` | 12.2:1 | 7.6:1 (dim 6.1:1) |
| a light photo-ish gray `#c9d2da` | `#4b5575` | 6.5:1 | **4.0:1** |
| a white page `#f2f5f8` | `#575f7e` | **5.6:1** | **3.4:1** |

Solving for the crossing point: `--text` still clears 7:1 over a plain ground as light as `#c0c0c0`, `--text-muted` 4.5:1 up to `#b8b8b8`, and `--text-dim` 4.55:1 up to `#878787`. A light *ground* is not
the failure — a light ground *behind a pane* is, because the film turns it milky while the ink stays put. Three consequences, all intentional:

1. **Never replace `--bg`.** It ships with the kit because it is the floor the film was graded
   against. Propping these panes over a page you did not control is the failure this table predicts.
2. **`--blur` is not decoration.** `blur(6px) saturate(108%)` is what stops high-frequency content
   behind a pane from reading straight through its text. Set it to `none` and the film is still
   transparent — it just stops being legible.
3. **Two panes never stack.** 56% over 56% is 81%, at which point the second layer is a painted
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
- **The in-card gradient is capped at 0.34, and the glow carries the rest.** A stronger gradient inside a
  card looks richer in isolation and washes the text sitting on it, so the light was moved out of the
  fill and onto the edge (`--shadow-1`'s bloom is 60%) — which is also where the reference put it.
- **The rim is 1px, the bloom is not small.** The reference's own rim glow measures 45–50%; a thin
  rim under a wide halo reads as a soft neon wash and flattens every control into the same blur, which
  is why `--shadow-1` keeps the bloom tight (14px) and puts the *brightness* up rather than the spread.
- **The rim and the film carry different jobs.** The rim is saturated (58% cyan); the film is dark and
  blue. Making the film lighter to look more colourful greys the whole kit out instead.
- **The nested tier is not a flat rectangle.** Code blocks in particular were reading as a plain blue
  box, so `--surface-2` gained the same weave-plus-edge-wash construction as a card, just quieter and
  coarser; the least that stops a bordered rectangle from looking like a wireframe.
- **The signature row shows `--photonic-pane`, not just `--photonic-screen`.** The pane is where the
  colour is; the screen is deliberately the quiet half.
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
