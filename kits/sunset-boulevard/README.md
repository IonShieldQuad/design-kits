# Sunset Boulevard

**An instrument deck on a city floor at midnight.** A violet-framed slab of opaque indigo, corners
cut at 18px, its face carrying the place's own perspective grid with its horizon at 62% of the card's
height — so the grid lands on the card's floor and the deck reads as a piece of the plane it stands
on. One warm object in the whole kit: the amber sun in the scene.

- Kit: `sunset-boulevard` · order `225` · mode `dark`
- Fonts: Chakra Petch · JetBrains Mono
- Tags: `dark` `outrun` `night` `retro-future` `neon`
- Source: **derived** from the user's `bespoke-desktop` Li//OS prototype
  (`prototypes/v9-lilythium`, place 07) — palette, panel construction and drawn motif taken from the
  prototype's own tokens, not re-invented here.

## Stance

This is a *place*, not a decade. `Li//OS` is one desktop with fifteen rooms and one grammar: a
hairline frame, an opaque face carrying a sheen band, a bottom occlusion band, a 157° face fall, a 5%
accent tint, one drawn texture, one accent hue, one signature motif. Everything in this kit comes out
of that grammar unchanged — the pane below is the desk's own `.card-in` ported to tokens, layer for
layer. What this place adds is the **plane**: the ground is not a backdrop, it is a floor that
recedes, and the card is a slab cut out of it.

So the register is an outrun night city seen from a deck: violet #B06CFF as the system colour, a
near-black indigo ground, 1px frames, chamfered corners, and one amber sun that is allowed to be the
only warm thing in the room.

## Lineage — the Li//OS desk family

| place | kit | order | accent | face | ground | shape | motif |
|---|---|---|---|---|---|---|---|
| 01 | `azure-technologies` | 205 | `#4FD8FF` | `#0A0F16` | `#05080D` | chamfer 16 | hex lattice |
| 02 | `mainframe-access` | 210 | `#54E08A` | `#04100A` | `#020704` | square | scanlines |
| 05 | `pastel-district` | 215 | `#FF8FC4` | `#23141D` | `#160C13` | round 6 | bokeh |
| 06 | `crimson-labyrinth` | 220 | `#FF4D5E` | `#140A0C` | `#090305` | octagon 12 | engraved rose |
| **07** | **`sunset-boulevard`** | **225** | **`#B06CFF`** | **`#150C28`** | **`#0A0512`** | **chamfer 18** | **perspective grid** |
| 08 | `viridian-fields` | 230 | `#147A57` | `#0C1410` | `#0A1512` | round 5 | engraved fern |

The axis that separates this place from its five siblings is **depth**: it is the member of the
family whose ground is a *plane in perspective* rather than a field. `azure-technologies` is a lattice
you read across, `mainframe-access` a raster you read down, `crimson-labyrinth` an engraving that
glows from the face; this one recedes, and the recession continues *inside* the cards because the
grid is part of the card material.

### Against the two retro siblings already in the library

The library already had `synthwave` (125) and `city-pop` (130), so this kit has to say exactly what
it is that they are not. It is a different **object**, not another palette of the same one:

| | `synthwave` (125) | `city-pop` (130) | **`sunset-boulevard` (225)** |
|---|---|---|---|
| register | an 80s poster: the page *is* the artwork | a daylight sleeve: airy, pastel, printed | an **instrument deck** standing on a floor |
| structure | a sunset band across the page top, then night | cream → pale horizon → sky-blue, low surface contrast | an opaque, hairline-framed, 18px-chamfered face on a receding ground |
| action colour | magenta `#ec4b8f` | coral `#d62f4b` | violet `#B06CFF` |
| second hue | cyan `#44a6d7` (technology) | teal `#1f9aa8` (water) | amber `#FFB84D` (the sun — and the warning colour) |
| the sun | a drawn hero motif in the system's own vocabulary | part of the sleeve SVG | one small plate in `.card-media`; never a wash, never a control |
| shape | 3–10px radii, no chamfer | 5–16px radii, no chamfer | **0 radii, 18px chamfer, 1px frames** |
| where the grid lives | the page ground | — | **the card's own material**, anchored to its floor |
| type | Audiowide · Rajdhani · Share Tech Mono | Sora · Manrope · Space Mono | Chakra Petch · JetBrains Mono (the desk's face) |

Put plainly: `synthwave` is a picture of the night, `city-pop` is a picture of the day, and this is
the piece of hardware you operate at midnight. If you want the picture, take one of those; if you want
the interface under it, take this.

## What the material is

`--surface` is `--sunset-boulevard-pane`, and it is a *layer stack*, not a fill. Top first, which is
also the light model:

1. **top wash** — `rgba(255,255,255,.12)` fading to nothing by 24%: the deck's ceiling catching light.
2. **the pink bloom** — a radial anchored *below* the card, `radial-gradient(120% 64% at 50% 116%)`
   at `rgba(255,106,213,.34)`. This is the sun coming up off the boulevard through the floor, and it
   is the reason this kit's card is not the family's default stack.
3. **the dark ramp** — the face colour to `rgba(7,3,18,.80)` at the bottom, so the bloom sits behind
   depth instead of on top of it.
4. **the texture** — `--sunset-boulevard-tex`, the perspective grid, pinned to the card's own floor
   at 62% of its height and applied at .09.
5. **the identity edge** — the neon ramp, `rgb(255,106,213) → rgb(161,92,255) → rgb(58,201,255)`,
   full width at opacity 1. Pink, violet and cyan in one 1px line: it is the kit's signature, and the
   only place those two extra hues are allowed to appear.
6. **the face** — `rgb(13,7,34)`, the rendered value. The stylesheet declares `#150C28`; the page
   paints this.

There is no 9% occlusion band and no 157° fall here: the bloom and the ramp do that work, and the
desk switches both defaults off for this place. The order still matters — the bloom sits under the
dark ramp, so it reads as light coming through material rather than as a sticker on the face.

`--surface-2` — inputs, badges, alerts, code blocks, `card-elevated` — is the *nested* tier and drops
layers 3 and 4: a 240-unit perspective drawing on a 2.5rem control is clutter, not material. It keeps
a shallow sheen (`rgba(255,255,255,.06)` → 0 at 60%), half the tint (`.04`) and the panel colour
`#120B1C`, one step up from the face.

Every surface is opaque, so `--blur: none`. The desk forbids glass and `backdrop-filter`, and a
blurred opaque card is only a repaint cost.

## The motif, with its numbers

The motif is the place's own `--tx-persp`, pasted verbatim from `docs/lilythium/textures.css` (no
redraw, no re-encode, no re-alpha — the desk applied `--txA` as a pseudo-element opacity, which a
background layer cannot do, and the folding is already verified at gallery-tile size). The drawing is
a 240 × 150 box: nine converging verticals from a vanishing point at (120, 28) and six horizontals at
42, 52, 66, 84, 108 and 138, stroked white at 0.7.

| | card (`--sunset-boulevard-tex`) | ground (`--sunset-boulevard-tex-ground`) |
|---|---|---|
| size | `100% 62%` | `200% 100%` |
| position | `50% 100%` — anchored to the card's bottom edge | `50% 0` — anchored to the top of the page |
| stroke alpha | `0.06` | `0.033` |
| horizon (the vanishing point) | 38% down the card + 28/150 of the band = **~49.6% of the card's height** | 28/150 of the viewport height |
| pitch | one 240-unit box = the full card width | one 240-unit box = **half** the viewport width |

Two scales, two jobs: the card carries the motif at the desk's own pitch and a 6% stroke because it is
the card's *material*; the ground carries it at half the alpha and twice the pitch because it is the
*room*. Equal weight would make the page one busy field and every card read as texture inside texture.
The ground additionally carries a 120px technical grid at `rgba(255,255,255,.028)` (verticals) and
`.024` (horizontals), and two soft fields of `#231040` — all percentage-sized, never px, because the
gallery renders `--bg` into a ~118px tile and a px-anchored scene would show the tile its top edge
only.

`--sunset-boulevard-field` is the whole ground, and `--bg` is nothing but that token, so the page, the
signature tile and the media plate cannot drift apart.

## The one warm object

The amber `#FFB84D` is the sun from the place's own scene, and it is the second accent. It appears in
exactly three places: `--accent-2` (the second stop in charts, the warm end of the progress ramp), the
`.card-media` place plate (`--media-bg`: the slat sun over the card-pitch grid on the face, at
`--media-op: 1`), and `--warn`. It is never a wash behind text and never a control. The slat cutting
is the face colour drawn across the disc in a `repeating-linear-gradient`, which is how the scene
draws it — five dark bars across the lower half, widening as they descend.

## Contrast — measured, not eyeballed

Every pair below is computed on resolved token values (WCAG 2.1 relative luminance) against **the
composited ground it actually sits on**, never against a declared tint. The card grounds are
composited: face `#150C28` + 5% violet + the 157° fall's white stop at the top-left, which is the
lightest ink ground in the kit (`#382D4B`); `surface-2` is `#120B1C` + 4% violet + 6% white
(`#261D32`); the tinted grounds are `--accent-soft` (16%) over the card (`#4B3768`) and over
`surface-2` (`#3C2A53`).

| foreground | required | worst ground it lands on | measured |
|---|---|---|---|
| `--text` `#F2EBFF` | ≥ 7:1 | card's lit band | **10.96:1** (17.35 on the ground) |
| `--text-muted` `#C9B8E6` | ≥ 4.5:1 | card's lit band | **6.95:1** |
| `--text-dim` `#AE9CCB` | ≥ 4.55:1 | card's lit band | **5.10:1** |
| `--accent-ink` `#CFA4FF` | ≥ 4.5:1 | `--accent-soft` over the card | **5.07:1** |
| `--accent-ink-hover` `#E0C4FF` | ≥ 4.5:1 | `--accent-soft` over the card | **6.58:1** |
| `--text-invert` `#12081F` on `--accent` | ≥ 4.5:1 | — | **5.96:1** (7.76:hover) |
| `--ok` `#45E0B0` | ≥ 4.5:1 | `surface-2` | **9.59:1** |
| `--warn` `#FFB84D` | ≥ 4.5:1 | `surface-2` | **9.34:1** |
| `--danger` `#FF5C7A` | ≥ 4.5:1 | `surface-2` | **5.40:1** |
| `--info` `#66D9FF` | ≥ 4.5:1 | `surface-2` | **9.89:1** |
| `--focus-ring` `#CFA4FF` | ≥ 3:1 | `bg` ground | **8.53:1** |
| `--accent-2` `#FFB84D` | ≥ 3:1 (graphical) | `surface-2` | **9.34:1** |

No value needed tuning to reach these: the token set as authored is clean. `--accent` `#B06CFF` is a
mid-light fill (5.46:1 against the card face), which is why `--text-invert` is a near-black ink
`#12081F` rather than white (white would be 3.26:1, under AA for a 14px label).

## Key choices

- **Violet is the action; amber is the scene.** `--accent` `#B06CFF` is the desk's own system violet
  and the only colour that asks to be clicked. `--accent-2` is the sun. `--danger` `#FF5C7A` is a warm
  pink-red, so it separates from the violet action by hue as well as by role.
- **The one collision, and it is deliberate.** `--warn` **is** `--accent-2` (`#FFB84D`), because the
  amber in this place is the sun and the warning light at once. The rule that keeps it honest: amber
  is a **status colour and a scene colour, not an action colour**. A warning chip may be amber; a
  button may not.
- **`--accent-ink` exists because the fill fails as a label.** `#B06CFF` is a fine fill but a poor
  small label on a violet-tinted card; `#CFA4FF` (the desk's `--accHi`) is the text member of the same
  family, and every eyebrow, link, active nav item and secondary-button label routes through it.
- **Cut, never rounded.** `--cut: 16px` with the family's own `--clip`, which cuts the **top-left and
  bottom-right** corners on the diagonal (the desk's asymmetric chamfer, not four symmetrical
  corners); `--radius-sm/md/lg` are `0px`,
  `--radius-pill` and `--check-radius` are `2px` so badges, chips, checkboxes and radios square up
  with the deck instead of quietly contradicting it.
- **The frame is drawn, not bordered.** `clip-path` removes the border along the diagonal, so the lab
  paints the frame as a `--frame-ring` polygon derived by `build.py` from this kit's own `--clip`, in
  the component's own border colour at `--border-w: 1px`. Verified in Chromium: the ring arrives and
  is applied to `.card::before`, and the diagonal keeps its line.
- **`--focus-inset: 2px`.** The same clip eats `outline`, so keyboard focus is painted inside the
  silhouette. Without it a chamfered kit has no visible focus state at all.
- **The nested tier drops the grid.** See above: 240-unit perspective on a 40px control reads as a
  printing fault, not as material.
- **Type is shared by the whole family on purpose.** Chakra Petch (display and body) + JetBrains Mono
  (labels, keys, readouts) is the desk's own pairing. These six kits are rooms in one operating
  system, and the type *is* the operating system — changing it per kit would be the one thing that
  makes them look like six unrelated themes. Change it in all of them or in none.

## Trade-offs

- **`clip-path` costs the drop shadow.** A chamfered card's `box-shadow` is clipped at the silhouette,
  so `--shadow-1`/`--shadow-2` read as weight under the slab rather than as a soft halo. That is the
  intended reading here (the deck is cut out of the plane), but a project wanting a floating card
  should use a sibling that rounds.
- **The frame is a ring, so it has no "outside".** Nothing may sit in the 1px the chamfer takes —
  an outline, a focus halo or a badge hanging off the corner is clipped away.
- **The nested tier is materially poorer than the deck.** Inputs and code blocks are plates, not
  slabs. That is correct for their size, but a page that is mostly forms will look like a flatter
  kit than a page that is mostly cards.
- **The ground is quiet on purpose.** At half the card's alpha and twice its pitch, the field token's
  signature tile reads as a dark chip with a violet bloom rather than as a pattern — it is the *room*,
  and the panes are where the material is. Do not raise its alpha "until it shows": the brief fixes
  those values and they were verified at 360 × 118.
- **Amber cannot be a CTA.** A project that wants a warm primary button is asking for a different kit
  (`summer-sunset`), not an override of this one — here that button would read as a warning.
- **One texture, two scales, no second motif.** The kit's identity is a single drawing used twice at
  two pitches. There is no rose, no lattice, no second device to reach for; anything a project adds
  will look like a sticker on the deck.

## When to use

Night-time nostalgia with an interface under it: music, media and game pages, event and stream
branding, album and festival microsites, portfolios and tools that should feel like a city at 1987
midnight — and, because it is a deck rather than a poster, dashboards and app shells in that register
too.

Use a sibling instead when: you want the **poster** of that night → `synthwave`; the **daylight
sleeve** → `city-pop`; the **heat** → `summer-sunset`; the **hardware** → `cassette`; a **calm,
light, clinical** product → `quiet`, `glass`; another room of this same OS → any other Li//OS place.

## Linter warnings kept deliberately

`python tools/build.py --only sunset-boulevard --no-export` reports these, and they are kept:

- `contrast-ratio: textColor (#cfa4ff) on backgroundColor (#b06cff29) has contrast ratio 1.62:1`
  (**three times**: `badge-accent`, `button-secondary-hover`, `nav-item-active`). The linter grades the
  tint's **declared** rgba instead of compositing it over what is behind it. Composited over the card's
  lightest band the pair is `#CFA4FF` on `#4B3768` = **5.07:1**, and `tools/verify-lab.cjs` — which
  samples the real rendered pixels next to every text box — passes the kit with no contrast errors.
- `orphaned-tokens`: `neutral`, `scene`, `scene-floor`, `surface-solid`, `border-strong`. `neutral`,
  `scene` and `scene-floor` document the ground ramp the whole kit is graded against; `surface-solid`
  is the print / no-filter stand-in; `border-strong` is the violet hairline (`--accLine`) used by
  secondary buttons and input focus in `tokens.css`. None of them is a component fill, which is the
  only thing the rule can see.
- `token-summary` — informational, not a finding.

No errors. `--accent-ink`, `--clip`, `--focus-inset`, `--check-radius`, `--media-bg`/`--media-op` and
`--fill-bg` are all declared, so the lab has the full optional set it needs for a chamfered, opaque,
non-smooth-surface kit.

## Files

Authored: `DESIGN.md`, `tokens.css`, `kit.json`, `README.md`. Generated by `tools/build.py`:
`index.html` (component lab), `DESIGN.html`, and — on the exporting run — `tokens.json`, `theme.css`,
`tailwind.theme.json`. Do not hand-edit the generated set.
