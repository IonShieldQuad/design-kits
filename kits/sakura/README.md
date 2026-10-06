# Sakura

**A spring day: saturated blossom pink against fresh leaf green, on a light tinted ground.**

`15` · light · `Zen Kaku Gothic New · Karla · IBM Plex Mono` · source: original

## Stance

The brief was one line — *"spring day: blossom pink with fresh leaf green, light and
cheerful, more colour than pastel"* — and the whole kit is that sentence translated.

**Not a quiet petal-drift, a spring day.** Two colours carry it and both are held at
visible saturation. The failure mode on either side is what this kit is built to avoid:

- **Go too pale and it is generic pastel.** A soft wash of near-white with a faint tint —
  which is what the library's `glass` kit already is.
- **Add too much pink and it is a nursery.** One sugary hue repeated until the page reads
  as a baby-shower invitation.

The escape from both is one move: **pink against living green.** Pink alone is a cliché;
pink beside a leaf is the season. So the green is not a swatch — it is a working
counterweight that shows up in the focus ring, the media/avatar/progress gradients, the
light half of the spring ramp and the scatter. And the two hues are married into a single
`--sakura-ramp`: blossom → **cream** → leaf, where the cream midpoint is what stops the
pink and the green from reading as two separate accents that merely meet.

Three decisions follow:

- **Pink drives action.** Sakura *is* the blossom, so the one saturated object on a screen is
  the blossom: primary button, toggle, checkbox, the tint behind active nav. Pink as a fill
  is the identity.
- **The ink is deep plum, never pink.** Pink body text on a pink ground is the other failure;
  reading ink is a warm plum-black (`#3a2438`).
- **The ground is a real gradient, not white.** Cool sky at the top of the first screen, warm
  petal below it, a leaf tint lower down — a room with a window open, never sterile white and
  never grey (grey is `zen-garden`, and grey is a wet day).

Use it for spring campaigns, florals, lifestyle and food brands, kids-adjacent-but-not-childish
product pages, and any marketing surface that wants **real colour** without going neon. **Not**
for dense data tooling, alert-heavy dashboards, or anything that needs a muted, deferential
chrome — this kit spends its loudness on the blossom and has none left for restraint.

## The palette, and the role of each colour

| Token | Value | Role |
|---|---|---|
| `--bg` | sky→petal→leaf gradient | **The ground.** A real gradient with a warm–cool shift; px stops. |
| `bg-stop-sky` … `bg-stop-end` | `#f1f6fb` / `#fdf1f6` / `#f3f8ee` / `#fdf3f6` / `#f9eef3` | The five stops, shipped as colours (a gradient is not a colour). `#f9eef3` is the darkest and the one all contrast is proved against. |
| `--bg-2` | `#fdf3f7` | Petal: masthead top stop and the solid stand-in for exports. |
| `--surface` | `#fffbfd` | Cards — warm white lifted above the tinted ground. |
| `--surface-2` | `#f8eef3` | Nested panels and inputs — the petal tint, settled below the card. |
| `--text` | `#3a2438` | **Deep plum ink.** All body and display type. |
| `--text-muted` | `#5e4557` | Secondary reading ink: card bodies, table cells. |
| `--text-dim` | `#6d5165` | Captions, placeholders, table headers. |
| `--text-invert` | `#ffffff` | Ink on the blossom action. |
| `--accent` | `#c8325f` | **Blossom pink — the action FILL.** Buttons, toggle, checkbox, nav tint. |
| `--accent-hover` | `#b02651` | The pressed step — one deeper, so a press bruises rather than glows. |
| `--accent-ink` | `#a81d4c` | **Pink as TEXT** — links, eyebrow, active nav, secondary-button labels, inline code. The fill pink is 2.7:1 as a label; this deep rose is 6.3:1. |
| `--accent-ink-hover` | `#8d1540` | The hover step for pink text. |
| `--accent-2` | `#2e8339` | **Fresh leaf green — the counterweight.** Focus, gradients, bars, avatar; the light half of the ramp. |
| `--accent-soft` | `rgba(200,50,95,.10)` | 10% blossom tint: focus halos, active nav, `badge-accent`. |
| `--ok` / `--warn` / `--danger` / `--info` | `#177040` / `#8f5c00` / `#b3261e` / `#2b6aa8` | Status, kept off the two brand hues so a status never reads as decoration. |
| `--border` / `--border-strong` | `#ecd6e0` / `#d9b9c8` | Petal hairline and emphasised line. |
| `--focus-ring` | `#2f8340` | **Fresh green** keyboard focus — the leaf in real UI, and never confusable with the pink action. |

## Signature extras

Declared in `kit.json` `signature`, rendered in the lab's Signature section:

- **`--sakura-petal`** — a petal/leaf **scatter** built from six `radial-gradient` dots at
  deliberately unequal radii (5 / 3.5 / 4.5 / 6 / 3 / 4px) so it never reads as a grid, and
  with roughly a third of the dots in **leaf green** so it is a season rather than a
  pink-on-pink wallpaper. It holds up at chip and thumbnail size, which is the whole reason
  it ships.
- **`--sakura-blossom`** — a **five-petal blossom**: five ellipses on a 72° ring
  (petal centres at 50%,22 / 76%,42 / 66%,74 / 34%,74 / 24%,42) alternating two pinks for a
  light and a shadow side, with a blossom-pink heart at the centre.
- **`--sakura-ramp`** — the **spring ramp**, blossom → cream → leaf in **px stops**
  (`#c8325f` 0 → `#f7a9c5` 90 → `#fdf1f6` 170 → `#dff0c8` 250 → `#7ac06a` 320 → `#2e8339` 420).
  The cream at 170px is the midpoint that joins the two hues.
- **`--sakura-fresh`** — a **fresh highlight** sheen for a page top or hero plate: cool white
  → leaf tint → petal blush → nothing, 0…340px.

## Derived, and why

- **`--accent-ink` was necessary, not optional.** `#c8325f` is a strong button fill (white on
  it is 5.2:1) and a **bad label** — 2.7:1 as text on the ground. A pink that has to carry
  white type must be deep; a pink that has to be readable *as type* must be deeper still.
  Hence two values: fill pink and rose text.
- **`--accent-2` is `#2e8339`, deeper than a "bright leaf" first guess.** At a lighter
  `#3f9b46` the white initials on the `--accent`→`--accent-2` avatar wash measured **3.51:1**
  — a failure. One step deeper to `#2e8339` lifts white-on-green to **4.75:1** and leaves no
  green lighter than the pink's own white-type floor. It is still unmistakably a *fresh*,
  chromatic leaf — the point is that it is saturated, not that it is pale.
- **The ground is a gradient with px stops.** The body's gradient box is the whole document
  height; a 0–100% ramp spreads a 5% tint over thousands of pixels and the first screen reads
  flat white. Fixed-length stops keep the same wash in view at any page length. It stays on
  `--bg` (unlike `zen-garden`, which moved its gradient to an extra) because the shared lab's
  masthead no longer nests `--bg` inside a second gradient, so a gradient ground is safe.
- **`--text-dim` is `#6d5165`, not a lighter grey.** The contract wants `--text-dim` ≥ 4.55:1
  against **both** `--bg` and `--surface`; the pink and green grounds are light, so the
  tertiary ink has to be a genuinely dark plum-rose rather than a mid grey. It clears 6.2:1 on
  the darkest ground stop and 6.8:1 on the card.
- **`--glow` is a blossom shadow, not a bloom.** `0 10px 22px -10px rgba(200,50,95,.42)` — a
  soft pink drop under the primary button. If it ever reads as light, it is too strong.
- **`--blur: none`.** Airy is not frosted; a pane of frosted glass is `glass`'s material and
  would put a high-contrast edge around every surface.
- **The transition has a hint of bounce** (`cubic-bezier(.3, 1.06, .45, 1)`): spring is
  movement, and a hard snap is the one thing a cheerful kit should not do.

## Typography, and why

**Zen Kaku Gothic New** (display) over **Karla** (body), with **IBM Plex Mono** for labels.

One-line justification for the display face: a **Japanese-designed humanist gothic whose
light, open letterforms give the airy cheer of the season** and tie the type to the same
place the blossom comes from — the kit's origin reads through letterform, not only colour.
It is the apt pick over a Japanese *mincho* (which would be a contemplative, journal-like
voice, and a spring day is awake, not solemn). Karla stays plain so the display face is the
only voice with a spring in it; IBM Plex Mono is a humanist mono, so labels stay legible
without becoming a machine voice.

## Trade-offs

- **Two pinks, and that is the point.** The kit carries `--accent` (`#c8325f`) *and*
  `--accent-ink` (`#a81d4c`). They are not redundant — one is a surface, one is type — but a
  reader new to the tokens may reach for the wrong one. The rule is in the Do's and Don'ts:
  fill vs label.
- **The ground has low identity on its own.** At thumbnail size a 5% tinted wash reads as
  near-white, exactly like `zen-garden`'s grey. This kit's recognisability in a grid comes
  from its **blossom button, its leaf focus ring and its saturated two-hue ramp**, not from
  the ground. If the ground must assert itself, apply `--sakura-ramp` or `--sakura-petal`
  behind a plate rather than darkening `--bg` (a darker ground pushes the kit out of "spring"
  and into "dusk").
- **Green is a fill, never a paragraph colour.** `--accent-2` measures well under 4.5:1 as
  text on the ground. It is scoped to fills, motifs, focus and gradients. That is the price
  of a leaf green bright enough to differentiate the kit at a glance.
- **No elevation drama.** Floating surfaces get `--shadow-2` and a hairline; there is no
  designed overlay tier. This kit is scoped to marketing and product surfaces, not to
  multi-layer app chrome.

## Contrast

All ratios computed from `tokens.css` (WCAG 2.1 relative luminance), against the **darkest**
ground stop `#f9eef3` — the worst point a viewer can scroll to — never the lightest. Full
log: `C:/Users/Lily/AppData/Local/hermes/cache/scratch/kit-verify-sakura.md`.

| Pair | Ratio | Target |
|---|---|---|
| `--text` on `--bg` (darkest stop) | 12.46:1 | ≥ 7 ✓ |
| `--text` on `--surface` | 13.74:1 | ≥ 7 ✓ |
| `--text-muted` on `--surface` | 8.30:1 | ≥ 4.5 ✓ |
| `--text-invert` on `--accent` | 5.15:1 | ≥ 4.5 ✓ |
| `--text-invert` on `--accent-hover` | 6.48:1 | ≥ 4.5 ✓ |
| `--text-dim` on `--bg` (darkest stop) | 6.15:1 | ≥ 4.55 ✓ |
| `--text-dim` on `--surface` | 6.79:1 | ≥ 4.55 ✓ |
| `--text-dim` on `--surface-2` | 6.14:1 | ≥ 4.55 ✓ |

Supporting pairs the lab actually renders: `--accent-ink` on `--bg` **6.30:1** (the link
colour) and on `--surface` **6.95:1**; `--accent-ink` on `--accent-soft` composited over any
ground ≥ **5.45:1** (active nav, `badge-accent`); `--text-muted` on `--surface-2` **7.51:1**;
white on the `--accent`→`--accent-2` avatar gradient ≥ **4.75:1** (worst, green, end); and
every status colour ≥ **4.96:1** on both panel surfaces.

## Linter warnings kept (0 errors)

`designmd lint kits/sakura/DESIGN.md` reports **0 errors, 13 warnings**, all of a class the
whole library keeps and none of them real:

- **3 × `contrast-ratio` on `button-secondary-hover`, `badge-accent`, `nav-active`.** All
  three sit on `{colors.accent-soft}`, which is `rgba(200,50,95,.10)`. The linter cannot
  composite an alpha background, so it measures the text against the *raw* 10% value and
  reports 1.4–1.8:1. Against the **composited** tint the real ratios are **5.45:1** (over
  `--surface-2`) and **5.47:1** (over the ground) — see the contrast log. Identical warnings
  appear on `zen-garden`, `glass` and `glorious-morning`.
- **10 × `orphaned-tokens`** on `bg-stop-*`, `bg-2`, `overlay`, `border`, `border-strong`
  and `focus-ring`. These are ground, line and focus values: they are consumed by
  `tokens.css` and by the shared lab, not by a `components:` entry, and the component schema
  has no property for a hairline or a focus outline. Every kit in the library has this set.

No warning is hidden; none affects rendering or contrast.
