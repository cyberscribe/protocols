#!/usr/bin/env python3
"""Does the sign structure survive a conservative store term?  Run 2026-08-28.

    signed   fit = fit0 + b*Lam*(2*Xv - 1)   a stale store actively HARMS
    bounded  fit = fit0 + b*Lam*Xv           a stale store merely fails to help

Coarse re-derivation, not the engine. Result: under `bounded` the whole 2x2 goes
to +0.0% -- the entire externalisation benefit was resting on the store's ability
to go negative. The sigma_A crossover survives and strengthens.
"""
import numpy as np

def steady(R, H, cH, g, qW, mode, d0=.02, dv=.02, f=.06, ret=.5, nb=.5, cR=.45,
           c0=.55, delta=.020, rhoD=.020, kap=.04, Dbase=.15, b=.35, etah=.9,
           Bm=.55, T=900, t0=.35, tR=1.0, tH=.6, tL=.25):
    X, V, D, L = .3, .27, .3, .4
    W = H
    for _ in range(T):
        lam = X*nb; t = max(t0 + tR*R + tH*H - tL*lam, .05); n = 1/t
        Vn = (1-d0)*V*(1-dv) + f*W*qW
        Xn = min(max((1-d0)*X + f*W + g*lam*(1-X) - ret*W*max(X-V, 0), 0), 1)
        V, X = min(max(Vn, 0), Xn), Xn
        L = max(L + .03*(c0*(1-lam) + cR*R + cH*H - L), 0)
        D = max(D + n*(delta*(1-R) - rhoD*R) - kap*(D-Dbase), 0)
    Xv = V/X if X > 1e-9 else 0.
    K = 1/(1+D)
    store = (2*Xv - 1) if mode == 'signed' else Xv
    fit = min(1, .55 + b*(X*nb)*store)
    cor = min(1, Bm + etah*R*K*.5)
    t = max(t0 + tR*R + tH*H - tL*(X*nb), .05)
    return ((fit*cor) / ((1+4*L) + (1+4*D))) / t


def best(E, qW, g, sA, mode):
    hb = 0 if sA <= 0 else .46 + .54*(1 - np.exp(-sA*2.6))
    qm = 1 if sA <= 0 else 1.0 - .57*(1 - np.exp(-sA*2.4))
    cH = .60*(1 - .75*E); q = qW*qm; bb = -1
    for R in np.arange(.1, 1.01, .15):
        for H in np.arange(0, 1.01, .125):
            Hs = max(H, hb*.9) if hb > 0 else H
            e = steady(R, Hs, cH, g, q, mode)
            if e > bb: bb = e
    return bb


if __name__ == '__main__':
    for mode in ['signed', 'bounded']:
        print(f"=== {mode} ===")
        base = best(0, 0.05, 0.10, 0, mode)
        for k, (E, q) in {'neither': (0, .05), 'tool only': (1., .05),
                          'practice only': (0, 1.), 'both': (1., 1.)}.items():
            print(f"  {k:<14} {(best(E,q,.10,0,mode)/base-1)*100:+6.1f}%")
        nr = best(.75, .9, .10, 0, mode)
        print("  crossover: " + " ".join(
            f"sA={s:<4}{(best(.75,.9,.10,s,mode)/nr-1)*100:+6.1f}%"
            for s in [0, .15, .3, .5, .8, 1.1]))
