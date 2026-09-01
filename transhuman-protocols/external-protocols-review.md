---
title: "Review — Externalised Protocols for Effective Human-AI Co-Cognition"
reviews: external-protocols.txt
date: 2026-08-28
status: draft-review
---

# Review — external-protocols.txt

Citation audit, feasibility assessment, and the binding of DRIVE + `diagrams/exec-fn-ai-org_2026-08-26.svg` onto the formal claims.

> **§2 is superseded.** The formal model has moved to [`external-protocols-model.md`](external-protocols-model.md) (v2, 2026-08-28), which adopts the explicit loading/promotion split. §1, §3 and §4 stand.

---

## 1. Citations

All six resolve. Every link points at the paper the text says it does, and every claim attributed is a claim the source makes. That is unusual and worth noting.

| Cited as | Actual | Verdict |
|---|---|---|
| Chen et al., 2026 — `10.1177/00187208261477486` | Chen, Liu, Ma, Zhang, Chen, Wang, Zhang, Tian, Gao & Shen, *How Cognitive Load Affects Dynamic Trust Calibration in Human–AI Collaboration: Evidence for Selective Pathway Effects*, **Human Factors** 2026 | ✅ exact. The paper's own frame is "two trust updating pathways"; process-based updating attenuated under high load |
| Bastani et al., PNAS 2025 — PMC12232635 | Bastani, Bastani, Sungu, Ge, Kabakcı & Mariman, *Generative AI without guardrails can harm learning*, **PNAS** 122, `10.1073/pnas.2422633122` | ✅ ~1,000 students, grades 9–11, Turkish high school, Fall 2023, preregistered (AsPredicted). GPT Base +48% on practice / **−17% on unaided exam**; GPT Tutor +127% on practice / no significant exam difference |
| Liu et al., 2026 — `arXiv:2604.04721v4` | Liu, Christian, Dumbalska, Bakker & Dubey, *AI Assistance Reduces Persistence and Hurts Independent Performance* — submitted 2026-04-06, revised 2026-08-05 | ✅ 1,222 participants; effects after ~10 min exposure; still a preprint |
| Wu et al., 2026 — `arXiv:2608.23543` | Wu, Belem, Fu, Steyvers & Smyth, *How AI Assistance Affects Human Skill Development: A Study of Learning with Logic Puzzles* — 2026-08-24, **HCOMP 2026** accepted | ✅ lower-cost assistance → more use; greater independent effort → larger latent-ability gains |
| Klein & Klein, 2025 — PMC12738859 | Klein & Klein, *The extended hollowed mind: why foundational knowledge is indispensable in the age of AI*, **Frontiers in AI**, 2025-12-11, `10.3389/frai.2025.1719019` | ✅ defines *cognitive sovereignty* and the *Sovereignty Trap* |
| Meng, 2026 — `arXiv:2606.15078v1` | Shuchen Meng, *Cognitive Debt: AI as Intellectual Leverage and the Dynamics of Systemic Fragility*, 2026-06-13 | ✅ *cognitive debt* = "the stock of unverified reasoning obligations" |

### Three fixes

1. **PNAS issued a correction** to Bastani et al.: `10.1073/pnas.2518204122` (PMC12403119, Aug 2025). It is behind a 403 and I could not read what it changes. Read it before the numbers above go into anything public.
2. **The last bullet lumps three terms across two citations.** Meng has *cognitive debt* but not the sovereignty terms; Klein & Klein have the sovereignty terms. Split the sentence so each term carries its own source.
3. **Wu et al. is underused.** As cited it is a supporting curiosity. Read together, its two findings are the mechanism the whole thesis needs: *cheap assistance crowds out the independent effort that is the thing producing capability gain.* That is a causal chain, not a correlation — promote it out of the list and into the argument.

### The shape of the evidence base

Every one of these is a short-horizon, task-level study, on students or paid participants, on well-specified problems with checkable answers, with the AI acting as a solution-provider. The thesis is about professionals, on ill-specified problems, where ground truth is delayed or absent, over months to years.

Nobody will contest that AI substitution degrades unaided performance on a maths problem in ten minutes. That is now well-evidenced. The distance from there to "protocols preserve professional judgment" is the entire contribution — so name it as the contribution rather than letting the citations imply the case is made. **The claim is that a task-level mechanism aggregates.** That is novel, defensible, and not yet tested by anyone.

One asymmetry to exploit: Bastani is the strongest study of the set and the only one that tests a *remedy*. But its guardrail is designed by teachers **into the tool**. The programme's guardrail is practised by the worker **around the tool**. That distinction — tool-side vs. practitioner-side externalisation — is the wedge, and the draft does not currently make it. It is also precisely what makes this a training proposition rather than a software one.

---

## 2. The formal model

### 2.1 `E` is doing two jobs and the notation hides the one that matters

As written, externalisation enters once, inside `w_p(L_t, E_t)`. But externalisation plausibly does three separable things:

- **(i) creates** process evidence that did not previously exist — criteria, contributions, checks and failures were not observable at all;
- **(ii) reduces load**, which raises `w_p` via `L_t`;
- **(iii) changes what the process evidence says** — a good harness emits different evidence from a bad one.

Path (ii) runs through `L_t`, which is itself a function of `E`. So the model as written cannot distinguish *"externalisation helped because it cut load"* from *"externalisation helped because it made the process legible."* Those imply different interventions and different training.

That distinction is the draft's own headline claim — "not merely a memory aid or load reducer" — and it is the one thing the notation collapses.

**Fix:** let `E` enter twice, explicitly, with a load path and an evidence path, so a design can null one and keep the other. That also names the discriminating experiment: **an externalisation that *adds* load while adding process evidence.** If the thesis is right, calibration should still improve.

### 2.2 The two equations never touch

`D_t` is defined and then never appears in `T_{t+1}`. As it stands these are two models side by side, not one theory.

The link is already established in our own simulator work: *a failing check is only informative to someone who knows what it means* — validation gated on expertise. Process evidence is not legible to a worker whose unaided capability has eroded. So:

```
w_p = w_p(L_t, E_t, K^observed-unaided_t)
```

That single argument closes the loop and turns a cost model into a trap model. Debt does not merely accumulate; it degrades the pathway by which trust would have been recalibrated, which raises reliance, which raises debt. This is the same result as the gating rule in `sim_aid_channel_findings` arriving from the trust side rather than the value side — two independent routes to the same structure is a good sign.

### 2.3 There is no lag

`T_{t+1}` receives outcome evidence at `t+1`. In professional work outcome evidence arrives months later, or never.

This is not a detail. `sim_oscillator_conditions` Condition 2 says lag decides whether the loop is a limit cycle or settles at all — and lag improves no other term in the model. It is probably the single largest structural difference between the lab settings the citations describe and the setting the thesis targets: outcome-dominance under load is merely suboptimal when outcomes land in ten seconds and catastrophic when they land in two quarters.

**Add a lag parameter to the outcome pathway.** One symbol, and it is what makes the professional case different in kind rather than degree.

### 2.4 `D_t` is unmeasurable as written — but it is a good product spec

`K^expected without substitutive AI` is a counterfactual trajectory of an individual. It cannot be observed. Two tractable substitutions:

- **Between-subjects with a control arm** (Bastani's design). `D` becomes an arm difference. Cheap, established, publishable — and loses the per-person diagnostic, which is the thing the venture actually needs.
- **Within-person with periodic unaided probes.** Measure `K^observed-unaided` directly at intervals; estimate the counterfactual from the person's own pre-AI slope plus a control cohort's slope. Feasible, and it *is* a diagnostic instrument — which is what `peakepro-diagnostics` already is.

One thing to be explicit about: **the probe changes what it measures.** Liu et al. get effects from ~10 minutes of exposure; a periodic unaided probe is itself a dose of unaided practice. In a study that is contamination. In a practice it is the intervention you are selling. Same instrument, opposite sign, depending on which activity you are doing — decide per study, and say so.

### 2.5 The buried constraint is the actual novelty

*"...without imposing continuous supervisory effort"* is the hardest and most valuable clause in the document and it is currently a subordinate phrase.

Preserving judgment by checking everything is not a finding; it is declining to use the tool. And our own simulator says "check your work more carefully" goes *negative* below about a third of full expertise. The defensible claim is stronger and narrower:

> **There exist externalisations whose supervisory cost is paid once, at setup, and amortised — not paid per task.**

That is testable, it is the difference between a protocol and mere vigilance, and it maps exactly onto the diagram.

---

## 3. DRIVE and the diagram as the mechanism layer

### 3.1 The mapping

| DRIVE | evidence pathway | aid channel | location in `exec-fn-ai-org` |
|---|---|---|---|
| **D**ecide | neither — this *is* the allocation choice | definition aids | human tracking: what reaches the loop at all |
| **R**equest | creates process evidence *ex ante* — criteria stated before the answer exists | definition + thought | loading: stores → loop |
| **I**nspect | process evidence, cheap, in-session | detection aids | working memory / the loop |
| **V**alidate | outcome evidence, gated on residual capability | validation aids | the loop's boundary with the human |
| **E**volve | converts an episode into durable evidence | study aids | **promotion: loop → stores** |

Note that Request is the one stage that generates process evidence *before* any output exists, which makes it the only stage immune to the gating problem in §2.2 — you do not need residual expertise to notice that you never stated a criterion. That is the cheapest defensible foothold in the whole method, and it is why Request should carry the intent/context/assumptions triad explicitly.

### 3.2 The diagram already draws the asymmetry the theory needs

Loading is short, grey, automatic. Promotion takes the long way round and is human-involved. **That asymmetry is `w_o` versus `w_p`.** Loading is cheap and produces no evidence about the worker's own capability; promotion is expensive and is the only point where the worker must decide whether something is true enough to keep.

Four of five DRIVE stages happen inside a session. Only Evolve crosses the promotion arrow.

Which gives the sharp claim to put at the centre of the programme:

> **The externalisation that preserves judgment is promotion, not loading.**
>
> Loading more context reduces load and improves output — and does nothing for calibration or debt, and plausibly worsens both by raising trust with no process evidence attached. Promotion is the costly, human-involved, once-per-insight act that both encodes process evidence *and* requires exercise of the discernment being measured.

This is worth building the programme on because:

- it is **falsifiable** and cheap to test (§4);
- it runs **counter to the industry's entire direction** — RAG, memory, longer context, auto-compaction are all investment in better loading;
- it **satisfies the amortisation constraint of §2.5 by construction** — a promoted standard applies to every future session, so its supervisory cost is paid once;
- the four stores form a **gradient of amortisation**: templates and project reference are cheap and local; working standards is expensive and global.

And the cascade already in the diagram — project reference → general reference → working standards — is a **ladder of evidence**: a thing climbs only when it has survived enough episodes. That is accumulated process evidence, drawn as geometry.

### 3.3 The gap in the diagram, and it is a real one

The `ALWAYS / AS-NEEDED / PER PROJECT` discipline pills are the `E` term made operational: they say which stores are guaranteed to be in a given session's evidence base. Working standards is `ALWAYS`. That makes it the highest-leverage and the highest-risk object in the system.

**There is no demotion arrow, no expiry, and no review on the stores.** Promotion has a human in the loop; nothing has a human in the loop after that. A wrong or stale standard is then silently loaded into every session forever, with no process evidence attached to it and no channel that would surface it.

So debt can accumulate **in the store rather than in the person** — a failure mode neither the trust equation nor the debt equation currently represents, because both are about an individual's capability.

This is the strongest link back to the GTD spine: GTD's non-negotiable component was the **weekly review**, and it existed for exactly this reason. DRIVE's Evolve is currently drawn one-directional. It needs a demotion path, or a sixth thing.

---

## 4. Feasibility

**Testable now, cheaply, with agentic tooling:**

1. **The loading-vs-promotion discriminator.** Two arms, identical tasks. Arm A receives a rich pre-loaded context. Arm B starts thin and must promote after each episode. Unaided probe at T+2 weeks. This is the study — it tests §3.2 directly, it is a within-reach RCT, and no one has run it.
2. **Chen et al. + an externalisation arm.** A direct extension of a paper published this year, using their load manipulation, adding the two `E` paths from §2.1. Small, fast, and it lands in an established conversation rather than starting one.

**Not testable yet — do not claim it:** anything about professional judgment over a career. Frame it as the horizon the programme is walking toward, with the aggregation claim (§1) as the near-term contribution.

**The programme shape that follows:** task-level replication and extension over months, then a longitudinal field study run *inside a consulting engagement*, where the diagnostic instrument is the client deliverable and the research data is a by-product. Venture and research become the same activity. That is the strongest structural asset in this whole thread and it should be stated as a design choice, not left to emerge.

---

## 5. Actions

- [ ] Read the PNAS correction `10.1073/pnas.2518204122` before quoting Bastani's figures publicly
- [ ] Split the Klein & Klein / Meng bullet so each term carries its own citation
- [ ] Promote Wu et al. from the list into the argument as the mechanism statement
- [ ] Rewrite `w_p` with `E` entering twice (load path, evidence path)
- [ ] Add `K^observed-unaided` as an argument to `w_p` — this is what joins the two equations
- [ ] Add a lag parameter to the outcome pathway
- [ ] Pick a `D_t` estimator (between-subjects vs. within-person probes) and state the probe-contamination position
- [ ] Raise "without continuous supervisory effort" from clause to thesis
- [ ] State the tool-side vs. practitioner-side distinction explicitly
- [ ] Add demotion / review to the diagram and to Evolve
