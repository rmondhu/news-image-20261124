// Render tools/scene-hormuz-preview.html to tools/scene-hormuz-preview.png.
// Preview only — not the entry. Run from the entry directory:
//   node tools/render-preview.mjs
import fs from 'node:fs';
const { chromium } = await import('/home/hatch/workspace/makefun/tools/node_modules/playwright/index.mjs');
const out = process.argv[2] || 'tools/scene-hormuz-preview.png';
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 840, height: 900 }, deviceScaleFactor: 2 });
await page.goto('file:///home/hatch/workspace/makefun/entries/news-image-20261124/tools/scene-hormuz-preview.html', { waitUntil: 'load' });
await page.waitForTimeout(300);
await page.screenshot({ path: out, fullPage: true });
await browser.close();
console.log(out, fs.statSync(out).size);
