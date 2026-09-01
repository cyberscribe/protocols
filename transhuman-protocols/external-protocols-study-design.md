---
title: "Study 1 — design review"
see_also: external-protocols-model.md, external-protocols-review.md
date: 2026-08-28
status: draft
---

# Study 1 — design review

Response to the proposed simulation. Verdict: **randomising the arrows rather than the protocol is the decision that makes this a real study**, and the two-time trust measurement with engineered disagreement is the right answer to identifiability. Four things need fixing before it will survive review, and one cheap addition would make it the first study to touch store-side debt.

---

## 1. What is right, and why it matters more than it looks

**Randomising Λ and Π, holding the rest constant.** A five-stage-bundle-vs-control study can only ever produce "the method works" — unfalsifiable in any useful way, and commercially the *weaker* claim, because it makes DRIVE a package rather than a mechanism. Manipulating the two arrows tests the identity `T^\*-P = w_o(O-P)`, not the brand. A null on the bundle would then have killed everything; a null on one arrow now just relocates the claim.

**Trust twice, with engineered process/outcome disagreement.** Correct, and it is the part I would have flagged as missing. `T` after `P` and before `O` reads `w_p` uncontaminated; the delayed reading gives the `w_o` update. Without disagreement cases `P` and `O` are collinear and neither weight is recoverable. This is the design's load-bearing element.

**The judgment-bearing promoted object.** This is a construct definition, not a measurement detail — it says what promotion *is*, and separates it from note-taking. It also maps onto the model more cleanly than you may have intended:

| promoted element | where it sits |
|---|---|
| done-criteria, assumptions | `Request`-side, generated *ex ante* — the one channel immune to the `K` gating, since you need no expertise to notice you never stated a criterion |
| decision rationale, verification evidence, failure conditions | `P` itself |
| **revision triggers** | **the demotion mechanism** |

That last row is worth pausing on: a revision trigger is a validity condition attached to a stored object. You have just solved store-validity (§6.5 of the model note) operationally, without needing it on the diagram.

**Equivalence bound rather than a nonsignificant `p`.** Right, and rarer than it should be.

---

## 2. The four fixes

### 2.1 The 2×2 confounds promotion with time-on-task — and the fix improves the claim

If promotion costs ten minutes a session and its absence costs zero, every effect on delayed `K` is attributable to "did more stuff." This is the first reviewer objection and it is fatal unaddressed.

Don't yoke it with filler. Make it a **third level**:

> **promotion: none / summary / judgment-bearing**

Time-matched, same material, only the *content* differs. Without the summary arm you have shown promotion beats nothing; with it you have shown *which kind*, which is the part that can be taught, and the part that justifies the six-element rubric.

### 2.2 The primary outcome is four different things, and they are not interchangeable

"Transfer, plausible-error detection, decision reconstruction, or model-unavailable performance" have different psychometrics and different positions in the causal chain. Preregister one, or falsifier 3's equivalence bound has no referent (equivalence on *which* measure?).

| measure | what it actually is | role |
|---|---|---|
| model-unavailable performance on transfer items | `K^{obs,u}` directly — the Bastani/Liu quantity | **primary** |
| plausible-error detection | whether process evidence is legible — this is `w_p`'s gate, not `K` | **mediator** |
| decision reconstruction | the promotion arm wrote down rationale, so of course it can reconstruct rationale — near-tautological | **manipulation check** |

That ordering makes the mediation testable as the model states it: promotion → preserved `K` → error detection → higher `w_p` → smaller `w_o(O-P)`. The whole chain, measured, in one study.

### 2.3 Falsifier 2 needs a paired assessment the design doesn't yet have — and it solves your power problem

"If promotion helps only while AI remains available, it produced better loading" requires **both** delayed measures in every arm. Currently only the unavailable one is specified, so you can detect "promotion helped unaided" but cannot recover the ratio, which is the interesting quantity.

Add a paired delayed assessment — an unaided block and an aided block, different items — and make the DV:

$$
\Delta = (\text{aided score}) - (\text{unaided score})
$$

Three things fall out at once:

1. Falsifier 2 becomes a number rather than a judgement call.
2. The model's real prediction is a **crossover**: loading helps aided performance and hurts unaided capability (via `∂g/∂Λ < 0`). That is far more falsifiable, and far more striking, than an equivalence test.
3. **The crossover is an interaction, and interactions cost roughly four times the sample.** Using `Δ` as the DV converts it into a main effect and recovers the power. This is the difference between a feasible study and an underpowered one.

Order matters: **unaided block always first.** Counterbalancing does not fix Liu's ten-minute contamination, it averages it in. Accept the order confound in the aided block, which is the block you care less about, and say so.

### 2.4 Task-level τ buys realism at the cost of the τ estimate

Randomising feedback timing per task is good for power and honest about the professional setting — outcomes genuinely do arrive interleaved. But two consequences:

- Participants learn the environment is mixed and reweight outcome evidence globally, which biases the τ effect toward null.
- **A mixed-τ stream does not have a τ.** You cannot estimate the stability boundary in `(η w_o, τ)` from it — and I argued that boundary is the figure.

Fix: **block it.** τ constant within a block of sessions, varying across blocks, order counterbalanced. Keeps within-person power, gives you a τ per block, and stops the mixing being total.

---

## 3. Three smaller things

**Load is in the model and not in the design.** `w_p` depends on `L_t`, but load is never manipulated here — Λ is a *partial* load manipulation confounded with the evidence path, which is precisely the point of separating them. So you can estimate `w_p` and `w_o` at whatever load obtains, but cannot test `∂w_p/∂L < 0`. For study 1 that is the right trade: cite Chen for the load term and test only the externalisation terms. But say it explicitly, because it will be asked.

**Collect `H_t` and object quality even though promotion is assigned.** Rating each promoted artefact against the six-element rubric gives you a manipulation check, a dose-response analysis within the promotion arm (more persuasive than the arm contrast alone), and — if promotion quality decays across sessions as trust rises — **a direct observation of `∂h/∂T < 0`**, the feedback that closes the loop, obtained free inside a causal study. Cheap; high payoff.

**Name what holding Request constant does to the claim.** Every arm states criteria and assumptions up front, and those are two of the six promoted elements. So the promotion-none arms *generate* judgment-bearing content and simply don't carry it forward. That is the cleanest possible operationalisation — same evidence produced, different persistence — but it means the contrast is specifically about **cross-session persistence**, not about generating judgment-bearing content at all. Narrower claim, much more defensible.

---

## 4. The cheap addition: test store-side debt

Nothing in the literature has touched the failure mode where debt accumulates **in the store rather than the person**. This design can test it for the cost of one item.

> Partway through the sequence, inject a stale or wrong element into the loaded context. Measure detection.

Promotion-arm participants have revision triggers attached to their own objects. Loading-arm participants have an `ALWAYS`-loaded standard with nothing attached to it. The detection-rate contrast is a direct measure of store-debt vulnerability, it turns the diagram's missing demotion arrow into an empirical result, and it is the finding most likely to be genuinely novel rather than a better-powered version of something already known.

---

## 5. Two things to decide before writing the protocol

**Scale.** At Bastani-like effects (`d ≈ 0.2–0.3`), a 2 × 3 design needs roughly 175 per cell for pairwise contrasts — ~1,000 participants. That is Bastani-scale, and it is only feasible because §2.3's `Δ` keeps the key test a main effect. Alternative: a sequential design with a preregistered stopping rule, which is cheaper and more honest than an underpowered fixed-`n`.

**Lab or field.** The falsifiers as written need standardised tasks, which means a lab study — and the §1 critique of the draft was that *the entire literature is students on toy problems*. Study 1 replicating that shape is fine and fast, but the differentiated study is standardised assessment items embedded in a multi-session engagement with real professional work between them. That is exactly the study the consulting engagement makes possible, and it is the strongest structural argument for running research and venture as one activity.

---

## 6. Naming

The proposal says "Define, Request, Iterate, and Validate." DRIVE is **Decide · Request · Iterate · Validate · Evolve**. If the five-step expansion is the defensible mark rather than the bare word, the stage names cannot drift in the protocol document — that is the artefact everything else will cite.
