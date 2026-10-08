# Tropical Breeze

A warm coastal holiday. Mid-afternoon on a beach: dry sand underfoot, the sea in front of it, a
palm leaning in from the corner, one low sun. The palette is **sand and sea-foam, sea turquoise,
palm green, and exactly one coral pop** — airy, fresh and saturated, but never neon.

- **Mode:** light · **Order:** 145
- **Fonts:** Baloo 2 (display) · Nunito (body) · DM Mono (labels, code)
- **Signature motifs:** `--tropical-breeze-frond`, `--tropical-breeze-wave`, `--tropical-breeze-parasol`
- **Files:** `tokens.css`, `DESIGN.md`, `kit.json`, `README.md`. No `kit.css` — every visual
  difference here is carried by tokens.

## Stance

This is a kit for the *warm, playful* register: a holiday, a travel page, a summer product, a
family app. It is deliberately **not** a minimal spa, and it is deliberately not a rainbow — the
whole discipline of the kit is that three structural hues can be bright without a fourth being
added for excitement. Coral is the only saturated object on a page; everything else is ground.

## The palette, and why these values

| Role | Token | Hex | Job |
|---|---|---|---|
| Action | `--accent` | `#cc3f26` | the single primary action colour; the parasol's panels |
| Second accent | `--accent-2` | `#0fae9e` | water, media, charts, progress, focus; **never text** |
| Third hue | `--ok` / palm green | `#257043` | the frond, success, the toolkit's plant life |
| Ground | `--bg-2` | `#f6f3e6` | warm sand |
| Paper | `--surface` | `#fffdf7` | cards |
| Inset | `--surface-2` | `#f2efe1` | inputs, badges, code, Signature tile base |
| Ink | `--text` | `#16342c` | deep palm-shadow green, never a neutral charcoal |
| Text accent | `--accent-ink` | `#a8291a` | coral as a *label*, which the fill cannot do |

Two decisions worth calling out:

1. **Coral is darkened on purpose.** Coral as a fill has to carry a cream label, so it is set at
   `#cc3f26` (`--text-invert` `#fffaf0` = 4.69:1) rather than at the bright `#ff7f50` the word
   usually suggests. The lighter coral survives as the tint (`--accent-soft`) and in the artwork,
   where it carries no text.
2. **Coral-as-text ships separately.** `--accent-ink` `#a8291a` is graded on every solid ground and
   on its own 13% tint composited over the surface — the badge case — and is the only coral used for
   a label. `--accent-2` turquoise is bright by design and is never used as text; `--info` is its
   text-safe sibling.

## Contrast — measured, not eyeballed

Because this is a **light** kit, the binding ground is the *palest* one, not an average. Every value
below is the WCAG ratio computed from the shipped hex pairs (`relative luminance`, sRGB). The
composited rows are `α·fg + (1−α)·bg` in sRGB byte space, which is what the verifier samples.

```
ground                      text   muted    dim   acc-ink     ok   warn danger   info
--bg stop #dff2ea          11.54    6.49   5.00     6.01    5.18   5.08   5.58   4.71
--bg stop #e9f4e4          11.86    6.67   5.14     6.18    5.33   5.22   5.74   4.84
--bg stop #f2f2e0          11.88    6.68   5.15     6.19    5.34   5.23   5.74   4.85
--bg stop #faf0da          11.87    6.68   5.14     6.19    5.33   5.22   5.74   4.85
--bg stop #f7edd6          11.55    6.50   5.00     6.02    5.19   5.08   5.58   4.72
--bg-2  #f6f3e6            12.09    6.80   5.24     6.30    5.43   5.32   5.85   4.94
--surface   #fffdf7        13.22    7.44   5.73     6.89    5.94   5.81   6.39   5.40
--surface-2 #f2efe1        11.66    6.56   5.05     6.08    5.24   5.13   5.64   4.76

accent-ink on --accent-soft (13% coral) composited over each ground:
  over --surface 5.73 · over --surface-2 5.10 · over --bg-2 5.27 · over every --bg stop 5.03–5.19
--text-invert #fffaf0 on --accent #cc3f26 ......... 4.69   (target 4.5)
--focus-ring #0b8578 at worst ..................... 3.88   (target 3.0)
```

**Worst pair in the table:** `--text-invert` on `--accent` = **4.69:1** (target 4.5) — the cream
button label on the coral fill. The tightest pair *on a light ground* is `--text-dim` on the
sea-foam stop `#dff2ea` (and on the sand stop `#f7edd6`) = **5.00:1** (target 4.55). Note which
ground binds: dark ink on a light ground is *least* legible on the darkest stop, so the two end
stops of the `--bg` walk are the ones to solve against, not the near-white card.

`--accent-2` `#0fae9e` measures only 2.41:1 as text on `--surface-2` — that is correct and
intentional: it is a fill and a watermark, it is never a label, and every place the lab would want a
"sea blue" ink it gets `--info` instead.

**Ceiling statement:** none required. `--surface-2` does not invert the kit — it is a *lighter-warm*
inset inside a lighter-cool page — so a single `--text-dim` clears every ground in the family.

## Signature motifs — and their measured non-flatness

Each token was rendered as `background:` on a 168×72 box (the lab's Signature tile, base
`--surface-2`), screenshotted in headless Chromium at 2× device scale (336×144 device px), and the
per-tile pixel standard deviation computed with PIL/numpy. A flat plate would score ~0.00.

| Motif | Job | std-dev (L) | distinct colours |
|---|---|---|---|
| `--tropical-breeze-frond` | the **mark** — a drawn palm frond | **27.88** | 130 |
| `--tropical-breeze-wave` | the **field** — tiling rolling crests | **38.16** | 48 |
| `--tropical-breeze-parasol` | the **emblem** — top-down parasol | **41.17** | 192 |

- **Frond** — a swept rachis with leaflets fanned off at an angle and shortening toward the tip.
  **Drawn** as inline SVG: a frond *is* a curve with leaflets, and no repeating gradient produces
  one — a stripe pattern renders as a fern print, not a leaf.
- **Wave** — three rolling crests at different amplitudes, each with a foam lip offset above it, over
  the sea's own gradient. Drawn so it **tiles seamlessly** (every path starts and ends on the same y
  with a matched slope), which is what makes it a field rather than a single mark. Rendered
  `0 0 / 96px 48px repeat`.
- **Parasol** — eight wedges alternating coral and cream around a turquoise hub, over warm peach.
  Drawn because a disc divided into wedges is a division of *angle* and no gradient produces that.
  It is the one place the coral and the turquoise meet.

A fourth candidate — a sand-grain dither — was **cut**: the beach grain is already carried by
`--media-bg`, and a fourth tile would only dilute the three. Three motifs, three different jobs.

## Differentiation

This kit sits between two kits it could collide with, and the separation is deliberate:

- **vs `city-pop`** (daytime 80s Tokyo, cream/coral/teal, elegant and airbrushed): tropical-breeze is
  **greener, warmer and more playful**. Its coral is an orange-leaning tomato (`#cc3f26`), not
  city-pop's crimson (`#d62f4b`); its second accent is a greener turquoise (`#0fae9e`), not
  city-pop's teal (`#1f9aa8`); and it adds a third structural hue city-pop does not have — palm
  green. City-pop's motifs are *scene illustrations* (a sky with a skyline and a sea); this kit's are
  a botanical mark, a texture field and a top-down emblem. Type is rounded (Baloo 2 / Nunito) where
  city-pop is geometric (Sora / Manrope).
- **vs `zen-garden`** (grey mist, calm, restrained): the opposite brief. There is **no grey anywhere**
  in tropical-breeze — the neutral is warm sand (`#f6f3e6`), the ink is green (never charcoal), and
  the palette runs at high saturation instead of low. Neither typography nor shape language overlaps.

## Opt-in capabilities used

- `--media-bg` + `--media-op: 1` — the card media panel is the **beach** (sky, low soft sun with its
  glitter path, five rolling crests, a curved shoreline with foam and wet sand, sand grain, a leaning
  palm cluster), not the lab's generic accent ramp. Drawn SVG; the crests and the reflection column
  need real geometry, and the first pass was re-cut because evenly-spaced identical crests read as a
  texture swatch.
- `--wash` — a soft low sun in the top-right corner of the masthead, as a translucent warm layer
  over the page's own sky stop. Modelled over `--bg` stop 0 at the glow's centre: `--text-dim`
  4.68:1, `--accent-ink` 5.63:1; both improve everywhere else, because the eyebrow sits at the far
  (unwashed) edge.
- `--fill-bg` — progress and avatars fill with a **deep-sea teal** gradient, not the default
  accent→accent-2 ramp. Cream initials and the bar both need a ground that can carry them
  (4.81:1–6.57:1), and turquoise owns the sea; coral stays reserved for action.
- `--accent-ink` / `--accent-ink-hover`, `--blur: none`, soft `--radius-*`, `--glow`.

## Trade-offs

- **`--accent-2` is not text-safe.** Deliberate. Any "sea blue" label in this kit must use `--info`.
- **`--accent-2` surfaces through the artwork, not a lab surface.** Because this kit opts into
  `--media-bg` and `--fill-bg`, the lab's two default consumers of `--accent-2` (the media panel's
  accent ramp and the progress/avatar fill) are overridden. Turquoise is therefore visible where the
  kit actually uses it — the wave crests, the sea in the media panel, the parasol hub, the focus
  ring family — and remains a first-class token for consumers, but it is not painted by a lab
  surface of its own. Measured compromise: leaving `--fill-bg` undeclared would have put cream
  initials on the turquoise half of the default ramp at ~2.7:1, which is a real defect; the
  override is the correct trade.
- **The coral is darker than "coral".** The bright coral lives only in tints and artwork, because a
  cream label on a bright coral measures under 4.5:1.
- **The beach panel is decorative, not a hero illustration.** At a 96px-tall media panel it reads as
  "warm tropical beach" at a glance; it is a texture, and it is not trying to be a finished painting.
- **`--bg` is a px-stopped gradient**, so the sea-foam → sand walk happens in the first viewport.
  Exports and no-gradient tools should use `--bg-2`.

## When to use it

Holiday and travel pages, lifestyle, food and family products, summer and kids' software, event and
booking pages — anywhere the brief is *warm, friendly and a bit playful*, and the design must not
tip into either corporate grey or neon.

## Self-check

```bash
cd H:/Work/design-kits
python tools/build.py --only tropical-breeze --no-export --no-lint
npm_config_yes=true node tools/verify-lab.cjs tropical-breeze
```
