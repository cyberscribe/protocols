---
title: "Why the posture machine works and the four-up doesn't"
see_also: external-protocols-model.md
date: 2026-08-28
status: draft
---

# Why the posture machine works and the four-up doesn't

Written before specifying any new figure, because the difference is a rule and not a matter of taste.

---

## 1. The diagnosis

**The posture machine carries a structure. The four-up carries a quantity.** Everything else follows.

| | posture machine | four-up |
|---|---|---|
| what the eye reads | which states exist, which are empty, how long each is dwelt | six continuous terms and a composite score, across four cells |
| robust to | every functional form and parameter value that preserves the topology | nothing — the numbers *are* the claim |
| the finding | **two empty chairs** — `010` "Verify, don't trust", `101` "Precautionary reclamation" | "tooling gives you your standards back, not your week", read off comparative magnitudes |
| can it show its own failure | yes — `PARKED`, `NOT A CYCLE`, undefined bits, printed in the middle of the ring | no |
| relation to the house rule *"no simulator number is evidence about the world"* | obeys it by construction: it shows no numbers | violates it in spirit: the headline **is** a number |

### Four specific things that sink the four-up

1. **Its headline is computed from a formula the project has not settled.** `theory-canonical.md` says effectiveness is a product; `theory-under-simulation.md` calls that an open inconsistency and says sum; `00-CURRENT.md` sides with sum on numerical grounds (the product has a pole at `debt → 0`); the DRIVE engine still computes the product. **The number on the flagship figure is a live argument, not a result.**
2. **Four of its six chips barely move.** Correctness saturates at 1.000 and spans 0.040 in total; fit sits at ≥0.99 in the default cell; `theory-canonical.md` says outright that "the engine's discrimination is entirely denominator-side." The figure gives equal visual weight to terms that carry no signal, and bands them in red/amber/green as if they did.
3. **The score is gameable by 3.7× by an agent who simply feels less indebted** — noted in the engine's own comments. A headline that moves that much on felt rather than true debt cannot be the thing a room is asked to read.
4. **Its retired predecessor failed the same way and the failure was diagnosed at the time**: `drive-exhibit.html` was retired, not replaced, because it "showed the opposite of its own thesis on two tiles." A multi-cell magnitude comparison can contradict itself cell by cell, and the more cells the likelier it does.

Under all four sits one structural fact: **the four-up needs seed 1163 of 200, running means from batch 60, a clock starting at frame 55, and shared never-shrinking scales in order to stay still.** That machinery is honest — it is exactly what `VIEW-DECISIONS.md` demands — but the volume of it is the tell. A picture that needs that much stabilisation is carrying a quantity the model cannot hold steady.

### And the thing the posture machine did that nothing else has

The payload is **an absence**. Two chairs, drawn, permanently outside the ring, with the edges that would reach them dashed in — and nothing ever arrives. A viewer sees a hole. Holes are memorable in a way that a bar three-fifths full is not, and an absence cannot be argued down by an audience that distrusts the numbers, because there are no numbers to distrust.

Then `v-habitability.mjs` supplies the second act: at one investment rate, `V` becomes **narrowly** habitable — 5.01% occupancy, 82 episodes, ring intact. Structure, before and after. No score.

---

## 2. The rule this yields

> **Show what the model makes impossible, not what it makes large.**

Corollaries, in the order they bind:

1. **If a figure's payload survives a 30% change in every parameter, build it. If not, it is an instrument, not an exhibit.**
2. **No composite score on an exhibit until the effectiveness form is settled.** Product-vs-sum has been open since at least 2026-08-21 and it has already cost one flagship figure.
3. **A term that does not vary does not get a tile.** Measure the observed range first; anything spanning less than its own band width is a constant and should be stated in the provenance line, not drawn.
4. **The figure must be able to print its own failure**, in the same place it prints its success.
5. **Empty seats must be found, not chosen.** This is the one that will be tempting to break: if the new figure is designed around a cell predicted to be empty and the cell turns out occupied, *that* is the result. Picking bits until a hole appears is staging, and `theory-canonical.md` §7 already forbids it — "simplify freely, alter never."

---

## 3. What the v3 model offers a structural figure

The central result `T^\* - P = (1-\alpha)(O-P)` is a magnitude. It belongs in the paper, not on the exhibit.

The structural content is elsewhere, and there is a lot of it:

**(a) The bipartite arrow map.** `Λ` reaches `{L, O, R}`; `Π` reaches `{P, C, K}`. Which channels each arrow touches is topology — true under every functional form. This is the "preservation is promotion, not loading" claim in a form that cannot be argued down by disputing a coefficient.

**(b) A three-bit state space with the same shape as the posture machine's.** Candidate bits, thresholded through the existing Schmitt quantiser:

| bit | quantity | reading |
|---|---|---|
| **π** | `H_t` — promotion effort | promoting / not |
| **ρ** | `R_t` — independent reasoning (solo share) | reasoning / displaced |
| **α** | `\|T_t - P_t\|` | calibrated / miscalibrated |

Eight cells. The model's prediction is that **(not promoting, displaced, calibrated) is unreachable** — you cannot stay calibrated while both displaced and not promoting. If that cell is empty, it is the same species of finding as the two chairs, and it says the thing the whole programme exists to say.

**(c) The trap has a visible signature in this space.** Loading moves you along `ρ` while `π` still looks fine — because loading *frees capacity* and so raises promotion effort even as it displaces reasoning (§3.1a, cost 2). So the figure would show a worker sliding along one axis while the axis a manager would watch stays green. That is the sentence — *the harm is detected by the very faculty it erodes* — as a trajectory rather than an epigram.

**(d) The habitability test already exists as code.** `v-habitability.mjs` is exactly the second act: does promotion make the empty cell habitable, and does the cycle survive. The idiom, the quantiser, the conformance harness, the deadband calibration, the ring layout, the palette, the standalone build — all of it is already written and digest-pinned.

**This is why the build is small and the specification is the whole job.**

---

## 4. What is missing before Claude Code can be handed anything

Ranked by what blocks what.

| # | gap | severity |
|---|---|---|
| 1 | **Which engine v3 is.** `trust-trap/model.mjs` is canonical and digest-pinned; v3 adds `R`, `K`, `C`, `Λ`, `Π` and replaces the trust update with a simplex. That is a fork or a seventh engine, not a patch — and six already exist behind a currency boundary. **Nothing can be built until this is decided, and adding a seventh without retiring one is how this fails.** | blocking |
| 2 | **Functional forms.** The v3 model is sign conditions only: `r(·), g(·), p(·), o(·), ℓ(·), λ(·), m(·)`. Sign conditions cannot be simulated. Precedent is strong and consistent across the tree (linear stocks with a restoring force; noisy-OR for evidence weight; bilinear for output; sigmoids only in DRIVE), so this is hours of choosing-with-precedent, not research — but it is not done. | blocking |
| 3 | **Parameter defaults for the new states.** `γ, δ_K, δ_C, θ_{0,T,L,ρ,Z}, β_{0,L,K}, η, τ`. `trust-trap` gives real anchors (τ=28, η=0.18, g=3.00, ρ_D=0.02) but its state space is not v3's, so they do not transfer unexamined. | blocking |
| 4 | **The effectiveness form.** Product vs sum, open since August. Irrelevant if the figure is topological; fatal if it is not. Settling it also retroactively repairs the four-up. | conditional |
| 5 | **Threshold definitions for the three bits.** The quantiser is written but "calibrated on medians of the run" needs a decision per bit: self or frozen. `posture-machine/MODEL.md` records that one mechanism ranking **reverses sign** between the two. | blocking for the figure |
| 6 | **Register.** Exhibit (plays itself, no controls, back of a room), instrument (sliders reach the failures, exports), or figure (reads as a figure, assumptions behind a gear). The briefs treat these as three different artefacts with different rules. | needed for spec |
| 7 | **"Game theory."** There is none in the tree. `game-mechanics.md` is a race — parallel single-agent decision problems on a leaderboard, no second player, no equilibrium concept. The optimisation search was explicitly closed on 2026-08-25: *"a fixed-policy optimum is a fixed-point question, and the subject matter is a limit cycle."* But `theory-under-simulation.md` §6 names the real formal parent — **costly state verification (Townsend 1979)**, with the novelty that *choosing not to verify degrades your ability to verify*. That is a genuine formal contribution and nobody has written it. It is also a different piece of work from the visualisation. | fork — needs a decision |

---

## 5. The order I would do it in

1. Settle #1 (which engine) and #7 (what "game" means) — both are decisions, not work.
2. Write functional forms and defaults into the model note as a `## Implementation` section, with every choice carrying its precedent from the existing tree.
3. Build headless first. Run the three-bit occupancy and the habitability test **before drawing anything.** If no cell is empty, the figure is a different figure — and finding that out costs a day, not a deliverable.
4. Only then specify the view, and specify it against `VIEW-DECISIONS.md` clause by clause.
