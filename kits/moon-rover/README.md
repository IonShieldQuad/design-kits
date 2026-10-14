# Moon Rover

**Dust, grit and one hard sun. This is the ground a mission is standing on — grey-brown regolith
under unfiltered light, a cast shadow with no penumbra, wheel ruts pressed into the surface, and a
small piece of hardware left standing in it.**

`34` · light · `Saira Condensed · Saira · Fira Mono` · source: original

## Stance

Not a picture of space — a picture of the *surface*. The register is mineral and physical: a
warm-grey/taupe regolith ground (#e6e2d7 at the top of the page settling to #d2ccbf), a near-black
warm ink, one dust-covered amber for action, and a cold blue-grey that appears for exactly one
reason. On the Moon the shadow really *is* blue — airless shadow is lit by earthshine and starlight
and nothing else — so the cold colour is the **shadow counterpoint**, not atmosphere. There is no
violet, no neon, no glow, no starfield and no black in this palette, because the sky is out of frame.

**The light model is three surfaces and a plate.** A card is a **sunlit plate**, a shade *lighter*
than the ground (#eeeae0 against a #d2ccbf lower ground); an inset is a **scooped recess**, a shade
*darker* (#c4beb0) — the same regolith with the sun taken off it; and everything casts a **zero-blur
offset plate** of shadow to the lower right. Nothing floats and nothing glows.

**Two grades of one material, and that is the load-bearing decision.** Regolith is drawn, and it
ships in two grades:

- `--moon-rover-dust` — the **ground grade**. Sunlit chalk grains with every darkening element
  capped at 11% alpha, because 12px captions are set on it.
- `--moon-rover-grit` — the **material grade**. Each grain keeps a lit facet, a shaded facet and a
  hairline cast sliver. It is used only where no type can sit: the card media panel and the
  signature tiles.

One grade cannot do both jobs. Regolith with honest micro-shadows is not a background you can set a
caption on, and pretending otherwise is how a kit ships as "dusty colours" with unreadable hints.
The split is measurable, not asserted: see the contrast table.

### Recognisable at 200×120

1. **A speckled mid-tone regolith ground** — the only kit in this set that starts from *dust*.
2. **One dust-covered amber** (#d9821c) as the sole saturated action colour, and it is always a
   fill, never a label.
3. **A hard offset shadow plate** on every card, button, nav item and switch — zero blur, always the
   same direction.
4. **A 3px "pill"** — badges, switch tracks and knobs, dots and the avatar are all square-ish
   machined plates. Nothing here is a capsule.

None of those four are `outer-space` (a dark void with nebula blooms and a glow), `space-noir` (a
dark inked print with film grain) or `cassette` (a light *beige plastic* panel whose depth is
**inset** everywhere and whose shadows are all inside the shell).

## Palette, with roles

| Token | Value | Role |
|---|---|---|
| `--bg` | `dust texture + linear-gradient(180deg, #e6e2d7 0px, #ded9cd 420px, #d2ccbf 1000px)` | the regolith ground — a texture layer over a three-stop ramp in **px** stops |
| `--bg-2` | `#ded9cd` | the dominant stop / solid stand-in for exports |
| `--surface` | `#eeeae0` | cards — the **sunlit plate** |
| `--surface-2` | `#c4beb0` | inputs, badges, code — the **scooped recess** |
| `--overlay` | `rgba(28,25,20,.56)` | modal scrim (shadow, not black) |
| `--text` | `#1e1c17` | the near-black warm ink |
| `--text-muted` | `#38332b` | second step |
| `--text-dim` | `#423d31` | captions, hints, table headers — the **binding pair** in this kit |
| `--text-invert` | `#191410` | dust-black printed **on** the amber plate |
| `--accent` | `#d9821c` | **THE DUST-COVERED AMBER.** The one action colour — fill only |
| `--accent-hover` | `#eb9a33` | the dust blown off it: the plate comes **up** on press |
| `--accent-2` | `#4a6a86` | **shadow blue-grey** — the one cool colour: media and fills, never an action |
| `--accent-soft` | `rgba(217,130,28,.15)` | 15% tint of `--accent`, derived — nav/tab fills, inline code, badges |
| `--accent-ink` | `#5e2b03` | the amber **as text** — a wet-rust brown of the same family |
| `--accent-ink-hover` | `#4a2102` | the hover step for accent text |
| `--ok` | `#1f4a28` | dusty green — nominal |
| `--warn` | `#553d04` | deep ochre, deliberately not a dimmed amber: a caution must not read as the action |
| `--danger` | `#7a2714` | oxide red — not scarlet |
| `--info` | `#26405a` | telemetry blue |
| `--border` / `--border-strong` | `#a49c8a` / `#786f5d` | the hard seams (opaque, low-contrast) |
| `--border-w` | `2px` | a machined edge, not a hairline |
| `--focus-ring` | `#2e4a63` | the cold family: keyboard focus is instrumentation, not the action |
| `--radius-sm/md/lg` | `2px` / `3px` / `5px` | machined plate geometry |
| `--radius-pill` | `3px` | **not a capsule** — see Shapes in `DESIGN.md` |
| `--cut` | `0px` | no chamfer and no `--clip`: this kit keeps its 2px frame on all four edges |
| `--shadow-1` | `4px 4px 0 0 rgba(38,33,24,.40), inset 1px 1px 0 rgba(255,253,246,.58)` | the hard cast plate + a one-pixel sunlit lip |
| `--shadow-2` | `7px 7px 0 0 rgba(30,26,18,.50), inset 1px 1px 0 rgba(255,253,246,.58)` | the deeper recess |
| `--glow` | `5px 5px 0 0 rgba(34,29,20,.52), inset 1px 1px 0 rgba(255,253,246,.64)` | the primary plate casts **further** — a raised plate on a sunlit surface does |
| `--blur` | `none` | an airless body has no diffusion |

## Which colour drives action

**Amber (`--accent`, #d9821c) — and only amber.** It fills the primary button, the checked
checkbox and switch, the progress bar, the avatar and the hard-banded fill, and nothing else. As a
label on this ground it measures **1.83:1**: a fill is not an ink. Accent-as-text therefore ships
separately as `--accent-ink` (#5e2b03), which clears **7.20:1** on the darkest ground stop and
**5.76:1** on its own 15% tint composited over the darkest recess.

- **Shadow blue-grey (`--accent-2`, #4a6a86)** is the second accent and the kit's one cool note. It
  means *shadow*: the shadow side of a card's media panel (the boulder's cast plate) and the second
  stop of fills. Its darker family members are `--info` and `--focus-ring`. It never acts.
- **Status colours stay off the amber by value and hue** — a dark dusty green, a deep ochre, an
  oxide red and a slate blue, all solved on `--surface-2`, the **darkest** ground any of them is
  drawn on (a badge keeps its own recess background), not on the easy pale card.
- **Why hover brightens.** The reflex on a light kit is to darken on hover, but the amber is a
  *fill*: brightening to `#eb9a33` is both physically honest (dust blown off a sunlit plate) and the
  legible move — its own label rises from 6.23:1 to **8.01:1**. Accent *text* darkens on hover
  instead (the standard light-kit step), which is why `--accent-ink-hover` is separate.

## Signature motifs

Three, three jobs, each drawn as base64 SVG because none of the three is expressible as a gradient.
Rendered as 168×72 tiles on `--surface-2` in the lab's Signature strip; **non-flatness measured from
the rendered page** as the standard deviation of the device pixels inside each tile (each tile is
336×144 device px at 2×, so a flat plate would score ≈ 0.5):

| Token | Job | std-dev | Where it lives |
|---|---|---|---|
| `--moon-rover-regolith` | **the material** | **21.24** | the grade the media panel is made of, at two scales |
| `--moon-rover-tracks` | **the trace** | **31.06** | the Signature strip; built from `--moon-rover-tread` |
| `--moon-rover-mast` | **the machine** | **26.22** | the Signature strip; a post, an arm, a box |

- **Regolith** — angular grains, each with a lit facet, a shaded facet and a hairline cast sliver;
  the ground grade is the same drawing with the micro-shadows capped. Two scales (56px and 112px,
  one tile at two sizes) so the ground never reads as wallpaper.
- **Wheel tracks** — two ruts with the displaced material pushed up along each edge: dark on the
  sunward *inner* wall, lit on the wall opposite, i.e. a groove in the light model this kit uses
  everywhere. The lane edges **wander** (and the artwork is built so the wander is continuous across
  the tile seam), the grouser bars are unevenly spaced with 15% of them filled in by drift, and the
  dust between and around the lanes is undisturbed. A regular ramp of bars reads as a ribbed mat or
  as hatching; that is the failure this motif exists to avoid, and it was checked cold against a
  reviewer before it shipped.
- **The mast** — a post, a cross-arm and an instrument box, drawn from three primitives. **No
  vehicle, no spacecraft silhouette, no agency mark, no mission artwork.** Its shadow is a real
  **planar projection** (a shear matrix in the artwork: a point at height *h* lands *h*/tan(elev)
  to the lower right), so the shadow is *longer than the object* — the one thing a drop shadow can
  never say.

**A motif that was cut, honestly.** The obvious third motif was a **crater rim as an arc band**.
Drawn the way the brief suggests, it rendered cold as a *wavy ribbon / dune stripe* — three parallel
arc bands following the same profile read as decoration, not as terrain — and a bowl seen from above
risked the smile/face read the brief warns about. It was replaced with the mast. The other cut
candidate, a **sample scoop**, read correctly as "a robotic arm with a bucket" but floated: at
168×72 with no ground line and no long shadow it had nothing to stand on, and the mast states the
kit's thesis (hard sun → long hard shadow) better.

## Contrast (verified numerically, not by eye)

Computed by `verify-moon-rover.py`, which **parses `tokens.css`** and resolves the `--bg` ramp stops
from it — no value is re-typed in the script — and which decodes the kit's own base64 SVG for the
texture grade and composites *that artwork's* layers in paint order. WCAG relative-luminance ratio.

### Required pairs (worst ground per row; full table in the script's output)

| Pair | Ground | Ratio | Target | |
|---|---|---|---|---|
| `--text` | `--surface-2` `#c4beb0` (darkest) | **9.19:1** | ≥ 7 | ✓ |
| `--text` | darkest `--bg` stop `#d2ccbf` | **10.64:1** | ≥ 7 | ✓ |
| `--text-muted` | `--surface-2` | **6.76:1** | ≥ 4.5 | ✓ |
| `--text-dim` | `--surface-2` | **5.83:1** | ≥ 4.55 | ✓ |
| `--text-invert` on `--accent` | `--accent` | **6.23:1** | ≥ 4.5 | ✓ |
| `--accent-ink` | `--surface-2` | **6.22:1** | ≥ 4.5 | ✓ |
| `--accent-ink` on 15% `--accent-soft` | composited over `--surface-2` | **5.76:1** | ≥ 4.5 | ✓ |
| `--focus-ring` | `--surface-2` | **4.98:1** | ≥ 3 | ✓ |
| `--ok` / `--warn` | `--surface-2` | **5.48 / 5.52:1** | ≥ 4.5 | ✓ |
| `--danger` / `--info` | `--surface-2` | **5.33 / 5.78:1** | ≥ 4.5 | ✓ |
| `--text-invert` on `--accent-hover` | `--accent-hover` | **8.01:1** | ≥ 4.5 | ✓ |

### The textured ground — graded as a texture, not as a flat ground

An image layer on `--bg` raises arbitrary pixels' luminance, so the ground grade's **worst composite
pixel** is computed from the shipped artwork: every darkening layer of the texture landing on the
same spot, over the darkest `--bg` stop.

| Composite | Pixel | `--text` | `--text-muted` | `--text-dim` | `--accent-ink` |
|---|---|---|---|---|---|
| **worst dark composite** (all dark layers stacked) | `#b2ac9f` | **7.53:1** | **5.54:1** | **4.78:1** | **5.10:1** |
| every layer of the art stacked | `#e9e6de` | 13.65:1 | 10.04:1 | 8.66:1 | 9.24:1 |
| lightest composite pixel | `#fcfaf2` | 16.29:1 | 11.99:1 | 10.34:1 | 11.02:1 |

And measured from the **rendered page** (a real screenshot of the built lab, sampled in the pure
ground margins): the darkest ground pixel actually produced is `#bab3a9` → `--text` **8.19:1**,
`--text-dim` **5.20:1**, `--accent-ink` **5.55:1**; the lightest is `#fcfaf2` → `--text` 16.29:1.

**The worst pair in the kit is `--text-dim` on the textured ground's worst dark composite =
4.78:1 (need 4.55).** That is the number the whole material decision above was tuned against.

Fill-only, for the record: `--accent` on the darkest ground stop is **1.83:1** and `--accent-2` is
**3.55:1**. Neither is a defect — the amber is the reason `--accent-ink` exists, and the blue-grey is
a plate colour.

**No carve-out is needed**, because this kit never inverts its surfaces. The recess `#c4beb0` is a
darker shade of the *same* dust rather than a dark well, so one near-black ink clears every ground it
is drawn on — which is why `--text-on-surface*` is deliberately **not declared**. The 3:1 control
boundary is also honoured where it matters most: the checkbox has no other affordance than its own
square, so its rim (#6e6656) measures 4.73:1 on the sunlit card and 3.07:1 on the darkest recess.

## Trade-offs

- **A mid-tone ground means dark-on-mid-tone throughout.** Every status colour has to be a *deep*
  mineral ink (a dark dusty green, a deep ochre, an oxide red) to clear 4.5:1 on the inset recess.
  The kit therefore cannot host a bright status chip; if you need one, put it on `--surface`.
- **Two grades of the material is more machinery than a gradient kit needs.** It costs ~34 KB of
  base64 in `tokens.css`, and it costs the author a discipline: placing the material grade where
  type sits will silently break captions. The alternative was a kit that is either flat or
  unreadable, and this one is neither.
- **The media panel shows the caster.** Its shadow is drawn *with* the boulder that throws it: a
  straight hard-stop gradient band was tried first and read, in a real 300×96 card, as a stray dark
  overlay or a broken image — a shadow with no caster, no contact line and no shape is a stripe.
  The cost is that the panel is a small scene rather than a pure swatch of texture.
- **The wheel ruts are a Signature motif rather than a component texture.** They were tried in the
  media panel alongside the boulder; at 300×96 the two reads competed and the shadow stopped being
  legible, so the panel keeps the shadow and the ruts are demonstrated in the strip. The tread
  artwork is a token, so a page can put it anywhere it earns its place.
- **No chamfer, no `--clip`.** A chamfer would cut the 2px frame along the diagonal, clip the
  zero-blur shadows that *are* this kit, and eat the focus ring. Three costs, no benefit.
- **`--radius-pill: 3px` is a deliberate break with the rest of the library.** Every other kit here
  uses `999px`; this one does not, because a capsule is the single most "software" shape there is.
  Toggle tracks, knobs, badges, dots and avatars all follow it.
- **`--check-appearance: none` means no tick mark.** A checked box is a filled amber square. That is
  the token contract's own model, and it suits a machined panel — but a consumer wanting a
  checkmark will need to draw one.
- **One honest seam, shared with the lab.** `templates/lab.css` hard-codes `border: 1px solid` on
  `.btn`, so buttons keep a 1px rim while cards, inputs, nav, badges, alerts and code blocks take the
  2px `--border-w`. Not fixable from `tokens.css`; a project using the kit directly should set it.
  The lab also fills `.card-media` with `--media-bg` at 96px tall, so the boulder field repeats
  horizontally — deliberate, and it reads as a boulder *field* rather than as a single rock.
- **The dark grade has a provable floor.** The 11% cap on the ground grade's dark elements is what
  keeps `--text-dim` above 4.55:1 even in the impossible worst case; raising it — to make the ground
  "dustier" — starts eating that margin first.

## How this kit differs from its neighbours

- **`outer-space`** (order 90, dark) is a **vista seen from nowhere**: a deep blue-violet void,
  four starfield tiles and three nebula blooms, with glassy panels floating over them and a pale
  starlight-gold *fill* whose label is the void itself. `moon-rover` has no sky, no bloom, no glass,
  no blur and no star: the ground is mid-tone and *close*, and its light comes from one low sun
  throwing a hard plate. One is awe at a distance; the other is dust at arm's length.
- **`space-noir`** (order 175, dark) is a **printed poster**: warm ink black, a drawn halftone
  screen and film grain, a burnt-orange action on near-black, hard poster frames. `space-noir` is
  *grain* (a film emulsion); `moon-rover` is *grit* (regolith with micro-shadows). Its brightest
  ground is #151311; this kit's darkest is #c4beb0, a fourteen-fold difference in the whole light
  model, and where noir's shadows are printed rules, this kit's are cast plates.
- **`cassette`** (order 110, light) is the other **light physical kit** — and the two share a
  philosophy about physicality while sharing almost nothing visually. Cassette is beige *plastic*:
  warm mid-tone ground, 4–12px moulded radii, a full-pill badge, brushed aluminium, and **depth that
  runs inwards** — every surface is *inset*, and a control is something you press into the shell.
  `moon-rover` is *mineral dust*: a cooler grey-taupe ground, 2–5px machined radii, a 3px badge, and
  **depth that runs outwards** — a hard cast plate to the lower right, because this kit's light comes
  from a sun rather than from a room. Cassette's palette is one lamp with a halo; this kit's is one
  shadow with an edge.
- **`space-program`** (the sibling half of this theme, being authored separately) is **mission
  control**: agency blue and clean, telemetry readouts and a HUD's precision. `moon-rover` is the
  ground that mission is standing on. The two are meant to be complementary and to share nothing
  visually: where the sibling is *institutional, blue and instrumented*, this one is *physical,
  dirty and lit* — where the sibling's vocabulary is a console, this one's is a footprint. If you
  are pairing them, take the sibling's blue for interface furniture and this kit's grey for anything
  that should look like it has been outside.

## When to use

Lunar, planetary and field-hardware pages; mission-ground and sample-return products; anything that
should feel like dust under one unfiltered sun rather than a view of space. It is a strong register
for hero-led marketing, dashboards for physical things (sensors, instruments, rovers, drones) and
documentation that should feel like a field manual.

**Avoid it** for anything that must look digital, glassy or cosmic — it is emphatically neither. It
is also a poor fit for very long-form reading at small sizes on the darkest grounds (a mid-tone dusty
page is a lot of page, and the ink is dark for a reason), and a project that already owns an amber
or a rust will fight it.

## Files

`DESIGN.md` (normative values) · `tokens.css` (the contract and the four drawn motifs) ·
`kit.json` (gallery metadata) · `index.html`, `DESIGN.html`, `tokens.json`, `theme.css`,
`tailwind.theme.json` (generated by `python tools/build.py --only moon-rover`).

No `kit.css`: every effect in this kit — the two texture grades, the hard cast plates, the milled
nav channel, the scooped inputs, the square controls, the boulder-and-shadow media panel — is a
token the lab already honours.

## Verify

```bash
cd H:/Work/design-kits
python tools/build.py --only moon-rover                                   # lab + exports
npx -y -p @google/design.md designmd lint kits/moon-rover/DESIGN.md      # 0 errors, 0 warnings
KIT_SHOTS="$LOCALAPPDATA/Temp/moon-rover-shots" node tools/verify-lab.cjs moon-rover   # PASS  moon-rover
python "$LOCALAPPDATA/hermes/cache/scratch/verify-moon-rover.py"         # the contrast table
```
