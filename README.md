# design-kits

Reusable visual themes for projects, for people **and** for AI agents. Each kit is a
self-contained palette + typography + shape spec, plus a live component lab so you can see
it before you commit to it.

Live gallery: https://ionshieldquad.github.io/design-kits/

## What a kit is

```
kits/<slug>/
├── DESIGN.md      # the spec — machine-readable tokens (YAML) + human rationale
├── tokens.css     # drop-in CSS custom properties — the thing you actually import
├── README.md      # stance, key choices, trade-offs, when to use it
├── index.html     # component lab (GENERATED — do not hand-edit)
├── tokens.json    # W3C DTCG export (GENERATED)
└── tailwind.theme.json   # Tailwind v3 theme export (GENERATED)
```

**One shared lab, many skins.** Every kit declares the *same* CSS variable names, so
`templates/lab.html` + `templates/lab.css` render any kit unchanged. The visual difference
is entirely `tokens.css`. That is what makes adding a theme cheap.

## Use a kit in a project

```html
<link rel="stylesheet" href="kits/quiet/tokens.css">
<link rel="stylesheet" href="kits/quiet/kit.css">   <!-- only if the kit ships one; most don't -->
```

`kit.css` is the escape hatch for a design whose identity lives in a *construction* rather than a
colour (layered panels, bespoke patterning). The build links it automatically when present — see
`docs/KIT-SPEC.md`. Everything else should be achievable from tokens alone; needing a `kit.css` is
the signal to check whether a contract token is missing.

Then write normal CSS against the variables — never against literal colours:

```css
.hero  { background: var(--bg);        color: var(--text); }
.cta   { background: var(--accent);    color: var(--text-invert); }
.panel { background: var(--surface);   border: 1px solid var(--border);
         border-radius: var(--radius-lg); }
```

## Tell an AI agent to use a kit

Point it at one file:

> Read `kits/quiet/DESIGN.md` and build the page using only those tokens.

`DESIGN.md` is Google's [DESIGN.md](https://github.com/google-labs-code/design.md) format
(Apache-2.0) — YAML front matter with normative values, markdown body with the reasoning.
Agents get exact values *and* the intent behind them. `AGENTS.md` in this repo says the same
thing in one screen.

## Add a new kit

```bash
mkdir kits/my-theme
$EDITOR kits/my-theme/DESIGN.md     # copy an existing one as a starting point
$EDITOR kits/my-theme/tokens.css    # define the token contract (see docs/KIT-SPEC.md)
python tools/build.py               # generates lab, gallery, exports; lints every kit
```

That's the whole loop. `tools/build.py` discovers kits by directory, so no registry to
update by hand. `docs/KIT-SPEC.md` is the authoring contract — required token names, section
order, palette limits.

## The kits

<!-- BEGIN KITS -->
| Kit | Tone | Use when |
|---|---|---|
| [`carbon`](kits/carbon/DESIGN.md) | dark · cool · technical · bold | portfolios, dev-tool marketing, anything that must look engineered |
| [`signal`](kits/signal/DESIGN.md) | dark · cool · technical · hud | dashboards, data-dense tools, resumes and CVs |
| [`quiet`](kits/quiet/DESIGN.md) | dark · app · minimal · soft | apps, settings panels, long-form reading |
| [`cyberpunk`](kits/cyberpunk/DESIGN.md) | dark · bold · technical · neon | games, music, nightlife, bold statements |
| [`summer-sunset`](kits/summer-sunset/DESIGN.md) | light · warm · retro · bold · synthwave | 80s synthwave poster — sunset sky, bold lines, orange · cyan · magenta. |
| [`chrome`](kits/chrome/DESIGN.md) | dark · metal · retro · bold · chrome | Liquid chrome on black — a metallic ramp, magenta action, cyan tertiary. |
| [`cyber-angel`](kits/cyber-angel/DESIGN.md) | light · sharp · bold · holo · geometric | hopeful product launches, AI/vision pages, bold light branding |
| [`geometric-dimensions`](kits/geometric-dimensions/DESIGN.md) | light · bold · geometric · retro | Bauhaus geometry lifted off the page on hard ink shadows |
| [`glass`](kits/glass/DESIGN.md) | light · soft · modern · glass | modern SaaS, overlays, hero cards |
| [`dark-glass`](kits/dark-glass/DESIGN.md) | dark · glass · soft · modern | Frosted panels over a violet-lit dark mesh |
| [`inside-the-machine`](kits/inside-the-machine/DESIGN.md) | dark · technical · mono · industrial · instrument | Machined instrumentation for a machine's interior |
| [`zen-garden`](kits/zen-garden/DESIGN.md) | light · calm · muted · organic · minimal | journaling, wellness, calm reading interfaces |
| [`outer-space`](kits/outer-space/DESIGN.md) | dark · cosmic · glowing · spacious | awe-led landing pages, science and space products, hero sections |
| [`kaleidoscope`](kits/kaleidoscope/DESIGN.md) | dark · kaleidoscope · faceted · multicolour | launch pages, games and music, gallery showcases |
| [`psychedelic`](kits/psychedelic/DESIGN.md) | light · psychedelic · organic · warm · retro · bold | gig and festival posters, album art and music brands, counterculture marketing, anything that should look screen-printed |
| [`glorious-morning`](kits/glorious-morning/DESIGN.md) | light · morning · fresh · bright · optimistic | morning-fresh product launches, wellness and productivity apps, children's and education products, anything that should feel like a clear start |
| [`cassette`](kits/cassette/DESIGN.md) | light · warm · retro · hardware · analogue | hardware, audio and device pages; anything that should feel like a physical panel rather than a screen |
| [`sakura`](kits/sakura/DESIGN.md) | light · spring · floral · fresh · bright · colourful | spring campaigns, florals and lifestyle brands that want real colour |
| [`gothic`](kits/gothic/DESIGN.md) | dark · bold · organic · editorial | music, subculture zines, nightlife, fashion/dark editorial |
| [`retro-anime`](kits/retro-anime/DESIGN.md) | dark · retro · anime · neon · synthwave · city-pop | night-time nostalgia: music, media and game pages, event and stream branding, anything that should feel like 1987 |
<!-- END KITS -->

## Token contract (v1)

| Group | Variables |
|---|---|
| Surfaces | `--bg` `--bg-2` `--surface` `--surface-2` `--overlay` |
| Text | `--text` `--text-muted` `--text-dim` `--text-invert` |
| Brand | `--accent` `--accent-hover` `--accent-2` `--accent-soft` |
| Status | `--ok` `--warn` `--danger` `--info` |
| Lines | `--border` `--border-strong` `--border-w` `--focus-ring` |
| Shape | `--radius-sm` `--radius-md` `--radius-lg` `--radius-pill` `--cut` |
| Type | `--font-display` `--font-body` `--font-mono` `--tracking-caps` |
| Depth | `--shadow-1` `--shadow-2` `--glow` `--blur` |
| Motion | `--dur` `--ease` |

Optional (the lab honours them when declared): `--clip` for a chamfered corner,
`--accent-ink` for a text-safe accent, `--text-on-surface` / `--text-on-surface-2`
(and `-muted`) for three-tier surface stacks where a card or an inset contrasts with the page.

A kit's own extra tokens are rendered in the lab: name them `--<slug>-*` (e.g.
`--chrome-gradient`, `--summer-sunset-sun`) and a **Signature** section shows them near the
top, so bespoke gradients and patterns are visible rather than merely declared.

Extras beyond the contract are allowed and ignored by the lab.

## Build / verify

```bash
python tools/build.py                 # generate labs, gallery, manifest + lint all kits
python tools/build.py --check         # fail if generated files are stale (CI)
npx -y -p @google/design.md designmd lint kits/quiet/DESIGN.md
node tools/verify-lab.cjs             # render every lab in headless chromium, write shots/
node tools/verify-lab.cjs carbon      # just one kit
```

`build.py` runs the official DESIGN.md linter on every kit and reports WCAG contrast
findings — that's the load-bearing reason to keep DESIGN.md authoritative.

`verify-lab.cjs` is the other half: it loads each lab in a real browser and fails if a token
is missing, a `{{placeholder}}` survived substitution, a `.card`/`.btn` didn't render, the
layout overflows horizontally, or a declared web font never loaded. It prints one JSON
verdict to `shots/verdict.json` and drops desktop + mobile + hero screenshots beside it.

CI (`.github/workflows/verify.yml`) runs both gates on every push.

## Deploy

Static output, no build step at serve time. Push to `main` → GitHub Pages serves the repo
root. `index.html` is the gallery.

## Credits

Token spec format: Google's DESIGN.md (Apache-2.0). Palettes for `carbon`, `signal` and
`quiet` are derived from existing projects of Lily Grinina's, used as reference ground truth.
