---
title: "Build spec — the externalisation sim (v0.3)"
build_target: peakepro-diagnostics/cognition-assessment/sim/externalisation/
theory: SIM-writeup-for-review.md (v0.2) + analysis/
supersedes: the v0.2 spec, which was ON HOLD pending this rewrite
date: 2026-08-28
---

# Build spec — the externalisation sim

Two phases with a gate between them: **headless across a skill ladder first, visualisation only after.**

**Standing rule inherited from the tree:** no number from this simulator is evidence about the world. It is a theory-refinement instrument. `theory-canonical.md` §7 applies throughout — *simplify freely, alter never.*

---

## 1. The objective, which is also the calibrator

$$
E=\frac{1}{\text{time}}\sum_i \frac{\text{fit}_i \times \text{correctness}_i}{\text{load}_i+\text{debt}_i}
$$

**There is no calibration target to fit, because the equation supplies its own.** Four parts, four jobs, and all four must be honoured or the model corners:

| part | job | what happens without it |
|---|---|---|
| `/time` | the regulariser — effort per item trades against items per period | scored per tick, the optimum corners on **maximum** effort |
| `Σ_i` | the cost terms are **per item** — debt accrues per item passed through at low attention, as in `core/loop.mjs` | a per-tick stock inside a per-item sum makes rushing free; corners on **minimum** effort |
| product over sum | says which terms are bounded: **multiply shares** (fit, correctness ∈ [0,1] — "how right") and **add accumulations** (load, debt — "how much you are carrying") | a clamped cost saturates and the bad behaviour becomes free. **Clamp the numerator, never the denominator** |
| the coefficients | **nuisance, not targets.** `E` is a rate over a dimensionless numerator, so across arms sharing every nuisance parameter they cancel in the comparison | parameters get fitted to a desired outcome, which assumes the conclusion |

Cost terms enter through the house affine map, `1 + 4x` (`MEASUREMENTS.md`), so the denominator is bounded below and never explodes — but is **never bounded above**.

**Method: hold constant and compare rates. Do not calibrate.** Time is the only non-arbitrary unit; everything else is measured against it. Derivation and the untuned result are in `analysis/effectiveness-as-calibrator.py`.

⚠️ **"Show effectiveness increasing through externalisation" is a hypothesis, not an objective.** Fitting to it proves nothing. The legitimate question is *where* it increases and where it does not.

---

## 2. Location and reuse

- **Build at** `sim/externalisation/`.
- **Archive in the same commit:** `core/model-v2.mjs`, `core/model-v4.mjs`, `core/mvm2.mjs`. Keeps the engine count flat behind the currency boundary.
- **Do not modify** `trust-trap/model.mjs` — digest-pinned, 39 conformance checks depend on it.
- **One line in `00-CURRENT.md`** placing this engine current and the three archived behind.

**Reused — read the files and match their interfaces, do not reimplement:** `posture-machine/quantise.mjs` · `posture-machine/machine.mjs` · `posture-machine/palette.js` · `posture-machine/conformance.mjs` (harness pattern) · `make-standalone.mjs` · `VIEW-DECISIONS.md` clause by clause.

**Not reused:** trust-trap's state vector. Its `S` is not our `R`; its `D` is not `1 − K`.

---

## 3. Notation

**Single letters for states, whole words for functions.** `π` is a constant, therefore reserved, therefore never a variable — the same class as `e` or `i`; `Π` is the product operator. `σ(·)` is out for the sigmoid (standard deviation, and the posture machine's sovereignty bit) — use `logistic()`.

| symbol | meaning |
|---|---|
| `T` | trust — belief about the assistant's **base** competence |
| `K` | capability (latent) |
| `X_m`, `V` | store mass, valid mass; `X_v = V/X_m` |
| `L` | load — **unbounded above** |
| `D` | debt — **unbounded above**, accrues per item |
| `B` | true base reliability — model-known, worker-unknown |
| `Λ` | loading (store → session) |
| `H`, `W` | write-back effort; actual write-back `W = e(E)·H` |
| `R` | independent reasoning (= solo share) |
| `S` | **skill ladder rung** — the primary sweep axis |
| `E`, `G` | externalisation affordance; reasoning guardrail |
| `ρ` | capacity / discipline |
| `α` | pathway allocation |
| `P`, `O`, `U` | process evidence, outcome, probe occasion |

⚠️ **Declare in the engine header:** trust-trap's `H` is *human contribution* and its `R` is *reclaim*; `τ` is our lag but its trust bit and DRIVE's decision temperature; `ρ` is our capacity but the tree's rate prefix.

---

## 4. The model

Discrete time. States clamped **[0,1] only where they are shares**; `L` and `D` are clamped below at 0 and not above.

### 4.1 Exogenous

| symbol | form |
|---|---|
| `B_t` | AR(1), φ 0.80, mean 0.55, uniform shock ±0.10, clamp [0.30, 0.80] |
| `n_t` | relevance, Beta(2,2), mean `n̄ = 0.5` |
| `U_t` | Bernoulli(0.02); **forces `R_t = 1` and `Λ_t = 0`** for that period |

Warm-start: 2,000 burn-in periods before any measurement, so `O_{t−τ}` is always defined.

### 4.2 Time, and items per period

```
t_item = max( t0 + tR·R_t + tH·H_t − tL·Λ_t , t_min )
n_t    = 1 / t_item                                    items completed this period
```

**This is the term that makes attention scarce.** Loading saves time; both behaviours cost it.

### 4.3 The two behaviours

```
H_t = logistic( h0 − h_T·T_t − h_L·L_t + h_ρ·ρ + h_E·E )         no Λ
R_t = logistic( r0 − r_T·T_t − r_L·L_t − r_Λ·Λ_t + r_G·G )        no ρ
```

`Λ` enters reasoning and never write-back; `ρ` enters write-back and never reasoning. Without non-shared drivers the two are collinear and the reading layer is meaningless (gate C2).

*(Phase 1 also runs a **fixed-policy** mode in which `R` and `H` are swept directly rather than generated — that is how the optima in `analysis/effectiveness-as-calibrator.py` were found, and it is the cleaner first result.)*

### 4.4 Load and debt — both unbounded above

```
L_{t+1} = L_t + λ_L·[ c_0·(1 − Λ_t) + c_R·R_t + c_H(E)·H_t − L_t ],   c_H(E) = c_H0·(1 − ε_E·E)
D_{t+1} = D_t + n_t·[ δ·(1 − R_t) − ρ_D·R_t·gate(S,K) ] − κ_D·(D_t − D_base)
```

**Debt accrues per item.** `gate(S, K)` is the gating rule from `sim_aid_channel_findings`: attention pays down debt only to the extent the work can actually be evaluated. This is what makes the skill ladder informative (§6).

### 4.5 The store — encode, retrieve, verify, revise or retire

```
V'    = (1 − δ_X)·V·(1 − δ_v) + f·W_t·q_W
X_m'  = (1 − δ_X)·X_m + f·W_t + g·Λ_t·(1 − X_m) − ret·W_t·(X_m − V)
X_v'  = V'/X_m'          (:= 0 when X_m' < ε)
Λ_t   = X_m · n_t
```

- **`g·Λ(1 − X_m)` appears in the mass equation and nowhere in the valid-mass equation.** Retrieval re-encodes material and carries no validity with it: *using a thing keeps it alive; only checking it keeps it true.*
- **`ret·W·(X_m − V)`** is *retire* — write-back effort also removes material that has gone invalid.
- **`q_W ≤ 1`** — incoming material is not automatically true. `q_W = 1` is an optimistic scenario, not the baseline.

**Analytic result to assert as a unit test.** At `W = 0`:

$$
X_m^{*}=1-\frac{\delta_X}{g\,\bar n}\quad\text{, positive iff } g\,\bar n>\delta_X
$$

Verified to 3dp from four initial conditions (`analysis/store-fixed-points.py`): `X* = 0.333 / 0.600 / 0.800` at `g = 0.06 / 0.10 / 0.20`, `δ_X = 0.02`, `n̄ = 0.5`. Transcritical, not bistable.

### 4.6 Evidence, outcome, trust

```
avail_t = 1 − (1 − G)·(1 − W_t)                          noisy-OR
ℓ_t     = avail_t · K_t                                  legibility gate
P_t     = ℓ_t·B_t + (1 − ℓ_t)·T_t                        illegible evidence echoes the prior
O_t     = min( cap, B_t·(1 + b·Λ_t·(2·X_v − 1)) + η_h·R_t·K_t·S )
α_t     = logistic( a0 − a_L·L_t + a_K·K_t )
T_{t+1} = T_t + η·[ α_t·(P_t − T_t) + (1 − α_t)·(O_{t−τ} − T_t) ]
```

Reduced form, since `P` contains `T`:

$$
T^{*}-B=\frac{(1-\alpha)(O-B)}{\alpha\ell+(1-\alpha)}
$$

**Attribution error is generated by the joint-output/base-AI gap and attenuated by legible process evidence.** Assert this as a unit test against the simulated fixed point.

`T` is belief about **base** competence. Calibration target is `E[B_t | ℐ_t]`, the rational AR(1) forecast — not a trailing window chosen because it made a bit behave.

### 4.7 Capability and measurement

```
K_{t+1} = (1 − δ_K)·K_t + γ·( R_t + κ·H_t )·(1 − K_t)          κ = 0 in the baseline
K^obs_t = K_t + ν_t     only where U_t = 1
D^cf_t  = K*_t − K^obs_t                                        readout for reporting
```

**`κ = 0` is the baseline; `κ > 0` is the explicit "externalisation builds capability" hypothesis and runs as an ablation.** Wu measures `R`, not `H` — the engine comment must say so, or the term will acquire a citation by proximity.

### 4.8 Scoring

```
fit_t  = clamp01( fit0 + b_fit·Λ_t·(2·X_v − 1) )
corr_t = clamp01( B_t + η_h·R_t·K_t·S )
E_t    = [ (fit_t · corr_t) / ((1 + 4·L_t) + (1 + 4·D_t)) ] · n_t
```

Report `E` as the run mean over the measurement window, alongside its parts.

⚠️ **Scoring pathology to watch** (`sim_aid_channel_findings`): under a rate form with cost in the denominator, a worker producing negative value has their loss *magnified* by cost reduction. With `fit, corr ≥ 0` the numerator cannot go negative and this does not bite — **but if signed correctness is ever reintroduced, it does.**

---

## 5. Parameters

**Inherited, not re-tuned** — a successor that cannot reproduce the established cycle is not a successor: `τ = 28`, `η = 0.18`, `δ_X = 0.02`, `f` (formation) `= 0.10`, `λ_L = 0.03`, `cap = 1.00`, `η_h = 0.90`, horizon 10,000 / burn-in 2,000, quantiser deadband 0.30.

**Shared nuisance — identical across every arm, never fitted:** `t0, tR, tH, tL`, `c_0, c_R, c_H0`, `δ, ρ_D, κ_D, D_base`, `a0, a_L, a_K`, `h*`, `r*`, `γ, δ_K`, `fit0, b_fit`. Set from precedent and plausibility, document the reason for each in one line, and **never adjust one to improve a result.**

**Swept — these are the hypotheses:** `S` (the ladder), `E`, `G`, `g`, `δ_v`, `ret`, `q_W`, `b`, `κ`, `r_Λ`.

---

## 6. Phase 1 — headless, across the skill ladder

**The skill ladder is the primary sweep.** `S ∈ {0.15, 0.3, 0.5, 0.7, 1.0}` — rungs chosen to straddle the existing finding that the marginal return on attention goes negative below about a third of full expertise.

For each rung, sweep `E` (affordance) and `g` (retrieval), in both fixed-policy and behavioural modes, and report:

- `E` (the objective) and each of its parts
- `R*`, `H*` — the optimal policy, and **whether `H* = 0`**
- `X_m`, `X_v` at steady state
- regime label: **living store · archive trap · forgetting recovery**
- calibration error `|T − E[B|ℐ]|`, throughput `n`, and long-run `K`

### The two results to look for

**A. The affordance threshold.** Untuned, with `S = 1`: at high write-back cost the optimal policy is `H* = 0` with store validity **0.00** — *the archive trap is the rational policy, not a failure of discipline* — and a good affordance moves `H*` to 0.6 and validity to 0.94, with `E` up ~14%. **Externalisation tooling does not make writing back better; it makes writing back worth doing.**

**B. Does that threshold move with skill?** This is what the ladder is for, and it is genuinely open. A first pass with skill entering correctness and debt-repayment symmetrically gave a **flat ladder** — `H*` barely moved across `S`. So the ladder is only informative if `gate(S, K)` is asymmetric: reasoning is gated on skill (you cannot evaluate what you do not understand) while write-back is much less gated (stating a criterion in advance needs no expertise). **If the ladder is flat under the asymmetric gate too, that is a null result about the gating rule and it gets reported.**

### Ablations — structural, not perturbative

`κ = 0` (baseline) vs `κ > 0` · `b = 0` · `δ_v = 0` · `δ_X = 0` · `g = 0`, and `g` either side of `δ_X/n̄` · `r_Λ = 0` · no output cap · no delay (`τ = 0`) · `q_W < 1` · load-dependent total updating gain instead of the strict simplex · **`L` and `D` clamped at 1** (this should reproduce the cornering and is the regression test for §1).

---

## 7. The gate

Proceed to Phase 2 only when these hold. **C1–C4 failing means stop and report.**

| # | check |
|---|---|
| **C1** | the engine oscillates; a limit cycle survives with all randomness removed |
| **C2** | **`\|corr(H, R)\|` bounded away from 1** across the whole swept space — the collapse test |
| **C3** | the store fixed point matches `X* = 1 − δ_X/(g·n̄)` to 3dp (unit test) |
| **C4** | the trust fixed point matches `T* − B = (1−α)(O−B)/(αℓ + 1−α)` (unit test) |
| **C5** | all three regimes are reachable somewhere in the swept space |
| **C6** | the displacement signature: raising `Λ` raises `H` and lowers `R` **in the same run** — and `r_Λ > r_L·c_0` is reported, since P1 is a parameter regime and not a structural consequence |
| **C7** | store-debt separates from person-debt: high-mass/low-validity distinguishable from low-mass on `E` |
| **C8** | the clamped-cost ablation reproduces the cornering |

**Rails.** Regimes must be *found*, not tuned into existence — if the sweep produces one behaviour everywhere, that is the result. No nuisance parameter is ever adjusted to improve an outcome. Report the fraction of the swept space in which each headline sign holds, on the frame.

---

## 8. Phase 2 — the view, in the standard idioms

**Register: instrument.** Not a figure. Follow `viewer.html` / `viewer-core.js` as the pattern; obey `VIEW-DECISIONS.md` clause by clause: 1280×720 logical scaled up never down, fixed composition with measured height, shared never-shrinking scales, colour carries a verdict and only where there is one, thresholds inside the observed range, rates not stocks, `setTimeout` not `requestAnimationFrame`, standalone rebuilt after every change, one provenance line on the frame.

House palette from `posture-machine/palette.js` as plain strings, not CSS custom properties. Poppins with a real fallback; monospace for every number.

**Panels:**

1. **The regime map** — the headline. `E` (affordance) against `g` (retrieval), one panel per skill rung. The `g·n̄ = δ_X` boundary is analytic and drawn as a line; the living/trap boundary is a **validity cut** and must be drawn as a cut, with the validity distribution shown so the arbitrariness is visible. *(One of the two boundaries is exact and one is not — do not let them look alike.)*
2. **The affordance threshold** — `H*` against write-back cost, one line per skill rung. The jump from `H* = 0` is the finding.
3. **The displacement panel** — `H` and `R` as `Λ` is dragged. C6 rendered.
4. **Store mass against store validity**, with the loaded quantity marked.
5. **The effectiveness decomposition** — `E` and its four parts over time, so the *concealment* is legible: maintenance drops throughput ~28% while `fit` rises. **Maintenance looks like slowdown; the quality it buys is the invisible term.**
6. **The eight-cell reading layer** (`W` / `R` / `C`) as *stationary occupancy, dwell times and transition hazards* — never reachable/unreachable. It is a reading of the continuous system, not the result.

**No composite score presented as a measurement**, and the instrument must print its own failure in the same place it prints its success: `PARKED` · `NOT A CYCLE` · `COLLAPSED` (C2) · `ONE REGIME ONLY`.

---

## 9. Out of scope for v1

**Concurrency** — prior attempts failed carrying concurrency, temperament, tooling and aids at once. **Four separate stores** — one two-dimensional stock; the stores differ by loading discipline and the harm mechanism is validity. **An optimising agent** — behavioural, plus a fixed-policy sweep; the fixed-point search was closed for good reason. **Game theory** — costly state verification with endogenous verification decay (Townsend 1979) is a real unwritten paper and a different one.

---

## 10. Order of work

1. Engine + archive + `00-CURRENT.md` line.
2. Unit tests C3 and C4 first — both have closed forms, so they fail loudly and early.
3. Fixed-policy sweep across the skill ladder. Result A, then result B.
4. Behavioural mode; C1, C2, C6, C7; ablations including C8.
5. **Gate.**
6. Instrument.
