# -*- coding: utf-8 -*-
"""Side B of the workshop takeaway card: DRIVE.

A port of slide 11 of the 4:5 trust-trap deck, not a new drawing. Five lettered circles down
the left as bullets, phase name beside each, descriptor beneath. Copy is the deck's, verbatim.

Same shape as exec-fn-portrait.py (side A) on purpose: a palette dict per theme, a build() that
returns the elements, a render(theme) wrapper, and the same 1040x1290 frame so the two sides
register when the card is flipped.

Circle colours: the deck's own five. They are used at full strength on dark; on light they are
darkened to hold white letters at 4.5:1, which the deck values do not (2.0-3.1:1 on white).
Hue and saturation are preserved, so the two renders read as the same five phases.
"""

W, H = 1040, 1290

DARK = dict(bg='#101828', panel='#131E33', band='#1B2A4A', rail='#16223A', stroke='#2F4068',
            ink='#FFFFFF', mut='#E9EEFA', dim='#9FB0C9', glyph='#FFFFFF')
LIGHT = dict(bg='#FFFFFF', panel='#FFFFFF', band='#F4F7FC', rail='#F7F9FD', stroke='#C3D0E4',
             ink='#0B1424', mut='#0B1424', dim='#5B6E8C', glyph='#FFFFFF')

# The deck's DRIVE palette (slide 11, Shapes 89/93/97/101/105).
PHASE = dict(D='#5C90F0', R='#3FBFAE', I='#E8A33D', V='#D9718F', E='#5ECB92')
# Light-card equivalents: same hue and saturation, lightness dropped until white letters clear
# 4.5:1. Needed because the card prints on white and the artwork is reduced from A4.
PHASE_LIGHT = dict(D='#2D70EC', R='#2B8276', I='#A46A13', V='#CD456C', E='#2B8656')

ROWS = [('D', 'Decide',   'What does “done” mean?'),
        ('R', 'Request',  'intent, context, assumptions, success criteria'),
        ('I', 'Iterate',  'stay in the loop and steer it'),
        ('V', 'Validate', 'confirm against done and success criteria'),
        ('E', 'Evolve',   'debrief, then update tooling, context, and practice')]

F = 'Poppins, Inter, "Segoe UI", Helvetica, Arial, sans-serif'


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;')


def txt(x, y, s, size=13, weight=400, fill='var(--ink)', anchor='start', ls=None):
    a = f'x="{x}" y="{y}" font-family=\'{F}\' font-size="{size}" font-weight="{weight}" fill="{fill}"'
    if anchor != 'start': a += f' text-anchor="{anchor}"'
    if ls: a += f' letter-spacing="{ls}"'
    return f'<text {a}>{esc(s)}</text>'


def build(p):
    o = []
    # panel, header band, and the rail the circles sit on -- Shapes 83, 84, 82 on the slide
    o.append('<rect x="36" y="64" width="968" height="1162" rx="18" fill="var(--panel)" '
             'stroke="var(--stroke)" stroke-width="1.6"/>')
    o.append('<path d="M36 82 A18 18 0 0 1 54 64 L986 64 A18 18 0 0 1 1004 82 L1004 204 L36 204 Z" '
             'fill="var(--band)"/>')
    o.append('<rect x="36" y="204" width="164" height="1022" fill="var(--rail)"/>')
    o.append('<path d="M36 204 L36 1208 A18 18 0 0 0 54 1226 L200 1226 L200 204 Z" '
             'fill="var(--rail)"/>')
    o.append('<line x1="36" y1="204" x2="1004" y2="204" stroke="var(--stroke)" stroke-width="1.2"/>')
    o.append(txt(76, 152, 'DRIVE', 54, 700, 'var(--ink)', ls='0.06em'))

    # TOP/PITCH chosen so the five rows sit with equal padding top and bottom inside the panel body
    TOP, PITCH, R = 264, 205, 39
    for i, (letter, name, desc) in enumerate(ROWS):
        y = TOP + i * PITCH
        o.append(f'<circle cx="118" cy="{y + R}" r="{R}" fill="{p[letter]}"/>')
        o.append(txt(118, y + R + 15, letter, 42, 700, 'var(--glyph)', 'middle', '0.02em'))
        o.append(txt(240, y + 36, name, 31, 700, 'var(--mut)'))
        o.append(txt(240, y + 74, desc, 19, 400, 'var(--dim)'))
        if i < len(ROWS) - 1:
            o.append(f'<line x1="240" y1="{y + 141}" x2="964" y2="{y + 141}" '
                     f'stroke="var(--stroke)" stroke-width="1"/>')
    return ''.join(o)


def render(theme='light'):
    pal = dict(DARK if theme == 'dark' else LIGHT)
    p = PHASE if theme == 'dark' else PHASE_LIGHT
    vars_ = ';'.join(f'--{n}:{v}' for n, v in pal.items())
    return (f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" style="{vars_}" '
            f'role="img" aria-label="DRIVE: Decide, Request, Iterate, Validate, Evolve">'
            f'<rect x="0" y="0" width="{W}" height="{H}" fill="var(--bg)"/>'
            + build(p) + '</svg>')


if __name__ == '__main__':
    for th in ('dark', 'light'):
        open(f'drive-portrait-{th}.svg', 'w', encoding='utf8').write(render(th))
    print('wrote drive-portrait-{dark,light}.svg')
