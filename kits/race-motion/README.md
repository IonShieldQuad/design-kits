# Race Motion

**Motorsport as broadcast.** Asphalt under lights, kerbs at the edge of the frame, a chequered
flag across it, and a display face that leans forward. Loud, fast and precise — the overlay, not
the showroom.

- Kit: `race-motion` · order `155` · mode `dark`
- Fonts: Saira (display, **italic**) · Inter (body) · JetBrains Mono (timing)
- Tags: `dark` `sport` `motorsport` `bold` `geometric` `high-contrast`
- Source: **original** — no reference images were sampled. Every value below was chosen for the
  register and then measured, not derived from a supplied file.
- Signature motifs: `--race-motion-chequer` · `--race-motion-kerb` · `--race-motion-slipstream`

## The register: asphalt, and why

The brief offered two registers — bodywork **white** (light) or asphalt **charcoal** (dark) — with
one signal yellow doing a single job either way. This kit takes **asphalt**, mode `dark`:

1. **It is the difference between a race and a car.** White ground + black type + a red accent is
   what every marque site already looks like; the brief asks for the energy of a race *broadcast*,
   and the broadcast is run at night, on tarmac. A light kit would have been a car brand.
2. **Both motifs need a dark ground.** A kerb is red *and* white; a chequered flag is black *and*
   white. On a white page, half of each motif disappears. The two devices the kit is built on only
   work against asphalt.
3. **The lighting is directional.** `--bg` is lit from the top of the frame and settles toward
   near-black down the page, which is a broadcast frame. A flat white page cannot model it.

The one **signal yellow** (`#ffd23f`) does exactly one job: *caution*. It is `tertiary`, it is
`--warn`, and it is the caution badge — and it never becomes a control colour or a second accent.

## Contrast — measured, not eyeballed

Grades are computed on the declared values and on **composited** translucent grounds
(`--accent-soft` over each surface). The binding ground for a dark kit is its **brightest** stop;
here that is `--surface-2` `#262a31`, not the page ground.

| Pair | Ratio | Ground | Target |
|---|---|---|---|
| `--text` on `--surface-2` (brightest ground) | 13.28:1 | `#262a31` | ≥ 7 ✓ |
| `--text` on `--bg` top stop | 13.44:1 | `#26292f` | ≥ 7 ✓ |
| `--text-muted` on `--surface-2` | 8.10:1 | `#262a31` | ≥ 4.5 ✓ |
| **`--text-dim` on `--surface-2`** (the binding dim pair) | **6.00:1** | `#262a31` | ≥ 4.55 ✓ |
| `--text-dim` on `--bg` top stop | 6.07:1 | `#26292f` | ≥ 4.55 ✓ |
| `--accent-ink` on `--surface-2` | 5.66:1 | `#262a31` | ≥ 4.5 ✓ |
| `--accent-ink` on `--accent-soft` over `--surface-2` (the badge) | 5.40:1 | composite | ≥ 4.5 ✓ |
| `--text-invert` on `--accent` | 5.46:1 | `#d40a00` | ≥ 4.5 ✓ |
| `--text-invert` on `--accent-hover` | 4.97:1 | `#e10600` | ≥ 4.5 ✓ |
| `--ok` on `--surface-2` | 8.07:1 | `#262a31` | ≥ 4.5 ✓ |
| `--warn` on `--surface-2` | 9.97:1 | `#262a31` | ≥ 4.5 ✓ |
| `--danger` on `--surface-2` | 4.89:1 | `#262a31` | ≥ 4.5 ✓ |
| `--info` on `--surface-2` | 5.25:1 | `#262a31` | ≥ 4.5 ✓ |
| `--focus-ring` on `--surface-2` | 12.34:1 | `#262a31` | ≥ 3 ✓ |
| `--focus-ring` on `--accent` (a white ring on the red fill) | 4.68:1 | `#d40a00` | ≥ 3 ✓ |

**Worst pair, overall: `--accent-ink` at 4.83:1** on the masthead's most-stressed composite ground
— the top `--bg` stop `#26292f` with both a white speed streak *and* the 20% red brake-glow over
it. The eyebrow lives on that wash, so it was graded there rather than on the bare stop (where it
is 5.73:1). **Worst pair on a flat ground: `--danger` at 4.89:1 on `--surface-2` `#262a31`.**
`tools/verify-lab.cjs`, sampling the actual rendered pixels, reports the worst *live* pair as
`--accent-ink` **5.93:1** on `.eyebrow` at 12px — the brake-glow wash simply does not reach the
text column, which is why the red was pushed right of it.

Two inks were lifted to clear these: `--text-dim` to `#a0a8b3` and `--accent-ink` to `#ff7a6d`,
and the wash's red was pulled back from 30% to 20% and pushed to the right of the text column.

Note the deliberate split: the red **fill** `#d40a00` is only 3.55:1 as a small label, so text-red
ships separately as `--accent-ink` `#ff7a6d`. Every link, eyebrow, active tab and badge label goes
through it.

## The three motifs

Each does a different job, and each was rendered as a `background:` on a 168×72 box on the tile
base `--surface-2`, screenshotted, and graded by per-tile pixel standard deviation (PIL):

| Token | Job | Non-flatness (std dev, 168×72) |
|---|---|---|
| `--race-motion-chequer` | identity — the finish flag | **110.84** |
| `--race-motion-kerb` | limit — the track edge | **108.53** |
| `--race-motion-slipstream` | motion — the media panel | **67.39** |

- **Chequer** — a true two-tone checker: `repeating-conic-gradient(#f2f5f8 0% 25%, #14171b 0%
  50%)` with `background-size: 1.5rem 1.5rem`, i.e. a 2×2 block per period and exactly **12px**
  squares. Crisp by construction (hard stops only). It is sized in `rem`, not `px`, on purpose: the
  build's swatch normaliser rewrites any `NNpx` gradient inside a single paren pair into smooth `%`
  stops, which would melt the checker into a conic swirl. Verified sharp, not blurred.
- **Kerb** — hard-banded red/white at −52°, 1rem bands, both stops sharing a position at every
  seam. Never a smooth ramp.
- **Slipstream** — **drawn** (inline SVG, base64). Tapering wedges that converge on the vanish
  point where the car has just passed, a bright core streak and a flare, drawn at 480×160 and
  scaled with `cover`. Two parallel repeating gradients gave flat wallpaper, not perspective (the
  first attempt measured 22.9 and read muddy); the convergence is real structure, so it is drawn.
  This is what `--media-bg` paints, so a media panel shows motion rather than the lab's default
  flat accent ramp.

## Type

Saira is the display face and is set **italic** — the register is a broadcast graphic and a
broadcast graphic leans forward. It was chosen over the other candidates in the brief because
**Chakra Petch has no italic at all**, and **Archivo**'s italic, while real, is a neutral grotesque
— Saira's slightly squared, technical italic *is* the sports-graphics voice. Inter keeps the body
legible in quantity where a display face does not, and JetBrains Mono is the timing tower: labels,
metrics and code, set wide in caps so small labels read as graphics.

The italic is a **token** (`--style-display: italic`), not a stylesheet: the lab gained the token
after this kit was authored with a `kit.css` for the same job. The contract names a font *family*
and never its *style*, which is exactly the kind of gap that should be a contract token rather than
a per-kit fork.

## No `kit.css`

This kit shipped with one and no longer has one. Both rules it contained were **missing contract
tokens**, so the lab was fixed and the file deleted:

1. **Italic display voice → `--style-display`.** `templates/lab.css` set no `font-style` and the
   contract had no font-style token, so a register that leans forward had no way to say so. The lab
   now binds the display selectors to `var(--style-display, normal)`.
2. **Focus that survives the chamfer → `--focus-inset`.** The kit opts into `--clip`, and
   `clip-path` clips `outline` along with the pixels — so the lab's own focus ring was cut away and
   a clipped control had **no** keyboard focus indicator. The lab now accepts an inset ring
   (`inset 0 0 0 var(--focus-inset, 0) var(--focus-ring)`), which paints inside the silhouette where
   the chamfer cannot reach. Inputs already keep a focus indicator via the border-colour change.

## Trade-offs, stated honestly

- **The two `clip-path` caveats apply.** (1) `clip-path` also cuts the **border** along the
  diagonal, so a chamfered edge is borderless — the 2px rule shows only on the straight edges.
  (2) It clips **`box-shadow`** (and `outline`), so `--shadow-1/2` and `--glow` read as *subtle*
  on clipped plates — though the keyboard focus ring no longer does, because it is inset. This is documented in `docs/KIT-SPEC.md` as a limitation, not a bug, and it
  suits a flat broadcast overlay — the chamfer and the hard bands carry the depth. `--glow` is
  still declared because the lab wires `.btn-primary` to it and unclipped chrome shows it.
- **The slipstream is a motif, not a photograph.** It reads as speed streaks with perspective; it
  is stylised broadcast iconography, not a rendered 3D trail.
- **`--accent-2` is bodywork white, not a third brand colour.** It is a media/fill accent. It is
  never used as text (that is `--accent-ink`) and never as a control fill.
- **Two accents is the ceiling.** The genre tempts a third neon; the signal yellow is deliberately
  restricted to caution so a "failed" badge can never read as the brand red.
- **No `--text-on-surface*` tokens.** The kit is a single dark family — `--surface` and
  `--surface-2` are both darker than the page's brightest stop — so `--text`/`--text-muted` remain
  legible on both tiers and no paired per-surface ink is needed (the three-tier carve-out does not
  apply here).

## When to use

Speed, sport and competition: race and esports coverage, motorsport team and event pages, timing
and telemetry dashboards, launch pages that need to feel loud and precise. Avoid it for anything
that must feel calm, clinical or trustworthy-at-9am — that is `quiet`, `glass` or `carbon`. For
the same decade in daylight, use `summer-sunset`; for hardware rather than momentum, `cassette`.
