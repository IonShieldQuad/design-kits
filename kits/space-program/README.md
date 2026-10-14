# Space Program

**Mission control — the room the mission is run from.** A near-white engineering drawing sheet with a
rimmed border and a module grid, white plates bolted onto it, one agency blue that acts, and a console
of drawn telemetry: a checklist, a block number and a status lamp cluster. Bright, technical,
paperwork-shaped — a program, not a sky.

- Kit: `space-program` · order `185` · mode **`light`** (white-dominant)
- Fonts: Big Shoulders Display · IBM Plex Sans · Overpass Mono
- Tags: `light` `mission-control` `engineering` `console` `telemetry` `checklist`
- Source: original

## Stance

A control room is not a night sky and it is not a weapons HUD. It is a bright room full of printed
forms, and the design language is **documentation**: an engineering drawing sheet, a checklist, a block
number, a lamp cluster, a plotted trace. This kit is the *program office* — the paperwork and the
consoles — and it deliberately contains nothing cosmic and nothing weaponised.

Three decisions carry the whole kit.

**The ground is white and the plates are whiter.** `--surface` is pure white, `--surface-2` is a pale
cool well, and `--bg` is a near-white drawing sheet with a rimmed border 14px in from the page edge, a
48px module grid and a fine 8px drafting grid. A bright kit has to be graded the *other* way round from
a dark one — the binding ground is the **darkest** one, not white — so every ink below is solved
against `--surface-2` and against the module-grid line, and the README table is worst-case, not best.

**One colour acts.** Agency blue acts; the signal ladder only reports. GO green, CAUTION amber and
ABORT red are *clarity colours* — each is the brightest value its hue can take and still carry a badge
label on the pale well, because the job is legibility, not decoration. The lamp **glass** in the drawn
motifs is the same hue one step brighter, which is how a real lamp works: bright glass, dark legend.

**Every control is an analog key.** Not a soft shadow and not a gradient — a hard, zero-blur cast
edge, and a press that **collapses that edge into an inset well** so the key visibly travels into the
panel. `--dur` is 80ms and `--ease` is `linear`: it clicks, it does not fade.

### Deliberately not its neighbours

This kit is the light, paperwork-side counterpart of `outer-space`, and the deliberate opposite of the
two kits closest to it in subject matter:

| | `outer-space` | `mecha-pilot` | `radioactive` | **`space-program`** |
|---|---|---|---|---|
| Mode / ground | dark starfield void | dark olive CRT board | light green-grey concrete | **light, near-white drawing sheet + module grid** |
| Register | the vista, the sky | the pilot's weapons HUD | the containment site | **the program office / console room** |
| One action colour | starlight gold | phosphor green | acid green | **agency blue** |
| Status ladder | aurora / amber / rose | green / amber / red (annunciator) | institutional lamps | **GO / CAUTION / ABORT, dark enough to be labels** |
| Signature devices | nebula blooms, starfield | reticle, range scale, caution tape | trefoil, hazard tape, spill | **checklist, block number, lamp cluster** |
| Depth | blurred glow + frosted glass | zero-blur offset | soft institutional drop shadow | **zero-blur cast edge, no glow, no blur at all** |
| Motion | eased, 240ms | 120ms | 180ms | **80ms, `linear` — a switch throws** |

No starfield, no nebula, no spacecraft silhouette, no reticle, no range tape and no caution stripes.
A cold viewer of this kit should say *"mission control"* and never *"space"*.

## Ground truth

| Token | Value | Note |
|---|---|---|
| `--bg` | rimmed border + 48px module grid + 8px drafting grid over two hard-stopped plates `#fbfcfe` / `#f2f6fb` | a **drawing sheet**, not a fade; every overlay only darkens |
| `--bg-2` | `#f2f6fb` | the second plate, solid — masthead/exports |
| `--surface` | `#ffffff` | the wall plate: cards are pure white |
| `--surface-2` | `#e9eef5` | the pale well — inputs, badges, code, tile base. **The darkest common ground: the binding one** |
| `--text` | `#0d1b2a` | 17.4:1 on white · 14.3:1 on the module-grid line |
| `--text-muted` | `#4a5768` | 6.31:1 on `--surface-2` |
| `--text-dim` | `#55627a` | 5.28:1 on `--surface-2` · **5.05:1** on the grid — captions, hints, legends |
| `--text-invert` | `#ffffff` | printed white ON the agency blue: 7.60:1 |
| `--accent` | `#12539f` | AGENCY BLUE — the one action colour |
| `--accent-hover` | `#0d3f80` | it goes deeper under load |
| `--accent-2` | `#2b6fc4` | the PLOTTER PEN — same family one step brighter. Charts, second series, the trace. Never an action |
| `--accent-soft` | `rgba(18,83,159,.15)` | derived: a 15% tint of `--accent` |
| `--accent-ink` | `#0e3f8f` | blue **as text**: 8.47:1 on the pale well, 6.74:1 on its own tint composited over it |
| `--ok` / `--warn` / `--danger` | `#10703a` / `#8f5404` / `#b81b12` | **GO / CAUTION / ABORT** — the brightest value each hue can take and still be a label |
| `--info` | `#17427e` | reference / telemetry blue |
| `--border` / `--border-strong` | `rgba(13,26,48,.16)` / `rgba(13,26,48,.34)` | a cast joint line / input rims |
| `--focus-ring` | `#0f4ba8` | 6.66:1 even on the module grid |
| `--radius-sm/md/lg` | `2px / 3px / 4px` | machined, not rounded and **not chamfered** (`carbon` owns the cut corner) |
| `--radius-pill` | `4px` | a badge is a stamped plate, not a lozenge |
| `--shadow-1` / `--shadow-2` | two hard bands, no blur | a plate standing 4px / 6px off the sheet |
| `--glow` | 6px of hard bands under the primary | the primary key's **machined edge**, not a halo |
| `--blur` | `none` | a control room is not frosted glass |
| `--dur` / `--ease` | `.08s` / `linear` | a switch throws |
| `--wash` | a flat 5% blue tint | no radial gradient anywhere in the kit |

## Derived, and why

- `--accent-soft: rgba(18,83,159,.15)` — a 15% tint of `--accent`, expressed as `rgba()` rather than
  re-typed as a hex so it can never drift from the blue.
- `--accent-ink: #0e3f8f` — the fill blue is right as a *fill* but wrong as an 11px legend; the ink is
  the same family darkened until it reads as text (8.47:1 on the well).
- `--text-invert` is `#ffffff`, printed on the blue: 7.60:1. Declared rather than assumed, because the
  label colour decides the pass/fail of every filled control.
- **`--accent` vs `--ok`** — the one real risk of a blue kit is that "go" and "do" blur together, so
  they are separated by *hue and role*: the action is a cool navy-blue plate with a white label, and
  GO is a green **lamp with a legend**. A blue plate can never be read as a green lamp, and no status
  colour is ever used as a control.
- **The lamp glass is not the token.** `--ok` is `#10703a` (a label colour); the *glass* in the drawn
  lamp cluster is `#16a34a`, the same hue one step brighter. That split is stated rather than blended:
  a token has to be legible as text, an object has to look lit.
- `--text-dim` is solved against the **module-grid line** (`#e1eaf4`) at 5.05:1, because captions and
  table headers sit directly on the sheet — grading it against white is how a caption ends up at 4.4:1
  on the one ground that matters.

## The three signature devices

Three motifs, three **different** jobs — the procedure, the identity, the state. All three are DRAWN
(base64 inline SVG) because a form built from blocks, ticks and lamp bezels cannot be expressed by a
gradient. Each carries its own hard-stopped base layer, so no tile ever shows the kit's flat surface.

- `--space-program-checklist` — **the procedure.** A blocky flight-checklist strip: a filled header
  bar, three ruled columns, three **ticked** square boxes and one open box, with value leaders struck
  down the right and the pending row dimmed. A repeating gradient makes an even rule pattern; it
  cannot make a tick inside a box.
- `--space-program-blocknumber` — **the identity.** A drawing title block: a heavy frame, a hatched
  revision cell, a dark binding edge and a stencil numeral (`04`) drawn as exact geometry — an
  octagonal zero with diagonal stencil breaks and a `4` with a broken stem — plus a legend rule
  beneath. (The first cut punched the breaks into the *top and bottom* strokes, and a cold viewer read
  the zero as a square bracket; the breaks sit on the two diagonals instead.)
- `--space-program-lamps` — **the state.** A console lamp cluster: four square lamps in dark bezels
  with a bright glass, a hard specular band and a leader rule, seated in a milled channel, legend
  printed in mono — GO · CAUTION · ABORT · OFF.

The plotted trace and the numbered graduation are deliberately **not** a fourth tile: they live on the
card media panel (`--media-bg`), which is a plotter output — a drafting grid, a two-pen trace, a
graduation tape with block numerals and a title block. (The first cut of that panel had a dark header
strip with three coloured squares in it, and a cold viewer read the whole thing as a macOS application
window with traffic-light controls; the strip is now a graduation tape and the lamps are gone.)

**Non-flatness, measured.** Each token was rendered as `background:` on a 168×72 tile over
`--surface-2` in real headless Chromium, screenshotted at 2×, and its per-tile luma standard deviation
taken with PIL. A flat plate scores ≈0.

| Tile | std-dev (luma) | luma range | job |
|---|---|---|---|
| `--space-program-checklist` | **69.19** | 36.9 – 255.0 | the procedure |
| `--space-program-blocknumber` | **91.85** | 25.1 – 251.9 | the identity |
| `--space-program-lamps` | **79.64** | 25.1 – 255.0 | the state |

All three were also **looked at cold** by a model that had not seen the intent: it read them as "a
checklist/card with checkboxes", "a numbered label / sign", and "an indicator lamp panel with GO, CAUT,
ABRT, OFF" — and read the numeral as `04`. Each one was checked again after every fix.

## Analog controls

The press is the point. A control **rests** on a cast edge and **collapses** into an inset well:

```css
--btn-shadow:        0 2px 0 0 var(--space-program-plate-deep), 0 4px 0 0 rgba(13,26,48,.22),
                     inset 0 1px 0 rgba(255,255,255,.95);   /* a 4px-thick key */
--btn-shadow-active: inset 0 3px 0 0 rgba(13,26,48,.34), inset 0 4px 0 0 rgba(13,26,48,.12),
                     0 1px 0 0 rgba(13,26,48,.12);          /* the key travels in */
--glow:              0 2px 0 0 #0a3a75, 0 4px 0 0 #08315f, 0 6px 0 0 rgba(13,26,48,.24);
```

`--btn-shadow-active` reaches **every** variant (including the primary, whose resting state is
`--glow`), so the whole control layer is one physical object. The same logic runs through the rest of
the hardware:

| | device | how |
|---|---|---|
| fields | **milled**, not laid on | `--input-inset: inset 0 2px 0 0 rgba(13,26,48,.34), inset 0 -2px 0 0 #ffffff` |
| nav + tabs | a **raised rail** | `--bar-shadow: 0 2px 0 0 plate-deep, 0 4px 0 0 rgba(…)`, current item = a key on it (`--bar-item-shadow`, `--bar-item-pad`) |
| switch | a seated track + a machined knob | `--toggle-shadow` (3px dark groove top, 3px light lip bottom), `--toggle-knob-shadow` (a 1.5px rim + a 2px cast) |
| checkbox | a **checklist box** | `--check-appearance: none`, `--check-radius: 0px`, 2px ruled box, filled when checked |
| progress / avatar | a **segmented console channel** | `--fill-bg`, hard-stopped, both segments dark enough for the white label |

Measured on the real rendered pixels (not asserted): the field's top edge steps **border `rgb(198,204,214)`
→ groove `rgb(158,166,177)` → fill `rgb(233,238,245)`**, and the switch's track steps **blue
`rgb(18,83,159)` → groove `rgb(16,58,109)`** with a light lip at the bottom.

## Nothing smooth — all five doors shut

1. **Curves** — no radius above 4px, and the native control is squared with `--check-radius: 0px`.
2. **Soft shadows** — every shadow in the kit is zero-blur; the "glow" is six pixels of hard bands.
3. **Gradients** — every gradient is hard-stopped (shared positions), including `--bg`, `--fill-bg` and
   each motif's base layer. There is **no radial gradient in the file at all**, and `--wash` is a flat
   tint rather than the masthead's default radial bloom.
4. **Scaled artwork** — every motif is vector, drawn at the size it displays; nothing is upscaled.
5. **Blur** — `--blur: none`, and no rule adds a `backdrop-filter`.

## Contrast (measured, not eyeballed)

Computed from the declared tokens by a scratch script that parses `tokens.css` with the repo's own
parser, then confirmed against the real rendered pixels by `tools/verify-lab.cjs`. Graded against the
ground each ink actually sits on, composites included.

| Ink | `--surface` | `--surface-2` | plate A | plate B | module grid | masthead wash |
|---|---|---|---|---|---|---|
| `--text` | 17.39 | 14.92 | 16.94 | 16.03 | 14.30 | 15.69 |
| `--text-muted` | 7.36 | 6.31 | 7.17 | 6.78 | 6.05 | 6.64 |
| `--text-dim` | 6.15 | 5.28 | 5.99 | 5.67 | **5.05** | 5.55 |
| `--accent-ink` | 9.88 | 8.47 | 9.62 | 9.10 | 8.12 | 8.91 |
| `--ok` | 6.18 | 5.30 | 6.02 | 5.69 | 5.07 | 5.57 |
| `--warn` | 6.11 | 5.24 | 5.95 | 5.63 | 5.02 | 5.51 |
| `--danger` | 6.56 | 5.62 | 6.39 | 6.04 | 5.39 | 5.91 |
| `--info` | 9.92 | 8.51 | 9.66 | 9.14 | 8.15 | 8.95 |
| `--focus-ring` | 8.10 | 6.95 | 7.89 | 7.47 | 6.66 | 7.31 |

Other required pairs: `--accent-ink` on its own 15% `--accent-soft` **composited** over each ground —
7.77 / 6.74 / 7.58 / 7.20 / 6.48 / 7.06:1 (the badge case; needs 4.5). `--text-invert` on `--accent`
**7.60:1**, on `--accent-hover` **10.30:1**, on the darker segment of the segmented channel
**11.20:1**. `--focus-ring` on the grid **6.66:1** (needs 3).

**Worst pair: `--text-dim` `#55627a` on the module-grid line `#e1eaf4` = 5.05:1** — a caption sitting
directly on the sheet, needing 4.55. The tightest *status* pair is `--warn` `#8f5404` on `--surface-2`
at **5.24:1** (needs 4.5). The tightest *accent* pair is `--accent-ink` on its own tint at 6.48:1.

**One declared non-type ground, stated rather than hidden.** The sheet's rimmed border is a 1px rule at
34% blue, 14px in from the page edge; `--text-dim` would measure **3.24:1** on it. It carries no type
*by construction* — the content column is `min(1040px, 100% - 2.5rem)`, so nothing can come closer than
20px to the viewport edge and the border sits in the margin. Everything the verifier samples is inside
the column, and `verify-lab.cjs` passes with the real pixel back-sampling.

## Trade-offs

- **A near-white kit has no place to hide.** Every joint is visible, so all of the identity has to be
  carried by geometry — the grid, the cast edges, the drawn objects. It is a poor fit for moody or
  cinematic work; that is `outer-space`.
- **The checkbox has no tick glyph.** Native controls ignore `border-radius` but cannot be given a tick
  mark by token, so the checked state is a **filled square** and the unchecked state a ruled box. In
  the paper-checklist idiom a filled box reads as "done"; a project that needs a literal ✓ must supply
  its own asset.
- **`--radius-pill: 4px` is a compromise.** The token drives both the badge shape and the switch
  thumb/knob. The first cut (2px) produced a thumb identical to the checkbox square and a cold viewer
  read the switch as "a checkbox dropped in a bar"; 4px separates them without unsquaring the badges.
  Badges are therefore rounded stamped plates rather than hard rectangles.
- **The switch is square-ish on purpose.** A 4px-cornered thumb in a 4px-cornered track is a machined
  slide switch, not an iOS pill. If you want a pill switch, this is the wrong kit.
- **The press is expressed only through the shadow.** `templates/lab.css` hard-codes
  `.btn:hover { transform: translateY(-1px) }` and offers no token for the active transform, so a
  pressed key is still lifted 1px while its cast edge collapses. The travel still reads (the edge is
  4px at rest and 1px pressed, measured), but a `--btn-hover-lift` / active-transform hook would let an
  analog kit seat the press completely. A capability the lab lacks, reported rather than worked around.
- **Big Shoulders Display is display-only.** It is a tall condensed signage face; below ~18px it is
  decoration rather than text, so body copy is IBM Plex Sans and every small legend is Overpass Mono.
  The section headings (16.8px) are the smallest place the display face appears.
- **The lamp glass colours are artwork, not tokens.** `#16a34a` / `#e08a0c` / `#d02014` live inside the
  drawn SVG; the tokens ship the dark, legible versions of the same hues.

## When to use

Program documentation and control-room surfaces: mission/ops consoles, telemetry and monitoring
dashboards, checklists and procedure UIs, safety and engineering tooling, printed-form products, any
interface that should read as a bright room with a status ladder rather than a vista. It is the light
counterpart of `outer-space` and the paperwork counterpart of `mecha-pilot`. Avoid it for night-mode
consoles, editorial calm, or anything that needs to feel cosmic rather than engineered.

## Files

`DESIGN.md` (normative values) · `tokens.css` (the contract) · `kit.json` (gallery metadata) ·
`README.md` (this file) · `index.html`, `DESIGN.html`, `tokens.json`, `tailwind.theme.json`, `theme.css`
(generated by `python tools/build.py --only space-program`). No `kit.css`: every construction in the
lab — including the pressed key, the milled field, the rail and the switch — is reached through tokens.
`designmd lint`: **0 errors, 0 warnings** (1 info: the token summary).
