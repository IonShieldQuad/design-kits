# AGENTS.md — design-kits

You are looking at a library of reusable UI themes. Before writing any UI code, pick a kit
and read its spec.

## Pick

| Kit | Tone | Use when |
|---|---|---|
| `carbon` | deep-space cyan/violet, cut corners, technical | portfolio, product marketing for dev tools |
| `signal` | deep-navy HUD, cyan + mint + amber, mono labels | dashboards, resumes, data-dense tools |
| `quiet` | near-black indigo, one soft accent, low drama | apps, settings panels, long-form reading |
| `cyber-angel` | light pearl + soft pastel glow, ethereal | calm/wellness, soft branding, hero sections |
| `summer-sunset` | warm coral→amber→violet gradients | friendly landing pages, events, consumer apps |
| `cyberpunk` | near-black + hot magenta/yellow/cyan, high contrast | games, music, bold statements |
| `glass` | translucent frosted panels over colour, subtle | modern SaaS, overlays, hero cards |

## Rules

1. Read `kits/<slug>/DESIGN.md` and use **only** the tokens it defines. Do not invent
   hex values or font sizes.
2. In new projects, link `kits/<slug>/tokens.css` once and reference `var(--token)`
   everywhere. Never inline a literal colour that a token already covers.
3. Token names are a fixed contract (`docs/KIT-SPEC.md`). If you need a new token, add it to
   the kit's `tokens.css` **and** its `DESIGN.md`, then run `python tools/build.py`.
4. `index.html`, `tokens.json` and `tailwind.theme.json` inside a kit directory are
   generated. Edit `DESIGN.md` / `tokens.css` and re-run the build instead.
5. Check contrast before shipping: `npx -y -p @google/design.md designmd lint kits/<slug>/DESIGN.md`.

## Add a kit

Create `kits/<slug>/` with `DESIGN.md`, `tokens.css`, `README.md`; run `python tools/build.py`.
Full contract: `docs/KIT-SPEC.md`.
