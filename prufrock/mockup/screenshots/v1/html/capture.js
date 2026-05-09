const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const HTML_DIR = path.join(__dirname);
const OUT_DIR = path.join(__dirname, '..');

const files = [
  ['01-seed-panel.html', '01-seed-panel.png'],
  ['02-timeline-mid.html', '02-timeline-mid.png'],
  ['03-timeline-complete.html', '03-timeline-complete.png'],
  ['04-lineage-full.html', '04-lineage-full.png'],
  ['05-lineage-path.html', '05-lineage-path.png'],
  ['06-map-full.html', '06-map-full.png'],
  ['07-poem-sidebyside.html', '07-poem-sidebyside.png'],
  ['08-participant.html', '08-participant.png'],
];

(async () => {
  const browser = await chromium.launch();
  const context = await browser.newContext({
    viewport: { width: 1440, height: 900 },
    deviceScaleFactor: 2,
  });

  for (const [html, png] of files) {
    const page = await context.newPage();
    const url = 'file://' + path.join(HTML_DIR, html);
    await page.goto(url, { waitUntil: 'networkidle' });
    await page.waitForTimeout(300);
    const outPath = path.join(OUT_DIR, png);
    await page.screenshot({ path: outPath, fullPage: false });
    await page.close();
    console.log(`✓ ${png}`);
  }

  await browser.close();
  console.log('Done.');
})();
