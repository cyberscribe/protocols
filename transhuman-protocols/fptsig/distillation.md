---
title: "SIGFPT reference distillation"
source: roam-export-fptsig
collected: 2026-05-08
status: distillation
purpose: "Lens-scored review of references extracted from the Formal Protocol Theory SIG Roam graph. Read this to decide which items to promote into read-and-review/ for individual processing."
related:
  - references.md                # thematic grouping (sibling)
  - urls-with-context.txt        # raw URL list with citing-line context (sibling)
  - ../feeds/brief.md            # lens definitions (criteria 1–7)
tags: [sigfpt, roam, protocol-theory, distillation]
---

# SIGFPT reference distillation

Each entry below is scored against the relevance criteria in `feeds-brief.md`.
The reason field names the criterion (1: protocol/practice articulated; 2: failure mode; 3: PI scaffolding; 4: PI surfaces directly; 5: adjacent practitioner under AI; 6: cultural/cognitive critique). Citations point back to the SIG page where the reference appears so you can recover context.

The set is deliberately strict — items present in the Roam graph but with no substantive connection to the human–AI collaboration thesis are pushed to `low` or `reject`, not promoted into the medium tier.

---

## Promotion shortlist

The fifteen entries most worth pulling into `read-and-review/` next. All are `high` and have either an articulated practice (criterion 1) or a documented failure mode (criterion 2).

1. Manheim & Garrabrant — *Categorizing Variants of Goodhart's Law*
2. Hollnagel — *The ETTO Principle*
3. Daston — *Rules: A Short History of What We Live By*
4. Leibo et al. — *Autocurricula and the Emergence of Innovation* (manifesto)
5. Theraulaz & Bonabeau — *A Brief History of Stigmergy*
6. Parunak — *A Survey of Environments and Mechanisms for Human-Human Stigmergy*
7. Iverson — *Notation as a Tool of Thought*
8. Mike Travers — *Protocols* index (hyperphor.com/ammdi)
9. Asparouhova — *The Kafka Index*
10. Drexler & Miller — *Agoric Open Systems*
11. Kornfeld & Hewitt — *The Scientific Community Metaphor*
12. Lynch (2002) — protocols-as-proxies-for-practice
13. Hewitt — *Offices Are Open Systems*
14. Heylighen — *Stigmergy as a Universal Coordination Mechanism*
15. *The Unreasonable Sufficiency of Protocols* (Summer of Protocols)

---

## High tier

### Failure modes & pathologies (criterion 2)

> **Manheim, D. & Garrabrant, S. — *Categorizing Variants of Goodhart's Law***
> arXiv:1803.04585. https://arxiv.org/abs/1803.04585
> *Tier:* high · *Reason:* criterion 2 — formal taxonomy of metric-gaming failures, directly applicable to protocol design where any measured criterion can be optimised against. Foundation for talking about alignment failure in a transhuman-protocols frame.
> *Cited in:* `Integration Jigsaw: Convergence~Divergences between groups.md`
> *Tags:* failure-modes, alignment, metrics

> **Hollnagel, E. — *The ETTO Principle: Efficiency-Thoroughness Trade-Off***
> Book / framework. (No SIG-supplied URL.)
> *Tier:* high · *Reason:* criterion 2 — names the universal trade-off agents make between throughput and care. Direct human–AI parallel: protocols mediate where on the ETTO curve the collaboration sits, and the trade-off is *the* thing to surface.
> *Cited in:* `Group 4 insights.md`
> *Tags:* failure-modes, resilience-engineering, trade-offs

> **Witsenhausen counterexample**
> https://en.wikipedia.org/wiki/Witsenhausen%27s_counterexample · slide deck https://cermics.enpc.fr/~delara/exposes/Game_models_with_information.pdf
> *Tier:* high · *Reason:* criterion 2 — canonical impossibility result in decentralised stochastic control. Why "obvious" coordination problems can be intractable; useful counter to over-confident protocol claims.
> *Cited in:* `Impossibilities and Symmetries.md`
> *Tags:* failure-modes, impossibility, control-theory

### Articulated protocols & practices (criterion 1)

> **Leibo, J. Z., Hughes, E., et al. — *Autocurricula and the Emergence of Innovation from Social Interaction: A Manifesto for Multi-Agent Intelligence Research***
> DeepMind, arXiv:1903.00742. https://arxiv.org/pdf/1903.00742
> *Tier:* high · *Reason:* criterion 1 — articulates the practice of designing learning environments such that protocols (strategies, norms) emerge from agent interaction rather than being hand-coded. Direct substrate for "protocols evolving with AI" framing.
> *Cited in:* `Autocurricula.md` (April 3 2026 SIG session)
> *Tags:* multi-agent, emergent-protocols, autocurricula

> **Hewitt, C. — Actor model corpus**
> Mike Travers' index https://hyperphor.com/ammdi/Carl-Hewitt#54454
> *Tier:* high · *Reason:* criterion 1 — the original "protocolised computation" frame. Agents as opaque message-passing units with private state; supervisor hierarchies; nondeterminism as feature. Underpins MCP, agent SDKs, and how transhuman work is *implemented* today.
> *Cited in:* `Ontology and Politics.md`, `Actor Models.md`, `Actor Models Dec 12 session transcript.md`
> *Tags:* actor-model, agents, computational-history

> **Kornfeld, W. & Hewitt, C. — *The Scientific Community Metaphor***
> MIT AI Memo 641. https://bitsavers.trailing-edge.com/pdf/mit/ai/aim/AIM-641.pdf
> *Tier:* high · *Reason:* criterion 1 — agents organised on the model of a scientific community: proposals, confirmation, no central authority. A fully-worked transhuman-collaboration protocol from 1981 that still reads as live.
> *Cited in:* `Actor Models.md`, `Actor Models Dec 12 session transcript.md`
> *Tags:* actor-model, epistemics, multi-agent

> **Hewitt, C. — *Offices Are Open Systems***
> Foundational paper. (No direct URL in SIG; widely indexed.)
> *Tier:* high · *Reason:* criterion 1 — frames human organisations as concurrent, asynchronous, decentralised actor systems. Protocols-for-orgs lineage that pre-dates the current human–AI conversation by decades.
> *Cited in:* `Actor Models Dec 12 session transcript.md`
> *Tags:* actor-model, organisations, coordination

> **Drexler, E. & Miller, M. — *Agoric Open Systems***
> Foundational paper. (Followed by Travers as protocol-relevant.)
> *Tier:* high · *Reason:* criterion 1 — market mechanisms inside computational architecture; institutions as abstraction boundaries. Direct relevance for thinking about protocols that mediate between human and AI economies of attention/work.
> *Cited in:* `Actor Models Dec 12 session transcript.md`
> *Tags:* market-mechanisms, computational-economics, abstraction-boundaries

> **Travers, M. — *Protocols* (and *Protocols∕Actors*, *Protocols∕Ideas*)**
> https://hyperphor.com/ammdi/Protocols
> *Tier:* high · *Reason:* criterion 1 + criterion 6 — Travers' working notes on protocols cover both the formal-actor lineage and the human side (rituals, social interaction, procedural epistemology). Live and idiosyncratic; rare combination.
> *Cited in:* `SIGFPT Member Directory.md`, `Actor Models.md`
> *Tags:* protocol-theory, ritual, epistemics

> **Theraulaz, G. & Bonabeau, E. — *A Brief History of Stigmergy***
> https://www.researchgate.net/publication/12680033
> *Tier:* high · *Reason:* criterion 1 — primary reference for indirect coordination through environmental marks. Quantitative (pheromone gradients) vs qualitative (structural cues) stigmergy. Applies cleanly to AI agents leaving traces in shared codebases / file systems / KGs.
> *Cited in:* `Stigmergy.md` (May 1 2026 SIG session)
> *Tags:* stigmergy, indirect-coordination, multi-agent

> **Parunak, H. V. D. — *A Survey of Environments and Mechanisms for Human-Human Stigmergy***
> https://www.abcresearch.org/abc/papers/E4MAS05HHS.pdf
> *Tier:* high · *Reason:* criterion 1 — generalises insect-origin stigmergy to human systems (markets, Wikipedia, status boards, web). Marker-based vs sematectonic distinction is directly useful vocabulary for human–AI shared workspaces.
> *Cited in:* `Stigmergy.md`
> *Tags:* stigmergy, indirect-coordination, social-systems

> **Heylighen, F. — *Stigmergy as a Universal Coordination Mechanism***
> https://pespmc1.vub.ac.be/Papers/Stigmergy-varieties.pdf · plus the substack primer https://francisheylighen.substack.com/p/stigmergy-the-most-important-concept
> *Tier:* high · *Reason:* criterion 1 — strongest "universal mechanism" claim; useful counter-frame to message-passing-only views of agent coordination.
> *Cited in:* `Stigmergy.md`
> *Tags:* stigmergy, coordination-theory

> **Iverson, K. — *Notation as a Tool of Thought***
> Turing Award lecture. https://www.eecg.utoronto.ca/~jzhu/csc326/readings/iverson.pdf
> *Tier:* high · *Reason:* criterion 1 — argues that notation is not display but cognition, and that good notation is the precondition for good thinking. Bedrock for any "protocols make collaboration legible" argument.
> *Cited in:* `Notation.md`
> *Tags:* notation, cognition, thinking-tools

> **OpenAI — *Emergent Tool Use from Multi-Agent Autocurricula***
> https://openai.com/index/emergent-tool-use/
> *Tier:* high · *Reason:* criterion 1 — empirical demonstration of emergent strategies / proto-protocols arising from multi-agent training. Reaches further than any specific protocol artefact: shows the conditions under which protocols *generate themselves*.
> *Cited in:* `Autocurricula.md`
> *Tags:* multi-agent, emergent-behaviour, empirical

### PI scaffolding (criterion 3)

> **Daston, L. — *Rules: A Short History of What We Live By***
> Princeton UP. https://press.princeton.edu/books/hardcover/9780691156989/rules
> *Tier:* high · *Reason:* criterion 3 — the thick / thin rule distinction is core vocabulary; thick rules require judgement and context, thin are low-discretion rigidity. Lets you talk about *which kind* of protocol a given human–AI handoff needs.
> *Cited in:* `Design Principles for Protocols.md`
> *Tags:* protocol-theory, history, judgement

> **Asparouhova, N. — *The Kafka Index***
> https://summerofprotocols.com/wp-content/uploads/2024/04/Kafka-Index-Nadia-Asparouhova-1.pdf
> *Tier:* high · *Reason:* criterion 3 — checklist for assessing protocols. Practical scaffolding rather than theory; useful for any protocol-quality argument in the pitch.
> *Cited in:* `Protocols and Drift.md`
> *Tags:* protocol-quality, checklist, practical

> ***The Unreasonable Sufficiency of Protocols***
> https://summerofprotocols.com/research/the-unreasonable-sufficiency-of-protocols
> *Tier:* high · *Reason:* criterion 3 — Summer of Protocols position study; sets the frame the SIG operates inside.
> *Cited in:* `Design Principles for Protocols.md`
> *Tags:* protocol-theory, sop-corpus

> **Lynch, M. (2002) — protocols as proxies for practice, always open to interpretation**
> Citation only; ethnomethodological STS frame.
> *Tier:* high · *Reason:* criterion 3 + criterion 6 — single-line position that names the gap between specified protocol and lived practice. Powerful counter when discussing AI-assisted "protocol compliance".
> *Cited in:* `Woodenman Group 2 - To Break or Not to Break the Protocol.md`
> *Tags:* sts, ethnomethodology, practice-theory

> ***One Tension to Rule Them All***
> https://protocolized.summerofprotocols.com/p/one-tension-to-rule-them-all
> *Tier:* high · *Reason:* criterion 3 — surfaces a single load-bearing tension as a protocol-design lens. Direct citable framing.
> *Cited in:* `Woodenman Group 1: There's Plenty of Rules at the Bottom.md`
> *Tags:* protocol-design, tension-curves

> **Chambliss, D. — *The Mundanity of Excellence***
> https://academics.hamilton.edu/documents/themundanityofexcellence.pdf
> *Tier:* high · *Reason:* criterion 3 — "design for mundanity" principle; excellence as accumulation of unspectacular routines. Direct relevance for what GTD-evolution-under-AI looks like in practice.
> *Cited in:* `Design Principles for Protocols.md`
> *Tags:* practice-design, routine, excellence

### PI surfaces directly (criterion 4)

> **The SIGFPT corpus itself**
> All pages in `fptsig-roam/`. Major hubs: `Talk — Towards a Formal Theory of Protocols.md`, `Protocol Foundations Workshop.md`, `Atomic Protocol Questions.md`, `Protocolizing Agent Space.md`, `Autocurricula.md`, `Stigmergy.md`, `Protocol Homework Problem Sets.md`.
> *Tier:* high · *Reason:* criterion 4 — this is what PI is currently publishing/discussing in its formal-theory wing. Directly pitchable into.
> *Tags:* pi-internal

> **Rao, V. — *Hysteresis and the Mark Makers***
> https://contraptions.venkateshrao.com/p/hysteresis-and-the-mark-makers
> *Tier:* high · *Reason:* criterion 4 — Bourdieu lens on protocol drift; live PI thinker writing on the topic.
> *Cited in:* `Amsterdam Talk.md`
> *Tags:* venkat-rao, protocol-drift, sociology

> **Rao, V. — *Welcome to the Cosmopolis***
> https://contraptions.venkateshrao.com/p/welcome-to-the-cosmopolis
> *Tier:* high · *Reason:* criterion 4 — frame for transhuman scale of protocol coordination.
> *Cited in:* `Amsterdam Talk.md`
> *Tags:* venkat-rao, transhuman, scale

> **Hilbert's 23 Problems** (as analogue for *Atomic Protocol Questions*)
> https://www.aemea.org/math/Hilbert_23_Mathematical_Problems_1900.pdf
> *Tier:* high · *Reason:* criterion 4 — the SIG's *Atomic Protocol Questions* page explicitly mixes Hilbert + Basket of Protocols. Reading the source is the way to take the framing seriously.
> *Cited in:* `Atomic Protocol Questions.md`
> *Tags:* problem-statement, framing, foundational

---

## Medium tier

### Adjacent practitioner / formal-substrate territory (criterion 5)

> **Process calculi reading bundle (π-calculus, CSP, session types, bigraphs)**
> Aggregate of ~14 papers in `Process Calculi.md` (see `references.md` §3 for the full URL list).
> *Tier:* medium · *Reason:* criterion 5 — formal substrate for "what is a protocol mathematically?" Heavy reading; promote individual papers (Hoare's CSP, Abramsky's Milner appreciation, the multiparty session types primer) only if a specific argument calls for them.
> *Cited in:* `Process Calculi.md` (Aug 8 2025 SIG session)
> *Tags:* formal-methods, concurrency, process-calculi

> **Maneuver automata bundle (Frazzoli et al.)**
> Frazzoli, Dahleh & Feron — *Maneuver-based motion planning for nonlinear systems with symmetries* (IEEE T-RO, 2005) https://web.mit.edu/dahleh/www/pubs/2005.1.pdf — plus 6 follow-on papers.
> *Tier:* medium · *Reason:* criterion 5 — clean analogue: protocol primitives + composition rules with provable safety. Useful for arguing "protocols admit formal verification" by transfer.
> *Cited in:* `Maneuver Automata.md`
> *Tags:* formal-methods, motion-planning, primitives-composition

> **Allen, J. F. — *Allen's Interval Algebra***
> https://en.wikipedia.org/wiki/Allen%27s_interval_algebra
> *Tier:* medium · *Reason:* criterion 5 — temporal coordination primitives. Directly applicable for describing protocol timing relationships ("X during Y", overlap, before/after) in a human–AI hand-off.
> *Cited in:* `Notation.md`, `Protocol Homework Problem Sets.md`, `RCC-TIC.md`
> *Tags:* notation, temporal-logic, primitives

> **Probabilistic Graphical Models — Stanford CS228 + Wikipedia**
> https://ermongroup.github.io/cs228/ · https://en.wikipedia.org/wiki/Graphical_model
> *Tier:* medium · *Reason:* criterion 5 — notation for conditional dependence between variables. Useful when protocols need to express what each agent knows or assumes about the others' state.
> *Cited in:* `Notation.md`
> *Tags:* notation, probabilistic-models

> **Pearl, J. — *Causality* (book) + do-calculus**
> https://en.wikipedia.org/wiki/Causality_(book) · primer https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/ · paper https://ftp.cs.ucla.edu/pub/stat_ser/r402.pdf
> *Tier:* medium · *Reason:* criterion 5 — causal vocabulary; useful for distinguishing what a protocol *causes* from what it merely correlates with in collaboration outcomes.
> *Cited in:* `Do-Calculus.md`
> *Tags:* causality, methodology

> **Gintis, H. — *The Bounds of Reason: Game Theory and the Unification of the Behavioral Sciences***
> Princeton UP.
> *Tier:* medium · *Reason:* criterion 5 — game-theoretic foundation flagged inside SIG as relevant. Background reading; specific chapters (correlated equilibria, signalling) are most pertinent.
> *Cited in:* `Autocurricula.md`
> *Tags:* game-theory, behavioural-science

> **Axelrod, R. — *The Complexity of Cooperation***
> ~1999. Iterated PD; tit-for-tat as proto-protocol.
> *Tier:* medium · *Reason:* criterion 5 — the canonical empirical case for emergent protocols out of repeated interaction. Foundational, but ground well-covered by anyone doing GTD-evolution work; cite as known reference rather than pull as fresh reading.
> *Cited in:* `Autocurricula.md`
> *Tags:* game-theory, iterated-games, cooperation

> **Epstein, J. & Axtell, R. — *Growing Artificial Societies* / Sugarscape**
> https://archive.org/details/growingartificia00epst · https://en.wikipedia.org/wiki/Sugarscape
> *Tier:* medium · *Reason:* criterion 5 — agent-based modelling lodestar; useful counter-example to over-formal protocol description (rules + bottom-up emergence vs spec-then-implement).
> *Cited in:* `Woodenman Group 1: There's Plenty of Rules at the Bottom.md`
> *Tags:* agent-based-modelling, emergence

> **Couzin, I. et al. — *Collective Memory and Spatial Sorting in Animal Groups***
> https://jmvidal.cse.sc.edu/library/couzin02a.pdf
> *Tier:* medium · *Reason:* criterion 5 — hysteresis in collective behaviour; analogue for protocol stickiness once a coordination state is reached.
> *Cited in:* `Woodenman Group 1.md`
> *Tags:* collective-behaviour, hysteresis

> **Mahajan, S. — *The Art of Insight in Science and Engineering* + *Street-Fighting Mathematics* (OCW)**
> https://mitpress.mit.edu/9780262526548 · https://ocw.mit.edu/courses/18-098-street-fighting-mathematics-january-iap-2008/
> *Tier:* medium · *Reason:* criterion 5 — methodological calibration ("street-fighting" approach to formal modelling), the SIG's recommended math-level reference. Useful prep for any quantitative argument in the pitch.
> *Cited in:* `Talk — Towards a Formal Theory of Protocols.md`
> *Tags:* methodology, fermi-estimation

> **Rao, V. — Paper Napkin Math methodology (Fermi estimation + Dyson design)**
> Session writeup; no external URL. Notebooks of Fermi estimates and order-of-magnitude design moves.
> *Tier:* medium · *Reason:* criterion 5 — methodological practice for protocol estimation. Light, transferable.
> *Cited in:* `Paper Napkin Math.md`
> *Tags:* methodology, fermi-estimation, sop-method

### Cultural / cognitive critique (criterion 6)

> **Latour, B. — Actor Network Theory**
> Body of work; no SIG-supplied URL.
> *Tier:* medium · *Reason:* criterion 6 — bottom-up view of how social structures emerge from networks of human and non-human actors. Useful counter-vocabulary when "protocol" risks being read as top-down imposition.
> *Cited in:* `Actor Models Dec 12 session transcript.md`
> *Tags:* sts, social-theory, actor-network-theory

> **Crouch, D. — *The Chivalric Turn***
> Book.
> *Tier:* medium · *Reason:* criterion 6 — early-medieval code as a protocol case study. Useful historical depth; one example among many.
> *Cited in:* `Early Medieval Code.md`
> *Tags:* historical, codes-of-conduct

> **Koolhaas, R. — *Junkspace***
> Essay.
> *Tier:* medium · *Reason:* criterion 6 — the "junkshake" example: handshakes losing meaning under runaway protocols. Compact metaphor for protocol decay under AI scale.
> *Cited in:* `Group 2 insights.md`
> *Tags:* metaphor, protocol-decay

> **Woodside, A. — *Lost Modernities***
> Book; flagged as next-step reading.
> *Tier:* medium · *Reason:* criterion 6 — non-Western protocol traditions; broadens the corpus of what "good protocol" can look like.
> *Cited in:* `List of projects | Protocol School September 02025.md`
> *Tags:* historical, non-western-traditions

> **Ghosh, A. — *The Great Derangement: Climate Change and the Unthinkable***
> https://en.wikipedia.org/wiki/The_Great_Derangement:_Climate_Change_and_the_Unthinkable
> *Tier:* medium · *Reason:* criterion 6 — argument about literary fiction's failure to model archetypes / non-individual scales. Indirect but cited inside SIG; relevant if pitch touches narrative or the limits of human-only sense-making.
> *Cited in:* `PFW Idea Index.md`
> *Tags:* narrative, scale, critique

---

## Low tier (touches topic, lacks transferable substance for this thesis)

> **Causality literature beyond Pearl primer**
> Only the primer + book entry justify scoring; deeper causal-inference reading is well outside SIG's actual use.
> *Reason:* criterion 7

> ***Civilized by Television: How television made sports spectatorship safer***
> One-off SIG case study; vivid but not generalisable to human–AI work.
> *Reason:* criterion 7

> **Stockhausen — *Prozession* meta-notation**
> Notation curiosity; cite if writing about graphical protocol notation specifically, otherwise drop.
> *Reason:* criterion 7

> **I²C protocol pedagogy (SparkFun, PlayWithCircuit)**
> Hardware-protocol tutorials. Ground-floor; not transferable.
> *Reason:* criterion 7

> **Junkspace cluster beyond the single Koolhaas reference**
> One reference is enough; further architectural-protocol-decay material would be over-collection.
> *Reason:* criterion 7

> **Ghosh + literary-fiction-and-archetype thread beyond the single citation**
> Already used at the level the SIG uses it; deeper engagement should come through Robert's poetry-protocols line, not via this catalogue.
> *Reason:* criterion 7

---

## Reject

> **Image, video, and admin URLs**
> Firebase image storage, Discord/Zoom/Excalidraw rooms, Granola/Gist/ChatGPT/Claude shared chats, Google Drive working files. Already filtered out of the URL list.
> *Reason:* not source material.

> **Hao Guang Tse poetry-venue links** (Grotto Journal, Basket Magazine, Misery Tourism, Whitedust)
> Tangential to the SIG; relevant to your separate poetry-protocols line, not the human–AI thesis. Live there if anywhere.
> *Reason:* off-thesis for this catalogue.

> **Any source already in feeds-config.json**
> If a SIG-cited source appears here that already runs in the recurring feed (e.g. a Venkat Rao post), that path is the right one — no need to also have it in `read-and-review/` from this distillation.
> *Reason:* duplicate surface.

---

## Notes

The set is biased toward the **stigmergy + actor-model + autocurricula** triad because these are the SIG's three live formal substrates for "what is a protocol?" and each maps cleanly to a human–AI collaboration concern (shared environment as coordinator; agents as opaque message-passing units; protocols as emergent rather than pre-specified).

The single tightest fit for your pitch may be the **Hollnagel ETTO + Manheim/Garrabrant Goodhart + Daston thick/thin** triad — three lenses that each bear directly on what makes a human–AI collaboration protocol *good* rather than just operational.

If you want to actually populate `read-and-review/`, the natural next move is to spin up files for the fifteen items in the promotion shortlist above. Each becomes a `2026-05-08-{source-slug}.md` per `CONVENTIONS.md`, with the body either clipped (where the source is openly fetchable) or stubbed with the citation and "fetch on read" note.
