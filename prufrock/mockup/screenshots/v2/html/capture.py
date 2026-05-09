#!/usr/bin/env python3
from pathlib import Path
from playwright.sync_api import sync_playwright

HTML_DIR = Path(__file__).parent
OUT_DIR = HTML_DIR.parent  # v2/

FILES = [
    ('01-seed-panel.html',    '01-seed-panel.png'),
    ('05-lineage-path.html',  '05-lineage-path.png'),
    ('06-map-full.html',      '06-map-full.png'),
    ('07-poem-sidebyside.html', '07-poem-sidebyside.png'),
    ('08-participant.html',   '08-participant.png'),
    ('10-concerns-network.html', '10-concerns-network.png'),
    ('11-long-view.html',     '11-long-view.png'),
    ('12a-long-chain.html',   '12a-long-chain.png'),
    ('12b-deep-time.html',    '12b-deep-time.png'),
    ('12c-handoff.html',      '12c-handoff.png'),
]

with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context(
        viewport={'width': 1440, 'height': 900},
        device_scale_factor=2,
    )
    for html_file, png_file in FILES:
        page = context.new_page()
        url = 'file://' + str(HTML_DIR / html_file)
        page.goto(url, wait_until='networkidle')
        page.wait_for_timeout(600)
        page.screenshot(path=str(OUT_DIR / png_file), full_page=False)
        print(f'  ✓  {png_file}')
        page.close()
    browser.close()

print('Done.')
