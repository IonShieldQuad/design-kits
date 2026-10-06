# Carbon

**Neon cyan on carbon black. Nothing round, everything cut. Mono labels, glowing actions.**

`01` · dark · `Space Grotesk · Orbitron · Inter` · source: derived from the msubinarylily portfolio

## Stance

Carbon is a machine bay, not a document. The ground is nearly colourless and the colour arrives
as light: a cyan wire that means "act" or "live", a violet wash that means "atmosphere", and
nothing else competing. Corners are cut with a `clip-path` chamfer instead of rounded, which is
the single gesture that makes the kit recognisable at thumbnail size.

Use it for portfolios, dev-tool marketing, and launch pages — anything that should look
engineered. Don't use it for long-form reading or for anything that needs to feel warm.

## Ground truth

Every value with a name in the source is the source's value:

| Token | Value | Source variable |
|---|---|---|
| `--bg` | `#0b0c10` | `--carbon` |
| `--bg-2` / `--surface` | `#13151c` | `--carbon-2` |
| `--text` | `#e6ebf2` | `--text-on-dark` |
| `--text-muted` | `#9aa6b4` | `--text-on-dark-dim` |
| `--accent` | `#00e5ff` | `--neon-cyan` |
| `--accent-2` | `#7c4dff` | `--neon-violet` |
| `--accent-soft` | `rgba(0,229,255,.16)` | `--neon-soft` |
| `--danger` | `#ff3d5e` | `--pole-hot` |
| `--info` | `#2f7bff` | `--pole-cold` |
| `--border` | `#2a2f3a` | `--line-dark` |
| `--accent-hover` | `#2ae9ff` | top stop of the primary button gradient |
| `--cut` | `14px` | `--cut` |
| `--ease` | `cubic-bezier(.22,.61,.36,1)` | `--ease` |
| `--text-invert` | `#04121a` | the literal the source paints on neon |
| `--blur` | `blur(16px) saturate(1.35)` | the sticky header's `backdrop-filter` |

## Derived, and why

- **`--surface-2: #1a1e27`** — the source has no third surface step. It is `--carbon-2` lifted
  one visible notch so inputs and nested panels separate from cards. It is the only surface
  value that is not literally in the source.
- **`--text-dim: #6f7b8a`** — the source's `--ink-dim` is a *light-surface* ink and is
  unreadable on carbon. Dim is `--text-muted` pulled toward the ground; it is for captions and
  placeholders only and is not contrast-guaranteed.
- **`--overlay: rgba(5,6,9,.74)`** — the board, darkened. The source's scrims are inline
  `rgba(11,12,16,α)` values; this is the same idea as one token.
- **`--ok: #3ddc97`, `--warn: #ffc46b`** — the source only ships cold/hot poles and neon.
  Status needs a green and an amber; both are chosen to sit at the same saturation as the
  rest of the palette rather than to introduce a new voice.
- **`--border-strong: #3b424f`** — `--line-dark` lifted, because an input rim has to read
  against `--surface-2`, not against the board.

## Deliberate deviations

- **Nothing is round.** `--radius-sm/md/lg/pill` are all `0px`, so badges and avatars render
  as squares in the shared lab. That is the kit working as intended: the chamfer is the only
  corner treatment in the language. (The lab's toggle switch and progress bar are hardcoded
  round in `templates/lab.css` and stay round for every kit.)
- **`--text-invert` is a near-black ink, not white.** The source paints `#04121a` on neon
  because full cyan is a fill colour, not a surface for white text.
- **Orbitron is not the display font.** The source reserves it for the wordmark and HUD labels
  (`--font-tech`, kept in `tokens.css` as an extra). It is requested in `fonts_url` and
  reported in `fonts_label`, but the shared lab does not exercise it — Orbitron at paragraph
  size would be unreadable.
- **The lab does not clip corners.** `templates/lab.css` cannot know about `--cut`, so the
  chamfer is opt-in: apply `clip-path: var(--clip)` (or `--clip-btn` on controls) yourself, and
  draw borders as two clipped layers — a clip-path slices a 1px border off across the diagonal.
  `--cut`, `--cut-lg` and `--clip-btn` are all present so the decision is one declaration.

## Contrast

| Pair | Ratio | Target |
|---|---|---|
| `--text` on `--bg` | 16.3:1 | ≥ 7 ✓ |
| `--text-muted` on `--surface` | 7.4:1 | ≥ 4.5 ✓ |
| `--text-invert` on `--accent` | 12.3:1 | ≥ 4.5 ✓ |

`--text-dim` measures 4.2:1 on a card and the status colours are status-only; both are
decorative/status and carry no guaranteed ratio.

## Trade-offs

- A near-black ground costs you the ability to use shadow for hierarchy. Carbon spends glow
  instead, which is a 1-value idea — easy to over-apply. Keep one glowing thing per screen.
- Zero radii plus clip paths means every plated component needs the two-layer border trick to
  look stroked. That is more CSS than a rounded card, and it is the whole point of the kit.
- Four font families is on the edge of the quality bar. It is defensible here only because
  each face has a hard boundary (display / body / instrument / logotype) and the lab exercises
  three.
