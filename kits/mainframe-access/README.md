# Mainframe Access

**Phosphor green on a black plate that emits.** A plate you look *at*, not through: a `#000000`
face, a green hairline for a frame, a green halo around it, a 1px specular lip along the top and a
floor ramp across it. The one thing drawn on the face is the place's own scanline, 1px rows at a 3px
pitch in green; there is no accent tint and no drawn motif, and the ground runs the same line at 6px.
Square to the pixel, one hue, and a status ladder carried by saturation and material rather than by
chroma. It is the only monochrome kit in the library.

- Kit: `mainframe-access` · order `210` · mode `dark`
- Fonts: Chakra Petch · JetBrains Mono
- Tags: `dark` `terminal` `monochrome` `phosphor` `technical`
- Source: **derived** from the user's `bespoke-desktop` Li//OS prototype
  (`prototypes/v9-lilythium`, place **02 "Mainframe Access"**) — palette, panel construction and
  holo pane taken from the prototype's own tokens, **with every value re-measured on the running
  page** (`getComputedStyle`), because this place's stylesheet is the pre-script state and disagrees
  with what renders: accent, ink ramp, hairline, card face, and the card motif all differ.

## Stance

This is a machine login, not a page. The interface is a black plate seated on a black grid, framed
by a green hairline and lit by a green halo, with a 1px specular lip at its top and a 157° fall
across it; the place's scanlines run behind it (1px every 6px) and inside the panes projected onto
it (1px every 3px). There is no second hue to lean on, so the kit makes value, saturation and
material do the work a palette does elsewhere: accent green is a **fill**, the pale phosphor is the
**text and the ok-state**, and the amber is the warning.

## Lineage — the LIL//OS desk family

| # | place | slug | order | accent | shape | motif |
|---|---|---|---|---|---|---|
| 01 | Azure Technologies | `azure-technologies` | 205 | `#4FD8FF` | chamfer 16 | hex lattice |
| **02** | **Mainframe Access** | **`mainframe-access`** | **210** | **`#5CF79B`** | **square** | **none on the card — scanlines on the ground and the holo pane** |
| 05 | Pastel District | `pastel-district` | 215 | `#FF8FC4` | round 6 | bokeh |
| 06 | Crimson Labyrinth | `crimson-labyrinth` | 220 | `#FF4D5E` | octagon 12 | engraved rose |
| 07 | Sunset Boulevard | `sunset-boulevard` | 225 | `#B06CFF` | chamfer 18 | perspective grid |
| 08 | Viridian Fields | `viridian-fields` | 230 | `#147A57` | round 5 | engraved fern |

All six share one grammar: a hairline frame, a face with a sheen band and a bottom occlusion band, a
157° face fall, one accent hue, one signature motif. They also share **the type** — Chakra Petch for
display and body, JetBrains Mono for labels — deliberately, because these are six places in one OS
and the type is the OS. A later session should not "fix" that per kit.

**What separates this place from its five siblings**, on four axes at once:

| axis | this place | nearest sibling |
|---|---|---|
| corner | square: `--cut: 0`, no `--clip`, radii 0/0/0, pill 2px | four places chamfer 16; two round 5–6 |
| chroma | one hue; the accent is the only colour in the interface | 01/05/06/07/08 each carry two or three |
| surface | **emissive**: black face, green hairline, green halo, no fill, no motif | every sibling paints its motif onto a tinted face |
| status | ladder resolved by **saturation and material**, not hue | the other five can move `--ok`/`--danger` to a new hue |

The second construction — the projected **holo pane** — is shared by the family, and this kit is the
one where it is hardest to spot that a card and a pane are different objects, because both are
black. The card has a hairline and a halo; the pane has corner marks and scanlines and neither.

The nearest collision is not inside this family but outside it: `signal` and `mecha-pilot` are also
dark and technical. They are dense dashboards and an instrument ladder; this is a login screen —
one plate, one hue, nothing to scan.

## What the material is

`--surface` is `--mainframe-access-pane`: the desk's `.card-in` for this place, and this place does
**not** use the family default. Layer order is top-first and **is** the light model:

```
sheen      180deg, rgba(210,255,222,.09) fading to nothing, in a 30px band at the top — a pale green
           light rather than a white one
floor      0deg, rgba(92,247,155,.05) at the top to rgba(0,0,0,.34) at the floor: a full-height
           green-lit ramp where the family default has a 9% occlusion band
tex        THE GREEN SCANLINE — 1px rows at a 3px pitch, rgba(92,255,140,.055)
edge       90deg accent hairline, rgba(92,247,155,.75), 7%→62%, 1px, pinned to the bottom
face       #000000 — the desk's rendered card colour
```

There is no 157° face fall and no accent tint: the desk renders both at zero here, and the plate's
shading comes from the floor ramp and the depth below it rather than from the corner-to-corner fall
the other five carry.

One of the family's layers is absent and one is redirected. The desk puts this place's texture
pseudo-element at `opacity: 0` and its accent tint at `0`, so `::after` paints nothing — but the
scanline is not missing: it lives in the `.card-in` stack itself, 1px rows at a 3px pitch in green,
which is why a card crop shows rows while `::after` is blank. What makes the plate readable without a
tint or a motif behind it is the **depth**, not the face: the deck's own
`drop-shadow(0 0 8px rgba(92,247,155,.16))`, its inset bloom
`rgba(92,247,155,.05) 0 0 30px` and its pale top lip `rgba(200,255,215,.22) 0 1px 0 inset` are
re-expressed as one `--shadow-1` — a box-shadow, because `filter` can hold a drop-shadow but not an
inset. That is why this is the family's one emissive member: the green is in the halo and the
hairline, never in the face.

The order that remains still matters: **a fall under the face is not a fall**, and the sheen sits
above everything because it is the reflection *of* the plate, not a layer *in* it. The occlusion band
is inert on a `#000000` face — it darkens a floor that is already black — and is kept because the
pane is the family's construction, so a project that swaps the face stop inherits a working band.

`--surface-2` — inputs, badges, alerts, code blocks, `card-elevated` — drops the identity edge and
keeps a 6% sheen plus a 2.5% accent tint on the place's own `--panel` `#071009`. It keeps the tint,
unlike the plate, because it is a **well cut into** the plate rather than the plate itself, and a
well with no fill at all is a hole. A 1px accent line on a 34px badge would be a second border, and a
4px scanline on a 2.5rem control would be a moiré: at a 40px control height the pitch repeats ten
times and reads as a printing fault.

Because every surface is opaque, `--blur: none`. The desk forbids glass and `backdrop-filter`, and a
blurred opaque card is only a repaint cost.

## The motif

The card has **none** — that is the measured truth for this place, not an omission (`--mainframe-access-tex: none`,
pasted verbatim from `docs/lilythium/textures.css`). Two motifs do render, at the two scales the desk
uses:

| | pitch | alpha | where |
|---|---|---|---|
| ground | 1px row every **6px** | **3.5%** white | `--mainframe-access-tex-ground`, inside `--mainframe-access-field` (`--bg`) |
| holo pane | 1px row every **3px** | **3%** white (5% at 60%) | `--mainframe-access-holo`, inside `--media-bg` |
| card | — | — | **none**: the desk renders `::after` at opacity 0 |

Both are pasted **verbatim** from `docs/lilythium/textures.css`, where the desk's pseudo-element
`opacity` is already folded into the stroke alpha. The pitch is the image's own period, so neither
layer declares a `background-size`: any size would have to be an exact multiple of 6px (or 3px) or it
would resample the 1px row into a soft 2px row.

The ground is deliberately quiet — a large-celled technical grid at 2.8%/2.4% white over the same
rows at 3.5% — because the components carry no pattern at all. In this place the two-scale rule
inverts: the page is the textured thing and the plates are the still ones.

## The holo pane

The desk has two kinds of surface, and the port needs both. A **card** is built out of the desk: an
opaque face, a hairline, sheen, occlusion, motif. A **pane** is projected onto it: no face, no border,
no shadow — a 13% veil, one accent bloom at its crown, CRT scanlines and four 24px corner marks. That
is the desk's `.pane-holo`, it is the family's signature, and it is wired here to the lab's media
panel through `--media-bg` / `--media-op: 1`.

`--mainframe-access-holo`, in layer order:

| layer | value |
|---|---|
| four corner marks, two 1px hairlines each | 24px, `rgba(92,247,155,.70)` |
| scanlines | 1px rows at a 3px pitch, `rgba(255,255,255,.03)` |
| crown bloom | `radial-gradient(120% 78% at 50% 0%, rgba(92,247,155,.055), transparent 62%)` |
| veil | `rgba(0,0,0,.13)` |

**One re-expression, stated because it is the only one.** The desk lays its 13% over the *scene*,
where 13% of the place's hue is a green tint. The lab's media panel sits on an opaque black card, so
the same 13% has nothing to tint and ships as a film of **black**: a veil that darkens rather than
greens. Everything above it is the desk's own construction, unchanged.

**What cannot be a token.** The desk animates a 180px accent band down the pane every 9s
(`@keyframes sweep`, with a `prefers-reduced-motion` guard). The lab has no element to put it on, so
the kit ships the construction and not the motion. If you rebuild the pane in a project with a real
DOM, add the sweep there; the token is the surface, not the animation.

## Key choices

- **The accent stays distinguishable from `--ok` by saturation and material, not by hue.** Both are
  the same phosphor family: `--ok` is `--accent-ink` `#BCF7CE`, the pale member, and it is only ever
  a status **label on an outlined chip**; the action is an **opaque `#5CF79B` plate** with dark ink.
  Re-checked against the re-measured accent, the value gap **narrowed** — 1.26:1 (`#54E08A` vs
  `#93F2B8`) became **1.14:1** (`#5CF79B` vs `#BCF7CE`) — while the chroma gap **widened**, from
  .55/.37 to .61/.23. So at 12–14px the distinction is a saturated plate beside a near-white wash,
  plus a filled control beside a stroked one. `photonic` makes the same argument with a solid plate
  against a lit pane.
- **A monochrome kit cannot afford a `--text-invert` that is white.** `#5CF79B` is a light fill
  (71% relative luminance): white on it is 1.38:1. The ink is `#02120A` — 13.93:1 on the accent,
  14.94:1 on its hover step.
- **The green is in the depth, and only one component gets to spend it.** `--shadow-1` carries the
  halo, the inset bloom and the pale lip together; `--glow` still belongs to `.btn-primary` alone. A
  page where every chip glows is a page of noise, and the desk's halo is a property of the plate.
- **The ground is a token, not a background.** `--mainframe-access-field` carries the two `#072A19`
  scene fields, the 120px technical grid, the 6px scanline and the `#020704 → #010302` ramp, and
  `--bg` **is** that token. It has to be the whole scene, not just the ramp: every signature token
  is judged at 168×72 on the tile base, and a two-stop `#020704 → #010302` ramp renders there as an
  empty near-black chip. Wrapping the scene is what makes the token legible as the ground.
- **The hairline is the accent.** `--border` is `rgba(92,247,155,.32)` and `--border-strong`
  `rgba(92,247,155,.52)`, both measured. On a black face a white hairline would be the brightest
  thing in the kit; the green one is only as bright as the halo it sits inside.
- **Amber is the desk's, not a new colour.** `--accent-2` is `#FFC04D`, this place's own amber
  sibling; it is the same value as `--warn` on purpose. In a one-hue kit a second decorative hue
  would be the first thing that stopped it being monochrome. `--acc2` `#C2FF8F` is *not* used as a
  second accent — it is the pale member of the accent family and serves as `--accent-ink-hover`.
- **Inputs are recessed, not raised.** `--input-inset` is `inset 0 1px 0` black 55% plus a 3.5%
  white inner keyline — a well, in black and white only.

## Trade-offs

- **The status ladder is mostly saturation, and that costs a hue.** A reader who has only ever seen a
  green-accent kit will expect `--ok` to be a *different* green. Here it is a paler, far less
  saturated one (chroma .23 against the accent's .61), and the distinction is carried by
  chip-vs-plate. After the accent was re-measured brighter, the **value** separation is the thinnest
  it has been (1.14:1): a 12px `ok` label and a small accent plate are close in lightness, and the
  difference is saturation and fill. If the interface needs a status that reads instantly at a glance
  without a shape cue, this is the wrong kit.
- **`--text-dim` is one step lighter than the desk's.** The measured `#6A9B7A` reads **3.96:1** on an
  18% accent tint over `--surface-2` (`#163A23`) — under the 4.55 floor — so it ships as `#77AB89`
  (4.79:1 there, 5.45:1 on the sheen band, 7.97:1 on the face). Same hue, +13 in lightness, and it
  is the only ink in the ramp that is not the desk's exact value.
- **`--danger` was lifted for the same reason.** `#FF6464` measures 4.36:1 on the accent-soft-over-
  panel composite now that the tint underneath is the brighter green; `#FF7070` measures 4.69:1
  there, 5.97:1 on `--surface-2` and 7.80:1 on the face. Both values are still far from `--accent`,
  which is the point of a danger colour in a green kit.
- **The 1px specular lip is not text-safe.** It composites to `#626262` and takes `--text` down to
  4.83:1. It is 1px of highlight under a 9% band; card padding puts the first glyph below it. The
  alternative is deleting the sheen, which is the family's identity.
- **The plate has no pattern, so the kit leans on two hairlines and a halo to be recognisable.** At
  200×120 that is the whole design: black plate, green outline, green glow. It identifies instantly
  against the other five, and it is also the shortest distance to "a black box with a green border" if
  the halo or the sheen is dropped. Neither is decoration; delete either and the kit stops being this
  place.
- **The shared type pairing buys a family and costs distinctiveness.** Six kits with the same two
  faces means the gallery's font column cannot tell them apart; the place has to be carried by
  shape and material. That is the brief's decision, and it is right for a family that is one OS.
- **The pixel fall is built from gradients, so it is invisible to a linter's declared-value check.**
  `scripts/contrast-audit.py` grades a declared `--accent-soft` as if it were opaque and reports
  1.14:1; the composited value (18% of `#5CF79B` over `#071009` = `#163A23`) is 10.42:1. The real
  check is `tools/verify-lab.cjs`, which samples pixels — it passes.
- **Native checkboxes and radios are squared by drawing the box**, not by a radius:
  `--check-appearance: none` plus `--check-bg: #071009`, a `1px solid rgba(92,247,155,.52)` border and
  `--check-checked: var(--accent)`. A native radio paints a circle inside its 1rem box whatever
  `--check-radius` says, and a circle is the one curve this kit forbids. Off is an outlined
  indicator; on is a filled key — the same material argument the action/status split uses.
  `--check-radius: 0px` is still declared, so the box's own corner is the kit's.
- **No `kit.css`, no `--clip`, no `--frame-ring`.** Everything the plate and the pane need is a layered
  background value; there is nothing to construct and no diagonal to reinstate.

## When to use

Developer tools, security and ops consoles, CI and deploy surfaces, terminal-adjacent products,
infrastructure documentation — anything that should feel like a machine login rather than a page,
on a dark ground.

Not: a marketing page that needs warmth (`pastel-district`, `sunset-boulevard`); an interface whose
whole point is a status colour ladder read at a glance (`signal`); a place that is green but organic
rather than rastered (`viridian-fields` — round 5, engraved fern, a darker `#147A57` accent); a page
that needs a visible motif at card scale (every sibling draws one on the face — this one does not).
Within this family the axis is *square, monotone, emissive*: if you want a chamfer, a second hue or a
drawn pattern, you want 01, 06 or 07.

## Linter warnings kept deliberately

`python tools/build.py --only mainframe-access --no-export` reports, and this kit keeps:

- `contrast-ratio: #bcf7ce on #5cf79b2e = 1.14:1` — three times, for `badge-accent`,
  `button-secondary-hover` and `nav-item-active`. The linter grades the tint's **declared** rgba
  instead of compositing it. Composited, `--accent-ink` on an 18% accent tint over the panel is
  **10.42:1**, and over `--surface-2` it is **13.25:1**. `tools/verify-lab.cjs`, which samples the
  rendered pixels, passes the kit with no contrast errors.
- `orphaned-tokens`: `neutral`, `border-strong`, `surface-solid`, `grid`, `scan` are defined but not
  referenced by a component. They document the ground (`neutral` = `#020704`, `grid` = `#072A19`,
  the scene field), the texture's stroke (`scan` = white, at 3.5% / 3%) and the two stand-ins
  (`border-strong` = the accent hairline, `surface-solid` = the rendered black face). A
  layered-background kit cannot express them as component fills, which is why they read as orphans.
  `--mainframe-access-tex` is deliberately *not* in `kit.json`'s `signature` list for the same
  reason it is `none`: a `none` tile renders as an empty chip. The pane replaced it there.
- `token-summary` — informational.

## Files

Authored: `DESIGN.md`, `tokens.css`, `kit.json`, `README.md`. Generated by
`python tools/build.py`: `index.html` (component lab), `DESIGN.html`, `tokens.json`, `theme.css`,
`tailwind.theme.json`. Do not hand-edit the generated set.
