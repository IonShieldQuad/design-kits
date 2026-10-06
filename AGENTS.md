# AGENTS.md — design-kits

You are looking at a library of reusable UI themes. Before writing any UI code, pick a kit
and read its spec.

## Pick

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
<!-- END KITS -->

## Rules

1. Read `kits/<slug>/DESIGN.md` and use **only** the tokens it defines. Do not invent
   hex values or font sizes.
2. In new projects, link `kits/<slug>/tokens.css` once and reference `var(--token)`
   everywhere. Never inline a literal colour that a token already covers.
3. Token names are a fixed contract (`docs/KIT-SPEC.md`). If you need a new token, add it to
   the kit's `tokens.css` **and** its `DESIGN.md`, then run `python tools/build.py`.
4. `index.html`, `tokens.json`, `theme.css` and `tailwind.theme.json` inside a kit directory
   are generated, and so is the picker table above. Edit `DESIGN.md` / `tokens.css` /
   `kit.json` and re-run the build instead.
5. The gallery number (`01`, `02`, …) is derived from `kit.json`'s `order` — don't hand-number.
6. Check contrast before shipping: `npx -y -p @google/design.md designmd lint kits/<slug>/DESIGN.md`.

## Add a kit

Create `kits/<slug>/` with `DESIGN.md`, `tokens.css`, `README.md`; run `python tools/build.py`.
Full contract: `docs/KIT-SPEC.md`.
