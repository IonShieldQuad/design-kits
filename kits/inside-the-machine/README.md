# Inside the Machine

**A machined instrument panel. Amber is the one thing that acts; green phosphor is everything
the machine reports; depth is engraved, not floating; and the mono carries the interface.**

`11` · dark · `IBM Plex Mono · IBM Plex Sans` · source: original

## Stance

This kit is the *interior* of a machine, not a product page about one. The ground is graphite
(#0d0f11), panels are milled into it, and every seam is an opaque 1px steel hairline — engraving
is subtractive, so the lines are cut, not lit. Two phosphor lamps do all the talking: **amber
(#ffb000) acts, green (#4dff9e) reports, red (#ff5147) faults.** Nothing floats: depth runs
inwards, with a lit top lip and a shadowed bottom lip on every recessed surface.

Use it for consoles, telemetry, device/firmware tooling, teardown docs, hardware dashboards and
anything whose subject is a system rather than a sentence. It is at its best with tables,
readouts, IDs and status rows — the lab's data section is the kit's home page, not its stress
test.

Four things make it recognisably *this* kit at 200×120:

1. **Mono-first typography.** In every other dark kit here the mono is a label font and a
   grotesque carries the headings. Here IBM Plex Mono sets the h1, the section headings, the
   eyebrows, the table headers, the badges and the metadata; IBM Plex Sans exists only for
   sentences.
2. **Engraved depth.** `--shadow-1` / `--shadow-2` are **inset** — lit top lip, shadowed bottom
   lip, deeper well for `card-elevated`. There is no soft outer drop shadow in the kit at all.
3. **Phosphor readouts on warm graphite.** Amber + green lamps over a neutral-warm charcoal,
   instead of Signal's cool navy or Cyberpunk's violet-black.
4. **Machined detail.** Opaque steel hairlines, `+0.12em` stamped caps labels, and radii capped
   at 4px so nothing reads soft.

## Ground truth

Every value below is authored for this kit; nothing is inherited from another kit's palette.

| Token | Value | Note |
|---|---|---|
| `--bg` | `#0d0f11` | graphite chassis |
| `--bg-2` | `#131719` | masthead gradient stop |
| `--surface` | `#16191d` | milled panel face |
| `--surface-2` | `#1b1f23` | recessed well, inputs |
| `--overlay` | `rgba(6,8,10,.78)` | modal scrim |
| `--text` | `#e9edef` | 16.3:1 on `--bg` |
| `--text-muted` | `#9aa4ad` | 7.0:1 on `--surface` |
| `--text-dim` | `#828d95` | 4.9:1 on `--surface-2` |
| `--text-invert` | `#0d0f11` | chassis ink on the amber plate |
| `--accent` | `#ffb000` | amber — the only action colour |
| `--accent-hover` | `#ffc233` | amber lifted one step |
| `--accent-2` | `#4dff9e` | green phosphor — readouts, media |
| `--accent-soft` | `rgba(255,176,0,.13)` | 13% amber tint, derived |
| `--ok` | `#4dff9e` | green phosphor: nominal |
| `--warn` | `#d99a2b` | amber held one step *down* |
| `--danger` | `#ff5147` | fault lamp |
| `--info` | `#6c99b8` | steel blue: data / telemetry |
| `--border` | `#2a2f35` | the machined seam (opaque) |
| `--border-strong` | `#4a535c` | input rim / emphasised rule |
| `--border-w` | `1px` | this kit is milled, not bold-line |
| `--focus-ring` | `#ffc233` | amber, one step lighter than action |
| `--radius-sm/md/lg` | `2px` / `3px` / `4px` | nothing softer than 4px |
| `--radius-pill` | `4px` | deliberate — see below |
| `--cut` | `0px` | no chamfers; the seam is the detail |
| `--shadow-1` | `inset 0 1px 0 rgba(255,255,255,.10), inset 0 -1px 0 rgba(0,0,0,.60), inset 0 2px 6px -3px rgba(0,0,0,.45)` | the recess |
| `--shadow-2` | `inset 0 1px 0 rgba(255,255,255,.13), inset 0 -1px 0 rgba(0,0,0,.68), inset 0 4px 14px -6px rgba(0,0,0,.60)` | the deeper well |
| `--glow` | `0 0 0 1px rgba(255,176,0,.45), 0 0 14px -2px rgba(255,176,0,.45)` | a lamp, not a shadow |
| `--blur` | `none` | machined metal is not frosted |

## Type: why the mono leads

- **IBM Plex Mono** is the display face, the label face and the readout face. It was drawn for
  engineering paperwork — it survives at 11px, it survives in a column, and it has a
  slightly-squared terminal that reads as stamped rather than drawn. Putting it on the h1 is the
  kit's whole position: on this machine even the title is a readout.
- **IBM Plex Sans** is the same superfamily, so nothing looks bolted on; it appears only where a
  human is reading a sentence (body copy, card bodies, hints).
- **One honest seam:** the shared lab styles `.btn` with `font: inherit`, so button text drawn
  in the lab comes from `--font-body`. The kit's *declared* button style is still the mono label
  (`{typography.label}` in `components:`), which is what a consumer copies. Recorded here rather
  than hidden: it is the one place where the shared lab's own inheritance overrides a kit's
  declared component face.
- **Stamped, not spaced.** Caps labels run `+0.12em` (`--tracking-caps`). Signal runs `0.14em`
  and Cyberpunk `0.18em`; stamping *compresses*, so this kit stays tighter than both.
- **Display tracking is `-0.01em`** — at 2.9rem a monospaced face will otherwise look loose.

## Derived, and why

- `--accent-hover: #ffc233` — one visible step up in lightness from `#ffb000`, same hue. A lamp
  getting brighter, not changing colour.
- `--accent-soft: rgba(255,176,0,.13)` — a 13% tint of `--accent`, expressed as `rgba()` rather
  than re-typed as a hex, because it is derivable and must stay in sync with the amber.
- `--warn: #d99a2b` — amber *held one step down*. The caution lamp and the action plate are the
  same family, but a stamp must never be as loud as a switch. This is also why `--warn` is not
  simply `--accent`.
- `--text-invert: #0d0f11` — the chassis ink. Amber is a fill, so the primary button's label is
  graphite, never white (white on `#ffb000` is ~1.6:1).
- `--border` / `--border-strong` are **opaque steel**, not translucent white. Every other dark
  kit in this set tints its hairlines; opaque steel is the engraved look and it is the reason
  the seams hold at 1px.
- `--radius-pill: 4px` — a stamped plate instead of a lozenge. The token keeps its contract name,
  but a fully round badge would read as a product-UI tag and undo the milled language. The
  shared lab's own switch keeps its hard-coded rocker, which is left alone deliberately.

### The shared lamps

`--ok` and `--accent-2` are the *same* green (`#4dff9e`), and that is the design: this machine
has one green lamp, and it means "nominal" whether it is filling a readout plate or lighting a
status chip. One lamp, one meaning. If you need a second green for something that does *not*
mean nominal, that is a sign the element should not be green.

## Contrast (verified numerically, not by eye)

Computed from `tokens.css` by script — see the verification log. WCAG relative-luminance ratio,
`(Lhi + .05) / (Llo + .05)`.

| Pair | Ratio | Target | |
|---|---|---|---|
| `--text` on `--bg` | **16.30:1** | ≥ 7 | ✓ |
| `--text-muted` on `--surface` | **6.96:1** | ≥ 4.5 | ✓ |
| `--text-invert` on `--accent` | **10.48:1** | ≥ 4.5 | ✓ |
| `--text-dim` on `--bg` | **5.66:1** | ≥ 4.55 | ✓ |
| `--text-dim` on `--surface` | **5.20:1** | ≥ 4.55 | ✓ |
| `--text-dim` on `--surface-2` | **4.89:1** | ≥ 4.55 | ✓ |

`--text-dim` clearing 4.55:1 on the *lightest* ground (`--surface-2`, the input well) is the
binding constraint: it is why the dim grey is `#828d95` rather than a darker, moodier value.
`--border` / `--border-strong` are deliberately below 3:1 (1.2–2.0:1) — they are decorative
seams, never the sole carrier of meaning.

## Trade-offs

- **The mono costs horizontal room.** IBM Plex Mono is wide, so the h1 and any tracked caps
  labels need more width than a grotesque would. Short labels and short titles are part of the
  kit, not an accident of the demo copy.
- **No outer shadow at all** means an element that genuinely must sit *above* the chassis (a
  modal, a tooltip) has no ready-made depth token and must lean on `--overlay` and `--glow`
  instead. That is intentional: this kit does not do floating layers.
- **`--radius-pill: 4px`** is a knowing bend of a token name. Consumers who assume "pill =
  999px" will get a square badge; that is the desired result here, and it is documented above.
  One visible consequence in the shared lab: `.badge` (pill) and `.badge-square` (`--radius-sm`,
  2px) now differ by 2px, so those two demos look near-identical. The kit is not distinguishing
  badges by roundness on purpose — it distinguishes them by colour.
- **Two amber tokens** (`--accent` and `--warn`) plus two uses of green (`--accent-2`, `--ok`)
  means a palette map shows repeats. The repeats are semantic, not accidental.
- **Amber as the action colour** is a warm choice in a field of cool dark themes. It is the
  fastest way to make the primary action findable on a graphite page, but it does mean the kit
  is a poor fit for a brand that already owns orange.

## Files

`DESIGN.md` (normative values) · `tokens.css` (the contract) · `kit.json` (gallery metadata) ·
`index.html`, `tokens.json`, `tailwind.theme.json`, `theme.css` (generated by
`python tools/build.py`).
