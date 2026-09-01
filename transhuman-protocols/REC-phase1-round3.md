---
title: "Recommendation — after the adjudicator run"
date: 2026-08-28
context: C2 cleared; crossover found; §7 refuted; C5 still fails and now fails differently
---

# After the adjudicator

The three flags are all mine and all accepted (§5). The important thing is at the bottom of your report and is being under-read.

---

## 1. "The outside witness abolishes the archive trap outright"

**That is the headline of the entire programme, and it changes what the model is about.**

Every previous framing had the trap as a *maintenance* problem — retrieval versus decay (`g·n̄ > δ_X`), the quality of what you write (`q_W`), whether anything gets retired. The adjudicator result says none of that is the binding constraint:

> **The archive trap is not a property of your tooling or your discipline. It is a property of working unwitnessed.**

That subsumes the venture claim rather than competing with it, and it is the first result in this programme that is about **two people** rather than one person and a machine.

### But it must be disambiguated before it is said out loud

**As `σ_A` widens, `H` rises monotonically to 1.00.** So a worker with any adjudicator writes back a lot — and a store that is always maintained cannot rot. That gives two completely different readings of "the trap is abolished", and they carry opposite advice:

| if the abolition holds… | the claim is | the advice |
|---|---|---|
| **only below the crossover** (`σ_A/σ_q < 0.30`) | *good review* abolishes the trap | invest in accurate review; a noisy reviewer is worse than none |
| **at every `σ_A`, including the harmful ones** | ***being observed*** abolishes the trap, independent of whether the observation is any good | accountability maintains the store even when the feedback is useless — and the store stays alive while `q_W` collapses to 0.43 |

**The second reading is darker, more interesting, and more likely to be true**, because the mechanism (`H → 1.00`) is driven by surprise magnitude and a noisy reviewer generates *more* surprise, not less. It would mean: **the watched worker keeps the archive alive and fills it with nonsense.** That is not "the trap is abolished" — it is the trap replaced by a different failure with the same signature.

**This is the next run, and it is one sweep:** re-check regime reachability across `σ_A` on both sides of 0.0210. Do not publish the abolition claim until it is disambiguated. It is exactly the class of over-read the checklist exists to catch — a correct number, a conclusion drawn one step too far.

---

## 2. C5's failure has changed shape, and the regime map should be retired

With no reviewer: two regimes. With a reviewer: one. Forgetting recovery: reachable by nobody, ever.

**So the model no longer supports a regime map** — drawing a one-cell map would be worse than drawing none. **Retire the panel.**

What replaces it is better, because the collapse is itself the structure:

> **The reviewer axis is the map.** Regimes exist on one side of it and vanish on the other.

A picture of *"here are the regimes, and here is the axis along which they cease to exist"* is a stronger structural object than a phase diagram — it shows a variable that removes a distinction rather than one that moves a boundary. And it is legible without any training.

---

## 3. §7 is refuted — and the refutation needs one diagnostic before it is banked

Your read is right: the aid does exactly what it was built for, everywhere, and buys nothing on the objective. And **you are right that `core/MODEL.md` §9 must be amended to say which quantity it was claiming** — attribution error or effectiveness. On attribution error the aid dominates 45/45. On `E` it loses 45/45. Those are not the same prediction and §9 does not distinguish them.

**One diagnostic before banking it, and I would raise it whichever way the result had gone.**

`K` saturates: `K' = (1 − δ_K)K + γR(1 − K)`. It has a ceiling. Time does not. So **any intervention that trades throughput for capability is structurally disadvantaged in a rate objective over a finite horizon** — the capability it buys cannot compound, and the throughput it costs is paid every item.

That may be why attribution does not pay. It may also be why *nothing* on the capability side pays.

**The diagnostic is cheap: does any intervention win on `E` by raising `K`?**

- If some do, my concern is void and the refutation stands clean and strong.
- **If none do, the objective has a blind spot** — it cannot reward capability preservation on any route, and the thesis's central claim is being tested against a measure structurally unable to register it.

That is worth knowing before phase 2, and it is not special pleading: it is a property of the objective that is true regardless of which way §7 came out.

---

## 4. The crossover is the venture asset — and it says something impolite

`σ_A/σ_q = 0.30`. **The reviewer must be about three times more accurate than the natural spread in output quality before they are worth having at all.** Above that, down to −36%.

The mechanism reads off the table and is the whole picture: **as the margin widens, `H` rises 0.46 → 1.00 while effective `q_W` falls 1.00 → 0.43. The noisier the reviewer, the more you write back, and the wronger what you write.**

State the practical consequence, because it is the part a room will remember:

> **Most real review fails this bar.** A reviewer whose error is comparable to the spread in the work is worse than no reviewer. Which is why "more oversight" and "more code review" so often fail to help — not because review is useless, but because *imprecise* review actively manufactures false lessons and files them.

That is counterintuitive, defensible, actionable, and it comes with a number. It is the strongest single thing this build has produced.

**It also reframes `q_W`.** Phase 1 said judgment-bearing content is a practice variable you control. This says **your reviewer's accuracy sets a ceiling on it** — you cannot write better lessons than the feedback you are drawing them from.

---

## 5. The three flags — all mine, all accepted

**The unit slip is the instructive one.** §4 gave a target as a ratio and §8 listed `h_S` as a coefficient, and `s̄` is ~7× smaller in scale than `T + L`, so `h_S = 20` is the target in engine units. General rule, worth a line in the spec: **a target expressed as a ratio must name the units of the thing it is a ratio of, or it will be read as a coefficient.**

Worth noting how well this validated: standalone 0.989 vs closed-loop 0.990, and ~0.32 vs 0.333. **The analytic table reproduced inside the full model to three decimals.** That is a good sign about both.

**Wiring C/D:** your resolution is correct and cleaner than what I wrote — D's gate survives on `ĝ_w = K·R`, with the adjudicator as an independent ungated channel. Two channels with different gating in one noisy-OR is exactly right; my §2 label was wrong, not the formula.

**Two bars, and they should be named separately.** You are right that clearing C2 and having a readable eight-cell layer are different things:

- **`C2-gate`** — `|corr| < 0.99`. Protects against the layer being trivially degenerate. Held by everything.
- **`C2-readable`** — `|corr| < 0.5`. Protects panel 6 as an actual reading.

At the reported **0.073–0.338**, part of the swept space already clears `C2-readable`. So **panel 6 is live where it clears and dark where it does not** — render it only in that region and say on the frame where the region is. That is better than either building it everywhere or dropping it.

---

## 6. Where the exhibit set now stands

The set has changed twice in two rounds and is stronger each time. Current ranking:

1. **The `σ_A` crossover with its mechanism** — a non-monotonicity with `H` and `q_W` moving in opposite directions beneath it. Best exhibit in the programme.
2. **The 0 / 0 / 40.5 interaction** — three cells at zero, pure interaction, instantly legible.
3. **The reviewer axis** — regimes on one side, none on the other. Replaces the regime map.
4. Panel 6, scoped to where it is readable.

**Retired:** the three-regime map.

The lay message now has a fourth line, and it is the one that will land hardest:

> Checking and not checking are a seesaw, and most advice just picks an end.
> Writing your judgment down is the one move that is off the seesaw — but the tool and the practice are worth nothing apart: zero, zero, forty together.
> Nobody maintains a store enough to keep it right and nobody abandons it enough to let it go.
> **And whether any of it works turns out to depend on someone else looking at the output — provided they are good at it. A reviewer who is merely present makes you write more, and write worse.**
