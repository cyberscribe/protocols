/**
 * Prufrock Protocol — Screencast Recorder v2
 *
 * Starts its own static HTTP server, records all demo screens via Playwright,
 * then converts webm → mp4 (H.264) and → ProRes .mov for Final Cut Pro.
 *
 * Usage: node record-demo.js
 * Requires: npm install playwright (done), ffmpeg in PATH
 *
 * Sequence (~3:00):
 *   0:00  01-seed-panel      18s  sonnet stagger + seed pulse
 *   0:18  06-map-full        25s  arc cascade across 14 countries
 *   0:43  08-participant     13s  Amara Osei profile + trail
 *   0:56  07-poem-sidebyside 20s  2026↔2126 + echo click + tooltip
 *   1:16  10-concerns-network 22s edge cascade: themes → poems
 *   1:38  11-long-view       15s  417-year ribbon
 *   1:53  12b-deep-time      26s  1700-year river + pace layer legend
 *   2:19  16-pace-layer-stack 13s protocol pace layers diagram
 *   2:32  17-single-line-layers 14s one line, all temporal scales
 *   2:46  14-seed-gilgamesh  14s  4,100-year inheritance
 *   3:00  end
 */

const { chromium } = require('playwright');
const path         = require('path');
const fs           = require('fs');
const http         = require('http');
const { execSync } = require('child_process');

const PORT    = 9191;
const BASE    = `http://localhost:${PORT}`;
const OUT_DIR = __dirname;

// ── Inline static-file server ──────────────────────────────────────────────
const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.js':   'text/javascript',
  '.css':  'text/css',
  '.svg':  'image/svg+xml',
  '.png':  'image/png',
  '.jpg':  'image/jpeg',
  '.ico':  'image/x-icon',
};

function startServer() {
  const server = http.createServer((req, res) => {
    const url      = req.url.split('?')[0];
    const filePath = path.join(OUT_DIR, url === '/' ? '00-index.html' : url);
    try {
      const data = fs.readFileSync(filePath);
      const ext  = path.extname(filePath).toLowerCase();
      res.writeHead(200, { 'Content-Type': MIME[ext] || 'text/plain' });
      res.end(data);
    } catch {
      res.writeHead(404); res.end('Not found');
    }
  });
  return new Promise(resolve =>
    server.listen(PORT, () => { console.log(`  ▸ HTTP server on :${PORT}`); resolve(server); })
  );
}

// ── Main ───────────────────────────────────────────────────────────────────
(async () => {
  const server = await startServer();

  const browser = await chromium.launch({
    headless: false,
    args: ['--disable-infobars', '--window-position=0,0'],
  });

  const context = await browser.newContext({
    viewport:    { width: 1440, height: 900 },
    recordVideo: { dir: OUT_DIR, size: { width: 1440, height: 900 } },
  });

  const page = await context.newPage();
  const go   = url  => page.goto(`${BASE}/${url}`, { waitUntil: 'networkidle' });
  const wait = ms   => page.waitForTimeout(ms);
  const nav  = text =>
    page.locator('nav .nav-tab').filter({ hasText: new RegExp(`^${text}$`) }).click();

  console.log('\n  ▸ Recording…\n');

  // ── 01 Seed Panel ─────────────────────────────────────── T=0s   (0:00)
  await go('01-seed-panel.html');
  await wait(18000);    // sonnet lines stagger in; seed lines pulse amber

  // ── 06 Map ────────────────────────────────────────────── T=18s  (0:18)
  await nav('Map');
  await page.waitForLoadState('networkidle');
  await wait(25000);    // 14 arc groups animate in; full map holds

  // ── 08 Participant ────────────────────────────────────── T=43s  (0:43)
  await nav('Participant');
  await page.waitForLoadState('networkidle');
  await wait(4000);     // page settles
  // Try to surface the tooltip by clicking any interactive trail element
  await page.evaluate(() => {
    const sel = [
      '.trail-dot', '.trail-item', '.contrib-dot',
      'circle[style*="pointer"]', '[data-poem]',
    ].join(', ');
    const el = document.querySelector(sel);
    if (el) el.dispatchEvent(new MouseEvent('click', { bubbles: true }));
  });
  await wait(9000);     // Amara's profile + trail visible

  // ── 07 Poem (2026 ↔ 2126) ────────────────────────────── T=56s  (0:56)
  await nav('Poem');
  await page.waitForLoadState('networkidle');
  await wait(4000);     // transmission strip pulses; 2126 column cascades in
  // Click right-col line 8 — Lena Berg echo line → cross-century tooltip
  await page.evaluate(() => {
    const lines = document.querySelectorAll('#right-col .poem-line');
    if (lines[7]) lines[7].click();
  });
  await wait(16000);    // tooltip with echo annotation visible

  // ── 10 Concerns Network ───────────────────────────────── T=76s  (1:16)
  await nav('Concerns');
  await page.waitForLoadState('networkidle');
  await wait(22000);    // seed→theme arcs, then theme→poem cascade; hold

  // ── 11 Long View ──────────────────────────────────────── T=98s  (1:38)
  await page.locator('.vbt').filter({ hasText: 'Long view' }).click();
  await page.waitForLoadState('networkidle');
  await wait(15000);    // 417-year ribbon reveal; hold

  // ── 12b Deep Time River ───────────────────────────────── T=113s (1:53)
  await page.locator('.vbt').filter({ hasText: 'Deep Time' }).click();
  await page.waitForLoadState('networkidle');
  await wait(26000);    // 1700-year river, historical labels, pace layer legend,
                        // 2026 spotlight; hold

  // ── 16 Pace Layer Stack ───────────────────────────────── T=139s (2:19)
  await go('16-pace-layer-stack.html');
  await wait(13000);    // bands, protocol connector, "fast learns / slow remembers"

  // ── 17 Single Line · All Layers ──────────────────────── T=152s (2:32)
  await go('17-single-line-layers.html');
  await wait(14000);    // core sample + annotation cascade

  // ── 14 Gilgamesh ──────────────────────────────────────── T=166s (2:46)
  await go('14-seed-gilgamesh.html');
  await wait(14000);    // 2026 response cascades in against 4,100-year seed

  // ── Wrap ──────────────────────────────────────────────── T=180s (3:00)
  console.log('  ▸ Capture complete — closing browser…');
  const rawPath = await page.video().path();
  await context.close();
  await browser.close();
  server.close();

  // Save webm
  const webmPath = path.join(OUT_DIR, 'prufrock-demo.webm');
  if (fs.existsSync(webmPath)) fs.unlinkSync(webmPath);
  fs.renameSync(rawPath, webmPath);
  const webmMB = Math.round(fs.statSync(webmPath).size / 1024 / 1024);
  console.log(`  ▸ WebM:   ${webmPath}  (${webmMB} MB)\n`);

  // ── Convert → H.264 mp4 (web delivery + FCP import) ──────────────────
  const mp4Path = path.join(OUT_DIR, 'prufrock-demo.mp4');
  console.log('  ▸ ffmpeg → H.264 mp4 (CRF 15, yuv420p)…');
  execSync(
    `ffmpeg -y -i "${webmPath}" -c:v libx264 -crf 15 -preset slow -pix_fmt yuv420p -an "${mp4Path}"`,
    { stdio: 'inherit' }
  );
  const mp4MB = Math.round(fs.statSync(mp4Path).size / 1024 / 1024);
  console.log(`  ▸ MP4:    ${mp4Path}  (${mp4MB} MB)\n`);

  // ── Convert → ProRes 422 HQ .mov (FCP timeline editing) ──────────────
  const movPath = path.join(OUT_DIR, 'prufrock-demo-prores.mov');
  console.log('  ▸ ffmpeg → ProRes 422 HQ .mov (FCP editing)…');
  execSync(
    `ffmpeg -y -i "${webmPath}" -c:v prores_ks -profile:v 3 -pix_fmt yuv422p10le -vendor apl0 -an "${movPath}"`,
    { stdio: 'inherit' }
  );
  const movMB = Math.round(fs.statSync(movPath).size / 1024 / 1024);
  console.log(`  ▸ ProRes: ${movPath}  (${movMB} MB)\n`);

  console.log('  ✓ Done.\n');
})().catch(err => { console.error(err); process.exit(1); });
