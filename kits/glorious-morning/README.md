# Glorious Morning

**First light as a UI kit.** A clear-sky gradient ground that opens on a gold dawn band inside
the first screen, a light-ray wash across it, and one sunrise-gold action colour against a clear
sky blue — with deep cool ink doing all the reading.

- **Mode:** light · **Order:** 105 · **Source:** original
- **Fonts:** Fraunces (display) · Nunito Sans (body) · DM Mono (labels)
- **Contract:** `docs/KIT-SPEC.md` v1 — every required token name is present in `tokens.css`,
  including `--border-w`.

## Stance

The library has three daylight kits now and the difference between them is **time of day and
energy**, not hue:

| Kit | Time | Feeling |
|---|---|---|
| `zen-garden` | overcast grey | quiet, static, restrained, desaturated |
| `summer-sunset` | dusk | synthwave, nostalgic, warm-dark, 2px poster lines |
| **`glorious-morning`** | **first light** | **clear, awake, optimistic, energetic** |

`glorious-morning` is the *fresh* one. It is bright rather than pastel-washed, energetic rather
than sleepy, and its material is **air and light** rather than paper or glass.

## Key choices

**The ground is air, not paper.** `--bg` is a very light *sky* tint — six stops of clear sky,
warm haze, gold and settling air — never cream (that is `summer-sunset`) and never plain white
(that is a document). The dawn band is the darkest stop, and that single fact drives the whole
ink scale.

**PX stops, so the dawn lands in the first screen.** The body's gradient box is the entire
document. A `0–100%` ramp would smear the six stops over thousands of pixels, so the first
screen would render one flat pale plate and the sunrise — the kit's entire reason to exist —
would sit far below the fold. Fixed `0px … 760px` stops keep the whole sequence in view at any
page length and any viewport. Unlike a % ramp, this is a gradient whose *signature is actually
visible*, which is the whole point.

**The dawn band is the contrast constraint, and the ink was NOT lightened to compensate.**
`#ffdf9e` (the gold band) is much darker than a white page — the other five stops run
13.1:1–15.4:1 for `--text`, but the band only reaches 12.6:1, and `--text-dim` clears 4.55:1
there at just 5.2:1. `#4d5d72` is the lightest cool slate that works, so the kit's tertiary
tier is a medium slate rather than the pale grey a "bright" palette invites. A bright,
low-contrast palette is exactly where light kits fail; the fix is a strong ink, never a
lighter one.

**Gold is a fill colour, and `--accent-ink` is its text colour.** This is the classic gold
trap: `#f0a90c` is an excellent button fill (**8.0:1** with deep navy on it) and an unreadable
small label (**~1.9:1** on the ground). So the kit ships a separate, much darker bronze of the
same family for accent-as-text — `--accent-ink: #7d5200` at 5.3:1 on the worst stop and 6.7:1
on `--surface`, with `--accent-ink-hover: #674300`. The eyebrow, links, active nav/tab,
secondary-button labels, inline code and `badge-accent` all use `--accent-ink`.

**Gold ≠ orange.** `#f0a90c` sits at hue **41°**; `summer-sunset`'s action orange `#ff7a1a` is
at hue **25°**. Same warmth, visibly different colour.

**Sunrise gold, clear-sky blue, leaf green — three roles, no rainbow.** Gold is the *one*
action colour (the sun arriving). Sky blue `#3a9be0` is the cool counterweight, carried by
`--accent-2` in gradients, bars, avatars and media — it is also the cool end of the sunrise
ramp. Fresh leaf green is the third and is **structural, not a call to action**: it appears as
`--ok` (`#187a43`, readable on every surface) and as the bright `--glorious-morning-leaf`
inside the dew sheen.

**Fraunces, because the kit should feel like a good morning and not a machine.** It is a warm
humanist soft-serif with an optical-size axis — it reads like a hand-set greeting card. Paired
with the rounded humanist Nunito Sans for body and the quiet DM Mono for labels. A neutral
grotesque would have made the palette feel clinical, which is precisely the failure mode for a
bright kit.

**Air is transparent, not translucent.** `--blur: none` and `--surface: #fbfdff` (opaque).
Nothing is frosted; the only translucency anywhere is the faint hairline.

## Signature material

All shipped as `--glorious-morning-*`. The six **material** tokens are declared in `kit.json`
`signature`, so the lab renders them in its **Signature** section; the two pale ground-stop
aliases are shipped and documented but deliberately not declared, because a ground stop painted
on the lab's own `--surface-2` chip is a 1.1:1 difference — an empty-looking tile.

| Token | What it is | In the lab |
|---|---|---|
| `--glorious-morning-sunrise` | the cool-sky → warm-gold ramp, **PX stops** so it reads in a short element | tile |
| `--glorious-morning-ray` | the light-ray wash — a `repeating-conic-gradient` of sun shafts | tile |
| `--glorious-morning-sun` | the low sun bloom, top-left of the first screen | tile |
| `--glorious-morning-dew` | the dew / fresh highlight; carries the one leaf green | tile |
| `--glorious-morning-leaf` | the bright leaf (`#38b26a`) — material only, never body text | tile |
| `--glorious-morning-halo` | a soft sunlit gold halo (a box-shadow extra, applied to a bevel) | tile |
| `--glorious-morning-sky` | the high clear sky stop (`#d6e9fc`) — ground-stop alias | not declared |
| `--glorious-morning-dawn` | the dawn band stop (`#ffdf9e`) — ground-stop alias | not declared |

## Trade-offs

- **One consciously-kept linter warning: `contrast-ratio` on `badge-accent`.** The linter
  compares a component's `textColor` against its `backgroundColor` with **alpha removed**, so
  `backgroundColor: rgba(240,169,12,0.16)` is scored as the *solid* gold `#f0a90c` and
  `--accent-ink` comes out at 3.37:1. That is a false positive: `--accent-soft` is a 16% wash,
  and composited over `--surface` the badge background is really `#f9f0d8`, where `--accent-ink`
  measures **6.00:1**. (The wash composites over the page ground, never over the solid accent —
  that pair is the only place in the kit where `#7d5200` ever sits on `#f0a90c`, and it does not
  happen in the lab.) Every light kit in this library carries this same class of warning —
  `zen-garden`, `glass` and `summer-sunset` all score **1.00:1** on it — so this is the mildest
  instance of a known artifact, not a defect. The warning is kept rather than "fixed" by
  darkening `--accent-ink` to the near-body-ink `#644000` the linter would demand.
- **The dawn band costs the tertiary ink.** Because the band is the darkest ground stop,
  `--text-dim` is a mid slate (`#4d5d72`) rather than a pale grey. This is intentional: the
  kit's brightness comes from the *ground*, not from weak ink.
- **`--glorious-morning-leaf` is 2.66:1 on `--surface`** — it is a decorative material stop
  (the tail of the dew gradient) and never carries text or meaning on its own. The readable
  green is `--ok` (`#187a43`, 4.8:1 on `--surface-2`). Noted here rather than darkened, since a
  bright leaf is the point.
- **The ground is heavier than a flat tint.** The kit spends its top ~500px on a gradient. That
  is a deliberate budget: it is what makes it recognisable in a 200×120 thumbnail.
- **No `--clip` / no chamfers.** The kit declares `--cut: 0px` and never sets `--clip`, so the
  shared lab's chamfer capability stays off. This is a rule, not an omission — see below.

## How it stays distinct

- **vs `zen-garden`** — zen-garden is an *overcast rainy day*: cool grey ground `#e8ecf0`, wet
  stone charcoal, a deep moss-sage action, thin hairlines, soft static shadows and a slow
  `.26s` ease. `glorious-morning` is the *same time-family of light kit with the weather
  inverted*: a clear sky that carries a gold dawn band, a **gold** action where zen-garden has
  sage, a snappier `.18s` motion, and warm shadow (the `--glow` sunlit halo) where zen-garden
  explicitly refuses any bloom. Zen-garden is stillness; this is the start.
- **vs `summer-sunset`** — summer-sunset is *dusk*: a warm sunset ramp that runs warm all the
  way down, **bold 2px aubergine outlines** doing the graphic work, synthwave orange `#ff7a1a`
  plus cyan plus magenta, and a retro display face (Audiowide). `glorious-morning` is cooler
  and softer at every level: a cool sky blue leads and the warmth is a *band of light*, the
  lines are **1px faint cool hairlines** (no bold line work at all), the palette is gold + sky
  blue + leaf green with no magenta or violet, and the display face is a humanist serif rather
  than a wide retro one.
- **vs `glass`** — glass is soft pastel **translucency**: `--surface` is `rgba(255,255,255,.58)`
  and `--blur: blur(20px) saturate(180%)` is load-bearing. Here `--surface` is opaque
  `#fbfdff` and `--blur: none`.
- **vs `cyber-angel`** — cyber-angel is a structural light shell: **black 1px rules**,
  **45° chamfers** (`--cut: 12px` + `--clip`), holo cyan. Here: **no black rules** (`--border`
  is a 14% cool-navy hairline) and **no chamfers** (`--cut: 0px`, `--clip` never declared).

## When to use

Morning-fresh product launches, wellness and habit apps, education and children's products,
onboarding and welcome flows, dashboards that should feel optimistic, anything that should feel
like a clear start.

**Don't** use it for night-time or after-dark surfaces, dense data tooling, or anything that
wants menace or weight.

## Files

| File | |
|---|---|
| `DESIGN.md` | normative values (YAML front matter) + rationale |
| `tokens.css` | the token contract |
| `kit.json` | gallery metadata incl. `signature` |
| `index.html` | generated component lab |
| `tokens.json`, `tailwind.theme.json`, `theme.css` | generated exports |

Regenerate with `python tools/build.py` from the repo root.
