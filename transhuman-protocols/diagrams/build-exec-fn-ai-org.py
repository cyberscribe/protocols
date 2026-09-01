#!/usr/bin/env python3
"""
Executive function across human and AI — redraw of exec-fn-ai-org.graffle.

No branding, no title, no gloss: the representation only.

Overlays on the base structure:
  1. SYNC — six content types, each with its own colour. Same colour in two
     places means the same thing held twice, to be kept in sync. Colour rides
     on dots and accent bars only, never on type, so contrast never suffers.
  2. LOAD vs PROMOTE — two opposite paths between the stores and the loop.
     Loading (stores into the loop) is short, grey, automatic. Promotion (loop
     back out into a store) takes the long way round and is human-involved.
  3. CASCADE — small arrows in the gaps: project reference promotes up to
     general reference, up to working standards. Templates sits outside it,
     separated by a wider gap and no arrow.
  4. VARIANT 'promotion' — the two side effects each crossing arrow has on the
     HUMAN copy, which the base drawing omits because it draws every crossing as
     a transfer. They have opposite signs, so they take opposite line endings:
       top, dashed, bar end    loading SUPPRESSES the occasion to reconstruct
       bottom, solid, arrow    promotion REHEARSES what it writes
     Arrow produces, bar inhibits — the systems-biology convention, so no gloss
     text is needed to read it.

1360x762, sized for a 16:9 slide. THEME swaps palette in one place.
"""
import sys

THEME = sys.argv[2] if len(sys.argv) > 2 else 'naa'
VARIANT = sys.argv[3] if len(sys.argv) > 3 else 'base'   # 'base' | 'promotion'
if THEME == 'itv':
    INK, BODY, MUT, FAINT = '#1E2761', '#232733', '#6B7280', '#B4BBCB'
    LINE, TINT, WASH = '#D9DEEA', '#E9EEFB', '#F6F8FD'
    BFONT = 'Calibri, Carlito, Segoe UI, Helvetica, Arial, sans-serif'
elif THEME == 'dark':
    # For the navy video deck. Lightness inverts, hue identity is kept: the cascade is
    # still three blues broadest-to-narrowest, tracking still green and purple,
    # templates still amber. Nothing is recoloured for decoration.
    INK, BODY, MUT, FAINT = '#FFFFFF', '#C6D2E4', '#8FA0BB', '#46587A'
    LINE, TINT, WASH = '#2F4068', '#17233C', '#141F36'
    BFONT = 'Poppins, Inter, Segoe UI, Helvetica, Arial, sans-serif'
else:
    INK, BODY, MUT, FAINT = '#0F172A', '#475569', '#64748B', '#CBD5E1'
    LINE, TINT, WASH = '#E2E8F0', '#EFF6FF', '#F8FAFC'
    BFONT = 'Inter, Segoe UI, Carlito, Helvetica, Arial, sans-serif'

if THEME == 'dark':
    PAPER, CARD = '#101828', '#16223A'
    # the loop is what the eye should land on first. On white a dark solid did that;
    # on dark it takes a raised panel with an accent edge, rather than borrowing a
    # content colour, which would collide with 'projects'.
    LOOPFILL, LOOPEDGE, LOOPTXT = '#24365C', '#5ECB92', '#FFFFFF'
    SUBFILL, SUBEDGE, SUBTXT = '#101A2E', '#3C5480', '#8FA0BB'
    P2 = ('#5ECB92', '#0B1424', '#5ECB92')
    P1 = ('#1B2942', BODY, '#46587A')
    P0 = ('#16223A', MUT, LINE)
    C = {'standards': '#C7D9FF',   # the promotion cascade, broadest first
         'general':   '#8FB6FF',
         'project':   '#5C90F0',
         'templates': '#E8A33D',   # outside the cascade
         'projects':  '#5ECB92',   # tracking
         'status':    '#C08BFF'}
else:
    PAPER, CARD = '#FFFFFF', '#FFFFFF'
    LOOPFILL, LOOPEDGE, LOOPTXT = INK, INK, '#FFFFFF'
    SUBFILL, SUBEDGE, SUBTXT = '#1E293B', '#334155', '#94A3B8'
    P2 = (INK, '#FFFFFF', INK)
    P1 = ('#FFFFFF', BODY, BODY)
    P0 = ('#FFFFFF', MUT, LINE)
    C = {'standards': '#1E3A8A',   # the promotion cascade, broadest first
         'general':   '#2563EB',
         'project':   '#60A5FA',
         'templates': '#B45309',   # outside the cascade
         'projects':  '#15803D',   # tracking
         'status':    '#9333EA'}

W, H = 1360, 762
o = []


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def rect(x, y, w, h, fill, stroke=None, rx=10, sw=1.2, extra=''):
    st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ''
    o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"{st}{extra}/>')


def txt(x, y, s, size=12, fill=None, weight=400, anchor='start', ls=0, italic=False):
    a = f' text-anchor="{anchor}"' if anchor != 'start' else ''
    l = f' letter-spacing="{ls}"' if ls else ''
    i = ' font-style="italic"' if italic else ''
    o.append(f'<text x="{x}" y="{y}" font-family="{BFONT}" font-size="{size}" '
             f'font-weight="{weight}" fill="{fill or BODY}"{a}{l}{i}>{esc(s)}</text>')


def rot(x, y, lines, colour):
    g = [f'<g transform="translate({x},{y}) rotate(-90)">']
    for i, (s, size, weight, fill) in enumerate(lines):
        g.append(f'<text x="0" y="{i * 14}" font-family="{BFONT}" font-size="{size}" '
                 f'font-weight="{weight}" fill="{fill}" text-anchor="middle" '
                 f'letter-spacing="0.7">{esc(s)}</text>')
    o.append(''.join(g) + '</g>')


def dot(x, y, key, r=4):
    o.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{C[key]}"/>')


def chip(x, y, key, label, ink=None):
    dot(x + 11, y + 11, key, 4.2)
    txt(x + 22, y + 15, label, 11, ink or BODY)
    return len(label) * 6.1 + 38


def pill(right, y, label, tone):
    fill, ink, edge = {2: P2, 1: P1, 0: P0}[tone]
    w = len(label) * 6.0 + 20
    rect(right - w, y, w, 19, fill, edge, rx=9.5, sw=1)
    txt(right - w / 2, y + 13.2, label, 8.5, ink, 800, 'middle', ls=0.9)


# ---- geometry -------------------------------------------------------------
DIV = 640
CTX_X, CTX_W, CTX_H = 48, 214, 128
TRK_X, TRK_W, TRK_H = 280, 330, 88
ROWS = [130, 310, 490]
LOOP_X, LOOP_W, LOOP_H = 666, 214, 96
WM_Y, WM_H = 356, 84
LOAD = 918                                   # stores -> loop, the short way
ST_X, ST_W, ST_H = 940, 290, 76
ST_Y = [130, 228, 326, 448]                  # three in cascade, then one outside
PROM = 1256                                  # loop -> stores, the long way
MIDY = ROWS[2] + TRK_H / 2

o.append(f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" '
         f'aria-labelledby="t d">')
o.append('<title id="t">Executive function across human and AI</title>')
o.append('<desc id="d">Human side: shared, individual and working-session tracking, with the '
         'context held at shared and individual level. AI side: a session replay loop — one of '
         'several that may be running — with sub-agents, tools and API calls beneath it, fed '
         'automatically by four context stores, and promoting back out into them with a human in '
         'the loop. Six content types are colour-keyed across both sides to show what must be '
         'kept in sync. Small arrows mark the promotion cascade from project reference up to '
         'general reference up to working standards; templates sits outside it.</desc>')
o.append('<defs>')
for name, c, sz in (('a', INK, 9), ('b', MUT, 8), ('c', BODY, 8)):
    o.append(f'<marker id="m{name}" markerUnits="userSpaceOnUse" markerWidth="{sz}" '
             f'markerHeight="{sz}" refX="{sz * 0.85}" refY="{sz / 2}" orient="auto">'
             f'<path d="M0,0 L{sz},{sz / 2} L0,{sz} Z" fill="{c}"/></marker>')
    o.append(f'<marker id="m{name}R" markerUnits="userSpaceOnUse" markerWidth="{sz}" '
             f'markerHeight="{sz}" refX="{sz * 0.15}" refY="{sz / 2}" orient="auto">'
             f'<path d="M{sz},0 L0,{sz / 2} L{sz},{sz} Z" fill="{c}"/></marker>')
# a rect, not a zero-width path: a degenerate bbox breaks marker scaling in
# several renderers, PowerPoint among them
o.append(f'<marker id="mbar" markerUnits="userSpaceOnUse" markerWidth="12" '
         f'markerHeight="22" refX="4" refY="11" orient="auto">'
         f'<rect x="2" y="0" width="3.2" height="22" fill="{MUT}"/></marker>')
o.append('</defs>')
rect(0, 0, W, H, PAPER, rx=0)

o.append(f'<line x1="{DIV}" y1="60" x2="{DIV}" y2="694" stroke="{FAINT}" stroke-width="2.5" '
         f'stroke-dasharray="9 9"/>')
txt(DIV - 40, 722, 'HUMAN', 20, FAINT, 800, 'end', ls=5)
txt(DIV + 40, 722, 'AI', 20, FAINT, 800, 'start', ls=5)

# ---- human: context -------------------------------------------------------
CTX_ITEMS = [('standards', 'working standards'), ('general', 'general reference'),
             ('project', 'project reference'), ('templates', 'templates')]
for title, y in (('Shared context', ROWS[0] - (CTX_H - TRK_H) / 2),
                 ('Individual context', ROWS[1] - (CTX_H - TRK_H) / 2)):
    rect(CTX_X, y, CTX_W, CTX_H, TINT, LINE)
    txt(CTX_X + 18, y + 28, title, 13.5, INK, 700)
    for i, (key, label) in enumerate(CTX_ITEMS):
        yy = y + 52 + i * 19
        dot(CTX_X + 22, yy - 4, key)
        txt(CTX_X + 34, yy, label, 11, BODY)

# ---- human: tracking ------------------------------------------------------
for name, y in zip(['Shared tracking', 'Individual tracking', 'Working session tracking'], ROWS):
    rect(TRK_X, y, TRK_W, TRK_H, CARD, LINE)
    txt(TRK_X + 20, y + 32, name, 15.5, INK, 700)
    x = TRK_X + 16
    x += chip(x, y + 46, 'projects', 'projects')
    chip(x, y + 46, 'status', 'status')

for a, b in ((ROWS[0] + TRK_H, ROWS[1]), (ROWS[1] + TRK_H, ROWS[2])):
    x = TRK_X + TRK_W / 2
    o.append(f'<line x1="{x}" y1="{a + 9}" x2="{x}" y2="{b - 9}" stroke="{INK}" '
             f'stroke-width="2.2" marker-start="url(#maR)" marker-end="url(#ma)"/>')

o.append(f'<line x1="{TRK_X + TRK_W + 9}" y1="{MIDY}" x2="{LOOP_X - 9}" y2="{MIDY}" '
         f'stroke="{INK}" stroke-width="2.6" marker-start="url(#maR)" marker-end="url(#ma)"/>')

# ---- AI: working memory ---------------------------------------------------
rect(LOOP_X, WM_Y, LOOP_W, WM_H, CARD, LINE)
txt(LOOP_X + 20, WM_Y + 32, 'Working memory', 15, INK, 700)
pill(LOOP_X + LOOP_W - 20, WM_Y + WM_H - 32, 'AUTOMATIC', 1)
o.append(f'<line x1="{LOOP_X + LOOP_W / 2}" y1="{WM_Y + WM_H + 9}" x2="{LOOP_X + LOOP_W / 2}" y2="{ROWS[2] - 9}" '
         f'stroke="{INK}" stroke-width="2.2" marker-start="url(#maR)" marker-end="url(#ma)"/>')

# ---- AI: the loop, one of several, with what runs beneath it --------------
for off, op in ((18, 0.40), (9, 0.62)):
    rect(LOOP_X + off, ROWS[2] + off, LOOP_W, LOOP_H, CARD, LOOPEDGE, rx=10, sw=1.4,
         extra=f' opacity="{op}"')
rect(LOOP_X, ROWS[2], LOOP_W, LOOP_H, LOOPFILL,
     LOOPEDGE if THEME == 'dark' else None, rx=10, sw=1.6)
txt(LOOP_X + LOOP_W / 2, ROWS[2] + 34, 'Session replay loop', 15.5, LOOPTXT, 700, 'middle')
rect(LOOP_X + 13, ROWS[2] + 50, LOOP_W - 26, 32, SUBFILL, SUBEDGE, rx=7, sw=1,
     extra=' stroke-dasharray="4 3"')
txt(LOOP_X + LOOP_W / 2, ROWS[2] + 70, 'sub-agents · tools · API calls', 10, SUBTXT, 600,
    'middle')


# ---- AI: the context stores ----------------------------------------------
STORES = [('standards', 'Working standards', None, 'ALWAYS', 2),
          ('general', 'General reference', None, 'AS-NEEDED', 0),
          ('project', 'Project reference', None, 'PER PROJECT', 1),
          ('templates', 'Templates', '(including agent role definitions)', 'AS-NEEDED', 0)]
for (key, name, sub, disc, tone), y in zip(STORES, ST_Y):
    rect(ST_X, y, ST_W, ST_H, WASH, LINE)
    o.append(f'<rect x="{ST_X}" y="{y + 10}" width="4.5" height="{ST_H - 20}" rx="2.2" '
             f'fill="{C[key]}"/>')
    txt(ST_X + 22, y + (30 if sub else ST_H / 2 + 5), name, 15, INK, 700)
    if sub:
        txt(ST_X + 22, y + 48, sub, 10, MUT)
    pill(ST_X + ST_W - 20, y + ST_H / 2 - 9.5, disc, tone)

# loading: every store into the loop, the short way
for y in ST_Y:
    cy = y + ST_H / 2
    o.append(f'<line x1="{ST_X}" y1="{cy}" x2="{LOAD}" y2="{cy}" stroke="{MUT}" stroke-width="1.6"/>')
    o.append(f'<circle cx="{LOAD}" cy="{cy}" r="3" fill="{MUT}"/>')
o.append(f'<path d="M {LOAD} {ST_Y[0] + ST_H / 2} L {LOAD} {ROWS[2] + 22} '
         f'L {LOOP_X + LOOP_W + 10} {ROWS[2] + 22}" fill="none" stroke="{MUT}" '
         f'stroke-width="2.2" marker-end="url(#mb)"/>')
rot(LOAD - 26, (ST_Y[0] + ST_Y[3]) / 2 + 40,
    [('loading', 10.5, 700, MUT), ('automatic', 9.5, 400, MUT)], MUT)

# promotion: out of the loop and back into a store, the long way round
o.append(f'<path d="M {LOOP_X + LOOP_W + 10} {ROWS[2] + 62} L {PROM} {ROWS[2] + 62} '
         f'L {PROM} {ST_Y[0] + ST_H / 2}" fill="none" stroke="{BODY}" stroke-width="2.2"/>')
for y in ST_Y:
    cy = y + ST_H / 2
    o.append(f'<line x1="{PROM}" y1="{cy}" x2="{ST_X + ST_W + 8}" y2="{cy}" stroke="{BODY}" '
             f'stroke-width="1.8" marker-end="url(#mc)"/>')
rot(PROM + 24, (ST_Y[0] + ST_Y[3]) / 2 + 44,
    [('promotion', 10.5, 700, BODY), ('human-involved', 9.5, 400, MUT)], BODY)

# the cascade: project reference promotes up to general, up to standards
for a, b in ((ST_Y[1], ST_Y[0] + ST_H), (ST_Y[2], ST_Y[1] + ST_H)):
    x = ST_X + 46
    o.append(f'<line x1="{x}" y1="{a - 3}" x2="{x}" y2="{b + 3}" stroke="{BODY}" '
             f'stroke-width="2" marker-end="url(#mc)"/>')

if VARIANT == 'promotion':
    # Both effects act on the SAME quantity -- the person's own copy -- with opposite
    # signs, so both land on the same box from different edges. Individual context is
    # the nearest thing the drawing has to a head; that it is only "nearest" is the
    # finding, not a rounding.
    IND_Y = ROWS[1] - (CTX_H - TRK_H) / 2
    IND_MID, IND_BOT = IND_Y + CTX_H / 2, IND_Y + CTX_H
    TRKMID = TRK_X + TRK_W / 2

    # loading suppresses the occasion to reconstruct: bar end, left edge
    o.append(f'<path d="M {LOAD} {ST_Y[0] + ST_H / 2} L {LOAD} 84 L 26 84 '
             f'L 26 {IND_MID} L {CTX_X - 11} {IND_MID}" fill="none" stroke="{MUT}" '
             f'stroke-width="1.8" stroke-dasharray="7 5" marker-end="url(#mbar)"/>')

    # promotion rehearses what it writes: arrow end, bottom edge
    o.append(f'<path d="M {PROM} {ROWS[2] + 62} L {PROM} 660 L {CTX_X + CTX_W / 2} 660 '
             f'L {CTX_X + CTX_W / 2} {IND_BOT + 11}" fill="none" stroke="{BODY}" '
             f'stroke-width="2.2" marker-end="url(#mc)"/>')

o.append('</svg>')
open(sys.argv[1] if len(sys.argv) > 1 else 'out.svg', 'w').write('\n'.join(o))
