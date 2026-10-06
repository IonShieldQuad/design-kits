# Gothic

**Industrial starkness with something alive growing through it.** A near-black ground, bone-white
type, one deep dry blood red, heavy condensed display caps — and exactly two organic motifs, a
thorn vine and a rose, shipped as pattern rather than decoration.

`19` · dark · `Oswald · Barlow · Roboto Mono` · source: original

## Stance

The structure is hard. Coal ground (`#0a0b0d`), bone text (`#efe9dd` — ash, not pure white), a
single blood red (`#a4131f`) for the thing that acts, Oswald at 700 for anything that has to be
shouted, and 0–3px corners. Nothing here is soft and nothing here is ornamental.

Then two things grow through it. A **thorn vine** — a barbed fence of bone canes with blood barbs —
and a **rose** — nested radial petal rings. They are the kit's only organic elements and they
appear as *substrate*, never as icons scattered over a page. That is the whole argument, and it is
the difference between this and a moody dark theme: a moody dark theme has atmosphere; this kit has
a fence and a flower fighting through a black wall.

**This is the stark subculture reading, not the romantic one.** No blackletter, no gilded serif, no
stained glass, no cathedral. The display face is a condensed grotesque off a hardcore flyer, and
that was a decision, not a default — the romantic/cathedral reading would have made a pleasant kit
and a much less specific one, and it would have collided with every "heritage" kit in the set.

Use it for music, subculture zines, nightlife, fashion/dark editorial, event posters and any brand
that wants to look like it was screenprinted rather than rendered. It is a poor fit for anything
that has to look friendly, safe or corporate — that is the point of it.

At 200×120 it is unmistakable: **coal, bone, and one deep dry red**, with a bone hairline grid, a
red bar, and a thorn fence behind everything. It is the only *neutral* kit in the dark column
(Cyberpunk is violet-black and neon, Outer Space is blue-violet and gold, Inside the Machine is
warm graphite and amber) and the only one with anything growing in it.

## Ground truth

Every value below is authored for this kit; nothing is inherited from another kit's palette.

| Token | Value | Note |
|---|---|---|
| `--bg` | `#0a0b0d` | coal ground, neutral-cool. Flat hex — no gradient to check |
| `--bg-2` | `#101114` | masthead gradient stop |
| `--surface` | `#141519` | panel |
| `--surface-2` | `#1c1d22` | inset well, inputs, badges |
| `--overlay` | `rgba(4,4,6,.80)` | modal scrim |
| `--text` | `#efe9dd` | bone — 16.29:1 on `--bg` |
| `--text-muted` | `#a8a294` | ash — 7.18:1 on `--surface` |
| `--text-dim` | `#8f8a7c` | dust — 5.71 / 5.29 / 4.88 on bg / surface / surface-2 |
| `--text-invert` | `#efe9dd` | bone ink on the blood plate — 6.45:1 |
| `--accent` | `#a4131f` | deep dry blood — the only action colour |
| `--accent-hover` | `#c01726` | the same red, arterial |
| `--accent-2` | `#b8555f` | welded rose — the rose motif's own red |
| `--accent-soft` | `rgba(164,19,31,.16)` | 16% blood tint, derived from `--accent` |
| `--accent-ink` | `#c9707a` | welded rose as TEXT — 5.70:1 on `--bg` |
| `--accent-ink-hover` | `#dc8a8f` | 7.57:1 on `--bg` |
| `--ok` | `#8aa05c` | dried moss |
| `--warn` | `#c99a34` | dried amber |
| `--danger` | `#e4564f` | vermilion fault |
| `--info` | `#8d99a6` | cold ash blue |
| `--border` | `rgba(239,233,221,.14)` | the bone hairline |
| `--border-strong` | `rgba(239,233,221,.32)` | input rim / emphasised rule |
| `--border-w` | `1px` | a stencil edge, not a brutalist slab |
| `--focus-ring` | `#efe9dd` | bone — never mistakable for the red action |
| `--radius-sm/md/lg` | `0px` / `2px` / `3px` | sharp |
| `--radius-pill` | `3px` | deliberate — see below |
| `--cut` | `0px` | no chamfer; that is Cyber-angel's signature |
| `--shadow-1` | `inset 0 1px 0 rgba(239,233,221,.05), 0 1px 0 rgba(0,0,0,.90), 0 14px 30px -22px rgba(0,0,0,.95)` | bone rim, hard line under, short falloff |
| `--shadow-2` | `inset 0 1px 0 rgba(239,233,221,.08), 0 22px 48px -24px rgba(0,0,0,.98), 0 0 0 1px rgba(164,19,31,.20)` | the raised plate, with the blood thread |
| `--glow` | `0 0 0 1px rgba(164,19,31,.50), 0 0 16px -6px rgba(164,19,31,.55)` | a shadow the blood casts, **not** a bloom |
| `--blur` | `none` | coal is not frosted glass |

## The two motifs

| Token | What it is | How it is built |
|---|---|---|
| `--gothic-thorn` | bone canes with blood barbs — a barbed fence | 3 × `repeating-linear-gradient`, all on a 34px period so every cane grows exactly one barb per cycle, plus a hairline of bone barb-hairs at 1/3 period |
| `--gothic-rose` | a rose head | 7 × `radial-gradient`: five uneven outer petals, a bone bloom, and the nested petal rings (welded-rose core, no white heart) |
| `--gothic-ash` | the worn ground | 2 × `radial-gradient` (bone bloom + shadowed corner) + a 3px grain and a 7px counter-grain |
| `--gothic-rim` | panel rim light | a `box-shadow` (in-set bone highlight + blood thread) — applied, not painted |
| `--gothic-blood` | the accent as a surface | 4 stops: `#6d0d15 → #a4131f → #c01726 → #3a0709` |
| `--gothic-vein` | one hairline, blood → bone → blood | 7 stops in a horizontal `linear-gradient` |

**Six tokens, two ideas.** Thorn and rose are the motifs; ash, rim, blood and vein are texture and
light. A third *motif* — an eye, a spider, a bat — is explicitly out of scope. Restraint is the
kit.

### The 34px thorn period was measured, not guessed

The thorn pattern was rendered at three densities at chip size (168×72, the lab's own tile) and
reviewed: **26px** merged into tartan plaid, **42px** dissolved into disconnected scratches, and
**34px** still read as a thorned fence — red barbs distinct, bone canes continuous.

The rose went through four rounds for the same reason. A pure nested-radial rose is *correct* and
reads as a **bullseye**; adding a bone-white heart made it read as an **eye** (a bright pinprick at
the centre of a dark disc is a catchlight). The shipped version keeps the nested rings for the
petal structure but wraps them in **five uneven outer petals** and replaces the white heart with a
welded-rose inner petal in a burgundy throat. It is the only one of the four that read as a flower
head at both chip and full size.

The motifs are the one part of this kit that could not be settled by arithmetic, so they were
settled by looking, three and four times respectively. Everything else was settled by a contrast
script.

## Type: why these three

- **Oswald — display and headings.** A heavy condensed grotesque: the letterform of the hardcore
  flyer, the industrial stencil, the agitprop poster. Narrow, vertical, flat terminals, no
  calligraphic gesture and no blackletter — which is exactly the reading that was asked for, and
  exactly the one that was rejected. Weight 700 on the h1, 600 on section headings; its condensed
  width lets a long title sit on one line, which is the whole point of a condensed face.
- **Barlow — body.** A slightly condensed grotesque drawn for signage. It survives at 15px, it
  shares Oswald's grotesque skeleton so the two never look bolted together, and being narrower than
  a normal-width sans it keeps the vertical rhythm tight. It never sets a title.
- **Roboto Mono — labels.** Eyebrows, badges, table headers, metadata, hints. Mono is the kit's
  *machine* voice: the serial number stencilled on the plate. Caps labels run `+0.22em`, much wider
  than Inside the Machine's stamped `+0.12em`, because a stencil on a black ground needs the air to
  stay legible at .72rem.
- **Display tracking is `-0.005em`** — almost nothing, on purpose. Oswald is already drawn
  condensed and the usual `-0.02em` display tightening closes its counters at 2.9rem.

## Derived, and why

- `--accent-hover: #c01726` — one visible step up in lightness from `#a4131f`, same hue. The stain
  goes arterial; it never changes colour.
- `--accent-soft: rgba(164,19,31,.16)` — a 16% tint of `--accent`, written as `rgba()` rather than
  re-typed as a hex, because it is derivable and must stay in sync with the red.
- `--accent-ink: #c9707a` — the text-safe member of the blood family. This is the one derivation
  the contrast numbers forced: `#a4131f` is **2.52:1** against the ground, so the deep red simply
  cannot carry small type. The welded rose at 5.70:1 can, and it happens to be the rose motif's own
  colour — the link colour and the motif are the same substance rather than two competing ideas.
- `--danger: #e4564f` — deliberately **lighter and hotter** than the accent. "Delete" must never
  read as "the action".
- `--text-invert: #efe9dd` (bone, not near-black). A deep red is deep enough to hold light ink
  (6.45:1), so the primary button keeps a bone label. This is the inverse of Cyberpunk and Inside
  the Machine, where the accent is bright and the button label is dark — and it is a direct
  consequence of choosing a *dry* red rather than a neon one.
- `--border` / `--border-strong` are **translucent bone**, not opaque steel and not a tinted hue:
  the hairline is the stencil edge of a bone plate on coal.
- `--radius-pill: 3px` — a stamped plate instead of a lozenge. The token keeps its contract name.

## Contrast (verified numerically, not by eye)

Computed from `tokens.css` by script — see the verification log. WCAG relative-luminance ratio,
`(Lhi + .05) / (Llo + .05)`.

| Pair | Ratio | Target | |
|---|---|---|---|
| `--text` on `--bg` | **16.29:1** | ≥ 7 | ✓ |
| `--text-muted` on `--surface` | **7.18:1** | ≥ 4.5 | ✓ |
| `--text-invert` on `--accent` | **6.45:1** | ≥ 4.5 | ✓ |
| `--text-dim` on `--bg` | **5.71:1** | ≥ 4.55 | ✓ |
| `--text-dim` on `--surface` | **5.29:1** | ≥ 4.55 | ✓ |
| `--text-dim` on `--surface-2` | **4.88:1** | ≥ 4.55 | ✓ |
| `--accent-ink` on `--bg` | **5.70:1** | ≥ 4.5 | ✓ |
| `--accent-ink` on accent-soft over `--surface-2` | **4.62:1** | ≥ 4.5 | ✓ |
| `--text` on `--surface-2` | **13.92:1** | ≥ 7 | ✓ |

`--text-dim` clearing 4.55:1 on the *lightest* ground (`--surface-2`) is the binding constraint;
it is why the dim tier is `#8f8a7c` rather than something moodier and darker. `--border` /
`--border-strong` sit at ~1.4–2.6:1 by design — decorative seams that never carry meaning alone.

**No contrast carve-out is needed.** All three surfaces are dark and share one polarity, so a single
`--text` / `--text-muted` / `--text-dim` family carries all three tiers and the kit does **not**
declare `--text-on-surface*` / `--text-on-surface-2*`. Those exist for the inverted tier (a dark
well inside a light shell); there is no inversion here, so declaring them would be noise.

## Trade-offs

- **A deep accent is a contrast liability as text, and the kit pays for it twice.** `#a4131f` is
  2.52:1 on the ground, so *every* red that has to be read — links, eyebrows, active nav, inline
  code, badge labels, secondary-button labels — is the welded rose (`--accent-ink`, `#c9707a`)
  instead. Two reds is the price of a dry red; the alternative was a neon one, which was refused.
  The upside is a blood plate that takes bone-white ink at 6.45:1, which no bright-accent dark kit
  here can do.
- **Any multi-family `repeating-linear-gradient` wants to become plaid.** The thorn was rendered at
  three densities before shipping and 34px was the only one that survived chip size. It still reads
  as a *fence*, not as a drawing of a vine — that is the honest ceiling of pure-CSS patterning, and
  the brief asked for a trellis read specifically. If you need literal thorn-shaped barbs, this
  token is the wrong tool and you want an SVG; the kit's position is that a substrate pattern
  should be a token, not an asset.
- **`--radius-pill: 3px`** is a knowing bend of a token name. One visible consequence in the shared
  lab: `.badge` (pill, 3px) and `.badge-square` (`--radius-sm`, 0px) now differ by 3px, so those
  two demos look near-identical. This kit distinguishes badges by colour and by the status dot, not
  by roundness. The same token makes `.avatar` a square of bone initials, which is correct here.
- **`--glow` is a restrained shadow, not a bloom.** With a deep accent, an actual glow would have
  had to be either invisible or neon; Cyberpunk owns the neon halo, so this kit's "glow" is a
  blood stain pooling under the plate. It is less showy than the name suggests.
- **Six signature tokens is close to the lab's ceiling of eight.** They are all used; none is
  filler. `--gothic-vein` is the weakest of the six as a *tile* (a horizontal rule rendered at
  72px tall reads as a band, not a hairline) but it is the strongest of the six as an actual
  export — a 1px blood-to-bone rule is the thing you reach for first.
- **The kit is a bad fit for anything friendly.** Bone on coal with a blood accent is not a
  neutral palette; using it for a healthcare product or a kids' app would be a category error.

## Files

`DESIGN.md` (normative values) · `tokens.css` (the contract) · `kit.json` (gallery metadata) ·
`index.html`, `tokens.json`, `tailwind.theme.json`, `theme.css` (generated by
`python tools/build.py`).
