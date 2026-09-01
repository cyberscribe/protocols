---
title: "Recommendation — after phase 1b"
date: 2026-08-28
context: A1 works and its prediction fails; C10 and C11 fail; NO FLIP is ambiguous
---

# After phase 1b

Two of the failures are worth more than the things they were attached to. Taking them in order of what I would do first.

---

## 1. C11 — do not patch it. The gate is wrong, and the effect may be real.

**C11 was a bad check and that is my error.** "`E` non-decreasing up the ladder" asserts that accuracy is monotonically good — which is precisely what the crossover result had already denied. I wrote a gate encoding an assumption the model had told me might be false, which is the same class of mistake as C1: importing a criterion instead of deriving one.

**And the 0.4% may not be an artefact.** Two readings, and they are worth separating before touching anything:

| reading | what it says |
|---|---|
| **modelling gap** | noise-driven write-back should be discounted in *quantity* as well as quality; `qW_eff` already does the quality half |
| **real effect** | **the value of review is partly its imperfection.** A perfect reviewer confirms you; a fallible one surprises you, and being surprised is what makes you write |

The second is the thesis eating its own tail, and it is the most interesting sentence in the report: *assistance too good to surprise you stops producing the practice that sustains you* — the same mechanism as the whole programme, with the reviewer in the AI's chair.

**But rungs 3 and 4 are pinned at the 0.90 reveal ceiling, so they are nearly the same reviewer by construction.** That is where a spurious 0.4% would come from.

**The discriminating test, which changes nothing in the model:** lift the reveal cap and re-run. If rung 4 then reveals more than rung 3 and the inversion vanishes, C11 was measuring the ceiling and should be re-scoped to exclude pinned rungs. **If it survives an uncapped reveal, it is real** — and it is a finding, not a bug. Either way you learn something and no model change is made against a failing gate.

---

## 2. C10 — the ceiling is the finding, and it is a knife-edge in one unanchored ratio

`K* = γR/(δ_K + γR)` caps `K·R` at `r/(1+r)` where `r = γ/δ_K`. **That ceiling is set entirely by one nuisance ratio** — the one whose comment already needed correcting once.

```
r = 2.5   →  ceiling 0.714   threshold at λ=1 is 0.700   margin 0.014 (2.0%)
r > 2.333 is required for the wedge to exist at all at λ=1
r ≥ 4.0   is required for a wedge with any depth (ceiling ≥ 0.80)
```

**So "self-review is essentially never worth doing" and "self-review has a wedge" are separated by `r` moving from 2.5 to 2.4.** That is not a result. It is a coincidence of an unmeasured parameter, and publishing either side of it would be indefensible.

**Recommendation: convert the knife-edge into a phase boundary.** Sweep `r = γ/δ_K` against `λ`, draw the 0.30 crossover across it, and report the locus. Then the claim becomes interpretable rather than arbitrary:

> **Self-review is worth doing only if you rebuild capability faster than a certain multiple of the rate you lose it.**

`r` is *how fast you regain skill versus how fast it decays* — a quantity a practitioner can reason about, and one worth trying to anchor empirically. A phase boundary in it is a real deliverable; a single point 2% from the edge is not.

**And note what three independent routes now agree on**, whichever side of the boundary `r` sits: the outside witness clears C2 where nothing endogenous could; self-review supplies only partial independence (0.752 against 0.073–0.338); and self-review cannot reach the accuracy threshold except at the very top of the architecture's range. **You cannot be your own witness** — by covariance, by accuracy, and by ceiling.

---

## 3. A1 — substitutes, not complements, and the mechanism generalises

Your diagnosis is right and it is the valuable part. **Complementarity requires that a factor can go to zero.** Tool × practice multiplied because either alone produces *literally nothing written*. The two stores each sit on a floor (`fit0 = 0.55`, `B ≈ 0.55`), so each is a marginal addition to a substantial base and there is nothing to compound.

That is a distinction worth carrying into the venture language, because it is the difference between two kinds of advice:

> **Tool and practice are a gate. Which store you invest in is an optimisation.**

**The row I would not bank yet is the second one.** *Fixed per-side investment: maintaining both (+24.3%) is worse than maintaining the better one alone (+32.6%)* — spending twice the budget for less. The mechanism has to be that consulting the human side costs attention (`Λ^H` is not free, by design) and that cost is not repaid once the AI side already carries correctness.

That is the diagram's asymmetry producing a policy consequence, and it is a strong claim — *do not maintain your project tracking if your AI context is good* — resting on `b_H`, `b_A` and the consult cost, none of them anchored. **Probe it before it goes anywhere:** does the ordering survive a sweep of `c_cons` and of `b_H/b_A`? If it flips at plausible values it is a parameter story; if it holds across the space it is a finding, and a provocative one.

The closed form generalising with the consult gate inside it — AI side persisting at 0.3333 while the human side collapses to 3.7e-89 at the same `g` — is the diagram's asymmetry made analytic. **That is worth writing up on its own** regardless of what happens to the complementarity prediction.

---

## 4. NO FLIP — accepted, and it would have printed the opposite of the truth

Straightforwardly right, and given §2 the emptiness that will actually occur is *never worth it*. Two states, not one:

- **`ALWAYS WORTH IT`** — `σ_self` below the crossover across all reachable `(L, D)`; the plane shades entirely safe.
- **`NEVER WORTH IT`** — above it everywhere; the plane shades entirely hazardous.

The plane shades a **region** in both cases rather than drawing a curve, and the legend names which. A single ambiguous state on a panel whose whole job is to say which side of a line you are on is exactly the defect the design rules exist to prevent.

---

## What I would do, in order

1. Uncapped-reveal re-run for C11 — cheapest, and it decides whether you have a finding or an artefact.
2. `(r, λ)` sweep for the flip locus — converts the knife-edge into the phase boundary that is the actual deliverable.
3. `c_cons` and `b_H/b_A` probe on the "maintaining both is worse" row.
4. Re-scope C11 and split NO FLIP in the spec.

Nothing in 1–3 changes the model. All three are measurements against the existing engine, and each one turns something currently unpublishable into something reportable either way.
