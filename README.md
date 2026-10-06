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
<link rel="stylesheet" href="kits/quiet/kit.css">   <!-- optional, if the kit ships one -->
```

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

## Token contract (v1)

| Group | Variables |
|---|---|
| Surfaces | `--bg` `--bg-2` `--surface` `--surface-2` `--overlay` |
| Text | `--text` `--text-muted` `--text-dim` `--text-invert` |
| Brand | `--accent` `--accent-hover` `--accent-2` `--accent-soft` |
| Status | `--ok` `--warn` `--danger` `--info` |
| Lines | `--border` `--border-strong` `--focus-ring` |
| Shape | `--radius-sm` `--radius-md` `--radius-lg` `--radius-pill` `--cut` |
| Type | `--font-display` `--font-body` `--font-mono` `--tracking-caps` |
| Depth | `--shadow-1` `--shadow-2` `--glow` `--blur` |
| Motion | `--dur` `--ease` |

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
