# Holographic

**Iridescent foil on dark.** A cool charcoal shelf carrying surfaces that shift hue across
their width as hard prismatic bands, one blue action, one violet counterpoint, and a
rainbow that lives in the material — not in a third accent.

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

- every signature ramp is **hard-stopped** (two stops sharing one px position);
- every shadow is a **zero-blur offset** (`4px 4px 0 0`), never a blurred drop shadow;
- `--blur: none`, no `backdrop-filter`, no bloom anywhere;
- the motifs are **drawn at tile size** (base64 SVG), crisp, not scaled up from a blur.

That is the tension the kit resolves. The reference file is called "Glowy stuff" and is
nothing but soft neon glow; a kit that copied the glow would be the smooth holographic
kit the brief calls a missed opportunity. The reference's *palette* (its gradient strokes
— mint→cyan→violet→magenta), its *geometry* (the rainbow iris, prismatic edges) and its
*type* (Gruppo) are kept; its *blur* is thrown away and replaced with diffraction.

## Key choices

- **The ground is three hard hue-shifting plates, not a fade.** `#33304a` (violet-cast)
  → `#212a38` (blue-cast) → `#16171f`, laid as hard bands so the ground itself shifts hue.
  A smoothly fading `--bg` is the biggest "smoothness" giveaway, so the ground is banded.
- **The action colour takes ink, not white.** `#54adff` with an ink label (`#0d0e14`,
  8.07:1) is both the stronger read and the foil move; near-white on the bright blue is
  3.4:1 and fails.
- **`--accent-ink` exists** (`#6ec0ff`) because `#54adff` is a fine *fill* but only 6.56:1
  as a small label on the brightest band, and 4.95:1 on its own 16% tint. Eyebrow, links,
  active nav and accent/secondary labels route through it.
- **The rainbow is a surface, not a colour role.** The palette is two accents; the
  spectrum is carried by the three signature ramps (below). This is what keeps a
  holographic kit from becoming "a rainbow kit".
- **The masthead wash is a hard-banded prismatic shear**, not the lab's smooth radial
  bloom — and it is graded as a *composite* (`#334053`), because a wash raises the ground
  the eyebrow and meta text sit on.
- **The checkbox is squared by token** (`--check-appearance: none`) so the native control
  obeys the kit's crisp geometry rather than rendering a round chip.

## Contrast — measured, not eyeballed

WCAG ratios computed from the declared hexes. For a dark kit the binding ground is the
**brightest** stop; the brightest plate is `#33304a`. Because the ground is variable and
the masthead carries a translucent wash, the tinted pairs are graded against their
**composite**.

| Pair | Measured | Ground | Required | |
|---|---|---|---|---|
| `--text` `#edeff7` | 11.00:1 | `#33304a` (brightest plate) | 7.0 | ✅ |
| `--text-muted` `#bcc1cf` | 7.02:1 | `#33304a` | 4.5 | ✅ |
| `--text-muted` on the wash | 5.48:1 | comp `#384263` | 4.5 | ✅ |
| `--text-dim` `#aeb5c7` | 6.16:1 | `#33304a` | 4.55 | ✅ |
| `--text-dim` on the wash | **4.81:1** | comp `#384263` | 4.55 | ✅ |
| `--accent-ink` `#6ec0ff` | 6.40:1 | `#33304a` | 4.5 | ✅ |
| `--accent-ink` on accent-soft over `#33304a` | **4.86:1** | comp `#384467` | 4.5 | ✅ |
| `--accent-ink-hover` `#8ed0ff` | 7.56:1 | `#33304a` | 4.5 | ✅ |
| `--text-invert` `#0d0e14` on `--accent` | 8.07:1 | `#54adff` | 4.5 | ✅ |
| `--ok` `#46e0a0` | 7.48:1 | `#33304a` | 4.5 | ✅ |
| `--warn` `#ffc46b` | 8.04:1 | `#33304a` | 4.5 | ✅ |
| `--danger` `#ff7585` | **4.89:1** | `#33304a` | 4.5 | ✅ |
| `--info` `#48cfe0` | 6.78:1 | `#33304a` | 4.5 | ✅ |
| `--focus-ring` `#6ec0ff` | 6.40:1 | `#33304a` | 3.0 | ✅ |
| ink on `--fill-bg` stop `#7cc4ff` / `#c58cf5` | 10.27 / 7.75 | fill stops | 4.5 | ✅ |

**Worst pair:** `--accent-ink` on the accent's own tint composited over the brightest
plate at **4.86:1** (need 4.5). The worst ground-bound pair is `--danger` at **4.89:1**.
Both clear their floors. `--accent-2` (violet `#b64ce8`) is a **fill / media / data-fill**
token and is never used as text; `--info` (`#48cfe0`) exists as the readable cyan.

## Signature motifs

Three, three different jobs, each drawn for the tile (base64 SVG where a gradient cannot
express the form):

1. **`--holographic-diffraction`** — the *material*. A hard-banded repeating spectrum
   ramp (cyan→blue→violet→magenta→pink→gold→lime→teal) with a dark land between every
   band: an infinite grating, not a single fade. A hard-stopped gradient expresses this
   exactly, which is why it is a gradient and not artwork.
2. **`--holographic-prism`** — the *geometry*. A beam enters a triangle and leaves as an
   ordered fan of hard bands. Drawn (base64 SVG): a fan diverges from a point, and a
   linear gradient cannot.
3. **`--holographic-aperture`** — the *glyph*. The reference's eight-bladed rainbow iris,
   a camera aperture that is also a spectrum wheel. Drawn: an aperture is arcs at angles a
   gradient cannot fake.

Non-flatness is reported in the build report (per-tile pixel standard deviation on
`--surface-2`); all three read as drawn, structured motifs against the tile base.

## Trade-offs

- **The ground is darker than the reference canvas.** The reference sits on a mid grey
  (`#414141`); a page ground that light cannot hold a 7:1 body text alongside a bright
  prismatic action, so the foil plates are deepened to `#33304a`→`#16171f`. The mid grey
  survives as `--surface` (`#252633`).
- **The glow is gone.** Every bloom in the source is a hard edge here. If you want the
  soft neon version, use `synthwave` — this kit is the crisp half of the same idea.
- **No `kit.css`.** Everything the kit needs is a token: the wash, the foil media panel,
  the recessed input, the hard bar/toggle shadows, the prismatic fill and the three drawn
  motifs. No stacked construction was required.

## When to use

Iridescent, futuristic, premium-tech branding: product launches, sci-fi and music media,
AI and dev-tool marketing, event and hardware identity — anything that should look like
foil catching light. Avoid it where the surface must feel calm, warm or trustworthy at
9am; for the smooth neon half of the decade's night, use `synthwave`.
