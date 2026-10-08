# Inside the Machine

**A machined instrument panel. Amber is the one thing that acts; green phosphor is everything
the machine reports; the surfaces are drawn carbon cloth, punched vents and brushed steel; the
CONTROLS — buttons, fields, checks, the nav, the switch — are milled plates and wells rather than
flat rectangles; depth is engraved, not floating; and the mono carries the interface.**

`11` · dark · `IBM Plex Mono · IBM Plex Sans` · source: original

## Stance

This kit is the *interior* of a machine, not a product page about one. The ground is graphite
(#0d0f11), panels are milled into it, and every seam is an opaque 1px steel hairline — engraving
is subtractive, so the lines are cut, not lit. Two phosphor lamps do all the talking: **amber
(#ffb000) acts, green (#4dff9e) reports, red (#ff5147) faults.** Nothing floats: depth runs
inwards, with a lit top lip and a shadowed bottom lip on every recessed surface.

A palette alone, though, reads as a colour scheme — so the kit also carries a **material**: a
woven carbon-fibre cloth, a punched vent plate and a banded brushed steel, each drawn as a
base64 SVG data URI. They are the surfaces the colours cannot describe (see *Material* below).

And a colour scheme *also* leaves every control flat, so the controls are **cut from the chassis
too**. The first pass textured the page but left the buttons, inputs, selects, textareas,
checkboxes, nav pills, tabs and toggle as flat dark UI — an industrial-*themed* page rather than
machined hardware. The second pass machined the components themselves: every field is a milled
**well**, every button wears a hard two-tone **bevel** and sits on a plate, the native controls
are squared to stamped **sockets**, and the nav/tab/toggle chrome takes the same recess and bevel
through a six-declaration `kit.css` (see *Machined components* below). No colour moved.

Use it for consoles, telemetry, device/firmware tooling, teardown docs, hardware dashboards and
anything whose subject is a system rather than a sentence. It is at its best with tables,
readouts, IDs and status rows — the lab's data section is the kit's home page, not its stress
test.

Six things make it recognisably *this* kit at 200×120:

1. **Mono-first typography.** In every other dark kit here the mono is a label font and a
   grotesque carries the headings. Here IBM Plex Mono sets the h1, the section headings, the
   eyebrows, the table headers, the badges and the metadata; IBM Plex Sans exists only for
   sentences.
2. **Engraved depth.** `--shadow-1` / `--shadow-2` are **inset** — lit top lip, shadowed bottom
   lip, deeper well for `card-elevated`. There is no soft outer drop shadow in the kit at all.
3. **Phosphor readouts on warm graphite.** Amber + green lamps over a neutral-warm charcoal,
   instead of Signal's cool navy or Cyberpunk's violet-black.
4. **Drawn machine material.** A carbon-fibre weave on the media blanks and three signature
   textures (weave, vent grille, brushed steel) — hardware you can see, not just colours.
5. **Machined controls.** A field is a milled well, a button is a beveled plate in a seat, and
   the native controls are squared sockets — so the components read as hardware, not as flat UI.
6. **Machined detail.** Opaque steel hairlines, `+0.12em` stamped caps labels, and radii capped
   at 4px so nothing reads soft.

## Ground truth

Every value below is authored for this kit; nothing is inherited from another kit's palette.

| Token | Value | Note |
|---|---|---|
| `--bg` | `#0d0f11` | graphite chassis |
| `--bg-2` | `#131719` | masthead gradient stop |
| `--surface` | `#16191d` | milled panel face |
| `--surface-2` | `#1b1f23` | recessed well, inputs |
| `--overlay` | `rgba(6,8,10,.78)` | modal scrim |
| `--text` | `#e9edef` | 16.30:1 on `--bg` |
| `--text-muted` | `#9aa4ad` | 6.96:1 on `--surface` |
| `--text-dim` | `#828d95` | 4.89:1 on `--surface-2` (the binding pair) |
| `--text-invert` | `#0d0f11` | chassis ink on the amber plate |
| `--accent` | `#ffb000` | amber — the only action colour |
| `--accent-hover` | `#ffc233` | amber lifted one step |
| `--accent-2` | `#4dff9e` | green phosphor — readouts, media |
| `--accent-soft` | `rgba(255,176,0,.13)` | 13% amber tint, derived |
| `--ok` | `#4dff9e` | green phosphor: nominal |
| `--warn` | `#d99a2b` | amber held one step *down* |
| `--danger` | `#ff5147` | fault lamp |
| `--info` | `#6c99b8` | steel blue: data / telemetry |
| `--border` | `#2a2f35` | the machined seam (opaque) |
| `--border-strong` | `#4a535c` | input rim / emphasised rule |
| `--border-w` | `1px` | this kit is milled, not bold-line |
| `--focus-ring` | `#ffc233` | amber, one step lighter than action |
| `--radius-sm/md/lg` | `2px` / `3px` / `4px` | nothing softer than 4px |
| `--radius-pill` | `4px` | deliberate — see below |
| `--cut` | `0px` | no chamfers; the seam is the detail |
| `--shadow-1` | `inset 0 2px 0 rgba(255,255,255,.10), inset 0 -2px 0 rgba(0,0,0,.62), inset 0 3px 9px -4px rgba(0,0,0,.48)` | the recess — 2px lips, the control chamfer's language |
| `--shadow-2` | `inset 0 2px 0 rgba(255,255,255,.13), inset 0 -3px 0 rgba(0,0,0,.70), inset 0 6px 16px -7px rgba(0,0,0,.60)` | the deeper well |
| `--glow` | `0 0 0 1px rgba(255,176,0,.55), 0 0 0 3px rgba(255,176,0,.14), var(--machine-bevel)` | a **zero-blur** amber bezel — see below |
| `--btn-shadow` | `var(--machine-bevel)` | the control edge on **every** button variant |
| `--machine-bevel` | 2px lit top lip, 3px dark bottom lip, lit/dark side lips, zero-blur seat, 8% face lift | the button/knob plate |
| `--machine-recess` | hard top shadow, 5px falloff, lit bottom lip, dark inner wall | the milled well — shared by fields, nav, tabs, toggle |
| `--blur` | `none` | machined metal is not frosted |
| `--check-appearance` | `none` | square the native checkbox **and radio** |
| `--check-bg` / `--check-border` / `--check-checked` | `var(--surface-2)` / `1px solid var(--border-strong)` / `var(--accent)` | an unchecked socket, a lit amber checked plate |
| `--media-bg` | `var(--inside-the-machine-weave)` | the media panel is carbon cloth, not a colour |
| `--media-op` | `1` | a texture washed to `.85` loses its weave |
| `--input-inset` | `var(--machine-recess)` | a field is a hole in the panel |
| `--inside-the-machine-weave` | drawn SVG, `24px` repeat | woven carbon-fibre cloth (surface) |
| `--inside-the-machine-grille` | drawn SVG, `12px` repeat | punched vent plate (structure) |
| `--inside-the-machine-steel` | hard-banded gradient | brushed steel, raked light (light) |

## Material — three drawn textures

A kit this dark reads as a colour scheme until real surfaces appear. So the palette is joined by
three textures, each with a *different job*, each drawn (base64 SVG / hard-stop gradient) rather
than smeared. Every one is rendered as a 168×72 tile on `--surface-2` in the lab's Signature
strip; the weave is additionally milled onto the media panel.

**Why a tile and not a ramp.** A smooth gradient cannot be a weave, a punched hole or a lit
chamfer — those are drawn forms (the same reason a rose cannot be rings). And a tile tuned for
subtlety renders *blank* at 168×72, which is the most-repeated defect in this library, so each is
tuned to be plainly visible and is proved non-flat below.

| Motif | Job | What it is | Tile std-dev (168×72) |
|---|---|---|---|
| `--inside-the-machine-weave` | **surface** | woven carbon-fibre cloth: a 2/2 twill, diagonal over/under sheen, under a raked specular sweep | **50.0** |
| `--inside-the-machine-grille` | **structure** | punched vent plate: each hole a near-black well with a bright lit lower lip | **26.9** |
| `--inside-the-machine-steel` | **light** | brushed steel rail: two co-prime grain periods + a raked specular band over hard bands | **49.8** |

*Non-flatness* is the per-tile pixel standard deviation of luminance, measured from the tiles
**as rendered in this kit's lab** (`.tile .chip`, 168×72 CSS px, Chromium at 2× device pixels;
PIL/numpy). A flat plate scores ~0; these are ~27–50, i.e. unmistakably textured. (The carbon
cloth milled on the media panel measures std-dev **53.2** over its ~297×96 CSS px.)

**The cloth.** A **2/2 twill**: continuous warp and weft tows, and in each crossing the tow that
is *on top* lights up (near-white over, near-black under) while the "over" cells step one column
per row — so the sheen forms the diagonal bands that make a twill read as carbon rather than as a
grid of beveled squares. Three earlier constructions (corner-shaded squares, crossed diagonal
bands, and a cast-shadow grid) each read as a lattice or raised tiles and were discarded. It is
the kit's one *surface*, and it is the reason the media panel is the place the material is
loudest. Over the whole tile now sits a **raked specular sweep** (a hard-stepped lit → flat →
shadowed diagonal band), so the light falls *across* the cloth at an angle and the weave reads
anisotropic rather than evenly printed. (A per-24px-tile overlay was tried first and simply tiled
into invisible noise; the sweep has to span the element.)

**The grille.** A plate of punched holes: a dark well (r 3.15) inside a steel ring (r 4.7) offset
down 0.8px so the lower lip catches light. It reads as perforated metal, not a dot grid — the
offset lip is the whole thing. The lip was brightened to `#95a2b0` against a `#030406` well in the
second pass: at the original lip the tile read as a flat dot grid at 168×72.

**The steel.** Vertical striations over **hard** px bands — a lit top rim, the bright specular
band, a machine-mark line, a dark chamfer foot. Hard stops, never a smooth ramp: a ramp reads as
fog, and half the library's chrome reads as fog for exactly this reason. Two changes make it read
as *metal* rather than as a printed stripe: the grain is now **two overlapping co-prime periods**
(2px and 7px, so the comb is not mechanically even), and a **broad raked specular band** sweeps
across it in one diagonal.

**Where the texture is *not*, and why.** The page ground, the masthead and every text block stay
flat graphite. `--text-dim` clears 4.55:1 only against grounds at or below `#1b1f23`; a weave
bright enough to be visible would drop `--text-dim` to ~2–4:1 wherever it passed under a caption.
So the material is kept to the text-free boxes (media blanks, signature tiles) where it can be
bold. There is **no textured `--bg` layer**: on this kit it cannot both earn its place and stay
legible.

**The one motif with no application.** `--inside-the-machine-steel` is a signature tile only. The
obvious home is `--fill-bg` (progress + avatar), but the avatar prints `--text-invert` (graphite)
on its fill, and steel dark enough to read as steel is too dark for that ink (a light aluminium
rail that fixes the avatar measured std-dev 29 and reads as weak grey). So `--fill-bg` keeps the
lab's phosphor ramp and the steel lives where it can be bold.

## Machined components — the second pass

A cold review of the first pass was right: *"the page has strong industrial cues, but most actual
components — buttons, inputs, selects, textareas, toggles, nav pills, tabs, cards — remain flat
dark UI. The materials are confined to the Signature strip and one card panel, so it reads as an
industrial-themed dark UI rather than machined hardware."* Colours and type were industrial; the
controls were still rectangles with a border. So the controls were **cut**, using only what the
shared lab already honours. **No palette value changed** — every move below is a *depth* move.

**1 · A field is a WELL, not a box** (`--input-inset` → `--machine-recess`). The highest-yield
change. `--machine-recess` is a hard shadow line at the inside top, a 5px falloff into the well, a
lit `rgba(255,255,255,.12)` line at the inside bottom, and a dark inner wall around all four
edges; `--input-inset` is simply that token. Rendered, the secondary-input top edge sits at
rgb(2,2,3) against a face of rgb(25,29,33) and a lit bottom lip of rgb(33,35,37) — a real
sunken field. It reads as recessed *even though* `--surface-2` is a step **lighter** than the card:
the recess, not the fill, carries it. At the previous `rgba(0,0,0,.55)`/`.05` alphas the well was
invisible at 100%.

**2 · Every button is a plate with a BEVEL** (`--btn-shadow` → `--machine-bevel`). The lab paints
`--btn-shadow` on *every* `.btn` variant; it previously reached only `.btn-primary` (through
`--glow`). `--machine-bevel` is a 2px lit top lip, a 3px shadowed bottom lip, lit/dark side lips
so the light has a direction, a hard zero-blur seat shadow, and — last — an 8% face lift.
Measured on the rendered secondary button: a lit top lip at rgb(99,101,102), a plate face at
rgb(32,34,36) against a page ground of rgb(13,15,17), and a bottom lip at rgb(7,7,8).
The 8% face lift is doing real work: secondary/ghost/danger have a **transparent** `--_bg`, so
without a plate the bevel has nothing to sit on and the controls stay outlines. The face lift is a
box-shadow layer, not a colour — it is the same neutral `rgba(255,255,255,.08)` on all five
variants, and on the amber plate it is invisible.

**3 · The glow is retired for a hard BEZEL** (`--glow`). `--glow` was a `14px` blurred amber
halo. A blur is the one thing on the page still reading as modern UI, so it is now **zero-blur**:
a hard 1px + 3px amber ring plus the same bevel. The machine reads as milled, not as glowing —
which is the test the brief set for switching to zero-blur. It is still amber and still only on
the amber switch, so "an energised control wears the lamp" survives; only the bloom is gone.

**4 · The native controls are squared** (`--check-appearance` + `--check-bg` / `--check-border` /
`--check-checked`). Chromium draws a **radio as a circle**, which a kit capped at
`--radius-pill: 4px` cannot have; `--check-appearance: none` makes both controls a stamped socket.
Unchecked is a small well on `--surface-2` with a `--border-strong` rim; checked is a lit amber
plate (the lab paints the fill — there is no glyph — so "on" is a **lamp**, which is this machine's
own vocabulary). The cost is the checkmark, and it is stated as a trade-off below.

**5 · The nav, tabs and toggle take the same language — via `kit.css`.** These three are chromed
directly in `lab.css` with a background and a border and **no shadow hook at all**: no token
reaches them, which is exactly the escape-hatch case in `KIT-SPEC.md` (a *construction*, not a
colour). The kit ships a six-declaration `kit.css` that plumbs the two construction tokens it
already defines onto them: the nav bar and the tab row become `--machine-recess` **channels**, the
current nav pill and current tab become `--machine-bevel` **plates**, and the toggle becomes a
recessed track with a beveled knob. It hardcodes no colour, invents no markup, and carries one
neutralisation — `.btn-link`, which the lab deliberately made a bare link, has the plate taken
back off it (`--btn-shadow` reaches it too, and a link is not a plate).

**What is deliberately still flat.** `Disabled` keeps `box-shadow: none` (the lab sets it) — an
inactive control *should* be flat. `Ghost` keeps its low emphasis (a faint plate and a bevel; it
is not meant to shout). And the `link` control is bare by design.

**The panel edge was deepened to match.** `--shadow-1` / `--shadow-2` were already inset (lit top
lip, shadowed bottom lip, falloff into the well) but at **1px** lips — the same hairline that made
the controls look flat. They are now 2px/2px (and 2px/3px for the deeper well), so a *panel* edge
is cut with the same chamfer as a *control* edge. No colour moved; only the lip height.

## Type: why the mono leads

- **IBM Plex Mono** is the display face, the label face and the readout face. It was drawn for
  engineering paperwork — it survives at 11px, it survives in a column, and it has a
  slightly-squared terminal that reads as stamped rather than drawn. Putting it on the h1 is the
  kit's whole position: on this machine even the title is a readout.
- **IBM Plex Sans** is the same superfamily, so nothing looks bolted on; it appears only where a
  human is reading a sentence (body copy, card bodies, hints).
- **One honest seam:** the shared lab styles `.btn` with `font: inherit`, so button text drawn
  in the lab comes from `--font-body`. The kit's *declared* button style is still the mono label
  (`{typography.label}` in `components:`), which is what a consumer copies. Recorded here rather
  than hidden: it is the one place where the shared lab's own inheritance overrides a kit's
  declared component face.
- **Stamped, not spaced.** Caps labels run `+0.12em` (`--tracking-caps`). Signal runs `0.14em`
  and Cyberpunk `0.18em`; stamping *compresses*, so this kit stays tighter than both.
- **Display tracking is `-0.01em`** — at 2.9rem a monospaced face will otherwise look loose.

## Derived, and why

- `--accent-hover: #ffc233` — one visible step up in lightness from `#ffb000`, same hue. A lamp
  getting brighter, not changing colour.
- `--accent-soft: rgba(255,176,0,.13)` — a 13% tint of `--accent`, expressed as `rgba()` rather
  than re-typed as a hex, because it is derivable and must stay in sync with the amber.
- `--warn: #d99a2b` — amber *held one step down*. The caution lamp and the action plate are the
  same family, but a stamp must never be as loud as a switch. This is also why `--warn` is not
  simply `--accent`.
- `--text-invert: #0d0f11` — the chassis ink. Amber is a fill, so the primary button's label is
  graphite, never white (white on `#ffb000` is ~1.6:1).
- `--media-bg: var(--inside-the-machine-weave)` and `--media-op: 1` — the media panel is filled
  by the weave *token*, not a re-typed copy of it, so the cloth and the signature tile can never
  drift; and it is held opaque because the default `.85` dim is a wash over the thing that is the
  point.
- `--input-inset: var(--machine-recess)` — the field recess is not re-declared; it *is* the
  chassis-well token. One definition, so a field, the nav channel, the tab row and the toggle
  track can never drift apart.
- `--machine-bevel: var(--btn-shadow)` and folded into `--glow` — the control edge is declared
  once. The lab paints `--btn-shadow` on every `.btn` but `.btn-primary` overrides `box-shadow`
  with `--glow`, so the bevel is *composed into* `--glow` rather than restated: the amber switch
  gets the identical edge as the secondary plate, and a change to the bevel moves both.
- `--border` / `--border-strong` are **opaque steel**, not translucent white. Every other dark
  kit in this set tints its hairlines; opaque steel is the engraved look and it is the reason
  the seams hold at 1px.
- `--radius-pill: 4px` — a stamped plate instead of a lozenge. The token keeps its contract name,
  but a fully round badge would read as a product-UI tag and undo the milled language. The
  shared lab's own switch keeps its hard-coded rocker, which is left alone deliberately.

### The shared lamps

`--ok` and `--accent-2` are the *same* green (`#4dff9e`), and that is the design: this machine
has one green lamp, and it means "nominal" whether it is filling a readout plate or lighting a
status chip. One lamp, one meaning. If you need a second green for something that does *not*
mean nominal, that is a sign the element should not be green.

## Contrast (verified numerically, not by eye)

Computed from `tokens.css` by script — see the verification log. WCAG relative-luminance ratio,
`(Lhi + .05) / (Llo + .05)`. **The palette is unchanged** — not by the material pass, and not by
the machining pass — so every number below is the same as it was; the textures live on text-free
boxes, and `verify-lab.cjs` re-samples the composited ground behind every text box and still passes.

| Pair | Ratio | Target | |
|---|---|---|---|
| `--text` on `--bg` | **16.30:1** | ≥ 7 | ✓ |
| `--text-muted` on `--surface` | **6.96:1** | ≥ 4.5 | ✓ |
| `--text-invert` on `--accent` | **10.48:1** | ≥ 4.5 | ✓ |
| `--text-dim` on `--bg` | **5.66:1** | ≥ 4.55 | ✓ |
| `--text-dim` on `--surface` | **5.20:1** | ≥ 4.55 | ✓ |
| `--text-dim` on `--surface-2` | **4.89:1** | ≥ 4.55 | ✓ |
| `--accent` as text on `--surface` | **9.62:1** | ≥ 4.5 | ✓ |
| `--accent` on `--accent-soft`@`--surface` (composite) | **7.47:1** | ≥ 4.5 | ✓ |

The **worst pair** is `--text-dim` on `--surface-2` at **4.89:1** (≥ 4.55) — the lightest ground,
the input well. That is the binding constraint: it is why the dim grey is `#828d95` rather than a
darker, moodier value, and why no texture may sit under type. `--border` / `--border-strong` are
deliberately below 3:1 (1.2–2.0:1) — they are decorative seams, never the sole carrier of meaning.

## Trade-offs

- **The mono costs horizontal room.** IBM Plex Mono is wide, so the h1 and any tracked caps
  labels need more width than a grotesque would. Short labels and short titles are part of the
  kit, not an accident of the demo copy.
- **No outer shadow at all** means an element that genuinely must sit *above* the chassis (a
  modal, a tooltip) has no ready-made depth token and must lean on `--overlay` and `--glow`
  instead. That is intentional: this kit does not do floating layers.
- **The material is drawn, and that has a cost.** Each texture is a base64 SVG (the only way a
  token may hold artwork) and a fixed-size tile; a consumer who stretches one to fill a panel
  gets a smeared, wrong-scale weave. Size it (`0 0 / 24px 24px repeat`) or don't use it.
- **`--radius-pill: 4px`** is a knowing bend of a token name. Consumers who assume "pill =
  999px" will get a square badge; that is the desired result here, and it is documented above.
  One visible consequence in the shared lab: `.badge` (pill) and `.badge-square` (`--radius-sm`,
  2px) now differ by 2px, so those two demos look near-identical. The kit is not distinguishing
  badges by roundness on purpose — it distinguishes them by colour.
- **The checkmark is gone.** Squaring the native controls with `--check-appearance: none` trades
  the tick glyph for a filled amber plate — because the lab paints a `background-color` and there
  is no glyph to draw. It reads correctly as a lit indicator (and the radio, which *had* to be
  squared, gains the most), but a consumer who needs a literal tick must add one. This is the one
  place a control loses information it previously carried.
- **`Ghost` is no longer fully chromeless.** The 8% face lift that makes the bevel legible on a
  transparent variant also gives the ghost control a faint plate. On a machine, every control has
  a surface — but a consumer who relied on "ghost = invisible until hover" gets a small plate
  instead. It is still the quietest control in the kit.
- **`kit.css` is a second file to copy.** The nav, tabs and toggle only machine if `kit.css` ships
  beside `tokens.css` (the lab links it automatically). A consumer who takes the tokens alone gets
  the milled controls everywhere the lab has a shadow hook, and flat nav/tabs/toggle. The README
  says exactly what it does and why tokens could not reach those three.
- **The bevel is a 2–3px cue.** At 100% on a normal-DPI display the chamber reads as machined; on
  a heavily-antialiased or very low-DPI surface the fine lips can soften toward "flat chip". The
  edges were deliberately made *2px/3px* rather than hairline (`0 1px`) for this reason, but the
  register is a fine one — this kit is milled, not chunky skeuomorphic.
- **The lamp no longer blooms.** Zero-blurring `--glow` is what makes the controls read as milled
  rather than glowing, but it removes the soft halo. A consumer who wants a phosphor bloom adds it
  themselves; the kit's position is that a bloom is the wrong idiom for a machined panel.
- **Only one texture reaches a real component** (the weave, on the media panel); the grille and
  the steel are signature motifs. That is a deliberate ceiling: the other natural homes
  (`--bg`, `--wash`, `--fill-bg`) all put a texture under type or under graphite ink, where it
  would have to be so faint it would stop being a texture. (The *machining*, by contrast, reaches
  every control — it is depth, not texture, so it costs no contrast.)
- **Two amber tokens** (`--accent` and `--warn`) plus two uses of green (`--accent-2`, `--ok`)
  means a palette map shows repeats. The repeats are semantic, not accidental.
- **Amber as the action colour** is a warm choice in a field of cool dark themes. It is the
  fastest way to make the primary action findable on a graphite page, but it does mean the kit
  is a poor fit for a brand that already owns orange.

## Files

`DESIGN.md` (normative values) · `tokens.css` (the contract) · `kit.css` (the escape hatch — the
six declarations that plumb the recess and bevel onto the nav, the tab row and the toggle, which
`lab.css` chromes with no shadow hook) · `kit.json` (gallery metadata, with a `signature` list
naming the three textures) · `index.html`, `tokens.json`, `tailwind.theme.json`, `theme.css`
(generated by `python tools/build.py`).
