#!/usr/bin/env node
/**
 * design-kits · lab verification harness
 *
 * Loads every kit's component lab in a real headless Chromium, checks that the kit's tokens
 * actually took effect (no missing variables, no unstyled page), captures desktop + mobile
 * screenshots, and prints ONE machine-checkable JSON verdict.
 *
 *   node tools/verify-lab.cjs                 # all kits
 *   node tools/verify-lab.cjs carbon signal   # named kits only
 *
 * Why this exists: a lab page can render "fine" while half the tokens silently fall back,
 * or while a font import fails and every heading quietly becomes system-ui. Text asserts
 * nothing here — we read computed styles and the font-loading API.
 *
 * Windows note: launch the bundled Chromium by path (there is often no system Chrome).
 */
const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");
const KITS_DIR = path.join(ROOT, "kits");
const OUT = process.env.KIT_SHOTS || path.join(ROOT, "shots");

// playwright-core ships with the Hermes install; fall back to a normal resolve.
function loadPlaywright() {
  const candidates = [
    process.env.PLAYWRIGHT_CORE,
    "C:/Users/Lily/AppData/Local/hermes/hermes-agent/node_modules/playwright-core",
    "playwright-core",
    "playwright",
  ].filter(Boolean);
  for (const c of candidates) {
    try { return require(c); } catch (_) { /* next */ }
  }
  throw new Error("playwright-core not found — set PLAYWRIGHT_CORE to its directory");
}

function findChromium() {
  if (process.env.CHROMIUM_PATH && fs.existsSync(process.env.CHROMIUM_PATH)) return process.env.CHROMIUM_PATH;
  const { homedir } = require("os");
  const bases = [
    process.env.PLAYWRIGHT_BROWSERS_PATH,
    path.join(process.env.LOCALAPPDATA || "", "ms-playwright"),
    path.join(homedir(), ".cache", "ms-playwright"),
    path.join(homedir(), "Library", "Caches", "ms-playwright"),
  ].filter((b) => b && fs.existsSync(b));
  for (const base of bases) {
    const dirs = fs.readdirSync(base).filter((d) => d.startsWith("chromium-")).sort().reverse();
    for (const d of dirs) {
      for (const rel of [
        "chrome-win64/chrome.exe", "chrome-win/chrome.exe",
        "chrome-linux/chrome", "chrome-linux64/chrome",
        "chrome-mac/Chromium.app/Contents/MacOS/Chromium",
      ]) {
        const p = path.join(base, d, rel);
        if (fs.existsSync(p)) return p;
      }
    }
  }
  return null;
}

// Token contract v1 — mirrored from tools/build.py
const REQUIRED_TOKENS = [
  "--bg", "--bg-2", "--surface", "--surface-2", "--overlay",
  "--text", "--text-muted", "--text-dim", "--text-invert",
  "--accent", "--accent-hover", "--accent-2", "--accent-soft",
  "--ok", "--warn", "--danger", "--info",
  "--border", "--border-strong", "--focus-ring", "--border-w",
  "--radius-sm", "--radius-md", "--radius-lg", "--radius-pill", "--cut",
  "--font-display", "--font-body", "--font-mono", "--tracking-caps",
  "--shadow-1", "--shadow-2", "--glow", "--blur",
  "--dur", "--ease",
];

const VIEWPORTS = [
  { name: "desktop", width: 1280, height: 900 },
  { name: "mobile", width: 390, height: 844 },
];

async function main() {
  const only = process.argv.slice(2).filter((a) => !a.startsWith("-"));
  const { chromium } = loadPlaywright();
  const exe = findChromium(); // null ⇒ let the package resolve its own bundled build (CI)
  fs.mkdirSync(OUT, { recursive: true });
  const launchOpts = exe ? { executablePath: exe, headless: true } : { headless: true };
  const browser = await chromium.launch(launchOpts);
  const slugs = fs.existsSync(KITS_DIR)
    ? fs.readdirSync(KITS_DIR).filter((d) => fs.existsSync(path.join(KITS_DIR, d, "index.html")))
    : [];
  const targets = only.length ? slugs.filter((s) => only.includes(s)) : slugs;

  const report = { browser: exe, chromium: browser.version(), kits: [], verdict: "pass" };

  for (const slug of targets) {
    const file = path.join(KITS_DIR, slug, "index.html");
    const entry = { slug, errors: [], warnings: [], consoleErrors: [], missingTokens: [], fallbackTokens: [], fonts: {}, shots: [] };

    for (const vp of VIEWPORTS) {
      const ctx = await browser.newContext({ viewport: { width: vp.width, height: vp.height }, deviceScaleFactor: 2 });
      const page = await ctx.newPage();
      page.on("pageerror", (e) => entry.errors.push(`${vp.name}: ${e.message}`));
      page.on("console", (m) => { if (m.type() === "error") entry.consoleErrors.push(`${vp.name}: ${m.text()}`); });
      page.on("requestfailed", (r) => entry.consoleErrors.push(`${vp.name}: requestfailed ${r.url().slice(0, 90)}`));

      await page.goto("file:///" + file.replace(/\\/g, "/"), { waitUntil: "load" });
      await page.evaluate(() => document.fonts.ready);
      await page.waitForTimeout(350);

      if (vp.name === "desktop") {
        // 1. do the tokens resolve, or is the page silently running on lab.css fallbacks?
        const tokenCheck = await page.evaluate((names) => {
          const cs = getComputedStyle(document.documentElement);
          const body = getComputedStyle(document.body);
          const missing = [], fallback = [];
          for (const n of names) {
            const v = cs.getPropertyValue(n).trim();
            if (!v) { missing.push(n); continue; }
            // an undefined var() with a fallback still computes — compare against the lab default
            if (v === "0px" && n.endsWith("radius")) fallback.push(`${n}=0px`);
          }
          return {
            missing,
            fallback,
            bodyBg: body.backgroundColor,
            bodyColor: body.color,
            accent: cs.getPropertyValue("--accent").trim(),
            displayFont: cs.getPropertyValue("--font-display").trim(),
            cardBg: (document.querySelector(".card") ? getComputedStyle(document.querySelector(".card")).backgroundColor : ""),
            cards: document.querySelectorAll(".card").length,
            buttons: document.querySelectorAll(".btn").length,
            swatches: document.querySelectorAll(".swatch").length,
            swatchHeights: Array.from(document.querySelectorAll(".swatch"))
              .map((e) => Math.round(e.getBoundingClientRect().height)),
            captionOverflow: Array.from(document.querySelectorAll(".swatch span"))
              .some((e) => e.scrollWidth > e.clientWidth + 1),
            overflowX: document.documentElement.scrollWidth > window.innerWidth + 1,
            placeholders: Array.from(document.querySelectorAll(".masthead h1, .card-title"))
              .map((e) => e.textContent).filter((t) => t && t.includes("{{")),
          };
        }, REQUIRED_TOKENS).catch((e) => ({ error: e.message }));

        Object.assign(entry, {
          missingTokens: tokenCheck.missing || [],
          fallbackTokens: tokenCheck.fallback || [],
          computed: {
            bodyBg: tokenCheck.bodyBg, bodyColor: tokenCheck.bodyColor, accent: tokenCheck.accent,
            displayFont: tokenCheck.displayFont, cardBg: tokenCheck.cardBg,
            cards: tokenCheck.cards, buttons: tokenCheck.buttons, swatches: tokenCheck.swatches,
 swatchHeights: tokenCheck.swatchHeights,
          },
        });
        if (tokenCheck.overflowX) entry.errors.push("desktop: horizontal overflow (scrollWidth > viewport)");
        if (tokenCheck.placeholders && tokenCheck.placeholders.length)
          entry.errors.push(`desktop: unsubstituted placeholders: ${tokenCheck.placeholders.join(", ")}`);
        if ((tokenCheck.cards || 0) === 0) entry.errors.push("desktop: no .card rendered");
        if ((tokenCheck.buttons || 0) === 0) entry.errors.push("desktop: no .btn rendered");
        const hs = tokenCheck.swatchHeights || [];
        if (hs.length > 1) {
          const min = Math.min(...hs), max = Math.max(...hs);
          if (max > min * 1.35)
            entry.errors.push(`desktop: swatch cells uneven (${min}px..${max}px) — a caption is wrapping into a tall block`);
        }
        if (tokenCheck.captionOverflow) entry.errors.push("desktop: a swatch caption overflows its cell");

        // 2. did the declared web fonts actually load?
        //    NOTE: fonts.check('16px "X"') answers for ONE weight — Google serves a face per
        //    weight, so a 400 probe returns false while the 700 face is loaded. Ask per face
        //    instead, and treat "family declared but zero faces ever fetched" as the failure.
        entry.fonts = await page.evaluate(async () => {
          await document.fonts.ready;
          const cs = getComputedStyle(document.documentElement);
          const SYSTEM = /^(system-ui|-apple-system|BlinkMacSystemFont|sans-serif|serif|monospace|ui-monospace|inherit|Segoe UI|Arial|Georgia|Times New Roman|Roboto|Helvetica Neue|Inter|Cascadia Mono|Consolas|SFMono-Regular|Menlo|Courier New)$/i;
          const firstOf = (v) => (v || "").split(",")[0].trim().replace(/^["']|["']$/g, "");
          // only the FIRST family of each stack is the intended font — everything after it is a
          // deliberate fallback chain (Cascadia Code, Consolas, ui-monospace …) and must not be asserted on
          const declared = [firstOf(cs.getPropertyValue("--font-display")),
                            firstOf(cs.getPropertyValue("--font-body")),
                            firstOf(cs.getPropertyValue("--font-mono"))]
            .filter((s) => s && !SYSTEM.test(s));
          const faces = {};
          for (const f of document.fonts) {
            faces[f.family] = faces[f.family] || { loaded: 0, unloaded: 0 };
            faces[f.family][f.status === "loaded" ? "loaded" : "unloaded"]++;
          }
          const files = performance.getEntriesByType("resource")
            .map((r) => r.name).filter((n) => n.includes("fonts.gstatic.com"));
          const families = {};
          for (const fam of [...new Set(declared)]) {
            const key = Object.keys(faces).find((k) => k.toLowerCase() === fam.toLowerCase());
            families[fam] = {
              loadedFaces: key ? faces[key].loaded : 0,
              unloadedFaces: key ? faces[key].unloaded : 0,
              fileRequested: files.some((u) => u.toLowerCase().includes(fam.toLowerCase().replace(/[^a-z]/g, ""))),
            };
          }
          return { families, gstaticFiles: files.length, googleCss: performance.getEntriesByType("resource").filter((r) => r.name.includes("fonts.googleapis.com")).length };
        }).catch((e) => ({ error: e.message }));

        // a declared family with no faces at all, or no face ever loaded, means every heading
        // silently fell back to a system font — the exact bug a screenshot will not reveal
        for (const [fam, st] of Object.entries(entry.fonts.families || {})) {
          if (!st.loadedFaces && !st.fileRequested) entry.errors.push(`desktop: webfont never served: ${fam}`);
          else if (!st.loadedFaces) entry.warnings.push(`desktop: webfont declared but no face loaded: ${fam}`);
        }
      }

      const shot = path.join(OUT, `${slug}-${vp.name}.png`);
      await page.screenshot({ path: shot, fullPage: vp.name === "desktop" });
      entry.shots.push(path.relative(ROOT, shot).replace(/\\/g, "/"));
      await ctx.close();
    }

    // desktop viewport-only crop of the masthead: what the gallery thumbnail has to sell
    const ctx = await browser.newContext({ viewport: { width: 1280, height: 1180 }, deviceScaleFactor: 2 });
    const page = await ctx.newPage();
    await page.goto("file:///" + file.replace(/\\/g, "/"), { waitUntil: "load" });
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(250);
    const hero = path.join(OUT, `${slug}-hero.png`);
    await page.screenshot({ path: hero });
    entry.shots.push(path.relative(ROOT, hero).replace(/\\/g, "/"));
    await ctx.close();

    entry.status =
      entry.errors.length || entry.missingTokens.length || entry.consoleErrors.length ? "fail" : "pass";
    if (entry.status === "fail") report.verdict = "fail";
    report.kits.push(entry);
    console.log(`${entry.status === "pass" ? "PASS" : "FAIL"}  ${slug}` +
      (entry.missingTokens.length ? `  missing: ${entry.missingTokens.join(",")}` : "") +
      (entry.warnings.length ? `\n      warn: ${entry.warnings.join("\n      warn: ")}` : "") +
      (entry.errors.length ? `\n      ${entry.errors.join("\n      ")}` : ""));
  }

  await browser.close();
  const verdictPath = path.join(OUT, "verdict.json");
  fs.writeFileSync(verdictPath, JSON.stringify(report, null, 2));
  console.log(`\nverdict: ${report.verdict.toUpperCase()}  (${report.kits.length} kits) → ${verdictPath}`);
  process.exit(report.verdict === "pass" ? 0 : 1);
}

main().catch((e) => { console.error("HARNESS FAIL:", e.message); process.exit(2); });
