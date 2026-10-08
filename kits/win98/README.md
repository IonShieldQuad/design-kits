# Windows 98

**Tagline:** Windows 95/98 desktop chrome — grey face, hard 3D bevels, navy title bar.
**Mode:** light · **Contract:** v1 · **Signature tokens:** `--win98-titlebar`,
`--win98-desktop`, `--win98-bevel-out`, `--win98-bevel-in`

## Stance

One grey plastic part, one bevel, one navy bar. This is a skin for the last desktop UI that
was *drawn* rather than *rendered*: every edge is a hard 1px step with no anti-aliasing, every
control is cut proud of the face or milled into it, and a single navy gradient caption tells you
what is active. The kit reproduces that with modern tokens — no bitmaps, no JavaScript, no
`kit.css`.

## Key choices

- **The bevel is the whole design.** `--shadow-1`, `--shadow-2`, `--glow` and `--input-inset`
  are all **inset** two-tone constructions (white top-left / near-black bottom-right, plus the
  classic `#dfdfdf` / `#808080` inner step). No token carries a blurred shadow — a 1998 toolkit
  had none. `--shadow-2` adds a *hard* `2px 2px 0` block for floating dialogs, never a blur.
- **`--glow` carries a bevel, not a glow.** The shared lab wires `--glow` to `.btn-primary`'s
  `box-shadow`. There is no glow in this UI, so the token holds the raised *navy* bevel instead.
  The name is the contract's; the value is ours.
- **Square, always.** `--radius-sm/md/lg/pill` are all `0px`. A single rounded corner would break
  the illusion, so even badges are squares.
- **Navy does double duty.** `#000080` is dark enough to work as a fill *and* as text (8.8:1 on
  the grey face), so `--accent-ink` is the same navy rather than a separately darkened cousin.
  The hover step stays navy (`#0000a0`) on purpose — see the warning below.
- **The white well is a real third tier.** Fields, code and badges are `#ffffff`, exactly as a
  text field was a white recess in the grey shell. Because that is a light-inside-light stack,
  `--text-on-surface-2` and `--text-on-surface-2-muted` are declared explicitly.
- **Historical values, moved only for legibility.** The palette is the 16-colour VGA set
  (`#c0c0c0` face, `#000080` caption, `#008080` desktop). Two values moved and both are measured:
  the "yellow" olive `#808000` is 4.19:1 on the white well, so it ships as `#6b6b00` (5.63:1);
  the alert red ships as the classic maroon `#800000` (10.9:1) because pure `#ff0000` is 4.0:1 —
  both stay inside the same family.
- **No smooth surfaces, including the lab's own defaults.** The lab v1.1 hooks are set to kill
  its two built-in gradients: `--wash` is the flat face colour (the default is a smooth radial
  accent bloom), and `--media-bg` is the 2px 50% **dither** (`repeating-conic-gradient(#000080 0
  25%, #c0c0c0 0 50%) 0 0 / 2px 2px`) with `--media-op: 1`, replacing the default two-stop accent
  gradient. A smooth blend is the one thing that instantly reads as "modern", not 1998.

## Contrast — measured, not eyeballed

Every pair is the WCAG ratio of the rendered colours. The `--bg` gradient is graded at **every px
stop**; the masthead's `--accent-soft` wash is **composited over its ground** before the
`--text-dim` ratio is taken.

| Pair | Ground | Ratio | Target |
|---|---|---|---|
| `--text` on `--bg` stop `#d8d5d0` | top of page | 14.35:1 | ≥ 7 |
| `--text` on `--bg` stop `#cecbc6` | | 12.98:1 | ≥ 7 |
| `--text` on `--bg` stop `#c4c1bc` | | 11.70:1 | ≥ 7 |
| `--text` on `--bg` stop `#c0c0c0` | darkest stop | 11.54:1 | ≥ 7 |
| `--text` on `--surface` (`#d4d0c8`) | cards | 13.66:1 | ≥ 7 |
| `--text` on `--surface-2` (`#ffffff`) | the well | 21.00:1 | ≥ 7 |
| `--text-muted` on the darkest `--bg` stop | | 6.94:1 | ≥ 4.5 |
| `--text-muted` on `--surface-2` | | 12.63:1 | ≥ 4.5 |
| `--text-dim` on the darkest `--bg` stop | | 6.25:1 | ≥ 4.55 |
| `--text-dim` on `--surface-2` | | 11.37:1 | ≥ 4.55 |
| `--text-dim` on `--wash` (`#c0c0c0`) | masthead ground | 6.25:1 | ≥ 4.55 |
| `--accent-ink` on the darkest `--bg` stop | | 8.80:1 | ≥ 4.5 |
| `--accent-ink` on `--surface-2` | | 16.01:1 | ≥ 4.5 |
| `--text-invert` on `--accent` (`#000080`) | primary button | 16.01:1 | ≥ 4.5 |
| `--text-invert` on `--accent-hover` | | 13.93:1 | ≥ 4.5 |
| `--ok` on `--surface-2` | | 5.14:1 | ≥ 4.5 |
| `--warn` on `--surface-2` | | 5.63:1 | ≥ 4.5 |
| `--danger` on `--surface-2` | | 10.95:1 | ≥ 4.5 |
| `--info` on `--surface-2` | | 6.34:1 | ≥ 4.5 |
| `--focus-ring` on the darkest `--bg` stop | | 8.80:1 | ≥ 3 |

Worst pair on a required path: **`--ok` on `--surface-2`, 5.14:1** (target 4.5) — the green lamp
on the white well, then `--text-dim` at 6.25:1. Every required pair clears with margin. No
carve-out is needed: the kit has no inverted ground, so one `--text-dim` covers every surface
including the white well.

## Signature tiles

Four `--win98-*` tokens render as ~168×72 tiles on `--surface-2`. All four are **background**
values, so the lab paints them rather than applying them, and each is structurally non-flat
(`--win98-bevel-out` / `--win98-bevel-in` are literal 2px edge constructions, not shadow values).
Per-tile pixel standard deviation is recorded in the delivery report.

## Trade-offs / limitations

- **Every button variant is beveled, because the lab was fixed rather than the kit.** The lab
  previously applied `box-shadow` exclusively to `.btn-primary` (via `--glow`), so
  `.btn-secondary`, `.btn-ghost` and `.btn-danger` had no shadow slot and read as flat bordered
  controls. That was a missing *contract token*, so the lab gained `--btn-shadow` (applied to all
  variants) and this kit declares it — rather than a `kit.css` override, which the contract
  forbids for exactly this case.
- **The active caption (title bar) has no lab component.** Its gradient lives in
  `--win98-titlebar` and appears in the Signature strip; the lab's `.nav`, `.tabs` and
  `.btn-primary` carry the navy in fill form. There is no `.window` markup to attach a real title
  bar to, so the token *is* the title bar here.
- **No `kit.css`.** Everything above is expressible with tokens, which is the point — a kit that
  needs a stylesheet to look like itself is a front-end, not a skin.
- **Two variants are deliberately not beveled.** `--btn-shadow` gives the raised edge to every
  button variant, but *ghost* and *link* carry no fill and no border, so there is nothing for a
  bevel to sit on — a raised outline around empty space reads as a bug, not as chrome. The kit's
  claim is therefore "every filled control is a moulded Win98 button", not "every element".
- **Native controls are squared by tokens.** `--check-appearance: none` plus the `--check-*` box
  tokens turn the checkbox and radio into squares; without them the browser draws round radios and
  the kit's one absolute rule ("nothing is round") would be false.

## When to use

Nostalgia with a straight face: retro dev-tool pages, product pages with a `.exe`-era gag, easter-
egg modes, or anything that should feel like it ran on a beige tower in 1998. Pair it with content
that is genuinely nostalgic — the chrome is loud about its decade and earns nothing if the copy
isn't in on the joke.

## Files

`tokens.css` · `DESIGN.md` · `kit.json` · `README.md`. Generated: `index.html`, plus
`tokens.json` / `tailwind.theme.json` / `theme.css` on an exporting build.
