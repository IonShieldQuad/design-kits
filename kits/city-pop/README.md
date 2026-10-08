# City Pop

**A Tokyo bay in daylight.** Cream sky warming through a pale horizon into sky-blue, the coral of
the sun on the water as the one action colour, and ocean teal for water, data and focus.

- Kit: `city-pop` · order `130` · mode `light`
- Fonts: Sora · Manrope · Space Mono
- Tags: `light` `retro` `city-pop` `pastel` `sunset` `80s`
- Source: original — re-tuned from a twilight draft to the daytime register the brief asked for

## Stance

City pop is a *place and an hour*, not just a palette: Tokyo, the bay, and the afternoon the sleeve
was photographed. The kit is built as that one scene — the page ground is cream warming to a pale
horizon and settling into sky-blue, and the three signature tokens are the three layers of the
scene: **sky, skyline, sea**.

It is deliberately the *daytime* member of the retro family. `synthwave` is this decade at night —
indigo, magenta, cyan neon, a striped sun over a wireframe grid. `summer-sunset` is this decade as a
saturated poster. City pop is the **airy, pastel, elegant** one: low contrast between surfaces,
hairlines instead of borders, soft radii, and no colour that shouts. Same decade, three registers.

## Contrast — measured, not eyeballed

Every pair below was computed on the **rendered** values (relative luminance, WCAG 2.1) against
*every* ground: all five `--bg` gradient stops plus `--surface` and `--surface-2`. The binding
ground is the **palest** stop, `#dceff3` — not the average and not the cream, because light ink on
a light kit fails at the top of the range.

| Foreground | Required | Worst ground | Measured |
|---|---|---|---|
| `--text` `#2f2a40` | ≥ 7:1 | `#dceff3` | **11.59:1** |
| `--text-muted` `#5d5670` | ≥ 4.5:1 | `#dceff3` | **5.84:1** |
| `--text-dim` `#6b6480` | ≥ 4.55:1 | `#dceff3` | **4.70:1** |
| `--accent-ink` `#a3203a` | ≥ 4.5:1 | `#dceff3` / its own 12% tint | **5.56 / 6.26:1** |
| `--text-invert` `#fff8f1` on `--accent` `#d62f4b` | ≥ 4.5:1 | — | **4.57:1** |
| `--ok` `#19784f` on grounds | ≥ 4.5:1 | `#dceff3` | **4.60:1** |
| `--warn` `#8a5a10` on grounds | ≥ 4.5:1 | `#dceff3` | **4.98:1** |
| `--danger` `#b3243a` on grounds | ≥ 4.5:1 | `#dceff3` | **5.47:1** |
| `--info` `#2c68c4` on grounds | ≥ 4.5:1 | `#dceff3` | **4.55:1** |
| `--focus-ring` `#1f7fa8` on grounds | ≥ 3:1 | `#dceff3` | **3.80:1** |

**Worst pair: `--text-dim` at 4.70:1** — the token behind every caption, hint and swatch label,
which is why it is the one held to ≥ 4.55:1.

The masthead carries an opt-in `--wash`, a translucent warm glow over the page's own daylight rather
than a plate. It is composited, so it was graded as a composite too: peak alpha is held at `.15` and
the wash is *lighter* than every stop it covers, so it can only raise contrast for the ink on top of
it rather than lower it.

No carve-out is needed: `--surface-2` here is a *warm inset*, not an inverting well, so a single
`--text-dim` clears both families.

`--accent` `#d62f4b` as a **fill** is 4.57:1 against the cream label — which is why it is darker than
the daylight around it. As a *small label* on cream it is under 4.5:1, which is exactly why
`--accent-ink`/`--accent-ink-hover` are declared. `--accent-2` `#1f9aa8` clears 3:1 (WCAG 1.4.11,
graphical objects) and is never used as body text.

## Key choices

- **Coral is a fill, not a label.** The action colour is set dark enough to carry a white label, and
  every text role routes through the lighter-*contrast* `--accent-ink` instead. This is the
  fill-vs-label split the contract asks for, and it is the reason the kit is not simply "sunset
  pink".
- **Every ink is graded against the blue stop.** In a light kit the binding ground is the *palest*
  one. `--text-dim` was solved against `#dceff3`, and `--ok`/`--info` were both deepened until they
  cleared it (they were 4.31 and 4.11 at first pass).
- **The ground is warm cream, never a neutral grey.** The palette is pulled toward cream and
  salt-blue because those are what the scene is made of.
- **Two accents, two jobs.** Coral `#d62f4b` = action; teal `#1f9aa8` = water, content and focus.
  Teal does focus duty because it survives on cream better than coral does.
- **No blur, no chamfer.** `--blur: none`, `--cut: 0px`. A sleeve is printed and airbrushed; its
  softness is in the radii (5–16px) and the curves of the drawn motifs, not in glass or bevels.
- **The sleeve keeps its sunset hour.** See below — the motifs are the album cover, and it is
  deliberate that they are warmer than the interface around them.

## The three signature devices

Each is drawn as base64 inline SVG with a colour base layer beneath, because a repeating gradient
cannot express any of them:

- `--city-pop-sky` — the **sky**: a vertical cream → coral → gold ramp with the sun low in the frame
  and soft cloud streaks across it. Drawn so the sun reads as a disc and the streaks as bands; a
  plain ramp reads as a wash of fog.
- `--city-pop-skyline` — the **city**: irregular rooftops, one antenna tower and a scatter of lit
  windows. Any tiling reads as crenellation, not a city.
- `--city-pop-sea` — the **bay**: hard horizontal water bands with the sun's broken reflection
  column stacked down the centre. The glitter path is structure, so it is drawn; a smooth ramp would
  read as a second sky. (This one took two attempts: the first read as an audio equaliser — detached
  uniform bars — until it became a continuous column cut by wavy water lines.)

Three motifs doing three different jobs (atmosphere, silhouette, surface). Three is the ceiling here
— the kit's whole premise is "one scene", and a fourth layer would crowd it.

**The motifs are the sleeve, and the interface is the room it is played in.** The drawn scene keeps
the warm sunset hour — which is what city-pop sleeve art actually depicts — while the UI ground stays
in daylight so body copy can live on it. The contrast between the two is the design, not an
oversight.

## Opt-in lab capabilities

- **`--media-bg` / `--media-op`** — the `.card-media` panel shows the whole sleeve as one
  **postcard**: a drawn SVG of the sky, the sun, the skyline and the bay with its glitter path.
  `--media-op: 1` lifts the lab's default `.85` dim so the scene reads at full strength. A media
  panel is exactly where a city-pop kit should show its scene rather than a generic accent ramp.
- **`--wash`** — the warm translucent glow on the masthead, described above.
- **`--bg` is left a clean gradient.** The lab accepts a full background layer list on `--bg` (an
  image plus its own size/position), and a drawn cloud band or coastal silhouette was tempting. It
  was declined on purpose: `--bg` is the ground every text token is measured against, and an image
  layer would raise the effective luminance of arbitrary pixels and break the 7:1 budget. The scene
  lives in the signature tokens and the media panel, where nothing sits on it.

## Trade-offs

- **The page cannot be the sleeve.** A UI cannot put body copy on a bright horizon, so the warmest
  stops live in the sky token and the media panel while the page ground stays light enough to read
  on. The sleeve is always warmer than any page that uses it.
- **The light register cost the palette its punch.** A daytime kit cannot have the saturated
  magenta-on-indigo contrast of the night kits; what it has instead is airiness. If you want the
  saturated version of this decade, that is `summer-sunset`.
- **Space Mono is a slab-ish mono.** It is a label and code face only; it never sets a heading.
- **The kit leans on drawn artwork for its identity.** Colours, type, shape and depth are all tokens,
  but the scene itself is three SVGs. That is legitimate per `docs/KIT-SPEC.md` (a motif is skin, not
  front-end) — but it does mean the kit is only as distinctive as those three tiles.
- **`--accent-2` is a fill/state token, never a label.** It clears 3:1, not 4.5:1.

## When to use

Daytime nostalgia with salt in the air: music, media and lifestyle pages, album and stream branding,
editorial features, portfolios that want warmth without weight. Avoid it for anything that must feel
clinical or night-time — that is `quiet`, `glass` or `dark-glass`. For this decade at **night**, use
`synthwave`; as a saturated **poster**, `summer-sunset`; in **hardware**, `cassette`.
