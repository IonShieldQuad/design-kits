# Gothic

**Dark feminine gothic — velvet, and something alive growing through it.** A deep plum ground, soft
ivory type, one velvet wine, a muted rose for anything you have to read, a warm **blush** that is the
candlelight bloom around the action, and a candlelight gold that earns its place as the light in the
room. A rose on a thorned stem, a lace veil, a dripping candle.

`19` · dark · `Cormorant Garamond · Lora · Roboto Mono` · source: original

## Stance

This kit was **re-registered**. It used to be *industrial starkness*: coal near-black, bone white,
one deep blood red, Oswald — a heavy condensed grotesque off a hardcore flyer — and hard 0–3px
corners. That was a coherent kit and it was deliberately rejected for this one. The register asked
for now is **witches, vampires, dark romance**, and the old one fought that register on three fronts
at once: the ground was neutral (not plum), the corners were sharp (not velvet), and above all the
**display face was the letterform of an agitprop poster, not a novel cover**. Every one of those is
reversed here.

What is *kept* is the thing that was never register-specific: **something alive growing through it**.
Thorns and roses suit a witch's garden as well as a black wall, so they stay — but they turned
rose-forward. The trellis became a **bloom on a stem**, the barbed fence became a **lace veil**, and
a **dripping candle** joined to light the room. It is still unmistakably dark; it is simply no longer
industrial.

The structure is soft now. Velvet plum ground (`#130b12`, a violet cast, never charcoal), ivory text
(`#f4ebe6` — bone, not pure white), a single wine (`#8f1d3f`) for the thing that acts, a muted rose
(`#e08ba6`) for the thing that is *read*, a warm **blush** (`#e3737d`) that is the bloom around the
action, and 5–16px corners with a true pill. Cormorant Garamond sets anything that speaks; Lora
carries the body quietly; Roboto Mono is the one machine voice left.

Use it for **dark romance, beauty and fashion editorial, nightlife, witchy or vampire branding, and
music**. It is a poor fit for anything that has to look friendly, safe or corporate — that is the
point of it.

At 200×120 it is unmistakable: **velvet plum, ivory and wine**, a rose in one corner and a candle in
the other. It is the only kit in the dark column that lives in the **red-plum** family (Cyberpunk is
violet-black and neon, Outer Space is blue-violet and gold, Inside the Machine is warm graphite and
amber) and the only one with a flower growing in it.

## Ground truth

Every value below is authored for this kit; nothing is inherited from another kit's palette.

| Token | Value | Note |
|---|---|---|
| `--bg` | `linear-gradient(180deg, #1a1019 0px, #130b12 320px, #0e0810 100%)` | velvet. Brightest stop `#1a1019` is the binding ground |
| `--bg-2` | `#130b12` | dominant stop / masthead floor |
| `--surface` | `#1f1420` | panel |
| `--surface-2` | `#28192a` | inset well, inputs, badges — the lightest dark |
| `--overlay` | `rgba(12,6,11,.82)` | modal scrim |
| `--text` | `#f4ebe6` | ivory — 15.79:1 on the top `--bg` stop |
| `--text-muted` | `#cdb6bf` | dusty mauve — 8.74:1 on `--surface-2` |
| `--text-dim` | `#b095a2` | mauve dust — 6.07 / 6.50 / 6.77 on surface-2 / surface / bg-top |
| `--text-invert` | `#f7ece8` | ivory ink on the wine plate — 7.50:1 |
| `--accent` | `#8f1d3f` | deep velvet wine — the only action colour |
| `--accent-hover` | `#ab2549` | the same wine warmed |
| `--accent-2` | `#c99a4e` | candlelight gold — the light in the room |
| `--accent-soft` | `rgba(143,29,63,.18)` | 18% wine tint, derived from `--accent` |
| `--accent-ink` | `#e08ba6` | muted rose as TEXT — 7.43:1 on `--bg`, 6.15:1 on tint over `--surface-2` |
| `--accent-ink-hover` | `#f0a6bc` | the rose lifted |
| `--blush` | `#e3737d` | warm rose — a **first-class accent** (the glow bloom + the media veil's heart); never a fault |
| `--ok` | `#8fb073` | muted sage |
| `--warn` | `#d9a94f` | candlelight amber |
| `--danger` | `#e0655a` | a true **warning red** — hot and red, clearly not the wine |
| `--info` | `#93a9c6` | moonlight blue |
| `--border` | `rgba(244,235,230,.14)` | the ivory hairline |
| `--border-strong` | `rgba(244,235,230,.30)` | input rim / emphasised rule |
| `--border-w` | `1px` | a fine lace hairline, not a slab |
| `--focus-ring` | `#e08ba6` | the rose — two steps lighter than the wine action |
| `--radius-sm/md/lg` | `5px` / `9px` / `16px` | velvet curve |
| `--radius-pill` | `999px` | a true lozenge — badges are pills, avatars are circles |
| `--cut` | `0px` | no chamfer; that is Cyber-angel's signature |
| `--shadow-1` | inset ivory rim + `0 10px 26px -16px` falloff | a panel resting on velvet |
| `--shadow-2` | inset rim + `0 24px 52px -24px` + `0 0 0 1px rgba(143,29,63,.22)` | the raised panel, with the wine thread |
| `--glow` | `0 0 0 1px rgba(143,29,63,.55), 0 0 24px -4px rgba(227,115,125,.50)` | a real candlelight bloom — in the **blush**, not wine |
| `--blur` | `none` | velvet is opaque, not frosted glass |

Optional capabilities declared: `--accent-ink`, `--accent-ink-hover`, `--wash`, `--media-bg`,
`--media-op`, `--fill-bg`, `--input-inset`.

## The three motifs (and the one texture)

| Token | What it is | Job | How it is built |
|---|---|---|---|
| `--gothic-rose` | a rose bloom on a thorned stem | the **mark** — something alive | drawn SVG (base64): three rings of closed, overlapping petals (6 / 5 / 3) with visible edges, filled so each ring occludes the one behind it, a furled bud spiralling inside, on a wine stem with a leaf |
| `--gothic-lace` | a lace veil | the **fabric** — a repeatable field | drawn SVG, fine netting + a four-petal flower, hearted by a rose dot |
| `--gothic-candle` | a dripping candle | the **light** — the gold's job | drawn SVG, lit pillar with wax running down both flanks |
| `--gothic-wine` | the accent as a surface | texture (not a motif) | a 4-stop velvet drape |

**Four tokens, three ideas.** A fourth *motif* beyond rose/lace/candle is out of scope — the three
already do three different jobs (mark, fabric, light) and a decorative fourth only dilutes them.
`--gothic-wine` is the accent as a surface, not a motif.

A fifth tile, `--gothic-vein` — a wine → rose → candle hairline — was **cut in review**. Rendered at
168×72 it was a plum → magenta → **orange** → gold → **yellow** horizontal band: a sunset/aurora ramp
that carried two hues the kit owns nowhere else, with no material cue for anything at all. Re-hueing
it would only have re-made the lace, so it was removed. It is the one edit of the three that is a
deletion rather than a redraw.

### Each motif is proofed non-flat on the tile, not just on the page

The single most-repeated defect in this library is a motif tuned for subtlety that renders as a flat
plate at chip size. So each token was rendered and measured **on the lab's own signature tile** — the
built `index.html`'s 168×72 `.chip` over `--surface-2` — screenshotted headless and measured with
PIL. Reported as the standard deviation of luminance across the tile (`0` would be a flat plate):

| Token | luminance std-dev (lab tile) | per-channel RGB std-dev | verdict |
|---|---|---|---|
| `--gothic-rose` | **24.0** | 41.0 / 19.4 / 23.7 | a solid layered bloom + stem, clearly not flat |
| `--gothic-lace` | **36.4** | 38.4 / 36.1 / 34.3 | a lattice, clearly not flat |
| `--gothic-candle` | **53.2** | 54.8 / 53.3 / 47.7 | a solid form + flame, clearly not flat |

The supporting texture clears it too (`--gothic-wine` 10.3) — not a flat plate — but its
non-flatness is a smooth gradient, not the failure mode this check exists for. (`--media-bg` also
measures 30.0, for reference.)

### The motifs were settled by looking — the rose took four attempts

- The **candle** failed once and was redrawn: it first shipped with a large warm halo behind the
  flame, which read as a **bullseye / eye** and as a flat column body. The halo is gone (warmth now
  lives in the flame core) and the wax runs down both flanks and pools at the foot, so it reads as
  *dripping*, not just lit.
- The **rose took four attempts, and two of them failed in review.** Version 1 was a nested/looped
  head — a **bullseye**; a bright heart in the middle then read as an **eye**. Version 2 was a single
  **asymmetric spiral**: it survived the arithmetic (a real, non-flat tile) but a cold reviewer read
  it as a **spiral / rosette / target / vinyl groove** — it "only read because it was labelled".
  The rule that came out of that: *a rose needs petal **divisions**, and outlines alone tangle.*
  Versions 3–4 were built as **closed, filled, overlapping petals** — occlusion gives clean petal
  edges where outline-only petals give a tangle — with a furled bud inside and a thorned stem.
- The shipped mark was re-rendered on the lab's own 168×72 `.chip` and graded **cold, with no
  label**. The verdict: *"it looks like a rose … 85–90% confidence"*, nothing clipped at the tile
  edges. That is the bar it had to clear, and it is the reason this token was redrawn rather than
  filed as good-enough.

The motifs are the one part of this kit that cannot be settled by arithmetic, so they are settled by
looking — and the rose is settled by looking *and being told nothing*.

## Type: why these three

- **Cormorant Garamond — display and headings.** A romantic, high-contrast old-style serif with fine
  hairlines and a calligraphic italic — the face of a dark-romance cover. It replaces Oswald
  (a heavy condensed grotesque), and that swap *is* the register change: a condensed grotesque is
  the letterform of a flyer or a stencil, and no amount of plum will make it romantic.
- **Lora — body.** A contemporary serif drawn for reading, with a brushed calligraphic warmth and a
  sturdy skeleton at 15px. It shares Cormorant's old-style proportions, and its lower contrast means
  it **supports the display quietly** instead of competing with Cormorant's hairlines. It never sets
  a title.
- **Roboto Mono — labels.** Eyebrows, badges, table headers, metadata, hints. The kit's one machine
  voice — a catalogue number on a reliquary. Caps labels run `+0.20em`.
- **Display tracking is `-0.01em`** — a touch only. Cormorant is a narrow old-style; the usual
  `-0.02em` display tightening begins to touch its fine joins at 2.9rem.

## Derived, and why

- `--accent-hover: #ab2549` — one visible step up in lightness from `#8f1d3f`, same hue. The wine
  warms; it never changes colour.
- `--accent-soft: rgba(143,29,63,.18)` — an 18% tint of `--accent`, written as `rgba()` rather than
  re-typed as a hex, because it is derivable and must stay in sync with the wine.
- `--accent-ink: #e08ba6` — the text-safe member of the wine family. This is the derivation the
  contrast numbers forced: `#8f1d3f` is **2.13:1** against the ground, so the deep wine cannot carry
  small type. The muted rose at 7.43:1 can, and it happens to be the rose motif's own colour — the
  link colour and the flower are the same substance.
- `--blush: #e3737d` — the palette's **warmth**, promoted in review out of `--danger`. It is the
  colour of the candlelight halo `--glow` casts around the primary action and of the heart of the
  `--media-bg` veil ramp. It is derived from nothing — it is the one hue the kit *chose* — and its
  6.20:1 on the ground is never spent as ink, only as bloom.
- `--danger: #e0655a` — a true warning **red**, deliberately hotter and redder than the wine.
  "Delete" must never read as "the action"; since review it must never read as the blush either,
  which is why the fault is a red and not a pink (the price is 4.89:1 on its own badge plate —
  the kit's tightest number). It is a *coral-leaning* red by necessity, not by choice: on a dark
  ground, saturation costs luminance, and a purer, hue-0 red at this lightness measures only
  4.03–4.37:1 on `--surface-2` — it would fail. `#e0655a` is the reddest value that clears the bar
  on the lightest dark the kit owns, and it is clearly distinct from the amber `--warn`.
- `--text-invert: #f7ece8` (ivory, not near-black). A deep wine is deep enough to hold light ink
  (7.50:1), so the primary button keeps an ivory label — the inverse of a bright-accent dark kit.
- `--accent-2: #c99a4e` (candlelight gold) — promoted to a real job rather than decoration: the
  candle flame, the lit end of the media ramp, and the gold half of the masthead candle glow.
- `--border` / `--border-strong` are **translucent ivory**, not opaque steel and not a tinted hue:
  the hairline is the edge of a lace veil on velvet.
- `--radius-pill: 999px` — a true lozenge, and a deliberate reversal of the old kit's `3px` stamped
  plate. It makes badges lozenges and `.avatar` a **circle** of ivory initials (the cameo read).

## Contrast (verified numerically, not by eye)

Computed from `tokens.css` by script — WCAG relative-luminance ratio, `(Lhi + .05) / (Llo + .05)`.
Translucent grounds are **composited** before grading (a badge's rose label is measured against its
18% wine tint over the surface, and the masthead's ivory/rose labels against the `--wash` bloom
over the top bg stop).

| Pair | Ratio | Target | |
|---|---|---|---|
| `--text` on `--bg` (top stop) | **15.79:1** | ≥ 7 | ✓ |
| `--text` on `--surface-2` | **14.15:1** | ≥ 7 | ✓ |
| `--text-muted` on `--surface-2` | **8.74:1** | ≥ 4.5 | ✓ |
| `--text-invert` on `--accent` | **7.50:1** | ≥ 4.5 | ✓ |
| `--text-invert` on `--accent-hover` | **5.86:1** | ≥ 4.5 | ✓ |
| `--text-dim` on `--bg` (top stop) | **6.77:1** | ≥ 4.55 | ✓ |
| `--text-dim` on `--surface` | **6.50:1** | ≥ 4.55 | ✓ |
| `--text-dim` on `--surface-2` | **6.07:1** | ≥ 4.55 | ✓ |
| `--text-dim` on `--wash` composite (masthead) | **5.34:1** | ≥ 4.55 | ✓ |
| `--accent-ink` on `--bg` (top stop) | **7.43:1** | ≥ 4.5 | ✓ |
| `--accent-ink` on accent-soft over `--surface-2` | **6.15:1** | ≥ 4.5 | ✓ |
| `--accent-ink` on accent-soft over `--surface` | **6.57:1** | ≥ 4.5 | ✓ |
| `--accent-ink` on `--wash` composite | **5.86:1** | ≥ 4.5 | ✓ |
| `--danger` on `--surface-2` (the danger badge's plate) | **4.89:1** | ≥ 4.5 | ✓ |
| `--danger` on `--surface` | **5.24:1** | ≥ 4.5 | ✓ |
| `--danger` on `--bg` (top stop) | **5.46:1** | ≥ 4.5 | ✓ |
| `--ok` / `--warn` / `--info` on `--surface` | 7.31 / 8.26 / 7.40:1 | ≥ 4.5 | ✓ |
| `--focus-ring` on `--bg` | **7.43:1** | ≥ 3 | ✓ |

The **blush** is *not* a text or status ink, so it carries no target — it renders only inside
`--glow` (a `box-shadow`) and as the heart of the `--media-bg` ramp. For reference it sits at
**6.20:1** on the top `--bg` stop and **5.56:1** on `--surface-2`.

**Worst pair: `--danger` (the warning red, `#e0655a`) on its own `--surface-2` badge plate at
4.89:1** — target 4.5. Moving the blush out of `--danger` is what produced the kit's tightest
number: a fault colour that is *lighter* than this stops reading as red, and one that is *darker*
stops clearing 4.5:1 on the lightest dark the kit owns. 4.89:1 is the honest price of a real red
here. Second-tightest, and the binding number for the whole text tiers, is `--text-dim` (mauve dust,
`#b095a2`) on the masthead `--wash` composite (≈`#3c2124`) at 5.34:1 (target 4.55); on a *solid*
ground the same token's worst is 6.07:1 on `--surface-2`, which is the lightest dark the kit owns
and the binding ground for a dark kit.

`--border` / `--border-strong` sit at ~1.4–2.6:1 by design — decorative seams that never carry
meaning alone. `--accent` itself is 2.13:1 on the ground, which is exactly why it is never used as
text (it is a fill only; `--accent-ink` is the text member).

**No contrast carve-out is needed.** All three surfaces are dark and share one polarity, so a single
`--text` / `--text-muted` / `--text-dim` family carries all three tiers and the kit does **not**
declare `--text-on-surface*` / `--text-on-surface-2*`. Those exist for the inverted tier (a dark
well inside a light shell); there is no inversion here, so declaring them would be noise.

## Trade-offs

- **A deep accent is a contrast liability as text, and the kit pays for it twice.** `#8f1d3f` is
  2.13:1 on the ground, so *every* wine that has to be read — links, eyebrows, active nav, inline
  code, badge labels, secondary-button labels — is the muted rose (`--accent-ink`, `#e08ba6`)
  instead. Two members of the wine family is the price of a deep wine; the alternative was a neon
  one, which was refused. The upside is a wine plate that takes ivory ink at 7.50:1.
- **A serif body is a UI body.** Lora at 15px is a reading face, and it sets buttons and labels as
  well as paragraphs because the lab inherits `--font-body` there. That is deliberate — running the
  chrome in the same serif is what makes the whole page read as *romantic* rather than as a dark
  dashboard with a fancy title — but it is a decision a reader should know was made, not an
  accident.
- **The gold had to be given a job or dropped.** "Do not add a colour for decoration" is the rule,
  so candlelight gold is the candle motif's flame, the lit end of the media ramp, and the gold half
  of the masthead glow. It is never an action fill. If the candle were removed the kit would need
  the gold removed with it.
- **The blush was rescued from `--danger` and given a job.** Review found the palette's one blush
  filed as "error": the softest, most romantic colour on the page meant *failed*. `--danger` is now a
  true warning red (`#e0655a`) and the blush (`#e3737d`) is a first-class accent in the **bloom
  family** — the halo `--glow` casts around the primary action, and the heart of the `--media-bg`
  veil ramp (which also retired the last off-palette hex, a stray magenta, from that ramp). The soft
  pink is now warmth, and nothing soft means "failed" any more.
- **The media ramp is now wine → blush → candlelight, and every stop is a palette colour.** Before,
  it was wine → *magenta* → candle, and the magenta was not in the palette at all; `card-media` /
  `card-media-2` still declare `primary` / `secondary` because those are the ramp's two *endpoints*,
  and the blush is what renders in its heart. A pink-into-candlelight ramp necessarily warms through
  a lit amber on the way; that is the gold heating the veil, and — unlike the cut tile — it sits
  *under the lace*, which is the material cue the tile never had.
- **The rose and the candle each shipped a bug on the first try** (a bullseye/eye rose, an
  eyelike-halo candle), and the rose then shipped a *second* bug that arithmetic could not catch: a
  clean spiral that was non-flat, contrast-safe, and still read as a **rosette** rather than a rose.
  All three were redrawn. Documented above under the motifs, because "look at the tiles, cold" is
  the check that catches this.
- **One DESIGN.md linter warning is kept on purpose:** `orphaned-tokens: 'blush' is defined but
  never referenced by any component`. The blush *does* render — in `--glow` and in `--media-bg` — but
  the DESIGN.md component schema has no `boxShadow` or `backgroundImage` property, so a colour whose
  entire job is a bloom and a gradient mid-stop cannot be pointed at from a component. Same reason
  `--glow`, `--border` and `--accent-soft` are described in prose. It is accepted, not accidental.
- **Four signature tokens is the budget.** They are all used; none is filler. The fifth was cut in
  review (see the motifs), which is the cheapest possible way to strengthen the remaining three.
- **The kit is a bad fit for anything friendly.** Wine and rose on plum is not a neutral palette;
  using it for a healthcare product or a kids' app would be a category error.

## Files

`DESIGN.md` (normative values) · `tokens.css` (the contract) · `kit.json` (gallery metadata) ·
`index.html`, `DESIGN.html`, `tokens.json`, `tailwind.theme.json`, `theme.css` (generated by
`python tools/build.py --only gothic`).
