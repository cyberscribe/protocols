---
title: "Recommendation — C1, C2, the f conflict, and q_W"
date: 2026-08-28
context: phase 1 complete, gate not passed (C1, C2 fail)
---

# Recommendation after phase 1

Four decisions. Two are corrections to my spec rather than to the model, and I want that said plainly, because "the model failed the gate" and "the gate was wrong" are different situations and only one of them is a goalpost move.

---

## 1. C2 — the fix, and why my earlier advice was half wrong

**The diagnosis is exactly right and my §3.2 recommendation was half wrong.** I said `H` and `R` need non-shared drivers and nominated `ρ`. Non-shared is necessary and not sufficient: **a driver that does not move cannot decorrelate two time series.** `ρ`, `E` and `G` shift intercepts. Correlation is about covariation. I gave a levels answer to a covariance question.

So the requirement is sharper than I wrote it: **non-shared *and* time-varying.**

**Recommended fix — one term, and it is theoretically required anyway:**

```
H_t = logistic( h0 − h_T·T_t − h_L·L_t + h_ρ·ρ + h_E·E + h_X·(1 − X̂_v,t) )
X̂_v,t = X_v,t · K_t + X_v-prior · (1 − K_t)        perceived validity, gated on capability
```

**Write-back should respond to how stale the store looks.** Four things follow, and only the first is about the gate:

1. It is time-varying and structurally non-shared — reasoning has no reason to track store validity; write-back has every reason. C2's mechanism is addressed rather than masked.
2. **It closes the protocol step the theory says is missing.** `encode → retrieve → verify → revise or retire`. Write-back is currently blind to store state, which is the definition of accumulation rather than judgment-bearing externalisation. This term *is* verify-and-revise.
3. **It creates a feedback loop with a lag** — validity falls, write-back rises, validity recovers, write-back falls. That is a candidate oscillator, so it is also the first thing to try for C1. Test C1 *after* it, not instead of it.
4. **It gives the archive trap a mechanism instead of a parameter.** Today the trap is `g·n̄ > δ_X`, a property of the tooling. With perceived validity gated on `K`, the trap becomes: *you stop maintaining the store because you can no longer see that it has gone wrong.* That is the thesis, and it currently isn't in the model.

**Preferred over endogenous `ρ`**, which is the other live candidate and also correct — but `ρ` buys numerical decorrelation and one loop, where this buys those plus a missing protocol step plus a mechanism for the headline failure mode. Keep endogenous `ρ` as the fallback if C1 still fails after this.

⚠️ **New collinearity risk to test, not assume.** `H` would depend on `X_v` while `R` depends on `Λ = X_m·n`. Mass and validity are distinct but store-driven, so they could re-correlate `H` and `R` through the store. They anti-correlate in the archive trap (high mass, low validity), so the interesting region should separate — but **C2 must be re-run across the `r_Λ = 0` slice specifically**, since that is where the collapse lives.

---

## 2. C1 — retire it as a stop-gate. This is my spec error.

**C1 should not have been a stop-and-report check, and the reason is the same error I flagged in the empty-cell gate one round earlier.**

I wrote "a successor that cannot reproduce the cycle is not a successor." That is true of a successor to the trust-trap model. **This is not that model.** It shares a reading layer and a lineage; it does not share a state vector, a subject, or a claim. Its claims are regimes, thresholds and a bifurcation — not an oscillation. Requiring it to cycle imported a criterion from a neighbouring artefact without checking that the mechanism transfers, which is precisely the mistake I diagnosed in the four-up post-mortem and then repeated.

The eigenvalue result supports this rather than excusing it: **+0.9936 real and over-damped is a slow drift, and slow drift is the honest description of the phenomenon.** Knowledge-work capability does not oscillate over months; it seeps.

**Recommendation:**
- **Demote C1 from stop-gate to reported property.** Not deleted — reported, with the Neimark–Sacker location (gain ≈ 23 against trust-trap's 3.00) as a **substantive finding about the difference between the two systems**, not a caveat. An eightfold gain deficit is a real, quotable structural fact: the externalisation loop is far more damped than the trust loop.
- **C5 stays a stop-gate.** That is the harder test and the one that matches this model's actual claims. The bar is not being lowered; it is being pointed at the right thing.
- Re-check C1's status after the §1 fix, since the store-validity feedback may supply gain by a route that is defensible rather than a near-step decision rule.

**Guard against self-serving revision:** this is legitimate only because C5 is retained and is harder. If C5 also failed, the correct response would be to stop, not to reinterpret.

---

## 3. The `f` conflict — the fix is a rule, not a value

`SPEC` §5 pins `f = 0.10` (inherited from trust-trap `stockFormationRate`); §6 result A quotes numbers computed at `f = 0.06`. Mine, and the resolution is not to pick a winner.

**`f` should never have been in the inherited list.** trust-trap's formation rate operates on a *different stock*: no mass/validity split, no retrieval re-encoding term, no retirement term. Importing a numeric value into a structurally different equation is the same category error as importing C1 — assuming that because a symbol has the same name, the quantity is the same quantity.

**Recommendation:**
- Move `f` from **inherited** to **shared nuisance**. Set it so the store occupies a working range without pinning against the mass ceiling, document the reason in one line, and hold it identical across arms — where, per §1 of the spec, it cancels.
- **Audit the other six inherited parameters against the same test:** *is the equation this value came from the equation it is going into?* `τ`, `η` and `cap` probably transfer (same role, same structure). `δ_X`, `λ_L` and `η_h` need checking. I would expect at least one more not to transfer.
- Record the rule in the spec: **a parameter is inheritable only if its equation is unchanged.**

---

## 4. `q_W` — stop looking for an anchor. It is the treatment.

**There is no empirical anchor for `q_W` and there should not be, because it is not a fact about the world.** It is a fact about the practice: writing "we decided X" has low `q_W`; writing "we decided X because A and B, and would revisit if C" has high `q_W`. **`q_W` is the operational definition of "judgment-bearing."** It is the thing DRIVE teaches.

And the phase-1 numbers say so. `q_W`'s mean effect climbs monotonically with affordance — 0.8%, 3.8%, 13.9%, 19.3%, **22.3%** — and at `q_W = 0.25` the affordance effect **vanishes outright**, `H* = 0` at both ends, gain 0.0%.

**That is not a nuisance parameter behaving badly. That is an interaction, and it is the most valuable result phase 1 produced:**

> **Tooling and practice are complements, not substitutes. Neither works alone.**
> Affordance without judgment-bearing content buys nothing — the gain goes to zero.
> Judgment-bearing content without affordance never gets written — `H* ≈ 0`.

Derived, not asserted. And it is the consulting proposition: nobody sells "buy the tool" or "learn the practice" honestly, because the model says either alone is worth approximately zero.

**Recommendation:**
- **Promote `q_W` from swept nuisance to a third treatment axis**, alongside `E` (affordance / tooling) and `G` (guardrail / pedagogy). Three treatments: what you can afford to write, what you are prompted to think, and **how good what you write is**.
- Report `E`-gain **decomposed across the three**, and report the interaction as the headline rather than the main effects.
- **The "cliff, not an elasticity" finding is the deliverable.** A threshold in `q_W` below which externalisation stops paying is "judgment-bearing or don't bother" with a number on it. Locate the cliff precisely — bisect it as was done for the ladder — and report where it sits.
- Sensitivity to `q_W` is then not a weakness to caveat. It is the measured value of doing it properly.

---

## 5. What this is all for — the lay frame

The load–debt conundrum, as a non-specialist experiences it:

> Checking your work costs you time and stress now. Not checking it costs you skill later. Every piece of advice about working with AI is really just telling you which end of that seesaw to sit on.

**The point of this model is that externalisation is the only move that is not on the seesaw.** Loading trades load for debt. Reasoning trades debt for load. Writing judgment back costs a *third* resource — time — and buys a store that reduces both load and debt on every future item. It leaves the plane.

Both of the model's live findings are conditions on that escape, and both are now quantities:

1. **It has to be cheap enough that you actually do it.** Without an affordance the optimal policy is to never write back — not laziness, arithmetic. (The affordance threshold.)
2. **What you wrote has to still be true.** Retrieval keeps material present without keeping it true, so an unmaintained store puts you back on the seesaw *and misleads you about where you are standing.* (`g·n̄ > δ_X`, and the perceived-validity gate from §1.)

And `q_W` supplies the third: **it has to have been worth writing.**

Three sentences for a room:

> Checking and not checking are a seesaw — one costs you now, the other costs you later, and most advice just picks an end.
> Writing down your judgment — not notes, *judgment*: what you decided, why, and what would change your mind — is the one move that isn't on the seesaw, because it pays on every future task instead of this one.
> It only works if it's cheap enough to actually do and what you wrote is still true. Most people fail the first. Most organisations fail the second.

---

## 6. One process note

Six headline claims, one stood, four overstated, one refuted, **no arithmetic wrong** — the errors were all in what was drawn from correct numbers. That is the same distribution as my own five errors earlier in this thread, and the countermeasure that caught them both times was an adversarial pass *after* the numbers were in.

**Make the adversarial review a standing step in the spec rather than a thing that happened once.** The §12 taxonomy of six error kinds is more reusable than any individual correction and should be lifted into the spec as a checklist run against every results section.
