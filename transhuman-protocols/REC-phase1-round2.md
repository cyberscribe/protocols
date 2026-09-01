---
title: "Recommendation — after the second gate run"
date: 2026-08-28
context: C2 and C5 fail as stop-gates; C1 reported. Four decisions implemented, downstream clean.
---

# After the second gate run

Three things happened that read as failures and are not. Taking them in order of what they change.

---

## 1. C2 has proved a theorem about the model, and the missing driver already has a name

The sequence found three conditions, each by failing:

| attempt | result | condition discovered |
|---|---|---|
| `ρ`, `E`, `G` | 81/81 collapse | must be **time-varying** |
| `h_X·(1 − X̂_v)` | 81/81 → 63/81; where the store saturates `sd(K·(X_m−V)) = 0` **exactly** | must **not go constant in the operating region** |
| `ρ = f(load)` | 18/18 collapse | must **not be a function of the shared states** |
| exogenous AR(1) `ρ` | 0/18, \|corr\| 0.26–0.33 | — |

**That is a result, not a blocker: within this model, write-back and reasoning cannot be separated by anything endogenous.** Every internal candidate either does not move, stops moving, or moves with what the two behaviours already share.

And the reluctance to adopt AR(1) `ρ` is correct — *"making `ρ` fluctuate is a claim about people, not about code."* Exactly right, and it is the reason to look harder rather than to accept it.

### The driver this model is missing is already established as necessary elsewhere in the same programme

`sim_oscillator_conditions`, from the oscillator work and predating this problem entirely:

> *"Recovery is fragile: it needs a value signal the worker did not generate. Sweeping the outside-witness share, mean judgment goes 0.65 at full external signal to 0.00 at or below 0.4, and escape from deep debt requires a clean external signal."*

**The externalisation model has no outside witness.** Every driver in it is internal to the worker. C2's sequence has independently rediscovered, from the covariance side, what the oscillator work found from the recovery side.

**Recommendation: the exogenous driver is not a personality parameter, it is the outside witness.**

A review or consequence signal arriving on a cadence the worker does not control — a colleague's question, a client challenge, a code review, an incident, a deadline. It:

- is **exogenous by construction** — you do not schedule your own surprises;
- **varies in time**, and does not go constant when the store saturates;
- is **not a function of `T`, `L`, `X` or `K`** — its *content* may depend on state, but its **arrival** does not, and the arrival is what supplies the independent variation;
- drives **write-back specifically** — you record what just got challenged — without driving in-the-moment reasoning.

All three discovered conditions, satisfied, without a claim about temperament. And it earns its place theoretically rather than numerically, which AR(1) `ρ` does not.

It also improves the venture story: **DRIVE stops being a solo discipline and becomes a practice with other people in it.** The thing that keeps write-back and thinking apart is somebody else asking.

---

## 2. C5's failure is the finding. Do not fix it first.

*"Forgetting recovery is reachable by nobody, even at `ρ = 0`. Behavioural `H` never approaches zero, so the store never decays away."*

**Read that as a result before treating it as a defect.** The v0.2 story offered forgetting as an escape: stop maintaining, the store decays, calibration recovers. C5 says that behaviourally **nobody stops maintaining enough for that to happen.**

> **The archive trap has no natural exit. You do not forget your way out of it.**
>
> You will always do just enough maintenance to keep the store alive, and never enough to keep it true.

That is darker than the three-regime story and far more recognisable: the wiki nobody deletes, the runbook that is 60% wrong, the onboarding doc from 2019. **Nobody deletes it and everybody reads it.**

It also *simplifies* phase 2 rather than blocking it. Two regimes with a threshold between them is a cleaner map than three — and the threshold is the affordance/`q_W` cliff you have already bisected.

### Then, and only then, the hurdle

`logistic(·)` is never zero, so a behavioural worker always writes back a little, and a little is enough to hold the store above the bifurcation. The fix is a **hurdle**: `H = 0` unless expected benefit exceeds a fixed cost, else `logistic(...)`.

**Justified independently of the regime it might unlock** — there is a real fixed cost to writing anything down at all (opening the thing, deciding it is worth it), and a smooth logistic that cannot reach zero is a known weakness of the form. That independence is what keeps this off the rail; **if forgetting-recovery is still unreachable with the hurdle in, that stands as the result.**

And the hurdle gives `E` a second, sharper mechanism: **an affordance does not only reduce the marginal cost of writing back, it lowers the threshold at which write-back happens at all.** Which is exactly why affordance alone buys 0% — with nothing worth writing, lowering the hurdle changes nothing.

**Order: report C5's failure as the finding, then run the hurdle as an ablation.** Not the reverse.

---

## 3. `q_W` — this is the exhibit, and it beats the regime map

```
affordance alone                +0.0%
judgment-bearing content alone  +0.0%
both                           +40.5%
```

Three cells at zero and one at forty. That is a **pure interaction with no main effects**, which is rare, and it satisfies the design rule better than anything else the model has produced: three cells at exactly zero is a structural claim, not a magnitude claim; a 2×2 cannot contradict itself cell by cell the way the four-up did; and a lay audience reads it in one second without being told how to.

**Recommendation: the headline exhibit is this 2×2, not the regime map.** The regime map becomes a supporting panel.

⚠️ **One caution, and it is the checklist doing its job.** The zeros come from `H* = 0` filling a whole column and a whole row — and the adversarial pass has *already* caught once that `H* = 0` was a grid corner with a true optimum near 0.01. **Re-run those cells at the bisected resolution before "zero" goes on a slide.** "Approximately zero" and "exactly zero" are different claims and only one of them survives a hostile reader. If it comes back as 0.4% rather than 0.0%, the finding is unharmed and the wording changes.

---

## 4. Scope C2 to what it protects, and unblock phase 2

C2 exists to protect **panel 6**, the eight-cell reading layer: two bits that are the same bit cannot report anything. It was never protecting the rest of the view.

**Recommendation: C2 gates panel 6, not phase 2.** Build phase 2 without panel 6, and **put the reason on the frame** — *"the eight-cell layer is unavailable: the two behaviours are not separable without an exogenous signal."*

That is not a goalpost move; it is scoping a check to the thing it checks, and it follows the rule that the instrument must be able to print its own failure. The failure gets **published on the figure** instead of blocking the figure.

---

## 5. Where this leaves the lay message

Sharper than before, and now with the second half earned:

> Checking your work and not checking it are a seesaw — one costs you now, the other costs you later, and most advice about AI just picks an end for you.
>
> Writing your judgment down is the one move that is not on the seesaw. But **the tool and the practice are worth nothing apart** — an affordance with nothing worth writing buys zero, and judgment worth writing that never gets written buys zero. Together, forty per cent.
>
> And the store you build will be read long after it stops being true, because **nobody maintains it enough to keep it right and nobody abandons it enough to let it go.**

The third line is new, and it is the one C5 bought.

---

## 6. Two smaller notes

**C1, now reported rather than gating:** an eightfold gain deficit against trust-trap (Neimark–Sacker at ≈23 versus 3.00) is a substantive statement about the difference between the two systems — the externalisation loop is far more damped than the trust loop. Publish it as a finding with that framing, not as a caveat about a check that used to fail.

**The audit predicting its own answers** — `τ`, `η`, `cap` transfer; `f`, `δ_X`, `η_h` fail; `λ_L` transfers as a timescale only — is the best evidence so far that the inheritance rule is real and not bookkeeping. Worth one line in the spec: *four of seven inherited parameters did not survive the test.*
