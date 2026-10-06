# Quiet

**Near-black indigo, one soft accent, small radii, and a lot of air.**

`03` · dark · `Inter` · source: derived from simple-website-test

## Stance

Quiet is the app chrome you stop noticing. It was a small business landing page — near-black
indigo ground, one periwinkle accent, 10–16px radii, no ornaments — and it is the right kit for
the surfaces you spend hours inside: settings, forms, dashboards that are mostly reading,
editors, long text.

The kit's whole method is *subtraction*. There is one accent, one family, no glow, no blur, no
gradients behind content, and a deliberately narrow radius scale. Hierarchy comes from spacing
and from the accent, in that order.

## Ground truth

| Token | Value | Source variable |
|---|---|---|
| `--bg` | `#0b0e13` | `--bg` |
| `--surface` | `#12161f` | `--panel` |
| `--border` | `#2a3140` | `--line` |
| `--text` | `#e8ecf3` | `--text` |
| `--text-muted` | `#b9c2d0` | `--muted` |
| `--accent` | `#5b7cfa` | `--accent` |
| `--accent-hover` | `#7390ff` | `--accent-hover` |
| `--danger` | `#ff8383` | `--danger` |
| `--dur` / `--ease` | `.15s` / `ease` | the source's button transition |
| radii | `6 / 8 / 12 / 999px` | the source's 10–16px chip / input / card scale, tightened |

## Derived, and why

- **`--surface-2: #171c27`** — the source has one panel step. Inputs and nested panels need a
  second, so it is `--panel` lifted one visible notch.
- **`--bg-2: #10141c`** — the ground, lifted. Used as the top stop of the masthead wash.
- **`--text-dim: #8a93a3`** — `--muted` desaturated and dropped toward the ground. Captions and
  placeholders only; it is not contrast-guaranteed.
- **`--text-invert: #0b0e13`** — *this is the one real deviation.* The source paints `#fff` on
  `--accent`, which measures **3.68:1** and fails WCAG AA. Inverting to the page ink measures
  **5.25:1** and keeps the accent exactly as the source shipped it. Changing the ink is a
  cheaper fix than changing the brand.
- **`--accent-2: #7d6ce8`** — the source has a single accent. Gradients and media plates need a
  second stop; one step around the wheel keeps it in the same family and keeps it out of the
  "second call to action" role.
- **`--ok: #5fbf8f`, `--warn: #e0b26b`, `--info: #6b93e0`** — the source only needed `--danger`.
  The other three are mixed at the same low saturation as `#ff8383` so status arrives as a tint
  rather than as a system colour.
- **`--border-strong: #3a4356`** — `--line` lifted, because an input rim has to read against
  `--surface-2`, not against the ground.
- **`--font-display`/`--font-body` are Inter**, not raw `Segoe UI`. Plain was the goal and
  Segoe UI is not portable — on a Mac or on Linux it silently becomes something else, which is
  the opposite of quiet. Inter keeps the plainness and makes it consistent.

## Deliberate deviations

- **Text on the accent is dark, not white** — see above. Most visible in the primary button.
- **`--text-dim`, `--border` and `--border-strong` are in `tokens.css` but not in the DESIGN.md
  `colors` map**, because the DESIGN.md component schema has no property that can reference a
  line colour and a tertiary caption asserts no contrast floor. Their values are stated in
  DESIGN.md prose.
- **`--glow` and `--blur` are literally `none`.** Both are required by the token contract; this
  kit's answer to them is the zero value, and that *is* the design.
- **`--cut: 0px`.** The chamfer belongs to Carbon and Signal. Mixing shape languages would make
  both arbitrary.

## Contrast

| Pair | Ratio | Target |
|---|---|---|
| `--text` on `--bg` | 16.3:1 | ≥ 7 ✓ |
| `--text-muted` on `--surface` | 10.1:1 | ≥ 4.5 ✓ |
| `--text-invert` on `--accent` | 5.25:1 | ≥ 4.5 ✓ |

The source's own `#fff` on `--accent` measures 3.68:1 — the reason `--text-invert` is inverted.
`--text-dim` measures a healthy 5.9:1 on a panel, so even the caption colour clears AA; it is
still scoped to captions because it is a *quiet* colour, not a contrast-limited one.

## Trade-offs

- Muted at 10:1 means the "secondary" text is nearly as loud as primary text. That is a choice:
  in a settings panel most copy *is* secondary, and greying it out is what makes dense UI tiring.
  Differentiate with size and weight instead.
- A single family means all differentiation is size + weight + spacing. In exchange there is no
  display/body mismatch to get wrong, and one webfont to load.
- No elevation at all means genuinely floating surfaces (menus, toasts) have to lean on their
  hairline and `--shadow-2`. That reads as under-designed in a marketing context — which is why
  this kit is scoped to tools, not landing pages.
