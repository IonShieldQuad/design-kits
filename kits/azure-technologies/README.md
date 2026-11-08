# Azure Technologies

**The reference place of the Li//OS desk family.** Place 01 of fifteen; six of them are ported
into this library and this is the one the other five are variations on. A near-black blue ground
(`#05080D`, floor `#030609`) with two soft fields of `#0B2233`, a 120px technical grid and a
36 x 20.7846 hexagon lattice at 4.95%; on it, opaque cards at `#0A0F16` carrying the same
lattice at 9%, a 9% sheen band with a 1px specular lip, a 9% bottom occlusion band, a 157° face
fall, a 5% cyan tint and a 1px cyan identity edge. Cyan `#4FD8FF` is hairlines and one filled
control; violet `#7E8CFF` is the second hue. 16px chamfer, 0px radii, `--blur: none`.

- Kit: `azure-technologies` · order `205` · mode `dark`
- Fonts: Chakra Petch · JetBrains Mono
- Tags: `dark` `cold` `geometric` `instrument` `hud`
- Source: **derived** from the user's `bespoke-desktop` Li//OS prototype
  (`prototypes/v9-lilythium`, `body[data-place="01"]`) — `--acc`, `--acc2`, `--accHi`, `--face`,
  `--panel`, `--ground`, `--sceneA`, `--sceneB`, `--glow`, `--accLine`, `--cp`, `--rad`,
  `--txA .055`, copied from `docs/lilythium/place-01.css`. The motif is pasted verbatim from
  `docs/lilythium/textures.css`; nothing was redrawn.

## Stance

An instrument panel, not a website. The register is cold and geometric: a plate that carries
light on its top edge, a lattice drawn into its face, one cyan hairline around it and one cyan
line along its bottom. Everything the kit does is measurable — 1px frames, a 16px chamfer, a 5.5%
motif, a 157° fall, a 46%-to-0% occlusion band — and nothing is soft: `--radius-*: 0px`,
`--ease: linear`, `--blur: none`.

**Why this one is the baseline.** The family's grammar is: one hairline frame, an opaque face
with a sheen band, a bottom occlusion band, a 157° fall, a 5% accent tint and one drawn motif at
5–9%; one accent hue per place; one signature motif. A sibling changes *one* of those — its hue,
its corner treatment, its motif — and keeps the construction. This kit is the version with the
fewest exceptions to explain: one accent (`#4FD8FF`), one motif (a geometric lattice, the only
one in the family that is a tessellation rather than a drawing or a scanline), one shape
(chamfer 16, the family's most common), zero rounding, and a status ladder that is four distinct
hues with no inversion to argue about. When a sibling looks wrong, diff it against this file.

## Lineage

| # | place | slug | order | accent | face | ground | shape | motif |
|---|---|---|---|---|---|---|---|---|
| **01** | **Azure Technologies — this kit** | `azure-technologies` | **205** | **`#4FD8FF`** | **`#0A0F16`** | **`#05080D`** | **chamfer 16** | **hex lattice** |
| 02 | Mainframe Access | `mainframe-access` | 210 | `#54E08A` | `#04100A` | `#020704` | square | scanlines |
| 05 | Pastel District | `pastel-district` | 215 | `#FF8FC4` | `#23141D` | `#160C13` | round 6 | bokeh |
| 06 | Crimson Labyrinth | `crimson-labyrinth` | 220 | `#FF4D5E` | `#140A0C` | `#090305` | octagon 12 | engraved rose |
| 07 | Sunset Boulevard | `sunset-boulevard` | 225 | `#B06CFF` | `#150C28` | `#0A0512` | chamfer 18 | perspective grid |
| 08 | Viridian Fields | `viridian-fields` | 230 | `#147A57` | `#0C1410` | `#0A1512` | round 5 | engraved fern |

**The axis.** Two siblings share this kit's 16px chamfer (06, 07) and one shares its second hue
family (07's violet). What is *only* here: a **tessellated** motif — a 36 x 20.7846 lattice whose
edges are at 60° and which tiles seamlessly at 144 x 83.14 on the ground — and an accent light
enough to need a dark ink (`--text-invert: #04121A`, 11.4:1 on `#4FD8FF`). Every other place's
accent is a mid-tone or darker hue read as text or as a border; here cyan is a *fill*, which is
why the kit carries `--accent-ink` (`#8BE8FF`) for labels and `--text-invert` for the fill — two
different jobs that one hue cannot do at once. 06 and 07 carry a drawn motif (an engraving, a
perspective grid), 02 carries scanlines, 05 bokeh, 08 an engraving; this is the only one where
the motif is architecture.

**The type is shared on purpose.** All six places ship Chakra Petch + JetBrains Mono, the desk's
own two faces. These are places inside one operating system and the type *is* the OS; giving a
place its own font would make the set a set of unrelated skins. If a future session wants to
"fix" the repetition, that is the line to read first.

## The material

`--surface` is not a colour, it is `--azure-technologies-pane` — the desk's own `.card-in`, ported
to one value. Layer order, top first, and the order *is* the light model:

```
sheen (1px specular lip)  >  occlusion  >  texture  >  identity edge  >  tint  >  face fall  >  face
```

| layer | value | why it is there and why it is *here* |
|---|---|---|
| sheen | `rgba(255,255,255,.30) 0 1px`, `.17 1px`, `.048 34%`, `0 100%`, box `100% 9%` | light arriving on the plate. Nothing on the plate tints it, so it is the top layer. Measured: `rgb(114,121,127)` at the lip, `rgb(81,90,96)` 2px down, `rgb(41,51,59)` at the band's edge. |
| occlusion | `rgba(0,0,0,.46) 0`, `.138 38%`, `0 100%`, box `100% 9%` at the bottom | the bottom of a plate is out of the light. It sits **above** the texture: an occlusion under the lattice leaves a full-strength lattice in the dark band, which reads as a rendering fault. |
| texture | `var(--azure-technologies-tex)` — 36 x 20.7846, `stroke-opacity .09` | the motif. Above the tint, because a 9% lattice under a 5% cyan wash is invisible. |
| identity edge | `rgba(79,216,255,.55)`, 1px, from 7% to 96% of the width, at the bottom | the one place a plate is brighter than its frame. Measured after the occlusion: `rgb(59,123,142)`. |
| tint | `rgba(79,216,255,.05)` | the place's colour on the face — 5%, the desk's own `--tintA`. |
| face fall | `157deg`: white `.12 0%` → `0 44%` → black `.24 78%` → `.52 100%` | the plate's own shading. Under the tint: the tint is colour on the face, so it takes the shading instead of replacing it. A fall under the face is not a fall. |
| face | `#0A0F16` | `--face`, opaque. The desk forbids glass, so there is nothing to see through. |

`--surface-2` is the **nested** tier — inputs, badges, alerts, code, `card-elevated` — and drops
the lattice and the identity edge: a 36 x 20.7846 lattice on a 2.5rem control is clutter, not
material. It keeps a 6% sheen, half the tint (4%) and `--panel #0A0F15`.

**`--blur: none`.** Every surface is opaque; the desk forbids `backdrop-filter`. A `blur()` on an
opaque card costs a repaint and changes nothing.

## The motif

A hexagon lattice, 6 edges at 60°, on a 24 x 20.78 unit cell. Two pitches, two jobs:

| where | pitch | stroke | measured |
|---|---|---|---|
| card material (`--azure-technologies-tex`) | **36 x 20.7846 px**, `0 0/36px 20.78px repeat` | white at **9%** (`stroke-opacity .09`) | row-average swing inside a quiet card band: `rgb(13,23,31)` → `rgb(21,31,39)` |
| page ground (`--azure-technologies-tex-ground`) | **144 x 83.14 px** (2x the card's) | white at **3.03%** (`stroke-opacity .0303`) | the same motif, larger and quieter |
| the technical grid under it | 120 x 120 px | white at 2.8% vertical, 2.4% horizontal | anchors the scene to the page |

Two scales, deliberately different jobs: the ground is large-celled and quiet, the components are
at the desk's own pitch and drawn stronger. Equal weight makes the page one busy field and every
card reads as texture inside texture. Both alphas are baked (the desk applied `--txA` as a
pseudo-element `opacity`, which a background layer cannot do) and both were verified at gallery
tile size, so do not raise them "until it shows". The ground carries **the same motif**, not a
second one — no place in this family tiles an engraving behind an engraving.

Every scene size is a percentage, never a px: the gallery renders `--bg` into a ~118px tile, and a
px-anchored radial shows it the top edge of the page instead of the scene.

## Contrast, measured

All ratios are from the rendered lab (`shots/azure-technologies-*.png`), sampling the pixel the
ink actually sits on — not the declared solid. **No ink value had to be changed to pass a check;
these are the first values, measured.**

| pair | ground | ratio | floor |
|---|---|---|---|
| `--text` `#E8F2F8` on `--bg` (lightest ground pixel) | `rgb(45,60,71)` | **10.00** | 7 |
| `--text` on the card face | `#0A0F16` | **16.92** | — |
| `--text` on the ground's bloom (`--sceneA` `#0B2233`) | `rgb(11,34,51)` | **14.32** | — |
| `--text` on a card title (below the media panel) | `rgb(28,39,46)` | **13.41** | 4.5 |
| `--text` on a card title at the top of a card | `rgb(36,48,56)` | **11.89** | 4.5 |
| `--text-muted` on a card body | `rgb(16,28,37)` | **9.98** | 4.5 |
| `--text-muted` on `--surface-2` (input, badge, alert) | `rgb(19,29,36)` | **9.87** | 4.5 |
| `--text-dim` on `--bg` | `rgb(45,60,71)` | **4.91** | 4.55 |
| `--text-dim` on a card (mean) | `rgb(30,42,52)` | **6.32** | 4.55 |
| `--text-dim` on `--surface-2` | `rgb(19,29,36)` | **7.39** | 4.55 |
| `--text-invert` `#04121A` on `--accent` (sampled fill) | `rgb(71,195,230)` | **9.23** | 4.5 |
| `--text-invert` on `--accent-hover` `#7FE4FF` (computed) | `#7FE4FF` | **13.05** | 4.5 |
| `--accent-ink` `#8BE8FF` on a `badge-accent` (composited `--accent-soft` over `--surface-2`) | `rgb(34,59,70)` | **8.46** | 4.5 |
| `--accent-ink` on `--surface-2` | `rgb(19,29,36)` | **12.27** | 4.5 |
| `--ok` `#4EE6B0` on `--surface-2` | `rgb(19,29,36)` | **10.80** | 4.5 |
| `--warn` `#FFC04D` on `--surface-2` | `rgb(19,29,36)` | **10.50** | 4.5 |
| `--danger` `#FF6377` on `--surface-2` | `rgb(19,29,36)` | **5.94** | 4.5 |
| `--info` `#A98BFF` on `--surface-2` | `rgb(19,29,36)` | **6.37** | 4.5 |
| table cell (muted) on the row wash | `rgb(28,75,91)` | **5.49** | 4.5 |

The sheen band is the one place the kit has a ceiling, and it is written into `tokens.css`: its
peak is `rgb(93,102,108)`, where `--text` measures 5.16:1 but `--text-muted` 3.38:1 and
`--text-dim` 2.53:1. It is a light source, not an ink ground — the 9% band is 18–25px on a real
card and the kit's first line of text starts at the 18px padding, below the `.17` stop, where all
three clear their floors (11.89 / 7.80 / 5.84). Anything placed *inside* the first ~10px of a
plate must be `--text` or `--accent-ink`.

## Key choices

- **Cyan is a fill, so the kit carries two cyan inks.** `#4FD8FF` is 11.5:1 on the face, but as a
  small label it reads as a button someone forgot to press; `--accent-ink` is the desk's own
  `--accHi #8BE8FF` (13.8:1) and `--text-invert #04121A` is the label on the fill (11.4:1). One
  hue, two jobs, two tokens — that is what `--accent-ink` exists for.
- **The frame is a ring.** `--clip` cuts the diagonal, so the border is painted on an edge that no
  longer exists. `tools/build.py` derives `--frame-ring` from `--cut: 16px` and paints the frame
  as the silhouette with an inset copy punched out; `--focus-inset: 2px` does the same for the
  keyboard ring, which `clip-path` also eats. Verified: `--frame-ring` resolves to
  `polygon(evenodd, 16px 0, …)` on the rendered page.
- **Zero rounding, including the native controls.** `--radius-*: 0px`, `--radius-pill: 2px`
  (not 0, so a badge fill does not clip its own glyphs), `--check-radius: 2px` *plus*
  `--check-appearance: none`, because a native checkbox ignores `border-radius` and would
  otherwise be the only circle on the page.
- **The status ladder is four distinct hues, no inversion.** `--ok #4EE6B0` is 26° of hue away from
  the cyan action and separated by material as well (an opaque accent plate against an outlined
  chip), so a cyan button never reads as "success" and mint never reads as "act". `--danger` is
  the only one with a tight margin (5.47:1) and it is used as text on `--surface-2`, never as a
  fill.
- **`--surface-2` drops the motif.** This is the family's rule and it is the right one: a lattice
  at card pitch inside a 2.5rem control is noise, and a tint without the motif is a printing
  fault, so the nested tier drops both.
- **`--media-bg` is a place plate.** The media panel is the scene's bloom and the motif at card
  pitch on the face at `--media-op: 1` — not the default accent→accent-2 ramp, which in a console
  reads as a marketing banner.
- **`--wash` is a field of the scene.** The masthead takes a `--sceneA` radial rather than the
  default `--accent-soft` bloom; the desk has no bloom beyond its own scene.

## Trade-offs

- **A clipped plate loses its shadow.** `clip-path` clips `box-shadow` along the silhouette, so
  the desk's `0 6px 16px rgba(0,0,0,.50)` (kept as `--shadow-1`, because the contract asks for it
  and non-clipped surfaces still use it) is effectively invisible on `.card`. Separation therefore
  comes from the 1px ring and the sheen lip, not from depth. That is the chamfer's cost, not a bug,
  and it is why the ring is derived rather than optional.
- **The identity edge is drawn under the occlusion band.** That is the desk's own layer order, so
  55% cyan renders at `rgb(59,123,142)` — a dim seal, not an underline. It is visible at 1x, and
  a sibling that wants a brighter seal would have to move the edge above the occlusion and give up
  the "bottom out of the light" model.
- **The sheen band is brighter than the ink floor.** Its peak (`rgb(93,102,108)`) clears 4.5:1 for
  `--text` only. The material's alphas are the desk's and are not negotiable, so the constraint is
  documented instead of softened: no muted or dim ink in the top 9%.
- **The ground is the quiet half, and it shows in the gallery.** `--azure-technologies-field`
  measures `rgb(3,6,9)` at its floor to `rgb(25,35,45)` at its bloom, median `rgb(7,18,27)` — a
  dark blue field over a slightly lighter tile base (`rgb(19,29,36)`), i.e. a *legible* chip but a
  quiet one. It is the correct read for this place (a console's ground is black; the colour is on
  the plates) and it is the half of the kit that a thumbnail cannot sell — the pane tile is the one
  that carries the identity at 168 x 72.
- **The shared type pairing costs distinctiveness in the gallery's font column.** All six places
  read `Chakra Petch · JetBrains Mono`, so the font chip cannot tell them apart. The hue, the motif
  and the corner treatment carry that job instead — deliberately, because the alternative is six
  unrelated skins.
- **Two frames on one control.** A chamfered, clipped component draws both its `border-color`
  (transparent, set by the generated frame style) and the ring; the border is kept only because
  the ring's thickness is taken from `--border-w`. Changing `--border-w` to 2px would thicken both.

## When to use

Sci-fi product and spacecraft pages, engineering and telemetry dashboards, monitoring and control
surfaces, a HUD-styled portfolio — anything that should read as an instrument panel rather than a
website, on a dark ground.

- Close call with **`sunset-boulevard`** (also chamfer 16, also a violet second hue): use this one
  when the register is cold and the motif should be architecture; use `sunset-boulevard` when the
  page needs a horizon, a perspective grid and a warmer violet-led light.
- Close call with **`mainframe-access`** (also a green-cyan instrument register): that one is
  square and scanline-based, and its ladder is monochrome; pick it for terminal/legacy-mainframe
  fiction, this one for orbital hardware.
- Not for dense data tables where the material must disappear (`signal`), not for a light page
  (`quiet`, `glass`), and not where the content is the colour (`city-pop`, `synthwave`).

## Linter warnings kept deliberately

`python tools/build.py --only azure-technologies --no-export` reports one finding, informational,
and no errors:

- `token-summary: Design system defines 16 colors, 5 typography scales, 5 rounding levels,
  5 spacing tokens, 22 components.` — the linter's summary line, not a defect. No
  `contrast-ratio` findings: every `components:` pair in `DESIGN.md` references a declared colour
  pair that clears its floor, and the composited pairs are in the table above.

Two things a reviewer should know about the checks:

1. **`scripts/contrast-audit.py` does not exist in this checkout.** The brief's second check
   (`python scripts/contrast-audit.py kits/azure-technologies`) cannot be run: there is no
   `scripts/` directory and no such file anywhere in the repository. It was replaced with an
   equivalent measured on the rendered page — every ink sampled against the pixel it sits on,
   including the composited `--accent-soft` badge ground — and `tools/verify-lab.cjs` (which
   composites the real DOM stack) is clean. If the coordinator's tree has the script, it should be
   re-run before the aggregate build.
2. **`--azure-technologies-field` is a dark signature tile by design.** At 168 x 72 it reads as a
   dark blue field, not as a bright chip; the numbers are in the trade-off above. Its two siblings
   (`--azure-technologies-pane`, `--azure-technologies-tex`) carry the colour and the lattice.

## Files

Authored: `DESIGN.md`, `tokens.css`, `kit.json`, `README.md`. Generated by
`python tools/build.py`: `index.html` (component lab), `DESIGN.html`, `tokens.json`,
`theme.css`, `tailwind.theme.json`. Do not hand-edit the generated set.
