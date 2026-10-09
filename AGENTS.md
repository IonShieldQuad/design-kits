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
| [`inside-the-machine`](kits/inside-the-machine/DESIGN.md) | dark · technical · mono · industrial · textured | consoles, telemetry, firmware/device tooling, teardown docs, hardware dashboards |
| [`zen-garden`](kits/zen-garden/DESIGN.md) | light · calm · muted · organic · minimal | journaling, wellness, calm reading interfaces |
| [`outer-space`](kits/outer-space/DESIGN.md) | dark · cosmic · glowing · spacious | awe-led landing pages, science and space products, hero sections |
| [`kaleidoscope`](kits/kaleidoscope/DESIGN.md) | dark · kaleidoscope · faceted · multicolour · glossy | launch pages, games and music, gallery showcases |
| [`psychedelic`](kits/psychedelic/DESIGN.md) | light · psychedelic · organic · screen-print · retro · bold | gig and festival posters, album art and music brands, counterculture marketing, anything that should look screen-printed |
| [`glorious-morning`](kits/glorious-morning/DESIGN.md) | light · morning · fresh · bright · optimistic | morning-fresh product launches, wellness and productivity apps, children's and education products, anything that should feel like a clear start |
| [`cassette`](kits/cassette/DESIGN.md) | light · warm · retro · hardware · analogue | hardware, audio and device pages; anything that should feel like a physical panel rather than a screen |
| [`sakura`](kits/sakura/DESIGN.md) | light · spring · floral · fresh · bright · colourful | spring campaigns, florals and lifestyle brands that want real colour |
| [`gothic`](kits/gothic/DESIGN.md) | dark · romantic · ornate · feminine · velvet | dark romance, beauty/fashion editorial, nightlife, witchy or vampire branding, music |
| [`synthwave`](kits/synthwave/DESIGN.md) | dark · retro · neon · synthwave · city-pop | night-time nostalgia: music, media and game pages, event and stream branding, anything that should feel like 1987 |
| [`city-pop`](kits/city-pop/DESIGN.md) | light · retro · city-pop · pastel · sunset · 80s | daytime nostalgia for music, media and lifestyle pages: album and stream branding, editorial features, anything that should feel like a Tokyo bay in the afternoon |
| [`win98`](kits/win98/DESIGN.md) | light · retro · windows · desktop · ui · pixel · 90s | a page that should FEEL like a 1998 desktop OS — nostalgic product pages, retro dev tools, easter-egg modes, anything that wants grey chrome and one navy title bar |
| [`pixel-dmg`](kits/pixel-dmg/DESIGN.md) | light · retro · pixel · gameboy · monochrome · arcade | retro-computing and emulator pages, chiptune and game tools, playful portfolios and 8-bit microsites that want one screen and four greens |
| [`tropical-breeze`](kits/tropical-breeze/DESIGN.md) | light · warm · tropical · playful · coastal · rounded | holiday and travel pages, lifestyle, food and family products, kids' and summer software — anything that should feel like a warm afternoon on the coast |
| [`mecha-pilot`](kits/mecha-pilot/DESIGN.md) | dark · mecha · hud · military · cockpit · instrumentation | military / flight HUD interfaces: sim and game UI, telemetry and mission consoles, weapon and sensor dashboards, anything that should read as a green instrument panel with a nominal/caution/critical ladder rather than a page |
| [`race-motion`](kits/race-motion/DESIGN.md) | dark · sport · motorsport · bold · geometric · high-contrast | speed, sport and competition: race and esports coverage, motorsport team pages, timing and telemetry dashboards, launch pages that need to feel loud and precise |
| [`kawaii`](kits/kawaii/DESIGN.md) | light · pastel · playful · cute · rounded · sticker | playful consumer and creator products — kids' and hobby apps, chat and community surfaces, sticker/emoji tooling, and landing pages that should feel fun rather than premium |
| [`radioactive`](kits/radioactive/DESIGN.md) | light · industrial · hazard · technical · clinical · toxic | institutional danger: industrial, safety, monitoring and telemetry dashboards, ops and incident UIs, science/medical tooling, anything that should feel like a controlled — not a cosy — environment |
| [`retro-anime`](kits/retro-anime/DESIGN.md) | light · retro · anime · shoujo · celestial · pastel | retro-romantic and magical: fan and fandom pages, game and visual-novel UI, zine and event branding, anything that should feel like a 90s shoujo title card |
| [`space-noir`](kits/space-noir/DESIGN.md) | dark · retro · poster · noir · print · cinematic | cinematic, adult, poster-grade branding — music and film pages, album and event covers, editorial features, anything that should feel like a printed 90s poster |
| [`holographic`](kits/holographic/DESIGN.md) | dark · iridescent · prismatic · futuristic · chrome · glow | iridescent, futuristic, premium-tech branding — product launches, sci-fi and music media, AI/dev-tool marketing, anything that should look like foil catching light |
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
