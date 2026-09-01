---
title: "Crossing the taxonomies — Heylighen's trace dimensions against our content types"
date: 2026-08-28
status: draft
see_also: externalisation-evidence-ledger.md, external-protocols-proposal-v2.md
---

# Crossing the taxonomies

Heylighen's stigmergy dimensions as the axes; the six colour-keyed content types plotted into them,
each **twice** — once as its human-side copy, once as its AI-side copy. The question the cross is
built to answer: *are our tiers well-formed, and what does the human/AI boundary actually do to a
trace?*

## The classification

| content type | trace kind | signal | evaporation | reach, AI side | reach, human side |
|---|---|---|---|---|---|
| working standards | marker-based | qualitative | very slow | **1.00** | 0.40 |
| general reference | marker-based | qualitative | slow | **0.60** | 0.25 |
| project reference | marker-based | qualitative | medium | **0.75** | 0.45 |
| templates | **sematectonic** | qualitative | slow | **0.55** | 0.20 |
| projects (tracking) | marker-based | **quantitative** | medium | 0.35 | **0.70** |
| status (tracking) | marker-based | **quantitative** | **fast** | 0.45 | **0.80** |

*Reach is measured **within scope** — when this trace is relevant, how reliably is it actually loaded.
That is the honest comparison; a global share would penalise `PER PROJECT` for being correctly scoped.
Evaporation follows the tier drift rates in `cascade.py`; tracking rates are new and invented.*

## Four things the cross shows

**1. The boundary does not move everything the same way — it swaps which side is reliable.**
For the four **context** types the AI-side copy has the greater reach; for the two **tracking** types
the human-side copy does. Stated plainly:

> **The AI reads your standards more reliably than you do. You know your status better than it does.**

That is the whole externalisation case and its limit, in one line, and it yields a design rule that is
not a platitude: **externalise the persistent-qualitative; keep the transient-quantitative in the loop
with a person.** Tracking is not context that hasn't been written down yet. It is a different kind of
trace and it belongs on the other side.

**2. The cascade is a trajectory through the space, not a hierarchy.** Project → general → standards
moves up and to the right: slower evaporation *and* wider reach together. Since leverage is
reach ÷ drift, and the axes are reach and inverse-drift, **leverage is simply up-and-right** — the
product of the two axes. The cascade is the gradient of the plane.

**3. Templates are off the cascade for a principled reason.** They are the only **sematectonic** type:
a template is the work itself in an unfinished state, stimulating its own completion — Heylighen's
half-built wasp nest. Everything else is a *marker about* work. The base diagram already separates
templates with a wider gap and no cascade arrow, on intuition. The theory supplies the reason, which
is a real validation of the existing drawing.

It also carries a consequence: **promoting into a template is completing work, not writing a note
about work.** The promotion operation is not the same operation there.

**4. Status sits in the pheromone corner** — high reach, fast evaporation, quantitative. That is
precisely a classical ant trail. It is also the single most dangerous thing to promote: pushing a
transient trace into a slow-evaporating, high-reach tier is the archive trap's *mechanism*, not merely
its symptom. **The cascade needs a floor, and status is below it.**

## Where our taxonomy is not well-formed

**~~`working standards` and `general reference` occupy nearly the same cell.~~ Withdrawn
2026-08-28.** The plane collapsed them because it has no axis for *which side a trace serves*, and on
reach alone they do look like one type with two policies. They are not:

- **working standards** are **bidirectional and grounding.** They scale the exchange to terms the
  person already holds, so the stream runs back into the human as well as sitting in the AI store.
  They improve the human's ability to interact with the AI meaningfully.
- **general reference** is **unidirectional.** Project-independent context about the operating
  environment, travelling human → AI and never returning.

The difference is **in the plumbing, not the policy** — which is exactly why a position-only plane
could not see it, and why the flow drawing (`separation-flow_2026-08-28.html`) exists. Directionality
is the missing dimension; the plane should carry it as a mark, or defer to the flow view.

**`projects` and `status` share a box and differ in evaporation by roughly an order of magnitude.**
The tier hierarchy is decay-rate-matched everywhere else; the tracking boxes are not. They should
probably split.

## How to argue with this

Every position is a **judgement**, not a measurement — that is the point of plotting it. Disagreement
here is concrete: move a point and say why. The two claims that would break if the positions are wrong
are (1) the context/tracking reach reversal and (2) templates as the sole sematectonic type. Both are
checkable against practice rather than opinion.
