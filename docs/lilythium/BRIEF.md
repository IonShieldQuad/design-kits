# Authoring brief — the LIL//OS desk family (six kits)

This is the shared contract for six kits being ported into this library from the user's
**bespoke-desktop** project (`H:\Work\bespoke-desktop`, prototype `prototypes/v9-lilythium`).
It supplements `docs/KIT-SPEC.md` — read that first; it is normative for file shape, the token
list, DESIGN.md rules and the quality bar. This file adds only what is specific to this family.

## What the family is

One desktop OS — `Li//OS` — whose places are fifteen variants of a single instrument-panel
grammar: a hairline frame, an opaque face carrying a sheen band, a bottom occlusion band, a
157° face fall, a 5% accent tint and one drawn texture at 5–9%; one accent hue per place; and one
signature motif. Six places passed as good; four are still being reworked and are **out of scope**.

| place | kit name | slug | order | accent | face | ground | shape | motif |
|---|---|---|---|---|---|---|---|---|
| 01 | Azure Technologies | `azure-technologies` | 205 | `#4FD8FF` | `#0A0F16` | `#05080D` | chamfer 16 | hex lattice |
| 02 | Mainframe Access | `mainframe-access` | 210 | `#54E08A` | `#04100A` | `#020704` | square | scanlines |
| 05 | Pastel District | `pastel-district` | 215 | `#FF8FC4` | `#23141D` | `#160C13` | round 6 | bokeh |
| 06 | Crimson Labyrinth | `crimson-labyrinth` | 220 | `#FF4D5E` | `#140A0C` | `#090305` | chamfer 16 | engraved rose |
| 07 | Sunset Boulevard | `sunset-boulevard` | 225 | `#B06CFF` | `#150C28` | `#0A0512` | chamfer 16 | perspective grid |
| 08 | Viridian Fields | `viridian-fields` | 230 | `#147A57` | `#0C1410` | `#0A1512` | round 5 | engraved fern |

The kit name **is** the place name from the desk's world chart — do not rename, decorate or
reinterpret it (no "Azure Technologies · Cold Cyber" or similar). The tagline explains the
render; the name is the place.

## The reuse rule

**Never invent a colour, a texture or a construction.** Everything comes from the place file
(`place-XX.css`) or from this brief:

- `--acc`, `--acc2`, `--accHi`, `--face`, `--ground`, `--panel`, `--sceneA`, `--sceneB`, `--glow`,
  `--tx`, `--txA`, `--cp`, `--rad` are the place's own values. Copy them.
- The **textures are already extracted and alpha-baked** in `docs/lilythium/textures.css`: each
  place has `--<slug>-tex` (the card, at the desk's own pitch and its own `--txA`) and
  `--<slug>-tex-ground` (the same motif at half the alpha, twice the pitch). Paste your two lines
  verbatim**. Do not redraw, re-encode, re-time or re-alpha anything — the desk applied `--txA`
  as a pseudo-element `opacity`, which a background layer cannot do, and the folding is already
  done and verified at gallery-tile size.

  **The stylesheet is not the truth — the running page is.** The built page carries a *legacy*
  motif per place and swaps it when its scripts run, so anything read out of the CSS text is the
  pre-script state. Measured differences, all of them real: place 01's legacy texture is a 72px
  hexagon grid with a spoke from each centre to its corners (it reads as a triangle grid) and the
  runtime value is a **36 x 20.7846 closed honeycomb at .09**; place 02's card texture is switched
  **off** (`::after` opacity 0) and its card is a black plate with a green hairline and a green
  outer glow; place 06's rose is applied at **.13**, not .085; place 07's grid at **.09**, not .06.

  Hence: `docs/lilythium/textures.css` and `docs/lilythium/runtime-<place>.json` are the only
  sources for motif, accent, ink ramp, hairline and card face. They were produced with
  `getComputedStyle()` on the settled page, not by parsing the CSS. The per-place JSON also records
  the rendered card colour and the card's own `drop-shadow`, which is the desk's only depth.
- The **panel construction is the desk's own `.card-in`**, ported below into token form. It is
  the family's identity; every one of the six uses it unchanged.
- Do not add a `kit.css`. Everything this family needs is reachable from tokens.

## The material, in token form

Paste this block into each `tokens.css` and substitute the bracketed parts. Layer order is
top-first and **is the light model**: sheen over occlusion over texture over tint over fall over
the face. A texture placed under the tint is invisible; a fall placed under the face is not a fall.

```css
/* THE CARD MATERIAL — the desk's own .card-in, ported.
   sheen (with its 1px specular lip) > occlusion > texture > identity edge > tint > fall > face */
--<slug>-pane:
  linear-gradient(180deg, rgba(255,255,255,.30) 0 1px,
                          rgba(255,255,255,.17) 1px,
                          rgba(255,255,255,.048) 34%,
                          rgba(255,255,255,0) 100%) 0 0/100% 9% no-repeat,
  linear-gradient(0deg,   rgba(0,0,0,.46) 0,
                          rgba(0,0,0,.138) 38%,
                          rgba(0,0,0,0) 100%) 0 100%/100% 9% no-repeat,
  var(--<slug>-tex) [pitch/placement],                 /* the place's drawn motif          */
  linear-gradient(90deg, transparent 0%,
                          rgba(<accRgb>,.55) 7%,
                          rgba(<accRgb>,.55) 62%,
                          transparent 96%) 0 100%/100% 1px no-repeat,   /* the identity edge */
  linear-gradient(rgba(<accRgb>,.05), rgba(<accRgb>,.05)),             /* the 5% tint       */
  linear-gradient(157deg, rgba(255,255,255,.12) 0%,
                          rgba(255,255,255,0) 44%,
                          rgba(0,0,0,.24) 78%,
                          rgba(0,0,0,.52) 100%),                       /* the face fall      */
  <face>;
--surface: var(--<slug>-pane);
```

`--surface-2` is the *nested* tier worn by inputs, badges, alerts, code blocks and
`card-elevated`. It drops the texture and the identity edge — a 4px scanline or a 268px engraving
on a 2.5rem control is clutter, not material — and keeps a shallow sheen plus half the tint:

```css
--surface-2:
  linear-gradient(180deg, rgba(255,255,255,.06), rgba(255,255,255,0) 60%),
  linear-gradient(rgba(<accRgb>,.04), rgba(<accRgb>,.04)),
  <panel>;                       /* the place's own --panel, one step up from --face */
```

Because every surface is opaque, `--blur: none` — the desk forbids glass and `backdrop-filter`,
and a blurred opaque card is only a repaint cost.

## The card material is per place, not per family

I first wrote that all six share one stack. They share the **construction order**, but each place
supplies its own numbers, and two places replace the stack outright. Measured with
`getComputedStyle()` on `.card-in` + `.card`:

| place | shape | identity edge | card stack |
|---|---|---|---|
| 01 azure | `--clip` 16px, TL+BR; radius 0 | accent, 7%–62%–96%, op .55 | sheen `.17/.047@34%/0` @ `100% 9%`; occlusion `.46/.137@38%/0`; fall `157deg .12/0/.24/.52`; face `#0A0F16` |
| 02 mainframe | none; radius 0 | accent solid, op .75 | **replaced**: sheen `rgba(210,255,222,.09)→0` @ `100% 30px`; `rgba(92,247,155,.05)→rgba(0,0,0,.34)`; **green scanline `rgba(92,255,140,.055)` 1px/3px**; face `#000` |
| 05 pastel | none; radius 6 | accent, 7%–62%–96%, op .55 | standard, face `rgb(35,20,29)` |
| 06 crimson | **octagon**: all four corners 12px, 8 points; radius 0 | deep crimson `rgb(142,31,43)`→`rgb(192,48,63)`, faded both ends, op .9 | sheen `.08/.024@34%/0`; occlusion `.48/.145@38%/0`; fall `157deg .05/0/.20/.50`; face `rgb(16,6,8)` |
| 07 sunset | `--clip` 18px, TL+BR; radius 0 | **neon ramp** `rgb(255,106,213)→rgb(161,92,255)→rgb(58,201,255)`, op 1 | **replaced**: top wash `.12→0` @24%; pink bloom `radial 120% 64% at 50% 116%` `.34`; dark ramp `rgb(13,7,34)→rgb(7,3,18,.80)`; face `rgb(13,7,34)` |
| 08 viridian | none; radius 5 | accent, 7%–62%–96%, op .55 | standard, face `rgb(12,20,16)` |

The two in-card accent radials (identity glow at `0% 100%`, crown at `50% -10%`) are present in the
markup for every place and sit at **0 alpha** in all six: the desk switches them off, so do not
"restore" them. Depth is the card's own `drop-shadow`, and it is per place too (06 is
`0 7px 18px rgba(0,0,0,.66)`, 07 is a magenta `0 0 10px rgba(255,90,200,.32)` plus a dark
`0 7px 14px`, the rest are `0 6px 16px rgba(0,0,0,.50)`).

## The ground

The desk's `.scene`: the place's ground, two soft fields of `--sceneA`, a faint technical grid,
and `--sceneB` at the floor. **Sizes in percentages, never pixels** — the gallery renders `--bg`
into a ~118px tile and a px-anchored scene shows the tile its top edge only.

```css
--bg:
  radial-gradient(80% 60% at 63% 38%, var(--<slug>-scene-a) 0%, transparent 62%),
  radial-gradient(120% 70% at 14% 96%, var(--<slug>-scene-a) 0%, transparent 72%),
  repeating-linear-gradient(90deg, rgba(255,255,255,.028) 0 1px, transparent 1px 120px),
  repeating-linear-gradient(0deg,  rgba(255,255,255,.024) 0 1px, transparent 1px 120px),
  var(--<slug>-tex-ground),
  linear-gradient(180deg, <ground> 0%, <sceneB> 100%);
```

Two scales, deliberately different jobs: the ground is large-celled and quiet (the motif at 55%
of the card's alpha over a 120px technical grid — twice the pitch for the tiling motifs, one
larger plate for the engravings), the components' material at the desk's own pitch and drawn
stronger. Equal weight makes the page one busy field and every card
reads as texture inside texture. Verified at 360×118 — the size the gallery actually renders —
so do not re-tune the alphas upward "until it shows".

## The rest of the contract

| desk token | contract token | note |
|---|---|---|
| `--acc` | `--accent` | the action colour, exactly as given |
| `--accHi` | `--accent-ink` | the desk already solved "accent as text" — this is that value. Also `--accent-ink-hover` one step lighter |
| `--acc2` | — | the pale member of the accent family; useful for `--accent-ink-hover` or a gradient stop, never as a second accent |
| second hue | `--accent-2` | the place's **own** second hue from its scene, not a new one (07's amber sun, 01's violet, 05's mint, 06's brass, 02's amber, 08's pale sky) |
| `--ink/--ink2/--ink3` (desk root) | `--text/--text-muted/--text-dim` | grade them against the composited pane; see the quality bar |
| `--face` | `--surface` face stop | |
| `--panel` | `--surface-2` face stop, `--bg-2` | |
| `--ground` | `--bg` floor | |
| `--sceneA/--sceneB` | the two field stops / the floor | |
| `--glow` | `--glow` | the desk's own `box-shadow` glow, `0 0 14px <its rgba>` |
| `--accLine` | `--border-strong` | the accent hairline |
| white 14% | `--border` | the desk's frame hairline; hover takes it to 35% |
| `--cp` | `--clip` + `--cut` | chamfered places only; **all three use cut 16**. `--frame-ring` is derived by `build.py` — do not author it |
| `--rad` | `--radius-sm/md/lg` | `0px` for the three chamfered places |

Additional required values, all of them the desk's:

- `--border-w: 1px` (the hairline is not negotiable in this family)
- `--dur: .18s`, `--ease: linear` — the desk transitions border-colour and tint linearly; nothing
  in this family eases
- `--shadow-1: 0 6px 16px rgba(0,0,0,.50)`, `--shadow-2: 0 10px 26px rgba(0,0,0,.55)`
  (the desk's `filter: drop-shadow(0 6px 16px rgba(0,0,0,.50))` and its well shadow)
- `--focus-inset: 2px` for the three chamfered kits — `clip-path` eats `outline`, so the ring is
  painted inside the silhouette. The three round/square kits omit it.
- `--check-radius`: chamfered/square places square their native checkboxes (`0px` or `2px`)
- `--fill-bg`: progress and avatar — a two-stop ramp from the accent's 25% tint to `--accent`
- `--media-bg` + `--media-op: 1`: a "place plate" — the scene bloom and the texture at card pitch
  on the face, not the default accent ramp

## The holo pane — the family's projected surface

The desk has two kinds of surface and the port needs both. A **card** is built out of the desk
(opaque face, hairline, sheen, occlusion, motif). A **pane** is projected onto it: no face, no
border, no shadow, just a 13% veil of the place's own hue, one accent bloom at its crown, CRT
scanlines, and four 24px corner marks. That construction is the desk's `.pane-holo`
(`experiments/panels-v3/index.html`, lines 153-183) and it is the family's signature; a family
without it is just six tinted plate skins.

Express it as one token and wire it to the lab's media panel:

```css
--<slug>-holo:
  /* four corner marks, two 1px hairlines each (the desk's .brk, at 24px) */
  linear-gradient(rgba(<accRgb>,.70),rgba(<accRgb>,.70)) left  top/24px 1px no-repeat,
  linear-gradient(rgba(<accRgb>,.70),rgba(<accRgb>,.70)) left  top/1px 24px no-repeat,
  linear-gradient(rgba(<accRgb>,.70),rgba(<accRgb>,.70)) right top/24px 1px no-repeat,
  linear-gradient(rgba(<accRgb>,.70),rgba(<accRgb>,.70)) right top/1px 24px no-repeat,
  linear-gradient(rgba(<accRgb>,.70),rgba(<accRgb>,.70)) left  bottom/24px 1px no-repeat,
  linear-gradient(rgba(<accRgb>,.70),rgba(<accRgb>,.70)) left  bottom/1px 24px no-repeat,
  linear-gradient(rgba(<accRgb>,.70),rgba(<accRgb>,.70)) right bottom/24px 1px no-repeat,
  linear-gradient(rgba(<accRgb>,.70),rgba(<accRgb>,.70)) right bottom/1px 24px no-repeat,
  /* the desk's .scan: 1px rows at a 3px pitch, 5% white, held at 60% */
  repeating-linear-gradient(0deg, rgba(255,255,255,.03) 0 1px, transparent 1px 3px),
  /* the crown bloom (the desk's second radial, .055) */
  radial-gradient(120% 78% at 50% 0%, rgba(<accRgb>,.055) 0%, rgba(<accRgb>,0) 62%),
  /* THE VEIL, as it behaves here: the desk lays 13% of the place's hue over the
     scene; the lab's media panel sits on an opaque card, so the same 13% is a
     film of black. Say that in the README — it is the one re-expression. */
  linear-gradient(rgba(0,0,0,.13), rgba(0,0,0,.13));

--media-bg: var(--<slug>-holo);
--media-op: 1;
```

Also add `--<slug>-holo` to `kit.json`'s `signature` list so the lab renders it at 168x72: it is
the token that tells you whether this kit is a desk skin or a coloured rectangle.

**What cannot be a token:** the desk animates a 180px accent band down the pane every 9s
(`@keyframes sweep`, with a `prefers-reduced-motion` guard). The lab has no element to put it on,
so the family ships the construction and not the motion. State that as a limitation in the README
rather than hiding it.

## Type — the family's own pairing, shared by all six

The desk ships exactly two faces and we keep both, unchanged:

```css
--font-display: "Chakra Petch", "Segoe UI", system-ui, sans-serif;
--font-body:    "Chakra Petch", "Segoe UI", system-ui, sans-serif;
--font-mono:    "JetBrains Mono", "Cascadia Mono", Consolas, monospace;
--tracking-caps: .14em;
--tracking-display: .004em;
```

`fonts_url` (identical in all six `kit.json`):
`https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap`
and `fonts_label`: `Chakra Petch · JetBrains Mono`.

Sharing the pair is deliberate: these six are places in one OS, and the type is the OS. Say so in
the README so a later session does not "fix" it.

## Status ladder

The desk has one alert red and no ladder, so each kit derives its four status colours from its
own place — and **the accent must stay distinguishable from `--ok` / `--danger`**, which is where
this family is easiest to get wrong:

- `mainframe-access` is monochrome by design: its ladder is `--ok` = `--accHi` (the pale phosphor),
  `--warn` amber, `--danger` red, `--info` pale blue. The action stays separable by *material* —
  an opaque accent plate against outlined chips — not by hue.
- `crimson-labyrinth` inverts the usual convention: crimson is the **action**, so `--danger` moves
  to a hot orange and `--warn` to brass. State this in the README; a red-danger beside a red
  action makes every button read as an error.
- The others take mint/amber/red/violet from their own scene. Starting values are in each place
  task; tune them until `scripts/contrast-audit.py` is clean.

## kit.json

```json
{
  "name": "<the place name>",
  "tagline": "<what the render is, one sentence, no hype>",
  "use_when": "<where a stranger should reach for this kit>",
  "signature": ["--<slug>-field", "--<slug>-pane", "--<slug>-tex"],
  "order": <from the table>,
  "fonts_url": "<the family URL above>",
  "fonts_label": "Chakra Petch · JetBrains Mono",
  "mode": "dark",
  "source": "derived from the user's bespoke-desktop Li//OS prototype (prototypes/v9-lilythium, place NN) — palette, panel construction and drawn motif taken from the prototype's own tokens",
  "tags": ["dark", "..."]
}
```

Do not write an `index` field — it is derived from `order`.

## README — what it must contain

1. **Stance**: one paragraph, what the render is and what it is for.
2. **Lineage**: the family table (all six, this one marked), and the axis that distinguishes
   *this* place from its five siblings. Two kits from one reference are the library's standing
   hazard; a sibling that cannot say what makes it different is a duplicate.
3. **What the material is**, with the layer order and why that order.
4. **The motif**, with the pitch it is drawn at on the card and on the ground (numbers).
5. **Key choices** and **trade-offs** (the accent/status collision if any; why `--blur: none`;
   what the shared type pairing buys and costs).
6. **When to use** — and, honestly, which sibling to use instead when it is close.
7. **Linter warnings kept deliberately**, if any, with the composited number that justifies it.

## Checks — run these, in this order, before reporting

```bash
cd H:/Work/design-kits
python tools/build.py --only <slug> --no-export          # lab + DESIGN.html + lint
python scripts/contrast-audit.py kits/<slug>             # every pair against every ground
node tools/verify-lab.cjs <slug>                         # computed styles in real Chromium
```

`--only` is safe to run in parallel (it skips the shared gallery, manifest and picker).
The aggregate build, the exports and the commit are run once by the coordinator — **do not run
`git`, do not run `build.py` without `--only`, do not edit any file outside `kits/<slug>/`**.

Report back: the three check results verbatim for the last line of each, the contrast numbers you
had to change a value to reach, and anything a reviewer would call a judgement call.
