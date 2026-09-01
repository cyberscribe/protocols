---
title: "Spec — phase 1b (headless) and the PI stage, in one pass"
date: 2026-08-28
build_target: peakepro-diagnostics/cognition-assessment/sim/externalisation/
supersedes: nothing — extends SPEC-externalisation-sim.md v0.3
---

# Phase 1b + stage spec

One document, two parts. **Part B is written against results-conditionals**, so it can be built without waiting for Part A — but nothing renders until the Part A checks pass.

---

## Part A — three model changes, headless

### A1. The store splits by side of the boundary, and each side acts on a different term

**This is the change that matters most.** The model currently has one store acting on `fit` only, so the AI-side context store — the thing the source diagram spends half its area on — is not represented in `correctness` at all.

Per `diagrams/exec-fn-ai-org`:

| store | what it holds | side | acts on |
|---|---|---|---|
| `X^H` | project outcomes, status, what was decided and how it landed | **human** | **fit** — did we build the right thing |
| `X^A` | standards, general and project reference, templates | **AI** | **correctness** — is what we built right |

Each keeps its own `(mass, validity)`. The wiring differences are not cosmetic:

```
fit_t   = clamp01( fit0  + b_H·Λ^H_t·(2·X^H_v − 1) )
corr_t  = clamp01( B_t   + b_A·Λ^A_t·(2·X^A_v − 1) + η_h·R_t·K_t·S )

Λ^A_t = X^A_m · n_t                      automatic — the grey arrow, free
Λ^H_t = X^H_m · n_t · consult_t          the human must look; costs attention
```

**Aggregation — two different means, and using the same one twice is the trap.**
Wherever load and displacement need a single loading figure, take the **plain mean**:
`Λ̄ = (Λ^H + Λ^A)/2`. Summing two shares exceeds 1 and puts `(1 − Λ)` negative — at
`X_m = 0.8` both sides and `n = 0.9`, the sum is **1.44** and `(1 − Λ) = −0.44`.

But **validity is already a ratio, so it pools by mass, not by plain mean**:
`X̄_v = (V^H·consult + V^A)/(X^H_m·consult + X^A_m)`. A plain mean lets a tiny pristine
store cancel a large stale one — big stale AI side plus small clean human side gives a
staleness signal of **+0.105 plain against −0.700 weighted**: *the plain mean says the
store is helping while the weighted one says it is hurting.*

**Reduction property, and assert it as a unit test.** At `consult = 1` with identical
sides, both aggregates collapse exactly to the one-store model — verified to 12 dp on
`Λ` and on `X_v` across three configurations. **Gate C13.**

**`Λ^H` is not free.** The diagram draws automatic loading only on the AI side; human-side tracking is read by a person. Add `c_cons·consult` to the load equation. That asymmetry is the diagram's central geometry and the model should not flatten it.

Write-back splits the same way: `H` allocates between recording *outcomes* (`H^H`) and recording *context* (`H^A`). Simplest v1: one `H` and a split parameter `φ ∈ [0,1]`. `φ` then becomes a treatment — *what kind of thing you write down* — which is a distinct question from `q_W` (*how good it is*).

**The prediction this generates, and it is sharp.** The objective multiplies `fit × correctness`. Two stores feeding two factors of a product means **the weaker one dominates**: investing in AI-side context while human-side tracking is stale buys almost nothing, and vice versa. That is a **second complementarity**, the same shape as tool × practice but on a different axis — and it is testable immediately.

⚠️ Do not assume it. `b_H` and `b_A` may differ enough that one side dominates at every reachable configuration, in which case the complementarity is a magnitude story and not a structural one. **Check whether both cells go to zero, as tool × practice did.**

### A2. The reviewer becomes a ladder, with self-review at the bottom and omniscience at the top

Rungs, all on one dial:

| rung | who | margin `σ_A` |
|---|---|---|
| 0 | **yourself, loaded** | `σ_self = S_FLOOR + A_D·D + A_L·L` — **endogenous** |
| 1 | yourself, fresh | `σ_self` evaluated at low `L`, `D` |
| 2 | a peer | fixed, moderate |
| 3 | an expert | fixed, low |
| 4 | **omniscient** | `σ_A = 0` — the ceiling, and the reference every other rung is measured against |

Rungs 0 and 1 are **the same person**, which is the point: the ladder is not only about who reviews you. Findings already in hand from `analysis/self-adjudication.py` (invented coefficients — shape and signs only):

- self-review is worth doing **only inside a wedge** in `(load, debt)` — **but the locus published in the probe was wrong by a 14× unit slip** and is superseded (see below);
- **the optimal number of self-review passes falls with starting load** — 5 fresh, 2 mid-day, 1 loaded, and past the optimum each pass makes the work *worse*;
- `|corr(H,R)| = 0.752` under self-review against 0.073–0.338 for an outside witness: **partial independence only.** The draw is fresh; the *scale* is a function of the shared states.

**The margin is derived, not posited.** The probe's `σ_self = S_FLOOR + A_D·D + A_L·L` read the 0.30 crossover as an absolute `σ` when it is a **ratio to `σ_q ≈ 0.07`** — absolute crossover **0.021**, so `S_FLOOR = 0.04` sat 1.9× past it before any load or debt and the locus was empty. The repair is not a rescale. Use the reveal gate already in the model:

```
ratio_self = λ · (1 − K_t·R_t)          K = 1/(1+D);  crossover at ratio 0.30
flip where  K·R = 1 − 0.30/λ            λ = 1  →  K·R = 0.70
```

Now "highly competent at the outset" means `K·R → 1`, `ratio_self → 0`, and self-review is genuinely worth doing — as it should be. The locus is **non-empty and bounded** (debt at flip: 0.43 at zero load, 0.21 at 0.2, 0.05 at 0.4, closed off entirely by load ≈0.5), and it is a **consequence of the model rather than three invented coefficients** — which was the probe's stated weakness anyway.

**The structural claim to test properly in the engine:** self-review loses accuracy and independence *at the same moment*, so the faculty that would notice the flip goes exactly when the flip happens.

### A3. Load and debt become first-class outputs, not equation chips

They are the conundrum. Report them per run, and compute the **flip locus** — the curve in `(L, D)` where `σ_self` crosses the 0.30 threshold — as a first-class artefact, because it is what Part B draws.

### A4. Not now, and say why

Robert's forward note — load and debt may also degrade *the effectiveness of the externalisations themselves*. That is a **third** channel and it **compounds**: today a stale store hurts through validity only; if load also degrades your ability to *use* a good store, the archive trap and the self-review spiral start feeding each other. Isolate first — this goes in after A1–A3 are wired and checked, on the same discipline that got the oscillator working.

Also deferred: the **sync** quantity — how far `X^H` and `X^A` have diverged from each other. That is the diagram's colour overlay ("the same thing held twice, to be kept in sync") and A1 finally creates a home for it. Note it as the next natural state, not a v1 term.

---

## Part B — the stage

**Register: stage, not viewer.** One screen, 1280×720, no scrolling, dials re-run on `input` not release, no prose, no jargon, no parameter names on screen. `VIEW-DECISIONS.md` clause by clause. House palette as plain strings. Poppins with a real fallback; monospace for every number. `setTimeout`, not `requestAnimationFrame`.

`mockups/pi-stage-mockup.html` is the layout reference and is approved as a starting point. Three changes.

### B1. Four dials — and the reviewer dial becomes the ladder

| dial | left | right |
|---|---|---|
| a place to put it | nothing | good tooling |
| worth writing down | bare notes | full judgment |
| **who checks the result** | **yourself, at the end of a long day** | **someone who is never wrong** |
| how much gets re-read | forgotten | always loaded |

The third dial is A2's ladder in plain words. **Rung 0 is where most people live**, and moving right is the whole consulting proposition made draggable.

### B2. The centrepiece: the load–debt plane with the flip locus on it

Reuse the posture-plane idiom — axes, crosshairs, a dot, a short trail — with **load on x and debt on y**, and the self-review flip locus drawn as a curve across it.

> **Above the line, checking your own work makes it worse.** The dot shows where the current settings put you.

This is the panel that earns the stage. It puts the conundrum, the worker's position and the self-review result in one picture, in an idiom the room has already seen, with no jargon at all. It also replaces the reviewer curve as the primary — keep that curve as a small secondary strip, or drop it.

### B3. Two stores, drawn on their two sides

Split the store bars into a human side and an AI side, laid out **left and right of a thin dashed divider** — the same divider as the source diagram, so anyone who has seen that picture reads this one for free. Mass and validity per side. Label the terms they feed: *the right thing* under the human side, *right* under the AI side.

### B4. Conditionals — write these as branches now, resolve them from Part A's output

| if Part A finds | panel shows |
|---|---|
| a second complementarity (both single-side cells → ~0) | a **second 2×2**, human-side × AI-side, beside the tool × practice one |
| one side dominates at every configuration | a single stacked bar with the dominant side marked, and the frame says which |
| the flip locus is empty (self-review always worth it) | the plane loses its curve and prints **`NO FLIP`** |
| `\|corr(H,R)\|` ≥ 0.5 at every rung | the eight-cell layer stays dark, with the reason on the frame |

**The stage must print its own failure in the same place it prints its success**: `NO FLIP` · `ONE REGIME ONLY` · `COLLAPSED` · `ONE SIDE ONLY`.

### B6. The honesty affordance — and this is what makes it *PI*-friendly rather than merely working

A formal-theory group's first question will be **"which of these numbers rests on something you made up?"** The stage should answer that before it is asked.

- Every dial and readout whose value depends on an **unanchored** nuisance parameter carries a small marker.
- One line names the count: *"n of the figures on this screen depend on m parameters with no empirical anchor."*
- A toggle — **`ROBUST ONLY`** — greys out everything that does not survive ±30% on every parameter it depends on, leaving the model's defensible subset lit.

The `(r, λ)` knife-edge is the case in point: `r = γ/δ_K` moving 2.5 → 2.4 flips *self-review is never worth doing* to *self-review has a wedge*. **A stage that cannot show that is not honest enough for this audience.** Under `ROBUST ONLY` the flip locus should go dark until the `(r, λ)` sweep has bounded it.

This is unusual and it is the reason to build it: a demo that volunteers its own soft spots earns a hearing that a demo defending its numbers does not.

### B5. Provenance

One line, and it must survive the split: *model output, never measurement · which model, which rung, which seed*. The mockup's current line — that magnitudes are illustrative — comes off only when the stage is wired to `model.mjs` and not before.

---

## Gate additions

C9 — **two-store separability**: `X^H` and `X^A` are distinguishable on `E`; the single-side cells are measured, not assumed.
C10 — **the flip locus exists and is bounded**: `σ_self` crosses 0.30 somewhere inside reachable `(L, D)`.
C11 — **rung monotonicity**: `E` is non-decreasing up the reviewer ladder at fixed everything else. **If it is not, something is wired backwards** — an omniscient reviewer cannot be worse than a vague one.
C12 — `Λ^H` costs attention and `Λ^A` does not; assert it directly, since flattening that asymmetry is the easiest mistake to make here.
C13 — **reduction**: at `consult = 1` with identical sides the two-store model equals the one-store model exactly, on `Λ` and on `X_v`.
C14 — **every threshold carries its units in its name.** `CROSS_RATIO = 0.30` (of `σ_q`) and `CROSS_ABS = 0.021` never share an identifier. Two unit slips of this exact kind have already cost a build each — `h_S` as ratio-vs-coefficient, and `CROSS` as ratio-vs-absolute.

Standing rails unchanged: nuisance parameters held identical across arms and never adjusted to improve a result; regimes and loci found, not tuned; if a check fails, stop and report.
