# Gothic

**Dark feminine gothic — velvet, and something alive growing through it.** A deep plum ground, soft
ivory type, one velvet wine, a muted rose for anything you have to read, and a candlelight gold that
earns its place as the light in the room. A rose on a thorned stem, a lace veil, a dripping candle.

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
(`#e08ba6`) for the thing that is *read*, and 3–14px corners with a true pill. Cormorant Garamond
sets anything that speaks; Lora carries the body quietly; Roboto Mono is the one machine voice left.

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
| `--accent-ink` | `#e08ba6` | muted rose as TEXT — 7.43:1 on `--bg`, 6.13:1 on tint over `--surface-2` |
| `--accent-ink-hover` | `#f0a6bc` | the rose lifted |
| `--ok` | `#8fb073` | muted sage |
| `--warn` | `#d9a94f` | candlelight amber |
| `--danger` | `#e3737d` | dusty-rose fault — lighter/hotter than the wine |
| `--info` | `#93a9c6` | moonlight blue |
| `--border` | `rgba(244,235,230,.14)` | the ivory hairline |
| `--border-strong` | `rgba(244,235,230,.30)` | input rim / emphasised rule |
| `--border-w` | `1px` | a fine lace hairline, not a slab |
| `--focus-ring` | `#e08ba6` | the rose — two steps lighter than the wine action |
| `--radius-sm/md/lg` | `3px` / `7px` / `14px` | velvet curve |
| `--radius-pill` | `999px` | a true lozenge — badges are pills, avatars are circles |
| `--cut` | `0px` | no chamfer; that is Cyber-angel's signature |
| `--shadow-1` | inset ivory rim + `0 10px 26px -16px` falloff | a panel resting on velvet |
| `--shadow-2` | inset rim + `0 24px 52px -24px` + `0 0 0 1px rgba(143,29,63,.22)` | the raised panel, with the wine thread |
| `--glow` | `0 0 0 1px rgba(143,29,63,.55), 0 0 24px -4px rgba(224,139,166,.45)` | a real candlelight bloom — in **rose**, not wine |
| `--blur` | `none` | velvet is opaque, not frosted glass |

Optional capabilities declared: `--accent-ink`, `--accent-ink-hover`, `--wash`, `--media-bg`,
`--media-op`, `--fill-bg`, `--input-inset`.

## The three motifs (and the two textures)

| Token | What it is | Job | How it is built |
|---|---|---|---|
| `--gothic-rose` | a rose head on a thorned stem | the **mark** — something alive | drawn SVG (base64), asymmetric spiral in three outer petals + wine thorns, over a plum bloom |
| `--gothic-lace` | a lace veil | the **fabric** — a repeatable field | drawn SVG, fine netting + a four-petal flower, hearted by a rose dot |
| `--gothic-candle` | a dripping candle | the **light** — the gold's job | drawn SVG, lit pillar with wax running down both flanks |
| `--gothic-wine` | the accent as a surface | texture | a 4-stop velvet drape |
| `--gothic-vein` | one hairline rule | texture | wine → rose → candle → rose → wine |

**Five tokens, three ideas.** A third *motif* beyond rose/lace/candle is explicitly out of scope —
the three already do three different jobs (mark, fabric, light), and a fourth would dilute them.
`--gothic-wine` and `--gothic-vein` are light and line, not motifs.

### Each motif is proofed non-flat on the tile, not just on the page

The single most-repeated defect in this library is a motif tuned for subtlety that renders as a flat
plate at chip size. So each token was rendered and measured **on the lab's own signature tile** — the
built `index.html`'s 168×72 `.chip` over `--surface-2` — screenshotted headless and measured with
PIL. Reported as the standard deviation of luminance across the tile (`0` would be a flat plate):

| Token | luminance std-dev (lab tile) | per-channel RGB std-dev | verdict |
|---|---|---|---|
| `--gothic-rose` | **27.1** | 37.6 / 24.2 / 27.2 | line art, clearly not flat |
| `--gothic-lace` | **32.8** | 35.7 / 33.3 / 31.8 | a lattice, clearly not flat |
| `--gothic-candle` | **52.1** | 53.7 / 52.3 / 46.8 | a solid form + flame, clearly not flat |

The two supporting textures clear it too (`--gothic-wine` 11.7, `--gothic-vein` 46.3) — neither is
a flat plate — but their non-flatness is a gradient, not the failure mode this check exists for.

### The motifs were settled by looking, three times

Both the rose and the candle failed a first rendering and were redrawn:

- The **rose** first shipped as a nested/looped head and read as a **bullseye**, and any attempt to
  put a bright heart in the middle read as an **eye** (a pinprick at the centre of a dark disc is a
  catchlight). The shipped version is a single **asymmetric spiral** off-centre inside three uneven
  petals; the stem and thorns disambiguate it firmly as botanical.
- The **candle** first shipped with a large warm halo behind the flame, which read as a **bullseye /
  eye** and as a flat column body. The halo is gone (warmth now lives in the flame core) and the wax
  now runs down both flanks and pools at the foot, so it reads as *dripping*, not just lit.

Both were re-rendered and re-checked at chip size before shipping. The motifs are the one part of
this kit that could not be settled by arithmetic, so they were settled by looking.

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
- `--danger: #e3737d` — deliberately **lighter and hotter** than the wine. "Delete" must never read
  as "the action".
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
16–18% wine tint over the surface, and the masthead's ivory/rose labels against the `--wash` bloom
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
| `--accent-ink` on accent-soft over `--surface-2` | **6.13:1** | ≥ 4.5 | ✓ |
| `--accent-ink` on accent-soft over `--surface` | **6.55:1** | ≥ 4.5 | ✓ |
| `--accent-ink` on `--wash` composite | **5.86:1** | ≥ 4.5 | ✓ |
| `--danger` on `--bg` (top stop) | **6.20:1** | ≥ 4.5 | ✓ |
| `--ok` / `--warn` / `--info` on `--surface` | 7.31 / 8.26 / 7.40:1 | ≥ 4.5 | ✓ |
| `--focus-ring` on `--bg` | **7.43:1** | ≥ 3 | ✓ |

**Worst pair: `--text-dim` (mauve dust, `#b095a2`) on the masthead `--wash` composite
(≈`#3c2124`, the candle glow over the top bg stop) at 5.34:1** — target 4.55. On a *solid* ground
the worst is the same token on `--surface-2` at 6.07:1. The dim tier is deliberately not moodier
and darker than this: `--surface-2` is the lightest dark the kit owns, and it is the binding ground
for a dark kit.

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
- **The media panel declares `primary` and `secondary` because those are what actually render.**
  `--media-bg` is the lace veil over a wine→rose→candle ramp, whose endpoints are `#8f1d3f` and
  `#c99a4e` — so `card-media` / `card-media-2` describe the ramp's two ends honestly rather than
  pointing at colours that never appear.
- **The rose and the candle each shipped a bug on the first try** (a bullseye/eye rose, an
  eyelike-halo candle) and were redrawn. Documented above under the motifs, because "look at the
  tiles" is the check that catches this and arithmetic cannot.
- **Five signature tokens is the budget.** They are all used; none is filler. `--gothic-vein` is the
  weakest as a *tile* (a horizontal hairline rendered 72px tall reads as a band) but the strongest
  as an actual export.
- **The kit is a bad fit for anything friendly.** Wine and rose on plum is not a neutral palette;
  using it for a healthcare product or a kids' app would be a category error.

## Files

`DESIGN.md` (normative values) · `tokens.css` (the contract) · `kit.json` (gallery metadata) ·
`index.html`, `tokens.json`, `tailwind.theme.json`, `theme.css` (generated by
`python tools/build.py`).
