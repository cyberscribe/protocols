#!/usr/bin/env python3
"""SUPERSEDED IN PART — see the header note below.

Self-adjudication: the reviewer IS the worker, iterating and accruing load.
Run 2026-08-28, headless probe (not wired to model.mjs -- same status as the
other files in this folder).

The one structural move: with an outside witness the margin sigma_A is exogenous.
With SELF-review it is a function of the worker's own state --

    sigma_self = S_FLOOR + A_D*D + A_L*L

-- so the reviewer's accuracy degrades with exactly the two quantities the rest
of the model says accumulate. Crossover 0.30 is inherited from the outside-witness
sweep: above it a reviewer is worse than none.

COEFFICIENTS ARE INVENTED. The shape and the signs follow from the structure;
the locus does not. Report the shape, not the numbers.
"""
import math, random
# !! UNIT SLIP, found 2026-08-28 and left visible on purpose.
# CROSS = 0.30 is a RATIO to sigma_q (~0.07). The absolute crossover is 0.021.
# Read as an absolute sigma, S_FLOOR = 0.04 already sits 1.9x past it, so the flip
# locus came out empty and the sign of the answer was wrong.
# The repair is NOT a rescale -- derive the margin from the reveal gate instead:
#     ratio_self = lam * (1 - K*R),  K = 1/(1+D),  crossover at ratio 0.30
# which makes the locus a consequence of the model rather than of three invented
# coefficients. Kept below for the record; superseded by SPEC-phase1b-and-viz.md A2.
SIGMA_Q, CROSS_RATIO = 0.07, 0.30
CROSS_ABS = CROSS_RATIO * SIGMA_Q          # 0.021
S_FLOOR, A_D, A_L, CROSS = 0.04, 0.55, 0.30, 0.30
def sigma_self(L, D): return S_FLOOR + A_D*D + A_L*L


def flip_locus():
    """Debt at which self-review stops being worth doing, per load level."""
    out = []
    for L in [0, .2, .4, .6, .8, 1.0]:
        d = (CROSS - S_FLOOR - A_L*L) / A_D
        out.append((L, d if d >= 0 else None))
    return out


def iterate(L0, D0, passes, cost=0.11, gain=0.20):
    """Each self-review pass costs load and is graded by the current margin.
    Beyond the crossover a pass is actively harmful, not merely useless."""
    L, D, q, hist = L0, D0, 0.55, []
    for i in range(passes):
        s = sigma_self(L, D)
        acc = max(0.0, 1 - s/CROSS)            # useful share
        harm = max(0.0, s/CROSS - 1) * 0.6     # past the crossover
        q = min(1.0, max(0.0, q + gain*acc - gain*harm))
        L = min(1.6, L + cost)
        hist.append((i+1, s, q))
    return hist


def corr_HR(N=4000, seed=3):
    """Does self-review supply the independent variation C2 needs?
    Only the DRAW is exogenous; its SCALE is a function of the shared states."""
    random.seed(seed); H = []; R = []; L, D = 0.3, 0.1
    for _ in range(N):
        L = min(1.2, max(0.0, L + random.gauss(0, .02) - .01*(L-.3)))
        D = min(1.0, max(0.0, D + random.gauss(0, .008) - .02*(D-.1)))
        s = sigma_self(L, D)
        surprise = abs(random.gauss(0, 1)) * s
        z = -1.0*L - 0.8*D
        H.append(1/(1+math.exp(-(z + 1.0*(surprise - s*0.8)))))
        R.append(1/(1+math.exp(-z)))
    ma, mb = sum(H)/len(H), sum(R)/len(R)
    sa = sum((v-ma)**2 for v in H)**.5; sb = sum((v-mb)**2 for v in R)**.5
    return abs(sum((H[i]-ma)*(R[i]-mb) for i in range(len(H)))/(sa*sb))


if __name__ == '__main__':
    print("1. WHERE SELF-REVIEW FLIPS FROM ASSET TO LIABILITY")
    for L, d in flip_locus():
        print(f"   load {L:.2f} -> flips at debt {d:.2f}" if d is not None
              else f"   load {L:.2f} -> never worth doing at any debt")
    print()
    print("2. ITERATING ON YOUR OWN RESULT")
    for lbl, L0, D0 in [("fresh, no debt", .15, .02), ("mid-day", .45, .15),
                        ("loaded & indebted", .70, .35)]:
        h = iterate(L0, D0, 7); b = max(h, key=lambda r: r[2])
        print(f"   {lbl:<20} best after {b[0]} pass(es), quality {b[2]:.3f}   " +
              " ".join(f"p{i}:{q:.2f}" for i, _, q in h))
    print()
    print("3. C2 UNDER SELF-REVIEW")
    print(f"   |corr(H,R)| = {corr_HR():.3f}   "
          "(outside witness 0.073-0.338; gate < 0.99; readable < 0.5)")
    print("   Partial independence only: the draw is fresh, the SCALE is endogenous.")
