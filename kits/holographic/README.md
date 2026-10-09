# Holographic

**Iridescent foil on dark.** A cool charcoal shelf carrying surfaces that shift hue across
their width as hard prismatic bands, an iridescence that reaches the *working parts* — every
button, field, bar and switch wears a hard prismatic edge — one blue action, one violet
counterpoint, and a rainbow that lives in the material, not in a third accent.

- Kit: `holographic` · order `180` · mode `dark`
- Fonts: Gruppo · Space Grotesk · Space Mono
- Tags: `dark` `iridescent` `prismatic` `futuristic` `chrome` `glow`
- Source: **derived** from the user's Figma reference — fileKey
  `4tEWhmZzpqWsjjwJrqS8lg`, node `4:2` ("Glowy stuff"). Palette, aperture geometry and
  Gruppo type are taken from that file; the register is re-expressed (see *Stance*). The
  kit is named by genre — no logo or trade dress is reproduced.

## Stance

Most "holographic" treatment is a soft rainbow gradient, and it reads as a pastel wash
rather than as foil. A holographic surface is **diffraction**: colour that shifts with
position, in hard prismatic bands with crisp transitions. So the one architectural
commitment here is that **the kit is non-smooth**, and it says so in its tokens:

- every signature ramp is **hard-stopped**, and the **foil is drawn** (base64 SVG, solid
  bands, no fade);
- every shadow is a **zero-blur offset** (`2px 2px 0 0`), never a blurred drop shadow;
- `--blur: none`, no `backdrop-filter`, no bloom anywhere;
- the motifs are **drawn at tile size** (base64 SVG), crisp, not scaled up from a blur.

That is the tension the kit resolves. The reference file is called "Glowy stuff" and is
nothing but soft neon glow; a kit that copied the glow would be the smooth holographic
kit the brief calls a missed opportunity. The reference's *palette* (its gradient strokes
— mint→cyan→violet→magenta), its *geometry* (the rainbow iris, prismatic edges) and its
*type* (Gruppo) are kept; its *blur* is thrown away and replaced with diffraction.

**The iridescence is in the components, not just the tiles.** A kit that quarantines its
rainbow into three decorative chips and ships flat blue controls has named itself
holographic without behaving holographically. So the working parts carry it too:

- **every button** wears a **chromatic-aberration edge** — three hard, zero-blur, zero-fill
  offset plates in different prismatic hues (violet `#b64ce8` → magenta `#ff5fd0` → teal
  `#3ee0c8`) stacked down-right, via `--btn-shadow`; the primary button's own halo
  (`--glow`) is the same prismatic stack under a crisp ink ring;
- **every field** is a milled recess with a violet left lip and a blue right lip
  (`--input-inset`);
- **nav and tabs** are a milled channel with prismatic inner lips (`--bar-shadow`), and the
  item riding in it wears the prismatic offset (`--bar-item-shadow`);
- **the switch** has a prismatic-lipped track and a violet/blue-edged knob
  (`--toggle-shadow`, `--toggle-knob-shadow`);
- **progress and avatar fills** are four hard prismatic bands (`--fill-bg`);
- **panels** shift hue across their width as hard bands (`--surface`), and **hairlines** are
  tinted toward the foil (`--border`).

## Key choices

- **There is a real foil material, not just gradients.** `--holographic-diffraction` is
  drawn as a **stamped foil sheet** (base64 SVG): its bands flip between silver, blue,
  cyan, violet, magenta, gold and teal with **abrupt** transitions, with a crisp dark land
  between them and silver specular highlights where metal would catch the light. It is
  *reused* as the card media panel (`--media-bg: var(--holographic-diffraction)`), so the
  surface a card shows is the foil, not a generic two-stop ramp. (The register already
  called the panel a "foil sheet"; the material had been missing.)
- **The ground is three hard hue-shifting plates, not a fade.** `#33304a` (violet-cast)
  → `#212a38` (blue-cast) → `#16171f`, laid as hard bands so the ground itself shifts hue.
  Panels (`--surface`) are banded the same way — violet-, blue-, plum- and teal-cast bands
  at near-constant luminance — so a card shifts hue like foil without ever becoming a worse
  ground for type. A smoothly fading `--bg` is the biggest "smoothness" giveaway.
- **The action colour takes ink, not white.** `#54adff` with an ink label (`#0d0e14`,
  8.07:1) is both the stronger read and the foil move; near-white on the bright blue is
  3.4:1 and fails.
- **`--accent-ink` exists** (`#6ec0ff`) because `#54adff` is a fine *fill* but only 6.40:1
  as a small label on the brightest band, and 4.86:1 on its own 16% tint. Eyebrow, links,
  active nav and accent/secondary labels route through it.
- **The rainbow is a surface, not a colour role.** The palette is two accents; the spectrum
  is carried by the foil, the prism fan and the iris. This is what keeps a holographic kit
  from becoming "a rainbow kit".
- **The masthead wash is a hard-banded prismatic shear**, not the lab's smooth radial
  bloom — and it is graded as a *composite* (`#334053`), because a wash raises the ground
  the eyebrow and meta text sit on.
- **The native controls are reskinned, not left to the browser.** `--check-appearance: none`
  replaces the browser's light default — a white box, jarring on this dark ground — with the
  kit's own: a `--surface-2` well, a violet hairline and an accent-blue checked fill. (The
  lab paints the checkbox and the radio with the same box, so they read as sibling chips
  rather than a tick and a disc; that is a shared-lab behaviour, noted here rather than
  worked around. The controls do take their own radius now (`--check-radius`), added after this
  kit showed the gap: binding the native controls to `--radius-pill` meant squaring a checkbox
  also unsquared every badge. This kit leaves it at the default — soft-round, matching its pills.

## Contrast — measured, not eyeballed

WCAG ratios computed from the declared hexes. For a dark kit the binding ground is the
**brightest** stop; the brightest plate is `#33304a`, and every banded surface/panel band
is deliberately darker than it, so the plate binds. Because the ground is variable and the
masthead carries a translucent wash, the tinted pairs are graded against their
**composite**.

| Pair | Measured | Ground | Required | |
|---|---|---|---|---|
| `--text` `#edeff7` | 11.00:1 | `#33304a` (brightest plate) | 7.0 | ✅ |
| `--text` on the banded panel (worst band) | 11.68:1 | `#17304d` (lightest panel band) | 7.0 | ✅ |
| `--text-muted` `#bcc1cf` | 7.02:1 | `#33304a` | 4.5 | ✅ |
| `--text-muted` on the wash | 5.48:1 | comp `#384263` | 4.5 | ✅ |
| `--text-dim` `#aeb5c7` | 6.16:1 | `#33304a` | 4.55 | ✅ |
| `--text-dim` on the banded panel (worst band) | 6.53:1 | `#17304d` | 4.55 | ✅ |
| `--text-dim` on the wash | **4.81:1** | comp `#384263` | 4.55 | ✅ |
| `--accent-ink` `#6ec0ff` | 6.40:1 | `#33304a` | 4.5 | ✅ |
| `--accent-ink` on accent-soft over `#33304a` | **4.86:1** | comp `#384467` | 4.5 | ✅ |
| `--accent-ink` on accent-soft over worst panel band | 5.08:1 | comp `#214469` | 4.5 | ✅ |
| `--accent-ink-hover` `#8ed0ff` | 7.59:1 | `#33304a` | 4.5 | ✅ |
| `--text-invert` `#0d0e14` on `--accent` | 8.07:1 | `#54adff` | 4.5 | ✅ |
| `--ok` `#46e0a0` | 7.48:1 | `#33304a` | 4.5 | ✅ |
| `--warn` `#ffc46b` | 8.04:1 | `#33304a` | 4.5 | ✅ |
| `--danger` `#ff7585` | **4.89:1** | `#33304a` | 4.5 | ✅ |
| `--info` `#48cfe0` | 6.78:1 | `#33304a` | 4.5 | ✅ |
| `--focus-ring` `#6ec0ff` | 6.40:1 | `#33304a` | 3.0 | ✅ |
| ink on `--fill-bg` stops `#54adff`/`#b64ce8`/`#ff5fd0`/`#3ee0c8` | 8.07 / **4.76** / 7.16 / 11.65 | fill stops | 4.5 | ✅ |

**Worst pair (before this pass):** `--accent-ink` on the accent's own tint composited over
the brightest plate at **4.86:1**. **Worst pair (now):** the ink label on the **violet band
of the new `--fill-bg`** (`#b64ce8`) at **4.76:1** — a pair the more saturated prismatic
fill introduced; it clears its 4.5 floor and is the binding one. The worst *ground-bound*
pair is `--danger` on the plate at **4.89:1**. The button/bar/field edges are box-shadows
outside the text box and never touch the sampled ground, so they do not enter the gate.
`--accent-2` (violet `#b64ce8`) is a **fill / media / data-fill** token and is never used
as text; `--info` (`#48cfe0`) exists as the readable cyan.

## Signature motifs

Three, three different jobs, each drawn for the tile (base64 SVG where a gradient cannot
express the form):

1. **`--holographic-diffraction`** — the *material*: now a **stamped foil**. Drawn (base64
   SVG): a sheet of 19 abrupt bands (silver / blue / cyan / violet / magenta / gold / teal)
   with crisp dark lands and silver speculars, vertical so it tiles seamlessly. Drawn rather
   than faded because a stamped sheet is a material with hard edges — and so the band count
   can be high enough that the banding is unmistakable at 168×72. It is **reused as
   `--media-bg`**, so the card panel shows the foil itself.
2. **`--holographic-prism`** — the *geometry*. A beam enters a triangle and leaves as an
   ordered fan of hard bands. Drawn (base64 SVG): a fan diverges from a point, and a
   linear gradient cannot.
3. **`--holographic-aperture`** — the *glyph*. The reference's eight-bladed rainbow iris,
   a camera aperture that is also a spectrum wheel. Drawn: an aperture is arcs at angles a
   gradient cannot fake.

Non-flatness is reported in the build report (per-tile pixel standard deviation on
`--surface-2`); all three read as drawn, structured motifs against the tile base. The
foil tile's mid-scan crosses 21 distinct flat runs in 168px — the bands are hard and,
at tile size, unmistakable.

## Trade-offs

- **The ground is darker than the reference canvas.** The reference sits on a mid grey
  (`#414141`); a page ground that light cannot hold a 7:1 body text alongside a bright
  prismatic action, so the foil plates are deepened to `#33304a`→`#16171f`. The mid grey
  survives as a band of `--surface`.
- **The glow is gone.** Every bloom in the source is a hard edge here. Even the new
  chromatic-aberration edge is a *hard* multi-hue offset — three solid plates, zero blur —
  not a rainbow glow. If you want the soft neon version, use `synthwave` — this kit is the
  crisp half of the same idea.
- **Every control now carries the prismatic edge**, which is the point, but it does mean
  the kit is loud: the edge is the same on every variant (the hook reaches all five) and
  only the disabled button drops it. If you want a calmer control layer, keep the foil and
  the banded surfaces but drop `--btn-shadow`.
- **No `kit.css`.** Everything the kit needs is a token: the wash, the foil (drawn), the
  media panel, the recessed input, the prismatic button/bar/toggle edges, the prismatic
  fill, the banded panel and the three drawn motifs. No stacked construction was required.

## When to use

Iridescent, futuristic, premium-tech branding: product launches, sci-fi and music media,
AI and dev-tool marketing, event and hardware identity — anything that should look like
foil catching light. Avoid it where the surface must feel calm, warm or trustworthy at
9am; for the smooth neon half of the decade's night, use `synthwave`.
