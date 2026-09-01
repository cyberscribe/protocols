---
title: "Poison and neutralisation — what the neighbouring literatures already model"
date: 2026-08-28
status: draft
see_also: NOTE-discipline-and-referencing.md, ../../peakepro-diagnostics/cognition-assessment/sim/correspondence/cascade.py
---

# Poison and neutralisation

Four literatures model something with our shape. **Two support our structure and two say we have it
wrong.** Taking the corrections first would be the wrong order — the strongest result is the one that
supports it, and it is stronger than anything we had.

---

## 1. Model collapse: replace versus accumulate — **supports, and adds a proof**

Shumailov et al. (Nature 2024) showed that generative models trained recursively on their own output
degrade. The result that matters for us is the follow-up: Gerstgrasser et al. (2024) prove that the
degradation depends entirely on **whether generated data replaces the original or accumulates
alongside it**:

- **replace** → test error rises with every iteration, unbounded
- **accumulate alongside real data** → test error has a **finite upper bound independent of the
  number of iterations**

Proven in a linear model, demonstrated across language models, diffusion models and VAEs.

**Why this is the best theoretical support the programme has.** Ask what plays the role of "real
data" in our architecture and the answer is **the human**. Externalisation and referencing are the
channel by which non-AI-generated material keeps entering the loop. Take the human out — low
discipline, thin working memory, nothing contributed — and the AI's cycle becomes purely
self-referential, which is the *replace* regime with unbounded degradation. Keep the human
contributing and the system sits in the *accumulate* regime, which is **provably bounded**.

> **The human is not a safety check bolted onto the loop. The human is the term that keeps the error
> bound finite.**

That is a system-level argument for discipline that does not depend on any of our own cognitive
claims, and it arrives from ML theory rather than psychology. Note the caveat: the theorem is about
*training* on generated data, ours is about *context*; the analogy is structural and should be
labelled as such.

## 2. Agent memory poisoning — **supports, with hard numbers on insidiousness**

AgentPoison (NeurIPS 2024) poisons an agent's memory or knowledge base and reports: **under 0.1% of
the store poisoned, over 80% attack success, under 1% degradation on benign tasks.**

That last figure is the whole point and it is our `cascade.py` result stated by another field: **the
system looks almost entirely healthy while being reliably steerable.** A tiny contaminated fraction,
no visible performance signal. Our finding that vigilance keyed to recent yield never triggers at low
poison rates is the behavioural half of the same phenomenon.

The 2026 literature on runtime memory poisoning in persistent agent systems is now active, which is
worth knowing for positioning: **the security field is arriving at our store from the adversarial
side while we arrive from the accidental side.** Same object, different threat model.

---

## 3. Continued influence — **our ratchet is too pessimistic**

Our model treats poison in the durable store as irreversible: it only ever goes up. The nearest human
analogue is the continued influence effect — misinformation keeps affecting judgement after it is
retracted.

Walter & Tukachinsky's meta-analysis (32 studies, 21 reports, **n = 6,527**) puts the residual at
**r = −.05, weak but significant**, and concludes that correction "does not entirely revert people's
attitudes and beliefs to their baseline" — while explicitly saying the effect is **"far from being
the robust and irreversible phenomenon it is often believed to be."**

**So neutralisation mostly works.** Our model allows none at all, which overstates the trap. The
correct form is a **partial** clearance: poison decays when corrected, but not to zero. Correction is
more effective when delivered immediately, from the same source, and with a coherent replacement
explanation rather than bare negation — all three of which map onto promotion-time review rather than
after-the-fact discovery, and are a reason to prefer catching at the gate.

**Model change owed:** add a clearance term to poison, and a residual floor. Without it the ratchet
result is an artefact of assuming no clearance.

## 4. Correlated inspectors — **our two gates are too generous**

We combine human and AI discernment as `1 − (1−h)(1−a)`, which assumes the two reviewers fail
independently. The inspection-reliability literature says repeated or redundant inspections are
routinely **not** independent — prior results bias later ones, and common-cause failure is the
standard reason redundant systems underperform their paper reliability (a long-standing result in
safety engineering; see also Reason's Swiss-cheese framing, where the holes in successive layers are
correlated rather than randomly placed).

For us the correlation is not incidental, it is **structural**: the human reads the AI's output and
the AI produced it, so both are conditioned on the same context. A plausible-but-wrong item is
plausible to *both*. This is the same object as our own `corroboration` mechanic in `cascade.py`,
where agreeing copies lower your guard — we already modelled it in one place and then assumed it away
in another.

**Model change owed:** `catch = 1 − (1−h)(1−a)^(1−ρ)` or an explicit shared-failure term, with ρ the
correlation. At ρ = 1 the two gates collapse into one and the second reviewer buys nothing. **Our
"two reviewers beat one better one" claim survives only for ρ well below 1, and we should say what
value it needs.**

---

## What to do

| # | change | effect on our results |
|---|---|---|
| 1 | Add partial poison clearance with a residual floor | Weakens the ratchet; the accumulation result must be re-derived |
| 2 | Add gate correlation ρ | Lowers catch rates; may overturn "two gates beat one" |
| 3 | Cite Gerstgrasser for the bounded/unbounded distinction | Strengthens the system-level case for discipline considerably |
| 4 | Cite AgentPoison for the <0.1% / >80% / <1% figures | Replaces our invented numbers on insidiousness with measured ones |

Changes 1 and 2 both make the model *less* favourable to us. Do them first.
