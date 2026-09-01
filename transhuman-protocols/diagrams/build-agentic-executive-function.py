#!/usr/bin/env python3
"""
Agentic executive function — one person, several concurrent agents.

Emits a 1360x762 SVG sized to drop straight onto a 16:9 slide. Matches the NAA
diagram grammar already in 00-gtd-ai/resources/diagrams (Inter/slate palette).

Two overlays are deliberately separable:
  - the MODEL (tiers, the human/AI line, the shared context stack) — tool-neutral
  - the EXAMPLE (kanban, GTD, memory.md, proj1/*.md ...) — grey mono, one instantiation

THEME swaps the whole palette in one place: 'naa' matches the diagrams folder,
'itv' matches the navy/Cambria deck grammar in workshop-2026-08-27/deck-build.
"""
import sys

THEME = sys.argv[2] if len(sys.argv) > 2 else 'naa'

if THEME == 'itv':
    INK, BODY, MUT, FAINT = '#1E2761', '#232733', '#6B7280', '#9AA2B4'
    LINE, PANEL, TINT = '#D9DEEA', '#F6F8FD', '#E9EEFB'
    LOAD, PROMOTE, GOVERN = '#1E2761', '#2E7D43', '#8A6D1A'
    FONT = 'Cambria, Caladea, Georgia, serif'
    BFONT = 'Calibri, Carlito, Segoe UI, Helvetica, Arial, sans-serif'
    MARK = '#1E2761'
else:
    INK, BODY, MUT, FAINT = '#0F172A', '#475569', '#64748B', '#94A3B8'
    LINE, PANEL, TINT = '#E2E8F0', '#F8FAFC', '#EFF6FF'
    LOAD, PROMOTE, GOVERN = '#1D4ED8', '#15803D', '#B45309'
    FONT = BFONT = 'Inter, Segoe UI, Carlito, Helvetica, Arial, sans-serif'
    MARK = '#DC2626'

MONO = 'ui-monospace, SFMono-Regular, Menlo, DejaVu Sans Mono, monospace'
W, H = 1360, 762
o = []


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def rect(x, y, w, h, fill, stroke=None, rx=8, sw=1, extra=''):
    s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ''
    o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"{s}{extra}/>')


def txt(x, y, s, size=12, fill=None, weight=400, anchor='start', font=None,
        ls=0, italic=False, opacity=None):
    a = f' text-anchor="{anchor}"' if anchor != 'start' else ''
    l = f' letter-spacing="{ls}"' if ls else ''
    i = ' font-style="italic"' if italic else ''
    op = f' opacity="{opacity}"' if opacity else ''
    o.append(f'<text x="{x}" y="{y}" font-family="{font or BFONT}" font-size="{size}" '
             f'font-weight="{weight}" fill="{fill or BODY}"{a}{l}{i}{op}>{esc(s)}</text>')


def mono(x, y, s, size=10, anchor='start'):
    """The working-example overlay. Always grey, always mono, always bracketed."""
    txt(x, y, s, size, FAINT, 400, anchor, MONO)


def arrow(x1, y1, x2, y2, colour, label='', sw=2.4, dash=None, double=False, at=0.5):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    st = f' marker-start="url(#head-{colour[1:]})"' if double else ''
    o.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{colour}" '
             f'stroke-width="{sw}"{d} marker-end="url(#head-{colour[1:]})"{st}/>')
    if label:
        mx, my = x1 + (x2 - x1) * at, y1 + (y2 - y1) * at
        lw = len(label) * 7.4
        o.append(f'<g transform="translate({mx},{my}) rotate(-90)">'
                 f'<rect x="{-lw / 2}" y="-17" width="{lw}" height="14" fill="#FFFFFF"/>'
                 f'<text x="0" y="-7" font-family="{BFONT}" font-size="9.5" font-weight="700" '
                 f'fill="{colour}" text-anchor="middle" letter-spacing="1.1">{esc(label)}</text></g>')


def gutter(x, y, s, anchor='end', fill=None):
    txt(x, y, s, 10, fill or MUT, 700, anchor, ls=1.3)


# ---- geometry -------------------------------------------------------------
L, R = 40, 1320                     # page margins
BX, BR = 140, 1220                  # diagram body
TRK_X, TRK_W = 140, 450             # tracking column
CTX_X, CTX_W = 630, 590             # context column
ROW1_Y, ROW_H = 110, 64             # team
ROW2_Y = 196                        # individual
SESS_Y, SESS_H = 282, 62            # session fan-out
LINE_Y = 362                        # the human / AI boundary
AG_Y, AG_H = 376, 60                # agent black boxes
PAN_Y, PAN_B = 476, 730             # shared agent context panel
NSESS = 4
CW = (TRK_W - 3 * 12) / NSESS       # session / agent card width
cx = [TRK_X + i * (CW + 12) for i in range(NSESS)]
mid = [x + CW / 2 for x in cx]

o.append(f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" '
         f'aria-labelledby="t d">')
o.append('<title id="t">Executive function with concurrent agents</title>')
o.append('<desc id="d">Two stacks — human tracking and shared context — scoped at team, individual '
         'and session level, cut by a human/AI boundary. Tracking stops at the boundary because the '
         'agent is a black box; context crosses it into a shared stack of project memory, general '
         'memory, templates and working standards that every concurrent session loads.</desc>')
o.append('<defs>')
for c in (LOAD, PROMOTE, GOVERN, FAINT, INK):
    o.append(f'<marker id="head-{c[1:]}" markerWidth="9" markerHeight="9" refX="6.5" refY="3" '
             f'orient="auto"><path d="M0,0 L6.5,3 L0,6 Z" fill="{c}"/></marker>')
o.append('</defs>')
rect(0, 0, W, H, '#FFFFFF', rx=0)

# ---- header ---------------------------------------------------------------
o.append(f'<text x="{L}" y="40" font-family="{BFONT}" font-size="20" font-weight="800" '
         f'fill="{MARK}" letter-spacing="1">NE<tspan fill="{INK}">&#187;</tspan>T ACTION '
         f'<tspan font-size="12" fill="{MUT}">ASSOCIATES</tspan></text>')
txt(680, 37, 'Executive function with concurrent agents', 26, INK, 800, 'middle', FONT)
txt(680, 62, 'One person, several live sessions. Tracking stays above the line. Context is what '
             'crosses — and promotion is what makes it stick.', 14, BODY, 400, 'middle')

# ---- column headers -------------------------------------------------------
for x, w, head, sub in (
        (TRK_X, TRK_W, 'TRACKING', 'deliverables · status'),
        (CTX_X, CTX_W, 'CONTEXT', 'general · project · standards · templates')):
    o.append(f'<rect x="{x}" y="96" width="20" height="2.5" fill="{INK}"/>')
    txt(x + 30, 102, head, 11, INK, 800, ls=1.6)
    txt(x + 30 + len(head) * 8.4 + 14, 102, sub, 11, MUT)
o.append(f'<line x1="{BX}" y1="108" x2="{BR}" y2="108" stroke="{LINE}" stroke-width="1"/>')

# ---- scope gutter ---------------------------------------------------------
gutter(128, ROW1_Y + 42, 'TEAM')
gutter(128, ROW2_Y + 42, 'INDIVIDUAL')
gutter(128, SESS_Y + 30, 'SESSION')
txt(128, SESS_Y + 44, '× n concurrent', 9, FAINT, 400, 'end')
gutter(128, AG_Y + 40, 'AGENTS', fill=INK)

# ---- tracking column ------------------------------------------------------
def card(x, y, w, h, title, sub, example, fill='#FFFFFF', stroke=None, ink=None, sub2=None):
    rect(x, y, w, h, fill, stroke or LINE, rx=9)
    txt(x + 16, y + 26, title, 14, ink or INK, 700)
    txt(x + 16, y + 45, sub, 11, MUT if not ink else '#CBD5E1')
    if sub2:
        txt(x + 16, y + 61, sub2, 11, MUT if not ink else '#CBD5E1')
    if example:
        mono(x + w - 16, y + 26, example, 10.5, 'end')


card(TRK_X, ROW1_Y, TRK_W, ROW_H, 'Shared tracking',
     'what the team owes each other, and where it has got to', '[ kanban ]')
card(TRK_X, ROW2_Y, TRK_W, ROW_H, 'Individual tracking',
     'everything I have committed to — agent work included', '[ GTD ]')

# status rolls up
for gy in ((ROW2_Y, ROW1_Y + ROW_H), (SESS_Y, ROW2_Y + ROW_H)):
    arrow(TRK_X + 40, gy[0] - 4, TRK_X + 40, gy[1] + 4, FAINT, sw=3)
txt(TRK_X + 54, ROW2_Y - 7, 'status rolls up', 9.5, FAINT, 700, italic=True)

# session fan-out
for i in range(NSESS):
    ghost = (i == NSESS - 1)
    rect(cx[i], SESS_Y, CW, SESS_H, '#FFFFFF', LINE, rx=9,
         extra=' stroke-dasharray="4 3"' if ghost else '')
    if ghost:
        txt(cx[i] + CW / 2, SESS_Y + 32, '+ n', 15, FAINT, 700, 'middle')
        txt(cx[i] + CW / 2, SESS_Y + 49, 'more tabs', 9, FAINT, 400, 'middle')
    else:
        txt(cx[i] + CW / 2, SESS_Y + 26, f'Session {i + 1}', 12.5, INK, 700, 'middle')
        txt(cx[i] + CW / 2, SESS_Y + 42, 'deliverable', 9.5, MUT, 400, 'middle')
        mono(cx[i] + CW / 2, SESS_Y + 56, '[ document ]', 9, 'middle')
txt(TRK_X + TRK_W + 12, SESS_Y + 26, 'terminal tabs,', 10, MUT)
txt(TRK_X + TRK_W + 12, SESS_Y + 40, 'chat sessions —', 10, MUT)
txt(TRK_X + TRK_W + 12, SESS_Y + 54, 'tracked by hand', 10, MUT, 700)

# ---- context column -------------------------------------------------------
def chips(right, y, items, colour):
    """Right-aligned pill row — the four content classes a context layer holds."""
    ws = [len(it) * 6.4 + 18 for it in items]
    cxp = right - (sum(ws) + 8 * (len(items) - 1))
    for it, w in zip(items, ws):
        rect(cxp, y, w, 20, '#FFFFFF', colour, rx=10, sw=1)
        txt(cxp + w / 2, y + 14, it, 10, BODY, 600, 'middle')
        cxp += w + 8


rect(CTX_X, ROW1_Y, CTX_W, ROW_H, TINT, LINE, rx=9)
txt(CTX_X + 16, ROW1_Y + 26, 'Shared context', 14, INK, 700)
txt(CTX_X + 16, ROW1_Y + 45, 'what the team agrees every agent should know', 11, MUT)
chips(CTX_X + CTX_W - 16, ROW1_Y + 22, ['general', 'project', 'standards', 'templates'], LINE)

rect(CTX_X, ROW2_Y, CTX_W, ROW_H, TINT, LINE, rx=9)
txt(CTX_X + 16, ROW2_Y + 26, 'Individual context', 14, INK, 700)
txt(CTX_X + 16, ROW2_Y + 45, 'my own working set — what I keep finding worth reusing', 11, MUT)
chips(CTX_X + CTX_W - 16, ROW2_Y + 22, ['general', 'project', 'templates'], LINE)

arrow(CTX_X + 40, ROW2_Y - 4, CTX_X + 40, ROW1_Y + ROW_H + 4, PROMOTE, sw=3)
txt(CTX_X + 54, ROW2_Y - 7, 'reusable — promoted to the team', 9.5, PROMOTE, 700)

# ---- the boundary ---------------------------------------------------------
o.append(f'<line x1="{L}" y1="{LINE_Y}" x2="{R}" y2="{LINE_Y}" stroke="{INK}" '
         f'stroke-width="1.6" stroke-dasharray="7 5"/>')
txt(L, LINE_Y - 8, 'HUMAN', 11, INK, 800, ls=2)
txt(L, LINE_Y + 18, 'AI', 11, INK, 800, ls=2)
txt(1040, LINE_Y - 8, 'tracking stops here · context carries on', 11, MUT, 400, 'end', italic=True)

# ---- agent black boxes ----------------------------------------------------
for i in range(NSESS):
    ghost = (i == NSESS - 1)
    rect(cx[i], AG_Y, CW, AG_H, INK, rx=9, extra=' opacity="0.32"' if ghost else '')
    if ghost:
        txt(cx[i] + CW / 2, AG_Y + 36, '+ n', 15, '#FFFFFF', 700, 'middle')
    else:
        txt(cx[i] + CW / 2, AG_Y + 25, 'agent', 12.5, '#FFFFFF', 700, 'middle', ls=1)
        txt(cx[i] + CW / 2, AG_Y + 41, 'replay + working memory', 8.5, '#94A3B8', 400, 'middle')
        o.append(f'<text x="{cx[i] + CW / 2}" y="{AG_Y + 56}" font-family="{MONO}" font-size="9" '
                 f'fill="#64748B" text-anchor="middle">[ memory.md ]</text>')
    # interaction across the line
    arrow(mid[i], SESS_Y + SESS_H + 3, mid[i], AG_Y - 3, INK, sw=1.6, double=True)

txt(TRK_X + TRK_W + 12, AG_Y + 24, 'black box —', 10, INK, 700)
txt(TRK_X + TRK_W + 12, AG_Y + 38, 'no tracking below', 10, MUT)
txt(TRK_X + TRK_W + 12, AG_Y + 52, 'the line by design', 10, MUT)
txt(TRK_X + TRK_W + 12, LINE_Y - 12, 'interaction', 9.5, MUT, 400, italic=True)

# ---- shared agent context panel ------------------------------------------
rect(BX, PAN_Y, 1092, PAN_B - PAN_Y, PANEL, LINE, rx=12)
o.append(f'<rect x="{BX + 20}" y="{PAN_Y + 16}" width="20" height="2.5" fill="{INK}"/>')
txt(BX + 50, PAN_Y + 22, 'SHARED AGENT CONTEXT', 11, INK, 800, ls=1.6)
txt(BX + 50 + 152, PAN_Y + 22, 'one stack — every concurrent session loads from it', 11, MUT)

BANDS = [
    ('Project memory', 'what this piece of work has established — decisions, constraints, state',
     'situational', '[ proj1/*.md ]', 'DELIVERABLE', FAINT),
    ('General memory', 'what holds across projects — how things are done here',
     'situational', '[ docs/*.md ]', 'REFERENCE', MUT),
    ('Templates', 'reusable shapes for recurring work — the roles an agent can take',
     'situational', '[ agents/*.md ]', 'ROLES', BODY),
    ('Working standards', 'how human and agent work together — autonomy, pushback, quality bar',
     'always', '[ soul.md · claude.md · vendor.md ]', 'RELATIONSHIP', INK),
]
by, bh, bgap = PAN_Y + 32, 46, 10
bx, bw = BX + 20, 1052
for i, (name, sub, load, ex, payload, accent) in enumerate(BANDS):
    y = by + i * (bh + bgap)
    rect(bx, y, bw, bh, '#FFFFFF', LINE, rx=8)
    o.append(f'<rect x="{bx}" y="{y + 8}" width="4" height="{bh - 16}" rx="2" fill="{accent}"/>')
    # load-discipline pill
    pw = 66
    always = load == 'always'
    rect(bx + 16, y + 15, pw, 18, INK if always else '#FFFFFF', INK if always else LINE, rx=9, sw=1)
    txt(bx + 16 + pw / 2, y + 28, load.upper(), 8, '#FFFFFF' if always else MUT, 700, 'middle', ls=0.9)
    txt(bx + 16 + pw + 18, y + 22, name, 14, INK, 700)
    txt(bx + 16 + pw + 18, y + 39, sub, 11, MUT)
    mono(bx + bw - 16, y + 30, ex, 10.5, 'end')
    txt(1240, y + 30, payload, 8.5, accent if accent != FAINT else MUT, 800, ls=0.9)

# ---- the three flows ------------------------------------------------------
arrow(mid[0], PAN_Y - 4, mid[0], AG_Y + AG_H + 6, LOAD, sw=3)
txt(mid[0] + 14, AG_Y + AG_H + 26, 'LOAD', 10, LOAD, 800, ls=1.1)
txt(mid[0] + 56, AG_Y + AG_H + 26, 'standards always · the rest situational', 10, MUT)
arrow(mid[2], AG_Y + AG_H + 6, mid[2], PAN_Y - 4, PROMOTE, sw=3)
txt(mid[2] + 14, AG_Y + AG_H + 26, 'PROMOTE', 10, PROMOTE, 800, ls=1.1)
txt(mid[2] + 76, AG_Y + AG_H + 26, 'so the next session inherits it', 10, MUT)
arrow(CTX_X + 460, ROW2_Y + ROW_H + 6, CTX_X + 460, PAN_Y - 6, GOVERN, 'GOVERN', at=0.72)
arrow(CTX_X + 540, PAN_Y - 6, CTX_X + 540, ROW2_Y + ROW_H + 6, PROMOTE, 'PROMOTE', at=0.28)

# ---- footer ---------------------------------------------------------------
txt(L, 754, 'Grey mono labels are one working example — kanban, GTD, a Claude Code file layout. '
            'The model is tool-neutral; swap the overlay for your own stack.', 10, FAINT, 400,
    italic=True)
txt(R, 754, 'LOAD is cheap and mostly automatic · PROMOTE is the human job that does not scale '
            'on throughput', 10, MUT, 400, 'end')

o.append('</svg>')
open(sys.argv[1] if len(sys.argv) > 1 else 'out.svg', 'w').write('\n'.join(o))
