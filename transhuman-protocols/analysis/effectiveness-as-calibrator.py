#!/usr/bin/env python3
"""The canonical effectiveness equation calibrates the model. Run 2026-08-28.

    E = SUM_i [ (fit_i * correctness_i) / (load_i + debt_i) ] / time

Taking all four parts seriously removes the need for a calibration target:

  /time      is the regulariser. Effort per item trades against items per period.
             Drop it and the score corners on MAXIMUM effort.
  SUM_i      says the cost terms are per ITEM. Debt accrues per item passed through
             at low attention, not per tick (as in core/loop.mjs).
  product /  says which terms are bounded: you MULTIPLY shares (fit, correctness in
  sum        [0,1] -- "how right") and ADD accumulations (load, debt -- "how much you
             are carrying"). Clamp the numerator, NEVER the denominator. Every
             cornering seen while deriving this was a clamped cost saturating, which
             makes the bad behaviour free.
  coeffs     are nuisance. E is a rate with a dimensionless numerator, so across arms
             sharing all nuisance parameters the coefficients cancel in the comparison.
             A shared parameterisation does not have to be right; it has to be shared.

Result, untuned: interior optima in both R and H, and with no externalisation
affordance the OPTIMAL policy is H* = 0 -- never write back -- with store validity
0.00. A good affordance moves H* to 0.6 and validity to 0.94.
"""
import numpy as np


def steady(R, H, cH, g=0.10, d0=0.02, dv=0.02, f=0.06, ret=0.5, nb=0.5,
           cR=0.45, c0=0.55, delta=0.020, rhoD=0.020, kap=0.04, Dbase=0.15,
           b=0.35, etah=0.9, Bm=0.55, T=6000,
           t0=0.35, tR=1.0, tH=0.6, tL=0.25):
    X, V, D, L = 0.3, 0.27, 0.3, 0.4
    W = H
    for _ in range(T):
        lam = X * nb
        t = max(t0 + tR * R + tH * H - tL * lam, 0.05)
        n = 1.0 / t                                              # items this tick
        Vn = (1 - d0) * V * (1 - dv) + f * W
        Xn = min(max((1 - d0) * X + f * W + g * lam * (1 - X)
                     - ret * W * max(X - V, 0), 0), 1)
        V, X = min(max(Vn, 0), Xn), Xn
        L = max(L + 0.03 * (c0 * (1 - lam) + cR * R + cH * H - L), 0)      # unbounded
        D = max(D + n * (delta * (1 - R) - rhoD * R) - kap * (D - Dbase), 0)  # per item
    Xv = V / X if X > 1e-9 else 0.0
    K = 1 / (1 + D)
    fit = min(1.0, 0.55 + b * (X * nb) * (2 * Xv - 1))
    corr = min(1.0, Bm + etah * R * K * 0.5)
    t = max(t0 + tR * R + tH * H - tL * (X * nb), 0.05)
    per = (fit * corr) / ((1 + 4 * L) + (1 + 4 * D))
    return dict(E=per / t, per=per, rate=1 / t, L=L, D=D, Xv=Xv, Xm=X, fit=fit, corr=corr)


def argmax(cH, **kw):
    best = None
    for R in np.arange(0.1, 1.01, 0.1):
        for H in np.arange(0.0, 1.01, 0.1):
            s = steady(R, H, cH, **kw); s['R'], s['H'] = R, H
            if best is None or s['E'] > best['E']:
                best = s
    return best


if __name__ == '__main__':
    print("Interior optima, untuned. cH is the cost of writing back; affordance lowers it.")
    for cH, lab in [(0.60, 'no affordance  '), (0.30, 'good affordance'), (0.15, 'strong         ')]:
        x = argmax(cH)
        print(f"  {lab} R*={x['R']:.1f} H*={x['H']:.1f} E={x['E']:.4f} "
              f"items/t={x['rate']:.2f} L={x['L']:.2f} D={x['D']:.2f} Xv={x['Xv']:.2f}")
    print("  => with no affordance the OPTIMAL policy is never to write back, and the")
    print("     store sits at validity 0.00. The affordance does not make write-back")
    print("     better; it makes it worth doing.\n")

    x = argmax(0.30); R = x['R']
    print(f"What a manager sees as maintenance rises (R={R:.1f} held, g=0.10):")
    for H in [0.0, 0.1, 0.2, 0.4, 0.7]:
        s = steady(R, H, 0.30)
        print(f"  H={H:<4} items/t={s['rate']:.2f} fit={s['fit']:.3f} "
              f"corr={s['corr']:.3f} E={s['E']:.4f} Xv={s['Xv']:.2f}")
    print("  => throughput falls ~28% while fit rises. Maintenance LOOKS like slowdown;")
    print("     the quality it buys is the invisible term. That is why the trap is chosen.\n")

    print("g=0 ablation (no retrieval persistence -- forgetting works):")
    for H in [0.0, 0.2, 0.7]:
        s = steady(R, H, 0.30, g=0.0)
        print(f"  H={H:<4} E={s['E']:.4f} Xm={s['Xm']:.2f} Xv={s['Xv']:.2f}")
