/**
 * Prufrock Protocol — Screencast Recorder
 * Runs a headed Chrome session, records video, navigates all demo screens.
 * Output: prufrock-demo.webm in this directory.
 *
 * Usage: node record-demo.js
 * Requires: npm install playwright (already done)
 */

const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const BASE    = 'http://localhost:9191';
const OUT_DIR = __dirname;

(async () => {
  const browser = await chromium.launch({
    headless: false,
    args: ['--disable-infobars', '--window-position=0,0'],
  });

  const context = await browser.newContext({
    viewport: { width: 1440, height: 900 },
    recordVideo: {
      dir: OUT_DIR,
      size: { width: 1440, height: 900 },
    },
  });

  const page = await context.newPage();
  const go   = url  => page.goto(`${BASE}/${url}`, { waitUntil: 'networkidle' });
  const wait = ms   => page.waitForTimeout(ms);
  const nav  = text => page.locator('nav .nav-tab').filter({ hasText: new RegExp(`^${text}$`) }).click();

  // ── 01 Seed Panel ─────────────────────────────────────── T=0s (0:00)
  await go('01-seed-panel.html');
  await wait(24000);                    // narrator: intro

  // ── 05 Lineage ────────────────────────────────────────── T=24s (0:24)
  await nav('Lineage');
  await page.waitForLoadState('networkidle');
  await wait(7000);                     // trail + node cascade animation

  // Click Amara node at p=6 (Poem 07) ────────────────────── T=31s (0:31)
  await page.evaluate(() => {
    const circles = Array.from(document.querySelectorAll('circle'))
      .filter(c => c.style.cursor === 'pointer');
    if (circles[6]) circles[6].dispatchEvent(new MouseEvent('click', { bubbles: true }));
  });
  await wait(8000);                     // tooltip visible; narrator

  // ── 06 Map ────────────────────────────────────────────── T=39s (0:39)
  await nav('Map');
  await page.waitForLoadState('networkidle');
  await wait(30000);                    // full arc cascade + hold

  // ── 07 Poem ───────────────────────────────────────────── T=69s (1:09)
  await nav('Poem');
  await page.waitForLoadState('networkidle');
  await wait(3000);                     // let page settle

  // Click right-col line 8 (echo line) ──────────────────── T=72s (1:12)
  await page.evaluate(() => {
    const lines = document.querySelectorAll('#right-col .poem-line');
    if (lines[7]) lines[7].click();
  });
  await wait(21000);                    // tooltip visible; narrator

  // ── 10 Concerns ───────────────────────────────────────── T=93s (1:33)
  await nav('Concerns');
  await page.waitForLoadState('networkidle');
  await wait(25000);                    // edge cascade + hold

  // ── 11 Long View ──────────────────────────────────────── T=118s (1:58)
  await page.locator('.vbt').filter({ hasText: 'Long view' }).click();
  await page.waitForLoadState('networkidle');
  await wait(20000);                    // ribbon reveal + hold

  // ── 12b Deep Time ─────────────────────────────────────── T=138s (2:18)
  await page.locator('.vbt').filter({ hasText: 'Deep Time' }).click();
  await page.waitForLoadState('networkidle');
  await wait(39000);                    // river reveal + closing hold

  // ── End ───────────────────────────────────────────────── T=177s (2:57)
  const videoPath = await page.video().path();
  await context.close();
  await browser.close();

  // Rename to a fixed, predictable filename
  const dest = path.join(OUT_DIR, 'prufrock-demo.webm');
  if (fs.existsSync(dest)) fs.unlinkSync(dest);
  fs.renameSync(videoPath, dest);

  console.log('\n✓ Recording saved to:', dest);
  console.log('  Duration: ~2:57   Size:', Math.round(fs.statSync(dest).size / 1024 / 1024) + ' MB');
})().catch(err => { console.error(err); process.exit(1); });
