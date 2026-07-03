# What Holds Up the "Knowledge Collapse" Argument

### A cross-disciplinary audit of the load-bearing assumptions in Acemoglu, Kong & Ozdaglar (2026), *AI, Human Cognition and Knowledge Collapse* (NBER w34910)

*Prepared for the Transhuman Protocols research thread, June 2026.*

---

## Why this audit

The paper's striking conclusion — that accurate agentic AI can improve every individual decision while quietly destroying the collective knowledge those decisions depend on — is not so much *derived* as *located*. The mathematics characterises thresholds and dynamics, but the qualitative result is largely pre-loaded into a handful of structural premises. The question worth asking, then, is not "is the math right?" (it appears to be) but "must we accept these premises, and does anything outside economics vouch for them?"

This document takes the eight most load-bearing assumptions, maps each to the scholarship that would justify or undermine it across cognitive science, philosophy, anthropology, organisational learning, labour economics, human factors, and the AI literature itself, and renders a candid verdict on how well each holds.

The headline: **most of the structure is unusually well-grounded across fields — strikingly so for an economic model — but the two assumptions that turn a steady-state *tax* into an irreversible *trap* are its weakest, and the most realistic AI dynamics live in an extension rather than the baseline.**

---

## Verdict at a glance

| # | Assumption | What it does in the model | Cross-field support | Verdict |
|---|------------|---------------------------|---------------------|---------|
| 1 | Knowledge cleaves into *general* vs *context-specific* | The foundational ontology | Economics, philosophy, KM, anthropology converge | **Strong** |
| 2 | Economies of scope: one effort jointly makes private skill + public knowledge | Creates the externality channel | Learning-by-doing, spillovers, schema induction | **Moderate–strong** |
| 3 | Strict complementarity (∆I = 0): specific knowledge worthless without general | Makes collapse *catastrophic* | Expertise & theory-ladenness support *complementarity*; not *strictness* | **Directionally strong, strict form overstated** |
| 4 | Agentic AI substitutes for learning effort (crowd-out) | The erosion mechanism | Cognitive offloading + a clean causal RCT | **Strong, but design-contingent** |
| 5 | The learning externality is largely *uninternalized* | Drives the wedge from social optimum | Free-rider theory yes; reputation/intrinsic motive complicate | **Moderate; overstated in strong form** |
| 6 | Knowledge is collective and *can be lost*; aggregation capacity *I* governs resilience | The collapse precedent + the policy lever | Cultural-evolution evidence is the best parallel | **Strong (with a non-monotonicity caveat)** |
| 7 | Knowledge depreciates (random-walk common state) | Forces continual replenishment | Mainstream in labour econ + org learning | **Strong** |
| 8 | Effort is highly elastic (ε > 4) | *Necessary* for a stable collapse trap | Best analogue (Frisch ≈ 0.15–0.5) is ~10× too small | **Weak / partly contradicted** |
| — | (Baseline) AI accuracy decoupled from the commons it consumes | Lets AI stay good while the commons dies | Model-collapse literature says coupled | **Contested idealization** |

---

## 1. The two-types ontology — *general vs context-specific knowledge*

**Role.** Everything rests on this carve: a shared, cumulative common state (general knowledge) and a private, idiosyncratic state (context-specific knowledge).

**The support is broad and, in one case, almost verbatim.** Hayek's *The Use of Knowledge in Society* (AER, 1945) draws exactly this line: against "knowledge of general rules" he sets "the knowledge of the particular circumstances of time and place" — dispersed, individual, usable only by the person in those circumstances. That is the model's binary, eighty years early. The same cut recurs independently in philosophy (Ryle's *knowing-how* vs *knowing-that*, 1949; Polanyi's tacit vs explicit, 1958/1966), in knowledge management (Nonaka & Takeuchi's SECI model, 1995, which not only assumes the binary but formalises conversions between the poles), and in learning anthropology (Lave & Wenger's situated knowledge, 1991).

**Where it frays.** The *binary* is contested even if the *distinction* is not. Harry Collins (*Tacit and Explicit Knowledge*, 2010) shows "tacit" hides at least three phenomena with very different transferability — so "context-specific knowledge" is not one thing. The Stanley & Williamson "intellectualism" revival (*J. Philosophy*, 2001) argues knowing-how reduces *to* knowing-that, attacking the cleanness of the split. And Polanyi himself held that *all* knowledge is rooted in the tacit — which undercuts a tidy partition. None of this sinks the model; it suggests the two-type carve is a defensible idealisation of what is really a spectrum or a finer taxonomy.

**Verdict: Strong.** The best-supported assumption in the set, with Hayek as a near-exact anchor.

---

## 2. Economies of scope — *one effort jointly produces private skill and public knowledge*

**Role.** This is the engine of the whole result. Because a single act of learning yields both your private signal *and* a thin contribution to the commons, anything that substitutes for the private motive (AI) collaterally starves public production.

**Support assembles from three literatures.** Arrow's learning-by-doing (1962) gives the exact economic precedent: learning is a by-product of experience and "an act of investment that benefits future investors" — joint production with a positive externality, stated outright. Jaffe, Trajtenberg & Henderson (QJE, 1993) supply the empirical bedrock that such knowledge genuinely spills (patent citations localise geographically). And cognitive science supplies the micro-mechanism by which working specific cases yields general structure: Gick & Holyoak's schema induction (1983) — two worked analogues let people abstract a transferable schema; Sweller's worked-example effect in the same spirit.

**Where it frays.** The cognitive literature's own caution is that the general by-product is *frequently inert*. Gick & Holyoak (1980) is famous precisely for showing people routinely *fail* to spontaneously transfer a relevant analogue without a hint. The spillover also requires absorptive capacity in the receiver (Cohen & Levinthal, 1990), limiting the pure public-good reading; and the magnitude/localisation of spillovers is debated (Thompson & Fox-Kean, AER, 2005). So the joint-production-as-single-act framing is a sound synthesis across fields rather than one tested proposition, and its weakest link is that the public by-product is real but does not generalise automatically.

**Verdict: Moderate–strong.** Each leg is well-grounded; the synthesis is plausible; the caveat is that "thin public contribution" is fragile, not automatic.

---

## 3. Strict complementarity — *∆I = 0, specific knowledge useless without general*

**Role.** This is what makes collapse a catastrophe rather than a cost: when general knowledge dies, the AI's excellent personalised advice becomes useless too.

**The complementarity is strongly supported; the strictness is not.** The directional claim — local data is far more valuable inside a general framework — is among the most robust findings in cognitive science and philosophy of science. Chase & Simon's chess studies (1973): experts reconstruct *real* boards far better than novices, but the advantage *vanishes on random boards* — specific perceptual input is only usable through an organised store of general patterns. Theory-ladenness (Hanson 1958; Kuhn 1962): observation without a framework is not coherent observation. Medical "illness scripts" and knowledge encapsulation (Schmidt & Boshuizen): patient-specific findings are interpreted only against general scripts.

**Where it frays.** The literature supports strong complementarity, not literal *zero* value. Even novices extract some signal; the chess advantage collapses to *novice level*, not to nothing. Theory-ladenness has empiricist critics. And the rival "two-worlds" theory in medicine holds that routine expert diagnosis often runs on pattern recognition with biomedical theory "rarely used," implying specific data can be acted on with thin general knowledge in routine cases. So ∆I = 0 is a modelling idealisation past the evidence; ∆I small-but-positive is the empirically honest version (and would soften, not eliminate, the collapse).

**Verdict: Directionally strong, strict form overstated.**

---

## 4. AI as substitute for effort — *the crowd-out mechanism*

**Role.** Agentic recommendations supply what effort was for, so people exert less, and the foregone effort would have built (and spilled over) knowledge.

**This now has a clean causal anchor.** The single most important study is the Bastani et al. RCT (~1,000 Turkish high-schoolers; *PNAS*, 2025, also circulated as "Generative AI Can Harm Learning"). Unrestricted GPT access *raised* practice performance (+48%) but, once removed, those students scored **~17% worse than controls** on the unaided exam — answer-serving AI as a crutch that suppressed skill acquisition. Crucially, a guardrailed "tutor" version that withheld answers and gave Socratic hints **eliminated the harm**. That is the model's assumption confirmed almost exactly — *and* its boundary condition named.

The mechanism is corroborated across fields: cognitive offloading (Sparrow et al., *Science*, 2011 — the "Google effects" / saving-induced forgetting; Storm & Stone's self-reinforcing "reliance effect"), the generation effect (Slamecka & Graf, 1978) and desirable difficulties (Bjork) as the deep reasons effort builds durable knowledge, automation complacency that resists training (Parasuraman & Manzey, 2010; Bainbridge's "Ironies of Automation," 1983), and a neural correlate in spatial cognition (Maguire's London cabbies; Dahmani & Bohbot, 2020, where habitual GPS use predicts *steeper* spatial-memory decline). AI-specific signals — the MIT "Your Brain on ChatGPT" EEG study (Kosmyna et al., 2025), the ~25% Stack Overflow contribution drop (del Rio-Chanona et al., *PNAS Nexus*, 2024), Wikipedia viewership declines (Lyu et al., 2025), and "metacognitive laziness" (Fan et al., *BJET*, 2025) — all point the same way.

**Where it frays.** The relationship is **design-contingent**, not intrinsic. The same Bastani study, plus Kestin et al.'s Harvard physics tutor (2024, >2× learning gains), shows AI engineered to *withhold* answers and scaffold effort flips from substitute to complement. Much of the correlational "AI erodes thinking" literature (e.g. Gerlich, 2025) cannot rule out reverse causation. And offloading is often adaptive — freed capacity improves other tasks (Storm & Stone, 2015). *Caveat for the citation trail:* the paper's own "Budiyono et al. (2025)" could not be independently confirmed, and two of the supporting empirical papers (Lyu; the Wikipedia work) are co-authored by the model's authors, so they are not independent corroboration.

**Verdict: Strong, but design-contingent.** The crowd-out is real for *unrestricted, answer-serving* AI — exactly the case the model targets — yet the substitute/complement status is endogenous to how the tool is built, which the model treats as fixed.

---

## 5. The uninternalized externality — *free-riding on a knowledge commons*

**Role.** Private contributions to general knowledge go uncaptured, so the market undersupplies the commons and AI deepens the shortfall.

**The floor is solid.** Olson's *Logic of Collective Action* (1965) is this assumption in classical form: rational agents undersupply public goods absent selective incentives, worse in large groups. Public-goods experiments confirm the dynamic empirically — contributions start moderate and *decay* toward free-riding without punishment (Fehr & Gächter; Ledyard's survey). Knowledge specifically is a recognised commons (Hess & Ostrom, 2007).

**Where it frays — substantially.** The strong form ("largely uninternalized") is the part most contradicted by modern evidence. Lerner & Tirole's "Simple Economics of Open Source" (2002) shows contributors capture private returns via reputation and career signalling; Lakhani & Wolf (2005) document intrinsic motivation as the dominant driver; Benkler's commons-based peer production (2002/2006) shows enormous public knowledge produced despite the free-rider logic; reputation systems (Stack Overflow karma, badges) are engineered precisely to internalise contribution; and Ostrom's life work shows communities routinely *solve* commons dilemmas through self-governance. The honest framing is *partial* internalisation → underprovision relative to the optimum, with the degree institution-dependent — itself a lever AI could move either way.

**Verdict: Moderate; overstated in the strong form.** Defensible as "incompletely internalised," not "uninternalised."

---

## 6. Collective knowledge that can collapse — *and the aggregation lever I*

**Role.** Two of the model's claims live here: that knowledge is collective and can vanish (the collapse warning) and that aggregation capacity *I* — connectedness, pooling, population reach — raises welfare and resilience.

**This is the paper's strongest cross-field foundation, and it comes from anthropology.** Cumulative cultural evolution gives both the cumulative-collective nature of knowledge (Tomasello's ratchet effect, 1999; Boyd & Richerson) and — decisively — *documented precedent for collapse*. Henrich's Tasmania case (*American Antiquity*, 2004): an isolated, small population lost a suite of technologies over millennia because transmission losses outran innovation below a connectivity threshold — adaptive individual behaviour producing *maladaptive collective loss*. That is the model's knowledge-collapse result, in the archaeological record. Derex et al. (*Nature*, 2013) reproduced it experimentally: smaller groups lost a complex skill that larger groups retained. And the aggregation lever has comparative and archaeological support: larger, better-connected populations carry more complex toolkits (Kline & Boyd, *Proc. R. Soc. B*, 2010; Powell et al., *Science*, 2009; the "collective brain," Muthukrishna & Henrich, 2016).

**Where it frays — and it's interesting.** Two caveats matter. First, the size→complexity *law* is empirically contested (Vaesen, Collard et al., *PNAS*, 2016): the mechanism is robust in theory, its dominance in the actual record is debated — so treat *I* as one important driver, not the sole one. Second, and more pointed: connectedness is **non-monotonic**. Derex & Boyd (*PNAS*, 2016) found *partially* connected groups out-innovated *fully* connected ones, because full connectivity caused premature convergence and killed the diversity needed for hard discoveries. This complicates the model's "more *I* is always better" — but it simultaneously hands the collapse thesis a sharper weapon: AI-driven *homogenisation* (the output-convergence already observed empirically) is precisely the mechanism by which too much aggregation could *reduce* the diversity that sustains complex knowledge. Worth foregrounding as a feature, not just a caveat.

**Verdict: Strong.** The best external validation the paper has; the one refinement is that aggregation likely has an interior optimum, not an unbounded benefit.

---

## 7. Knowledge depreciation — *the random-walk common state*

**Role.** Because the common state drifts (innovation variance Σ²), the commons must be continually replenished or it decays — which is what makes ongoing effort load-bearing.

**Mainstream across two literatures.** Human-capital and skill depreciation are standard in labour economics (Neuman & Weiss, 1995, with faster depreciation in dynamic sectors; De Grip & Van Loo's economics of skills obsolescence, 2002). Organisational forgetting is the direct empirical analogue: Argote, Beckman & Epple (*Management Science*, 1990) show organisational knowledge depreciates rapidly — cumulative output overstates retained learning. The popular "half-life of knowledge" figures (engineering, medicine) point the same way, though they're illustrative rather than rigorously estimated.

**Verdict: Strong.** Squarely consistent with established work; only the specific half-life numbers are soft.

---

## 8. High effort elasticity — *the assumption that makes the trap possible*

**Role.** This is the crux, and it deserves to be stated plainly. The model's *interesting* results — multiple steady states, path dependence, a stable collapse trap, complete collapse — exist **only** in the regime where effort is highly elastic: ε = 1/(α−1) > 4. In the low-elasticity regime you get a lower steady state, no trap. So whether catastrophic collapse is even *possible* hinges on agents cutting learning effort *very* sharply when returns dip.

**The evidence does not support an elasticity this high — and the closest analogue cuts hard against it.** The natural empirical reference is the intensive-margin labour-supply (Frisch) elasticity: how much people adjust effort when its return changes. Those estimates are *small* — Chetty's synthesis (*Econometrica*, 2012) lands around 0.15 raw / ~0.33 friction-corrected; Keane's survey (*JEL*, 2011) medians near 0.2. That is one to two orders of magnitude below the ε > 4 the trap requires. Study-effort field experiments show modest average responses with a responsive right tail — heterogeneity, not high average elasticity.

**The defence, and its limit.** A defender can fairly say learning effort is not labour hours — it may be more discretionary and elastic than prime-age work. That's legitimate, but it is an *assertion*; the best-measured analogue we have is small, and the authors themselves note institutions (medical-training minimums, sheer difficulty) push *toward* inelasticity. The recent deskilling RCTs confirm the *sign* (people cut independent effort when a tool substitutes) but never the *magnitude*.

**Verdict: Weak / partly contradicted.** The honest reading is that complete collapse is a *conditional* result — "if effort is extraordinarily elastic, then…" — rather than a grounded prediction. This is the assumption a hostile referee attacks first, and rightly.

---

## Bonus tension: is the AI really decoupled from the commons it eats?

The baseline holds agentic accuracy τ_A *fixed* even as the human commons collapses — letting the AI stay excellent while the knowledge it was trained on disappears, which is what produces the clean paradox. The model-collapse literature says this decoupling is unrealistic in the limit: recursive training on model-generated data causes irreversible quality loss (Shumailov et al., *Nature*, 2024; "self-consuming models go MAD," Alemohammad et al., 2023; "strong model collapse," Dohmatob et al., 2024). The AI's accuracy is *endogenous* to the real-data corpus.

But it's not decisive: Gerstgrasser et al. (2024) show that *accumulating* real alongside synthetic data, plus curation, bounds the error and prevents collapse — so under realistic data management τ_A can stay roughly fixed. The fair reading: the decoupled baseline is a defensible idealisation, not a robust certainty, and the paper's own synthetic-data extension (§5.2) — where collapse bottoms out at a *low-but-positive* steady state because verifiable synthetic data still generates some novelty — is the more realistic case and deserves foregrounding.

*One citation hazard worth flagging given the authorship:* the strongest "AI accelerates discovery" complement evidence used in this debate, Toner-Rodgers (2024) on AI and materials R&D, was **disavowed by MIT in May 2025** ("no confidence in the provenance, reliability, or validity of the data") and withdrawn — and Acemoglu had publicly praised it before it was discredited. The durable complement evidence is elsewhere: Brynjolfsson, Li & Raymond (*QJE*, 2025), where an AI assistant *diffused* expert tacit knowledge to novices (knowledge spread, not erosion), and AlphaFold / RFdiffusion (Jumper et al., 2021; Watson et al., 2023) as AI generating validated new science.

---

## Bottom line

If you want the minimal creed required to *believe the qualitative result*, accept assumptions **2, 3, 4, and 5** — joint production, complementarity, AI-as-substitute, and an unpriced commons. Those four are individually well-supported across multiple disciplines (with 3 and 5 needing softening from their strict forms), and together they make erosion of the commons close to definitional. Add **6 and 7** — collective knowledge that can be lost, and depreciation — and you have a mechanism with a real historical precedent (Tasmania) and mainstream economic grounding.

The argument's vulnerability is concentrated, not diffuse. It lies almost entirely in **assumption 8 (high effort elasticity)**, which the empirical record actively undercuts and which is *necessary* for the dramatic trap, and secondarily in the **decoupled-AI baseline**, which the model-collapse literature challenges and which the paper's own extension partly repairs. Strip those two and you are left with a robust, well-evidenced claim that agentic AI imposes a *steady-state tax* on collective knowledge; it is only with those two that the tax becomes an *irreversible cliff*.

The deepest irony for the Transhuman Protocols thread: the strongest scientific warrant for "knowledge can collapse" comes not from economics but from the anthropology of *pre-literate* human societies. The same connectivity-and-transmission dynamics that let isolated Tasmanians lose the bone tool may govern whether a hyper-connected, AI-mediated civilisation loses the capacity that built its tools — with the twist that *too much* connectivity (homogenisation) may be as dangerous as too little.

---

## Sources

**Knowledge ontology & complementarity**
- Hayek, F. (1945). The Use of Knowledge in Society. *American Economic Review* 35(4):519–530.
- Ryle, G. (1949). *The Concept of Mind.*
- Polanyi, M. (1958) *Personal Knowledge*; (1966) *The Tacit Dimension.*
- Nonaka, I. & Takeuchi, H. (1995). *The Knowledge-Creating Company.* Oxford UP.
- Collins, H. (2010). *Tacit and Explicit Knowledge.* Univ. of Chicago Press.
- Lave, J. & Wenger, E. (1991). *Situated Learning.* Cambridge UP.
- Stanley, J. & Williamson, T. (2001). Knowing How. *Journal of Philosophy* 98(8):411–444.
- Arrow, K. (1962). The Economic Implications of Learning by Doing. *Rev. Econ. Studies* 29(3):155–173.
- Jaffe, A., Trajtenberg, M. & Henderson, R. (1993). Geographic Localization of Knowledge Spillovers. *QJE* 108(3):577–598. [Cf. Thompson & Fox-Kean, *AER*, 2005.]
- Gick, M. & Holyoak, K. (1983). Schema Induction and Analogical Transfer. *Cognitive Psychology* 15:1–38. [Cf. 1980 on transfer failure.]
- Sweller, J. (1988). Cognitive load during problem solving. *Cognitive Science.*
- Chase, W. & Simon, H. (1973). Perception in Chess. *Cognitive Psychology* 4:55–81.
- Chi, M., Glaser, R. & Farr, M. (1988). *The Nature of Expertise.*
- Hanson, N. R. (1958). *Patterns of Discovery*; Kuhn, T. (1962). *The Structure of Scientific Revolutions.*
- Schmidt, H. & Boshuizen, H. (knowledge encapsulation / illness scripts).
- Cohen, W. & Levinthal, D. (1990). Absorptive Capacity. *Admin. Science Quarterly.*

**Cognitive offloading & deskilling**
- Sparrow, B., Liu, J. & Wegner, D. (2011). Google Effects on Memory. *Science* 333:776–778.
- Risko, E. & Gilbert, S. (2016). Cognitive Offloading. *Trends in Cognitive Sciences* 20:676–688.
- Storm, B. & Stone, S. (2015). Saving-Enhanced Memory. *Psychological Science* 26:182–188. Storm, Stone & Benjamin (2016/2017, *Memory*) — reliance effect.
- Slamecka, N. & Graf, P. (1978). The Generation Effect. *JEP:HLM* 4(6):592–604.
- Bjork, R. (1994). Desirable difficulties / "new theory of disuse."
- Parasuraman, R. & Manzey, D. (2010). Complacency and Bias in Human Use of Automation. *Human Factors* 52(3):381–410.
- Bainbridge, L. (1983). Ironies of Automation. *Automatica* 19(6):775–779.
- Maguire, E. et al. (2000). Navigation-related structural change in taxi drivers' hippocampi. *PNAS.*
- Dahmani, L. & Bohbot, V. (2020). Habitual use of GPS negatively impacts spatial memory. *Scientific Reports* 10:6310.
- Kosmyna, N. et al. (2025). Your Brain on ChatGPT. arXiv:2506.08872. [Preprint; small N.]
- del Rio-Chanona, R. et al. (2024). LLMs reduce public knowledge sharing on Q&A platforms. *PNAS Nexus* 3(9):pgae400.
- Lyu, H., Siderius, J., Li, ..., Acemoglu, D., Huttenlocher, D. & Ozdaglar, A. (2025). Wikipedia Contributions in the Wake of ChatGPT. ACM Web Conf.
- Jakesch, M. et al. (2023). Co-Writing with Opinionated Language Models Affects Users' Views. *CHI '23.*
- Gerlich, M. (2025). AI Tools and Critical Thinking. *Societies* 15(1):6. [Correlational.]
- Fan, Y. et al. (2025). Beware of Metacognitive Laziness. *British Journal of Educational Technology.*
- Bastani, H. et al. (2025). Generative AI [without guardrails] can harm learning. *PNAS* (SSRN 2024). **[Keystone causal RCT.]**
- Kestin, G. et al. (2024). AI Tutoring Outperforms Active Learning (Harvard physics). [Complement case.]
- *Unconfirmed:* "Budiyono et al. (2025)" cited in the paper could not be independently verified.

**Commons & cultural evolution**
- Olson, M. (1965). *The Logic of Collective Action.* Harvard UP.
- Hess, C. & Ostrom, E. (2007). *Understanding Knowledge as a Commons.* MIT Press. Ostrom, E. (1990). *Governing the Commons.* Cambridge UP.
- Fehr, E. & Gächter, S. (2000, *AER*; 2002, *Nature*) — public-goods contribution decay & punishment. Ledyard, J. (1995). Public Goods survey, *Handbook of Experimental Economics.*
- Benkler, Y. (2002). Coase's Penguin. *Yale Law Journal* 112(3):369–446; (2006) *The Wealth of Networks.*
- Lerner, J. & Tirole, J. (2002). Some Simple Economics of Open Source. *J. Industrial Economics* 50(2):197–234.
- Lakhani, K. & Wolf, R. (2005). Why Hackers Do What They Do. MIT Press.
- Tomasello, M. (1999). *The Cultural Origins of Human Cognition.* Harvard UP. Boyd, R. & Richerson, P. (1985, 2005).
- Henrich, J. (2015). *The Secret of Our Success.* Princeton UP.
- Muthukrishna, M. & Henrich, J. (2016). Innovation in the collective brain. *Phil. Trans. R. Soc. B* 371:20150192.
- Henrich, J. (2004). Demography and Cultural Evolution: the Tasmanian Case. *American Antiquity* 69(2):197–214.
- Powell, A., Shennan, S. & Thomas, M. (2009). Late Pleistocene Demography and Modern Human Behavior. *Science* 324:1298–1301.
- Kline, M. & Boyd, R. (2010). Population size predicts technological complexity in Oceania. *Proc. R. Soc. B* 277:2559–2564.
- Derex, M. et al. (2013). Experimental evidence for the influence of group size on cultural complexity. *Nature* 503:389–391.
- Derex, M. & Boyd, R. (2016). Partial connectivity increases cultural accumulation within groups. *PNAS* 113(11):2982–2987.
- Vaesen, K., Collard, M. et al. (2016). Population size does not explain past changes in cultural complexity. *PNAS* 113(16):E2241–E2247. [Critique.]

**Depreciation, elasticity, model collapse, complement evidence**
- Neuman, S. & Weiss, A. (1995). Schooling vintage & earnings. *European Economic Review* 39(5):943–955.
- De Grip, A. & Van Loo, J. (2002). The Economics of Skills Obsolescence. *Research in Labor Economics* 21.
- Argote, L., Beckman, S. & Epple, D. (1990). The Persistence and Transfer of Learning. *Management Science* 36(2):140–154.
- Chetty, R. (2012). Bounds on Elasticities... Labor Supply. *Econometrica* 80(3):969–1018.
- Keane, M. (2011). Labor Supply and Taxes: A Survey. *JEL* 49(4):961–1075.
- Levitt, S., List, J., Neckermann, S. & Sadoff, S. The Behavioralist Goes to School. NBER WP 18165.
- Shumailov, I. et al. (2024). AI models collapse when trained on recursively generated data. *Nature* 631:755–759 (+ 2025 Author Correction). Shumailov et al. (2023), The Curse of Recursion, arXiv:2305.17493.
- Alemohammad, S. et al. (2023). Self-Consuming Generative Models Go MAD. arXiv:2307.01850.
- Dohmatob, E., Feng, Y. et al. (2024). Strong Model Collapse. arXiv:2410.04840.
- Gerstgrasser, M., Schaeffer, R. et al. (2024). Is Model Collapse Inevitable? arXiv:2404.01413. [Counterpoint.]
- Brynjolfsson, E., Li, D. & Raymond, L. (2025). Generative AI at Work. *QJE* 140(2) (NBER WP 31161, 2023).
- Jumper, J. et al. (2021). Highly accurate protein structure prediction with AlphaFold. *Nature* 596:583–589. Watson, J. et al. (2023). De novo design with RFdiffusion. *Nature* 620:1089–1100.
- **Avoid:** Toner-Rodgers (2024), AI and materials R&D — disavowed/withdrawn by MIT (May 2025).
