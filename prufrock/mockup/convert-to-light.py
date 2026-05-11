#!/usr/bin/env python3
"""Convert Prufrock Protocol v2 mockup from dark mode to Long Now light palette.

Palette rationale:
- Background: warm parchment (#f5f0e8) and slightly deeper panels (#ece7db)
- Text: dark warm charcoal (#1a1410) descending through warm browns to muted tans
- Borders: warm tan (#c8b898)
- Accent: #a8623c copper — unchanged, it is already the Long Now copper
- Data-visualisation theme colours (mortality, love, memory …) are unchanged
- Map ocean SVG gradient is restored to dark after global conversion
"""

import os
import glob

HTML_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        'screenshots', 'v2', 'html')

# Ordered replacements — applied to every .html in v2/html (no node_modules).
# Hex colours: 6-char, never confused with adjacent digits in this codebase.
# rgba() strings: exact-match only, so the THEMES data colours are untouched.
GLOBAL = [
    # ── Backgrounds ────────────────────────────────────────────
    ('#1c2530', '#f5f0e8'),   # main body bg → warm parchment
    ('#1c2028', '#ece7db'),   # panel / card bg → deeper parchment
    ('#1e2530', '#ece7db'),   # nav / controls bg
    ('#1a2130', '#e8e3d5'),   # notification banner bg (interruption)
    ('#1e2228', '#eae5d9'),
    ('#1c1f26', '#eee9dd'),
    ('#1a2028', '#eae5d9'),
    ('#1a1f28', '#eee9dd'),
    ('#1a1e26', '#eee9dd'),
    ('#1e2a34', '#e8e3d5'),
    ('#1e2830', '#eae5d9'),
    ('#1e2634', '#eae5d9'),
    ('#1e2430', '#ece7db'),
    ('#1a2430', '#ece7db'),
    ('#243038', '#e0dbc8'),
    ('#222c3c', '#d8d2c4'),
    ('#222c38', '#d8d2c4'),
    ('#222028', '#e8e3d7'),
    ('#181e28', '#eee9dd'),
    ('#141c28', '#f0ebe0'),   # prompt-area inside phone (now parchment interior)
    ('#141c24', '#ece7db'),   # rchain-item bg
    ('#0f161e', '#f4efe4'),   # compose-area inside phone
    ('#14181f', '#f0ebe0'),   # map nav / controls bg (map-specific dark variant)
    ('#1e2832', '#c8b898'),   # map nav border
    ('#0e1219', '#f5f0e8'),   # map body bg / slider thumb border

    # ── Primary text ───────────────────────────────────────────
    ('#e8dec4', '#1a1410'),
    ('#dcd4be', '#2a2018'),
    ('#c8c0b0', '#3a2c20'),

    # ── Secondary text ─────────────────────────────────────────
    ('#a8a090', '#4a3828'),
    ('#9a8e80', '#4a3828'),
    ('#8a8278', '#5a4838'),
    ('#8a8878', '#4a3828'),   # pa-text inside phone
    ('#7a7870', '#6a5848'),
    ('#7a7066', '#6a5848'),
    ('#6a6860', '#7a6858'),
    ('#5a5450', '#7a6a58'),
    ('#5a6070', '#7a6858'),   # pa-name inside phone
    ('#5a6878', '#7a6858'),
    ('#4a5868', '#6a5848'),
    ('#4a5060', '#8a7868'),
    ('#4a5260', '#8a7868'),
    ('#4a5468', '#8a7868'),
    ('#3c3834', '#9a8878'),
    ('#3c4050', '#9a8a78'),
    ('#3a4050', '#9a8a78'),
    ('#3a4250', '#9a8a78'),
    ('#3a3a40', '#b0a090'),
    ('#3a6878', '#5a7870'),   # keep blue tint for interactive elements

    # ── Dim / near-invisible text ──────────────────────────────
    ('#3a3632', '#b0a090'),
    ('#322e2a', '#a09080'),
    ('#322e28', '#a09080'),
    ('#34302c', '#a09080'),
    ('#2e3848', '#a09080'),
    ('#2e2a26', '#b0a090'),
    ('#2c2826', '#a09080'),
    ('#2a4050', '#8a7868'),
    ('#2a4858', '#5a6878'),   # annotation subtitle text (keep blue tone)
    ('#2a2818', '#b4a490'),
    ('#262220', '#b0a090'),
    ('#221e1a', '#b8a898'),   # SVG time-break labels in long-view
    ('#1e1a14', '#b8a898'),
    ('#1e4050', '#3a7068'),   # "new in 2126" Transhumanism label (keep teal)
    ('#1a1612', '#b4a898'),
    ('#2e4540', '#3a7060'),   # "new in 2126" Climate label (keep green)

    # ── Borders ────────────────────────────────────────────────
    ('#232a32', '#c8b898'),
    ('#2a3340', '#c0b090'),
    ('#2e3640', '#b8a888'),
    ('#2a3848', '#c0b090'),
    ('#2a3240', '#c0b090'),
    ('#2c3240', '#c0b090'),
    ('#1e2838', '#c8b898'),   # phone btn-cancel border

    # ── MOCKUP banner ──────────────────────────────────────────
    ('#523018', '#c07838'),

    # ── Muted copper (dark accent → medium copper on light bg) ─
    ('#6a3a18', '#8a5028'),

    # ── SVG annotation boxes (dark near-opaque → parchment) ────
    ('rgba(28,37,48,.95)',  'rgba(244,239,232,.96)'),
    ('rgba(28,37,48,0.95)', 'rgba(244,239,232,.96)'),
    ('rgba(28,24,18,.9)',   'rgba(244,239,232,.95)'),
    ('rgba(28,24,18,0.9)',  'rgba(244,239,232,.95)'),

    # ── Active button highlights: white overlay → black ─────────
    ('rgba(255,255,255,.05)',  'rgba(0,0,0,.06)'),
    ('rgba(255,255,255,.06)',  'rgba(0,0,0,.07)'),
    ('rgba(255,255,255,.04)',  'rgba(0,0,0,.05)'),
    ('rgba(255,255,255,.08)',  'rgba(0,0,0,.10)'),
    ('rgba(255,255,255,.07)',  'rgba(0,0,0,.08)'),
    ('rgba(255,255,255,.03)',  'rgba(0,0,0,.04)'),
    ('rgba(255,255,255,.012)', 'rgba(0,0,0,.04)'),
    ('rgba(255,255,255,.018)', 'rgba(0,0,0,.06)'),

    # ── SVG chart lines / labels: white on dark → dark on light ─
    ('rgba(255,255,255,.12)',  'rgba(0,0,0,.15)'),
    ('rgba(255,255,255,.18)',  'rgba(0,0,0,.35)'),
    ('rgba(255,255,255,.25)',  'rgba(0,0,0,.40)'),
    ('rgba(255,255,255,.40)',  'rgba(0,0,0,.60)'),
    ('rgba(255,255,255,.28)',  'rgba(0,0,0,.50)'),
    ('rgba(255,255,255,.1)',   'rgba(0,0,0,.15)'),
    ('rgba(255,255,255,.5)',   'rgba(0,0,0,.60)'),
    ('rgba(255,255,255,.45)',  'rgba(0,0,0,.55)'),
    ('rgba(255,255,255,.60)',  'rgba(0,0,0,.70)'),
    ('rgba(255,255,255,.80)',  'rgba(0,0,0,.80)'),
]

# Map file: after GLOBAL the second ocean gradient stop (#0e1219 → #f5f0e8).
# Restore it to a deep ocean dark so the immersive map SVG stays readable.
MAP_OCEAN_FIX = (
    '<stop offset="100%" stop-color="#f5f0e8"/>',
    '<stop offset="100%" stop-color="#0c1018"/>',
)


def convert_file(path: str) -> None:
    with open(path, encoding='utf-8') as f:
        content = f.read()
    for old, new in GLOBAL:
        content = content.replace(old, new)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)


def fix_map(path: str) -> None:
    with open(path, encoding='utf-8') as f:
        content = f.read()
    content = content.replace(MAP_OCEAN_FIX[0], MAP_OCEAN_FIX[1])
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)


def main() -> None:
    pattern = os.path.join(HTML_DIR, '*.html')
    files = sorted(f for f in glob.glob(pattern) if 'node_modules' not in f)

    for path in files:
        convert_file(path)
        print(f'  converted  {os.path.basename(path)}')

    map_path = os.path.join(HTML_DIR, '06-map-full.html')
    fix_map(map_path)
    print(f'  ocean restored  {os.path.basename(map_path)}')

    print(f'\n{len(files)} files converted to Long Now light palette.')


if __name__ == '__main__':
    main()
