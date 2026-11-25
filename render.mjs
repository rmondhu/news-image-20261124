// Render render.html to entry.png (1024x1024) with Playwright/Chromium installed in home.
// Run from this directory:  node render.mjs   (writes entry.png here)
// Deterministic: fixed layout, no network, no random, no timestamps.
import fs from 'node:fs';
const { chromium } = await import('/home/hatch/workspace/makefun/tools/node_modules/playwright/index.mjs');
const out = process.argv[2] || 'entry.png';
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1024, height: 1024 }, deviceScaleFactor: 1 });
await page.goto('file:///home/hatch/workspace/makefun/entries/news-image-20261124/render.html', { waitUntil: 'load' });
await page.waitForTimeout(300);
await page.screenshot({ path: out });
await browser.close();
console.log(out, fs.statSync(out).size);
