---
title: "Discipline and referencing — two constructs, one ritual"
date: 2026-08-28
status: draft
see_also: external-protocols-proposal-v2.md, ../../peakepro-diagnostics/cognition-assessment/settled-questions.md
---

# Discipline and referencing

## The definitions

**Referencing** *(canonical term)* — deliberately engaging with what was externalised, for context
and orientation. It is **not** loading. Loading is automatic and free on the AI side and incidental
on the human side; referencing is an act, it costs something, and without it externalisation does
nothing for the bucket that leaks. The store fills and the head still empties.

**Discipline** — **the degree to which the ritual is decoupled from felt need.**

$$\text{ritual}_t \;=\; (1-D)\cdot \tilde{n}_t \;+\; D, \qquad
\tilde{n}_t = \tilde{n}_{t-1} + \lambda\,(n_t - \tilde{n}_{t-1})$$

where `n` is actual need and `ñ` is felt need, which lags it. At `D = 0` the ritual tracks the
feeling; at `D = 1` it runs regardless. Discipline governs **both limbs — externalising and
referencing** — because they are the same ritual.

Discipline is not effort, and it is not conscientiousness as a trait. It is a *coupling coefficient*.
That is what makes it a training target rather than a personality finding.

## Why this is the right shape

The offloading literature says people offload on **felt need**: low confidence drives more
externalising (Boldt & Gilbert 2019), and metacognitively impaired participants fail to scale it with
difficulty at all (Cherkaoui & Gilbert 2017). So a well-calibrated strong performer externalises
*less* — which reads as sensible, and is, right up to the point where the feeling is wrong.

And the feeling is systematically wrong in exactly the way that matters, because **it lags.** You stop
feeling the need while the bucket is still draining. You ease off precisely when you should not, and
find out several sessions later.

**Discipline is the parameter that says: do it anyway.**

## The claim this licenses about the trust trap

The trap runs: trust ↑ → promotion effort ↓ → process evidence thins → capability erodes → weight
shifts to stale outcome evidence → trust ↑. Every model we have written makes the corrective act a
function of the state that the trap corrupts.

> **The trap is not that people trust too much. It is that the corrective act is gated on doubt.**

Discipline ungates it. `H = h(T, L, ρ)` with `∂h/∂T < 0` is the trap's feedback edge; discipline is
`1 − |∂h/∂T|`, and at `D = 1` the edge is cut and the loop cannot close. **That is the mechanism by
which consistent externalisation and referencing break the cycle**, stated in the model's own terms
rather than asserted alongside it.

It also settles the programme's posture. You do not teach people to distrust the AI — that is an
attitude intervention, it fights a feeling, and the feeling is not the problem. You teach a ritual
that runs whether or not the feeling shows up. **That is a training proposition, and it is why this
is a training business and not a software one.**

## The convergence worth noticing

`sim/correspondence/cascade.py` found, from an entirely different direction, that vigilance which
responds to its own recent yield has a hole in it: at low poison rates nothing triggers checking and
~85% passes through, while at high rates vigilance catches ~89%. The conclusion recorded there was
*"an argument for scheduled checking rather than triggered checking — a gate whose rate does not
depend on its own recent yield."*

**Scheduled-not-triggered is discipline.** Two independent routes to the same parameter — the third
time in this programme that has happened, after the gating rule arriving from the value side and the
trust side at once. Convergence of that kind is the best evidence available that the structure is
real rather than chosen.

## What to test

Discipline is measurable without asking anyone how disciplined they are: it is the **correlation
between externalising/referencing behaviour and felt need**. A low correlation *is* high discipline.
That is a behavioural measure, it needs no self-report of the construct itself, and it dodges the
self-report inflation the TMS meta-analysis warns about (see `settled-questions.md` §3).

Prediction, and it is falsifiable: **among people with equal externalisation volume, those whose
externalisation is less correlated with felt need will show less capability erosion.** Volume is not
the protective factor. Decoupling is.

## Still open

Whether discipline raises **discernment** — the edge that would connect the human side to the AI side
for the first time. Left out deliberately: a positive loop produces spirals by construction, and the
honest output is the threshold loop gain rather than the spiral itself.
