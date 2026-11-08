# Viridian Fields

**A matte botanical console — deep emerald, an engraved fern, no glow.** This is the one place in
the Li//OS desk that is absorbed rather than lit. The action colour is a dark, matte emerald and it
is the only opaque fill on the page; the ink on it is the lightest thing in the kit; the material is
a plate carrying one fern engraved at 248px, not a field of leaves; and the only emanation anywhere
is the place's own 14px emerald shadow at 26%, under the primary button. Its one projected surface —
the family's holo pane — is here a bracketed window onto the same plate rather than a light: its
24px corner marks measure 2.52:1 and its crown bloom 1.06:1. Restraint is the whole idea, so the
restraint is a token decision and not a mood.

- Kit: `viridian-fields` · order `230` · mode `dark`
- Fonts: Chakra Petch · JetBrains Mono
- Tags: `dark` `botanical` `matte` `nature` `calm`
- Source: **derived** from the user's `bespoke-desktop` Li//OS prototype (`prototypes/v9-lilythium`,
  place 08) — palette, panel construction and the drawn fern are the prototype's own tokens, taken
  from `docs/lilythium/textures.css` already alpha-baked and pasted unmodified.

## Stance

Every other dark kit in this library is a light source. This one is the surface the light has
already left. The desk's note for place 08 is explicit about the difference from its sibling
Mainframe Access: *that* green is phosphor read as information — bloom, scanlines, a glow wash.
*This* green is a deep matte emerald, the colour of the underside of a leaf, and the interface is a
console set on it.

The desk enforces that at the source, and this is the strongest evidence the port has for "not
emissive": for place 08 the desk sets its **two in-card accent radials — the identity glow under the
frame and the crown glow over the card — to zero alpha.** Not dimmed: switched off. That is why the
card material below has no radial in it at all, and why the only emanation in the kit is the
place's own 14px shadow at its own width. There is no bloom over the ground, no accent wash, and no
glass: `--blur: none`, because a blurred opaque card buys nothing and costs a repaint.

The one scanline ruling in the kit lives inside the holo pane — 1px rows at a 3px pitch, 3% white,
measured at **1.07:1** — and so does its one bloom, the pane's crown, measured at **1.06:1**. Both
are devices rather than emissions; see [The holo pane](#the-holo-pane) for why they measure what
they measure and why they were not raised.

What replaces the light is **drawing**: a 1px frame, a sheen band with a specular lip, a 157° face
fall, an emerald identity edge along a plate's floor, one engraved fern, and — on the pane — a
bracket and a ruling. A matte surface is legible because of its edges, not its highlights.

## Lineage — and what makes this one different

| place | kit | order | accent | shape | motif |
|---|---|---|---|---|---|
| 01 | Azure Technologies | 205 | `#4FD8FF` | chamfer 16 | hex lattice |
| 02 | Mainframe Access | 210 | `#54E08A` | square | scanlines |
| 05 | Pastel District | 215 | `#FF8FC4` | round 6 | bokeh |
| 06 | Crimson Labyrinth | 220 | `#FF4D5E` | octagon 12 | engraved rose |
| 07 | Sunset Boulevard | 225 | `#B06CFF` | chamfer 18 | perspective grid |
| **08** | **Viridian Fields** | **230** | **`#147A57`** | **round 5** | **engraved fern** |

All six are one instrument-panel grammar: a hairline frame, an opaque face carrying a sheen band and
a bottom occlusion band, a 157° face fall, a 5% accent tint, one drawn texture at 5–9%, one accent
hue, one signature motif, and one type pairing — plus the family's second surface, the projected
holo pane (13% veil, four 24px brackets, a 3px ruling, a crown bloom), which all six carry at the
desk's own alphas. That is why "has a pane" is not an axis: what a pane *does* differs by place,
and here it does not glow. The axis that separates the six is **what the accent does to the ink**:

- In the other five the accent is a *light* — a cyan, a phosphor green, a pink, a crimson, a violet
  at thumbnail brightness — so the fill is bright and the ink on it is dark.
- Here the accent is **dark** (`#147A57`, 0.15 relative luminance) and the ink on it is light
  (`#EAF6F0`). That single inversion is why this kit has an `--accent-ink` at all (the fill is
  3.4:1 on a pane and unreadable as a label) and why `--text-invert` is a light ink instead of a
  dark one. **Do not "correct" either one to match its siblings.**

**Against `zen-garden`** (light, calm, muted, order 85), which is the sibling a stranger is most
likely to confuse this with: that kit is *daylight* — a light raked-sand ground, wet-stone ink, a
moss sage action, soft wide shadows, 8–14px radii, and no drawing at all. This kit is *understory*:
a dark matte console, a hairline 1px frame, a 5px radius, an engraved plate in the corner of every
card and a single fern struck into the ground. One is weather; the other is material. They share a
mood (restraint) and nothing else — not polarity, not shape, not construction, not type.

## What the material is

The card is the desk's own `.card-in`, ported to one token (`--viridian-fields-pane`). Layer order,
top first, and the order *is* the light model:

| # | layer | value | job |
|---|---|---|---|
| 1 | sheen + 1px specular lip | `rgba(255,255,255,.30) 0 1px → .17 1px → .048 34% → 0 100%`, band `100% 9%` | the top edge catches light |
| 2 | occlusion | `rgba(0,0,0,.46) → .138 38% → 0`, band `100% 9%` at the floor | the bottom of a plate falls away |
| 3 | **engraved fern** | the place's plate, `100% 82% / 248px auto no-repeat` | the mark struck into the corner |
| 4 | identity edge | `rgba(20,122,87,.55)`, 1px along the floor | the accent, as a line |
| 5 | tint | `rgba(20,122,87,.05)` | the hue, absorbed into the face |
| 6 | face fall | `157deg`, white .12 → 0 44% → black .24 78% → .52 100% | the instrument face |
| 7 | face | `#0C1410` | the opaque floor |

Why that order: a texture under the tint is invisible, a fall under the face is not a fall, and the
sheen has to be over everything or it reads as a light *inside* the material rather than on it.

`--surface-2` is the nested tier worn by inputs, badges, alerts, code blocks and `card-elevated`.
It drops the fern and the identity edge — a 248px engraving on a 2.5rem control is clutter, not
material — and keeps a shallow sheen plus half the tint over the desk's `--panel` (`#0F1D19`).

Because every *card* surface is opaque, `--blur: none`. The desk forbids glass and there is nothing
behind a plate to see. The holo pane is the one surface that shows what is behind it, and it does so
with a 13% film of black rather than a `backdrop-filter`: a veiled plate is not a blurred one, and
it costs no repaint.

## The motif

One engraved fern, drawn once and never tiled. The alphas are baked into the SVG; nothing here was
re-tuned.

| where | pitch | alpha | placement |
|---|---|---|---|
| the card plate | **248px** wide, `auto` tall | stroke `#fff` at **9%** | bottom-right of the plate (`100% 82%`), `no-repeat` |
| the ground | **520px** wide, `auto` tall | stroke `#fff` at **4.95%** | near the floor of the page (`100% 86%`), `no-repeat` |
| the media panel | **no plate of its own** | — | the card's engraving shows through the pane's 13% veil at 87%; see below |

Two scales, different jobs: on a card the fern is a **plate** — a mark you can read across a plate's
corner; on the ground it is a **presence** — the same engraving at twice the size and roughly half
the alpha, so it sits behind the page rather than decorating it. Neither repeats. An earlier build
of the texture tiled the engraving at 96px; that is superseded, and repeating the fern anywhere
makes it wallpaper.

Both declarations are pasted **verbatim** from `docs/lilythium/textures.css` and are byte-identical
to it — re-pasted and re-checked against `docs/lilythium/runtime-08.json` (`texture_applied_opacity:
0.09`), not re-derived and not re-alpha'd. The plate is 248px wide at `100% 82%`, drawn once, and
the ground line is the same drawing at 520px.

## The holo pane

The desk has two kinds of surface and this port carries both. A **card** is built out of the place:
opaque face, hairline, sheen, occlusion, engraved plate. A **pane** is *projected* onto one: no
face, no border, no shadow — just a film, four brackets, a ruling and a bloom. That is the desk's
`.pane-holo`, it is `--viridian-fields-holo`, and `--media-bg` is wired to it, so the lab's media
panel is this place's projected surface.

| device | value | job |
|---|---|---|
| veil | 13% black | what separates the pane from the plate |
| corner marks | four 24px brackets, `rgba(20,122,87,.70)` | the frame, scored into the pane |
| scanlines | 1px rows at a 3px pitch, 3% white | the CRT ruling |
| crown bloom | `radial-gradient(120% 78% at 50% 0%, rgba(20,122,87,.055) 0%, rgba(20,122,87,0) 62%)` | the light, as the family has it |

### The tension, resolved

This is the family's one matte kit and the pane is the family's one lit object — a bloom at a crown
is a claim about emission, and this kit's entire argument is that nothing here emits. The
resolution is **not** to split the difference on alpha: the desk's `.70` and `.055` are the family's
and are kept exactly. It is to let this place's accent do at those alphas what it does everywhere
else — absorb — and then to say what that measures. Every number below is composited from the
running lab: `getComputedStyle()` on the settled page plus pixel sampling of the rendered panel, not
derived from the stylesheet.

| measurement | value |
|---|---|
| corner mark, as it composites over the pane | `rgb(24, 99, 72)`, luminance **0.096** |
| the accent fill it is made of (`#147A57`) | luminance **0.148** — the mark is **1.35:1 *darker*** than the button |
| mark against the pane's darkest ground | **2.52:1** |
| crown bloom at its strongest (panel top centre) | **+6 of 255** in green; **1.06:1** against the same pixel bloom-free |
| scanline light row against dark row | **+6 of 255**; **1.07:1** |
| the pane's own ground against the plate below it | **1.09:1 *darker*** |

Read that stack in order and the pane resolves itself. **The veil is black, so the pane can only
subtract:** its ground measures 1.09:1 *below* the card it is laid on, which makes the panel the
darkest thing in the card — a window, not a lamp. Then the accent appears twice, and both times it
is absorbed: at `.70` it composites to a line *darker* than the button it shares a hue with (0.096
against 0.148), and at `.055` it lifts the crown by six levels of 255. So: **the bloom is inert
here, and that is the honest result rather than a defect.** Six levels sits under any perceptual
threshold worth quoting and 1.06:1 is indistinguishable from grain. The pane is legible in this
place because of its **drawn** devices — a 24px bracket at 2.52:1 and a 3px ruling at 1.07:1 — and
not because of its light. Which is the sentence the rest of the kit already makes: a matte surface
is legible by its edges, not its highlights.

That is what a projected pane looks like in a place whose whole point is that nothing glows. The
family's construction survives intact — the film, the four brackets, the ruling, the bloom, at the
desk's own alphas — and the *light* in it does not survive. The pane keeps its shape and loses its
emission, and the six levels are the measurement of that loss.

**Inert in one direction only, and not raised.** The brackets read and the ruling reads; the crown
does not. Lifting `.055` until the crown reads would import a sibling's register — a lit object in
the one place whose claim is absorption — and dropping the bloom would make this pane a different
construction from its five siblings'. Keeping the family's alpha and reporting the six levels is the
only choice that is both honest and the same object.

### Two re-expressions, both deliberate

- **The veil is black, not 13% of the hue.** The desk's pane is laid over the scene; this one is
  laid on an opaque card, where 13% of an already-absorbed emerald is not measurable. A film of
  black is what the same 13% means here, and it is the one place this kit re-expresses the desk.
- **The card's fern shows through the panel at 87%.** A pane has no face, so what is behind it is
  what you see under the film: the panel carries the card's own engraving beneath it. That is
  correct — the pane is projected *onto the plate* — and it is worth knowing before someone
  "fixes" it by painting a face into the token, which would turn a projected pane back into a card.

### What cannot be a token

The desk sweeps a 180px accent band down the pane every 9s (`@keyframes sweep`, with a
`prefers-reduced-motion` guard). The lab has no element to put that animation on, so this kit ships
the construction and **not the motion** — a stated limitation, not an omission.

## Key choices

- **The accent is a fill, and the pale member is the label.** `--accent` `#147A57` on a pane is
  3.4:1 — fine as a button, wrong as an eyebrow. `--accent-ink` is the desk's own `--accHi`
  `#5BCBA0` (9.0:1 on the flat pane, 6.4:1 on a card's lit end, 5.9:1 on the scene field).
- **`--text-invert` is light** (`#EAF6F0`, 4.79:1 on the accent) because the fill is dark. This is
  the inverse of the other five places and the single most likely thing for a later session to
  "fix" wrongly.
- **The fill hover goes deeper, not lighter.** `--accent-hover` is `#116B4C`: with a light label on
  a dark fill, raising the fill's luminance *drops* the label to 3.96:1. A press settles.
- **`--ok` is kept clearly lighter than the accent.** Both are greens, so the state colour is held
  at 0.50 relative luminance against the accent's 0.15 (2.8:1 apart) and stays minty. A green chip
  beside a green button has to be separated by lightness and by material — the button is an opaque
  plate, the chip is an outlined pill.
- **The accent hairline is the rim of every control.** `--border-strong` is the desk's `--accLine`
  (`rgba(20,122,87,.60)`), and `--border` is the desk's frame white at 14%. One is a plate's rim,
  the other is the page's rule; they are not interchangeable.
- **The ground is quiet by design.** Two soft fields of the scene's `#16382B`, a 120px ruling and
  one 520px fern — large-celled, half the card's alpha. Equal weight would make the page one busy
  field and every card read as texture inside texture.
- **The pane keeps the family's alphas, not this place's.** `.70` for the brackets and `.055` for
  the crown are the desk's, unmodified, and the measurements above are what they do on a near-black
  plate: 2.52:1 and 1.06:1. A kit that "tuned" those numbers would stop being the same object as
  its five siblings — and the one thing this family cannot afford is six tinted plate skins.
- **Type is the family's, unchanged.** Chakra Petch over Chakra Petch with JetBrains Mono labels.
  All six places ship it because they are places in one OS and the type *is* the OS. It is not an
  oversight.

## Trade-offs

- **A dark accent is a weaker call to action.** `#147A57` is quieter than any sibling's accent by
  construction: on the ground it measures 2.2:1, so it cannot be read as a colour *at all* — only
  as a shape with a light label on it. That is the register, but it means a page whose primary
  button must shout needs another kit.
- **`--text-dim` is unusually light** (`#A2B9AD`, 5.6:1 on the scene field and 8.7:1 on a flat
  plate). On a matte kit, greying secondary copy into nothing is what makes an interface feel *dim*
  rather than *quiet*; the tier is separated by size and weight instead.
- **No glow means no focal halo.** The primary button is found by its opacity and its label
  contrast, not by a bloom. At thumbnail size that makes it the calmest tile in the family, and the
  least eye-catching.
- **The fern is a drawn asset, not a gradient.** It is ~4KB of base64 declared once as
  `--viridian-fields-tex` and referenced by the card material and the signature tile, so it is not
  duplicated. No gradient makes a fern — this is the case `docs/KIT-SPEC.md` covers under drawn
  artwork, and it carries its own alpha plus a colour layer beneath it.
- **The projected pane carries no light here.** Its brackets are 2.52:1 — a visible edge, but under
  the 3:1 WCAG sets for graphical objects, so the marks are ornament and must never become the only
  carrier of a state (use the accent plate or a label). Its crown bloom measures 1.06:1, which is
  the measurement of "this place does not emit" applied to the family's own lit device.
- **No sweep.** The desk animates a 180px band down the pane every 9s; the lab has no element to
  hang it on, so the port ships the construction without the motion. Anyone adding it should keep
  the reduced-motion guard and must not raise the band's alpha to compensate.
- **The signature tile for `--viridian-fields-tex` is faint, on purpose.** At 168×72 it shows a
  crop of white strokes at 9% over the nested tier — an engraving, not a chip of colour. Three of
  the four tiles (`--viridian-fields-pane`, `--viridian-fields-holo`, `--viridian-fields-field`)
  carry the identity; that one documents the mark.
- **`--fill-bg` cannot rise above the accent.** The progress ramp and the avatar go from a 25% tint
  of the accent to the accent itself; anything lighter and the avatar's light initial fails 4.5:1.
- **No `kit.css`.** Everything this kit needs is reachable from tokens — the plate and the pane are
  layered backgrounds, the fern is a data URI, the shape is a radius.

## When to use

Calm and natural products, long-reading interfaces, landscape and field-work tools, botanical and
ecological anything, quiet internal consoles — places that should feel **grown rather than lit.**

Siblings instead: **`zen-garden`** when the page must be light (this one is a dark console with an
engraved plate; that one is raked sand in daylight). **`mainframe-access`** when the green must read
as information — terminal, telemetry, phosphor. **`crimson-labyrinth`** when the motif should be
ornamental engraving on a hot ground rather than botanical. **`signal`** or **`quiet`** for dense
data tools where this register is too atmospheric.

## Contrast

WCAG 2.1 relative luminance, composited against the pixels the ink actually sits on — the pane is
graded at both its flat face (`#0C1914`) and the lit end of its 157° fall (`#293530`), and the
ground at the scene field (`#16382B`) with the page ruling over it.

| Pair | Ratio | Target |
|---|---|---|
| `--text` on `--bg` (scene field + ruling) | **10.61:1** | ≥ 7 ✓ |
| `--text` on `--bg` (field + ruling + fern stroke) | **9.24:1** | ≥ 7 ✓ |
| `--text-muted` on `--surface` | **10.66:1** | ≥ 4.5 ✓ |
| `--text-muted` on the fall's lit end | **7.55:1** | ≥ 4.5 ✓ |
| `--text-dim` on `--bg` (field + ruling) | **5.64:1** | ≥ 4.55 ✓ |
| `--text-dim` on `--bg` (field + ruling + fern stroke) | **4.92:1** | ≥ 4.55 ✓ |
| `--text-dim` on `--surface` / lit end | **8.65 / 6.12:1** | ≥ 4.55 ✓ |
| `--text-invert` on `--accent` | **4.79:1** | ≥ 4.5 ✓ |
| `--accent-ink` on `--bg` (scene field + ruling) | **5.88:1** | ≥ 4.5 ✓ |
| `--accent-ink` on `--surface` / lit end | **9.01 / 6.38:1** | ≥ 4.5 ✓ |
| `--accent-ink` on `--accent-soft` (22%) over the pane | **7.32:1** | ≥ 4.5 ✓ |
| `--accent-ink` on `--accent-soft` over `--surface-2` | **5.81:1** | ≥ 4.5 ✓ |
| `--ok` / `--warn` / `--danger` / `--info` on `--surface-2` | **7.49 / 7.19 / 5.19 / 5.61:1** | ≥ 4.5 ✓ |
| `--accent` against `--ok` (separation) | **2.80:1** (lum .15 vs .50) | distinguish by material |

The pane's devices are not text and are graded as ornament rather than against a text floor:
brackets **2.52:1**, ruling **1.07:1**, crown bloom **1.06:1**, and the pane's ground **1.09:1
below** the plate it is projected on (see [The holo pane](#the-holo-pane)). Nothing in the pane is
used to carry a word, so none of those numbers is a WCAG text pair.

## Values re-measured, and what that changed

This kit was re-verified against the **running page**, not its stylesheet — the prototype's scripts
swap motif alphas and placements after load, so the CSS text is the pre-script state and this port
had been built from it. `docs/lilythium/runtime-08.json` and `docs/lilythium/textures.css`
(`getComputedStyle()` on the settled page) are the sources:

- **The two motif declarations are byte-identical to `textures.css`** — 248px at `100% 82%` for the
  card, 520px at `100% 86%` for the ground, alphas `0.09` and `0.0495` baked into the SVG and not
  re-derived. Runtime confirms `texture_applied_opacity: 0.09`.
- **Colours, inks, hairlines and shape were confirmed unchanged**: accent `#147A57`, accent-ink
  `#5BCBA0`, the ink ramp, `--border` `rgba(255,255,255,.14)`, face `#0C1410`, radius 5px, no clip,
  and the place's own `drop-shadow(0 6px 16px rgba(0,0,0,.50))`.
- **The desk switches this place's two in-card accent radials to zero alpha** (identity glow and
  crown glow) — recorded above as the evidence for the "not emissive" claim.
- **The pane was added, not tuned**: `--viridian-fields-holo` at the family's own `.70` / `.055`,
  wired to `--media-bg` at `--media-op: 1`, and added to `kit.json`'s `signature`.
- The linter's token summary (22 colours, 7 type scales, 4 radii, 5 spacing, 26 components) is
  unchanged: the pane is a construction, not a new colour.

## Values changed, with the numbers that forced them

| token | from | to | why |
|---|---|---|---|
| `--danger` | `#E05A5A` | `#EE7A70` | `#E05A5A` measured **3.92:1** on `--surface-2` (a status badge is an outlined chip on that tier) and **3.51:1** on a card's lit end, against a 4.5 floor. The tuned red holds **5.19:1** and **4.65:1** and keeps its hue. |
| `--accent-hover` | (a lighter step, as the family's other places take) | `#116B4C` | with a light label on the fill, a lighter hover took `--text-invert` from 4.79:1 to **3.96:1**. Deeper instead: **5.86:1**. |
| `--accent-soft` | 16% (library habit) | `rgba(20,122,87,.22)` | at 16% the accent badge tint was nearly invisible on the nested tier; 22% keeps `--accent-ink` at **5.81:1** there, so the chip gains presence without costing legibility. |

## Linter warnings kept deliberately

`python tools/build.py --only viridian-fields --no-export` is clean of errors and reports these,
all of which are kept:

- **`contrast-ratio: textColor (#5bcba0) on backgroundColor (#147a5738) has contrast ratio 2.66:1`**
  (three times: `badge-accent`, `button-secondary-hover`, `nav-item-active`). The linter grades the
  accent tint's **declared** rgba instead of compositing it — it is comparing pale ink against a
  22%-opaque emerald as if the emerald were opaque. Composited over what is actually behind it,
  `--accent-ink` measures **7.32:1** on a pane and **5.81:1** on the nested tier, and
  `tools/verify-lab.cjs` — which samples the real rendered pixels — passes the kit.
- **`orphaned-tokens`: `neutral`, `border-strong`, `bg-stop-1`, `bg-stop-2`, `bg-stop-3`, `fern`.**
  These document the ground ramp (`#16382B` scene field → `#0A1512` ground → `#050B08` floor), the
  accent hairline every control is rimmed with (`rgba(20,122,87,.60)`), and the engraved plate's
  stroke colour. The DESIGN.md component schema has no `borderColor` sub-token — the linter rejects
  it as a broken ref — so the rims are carried in tokens and prose rather than in the component map.
  Every one of these values is load-bearing in `tokens.css`; none is a leftover.
- **`token-summary`** is informational (22 colors, 7 type scales, 4 radii, 5 spacing, 26 components).

