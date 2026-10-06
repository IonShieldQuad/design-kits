# Signal

**A deep-navy HUD. Brand cyan for action, mint and amber for status, mono for anything that is
a fact.**

`02` · dark · `Chakra Petch · Inter · JetBrains Mono` · source: derived from the resume site

## Stance

Signal is an instrument panel. The ground is a near-black navy with a blue cast; panels are
navy panes cut with a 16px chamfer; every label, number and badge is set in mono so the page
reads as a readout. Cyan is the single action colour, blue is the second accent, and mint +
amber are status lights that never carry a primary action.

Use it for dashboards, consoles, résumés and data-dense tools. It holds up at small type and in
tables — the one thing the other two kits in this family deliberately avoid.

## Ground truth

| Token | Value | Source variable |
|---|---|---|
| `--bg` | `#05070d` | `--bg0` |
| `--bg-2` | `#0b1322` | `--bg2` |
| `--text` | `#eaf3ff` | `--text` |
| `--text-muted` | `#8ea3c4` | `--muted` |
| `--text-dim` | `#5f7396` | `--dim` |
| `--accent` | `#37d7ff` | `--c-cyan` |
| `--accent-2` | `#4a9dff` | `--c-blue` |
| `--ok` | `#43ffb4` | `--c-mint` |
| `--warn` | `#ffc46b` | `--c-amber` |
| `--info` | `#8b6cff` | `--c-vio` |
| `--border` | `rgba(130,180,255,.16)` | `--line` |
| `--radius-md` | `6px` | `--radius` |
| `--cut` | `16px` | `--cut` |
| `--shadow-2` | `0 18px 50px rgba(0,0,0,.28)` | the `.panel` shadow |
| `--glow` | `0 0 14px rgba(55,215,255,.4)` | the pressed-switch glow |
| `--blur` | `blur(10px)` | the topbar `backdrop-filter` |

## Derived, and why

- **`--surface: #0c1426` and `--surface-2: #101b32` are the source's panel colours without
  alpha.** The source declares `--panel: rgba(12,20,38,.82)` and `--panel-2: rgba(16,27,50,.55)`
  because they sit over a *fixed gradient* background with radial washes. The shared lab page is
  flat, and a low-alpha navy over near-black composites to almost nothing — cards would vanish.
  So the kit publishes the opaque panel colours and keeps the frosted signature with
  `--blur: blur(10px)`. The original rgba values are preserved as `--panel` / `--panel-2` extras
  if you do have a gradient underneath.
- **`--text-invert: #04121a`** — the ink the source paints on cyan. It is a derivation only in
  the sense that the source writes it as a literal; nothing else on cyan clears AA.
- **`--accent-hover: #5fe0ff`** — the source has no hover token for cyan (its hovers change
  background, not the brand). Lifted one visible step from `--c-cyan`.
- **`--danger: #ff6b7a`** — the source ships no red at all. A status system without one is
  incomplete; this red is set at the same saturation as the amber so it joins the palette
  instead of shouting over it.
- **`--border-strong: rgba(130,180,255,.34)`** — the source's `--line` at double alpha, for
  input rims and emphasised dividers.

## Deliberate deviations

- **Panels are flattened** (see above). This is the one place the kit knowingly trades the
  source's exact CSS for a lab that actually shows the cards. Both forms ship: opaque in the
  contract tokens, translucency in the extras.
- **`--text-dim`, `--border` and `--border-strong` are in `tokens.css` but not in the
  DESIGN.md `colors` map.** The DESIGN.md component schema has no `borderColor` property and a
  tertiary caption asserts no contrast floor, so listing them would only generate orphan
  warnings for values that are very much in use. Their values are stated in DESIGN.md prose.
- **Chakra Petch is display-only.** Body is Inter at 1.6; Chakra Petch below ~18px turns into
  decoration.
- **The lab does not clip corners.** `--cut: 16px` + `--clip-corner` are opt-in, exactly as in
  the source, where the polygon is applied per-component rather than globally.

## Contrast

| Pair | Ratio | Target |
|---|---|---|
| `--text` on `--bg` | 18.0:1 | ≥ 7 ✓ |
| `--text-muted` on `--surface` | 7.2:1 | ≥ 4.5 ✓ |
| `--text-invert` on `--accent` | 11.1:1 | ≥ 4.5 ✓ |

`--text-dim` (3.8:1 on a panel) is a caption/placeholder colour and is treated as WCAG-exempt,
matching the source's own use of `--dim` for metadata only.

## Trade-offs

- Flattening the panels loses a little of the source's depth. It is the right call for a kit
  that has to work as a drop-in on any page; keep the rgba extras if you have the gradient.
- Four accent hues (cyan, blue, violet) plus two status colours is more colour than the quality
  bar would normally allow. It is disciplined here only because the roles are disjoint — the
  lab shows cyan, blue, mint and amber all doing different jobs on one screen without any of
  them competing.
- The corner cut and the small radii fight slightly: a 6px radius next to a 16px chamfer can
  look accidental if both appear on the same element. Keep radii on inputs and badges, chamfers
  on panels.
