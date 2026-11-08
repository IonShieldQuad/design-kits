# Pastel District

**A dreamy pink instrument panel — bokeh light behind hairline glass.** Place 05 of the Li//OS desk
family, and the only warm-soft place in it. The desk's grammar is intact and unchanged: a 1px frame,
an opaque face carrying a sheen band along its top edge and an occlusion band along its floor, a 157°
fall, a 5% tint of the accent, one drawn motif at 5%, and a hairline of accent along the card's
bottom. What changes is the **subject**: everywhere else in this family the object is a machined
plate; here it is nine discs of light that have gone out of focus, sitting behind that glass.

- Kit: `pastel-district` · order `215` · mode `dark`
- Fonts: Chakra Petch · JetBrains Mono
- Tags: `dark` `pastel` `dreamy` `soft` `nocturnal`
- Source: **derived** from the user's `bespoke-desktop` Li//OS prototype
  (`prototypes/v9-lilythium`, place 05). Palette, panel construction and the nine discs are the
  place's own tokens, copied rather than chosen.
- **Every value was re-measured from the running page** — `getComputedStyle()` on the settled
  prototype (`docs/lilythium/runtime-05.json`, `docs/lilythium/textures.css`), never parsed out of
  its stylesheet. The built page carries a *legacy* motif per place and swaps it when its scripts
  run, so anything read from the CSS text is the pre-script state; for this place the runtime motif
  happens to be the same nine discs, at an *applied* opacity of .05 rather than a declared one, and
  that applied value is what is baked into the stops below. The CSS comment in `tokens.css` records
  the same provenance.

## Stance

A room in an operating system that was drawn at night and lit from behind the furniture. The
instrument-panel grammar is the OS — frame, sheen, floor, fall, one accent, one motif — and in this
room the thing the panel is looking at is a bloom. So the card is a pane you read *across* rather
than a plate you read *on*: the discs are inside the material, behind the tint, under the sheen, the
corners are 6px instead of a 16px chamfer, and the accent is a hairline at the floor rather than a
glowing edge. Nothing is cut, nothing blurs, nothing glows twice.

## Lineage

Six places from one desk. The name is the place name from the prototype's own world chart.

| # | place | slug | corner | accent | motif | what it is |
|---|---|---|---|---|---|---|
| 01 | Azure Technologies | `azure-technologies` | chamfer 16 | `#4FD8FF` | hex lattice | cold corporate network |
| 02 | Mainframe Access | `mainframe-access` | square | `#54E08A` | scanlines | monochrome terminal |
| **05** | **Pastel District** | **`pastel-district`** | **round 6** | **`#FF8FC4`** | **bokeh** | **← this kit** |
| 06 | Crimson Labyrinth | `crimson-labyrinth` | chamfer 16 | `#FF4D5E` | engraved rose | theatrical, inverted status |
| 07 | Sunset Boulevard | `sunset-boulevard` | chamfer 16 | `#B06CFF` | perspective grid | wide violet dusk |
| 08 | Viridian Fields | `viridian-fields` | round 5 | `#147A57` | engraved fern | analog, organic, green |

**The axis is temperature and focus.** Five of the six are cool — cyan, phosphor green, crimson,
violet, viridian — and four of those are cut: a chamfer is a cut, a lattice is in register, a colour
is emitted. Pastel District is warm, and its light is *out of focus* — a bloom instead of a grid,
nine discs instead of a tiled field, 6px instead of a 16px chamfer. Its nearest sibling by shape is
Viridian Fields, which is also round, so temperature and motif have to do the separating there; they
do, because a green engraved fern is the opposite of a warm pink bloom.

Two kits from one reference is the standing hazard of this library. The guard here is structural:
you cannot mistake a soft 6px pink bloom for a 16px chamfer with a hex lattice at any size the
gallery renders.

## The material

`--surface` is `--pastel-district-pane`: one value, seven layers, and **the layer order is the light
model**:

| # | layer | what it is | why it is there in this order |
|---|---|---|---|
| 1 | sheen | white 30% on the first 1px, 17% on the next, 4.7% to 34% of a 9%-tall band | the specular lip: glass has a bright top edge, and it must be *over* everything or it is paint |
| 2 | occlusion | black 46% → 13.7% → 0 over a 9% band at the floor | the card sits in shadow where it meets the page; over the motif, or the discs float in front of the card |
| 3 | **the nine discs** | the place's `--tx-bokeh`, alpha-baked at `--txA` `.05` | **behind** the tint — that is the whole kit. Over the tint they are a dotted pattern; under it they are light behind glass |
| 4 | identity edge | accent 55%, 1px, inset 7%…96% along the floor | the family's accent hairline, and the only one of the four kits where it is a straight line rather than a ring |
| 5 | tint | accent at 5% | warms the face toward the place; it must sit over the motif or the discs read as white, not as pink light |
| 6 | fall | 157°: white 12% → 0 by 44% → black 24% at 78% → black 52% | the face is lit from above-left and falls away down-right; over the face or it is not a fall |
| 7 | face | `#23141D` | the desk's `--face`, and the only opaque layer |

`--surface-2` — inputs, badges, alerts, code blocks, `card-elevated` — drops the discs and the
identity edge and keeps a shallow sheen and half the tint on the place's `--panel`. Nine discs on a
2.5rem control is clutter, not material.

**The identity edge composites under the occlusion band**, because that is where the desk put it: at
the card's bottom row the accent at 55% sits under black at 46%. Measured on the rendered page it
lands at `rgb(82,45,63)` against a card body of `rgb(21,11,17)` — a warm plum-pink hairline, not a
bright underline. That is the shared construction, not a local tuning: all six places do it, and
re-ordering the layers to make this kit's line hotter would make it the odd one out.

**Two accent radials the desk's card also carries are absent here, deliberately.** `.card-in` has an
identity glow and a crown radial *inside* the card, and on the running page both are at **0 alpha**
for place 05 — measured, not inferred (`runtime-05.json`). A 0-alpha radial paints nothing, so they
are simply not in `--pastel-district-pane`, and there is no placeholder layer standing in for them.
Do not "restore" them: a pink bloom inside the card is a different kit's construction, and this one
already gets its glow from the ground and its hard light from the holo pane.

## The motif

Nine discs, drawn as radial gradients, **positioned in %** so one stack fills any box, at the radii
the desk drew them: 3, 4, 4, 5, 5, 5, 6, 6, 7px (with 1px of falloff). Two scales, deliberately
different jobs:

| | where | peak alpha | pitch | how it is placed |
|---|---|---|---|---|
| card | `--pastel-district-tex`, layer 3 of the pane | **.0425** (the desk's `--txA` .05 folded into the stop) | no pitch — % positions, 3–8px radii | `0 0/100% 100% no-repeat` |
| ground | `--pastel-district-tex-ground`, one layer of `--bg` | **.0234** — the source's own ground step (`.0425 → .0234`, 55%) | same nine, same positions | `0 0/100% 100% no-repeat`, over a 120px technical grid |

Both declarations are pasted **verbatim** from `docs/lilythium/textures.css`. The alpha is baked
into the stops because the desk applied `--txA` as a pseudo-element `opacity`, which a background
layer cannot do — so nothing here may be re-timed, re-alpha'd or re-drawn, and the numbers above are
descriptions of the source, not knobs.

Bokeh is the only motif in this family that cannot tile: a repeated constellation is a pattern, and
a pattern is the opposite of out-of-focus light. That is why the card and the ground carry the same
nine rather than a tiled field, and why the ground's job is to be *quieter* — its own lower alpha — rather
than twice the pitch.

## The holo pane — the family's projected surface

The desk has **two** kinds of surface and this port needs both. A **card** is built out of the desk:
an opaque face, a hairline, a sheen, an occlusion, one drawn motif. A **pane** is *projected onto*
one — no face, no border, no shadow, just a 13% veil, one accent bloom at its crown, 3px CRT
scanlines and four 24px corner marks. That is the desk's `.pane-holo`, and it is the family's
signature; a family of six tinted plate skins is what you get without it. It ships as one token,
`--pastel-district-holo`, wired to the lab's media panel (`--media-bg`) at `--media-op: 1` and named
in `kit.json`'s `signature`, so it renders both at 168×72 in the Signature row and at full size under
the cards.

| # | layer | what it is | why here |
|---|---|---|---|
| 1 | four corner marks | eight 1px hairlines: two per corner, 24px arms, accent at 70% | they are the projection's registration brackets — *over* the veil or they read as part of the card |
| 2 | scanlines | 1px rows at a **3px** pitch, white at 3% — the desk's `.scan`, held at 60% | the CRT grille: the one thing that says "emitted", not "printed" |
| 3 | crown bloom | accent at 5.5%, 120% × 78% at `50% 0%` | the light source the grille is cutting across |
| 4 | veil | black at 13% | the film; last in the stack because it is the surface itself |

**In most of the family the pane is a HUD. Here it is the subject stated a second time.** This
place's subject is light falling out of focus: the nine discs are that light *diffuse*, and the pane
is the same light *given an edge* — the crown bloom is a light source with a boundary, and the 3px
grille across it is the only hard geometry in the kit apart from the 1px frame. Diffuse light and
focused light on the same card is the whole kit in one object, and it is why this kit gets more out
of the pane than its five siblings do. Measured on the lab's own render: the panel's centre column
runs `rgb(65,43,55)` at the top edge to `rgb(46,29,38)` at mid-height and `rgb(41,24,33)` at the
floor, with the corner arms measuring `rgb(195,112,152)` — so the bloom is a real falloff and the
marks are the brightest thing on the surface, not decoration.

Two things about the pane have to be said plainly rather than left to the code:

- **The veil is re-expressed as a black film.** The desk lays 13% of the place's own pink over the
  *scene*, where it tints the air behind a floating panel. The lab's media panel sits **on an opaque
  card**, and a pink film there would only be more card — it has nothing to tint. So the same 13% is
  a film of **black**: it darkens what is underneath, which is what makes the bloom and the brackets
  read as *projected onto* a surface rather than painted in the card's own colour. No face is added;
  the card underneath is the face. This is the one place the construction is not the desk's
  verbatim — mark length, line weights, the 3px pitch, the .055 bloom and the 13% strength are all
  the desk's own measured values.
- **The 9s sweep cannot be a token.** The desk animates a 180px accent band down the pane every 9
  seconds (`@keyframes sweep`, behind a `prefers-reduced-motion` guard). A background value carries
  no keyframes and the lab has no element to run them on, so the family ships the construction and
  not the motion — the pane here is the desk's, standing still. A project that wants the sweep adds
  one absolutely-positioned band with that animation; nothing in this kit has to change for it.

## Key choices

- **Pink is a light fill, so the ink on it is dark.** `--text-invert: #2A0F1B` at **8.4:1** on
  `#FF8FC4` (10.0:1 on the hover step). White would have been 1.4:1 and is the mistake this palette
  invites.
- **`--accent-ink` exists because the fill fails as a label.** `#FF8FC4` reads at 5.7:1 on the
  composited pane but reads as a *button*; 12px labels take the desk's own `--accHi` `#FFB9DB`
  (**7.6:1** on the pane, **7.5:1** on the accent badge's composited tint).
- **`--danger` is deliberately darker and more saturated than the action.** `#FF7086` is only **21°
  off** `#FF8FC4` in hue, so hue cannot carry the separation — chroma and value do. The red is
  4.86:1 on the page floor and 5.52:1 on `--surface-2`, where an error actually appears; the pink is
  an opaque *plate* with a dark label, so an error never reads as a pastel button. Put them in the
  same control group and you need the label to tell them apart — that is the trade, and it is the
  one place this kit is fragile.
- **Mint is one hue doing two jobs.** The place's scene has exactly one pale mint, so `--accent-2`
  and `--ok` are the same value (`#6EE7B0`). They never compete: the counterpoint appears in a chart
  series and in the `ok` chip, never as an action colour. It is honest to the source rather than
  inventing a second green to tell them apart.
- **`--fill-bg` completes at 55%.** The desk's ramp is the accent's 25% tint into the accent, but
  the avatar's label sits at the ramp's midpoint, where `#2A0F1B` on a 62% pink is 3.8:1. Running
  the ramp out to the solid accent by 55% keeps the two-stop construction and the label's 8.4:1.
- **The media panel is the holo pane, not a place plate and not an accent ramp.** `--media-bg` is
  `--pastel-district-holo`: no face, four corner marks, a 3px grille, one crown bloom, one 13% film.
  It replaced an earlier plum-bloom plate in this kit, and the plate was **removed rather than kept
  as an alternate** — a construction defined and bound to nothing is exactly how a port ends up with
  a superseded surface still shipping, and the pane is the better answer here anyway: the card is
  already the diffuse version of this place's light, so the media area is where it gets to be sharp.
- **`--media-op: 1`**, because the pane is already that dark; the default .85 greys it.
- **The holo pane is the kit's second signature tile** (168×72, alongside `pane`, `tex`, `field`).
  At that size the four 24px brackets and the grille are the whole read — which is the point: a
  viewer can tell from the tile that this is a projected surface and not a coloured rectangle.

## Trade-offs

- **No `--clip`, no chamfer, and that costs silhouette.** A chamfer is the family's loudest shape
  cue and this kit gives it up for softness. The compensation is that no other place has a round
  corner, so the 6px reads as identity by *exclusion* — but at gallery-tile size the two round
  places (05, 08) are closer to each other than any pair of the chamfered four.
- **Every surface is opaque, so `--blur: none`.** Photonic spends a `backdrop-filter` because its
  panes are 56% film; here the translucency is *inside* the material — a 5% tint over baked discs —
  which no `backdrop-filter` can produce. A blur would cost a compositor layer and change nothing.
- **The shared type pairing costs softness.** Chakra Petch is a squared technical face; a stricter
  reading of "dreamy" would reach for something rounder. The family's argument is that the place
  supplies the register and the OS supplies the voice — six rooms, one building. Don't "fix" the
  fonts: they are identical in all six kits on purpose.
- **The `--pastel-district-tex` signature tile reads faint at 168×72.** It is the raw motif at the
  desk's own 5% over the tile's nested surface — a 9-level lift. The brief forbids re-timing it, so
  it stays; the `holo`, `pane` and `field` tiles are the three that sell the kit, and the `tex` tile
  is honest about being an overlay. (Do not raise the alpha to "make the tile show": the card then
  reads as a dotted fill.)
- **The ground is a slow field.** Both scene blobs are sized in % of the *document*, so on a 3500px
  page the plum peak lands around 38% of the scroll rather than at the masthead; `--wash` exists to
  put a bloom at the top, and it is the same plum rather than the default accent-soft radial.

## When to use

Soft, playful or nocturnal products: anime and music editorial, generative-tool and creative-coding
panels, a portfolio that should feel lit rather than lit-up, a product page for something cute that
is not a toy. Anything that wants pink at night without going pastel-**light**.

Reach for a sibling instead when: the brief is cold and technical (**`azure-technologies`**), a
monochrome terminal (**`mainframe-access`**), theatrical and dangerous (**`crimson-labyrinth`**),
violet and wide (**`sunset-boulevard`**), or green and analog (**`viridian-fields`**). Outside the
family: `kawaii` if the dreaminess should be *cute* rather than nocturnal, `retro-anime` or `sakura`
if it should be pink and light, `city-pop` if it is a poster rather than a panel.

## Linter warnings kept deliberately

`python tools/build.py --only pastel-district --no-export` reports six warnings and one summary
line, and this kit keeps all of them (no errors; exit 0):

- `contrast-ratio: #ffb9db on #ff8fc42e = 1.32:1` — three times (`badge-accent`,
  `button-secondary-hover`, `nav-item-active`). The linter grades the accent tint's **declared**
  rgba and cannot composite it. Composited: `#FFB9DB` is **7.5:1** on the badge (18% accent over
  `--surface-2`), **5.4:1** on the active nav item (18% accent over the pane) and **6.4:1** on the
  secondary button's hover (18% accent over the page floor). `tools/verify-lab.cjs`, which samples
  the real DOM stack, passes the kit with no contrast error.
- `orphaned-tokens: neutral`, `scene`, `scene-floor` — the ground's three values. They are the page,
  not a component: `neutral` is the floor the inks are graded against, `scene` is the plum field and
  `scene-floor` is what the ramp ends on. DESIGN.md's component list has no sub-token for a page
  ground, so they are unreferenced by construction. (A fourth, `border`/`border-strong`, would have
  been orphaned too; `section-rule` and `divider` reference them.)
- `token-summary: 21 colors, 7 typography scales, 4 rounding levels, 5 spacing tokens, 23
  components` — informational.

Two notes on the tooling, since a later session will look for them:

1. **`scripts/contrast-audit.py` does not exist in this repo** (it is named in
   `docs/lilythium/BRIEF.md`). The contrast table in DESIGN.md and this file was produced by
   compositing the layer stacks in sRGB offline and then checked against
   `tools/verify-lab.cjs`, which samples the rendered pixels next to each text box.
2. **`borderColor` is not a recognised DESIGN.md component sub-token**, so no border can be declared
   in the spec's component block; the frame is documented in prose and in `tokens.css`.

## Files

Authored: `DESIGN.md`, `tokens.css`, `kit.json`, `README.md`. Generated by
`python tools/build.py`: `index.html` (component lab), `DESIGN.html`, and — once the aggregate run
exports — `tokens.json`, `theme.css`, `tailwind.theme.json`. Do not hand-edit the generated set.
