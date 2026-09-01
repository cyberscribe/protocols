---
title: "The externalisation simulation — v0.2, rewritten after review"
audience: a reviewer with no prior exposure to this project
date: 2026-08-28
status: pre-build. Nothing here has been run. v0.1 is archived as .archive-SIM-writeup-v0.1.md
---

# The externalisation simulation — v0.2

Rewritten in response to a review that returned **"do not build; rewrite once, then build."** All four blocking defects are accepted; §12 records what changed, what I pushed back on, and one addition the review's own argument implies.

**Nothing here has been run.**

---

## 1. The question

Several experiments show that **unguarded assistance can improve assisted performance while impairing subsequent unaided performance** — and, in the same experiment, that a guardrailed version improves assisted performance *more* without the unaided penalty. The counterexample matters as much as the effect: the harm is not intrinsic to assistance, it is a property of a particular configuration.

The question here is what makes the difference over long horizons:

> Context flows into each session automatically and free. Judgment flows back into storage only when someone deliberately puts it there, at a cost. **Does a maintained externalisation protocol produce a stable regime in which assistance is captured without capability loss — and what distinguishes that regime from the ones next to it?**

---

## 2. What changed, in one paragraph

v0.1 asked whether an arbitrarily quantised state cell stayed empty. That was the wrong target: emptiness in a continuous stochastic system depends on run length, thresholds, noise and initial conditions, and — as the review showed — the predicted emptiness did not even follow from the equations. **v0.2 asks instead which of three regimes the system settles into, and where the boundaries between them lie.** A regime boundary is a structural object in the way an occupancy count is not.

---

## 3. The three regimes — the headline

| regime | mechanism | signature |
|---|---|---|
| **Living store** | write-back refreshes and retires material fast enough that validity holds; loading reduces load without displacing reasoning | high `X_v`, capability sustained, calibration error small |
| **Archive trap** | mass grows faster than validity, and the most-loaded material is the least-reviewed; assisted outcomes stay good and conceal capability loss | high `X_m`, low `X_v`, capability falling, calibration error growing |
| **Forgetting recovery** | maintenance stops, stale context decays out of use, calibration recovers — but capability has to be rebuilt from a lower base | `X_m → 0`, calibration error returns toward zero, `K` recovering slowly from a deficit |

**Forgetting recovery is not a nice-to-have; it is what the equations actually produce** when writing-back stops and store mass decays geometrically. The review derived it and it is more interesting than what it replaced: *the archive stops lying to you once you stop reading it, but you do not get the years back.*

The conceptual frame is Kei Kreutler's, from this project's own Protocol Reader corpus: **latent memory versus living memory** — "living memory enacts worlds which live and die by attention" — and *threshold forgetting*. Storage is not memory preservation. A protective externalisation system is a protocol:

```
encode → retrieve → verify → revise or retire
```

**v0.1 implemented encode and automatic retrieve and neither of the last two.** It therefore modelled accumulation, not judgment-bearing externalisation — the same hole this project had already identified in its own diagram (no demotion arrow) and then reproduced in the model. §5.4 fixes it.

---

## 4. The treatment channels, now separated

v0.1 had one variable `Z` doing five jobs: enabling store growth, raising writing-back, raising reasoning, making process evidence available, and standing in for pedagogical guardrails. A high-`Z` run could not distinguish protection-by-externalisation from protection-by-preserved-reasoning. **That defeated the stated question.** Split:

| symbol | what it is | acts only on |
|---|---|---|
| `E` | **externalisation affordance** — storage, capture tooling, templates | the cost and the efficacy of writing back |
| `G` | **reasoning guardrail** — hints rather than answers | reasoning, and process observability |
| `H` | writing-back **effort** — a behaviour, not a treatment | — |
| `W = e(E)·H` | **actual writing back** | the store, and process evidence |

**Bastani's GPT Tutor belongs in `G`, not `E`.** Its guardrail was pedagogical — hints instead of solutions — not a storage or logging intervention. v0.1 mapped it to the observability channel and that was simply wrong.

**The state machine now classifies `W`, never `H`.** v0.1 called `H` "writing back" while the store was fed by `W = ZH`; the reading layer and the dynamics disagreed about what the bit meant.

---

## 5. The model

Discrete time; `logistic(x) = 1/(1+e^{-x})`; states clamped to `[0,1]`.

### 5.1 Exogenous, and fully specified

| symbol | meaning | form |
|---|---|---|
| `B_t` | the assistant's true base reliability | AR(1), φ = 0.80, mean 0.55, uniform shock ±0.10, clamped [0.30, 0.80] |
| `n_t` | task relevance draw — what share of the store this task can use | Beta(2,2), i.i.d., mean n̄ = 0.5 |
| `U_t` | unaided probe occasion | Bernoulli(p_U), p_U = 0.02; **`U_t = 1` forces `R_t = 1` and `Λ_t = 0` for that period** |

`B` is known to the model and never to the worker. The delay buffer is warm-started by running 2,000 burn-in periods before any measurement, so `O_{t−τ}` is always defined.

### 5.2 The two behaviours

```
H_t = logistic( h0 − h_T·T_t − h_L·L_t + h_ρ·ρ + h_E·E )              writing-back effort
R_t = logistic( r0 − r_T·T_t − r_L·L_t − r_Λ·Λ_t + r_G·G )            reasoning
```

`Λ` enters reasoning and never writing-back; `ρ` (capacity/discipline) enters writing-back and never reasoning. Without non-shared drivers the two are collinear and the reading layer is meaningless. Whether the separation is sufficient in the fitted system is a gate condition, not a guarantee (§10, W1).

### 5.3 Costs — both behaviours consume capacity

```
L_{t+1} = L_t + λ_L·[ c_0·(1 − Λ_t) + c_R·R_t + c_H(E)·H_t − L_t ]
c_H(E)  = c_H0·(1 − ε_E·E)
```

**v0.1 had no cost on either behaviour**, which removed the central trade-off from a model whose entire subject is a trade-off. Externalisation is supposed to cost attention now to reduce load or debt later; in v0.1 it was free. This also gives `E` a mechanism: an externalisation affordance is a thing that makes recording cheaper, which is what tooling actually does.

### 5.4 The store — encode, verify, revise, retire

Tracked as total mass `X_m` and valid mass `V`, with `X_v = V/X_m`.

```
V'    = (1 − δ_X)·V·(1 − δ_v) + f·W_t·q_W                  valid mass
X_m'  = (1 − δ_X)·X_m + f·W_t + g·Λ_t·(1 − X_m)            total mass — note the retrieval term
                     − ret·W_t·(X_m − V)                    retirement targets invalid mass
X_v'  = V'/X_m'          (X_v' := 0 when X_m' < ε)
Λ_t   = X_m · n_t
```

**`g·Λ(1 − X_m)` is the mechanism, and it is not what v0.2 first proposed.** Retrieval **re-encodes mass and carries no validity with it**: `g` appears in the mass equation and nowhere in the valid-mass equation. Using a document keeps it present; only verifying it keeps it true. That is Kreutler's latent/living distinction as a term rather than as a metaphor.

Three things are new and each answers a specific defect:

1. **`ret·W·(X_m − V)`** — writing back does not only add. Effort spent on the store also removes material that has gone invalid. This is *retire*, and it is what makes the model about judgment-bearing externalisation rather than accumulation.
2. **`q_W ≤ 1`** — incoming material is not automatically true. `q_W = 1` is an optimistic upper bound to be run as a scenario, not the baseline.
3. **`g·Λ(1 − X_m)`** — retrieval keeps material present without making it true. §7 P4 gives the bifurcation this produces and §12 records that the first version of this term did not work.

### 5.5 Evidence

```
avail_t = 1 − (1 − G)·(1 − W_t)                             noisy-OR: guardrail or writing back
ℓ_t     = avail_t · K_t                                     legibility gate
P_t     = ℓ_t·B_t + (1 − ℓ_t)·T_t
```

Process evidence must be produced — by a guardrail that forces articulation, or by the act of recording — and then be legible, which takes residual capability. Illegible evidence **echoes the prior rather than misleading**: it fails to correct, it does not deceive.

### 5.6 Outcome

```
human_t = R_t·K_t
O_t     = min( cap, B_t·(1 + b·Λ_t·(2·X_v − 1)) + η_h·human_t )
```

Valid context helps, stale context hurts, and output is capped — so a highly capable worker's contribution saturates and stops being visible in outcomes.

### 5.7 Trust — and what it is trust *in*

```
α_t     = logistic( a0 − a_L·L_t + a_K·K_t )
T_{t+1} = T_t + η·[ α_t·(P_t − T_t) + (1 − α_t)·(O_{t−τ} − T_t) ]
```

**`T` is the worker's belief about the assistant's *base* competence** — not about the configured assistant-plus-store system. This has to be stated, because a worker who learns the system's conditional performance and believes it is being *rational*, not miscalibrated. The thesis is an attribution claim: the error is failing to subtract one's own contribution and the store's.

Substituting `P` and solving properly — `P` contains `T`, so v0.1's "fixed point" was circular:

$$
T^{*}=\frac{\alpha\ell B+(1-\alpha)O}{\alpha\ell+(1-\alpha)}
\qquad\Longrightarrow\qquad
\boxed{\;T^{*}-B=\frac{(1-\alpha)\,(O-B)}{\alpha\ell+(1-\alpha)}\;}
$$

**Attribution error is generated by the gap between joint output and base assistant capability, and attenuated by legible process evidence.** Both terms are honest: `O > B` because the worker and the store really did contribute. This is the identity to build on; v0.1's `(1−α)(O−P)` was algebraically true and analytically useless.

Calibration target is `E[B_t | ℐ_t]`, the rational forecast given the AR(1) — not a trailing window chosen because it made a bit behave.

### 5.8 Capability

```
K_{t+1} = (1 − δ_K)·K_t + γ·( R_t + κ·H_t )·(1 − K_t)
```

**`κ = 0` in the baseline.** `κ > 0` is the explicit "externalisation builds capability" hypothesis and runs as an ablation. v0.1 flagged this term as unsupported by the evidence and then put it in the baseline anyway, which inserts the desired conclusion into the equation that is supposed to produce it.

### 5.9 Measurement

```
K^obs_t = K_t + ν_t     only where U_t = 1        ν ~ N(0, σ_ν²)
D_t     = K*_t − K^obs_t                          readout, never fed back
```

`K*` runs the same equation at a reference reasoning level with `Λ = 0`. Probes perturb what they measure — `U_t = 1` forces a period of unaided reasoning — and the model says so explicitly rather than noting it in prose.

---

## 6. What is measured

**Primary outcomes are continuous:** long-run unaided capability; assisted outcome; calibration error `|T − E[B|ℐ]|`; load; store validity; outcome volatility; reasoning and writing-back effort.

**The eight-cell state machine is a reading layer only.** Reported as stationary occupancy, dwell times and transition hazards — never as reachable/unreachable. v0.1 made "was this cell ever occupied in 8,000 periods" the primary result, which is a statistic dominated by run length, initial conditions, arbitrary Schmitt thresholds and noise realisations. The precedent it was copying — a state machine whose empty seats are unreachable because *no transition edge leads there* — is a topological fact. Rarely-visited regions of a continuous stochastic space are not the same kind of object, and v0.1 copied the form without the mechanism.

---

## 7. Predictions

**P1 — the displacement signature, stated correctly as a parameter-regime hypothesis.** At the load equilibrium, holding trust fixed:

```
∂logit(H)/∂Λ = h_L·c_0 > 0          loading relieves load, so recording rises
∂logit(R)/∂Λ = r_L·c_0 − r_Λ        reasoning falls only if  r_Λ > r_L·c_0
```

So *better provisioning means recording more and thinking less* holds **only when the direct displacement effect exceeds the indirect load-relief effect.** v0.1 claimed this followed from the sign structure. It does not. `r_Λ > r_L·c_0` is now a stated condition and `r_Λ = 0` is an ablation.

**P2 — writing back is self-limiting.** It costs capacity now (§5.3) and grows the store that displaces reasoning later (`X_m → Λ → R`). Both mechanisms push toward an interior optimum in `H`. In v0.1 only the second existed and the first was missing entirely, which is why the claimed optimum had no mechanism.

**P3 — store-side debt separates from person-side debt.** A run with high mass and low validity is distinguishable on outcomes from a run with low mass. No model in this project or in the literature represents the artefact rotting rather than the person.

**P4 — the archive trap exists above a bifurcation in retrieval, and the condition is exact.** Solving the store subsystem at `W = 0`:

$$
X_m^{*}=1-\frac{\delta_X}{g\,\bar n}
\qquad\text{positive iff}\qquad
\boxed{\;g\,\bar n>\delta_X\;}
$$

**Verified numerically** (δ_X = 0.02, n̄ = 0.5, 40,000 ticks, four initial conditions): predicted `X*` of 0.333 / 0.600 / 0.800 at `g` = 0.06 / 0.10 / 0.20 reproduced exactly, and collapse to zero below the boundary from every starting point.

Below the boundary, maintenance stopping means `X_m → 0`, `Λ → 0`, `O → B` — **the stale store deletes itself and calibration recovers.** Above it, the store persists at `X_m*` **with validity going to zero**, because retrieval carries no validity. That is the archive trap, and it is a transcritical bifurcation rather than a basin boundary: a single sharp parameter condition, not a knife-edge dependent on where you happened to start.

**Whether the archive trap exists at all is therefore the question `g·n̄ > δ_X`, and it is the sharpest single question in the model.**

---

## 8. The regime map is the figure

Sweep maintenance (`c_H`, or `ρ`) against retrieval `g` and locate the boundaries.

**One of the two boundaries is exact and one is not, and the difference should be drawn.** *Forgetting-recovery versus persistence* is `g·n̄ = δ_X` — analytic, threshold-free, verified. *Archive trap versus living store* is a cut on store validity and **is** a chosen threshold; it inherits the arbitrariness the review objected to in the empty-cell gate, one level up. Report the validity **distribution** across the sweep, not only the classification, so the cut is visible as a cut.

Verified at `g = 0.10`: `W = 0` → mass 0.600, validity 0.000 (the store persists and is entirely stale); `W = 0.05` → 0.367 / 0.207; `W = 0.15` → 0.401 / 0.567. The transition is smooth in `W`, which is why the second boundary is a cut and not a bifurcation.

A phase diagram is a structural object: its boundaries survive changes in exact values that shift every quantity on it, it cannot contradict itself cell-by-cell the way a multi-panel magnitude comparison can, and **it can print its own failure** — `NO REGIME BOUNDARY FOUND` means the model produces one behaviour everywhere and there is nothing to show.

---

## 9. Prior expectations to reproduce before any new claim

1. A limit cycle survives with all randomness removed.
2. Longer feedback delay destabilises. *(The `1/τ` boundary quoted in v0.1 is the standard scalar delay-recursion result and has not been derived for this system — see W4.)*
3. **The Bastani pattern:** high `G` should raise assisted outcomes *and* leave unaided capability intact, while high assistance at `G = 0` raises assisted outcomes and lowers unaided capability. This is now a real test, because `G` is a separate channel.

---

## 10. Where to press

| # | weakness |
|---|---|
| **W1** | **Separability of `H` and `R`.** They share three drivers and differ in one each. `\|corr(H,R)\|` bounded away from 1 across the swept space is a gate condition; untested. |
| **W2** | **`g`, retrieval re-encoding, is new and uncalibrated.** P4 depends entirely on `g·n̄ > δ_X` and nothing in the literature measures either side of it. |
| **W2b** | **The living/trap boundary is a validity cut, not a bifurcation.** Only the forgetting boundary is threshold-free. |
| **W3** | **`ρ` is exogenous.** If discipline itself erodes under load, writing-back loses its distinguishing driver and W1 bites. |
| **W4** | The delay-stability boundary is quoted, not derived for this system. |
| **W5** | **Empirical anchors are thin.** Wu et al. is 124 participants, ~56-minute median session, a *perfectly correct simulated* assistant, and a cost manipulation significant only at p < 0.10. It is structurally suggestive; it is not load-bearing and must not be cited as though it were. |
| **W6** | **Chen supports pathway reweighting, not conservation of total updating weight.** The strict simplex is kept for parsimony; a load-dependent overall gain runs as a structural alternative. |
| **W7** | Every anchor is short-horizon lab or classroom work with the assistant as solution-provider on checkable problems. That the mechanism *aggregates* to professional practice over months is the contribution and is untested by anyone. |
| **W8** | One store, not four. Retrieval reinforcement partly recovers the always-loaded/rarely-reviewed distinction, but not the full structure. |

---

## 11. Ablations, replacing "±30% on everything"

Structural, not perturbative: `κ = 0` (baseline) and `κ > 0` · `b = 0` · `δ_v = 0` · `δ_X = 0` · `g = 0` and `g` either side of `δ_X/n̄` · `r_Λ = 0` · no output cap · no delay · `q_W < 1` · load-dependent total updating gain instead of the simplex. Each answers "does the result depend on this mechanism", which "±30%" does not.

---

## 12. Response to the review

**Accepted in full:** `Z` confounded the treatment beyond recovery and is split into `E` and `G`; Bastani's tutor is a reasoning guardrail and was in the wrong channel; writing-back was costly in prose and free in the equations; the state machine classified `H` while the store was fed by `W`; P1 was misstated as structural when it is a parameter regime; **P4 was wrong — mass decays, `Λ → 0`, and the stale-store bias deletes itself**; empty-cell occupancy is the wrong primary result; the `(1−α)(O−P)` identity was circular and `(1−α)(O−B)/(αℓ+1−α)` is the useful one; `T` must be defined as belief about base competence; the calibration target must be principled rather than chosen for effect; `κ = 0` belongs in the baseline; Wu and Chen were both over-weighted; the opening claim overstated the finding and dropped the guardrail counterexample.

**One addition the review's own argument implies — and my first version of it did not work.** "Forgetting recovery" follows from *uniform* mass decay, but real stores do not decay uniformly: the material that persists is the material that keeps being retrieved, and in this project's own source diagram the store marked `ALWAYS` is precisely the one nobody reviews.

I first wrote this as reduced decay, `δ_eff = δ_X0(1 − s·Λ)`. **Solved numerically, it fails.** With `n̄ = 0.5` and `X_m ≤ 1`, `s·Λ ≤ 0.5s`, so decay is only slowed and mass still reaches zero for every `s ≤ 1`; at `s ≥ 2` decay hits zero and the store freezes wherever it started — a continuum of neutral fixed points, not an attractor.

The form that works puts retrieval in the **mass** equation and not the valid-mass equation: `g·Λ(1 − X_m)`. Retrieval re-encodes material without carrying validity with it. That gives an exact transcritical bifurcation at `g·n̄ = δ_X` (§7 P4), verified numerically, and it states the Kreutler distinction as a mechanism: **using a thing keeps it alive; only checking it keeps it true.**

This is not a rescue of P4. P4 is now conditional on a stated inequality, and `g = 0` and `g` either side of `δ_X/n̄` are the first ablations.

**Small divergence.** Keeping `W = e(E)·H` rather than `W = H`: an externalisation affordance genuinely affects whether an intention to record produces usable material, not only how much it costs. The classification point is accepted either way — the bit reads `W`.

**Not yet resolved:** whether `ρ` should stay exogenous (W3); how `g` could be calibrated against anything real (W2); the validity cut (W2b); and **defaults for the ~20 new parameters, which no longer have a calibration target** — v0.1 fitted to reproduce the trust-trap ring, and the ring is not this model's target. Parameters must now be set by argument and precedent, and the three regimes discovered rather than fitted. Where the argument is weak, the ablation list carries the weight.
