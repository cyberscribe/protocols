#!/usr/bin/env python3
"""Trace space — Heylighen's stigmergy dimensions crossed with our six content types.

Zero-based: not a redraw of exec-fn-ai-org. The axes ARE the theory.

    x  reach        within scope, how reliably the trace is actually loaded
    y  persistence  -log10(evaporation rate); slow-evaporating is high

Leverage is reach / drift, and the axes are reach and inverse-drift, so leverage
is the PRODUCT of the axes: up-and-right, with hyperbolic contours. The cascade
is the gradient of the plane rather than a hierarchy drawn beside it.

Each content type appears twice, joined by an arrow from its human-side copy to
its AI-side copy. Arrow direction is the finding: it points RIGHT for context
(the AI loads it more reliably than you recall it) and LEFT for tracking (you
know it better than the AI does).

Positions are JUDGEMENTS, not measurements. Edit TYPES and re-run to argue.
"""
import sys

# key: (label, drift, reach_ai, reach_human, sematectonic, quantitative, label_pos)
TYPES = [
    ('standards', 'working standards', 0.002, 1.00, 0.40, False, False, 'below-l'),
    ('templates', 'templates',         0.004, 0.55, 0.20, True,  False, 'above'),
    ('general',   'general reference',  0.010, 0.60, 0.25, False, False, 'below'),
    ('project',   'project reference',  0.060, 0.75, 0.45, False, False, 'above'),
    ('projects',  'projects',           0.080, 0.35, 0.70, False, True,  'below'),
    ('status',    'status',             0.400, 0.45, 0.80, False, True,  'above'),
]
C = {'standards': ('#1E3A8A', '#5B8DEE'), 'general': ('#2563EB', '#85AFF5'),
     'project':   ('#60A5FA', '#AECFFB'), 'templates': ('#B45309', '#E0902F'),
     'projects':  ('#15803D', '#4ADE80'), 'status':    ('#9333EA', '#C084FC')}

W, H = 940, 600
L, R, T, B = 104, 862, 46, 500
PMIN, PMAX = 0.10, 2.95
import math
sx = lambda r: L + r * (R - L)
sy = lambda p: B - (p - PMIN) / (PMAX - PMIN) * (B - T)
pers = lambda d: -math.log10(d)
f = lambda v: f'{v:.1f}'

MODE = sys.argv[2] if len(sys.argv) > 2 else 'static'
def col(key):
    return C[key][0] if MODE == 'static' else f'var(--k-{key},{C[key][0]})'

s = []
a = s.append
a(f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Six content types plotted by how '
  f'reliably each is loaded against how slowly it goes stale, each shown twice — once as the '
  f'copy the person holds and once as the copy the AI holds, joined by an arrow. For the four '
  f'context types the arrow points right, meaning the AI loads them more reliably. For the two '
  f'tracking types it points left, meaning the person holds them better.">')
a('<defs>')
for k in C:
    a(f'<marker id="ah-{k}" markerWidth="9" markerHeight="9" refX="7.6" refY="4.5" '
      f'orient="auto"><path d="M0,0 L9,4.5 L0,9 Z" fill="{col(k)}"/></marker>')
a('</defs>')

# leverage contours: reach x persistence = const
for c in (0.45, 0.9, 1.5, 2.2):
    pts = []
    for i in range(61):
        r = 0.12 + i * (1.0 - 0.12) / 60
        p = c / r
        if PMIN <= p <= PMAX:
            pts.append(f'{sx(r):.1f},{sy(p):.1f}')
    if len(pts) > 1:
        a(f'<polyline points="{" ".join(pts)}" fill="none" stroke="currentColor" '
          f'stroke-width="1" opacity="0.17" stroke-dasharray="3 4"/>')
a(f'<text x="{R-6}" y="{T+15}" text-anchor="end" font-size="10.5" fill="currentColor" '
  f'opacity="0.42" letter-spacing="1.4">MORE LEVERAGE ↗</text>')

# axes
a(f'<line x1="{L}" y1="{B}" x2="{R}" y2="{B}" stroke="currentColor" stroke-width="1.2" opacity="0.35"/>')
a(f'<line x1="{L}" y1="{T}" x2="{L}" y2="{B}" stroke="currentColor" stroke-width="1.2" opacity="0.35"/>')
a(f'<text x="{(L+R)/2}" y="{B+42}" text-anchor="middle" font-size="12.5" fill="currentColor" '
  f'opacity="0.7">Reach — how reliably it is actually loaded, in scope →</text>')
a(f'<text transform="rotate(-90 22 {(T+B)/2})" x="22" y="{(T+B)/2}" text-anchor="middle" '
  f'font-size="12.5" fill="currentColor" opacity="0.7">Persistence — how slowly it goes stale →</text>')
for lab, p in (('minutes', 0.4), ('weeks', 1.22), ('months', 2.0), ('years', 2.7)):
    a(f'<text x="{L-12}" y="{sy(p)+4}" text-anchor="end" font-size="10" fill="currentColor" '
      f'opacity="0.45" font-family="ui-monospace,monospace">{lab}</text>')

# the cascade, through the AI-side points
casc = [t for t in TYPES if t[0] in ('project', 'general', 'standards')]
casc.sort(key=lambda t: t[2], reverse=True)
cp = [(sx(t[3]), sy(pers(t[2]))) for t in casc]
ex, ey = cp[-1]; px, py = cp[-2]
dx, dy = ex - px, ey - py; n = math.hypot(dx, dy)
cp[-1] = (ex - dx / n * 26, ey - dy / n * 26)
pts = ' '.join(f'{x:.1f},{y:.1f}' for x, y in cp)
a(f'<polyline points="{pts}" fill="none" stroke="currentColor" stroke-width="9" '
  f'opacity="0.075" stroke-linejoin="round" stroke-linecap="round"/>')

for key, label, drift, rai, rh, sema, quant, pos in TYPES:
    c = col(key)
    y = sy(pers(drift)); xa, xh = sx(rai), sx(rh)
    d = 1 if xa > xh else -1
    a(f'<line x1="{xh + d*11:.1f}" y1="{y:.1f}" x2="{xa - d*13:.1f}" y2="{y:.1f}" '
      f'stroke="{c}" stroke-width="1.7" opacity="0.62" marker-end="url(#ah-{key})"/>')
    # human copy: hollow
    if sema:
        a(f'<rect x="{xh-7:.1f}" y="{y-7:.1f}" width="14" height="14" transform="rotate(45 {xh:.1f} {y:.1f})" '
          f'fill="none" stroke="{c}" stroke-width="2.2"/>')
        a(f'<rect x="{xa-7.5:.1f}" y="{y-7.5:.1f}" width="15" height="15" transform="rotate(45 {xa:.1f} {y:.1f})" '
          f'fill="{c}"/>')
    else:
        a(f'<circle cx="{xh:.1f}" cy="{y:.1f}" r="7" fill="none" stroke="{c}" stroke-width="2.2"/>')
        a(f'<circle cx="{xa:.1f}" cy="{y:.1f}" r="7.5" fill="{c}"/>')
    if quant:   # quantitative traces get an inner ring
        a(f'<circle cx="{xa:.1f}" cy="{y:.1f}" r="3" fill="#FFFFFF" opacity="0.85"/>')
    ox, oy, anch = {'above': (0, -17, 'middle'), 'below': (0, 25, 'middle'),
                    'below-l': (14, 27, 'end')}[pos]
    a(f'<text x="{xa+ox:.1f}" y="{y+oy:.1f}" text-anchor="{anch}" font-size="13" '
      f'font-weight="600" fill="{c}">{label}</text>')

a(f'<g font-size="11" fill="currentColor" opacity="0.6">')
a(f'<circle cx="{L+8}" cy="{B+70}" r="6.5" fill="none" stroke="currentColor" stroke-width="2"/>')
a(f'<text x="{L+22}" y="{B+74}">the copy you hold</text>')
a(f'<circle cx="{L+152}" cy="{B+70}" r="7" fill="currentColor"/>')
a(f'<text x="{L+166}" y="{B+74}">the copy the AI holds</text>')
a(f'<rect x="{L+318}" y="{B+64}" width="13" height="13" transform="rotate(45 {L+324.5} {B+70.5})" '
  f'fill="currentColor"/>')
a(f'<text x="{L+338}" y="{B+74}">the work itself, unfinished</text>')
a(f'<circle cx="{L+520}" cy="{B+70}" r="7" fill="currentColor"/>')
a(f'<circle cx="{L+520}" cy="{B+70}" r="3" fill="#FFFFFF" opacity="0.85"/>')
a(f'<text x="{L+534}" y="{B+74}">a quantity, not a kind</text>')
a('</g>')
a('</svg>')

open(sys.argv[1] if len(sys.argv) > 1 else 'trace-space.svg', 'w').write('\n'.join(s))
