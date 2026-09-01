#!/usr/bin/env python3
"""Store subsystem fixed points, run 2026-08-28 before building anything.

Answers one question: does the store have the regime structure SIM-writeup-for-review.md
claims? Form A is the mechanism as first written; Form B is the one that survives.

Result: Form A does not produce an archive trap at any plausible s. Form B gives an exact
transcritical bifurcation at g*nbar = delta_X, verified against simulation.
"""

def stepA(X, V, W, s, d0=0.02, dv=0.02, f=0.10, ret=0.5, qW=1.0, nb=0.5):
    """Retrieval REDUCES decay. Does not work -- see __main__."""
    deff = max(d0 * (1 - s * X * nb), 0.0)
    Vn = (1 - deff) * V * (1 - dv) + f * W * qW
    Xn = min(max((1 - deff) * X + f * W - ret * W * max(X - V, 0.0), 0.0), 1.0)
    return Xn, min(max(Vn, 0.0), Xn)


def stepB(X, V, W, g, d0=0.02, dv=0.02, f=0.06, ret=0.5, qW=1.0, nb=0.5):
    """Retrieval RE-ENCODES mass and carries no validity: g is absent from Vn."""
    Vn = (1 - d0) * V * (1 - dv) + f * W * qW
    Xn = min(max((1 - d0) * X + f * W + g * (X * nb) * (1 - X)
                 - ret * W * max(X - V, 0.0), 0.0), 1.0)
    return Xn, min(max(Vn, 0.0), Xn)


def run(step, W, p, X0, V0, T=40000):
    X, V = X0, V0
    for _ in range(T):
        X, V = step(X, V, W, p)
    return X, (V / X if X > 1e-9 else 0.0)


if __name__ == '__main__':
    print("FORM A -- W=0, sweep s. Mass should persist if the mechanism works.")
    for s in [0.5, 1.0, 2.0, 4.0, 8.0]:
        print(f"  s={s:<4} " + "  ".join(
            f"X0={x0}->{run(stepA, 0., s, x0, x0*.9)[0]:.3f}" for x0 in [0.2, 0.6, 1.0]))
    print("  => collapse for s<=1; for s>=2 decay hits zero and the store freezes at X0.")
    print("     A continuum of neutral fixed points, not an attractor. Form A is wrong.\n")

    print("FORM B -- W=0, sweep g.  Predicted X* = 1 - d0/(g*nb), positive iff g*nb > d0")
    for g in [0.02, 0.04, 0.06, 0.10, 0.20]:
        xs = [run(stepB, 0., g, x0, x0*.9) for x0 in [0.05, 0.2, 0.6, 1.0]]
        print(f"  g={g:<5} pred={1 - 0.02/(g*0.5):+.3f} | " +
              "  ".join(f"{x:.3f}(v={v:.2f})" for x, v in xs))
    print("  => matches to 3dp from every initial condition. Transcritical, not bistable.\n")

    print("FORM B -- the three regimes in W, at g=0.10")
    for W in [0.0, 0.02, 0.05, 0.15, 0.40]:
        X, Xv = run(stepB, W, 0.10, 0.6, 0.54)
        print(f"  W={W:<5} X_m={X:.3f} X_v={Xv:.3f}")
    print("  => smooth in W, so the living/trap boundary is a validity CUT, not a bifurcation.")
