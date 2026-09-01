---
title: "Formal model — externalised protocols for human-AI co-cognition"
supersedes: the equations in external-protocols.txt
see_also: external-protocols-review.md
date: 2026-08-28
status: draft
---

# Formal model (v3)

*v3 (2026-08-28): `R` (independent reasoning) added as a state; measurement layer added; strict simplex adopted. See §10.*

Response to the proposed revision. Verdict first: **the Λ/Π split is the right structural move and it buys more than it was asked to.** Two gaps stop the system running, one addition makes the central claim quantitative, and there is a closed-form result sitting in the delta-rule form that is worth building the paper around.

---

## 1. What the revision gets right

**Separating Λ (loading) from Π (promotion) as distinct objects.** This is the theory written into the algebra rather than asserted alongside it. Λ enters `L` and `O`; Π enters `P` and `C`. Loading buys performance and load relief; promotion buys evidence. Nothing has to be argued — the asymmetry is now a fact about which symbols appear in which equations.

**The delta-rule form `(P_t − T_t)`.** A real improvement on the draft's additive `+ w·evidence`. It bounds `T`, gives it fixed points, and makes it a proper Rescorla–Wagner updater rather than an unbounded accumulator. One commitment comes with it: **`P`, `O` and `T` must now be commensurate** — both evidence channels have to be rendered as implied-trustworthiness on `T`'s scale. Worth stating explicitly, because otherwise the unit mismatch gets silently absorbed into `η_p` and `η_o` and they stop meaning anything.

**`O_{t−τ}`.** Right, and a plain fixed lag is the right first cut — no need for a distributed lag yet.

**`w_p(L_t, K^{obs,u}_t)` with `∂w_p/∂K > 0`.** This is what joins the two equations. Process evidence is only legible to someone with residual unaided capability.

---

## 2. The result this form gives you free

Impose `w_p + w_o = 1` (see §4.1). The fixed point of the trust update is then:

$$
T^\* = w_p P + w_o O
$$

Take process evidence as the calibration target — that is what "calibrated judgment" means here: trust tracking actual reliability, which is what `P` reveals and `O` only proxies. Then:

$$
\boxed{\;T^\*-P \;=\; w_o\,(O-P)\;}
$$

**Miscalibration is the outcome–process gap, times the load-driven weight on outcome.** Two terms, and the whole theory sorts into them:

| intervention | term it moves |
|---|---|
| thought aids, load reduction | `w_o` ↓ |
| detection aids, better harness (larger `Z`) | `P` ↑ |
| study aids, promotion, preserved `K` | `(O − P)` ↓ |
| shorter feedback lag | `τ` — not in this equation at all; it governs whether the system *reaches* `T*` (§5) |

And the trap needs no irrationality. `O > P` precisely because **substitutive AI genuinely produces good outcomes** — that is Bastani's +48% on practice problems. Outcome evidence is honest and favourable; process evidence is honest and unfavourable; load shifts weight from the second to the first. Overtrust follows from two true signals and a weighting.

That is the sentence to lead with. It is also the reason the programme is not a scold: nobody in this model is being lazy or credulous.

*(Note what this costs: it makes `P` the normative anchor by assumption, not derivation. Defensible — if `O` were an unbiased estimator of reliability there would be no thesis — but say so rather than letting it look derived.)*

---

## 3. Two gaps that stop the system running

### 3.1 `K^{obs,u}` has no equation of motion

It now appears inside `w_p` and inside `o(·)`, but nothing updates it. The system cannot be simulated as written. This is the blocking gap.

$$
K_{t+1} = (1-\delta_K)K_t + \gamma\,g(R_t,H_t),
\qquad
R_t = r(T_t,L_t,\Lambda_t,Z_t),\quad \frac{\partial r}{\partial \Lambda}<0
$$

**`Λ` must not enter `g` directly.** Wu's predictor is *solo share* — independent problem-solving effort — and AI-request frequency stops predicting skill change once initial ability and solo share are controlled (`α_usage` posterior mean 0.0004), with the solo-share coefficient explicitly flagged as associational. So Wu supports *"assistance harms skill when it displaces reasoning"*, not *"loading harms skill holding reasoning constant."* An unconditional `∂g/∂Λ < 0` overclaims the source.

The fix is a separate state: independent reasoning `R_t`, decreasing in `Λ`, feeding capability alongside promotion effort. Loading then carries no contemporaneous penalty and becomes globally harmful **only through displacement**. `K^{*,u}` runs the same equation at a reference `R` with `Λ = 0`.

If you want the stronger unconditional hypothesis, keep `g(H,\Lambda)` but call `Λ` *substitutive* loading and cite Wu as motivation rather than confirmation.

### 3.1a Two things `R` costs, and one it buys

**It buys instrumentation.** `R` is *more* observable than `K` — solo share is exactly what Wu measured, and in a task stream it is the proportion of steps taken before invoking the model. Adding the state costs nothing empirically.

**Cost 1 — `R` and `H` are near-collinear.** Both decrease in `T` and `L`, both increase in `Z`. Their only structural difference is that `R` depends on `Λ` and `H` does not, so **`γg(R,H)` is decomposable only through the `Λ` manipulation.** The loading × promotion factorial is now load-bearing for identifying the model, not merely for testing the hypothesis. Under-powering the loading arm loses the parameter, not just the contrast.

**Cost 2 — `Λ` has a competing positive path to `H`.** Loading reduces `L`; `H` decreases in `L`; so loading *raises* promotion effort by freeing capacity, while lowering `R`. The net effect on `K` is ambiguous by construction. That is a genuine consequence of the structure and should be stated as a prediction rather than discovered in the data: **for a worker who does promote, loading may be net positive.** The harm is concentrated in those whom loading tips out of promoting.

### 3.2 `T` is updated and then consumed by nothing

Trust is an epiphenomenal readout in the current system. Nothing depends on it, so the trap cannot close and `1{Evolve_t}` has to be supplied by hand — which means the model cannot explain the one behaviour it exists to explain, namely **why people stop promoting**.

$$
H_t = h(T_t, L_t, \rho), \qquad \frac{\partial h}{\partial T}<0
$$

With that one line the loop runs on its own: `T ↑ → H ↓ → P` thin and `K` erodes `→ α ↓ →` trust updates increasingly on stale, favourable `O_{t−τ} → T ↑`. Under long `τ` the corrective channel is both down-weighted *and* out of date, which is the professional setting.

### 3.3 Latent capability needs a measurement equation

$$
K^{obs,u}_t = m(K_t,U_t)+\nu_t
$$

where `U_t` is an unaided opportunity or probe.

Be precise about *why* this is needed, because the obvious reason is wrong. It is **not** that letting `α_t` depend on `K` illegally observes a latent state — the model does not claim the *agent* observes their capability, it claims capability *causes* the weighting, which is exactly the sim's gating rule ("a failing check is only informative to someone who knows what it means"). Competence, not self-knowledge. So `α_t` should take **latent `K_t`**, and anything that writes `K^{obs,u}` into `α_t` has reproduced the problem it was trying to fix.

What the model actually lacked is a **link to data**: `K` is latent, the delayed unaided probe is the estimator, and without `m(·)` there is no equation connecting them.

Bonus: `U_t` now appears in two places — as a measurement occasion in `m(·)` and as reasoning in `R_t`. That makes the probe-contamination problem representable rather than merely noted. A probe *is* a dose of unaided practice; now the model says so.

---

## 4. The addition that makes the central claim quantitative

**Π should enter `K`, not only `P` and `C`.**

As drafted, promotion buys evidence and store content. But deciding what from a session is worth keeping *is* effortful cognition — reflection, reconstruction, codification. Note this is a *separate* contribution from `R`: `g(R_t,H_t)` has two arguments, and promotion contributes through the second even at constant independent reasoning. (Wu measures `R`, not `H`, so this arm of the claim is a hypothesis of ours, not a finding of theirs — do not cite Wu for it.) With `H` in `g`:

- **Π appears in three places** — `P` (evidence), `C` (store), `K` (capability)
- **Λ appears in two** — `L` (relief), `O` (performance)

and "preservation is promotion, not loading" stops being a slogan and becomes a count of causal channels. It is also the mechanism by which promotion satisfies the amortisation constraint: one act, three returns, paid once.

### 4.1 Identifiability: drop two parameters

`η_p w_p` and `η_o w_o` are multiplicatively confounded — four free parameters where the data supports two, and neither `η` is estimable. Impose a strict simplex with a single allocation parameter:

$$
\alpha_t=\sigma\!\left(\beta_0-\beta_L L_t+\beta_K K_t\right),
\qquad
T_{t+1}=T_t+\eta\left[\alpha_t P_t+(1-\alpha_t)O_{t-\tau}\right],
\qquad 0<\eta\le 1
$$

with `P_t` and `O_t` as **signed trust innovations**. Only two free quantities remain: total responsiveness `η` and pathway allocation `α_t`.

**Justification, stated honestly.** Chen's coefficients are conditional mixed-model slopes, not commensurable pathway weights, so they cannot be summed to test conservation — the simplex is *not* empirically established there. What Chen does establish is the authors' own interpretation: **reconfiguration, not global impairment.** Process sensitivity falls while outcome influence rises. That interpretation favours the strict simplex, and that is the whole of the warrant. Say it that way rather than implying a conservation test exists.

**Renotation warning.** The innovation form hides §2's result. It survives — if `P_t = \tilde P_t - T_t` and `O_{t-\tau} = \tilde O_{t-\tau} - T_t`, the fixed point is still `T^\* = α\tilde P + (1-α)\tilde O`, so miscalibration is still `(1-α)(\tilde O - \tilde P)`. Restate it explicitly wherever the innovation form is used, or the headline identity quietly disappears.

**If you keep a separate sensitivity term** `ΔT_t = η r_t[α_t P_t + (1-α_t)O_{t-τ}]`, then `η` and an unrestricted `r_t` are scale-confounded again. Anchor `r_t = 1` at the low-load reference condition rather than fixing `η = 1` — the latter forces full updating in a single step, which is substantively wrong.

---

## 5. `τ` deserves its own analysis, and it is a figure

`τ` does not appear in `T*`. It governs whether the system converges to `T*` at all — which is `sim_oscillator_conditions` Condition 2 arriving from the trust side.

For the linearised scalar delay recursion `x_{t+1} = x_t − k·x_{t−τ}` the stability boundary is the standard

$$
k < 2\sin\!\left(\frac{\pi}{2(2\tau+1)}\right) \;\approx\; \frac{\pi}{2\tau}\ \ (\tau \text{ large})
$$

with `k = η w_o`. So **the tolerable outcome-channel gain falls roughly as 1/τ**: `τ=0 → k<2`, `τ=1 → k<1`, `τ=5 → k<0.29`. A practitioner whose outcomes land in quarters has almost no tolerable gain on the outcome channel — which is a precise statement of why professional settings are structurally worse than every setting in the cited literature, and why shortening the lag is an intervention that improves no term in the model yet changes everything.

Verify numerically in the existing sim rather than quoting the closed form; the full system is not scalar. **The stability boundary in `(η w_o, τ)` is the figure.**

---

## 6. Smaller fixes

| # | issue | fix |
|---|---|---|
| 1 | `1{Evolve_t}` is redundant with `H_t = 0` — and makes the system non-differentiable exactly where you want comparative statics | drop the indicator; `π(Z_t, 0) = 0` already does the work. `H_t ≥ 0` is the decision variable, under the capacity constraint the sim already has |
| 2 | `P_t = p(Z_t, Π_t)` double-counts: `Π_t = π(Z_t, H_t)`, so `Z` enters twice | `P_t = p(Z_t, H_t)`. Promotion and evidence-generation are two outputs of the same act, not one causing the other — you get the evidence *by* doing the promoting |
| 3 | `Z_t` is exogenous and undefined | make it a design variable: `Z_t = z(\text{harness}, q_t)`. `Z` is what tooling buys — it is the definition/detection channels, and it is exactly the **tool-side vs practitioner-side** axis. Harness becomes an experimental arm |
| 4 | `Λ` is costless, so a maximiser always loads maximally | **keep it costless.** The harm should be pure opportunity cost via `∂g/∂Λ < 0`. "Loading is locally optimal and globally harmful" is a far stronger claim than "loading has hidden costs" |
| 5 | `δ_C` is passive decay, not review | uniform decay treats a *wrong* standard exactly like an unused one — and an `ALWAYS`-loaded wrong standard never decays. Either make `δ_C` depend on non-use (and show that the alarming behaviour follows), or give `C` a validity dimension so that loading low-validity content degrades `O`. The second lets store-debt be distinct from person-debt |
| 6 | notation collision | `δ_C` here vs `δ` (debt accrual) in the sim; `S_t` is undefined and, if it is sovereignty, is near-collinear with `K^{obs,u}` — pin it or drop it |
| 7 | `D_t` now appears nowhere else | that is correct and worth saying out loud: **`D` is diagnostic output, not dynamics.** It is literally the instrument's readout. `K^{obs,u}` carries the dynamics |
| 8 | `ℓ` is monotone in `Λ` | over-loading raises load (irrelevant context, more surface to check). If you want the model to say anything about context hygiene, `ℓ` is U-shaped in `Λ`. Optional for v2 |

---

## 7. Consolidated system

**Design variables / arms:** harness (sets `Z`), `q_t` (task), `U_t` (probe occasions). `H_t` and `R_t` are *behaviours*, not assignments — both are measured.

$$
\begin{aligned}
Z_t &= z(\text{harness},q_t) && \text{session observability} \\
\Lambda_t &= \lambda(C_t,q_t) && \text{automatic loading, no contemporaneous penalty} \\
H_t &= \sigma\!\left(\theta_0-\theta_T T_t-\theta_L L_t-\theta_\rho\rho+\theta_Z Z_t\right) && \text{promotion effort} \\
R_t &= r(T_t,L_t,\Lambda_t,Z_t),\qquad \tfrac{\partial r}{\partial \Lambda}<0 && \text{independent reasoning (= solo share)} \\
\Pi_t &= \pi(Z_t,H_t),\qquad P_t=p(Z_t,H_t),\qquad \pi(Z,0)=p(Z,0)=0 \\
C_{t+1} &= (1-\delta_C)C_t+\Pi_t \\
L_t &= \ell(q_t,S_t,\Lambda_t) \\
O_t &= o(q_t,S_t,K_t,\Lambda_t) \\[2mm]
K_{t+1} &= (1-\delta_K)K_t+\gamma\,g(R_t,H_t) && \text{latent capability} \\
K^{obs,u}_t &= m(K_t,U_t)+\nu_t && \text{measurement — probe-dependent} \\
D_t &= K^{*,u}_t-K^{obs,u}_t && \text{readout, not state} \\[2mm]
\alpha_t &= \sigma\!\left(\beta_0-\beta_L L_t+\beta_K K_t\right) && \text{pathway allocation — latent }K \\
T_{t+1} &= T_t+\eta\left[\alpha_t P_t+(1-\alpha_t)O_{t-\tau}\right], \qquad 0<\eta\le 1
\end{aligned}
$$

No hand-supplied Evolve indicator. Trust and load endogenously suppress promotion. Promotion and process evidence are siblings of one act. Loading is locally free and harms only by displacement. Promotion contributes to capability separately from independent reasoning.

## 8. What this makes the empirical programme

`T^\* - P = w_o(O-P)` says what to measure: the gap between how well things went and how well the process warranted, and the weight on each. Chen et al. already control AI correctness independently of outcome, which is exactly the manipulation that separates them.

**The extension study:** reproduce Chen's load manipulation, add two externalisation arms that dissociate the paths the old `w_p(L_t,E_t)` conflated — one that raises `Z` while *adding* load, one that reduces load without raising `Z` — and measure whether `w_o(O−P)` shrinks in the first. If the thesis is right, the load-adding arm still improves calibration.

That is a small, fast study inside a conversation that opened this year, and it tests the one claim nobody has tested.

---

## 9. Diagram — demotion without new geometry

You are right that demotion/expiry/review do not fit as new objects. They do not need to be new objects: **demotion is the cascade running backwards.** A standard that stops holding becomes general reference, becomes project reference, goes.

So the two existing cascade arrows become double-headed — `marker-start="url(#mcR)"` on the lines already drawn at `x = ST_X + 46`. The `mcR` marker already exists, it is the same idiom the human-tracking arrows use, no new lines, no crossings, and templates correctly stays outside it.

Built as `diagrams/exec-fn-ai-org_2026-08-28-demotion.svg` (one-line diff from `build-exec-fn-ai-org.py`) if you want to look at it before deciding.

What it cannot show is store *validity* — §6.5. That may genuinely have no home on this diagram, and may be right to leave in the model only.

---

## 10. Changelog — v2 → v3

| change | why |
|---|---|
| `∂g/∂Λ < 0` removed; `R_t` added as a state with `∂r/∂Λ < 0` | Wu's predictor is solo share, not request frequency — `α_usage` posterior mean 0.0004 once initial ability and solo share are controlled, and the solo-share coefficient is explicitly associational. v2 overclaimed the source |
| measurement equation `K^{obs,u} = m(K_t,U_t)+ν_t` added; `α_t` takes **latent** `K_t` | the model lacked a link to data. It did *not* have an illegal-observation problem — capability causes the weighting, it is not observed by the agent |
| strict simplex with single `α_t`, innovation form | drops two unidentifiable parameters. Warranted by Chen's *interpretation* (reconfiguration), not by a conservation test their coefficients cannot support |
| `Π → K` retained but decoupled from Wu | promotion contributes via `g`'s second argument; that arm is our hypothesis, not Wu's finding |

**Open, and unresolved:** whether `Z` needs to be a vector `(Z^{tool}, Z^{practice})`. The concern is real — v2 conflated *what the harness makes observable* with *who does the intervening* — but as proposed `Z^{practice}` duplicates `H`, and they would be collinear in exactly the way §3.1a warns about. The simpler resolution is that `Z` stays scalar and tool-side while `H` is practitioner-side, which is also what makes them a clean factorial in the design. Decide before the protocol is written.
