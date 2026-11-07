# Mainframe Access

**Phosphor-green terminal glass on a black grid.** A plate you look *into*: 4px scanline rows at
5% white over a 5% accent tint, a 1px specular lip along the top, a 46% occlusion band along the
floor, and a 157° fall between them. Square to the pixel, one hue, and a status ladder carried by
value and material rather than by chroma. It is the only monochrome kit in the library.

- Kit: `mainframe-access` · order `210` · mode `dark`
- Fonts: Chakra Petch · JetBrains Mono
- Tags: `dark` `terminal` `monochrome` `phosphor` `technical`
- Source: **derived** from the user's `bespoke-desktop` Li//OS prototype
  (`prototypes/v9-lilythium`, place **02 "Mainframe Access"**) — palette, panel construction and
  drawn motif taken from the prototype's own tokens, not re-drawn.

## Stance

This is a machine login, not a page. The interface is a plate of terminal glass over a black grid,
lit from above (a 1px specular lip and a 4.8% sheen band), seated by its own shadow at the bottom
(a 46% occlusion band), and etched with the one texture the desk uses for this place: a horizontal
scanline at the desk's own 4px pitch. There is no second hue to lean on, so the kit has to make
value and material do the work a palette does elsewhere: accent green is a **fill**, the pale
phosphor is the **text and the ok-state**, and the amber is the warning.

## Lineage — the LIL//OS desk family

| # | place | slug | order | accent | shape | motif |
|---|---|---|---|---|---|---|
| 01 | Azure Technologies | `azure-technologies` | 205 | `#4FD8FF` | chamfer 16 | hex lattice |
| **02** | **Mainframe Access** | **`mainframe-access`** | **210** | **`#54E08A`** | **square** | **scanlines** |
| 05 | Pastel District | `pastel-district` | 215 | `#FF8FC4` | round 6 | bokeh |
| 06 | Crimson Labyrinth | `crimson-labyrinth` | 220 | `#FF4D5E` | chamfer 16 | engraved rose |
| 07 | Sunset Boulevard | `sunset-boulevard` | 225 | `#B06CFF` | chamfer 16 | perspective grid |
| 08 | Viridian Fields | `viridian-fields` | 230 | `#147A57` | round 5 | engraved fern |

All six share one grammar: a hairline frame, an opaque face carrying a sheen band, a bottom
occlusion band, a 157° face fall, a 5% accent tint and one drawn texture at 5–9%; one accent hue;
one signature motif. They also share **the type** — Chakra Petch for display and body, JetBrains
Mono for labels — deliberately, because these are six places in one OS and the type is the OS. A
later session should not "fix" that per kit.

**What separates this place from its five siblings**, on four axes at once:

| axis | this place | nearest sibling |
|---|---|---|
| corner | square: `--cut: 0`, no `--clip`, radii 0/0/0, pill 2px | four places chamfer 16; two round 5–6 |
| chroma | one hue; the accent is the only colour in the interface | 01/05/06/07/08 each carry two or three |
| texture | straight rows, 1px every 4px — a raster, not a drawing | lattice, bokeh, rose, perspective grid, fern |
| status | ladder resolved by **value and material**, not hue | the other five can move `--ok`/`--danger` to a new hue |

The nearest collision is not inside this family but outside it: `signal` and `mecha-pilot` are also
dark and technical. They are dense dashboards and an instrument ladder; this is a login screen —
one plate, one hue, nothing to scan.

## What the material is

`--surface` is `--mainframe-access-pane`, the desk's own `.card-in` ported to a token. Layer order
is top-first and **is** the light model:

```
sheen      180deg, white 30% on its first 1px, 17% on the next, 4.8% at 34%, gone by 100%
           in a 9%-tall band at the top
occlusion  0deg, black 46% at the floor, 13.8% at 38%, gone by 100% — in a 9%-tall band at the bottom
texture    4px scanline rows, white 5%, from the place's own --tx
edge       90deg accent hairline, rgba(84,224,138,.55), 7%→62%, 1px, pinned to the bottom
tint       5% of #54E08A across the plate
fall       157deg, white 12% at the top-left to black 52% at the bottom-right
face       #04100A
```

The order matters and is the family's: **a texture under the tint is invisible** (1px of white
inside a green wash at 5% is 1 level of difference), and **a fall under the face is not a fall**.
The sheen sits above everything because it is the reflection *of* the glass, not a layer *in* it.

`--surface-2` — inputs, badges, alerts, code blocks, `card-elevated` — drops the texture and the
identity edge and keeps a 6% sheen plus half the tint (`rgba(84,224,138,.025)`) on the place's own
`--panel` `#071009`. A 4px row on a 2.5rem control is a moiré, not material: at a 40px control height
the pitch repeats ten times and reads as a printing fault. A 1px accent line on a 34px badge is a
second border.

Because every surface is opaque, `--blur: none`. The desk forbids glass and `backdrop-filter`, and a
blurred opaque card is only a repaint cost.

## The motif

One motif, two scales, both numbers from the desk:

| | pitch | alpha | where |
|---|---|---|---|
| card | 1px row every **4px** (25 rows per 100px) | **5%** white | `--mainframe-access-tex`, inside `--surface` and `--media-bg` |
| ground | 1px row every **8px** | **2.75%** white | `--mainframe-access-tex-ground`, inside `--mainframe-access-field` |

Both are pasted **verbatim** from `docs/lilythium/textures.css`, where the desk's pseudo-element
`opacity` (`--txA: .05`) is already folded into the stroke alpha. The pitch is the image's own
period, so neither layer declares a `background-size`: any size would have to be an exact multiple
of 4px or it would resample the 1px row into a soft 2px row.

Measured on a rendered card at 3× device scale, the row is 1 CSS px of ~2× the surrounding
luminance, every 4 CSS px, across the full width — that is the material, not a gradient band.

## Key choices

- **The accent stays distinguishable from `--ok` by material, not by hue.** Both are the same
  phosphor family: `--ok` is `--accent-ink` `#93F2B8`, the pale member, and it is only ever a
  status **label on an outlined chip**; the action is an **opaque `#54E08A` plate** with dark ink.
  At 12–14px the difference is not a hue difference at all — it is a filled control beside a
  stroked one, which is how a terminal has always distinguished a key from an indicator. `photonic`
  makes the same argument with a solid plate against a lit pane.
- **A monochrome kit cannot afford a `--text-invert` that is white.** `#54E08A` is a light fill
  (57% relative luminance): white on it is 1.7:1. The ink is `#02120A` — 11.35:1 on the accent,
  13.55:1 on its hover step.
- **The ground is a token, not a background.** `--mainframe-access-field` carries the two `#072A19`
  scene fields, the 120px technical grid, the 8px scanline and the `#020704 → #010302` ramp, and
  `--bg` **is** that token. It has to be the whole scene, not just the ramp: every signature token
  is judged at 168×72 on the tile base, and a two-stop `#020704 → #010302` ramp renders there as an
  empty near-black chip. Wrapping the scene is what makes the token legible as the ground.
- **Amber is the desk's, not a new colour.** `--accent-2` is `#FFC04D`, this place's own amber
  sibling; it is the same value as `--warn` on purpose. In a one-hue kit a second decorative hue
  would be the first thing that stopped it being monochrome.
- **No `--btn-shadow`, no `--bar-shadow`.** Every control is a hairline frame on a plate; the only
  thing that emits is `.btn-primary` via `--glow` (`0 0 14px` at the accent's 34%). One emitter per
  page is what keeps a terminal reading as a terminal.
- **Inputs are recessed, not raised.** `--input-inset` is `inset 0 1px 0` black 55% plus a 3.5%
  white inner keyline — a well, in black and white only.

## Trade-offs

- **The status ladder is mostly value, and that costs a hue.** A reader who has only ever seen a
  green-accent kit will expect `--ok` to be a *different* green. Here it is a paler one, and the
  distinction is carried by chip-vs-plate. If the interface needs a status that reads instantly at
  a glance without a shape cue, this is the wrong kit.
- **`--danger` `#FF6464` measures 3.30:1 on the lightest band a glyph can occupy.** That band is
  the top 9% sheen strip (composite `#394940`), where no danger text is placed: the invalid-field
  hint sits on the page ground (7.01:1) and the danger badge on the card's dark floor (6.43:1).
  Clearing the sheen band would take a red so pale it becomes a warning. It is 5.60:1 on
  `--surface-2` and 6.10:1 on the mid plate, which is where it actually appears. The value was
  lifted from the desk-adjacent `#FF5C5C` because that one sat at 4.44:1 on the accent-soft-over-panel
  composite, four hundredths under the floor there.
- **The 1px specular lip is not text-safe.** It composites to `#6E7973` (18.2% luminance) and takes
  `--text` down to 4.06:1. It is 1px of highlight under a 9% band; card padding puts the first
  glyph below it. The alternative is deleting the sheen, which is the family's identity.
- **The shared type pairing buys a family and costs distinctiveness.** Six kits with the same two
  faces means the gallery's font column cannot tell them apart; the place has to be carried by
  shape and material. That is the brief's decision, and it is right for a family that is one OS.
- **The pixel fall is built from gradients, so it is invisible to a linter's declared-value check.**
  `scripts/contrast-audit.py` grades a declared `--accent-soft` as if it were opaque and reports
  1.26:1; the composited value (18% of `#54E08A` over `#0B1C13` = `#183F28`) is 8.74:1. The real
  check is `tools/verify-lab.cjs`, which samples pixels — it passes.
- **Native checkboxes and radios are squared by drawing the box**, not by a radius: `--check-appearance:
  none` plus `--check-bg: #071009`, a `1px solid rgba(84,224,138,.6)` border and `--check-checked:
  var(--accent)`. A native radio paints a circle inside its 1rem box whatever `--check-radius` says,
  and a circle is the one curve this kit forbids. Off is an outlined indicator; on is a filled key —
  the same material argument the action/status split uses. `--check-radius: 0px` is still declared, so
  the box's own corner is the kit's.
- **No `kit.css`, no `--clip`, no `--frame-ring`.** Everything the plate needs is a layered
  background value; there is nothing to construct and no diagonal to reinstate.

## When to use

Developer tools, security and ops consoles, CI and deploy surfaces, terminal-adjacent products,
infrastructure documentation — anything that should feel like a machine login rather than a page,
on a dark ground.

Not: a marketing page that needs warmth (`pastel-district`, `sunset-boulevard`); an interface whose
whole point is a status colour ladder read at a glance (`signal`); a holographic or lit-from-behind
surface (`photonic`, `holographic`); a place that is green but organic rather than rastered
(`viridian-fields` — round 5, engraved fern, a darker `#147A57` accent). Within this family the
axis is *square monotone raster*: if you need a chamfer or a second hue, you want 01, 06 or 07.

## Linter warnings kept deliberately

`python tools/build.py --only mainframe-access --no-export` reports, and this kit keeps:

- `contrast-ratio: #93f2b8 on #54e08a2e = 1.26:1` — three times, for `badge-accent`,
  `button-secondary-hover` and `nav-item-active`. The linter grades the tint's **declared** rgba
  instead of compositing it. Composited, `--accent-ink` on an 18% accent tint over the mid plate
  is **8.74:1**, and over `--surface-2` it is **7.95:1**. `tools/verify-lab.cjs`, which samples the
  rendered pixels, passes the kit with no contrast errors.
- `orphaned-tokens`: `neutral`, `border-strong`, `surface-solid`, `grid`, `scan` are defined but not
  referenced by a component. They document the ground (`neutral` = `#020704`, `grid` = `#072A19`,
  the scene field), the texture's stroke (`scan` = white, at 5% / 2.75%) and the two stand-ins
  (`border-strong` = the accent hairline, `surface-solid` = the face). A layered-background kit
  cannot express them as component fills, which is why they read as orphans.
- `token-summary` — informational.

## Files

Authored: `DESIGN.md`, `tokens.css`, `kit.json`, `README.md`. Generated by
`python tools/build.py`: `index.html` (component lab), `DESIGN.html`, `tokens.json`, `theme.css`,
`tailwind.theme.json`. Do not hand-edit the generated set.
