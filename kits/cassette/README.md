# Cassette

**The front panel of a 1970s receiver. Warm beige plastic, brushed aluminium trim, chunky controls
pressed into the shell — and exactly one amber LED doing all the acting.**

`110` · light · `Overpass · Overpass Mono` · source: original

## Stance

A theme built from a physical object, not a screen. The ground is warm beige **plastic** —
#e2d8bf at the top lip settling to #d3c6a6 in the lower case — with a moulded sheen across it,
brushed aluminium for the trim, and controls big enough to feel like they have travel. "Chunky" is
a real specification: `--border-w: 2px` moulded seams, 4–12px radii plus a full pill, 40px controls,
12×20px button padding, 20px card padding.

**One thing on this panel lights up.** The amber/orange LED (`--accent` = `#e86f0a`) fills the
primary button, the checked toggle, the progress bar and the media plate, and nothing else. It is a
lamp behind a beige bezel, so it is a *fill*: as small lettering on beige it measures **1.85:1**.
Accent-as-text is therefore a separate, much darker burnt orange (`--accent-ink` = `#7a3600`,
5.26:1 on the shell). That is the single most important decision in the kit — a receiver solves the
same problem the same way, by glowing behind a bezel and *printing* its labels in dark ink.

**The ink is warm brown, never grey.** Panel lettering is warm dark brown (#2b2115); a neutral grey
would read as a different material. The ink is deliberately not lightened to keep the page "soft" —
see the contrast table; a beige ground eats contrast fast.

**Depth runs inwards.** Every surface is pressed into the shell: `--shadow-1`/`--shadow-2` are
*inset* stacks (lit top lip, shadowed bottom lip, short falloff into the well) and there is no soft
outer drop shadow anywhere in the kit. `card-elevated` is *more* pressed in, not more lifted.

Use it for hardware, audio, device/firmware and retro-product pages — anything whose subject is an
object rather than a web app.

### Recognisable at 200×120

1. **A mid-tone beige plastic ground.** `#e2d8bf → #d3c6a6` is far darker and warmer than the paper
   grounds of this set (`geometric-dimensions` is bone `#f4f1ea`, `glorious-morning` is #eaf5ff
   sky); it is the one kit that starts from *moulded plastic*.
2. **Amber/orange as the only saturated thing.** One lamp, and it is the primary button.
3. **Inset everything.** 2px moulded seams, lit lips, shadowed bottoms — no element floats.
4. **A chunky moulded silhouette.** 8px buttons, 12px cards, full-pill badges, 40px controls.

None of those four are `geometric-dimensions` (light, paper, zero-radius, *hard offset* shadows) or
`inside-the-machine` (dark, graphite, mono-first, milled 1px hairlines).

## Palette, with roles

| Token | Value | Role |
|---|---|---|
| `--bg` | gradient `#e2d8bf 0px → #dcd1b6 340px → #d3c6a6 900px` | the beige plastic shell (px stops — see below) |
| `--bg-2` | `#dcd1b6` | solid stand-in for exports / masthead |
| `--surface` | `#e9e0c9` | cards — the sub-panel face, a shade *lighter* than the shell |
| `--surface-2` | `#cabc9b` | inputs, badges, code — the inset bay, the same plastic pressed *deeper* |
| `--overlay` | `rgba(38,27,14,.58)` | modal scrim (warm shadow, not black) |
| `--text` | `#2b2115` | the warm brown panel ink |
| `--text-muted` | `#514327` | secondary text |
| `--text-dim` | `#5a4a2d` | captions, hints, table headers |
| `--text-invert` | `#241708` | panel ink printed ON the amber plate |
| `--accent` | `#e86f0a` | **THE LED.** The one action colour — fill only |
| `--accent-hover` | `#fb8118` | the lamp turned **up** (see below) |
| `--accent-2` | `#2f8e85` | meter teal — the one cool note: media, chart series, the bar's second stop |
| `--accent-soft` | `rgba(232,111,10,.15)` | 15% amber tint, derived — nav/tab fills, inline code |
| `--accent-ink` | `#7a3600` | amber **as text** — the burnt orange (5.26:1 on the shell) |
| `--accent-ink-hover` | `#632900` | the hover step for accent text |
| `--ok` | `#18522a` | moulded green lamp |
| `--warn` | `#624502` | dark ochre, held far below the amber in value |
| `--danger` | `#8b1e0e` | record / tally red |
| `--info` | `#274669` | petrol blue — data and telemetry |
| `--border` / `--border-strong` | `#b6a684` / `#8f7f5f` | the moulded seams (opaque warm brown) |
| `--border-w` | `2px` | a panel edge is a moulded step, not a hairline |
| `--focus-ring` | `#9c4505` | deep orange — focus must not look like the bright hover lamp |
| `--radius-sm/md/lg` | `4px` / `8px` / `12px` | moulded, generous |
| `--radius-pill` | `999px` | a hardware tag / a toggle end |
| `--cut` | `0px` | moulded, not chamfered |
| `--shadow-1` | `inset 0 1px 0 rgba(255,252,240,.55), inset 0 -2px 0 rgba(94,74,44,.20), inset 0 3px 8px -4px rgba(72,55,30,.42)` | the recess |
| `--shadow-2` | `inset 0 1px 0 rgba(255,252,240,.62), inset 0 -2px 0 rgba(94,74,44,.24), inset 0 5px 14px -6px rgba(72,55,30,.55)` | the deeper bay |
| `--glow` | `0 0 0 1px rgba(140,60,0,.30), 0 4px 14px -3px rgba(232,111,10,.55), inset 0 1px 0 rgba(255,226,170,.65), inset 0 -2px 0 rgba(120,50,0,.30)` | the amber lamp's halo — energised controls only |
| `--blur` | `none` | moulded plastic is not frosted |

## Which colour drives action

**Amber (`--accent`, #e86f0a) — and only amber.** It fills the primary button, the checked toggle,
the progress bar and the media plate. Because it is a *lamp*, the accent-as-text pair
(`--accent-ink` / `--accent-ink-hover`) carries every label, link, active tab and inline code in a
much darker burnt orange of the same family.

- **Meter teal (`--accent-2`, #2f8e85)** is the second accent and the kit's one cool note — the
  tint of a lit tuning dial. It appears in media plates, chart series and the bar's second gradient
  stop. It is never a control: a second saturated action colour would mean two lamps on a panel
  that has one.
- **Status colours stay off the amber by value and hue.** Green (#18522a), dark ochre (#624502),
  record red (#8b1e0e) and petrol (#274669) all sit far below the LED in lightness, so a "draft"
  chip never reads as the button next to it. `--warn` is the interesting one: it is a genuine
  caution ink, not a dimmed copy of the accent, because a caution must not look like a lamp.
- **Why hover brightens.** On a light kit the reflex is to darken on hover, but darkening the LED
  drops its own label to **4.1:1** — below AA, on the state you are most likely to be looking at.
  Brightening to `#fb8118` raises it to **6.87:1** and is the physically honest move: a lamp coming
  up, not a lamp changing colour.

## What drives the numbers

- **`--bg` uses PX stops, not %.** The body's gradient box is the whole document; a % ramp would
  smear three stops over thousands of pixels and the first screen would show one flat plate. The px
  stops land the whole shell — bright top lip, settling into the warmer lower case — inside the
  first screen. **Contrast is checked against the darkest stop, `#d3c6a6`**, not against the
  comfortable one. Every ground-relative ratio in the table is computed against it.
- **`--accent-soft` is derived**, not invented: a 15% tint of `--accent`, written as `rgba()`
  rather than re-typed as a hex, so it cannot drift from the amber.
- **The two line colours are opaque warm browns**, not translucent white. The seam between two
  moulded parts is a *darker shade of the same plastic*, and an opaque seam is what holds at 2px.
- **Inset lip alphas sit above the "barely there" 5% range.** At 5% a 1px highlight does not
  survive a normal-density display, and on a mid-tone beige the falloff term is what sells the
  recess.
- **No `--clip`, no `--text-on-surface*`.** Neither optional capability is earned here: this kit
  never inverts its surfaces (the inset is a darker shade of the same beige, not a dark well), so a
  single warm ink is legible on all three grounds — proven below — and a chamfer would cut the 2px
  moulded rim that is half the kit's silhouette. `--accent-ink` / `--accent-ink-hover` *are* declared,
  because amber-as-text is the one capability this palette cannot do without.
- **`--shadow-1`/`--shadow-2` are inset**, and `--glow` carries the primary button's halo because
  the shared lab wires `.btn-primary`'s `box-shadow` to `--glow` rather than to a shadow token.

## The physical textures (kit extras)

Eight `--cassette-*` tokens, declared in `kit.json` `signature` and rendered in the lab's Signature
section. These are the material, not decoration:

| Token | What it is |
|---|---|
| `--cassette-brushed` | brushed aluminium — a 1px `repeating-linear-gradient` of light/dark silver lines over a faint vertical shading, so it catches the room the way a real brushed rail does. A *fine repeating ramp* is what makes metal read; a smooth gradient reads as plastic. |
| `--cassette-aluminium` | the flat aluminium tone for trim that is not textured (rail edges, screw bezels, the underside of a lip). |
| `--cassette-grille` | **speaker grille** — a `radial-gradient` dot tiling on a 6px pitch, laid over the shaded beige of the cloth. The single most recognisable hi-fi texture, and it *is* expressible. |
| `--cassette-vu-scale` | **VU-meter scale** — *graduated* tick marks on a warm cream face: a tall tick every 45px, a short one every 9px. Two tick layers, each carrying its own `background-size` in the shorthand, which is the only way one token can hold ticks of two heights. |
| `--cassette-knurl` | **knurled knob** — a `repeating-conic-gradient`. Ribs that radiate from a centre are only expressible as a conic gradient; apply on a circular element. |
| `--cassette-led-glow` | the amber lamp's halo **and lit core** — an outward bleed onto the shell plus an inner amber wash (a `box-shadow`, so the lab *applies* it rather than painting it). A lamp has no halo without a core, so both live in the one token. |
| `--cassette-plastic-sheen` | the moulded gloss: a bright band across the top of a shell, a faint warm smudge along the bottom. |
| `--cassette-window` | the smoked **display window** — the one dark surface in the kit. Amber readouts and the LED glow are drawn on *this*, never on beige. |

## Type: why Overpass

- **Overpass** (display + body) is derived from Highway Gothic, the American signage face: drawn to
  survive paint, stencils and small physical panels. A mechanical/technical grotesque, not a
  friendly UI sans — which is what a front panel's lettering is.
- **Overpass Mono** (labels, eyebrows, badges, table headers, readouts) is **the same drawing at one
  width**. A real panel's silkscreen and its spec plate share a hand, so the label face and the body
  face belonging to one family is the argument, not a shortcut. Caps are tracked `+0.1em` — stamped
  and compressed, tighter than a HUD's 0.14–0.18em.
- **Not a retro script, not a 1950s diner face.** The kit is 1970s *industrial*; a script or a
  diner slab would turn a receiver into a jukebox.
- **One honest seam:** the shared lab styles `.btn` with `font: inherit`, so buttons drawn in the
  lab take their text from `--font-body`. The kit's *declared* button face is the mono
  (`{typography.label}` in `components:`), which is what a consumer copies. Recorded, not hidden.

## Contrast (verified numerically, not by eye)

Computed by `verify-cassette.py`, which parses `tokens.css` (no value is re-typed in the script),
resolves the `--bg` gradient to its stops and picks the darkest one. WCAG relative-luminance ratio,
`(Lhi + .05) / (Llo + .05)`.

### Required pairs

| Pair | Ratio | Target | |
|---|---|---|---|
| `--text` on `--bg` (darkest stop `#d3c6a6`) | **9.31:1** | ≥ 7 | ✓ |
| `--text` on `--bg` (lightest stop `#e2d8bf`) | **11.13:1** | ≥ 7 | ✓ |
| `--text-muted` on `--surface` | **7.32:1** | ≥ 4.5 | ✓ |
| `--text-invert` on `--accent` | **5.59:1** | ≥ 4.5 | ✓ |
| `--text-dim` on `--bg` (darkest stop) | **5.06:1** | ≥ 4.55 | ✓ |
| `--text-dim` on `--surface` | **6.51:1** | ≥ 4.55 | ✓ |

### Supplementary

| Pair | Ratio | |
|---|---|---|
| `--text-dim` on `--surface-2` (the inset bay) | **4.56:1** | ✓ ≥ 4.5 |
| `--text-invert` on `--accent-hover` | **6.87:1** | ✓ |
| `--accent-ink` on `--bg` (darkest) / `--surface` / `--surface-2` | **5.26 / 6.78 / 4.75:1** | ✓ |
| `--accent-ink-hover` on `--surface-2` | **6.05:1** | ✓ |
| `--ok` / `--warn` / `--danger` / `--info` on `--surface-2` | **4.90 / 4.71 / 4.88 / 5.16:1** | ✓ |
| `--text-muted` on `--surface-2` | 5.12:1 | |
| `--focus-ring` on `--bg` (darkest) | **3.79:1** | ✓ WCAG 1.4.11 (≥ 3) |
| `--border-strong` / `--border` on `--bg` (darkest) | 2.31 / 1.41:1 | decorative seams |
| `--accent` / `--accent-2` on `--bg` (darkest) | 1.85 / 2.33:1 | **fills only** — see below |
| `--text-invert` on `--accent-2` (avatar initial) | 4.44:1 | |

**No carve-out is needed here.** The inset bay `--surface-2` is a *darker shade of the same beige*
(#cabc9b), not an inverted dark well, so one warm ink clears **every** ground it is drawn on — which
is the whole reason the kit declined `--text-on-surface*`. The `surface-2` ground is also the
*binding* constraint for the status inks: `--warn` (`#624502`) is as dark as it is precisely so a
caution chip clears 4.5:1 on the bay rather than on the easy pale card. If you lighten `--surface-2`
toward white the status colours get easier; if you darken it past `#c2b394`, they start to fail.

The 1.85:1 of the amber on beige is not a defect — it is the reason `--accent-ink` exists, and the
measurement that proves a lamp is not an ink.

## Trade-offs

- **The ground is mid-tone, so the palette is dark-on-beige throughout.** Every status colour has to
  be a *deep* ink (a dark ochre rather than a bright amber, a record red rather than a scarlet) to
  clear 4.5:1 on the inset bay. That is the correct reading of a 1970s panel, but it does mean the
  kit cannot host a bright status chip; if you need one, put it on `--surface`, not `--surface-2`.
- **Amber is a strong brand to borrow.** A project that already owns orange will fight this kit.
- **No chamfers and no chamfer-related glow re-wiring** — `--cut: 0px`, so the lab's `--clip` path
  is unused. A 2px rim on a 12px radius is the whole silhouette.
- **Inset depth means no floating layers.** A modal or tooltip has no outer-shadow token to lean on
  and must use `--overlay` plus `--glow`. Intentional: this kit does not do floating panels.
- **`--radius-pill: 999px` is a full pill** — a deliberate maximum-radius choice (the largest in
  the set) so a badge reads as a chunky hardware tag. If you want a stamped rectangular plate,
  that is `inside-the-machine`'s device, not this one.
- **The shared lab hard-codes** `border: 1px solid` on `.btn` (so buttons keep a 1px rim while
  cards, inputs, nav, badges, alerts and code blocks take the 2px `--border-w`), and `999px`/`50%`
  on `.toggle input`, `.dot` and `.bar`. Neither is fixable from `tokens.css`; a project using the
  kit directly should set those by hand. Recorded rather than papered over.
- **Two of the eight signature textures** (the grille and the VU scale) are multi-layer `background`
  shorthands, because a dot tiling needs a pitch (`/ 6px 6px repeat`) and a scale needs a face under
  its ticks. They are applied as `background: var(--cassette-grille)` — a single declaration, like
  any other background token.

## When to use

Hardware and device pages, audio/music products, retro-industrial or "workshop tool" marketing,
firmware and console front-ends that should feel like an object, and any page where the metaphor is
*a panel you operate*. Avoid it for long-form reading (beige at 15px is a lot of page), for brands
that need a cool, clinical register, and for anything that must look like glass or paper — this kit
is emphatically neither.

## Files

`DESIGN.md` (normative values) · `tokens.css` (the contract) · `kit.json` (gallery metadata) ·
`index.html`, `tokens.json`, `tailwind.theme.json`, `theme.css` (generated by
`python tools/build.py`).

## Verify

```bash
python tools/build.py --no-export --no-lint          # lab html + token-contract check
python "C:/Users/Lily/AppData/Local/hermes/cache/scratch/verify-cassette.py"   # contrast table
```
