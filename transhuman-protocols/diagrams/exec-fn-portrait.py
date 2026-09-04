# -*- coding: utf-8 -*-
"""Transpose the executive-function diagram from landscape to portrait.

The landscape original is four columns wide, which is why scaling it into a 4:5 frame leaves
a band. Portrait splits the human/AI divide horizontally instead of vertically and stacks the
two halves, so each half gets the full width and the boxes grow rather than shrink.

Palette is CSS custom properties, so the same source renders dark for the video and light for
an A4 handout: `render(theme='light')`.
"""
W, H = 1040, 1290

DARK = dict(bg='#101828', card='#16223A', card2='#141F36', card3='#17233C', stroke='#2F4068',
            ink='#FFFFFF', mut='#C6D2E4', dim='#8FA0BB', faint='#46587A',
            pill='#1B2942', pillstroke='#46587A', loop='#5ECB92', loopfill='#24365C',
            inner='#101A2E', innerstroke='#3C5480', rule='#FFFFFF')
LIGHT = dict(bg='#FFFFFF', card='#F4F7FC', card2='#F7F9FD', card3='#EEF3FA', stroke='#C3D0E4',
             ink='#0B1424', mut='#31435F', dim='#5B6E8C', faint='#93A4BE',
             pill='#E8EFF9', pillstroke='#B4C4DC', loop='#1E9B62', loopfill='#E4F5EC',
             inner='#FFFFFF', innerstroke='#B4C4DC', rule='#31435F')
KEY = dict(ws='#C7D9FF', gr='#8FB6FF', pr='#5C90F0', tpl='#E8A33D',
           projects='#5ECB92', status='#C08BFF')
KEY_LIGHT = dict(ws='#5C90F0', gr='#3A73D9', pr='#1F4FA8', tpl='#B7761E',
                 projects='#1E9B62', status='#7C46C4')

F = 'Poppins, Inter, "Segoe UI", Helvetica, Arial, sans-serif'
M = '"JetBrains Mono", ui-monospace, monospace'

def esc(s): return s.replace('&','&amp;').replace('<','&lt;')

def txt(x,y,s,size=13,weight=400,fill='var(--ink)',anchor='start',fam=F,ls=None,op=None):
    a=f'x="{x}" y="{y}" font-family=\'{fam}\' font-size="{size}" font-weight="{weight}" fill="{fill}"'
    if anchor!='start': a+=f' text-anchor="{anchor}"'
    if ls: a+=f' letter-spacing="{ls}"'
    if op: a+=f' opacity="{op}"'
    return f'<text {a}>{esc(s)}</text>'

def card(x,y,w,h,fill='var(--card)',stroke='var(--stroke)',rx=12,sw=1.2,extra=''):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{sw}"{extra}/>')

def pill(x,y,w,label,fill='var(--pill)',stroke='var(--pillstroke)',ink='var(--mut)'):
    return (card(x,y,w,24,fill,stroke,rx=12,sw=1)
            + txt(x+w/2, y+16.5, label, 10, 800, ink, 'middle', M, '0.06em'))

def dotrow(x,y,items):
    out=[]; cx=x
    for label,colour in items:
        out.append(f'<circle cx="{cx+5}" cy="{y-4}" r="5" fill="{colour}"/>')
        out.append(txt(cx+18, y, label, 13, 400, 'var(--mut)'))
        cx += 22 + len(label)*7.4
    return ''.join(out)

def bullets(x,y,items,step=25):
    out=[]
    for i,(label,colour) in enumerate(items):
        yy=y+i*step
        out.append(f'<circle cx="{x+5}" cy="{yy-4}" r="4.6" fill="{colour}"/>')
        out.append(txt(x+18, yy, label, 13, 400, 'var(--mut)'))
    return ''.join(out)

def build(k, stage=2):
    o=[]
    # ---------------- human band -------------------------------------------
    # context cards
    # the two context cards and the three tracking cards read as two aligned groups, so
    # both span exactly 102..466 rather than merely starting together
    for title,yy in [('Shared context',72),('Individual context',264)]:
        o.append(card(36, yy, 300, 172, 'var(--card3)'))
        o.append(txt(60, yy+40, title, 16, 700, 'var(--ink)'))
        o.append(bullets(60, yy+70, [('working standards',k['ws']),('general reference',k['gr']),
                                     ('project reference',k['pr']),('templates',k['tpl'])], step=26))
    # tracking cards
    for title,yy in [('Shared tracking',72),('Individual tracking',202),('Working session tracking',332)]:
        o.append(card(380, yy, 610, 104, 'var(--card)'))
        o.append(txt(408, yy+40, title, 18, 700, 'var(--ink)'))
        o.append(dotrow(408, yy+74, [('projects',k['projects']),('status',k['status'])]))
    for yy in (176, 306):                        # sync arrows between the tracking levels
        o.append(f'<line x1="685" y1="{yy}" x2="685" y2="{yy+26}" stroke="var(--rule)" '
                 f'stroke-width="2" marker-start="url(#up)" marker-end="url(#dn)"/>')

    if stage < 2:            # first click shows the human half alone
        return ''.join(o)
    # ---------------- the divide -------------------------------------------
    o.append(txt(36, 508, 'HUMAN', 15, 800, 'var(--faint)', ls='0.34em'))
    o.append('<line x1="24" y1="524" x2="1016" y2="524" stroke="var(--faint)" '
             'stroke-width="2.5" stroke-dasharray="9 9"/>')
    o.append(txt(36, 556, 'AI', 15, 800, 'var(--faint)', ls='0.34em'))
    # the cross-divide sync: in landscape this arrow is horizontal; here it is the hinge
    o.append('<line x1="685" y1="436" x2="685" y2="586" stroke="var(--rule)" stroke-width="2" '
             'marker-start="url(#up)" marker-end="url(#dn)"/>')
    o.append(txt(705, 508, 'in sync', 12, 600, 'var(--dim)', fam=M, ls='0.06em'))

    # ---------------- AI band ----------------------------------------------
    RX, RW = 380, 610          # right column, same x extent as the tracking cards above                    # right column: session loop and working memory
    # session replay loop: top edge on store 1, bottom edge on store 2, with its siblings
    # pulled out far enough to read as a stack rather than a drop shadow
    for dx in (18, 9):   # the stack must clear working memory's top edge at 846
        o.append(card(RX+dx, 586+dx, RW, 236, 'var(--card)', 'var(--loop)', sw=1.2))
    o.append(card(RX, 586, RW, 236, 'var(--loopfill)', 'var(--loop)', sw=1.6))
    o.append(txt(RX+30, 634, 'Session replay loop', 19, 700, 'var(--ink)'))
    o.append(card(RX+30, 664, 340, 46, 'var(--inner)', 'var(--innerstroke)', rx=10, sw=1))
    o.append(txt(RX+200, 693, 'sub-agents · tools · API calls', 12, 600, 'var(--dim)', 'middle'))
    o.append(txt(RX+30, 762, 'one of several that may be running', 12, 400, 'var(--dim)'))
    # working memory: top edge on store 3, bottom edge on store 4
    o.append(card(RX, 846, RW, 252, 'var(--card)'))
    o.append(txt(RX+30, 898, 'Working memory', 19, 700, 'var(--ink)'))
    o.append(pill(RX+30, 918, 104, 'AUTOMATIC'))
    o.append(txt(RX+30, 990, 'what the session is holding right now', 12, 400, 'var(--dim)'))
    o.append(f'<line x1="{RX+RW/2}" y1="826" x2="{RX+RW/2}" y2="842" stroke="var(--rule)" '
             f'stroke-width="2" marker-start="url(#up)" marker-end="url(#dn)"/>')

    # the four stores, down the left
    stores=[('Working standards','ALWAYS',k['ws'],586,None),
            ('General reference','AS-NEEDED',k['gr'],714,None),
            ('Project reference','PER PROJECT',k['pr'],842,None),
            ('Templates','AS-NEEDED',k['tpl'],970,'(including agent role definitions)')]
    for title,badge,colour,yy,sub in stores:
        h=112 if sub is None else 128
        o.append(card(36, yy, 300, h, 'var(--card2)'))
        o.append(f'<rect x="36" y="{yy+18}" width="5" height="{h-36}" rx="2.5" fill="{colour}"/>')
        o.append(txt(62, yy+42, title, 16, 700, 'var(--ink)'))
        if sub: o.append(txt(62, yy+64, sub, 11, 400, 'var(--dim)'))
        o.append(pill(62, yy+(62 if sub is None else 80), 96 if len(badge)<9 else 112, badge))
    # --- connector layer -----------------------------------------------------
    # Transposed from the landscape original, flow for flow:
    #   stores -> loading rail -> session loop            (one way, automatic)
    #   session loop -> promotion rail -> all four stores AND human Individual context
    #   project reference -> general reference -> working standards  (cascade; templates is outside it)
    #   a dashed tie marking that the same content types exist on both sides of the divide
    SY = [642, 770, 898, 1034]                 # vertical centre of each store
    # promotion cascade between the top three stores
    for yy in (714, 842):
        o.append(f'<line x1="196" y1="{yy-6}" x2="196" y2="{yy-22}" stroke="var(--dim)" '
                 f'stroke-width="1.6" marker-end="url(#tipS)"/>')
    # loading: each store stubs into the rail, the rail feeds the loop
    for yy in SY:
        o.append(f'<line x1="336" y1="{yy}" x2="352" y2="{yy}" stroke="var(--dim)" stroke-width="1.4"/>')
    o.append(f'<path d="M352 {SY[0]} L352 {SY[-1]}" fill="none" stroke="var(--dim)" stroke-width="1.4"/>')
    o.append(f'<line x1="352" y1="670" x2="{RX-3}" y2="670" stroke="var(--dim)" stroke-width="1.4" '
             f'marker-end="url(#tipS)"/>')
    o.append('<g transform="translate(368,880) rotate(-90)">'
             + txt(0,-4,'loading',12,700,'var(--dim)','middle',M,'0.06em')
             + txt(0,11,'automatic',10,400,'var(--dim)','middle',M,'0.06em') + '</g>')
    # promotion: out of the loop, down the right, along the bottom, up the left, into every
    # store and on across the divide into the human's individual context
    o.append(f'<path d="M{RX+RW+18} 700 L1018 700 L1018 1152 L18 1152 L18 380" fill="none" '
             f'stroke="var(--mut)" stroke-width="1.5"/>')
    for yy in SY:
        o.append(f'<line x1="18" y1="{yy}" x2="34" y2="{yy}" stroke="var(--mut)" '
                 f'stroke-width="1.5" marker-end="url(#tipM)"/>')
    o.append('<line x1="18" y1="380" x2="34" y2="380" stroke="var(--mut)" stroke-width="1.5" '
             'marker-end="url(#tipM)"/>')
    # label on the bottom leg: the right margin has no room beside the stacked loop cards
    o.append(txt(520, 1146, 'promotion', 12, 700, 'var(--mut)', 'middle', M, '0.06em'))
    o.append(txt(520, 1172, 'human-involved', 10, 400, 'var(--dim)', 'middle', M, '0.06em'))
    # the same content types exist on both sides: a dashed tie across the divide
    o.append('<path d="M196 586 L196 450" fill="none" stroke="var(--dim)" stroke-width="1.4" '
             'stroke-dasharray="7 5" marker-end="url(#bar)"/>')
    return ''.join(o)

def render(theme='dark', stage=2):
    pal = dict(DARK if theme=='dark' else LIGHT)
    k   = KEY if theme=='dark' else KEY_LIGHT
    vars_=';'.join(f'--{n}:{v}' for n,v in pal.items())
    arrow=lambda i,d,c,s: (f'<marker id="{i}" markerWidth="9" markerHeight="9" refX="{7.6 if d=="dn" else 1.4}" '
        f'refY="4.5" orient="auto" markerUnits="userSpaceOnUse">'
        f'<path d="{"M0,0 L9,4.5 L0,9 Z" if d=="dn" else "M9,0 L0,4.5 L9,9 Z"}" fill="{c}"/></marker>')
    return (f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" style="{vars_}" '
            f'role="img" aria-label="Executive function across human and AI, portrait">'
            f'<defs>{arrow("dn","dn","var(--rule)",2)}{arrow("up","up","var(--rule)",2)}'
            f'{arrow("tipS","dn","var(--dim)",1.4)}{arrow("tipM","dn","var(--mut)",1.5)}'
            f'<marker id="bar" markerWidth="12" markerHeight="20" refX="4" refY="10" '
            f'orient="auto" markerUnits="userSpaceOnUse">'
            f'<rect x="2" y="0" width="3" height="20" fill="var(--dim)"/></marker></defs>'
            f'<rect x="0" y="0" width="{W}" height="{H}" fill="var(--bg)"/>'
            + build(k, stage) + '</svg>')

if __name__=='__main__':
    for th in ('dark','light'):
        open(f'exec-fn-portrait-{th}.svg','w',encoding='utf8').write(render(th))
    open('exec-fn-portrait-dark-stage1.svg','w',encoding='utf8').write(render('dark', stage=1))
    print('wrote both themes plus the stage-1 build')
