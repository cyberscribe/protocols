---
title: "Design — the adjudicator (outside witness)"
date: 2026-08-28
for: sim/externalisation, model change addressing C2
---

# The adjudicator

The exogenous driver C2 requires, designed as an **adjudicator of output** rather than an inspector of the store.

---

## 1. What it is, and what it deliberately is not

**It is:** a second observer of each finished item, reporting an assessment of `fit × correctness` **on every item**, accurate **within a margin**.

**It is not:** an inspector of the externalised system. It never reads the store, never reports that a standard has gone stale, never decomposes an outcome into "you" versus "your context". It sees output only.

That restriction is not modesty. It is what makes the design test something (§7).

---

## 2. Mechanism, per item

```
true quality        q_i  = fit_i × corr_i                         hidden, and capped in what the worker sees
worker self-reveal  ĝ_w  = K_t · R_t                              gated on capability and attention
adjudicator reveal  ĝ_a  = ĝ_a(σ_A)                               a property of the adjudicator, not the worker
combined reveal     ĝ_i  = 1 − (1 − ĝ_w)(1 − ĝ_a),  ĝ_i ≤ 0.90    noisy-OR, house form, no reveal ever certain
worker's estimate   q̂_i  = ĝ_i·q_i + (1 − ĝ_i)·prior_i
adjudicator verdict a_i  = q_i + ε_i,      ε_i ~ N(0, σ_A²)       every item, i.i.d.
surprise            s_i  = | a_i − q̂_i |
```

`σ_A` is the margin of accuracy. `ĝ_a` is derived from it, not set separately.

**The `0.90` ceiling and the noisy-OR are inherited deliberately** — `game-mechanics.md` §14 fixes the reveal ceiling at 0.90 as `[SPEC]`, "no reveal is ever certain", and adopts wiring D. Reuse both; do not invent a new reveal form.

---

## 3. Where it enters — and why this separates `H` from `R` when nothing else did

```
H_t = logistic( h0 − h_T·T_t − h_L·L_t + h_ρ·ρ + h_E·E + h_S·s̄_t )
R_t = logistic( r0 − r_T·T_t − r_L·L_t − r_Λ·Λ_t + r_G·G )          ← no surprise term
```

**The separation is temporal, not parametric, and that is why it works where three parametric attempts failed.**

- **`R` is chosen *ex ante*** — before the item is done, from the state at decision time.
- **`H` is chosen *ex post*** — after the verdict.
- The verdict arrives **between** them. It is new information by construction.

You can act on a specific verdict by recording it. You cannot retroactively reason harder on a finished item. So `H` gets a direct surprise term and `R` does not, and the asymmetry needs no claim about temperament.

**`R` is not blind to feedback** — it responds through `T`, which surprise already moves. That path is *shared* and stays shared. The direct term is the only non-shared one, and it is the independent variation.

### It survives the exact condition that killed `h_X`

`h_X·(1 − X̂_v)` went constant where the store saturated: `sd(K·(X_m − V)) = 0` exactly. Surprise cannot go constant, because `ε_i` is redrawn every item regardless of what any state is doing. Checked against all three conditions the failures discovered:

| condition | met |
|---|---|
| time-varying | ✓ fresh draw per item |
| does not go constant in the operating region | ✓ `ε` is independent of every state |
| not a function of the shared states | ✓ `q_i` is endogenous, `ε_i` is not, and surprise inherits `ε`'s variance |

---

## 4. How much surprise is needed — set this as a design target, not a discovery

Simulated directly (200k draws, `H` and `R` sharing one driver bundle):

| `h_S·sd(s)` as a multiple of the shared drivers' contribution to `H`'s logit | `\|corr(H,R)\|` |
|---|---|
| 0.10 | 0.994 |
| **0.142** | **0.989** — just clears the 0.99 gate |
| 0.30 | 0.956 |
| 0.48 | 0.897 |
| 1.0 | 0.697 |
| ~3 | ~0.32 — the range exogenous AR(1) `ρ` achieved |

**Clearing the gate is easy; a genuinely separable reading layer is demanding.** To reach the 0.26–0.33 band, surprise must carry roughly **three times** the combined weight of trust and load in `H`.

That is a substantive claim and it should be stated as one rather than discovered as a fitting result:

> **Write-back is driven more by what got challenged than by how you feel.**

Which is DRIVE in another form — Evolve is triggered by what Validate returned, not by mood. If the model cannot be made to satisfy that at defensible parameter values, that is a finding about the method, not a tuning problem.

---

## 5. A scalar verdict, not a diagnosis

The adjudicator returns **a number**, not a reason.

This is forced by a prior result rather than chosen: `sim_aid_channel_findings` records that validation gated on expertise is worthless once expertise has collapsed, because *"a failing check is only informative to someone who knows what it means."* **A score needs no expertise to read; a diagnosis does.** An adjudicator that explains itself would be silently gated on the very capability the model says erodes — and would therefore stop working exactly when it was needed.

It also matches the constraint directly: assess `fit + correctness`, do not inspect the store.

---

## 6. The margin of accuracy generates the sharpest new prediction

`σ_A` has two regimes, and the second one is worth the build on its own:

- **Small `σ_A`** — verdicts are informative; surprise is mostly real signal; write-back records real lessons.
- **Large `σ_A`** — surprise is mostly measurement error; **write-back records responses to phantom problems.**

The second case writes conclusions drawn from noise into the store, which is a fall in `q_W` — **the treatment variable that phase 1 made the headline.** So:

> **`σ_A` and `q_W` are coupled: an inaccurate adjudicator degrades the store it prompts you to write.**
>
> **Bad review is worse than no review, because it fills your store with wrong lessons.**

That is testable in this model, novel as far as the literature goes, and immediately legible to a lay audience. **Sweep `σ_A` and look for a crossover** where a noisy adjudicator scores below no adjudicator at all. If the crossover exists, it is a better headline than the 0/0/40.5 table because it is a *non-monotonicity*, and non-monotonicities survive scepticism that magnitudes do not.

---

## 7. What it cannot see, and the experiment that sets up

Because the adjudicator sees output and never the store, **the worker cannot tell whether a bad verdict means *I rushed* or *my context was wrong*.** They receive a joint outcome and must decompose it unaided.

That is precisely the gap `core/MODEL.md` §9 names as the sharpest untested prediction in the whole tree:

> *"nothing in the five channels helps a worker decompose a joint outcome after the fact… If the model is right that attribution error is the engine, an aid that attacks attribution directly should dominate every other channel. That is the sharpest prediction the model makes and it is currently untested."*

**This design makes that testable with one variant.** Two adjudicators:

- **scalar** — returns `a_i` only (the design above);
- **attributed** — returns `a_i` split into the part traceable to the store and the part traceable to the worker's own effort.

If the attributed adjudicator dominates every other channel, the tree's sharpest untested prediction is confirmed, and it was confirmed by an aid that is buildable in practice — a reviewer who says *"this is wrong because your template is out of date"* rather than *"this is wrong."*

**Note the tension to keep honest:** an attributed verdict is closer to a diagnosis, so §5's gating concern applies to it. That is not a reason to avoid the variant — it is the thing the variant measures. Report both effects.

---

## 8. Parameters and ablations

**New:** `σ_A` (margin), `h_S` (weight of surprise in write-back), `s̄` window length, and an `adjudicator ∈ {none, scalar, attributed}` arm.

**Ablations:**

| ablation | asks |
|---|---|
| `adjudicator = none` | the current model — the C2 baseline |
| `h_S = 0` | is it the *signal* or merely the *variance* that decorrelates? |
| `σ_A → 0` | the perfect-adjudicator ceiling |
| `σ_A` swept | the crossover in §6 |
| `attributed` vs `scalar` | the §7 prediction |
| verdict on a random subset rather than every item | does "every time" matter, or would a cadence do? |

**Retain `h_X` from the previous round.** It failed as a C2 fix and it succeeded as theory — it closes `verify → revise or retire` and it moves workers in and out of the trap at low discipline and high retrieval. It should stay in the model on those grounds, with the record stating plainly that it was kept for what it does and not for the check it did not clear.
