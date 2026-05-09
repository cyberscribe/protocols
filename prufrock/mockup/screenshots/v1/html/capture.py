import os
from pathlib import Path
from playwright.sync_api import sync_playwright

HTML_DIR = Path(__file__).parent
OUT_DIR = HTML_DIR.parent

FILES = [
    ('01-seed-panel.html', '01-seed-panel.png'),
    ('02-timeline-mid.html', '02-timeline-mid.png'),
    ('03-timeline-complete.html', '03-timeline-complete.png'),
    ('04-lineage-full.html', '04-lineage-full.png'),
    ('05-lineage-path.html', '05-lineage-path.png'),
    ('06-map-full.html', '06-map-full.png'),
    ('07-poem-sidebyside.html', '07-poem-sidebyside.png'),
    ('08-participant.html', '08-participant.png'),
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
        page.wait_for_timeout(400)
        out_path = str(OUT_DIR / png_file)
        page.screenshot(path=out_path, full_page=False)
        page.close()
        print(f'✓ {png_file}')
    browser.close()

print('Done.')
