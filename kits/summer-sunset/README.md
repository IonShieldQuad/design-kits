# Summer Sunset

**Warm cream light, with a coral → amber → violet ramp.**

Part of [design-kits](../../README.md). Index `05`, order `50`, mode `light`, source `original`.

## Stance

The only warm light kit in the set. The ground is a cream-to-blush sunset-sky gradient, the
type is deep plum-brown, and every drop of heat lives in the accents: coral `#ff7a59` for
action, violet `#7b4bd8` as the cool counterweight, amber `#ffb347` in the middle of the
signature ramp. Rounded corners, generous padding, a soft serif for display.

Where a typical "warm" theme goes beige-and-orange and becomes unreadable, this one keeps the
ground and the prose calm and confines the sunset to the elements that can take it.

## Key choices

- **A gradient ground.** `--bg` is `linear-gradient(180deg, #fff8f1, #ffe8da 55%, #ffddcb)`,
  which reads as a whole sky behind the page. `--bg-2: #fff3e9` is the solid stand-in for
  exports and tools that cannot parse a gradient token.
- **Plum-brown text, not orange.** `--text` `#2b1d2f` hits **12.5:1** on the darkest ground
  stop and 15.1:1 on the lightest. Coral, amber and violet are never used for body copy.
- **Dark type on coral.** White on `#ff7a59` is ~2.6:1, so `--text-invert` is the same plum as
  the body text — **6.2:1** on the accent. Ink on a sunset postcard.
- **The full ramp is a token.** `--accent` (coral) and `--accent-2` (violet) drive the
  lab-visible gradients on media, progress bars and avatars; `--summer-sunset-ramp` carries
  all three stops as one gradient for downstream use, with `--summer-sunset-amber` as the
  middle value.
- **Warm shadows.** Every drop shadow is brown-tinted (`rgba(122,63,32,…)`), never black — this
  is the difference between "late afternoon" and "dirty".
- **Round and open.** 10 / 14 / 18px radii, 1.35rem card padding, `--dur: .22s` with an eased
  curve. `--cut: 0px`: no notches anywhere.

## Trade-offs

- **A gradient `--bg` invalidates the lab masthead's own `background` shorthand** (CSS does
  not allow a gradient as a colour stop inside another gradient), so the masthead renders
  transparent and the page gradient simply shows through, seamless. A side effect: the
  masthead loses its local coral accent wash in the shared lab; the coral still appears in
  the eyebrow, buttons, tints and banners. Deliberate and accepted — the full-sky ground is
  worth more than a local wash, and it is what makes the kit unmistakable at thumbnail size.
- **`--text-invert` equals `--text`.** Unusual on paper, correct in practice: it is the only
  way to keep AA on a coral accent without whitening the type. Don't "fix" it.
- **Status colours are darker than the brand set** (green `#1f8a5b`, amber-brown `#a86a12`,
  red `#d64545`, blue `#3f6fd8`) so they stay legible on warm white.
- **`--text-dim` is 3.6:1 on `--surface`** — captions and placeholders only, never body copy.

## Verification

Contrast (`docs/KIT-SPEC.md` targets; `--bg` checked against its darkest stop `#ffddcb` as the
worst case for dark type): `--text` on `--bg` **12.5:1** (≥7) · `--text-muted` on `--surface`
**5.9:1** (≥4.5) · `--text-invert` on `--accent` **6.2:1** (≥4.5). All token contract names
present. Builds clean with `python tools/build.py`.

`designmd lint`: **0 errors**. Warnings are `orphaned-tokens` only (status colours,
`--focus-ring`, and the spacing/rounding scales that the shared lab consumes straight from
CSS). Note that the `--bg` **gradient itself is not expressible in the DESIGN.md `colors:`
block** — that block only accepts CSS colours, so the three gradient stops ship as
`bg-stop-1/2/3` and the ramp stops as `ramp-coral/amber/violet`. The gradients themselves live
in `tokens.css`.

## Use when

Landing pages, events and ticketing, consumer and lifestyle apps, food and travel branding,
onboarding, anything that should feel like a good morning. Not for dense data tooling or
anything that needs a cool, clinical voice.
