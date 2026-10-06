# Kaleidoscope

**Mirrored jewel facets. Symmetry instead of restraint.**

A dark kit that is deliberately multi-hue — ruby, amber, emerald, sapphire and violet — and
stays coherent because *every pattern in it is mirrored*. The library's usual rule ("one accent,
one second accent") is suspended here on purpose; the discipline moved from the palette into the
geometry. `docs/KIT-SPEC.md` says a third "look at me" colour is how kits start looking like a
rainbow. That is true, and this kit answers it rather than ignoring it: five hues are survivable
only because exactly two of them have a job and the rest are folded into patterns.

## The argument, in one paragraph

A kaleidoscope is a radial object. Its colour is not restrained; its *form* is. So the kit takes
the colour as given (five facets) and puts all the discipline in the mirror: a conic fan that
repeats its own first half back, a shard lattice that pairs 60° with 120°, a rose window that
mirrors outward from its centre, and a chamfer that cuts opposite corners rather than rounding
them. Any pattern added to this kit should be able to answer "where is your mirror?" If it can't,
it belongs to a different kit.

## Roles — which facet does what

| Facet | Token | Job |
|---|---|---|
| **Ruby** `#ff2d6f` | `--accent` | **The one facet that acts.** The single filled primary control on a screen, plus its hover, plus ruby hairlines. |
| **Sapphire** `#5b86ff` | `--accent-2` | **Cool counterweight.** Media gradient (`--accent` → `--accent-2`), progress bars, avatars, the focus ring. Never fills an action. |
| Emerald `#19dda0` | `--kaleidoscope-emerald` | structure / graphic: pattern stop, chart series, a chart-side tint. |
| Amber `#ffb020` | `--kaleidoscope-amber` | structure / graphic: the spark at the centre of the rose window, the middle of the prism ramp. |
| Violet `#a678ff` | `--kaleidoscope-violet` | structure / graphic: pattern stop, the lit facet edge, hairline tint. |

Emerald, amber and violet **never fill a control and are never used as text**. That constraint is
the whole reason five hues do not become a mess: two facets ask for attention, three are material.

## How symmetry keeps it from being a mess

Four mechanisms, all checkable in `tokens.css`:

1. **Every pattern is mirrored.** `--kaleidoscope-star` is a `repeating-conic-gradient` whose
   period is 180°, so the second half of every turn is the first half reflected. `--kaleidoscope-shard`
   lays three `repeating-linear-gradient`s at 0°, 60° and 120° — 60 and 120 are reflections of
   each other about the vertical, so the lattice is symmetric about the centre line.
   `--kaleidoscope-rose-window` is radial and built from *pairs* of the same rings.
2. **Only two facets have roles.** Fills are ruby; media is sapphire. A screen with two filled
   controls is a bug, not a variation.
3. **One geometry.** Two cuts, no curves: `--clip` (10px, two opposite corners) for controls and
   `--kaleidoscope-facet-clip` (22px, all four corners) for surfaces. Never both on one element.
4. **A near-neutral ground.** The page is a deep indigo aperture (`#191345` → `#050410`), not a
   coloured field. Facets read as light *through* glass only if the ground refuses to compete.

The type does the same job: three neutral faces (Sora / Inter / IBM Plex Mono) and no display
gimmick, so the geometry is the loudest thing on the page.

## Contrast

Verified numerically (see the log referenced below). The ground is a gradient, so the checks were
run against the **darkest stop `#050410`** *and* against the lightest stop plus the masthead's own
15% ruby wash — the masthead is where the ramp is brightest, so that is the worst real case for
dim text and for accent-coloured text.

| Pair | Ratio | Floor |
|---|---|---|
| `--text` on `--bg` (darkest stop) | 18.60:1 | 7:1 |
| `--text-muted` on `--surface` | 9.10:1 | 4.5:1 |
| `--text-invert` on `--accent` (ruby) | 5.67:1 | 4.5:1 |
| `--text-invert` on `--accent-hover` | 6.91:1 | 4.5:1 |
| `--text-dim` on `--bg` (darkest stop) | 6.75:1 | 4.55:1 |
| `--text-dim` on `--surface` | 6.04:1 | 4.55:1 |
| `--text-dim` on `--surface-2` (closest pair in the kit) | 5.26:1 | 4.55:1 |
| `--text-dim` over the masthead wash (worst ground) | 4.92:1 | 4.55:1 |
| `--accent-ink` on `--bg` / on `--surface` | 7.76:1 / 6.95:1 | 4.5:1 (small text) |
| `--accent-ink` over the masthead wash | 5.66:1 | 4.5:1 |
| `--text-invert` on the avatar/media gradient midpoint | 4.73:1 | 4.5:1 |
| status badges on `--surface-2` (ok / warn / danger / info) | 7.48 / 7.05 / 5.64 / 6.79:1 | 4.5:1 |

Two pairs *fail* and are the reason two tokens exist: white on ruby is **3.59:1** (hence the
near-black `--text-invert`) and ruby `#ff2d6f` as a small label over the masthead's own wash is
**4.14:1** (hence `--accent-ink` `#ff6f9c`).

**No `--text-on-surface*` tokens are declared, and that is a deliberate call.** Those exist for a
*three-tier stack that inverts* (a dark well inside a light shell, or the reverse). This kit's
three grounds — `--bg`, `--surface`, `--surface-2` — are all dark and within ~2.5:1 of each other
in luminance, so a single text tier clears every one of them; the one pair that is closest,
`--text-dim` on `--surface-2`, is 5.26:1. Adding overrides would be ceremony, not safety.
Stated here rather than left implicit.

## Key choices, and what they cost

- **`--surface-2` is lighter than `--surface`.** Nested panes *catch light* rather than sinking
  into a well: elevation is luminance, not distance. Cost: `--surface-2` is not usable as a
  deliberately dark inset. If you need one, use `#050410` — the darkest stop of the ground, and
  the fill of the `facet-panel` component in `DESIGN.md` — as the dark tier.
- **Surfaces are opaque, not translucent.** A glassy pane would be more on-theme, but it turns
  every contrast claim into a claim about a composite over a gradient. Opaque keeps every pair
  provable against a hex. The "glass" reading comes from the *patterns* and the lit edges
  instead.
- **The chamfer costs the border along the diagonal.** `clip-path` cuts the border with the
  shape, so the two cut edges are borderless. At `--cut: 10px` that is a thin bright sliver
  — and it is what makes the corner read as *cut stone* rather than a rounded box.
- **The chamfer also eats outer shadows and outlines.** This is worse than it sounds and it is
  documented rather than worked around: everything the lab clips — cards, buttons, inputs,
  badges, alerts, nav, code blocks — loses any outward `box-shadow`, including a focus ring.
  So `--shadow-1`, `--shadow-2` and `--glow` are **inset-first** (insets are painted inside the
  box and survive the clip), `--kaleidoscope-glint` is the outer bloom for elements you choose
  *not* to clip, and keyboard focus is carried by the sapphire border/focus-ring colour rather
  than by an outside outline.
- **`--radius-pill` is 6px, not 999px.** A 999px pill cannot survive a chamfer — the diagonal
  slices across the rounded end and produces a notched lozenge. Badges and avatars are
  chamfered chips here. Cost: no true pills and no circular avatars in this kit; that is the
  geometric vocabulary.
- **`--accent-ink` is declared, and it is not `--accent`.** `#ff2d6f` is 4.14:1 as a small label
  over the masthead's ruby wash, so text uses `#ff6f9c` (same hue, lifted) while fills use
  `#ff2d6f`. Two weights of one decision, not two accents.
- **`--text-invert` is near-black.** White on ruby is 3.59:1. The jewel is kept and the ink is
  darkened instead.
- **Status colours are off the facets by value.** Every hue family is taken, so `--ok`,
  `--warn`, `--danger` and `--info` are *duller and deeper* than the facet they resemble, and
  `--danger` is pushed to orange-red vermilion so a destructive state can never be read as the
  ruby action.

## The second, more aggressive facet clip

`--kaleidoscope-facet-clip` cuts **all four** corners at `--kaleidoscope-cut-lg: 22px`, against
the baseline `--clip` that cuts two opposite corners at 10px. It is exported for hero panels,
media frames and modal shells and applied explicitly:

```css
.hero { clip-path: var(--kaleidoscope-facet-clip); }
```

It is not in the lab's **Signature** section because the lab renders signature tokens only as a
`background` or a `box-shadow`, and a `polygon()` is neither — it would appear as an empty chip.

## Lint

`designmd lint` reports **0 errors, 0 warnings** (1 info: the token summary).

Getting there required two deliberate moves, both of which are worth knowing:

- **`button-secondary-hover` is prose, not a component entry.** DESIGN.md cannot express "label on
  a translucent tint": the linter compares the label to the raw `#ff2d6f26` tint, uncomposited, and
  reports 1.22:1. On screen the tint sits over the page ground, where `--accent-ink` measures
  6.88:1. Rather than weaken the colour to satisfy a false positive, the state is specified in
  prose and in `tokens.css` (`--accent-soft`).
- **The line and ring colours are declared as 1px fills.** `border`, `border-strong`,
  `focus-ring`, `overlay` and `accent-soft` cannot be referenced by `borderColor` (the schema has
  no such property and silently drops it), so they are carried by `divider`, `divider-strong`,
  `focus-indicator`, `overlay-scrim` and `input-ring` components instead. Same values, expressible
  vocabulary — no orphaned tokens.

`--kaleidoscope-cut-lg` and `--kaleidoscope-facet-clip` are deliberately absent from the kit.json
`signature` list: the lab renders signature tokens only as a `background` or a `box-shadow`, and a
`polygon()` is neither — it would appear as an empty chip.

## When to use it

Launch pages, game and music UI, portfolio and gallery surfaces, anything that should read as
*crafted* rather than merely dark. Do not use it for long-form reading, dense data entry, or any
form where five hues is more signal than the content deserves.

## Files

- `DESIGN.md` — normative values and rationale
- `tokens.css` — the skin (contract v1, plus the facet and pattern extras)
- `index.html` — generated component lab (`python tools/build.py`)
- `tokens.json`, `tailwind.theme.json`, `theme.css` — generated exports
