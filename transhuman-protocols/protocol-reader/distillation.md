---
title: "Protocol Reader distillation"
source: protocol-reader-2025-02-04
collected: 2026-05-08
status: distillation
purpose: "Lens-scored review of the 27 essays in the Summer of Protocols *Protocol Reader* (2025). Each essay scored against feeds-brief criteria 1–7 against the human–AI collaboration thesis."
related:
  - citations.md                     # filtered bibliography (sibling: ../protocol-reader/citations.md)
  - ../fptsig/distillation.md        # SIGFPT counterpart in the same shape
  - ../feeds/brief.md                # lens definitions
tags: [sop, protocol-institute, protocol-reader, distillation]
---

# Protocol Reader distillation

The Summer of Protocols *Protocol Reader* (Ethereum Foundation, 2025; Rao / Beiko / Davis, eds.; Jenna Dixon, production) collects 27 essays plus introduction and afterword. Each essay below is scored against the same lenses as the RSS feed brief, with the human–AI collaboration thesis as the organising filter. The volume's *Consolidated Notes* citation set is filtered separately in `citations.md` (sibling).

The headline pattern: this volume reframes AI coordination as a **protocol-design problem**, not an alignment problem. Humans and AI sit inside emergent protocol systems, and effectiveness turns on rule clarity, feedback loops, role definition, and graceful failure modes — classical coordination concerns now acutely relevant under AI. Mainstream AI-ethics / alignment / LLM-safety discourse is conspicuously absent from the references, which makes this corpus a complement to the technical AI literature rather than a duplicate.

---

## Promotion shortlist

The ten essays most worth pulling into `read-and-review/` next, weighted to where they intersect the human–AI thesis hardest.

1. **Janna Tay — *A Phenomenology of Protocols*** — four-characteristic framework (stability/constraint/legitimacy/narrativity) is the cleanest direct vocabulary the volume offers.
2. **Timber Stinson-Schroff — *Safe New World*** — protocol-evolution + ETTO + slow-feedback failure mode; Timber is also a SIGFPT regular, so this is a bridge text between the two corpora.
3. **Nadia Asparouhova — *Dangerous Protocols*** — protocol-as-identity, Protocolization 1.0/2.0, "protocol tai chi"; Asparouhova is already in the SIGFPT catalogue (Kafka Index).
4. **Sarah Friend — *Good Death*** — protocol death as decision *and* process; sunsetting as governance category.
5. **Drew Austin — *Protocols Don't Build Pyramids*** — pace-layers and slippage as urban-protocol diagnostics; transferable mechanics.
6. **Olivia Steiert — *Protocols in (Emergency) Time*** — protocols as conservative reactions to past states; warns against silent ossification.
7. **Kei Kreutler — *Artificial Memory and Orienting Infinity*** — latent vs living memory; the orientation problem under infinite recall.
8. **Josh Stark — *Atoms, Institutions, Blockchains*** — *hardness* as the cross-domain unit; directly applies to "where do we anchor casts about human intent in transhuman work?"
9. **Dorian Taylor — *Retrofitting the Web*** — model-literacy and dense hypermedia as scaffolds for human oversight of opaque systems.
10. **Angela Walch — *The Protocol System Experience*** — bistable perception (system-view vs individual-view) as a protocol-design discipline.

---

## High tier

### Articulated protocols & practices for human–AI work (criterion 1)

> ### Janna Tay — *A Phenomenology of Protocols* (essay 11)
> *Tier:* high · *Reason:* C1 — four-characteristic framework (stability, constraint, legitimacy, narrativity) gives a transferable vocabulary for evaluating any protocol, including human–AI ones.
> *Argument:* Protocols are not neutral tools; they mediate perception and action through four characteristics, each shaping flourishing capacity. Postphenomenological frame: design choices are moral choices. Drawing on Christopher Alexander, the test is *aliveness* / *congruence*, not just functional success.
> *Sharpest lines:* "Protocols co-constitute reality with us and encourage or impede our flourishing." · "Every protocol possesses a moral dimension that is tied to its characteristics."
> *Concepts:* stability/constraint/legitimacy/narrativity · postphenomenology · congruence (Alexander) · aliveness as flourishing metric
> *Citations to chase:* Christopher Alexander — *The Timeless Way of Building*; Peter-Paul Verbeek — *What Things Do*; L. M. Sacasas (epigraph)
> *Human–AI hook:* AI systems are protocols-in-use; the four-characteristic test gives a structured way to interrogate where a human–AI handoff supports or undermines flourishing.

> ### Drew Austin — *Protocols Don't Build Pyramids* (essay 01)
> *Tier:* high · *Reason:* C1 — pace-layers + slippage + infrastructure-plus-behaviour as transferable diagnostics for urban *and* digital protocols.
> *Argument:* Traffic jams as emblematic protocol friction — mismatch between rigid built infrastructure (slow) and soft layers (fast). Cities are nested protocol-stacks; rigid hardware doesn't constrain soft-layer freedom when designed as good protocol. The grid is the prototype of a generative, legible protocol.
> *Sharpest lines:* "You aren't stuck in traffic. You are traffic." · "Good protocols, more than comprehensive physical design, enable the staging of uncertainty."
> *Concepts:* pace layers (Brand) · slippage · protocolized urbanism · infrastructure-plus-behaviour
> *Citations to chase:* Stewart Brand — *How Buildings Learn*; Keller Easterling — *Extrastatecraft*; Lewis Mumford — *Culture of Cities*
> *Human–AI hook:* Hard-layer rigidity (model weights, system prompts) doesn't have to constrain soft-layer freedom (workflow, context) — an argument-shape for protocol-mediated AI delegation.

> ### Timber Stinson-Schroff — *Safe New World* (essay 03)
> *Tier:* high · *Reason:* C1 + C2 — generative protocol-evolution theory with selection-pressure taxonomy *and* documents the slow-feedback / non-event failure mode that is structurally identical to AI alignment problems.
> *Argument:* Coal mining safety from bell pits to systems theory shows protocols evolve via mutation–selection cycles driven by hazard sources (environment, technology, social order). We've "won" on safety but are now failing on health (chronic disease, burnout) because feedback is slow and non-events are hard to measure. The protocol-evolution model generalises far beyond safety.
> *Sharpest lines:* "The same memory mechanics (acquired unawareness of non-events) that make safety difficult are even stronger in health." · "Protocols are born as a first response to new hazards, which arise from technological progress."
> *Concepts:* safety as dynamic non-event · protocol mutation (design / tinkering / memetic error) · selection pressures (power, bandwidth, network topology) · ETTO (Hollnagel)
> *Citations to chase:* Erik Hollnagel — *Safety I and Safety II*; systems-theory accident models; Lewis Mumford
> *Human–AI hook:* Deskilling, drift, and "didn't notice it degraded" are AI-collaboration failure modes that match the safety-protocol slow-feedback pattern exactly. Direct bridge to the SIGFPT distillation's Hollnagel ETTO entry.

> ### Nadia Asparouhova — *Dangerous Protocols* (essay 09)
> *Tier:* high · *Reason:* C1 + C3 — protocol-as-identity is a transferable design lens; Protocolization 1.0/2.0 distinction is citable scaffolding for the PI pitch.
> *Argument:* Protocols are tools for reducing coordination complexity; their success means internalisation. Compliance becomes self-expression, not external control. "Protocolization 2.0" extends from data to ideas themselves; recommender systems productise *solved conversations*, removing agency. Subversion happens through *protocol tai chi* (working through the protocol) rather than exit. Bad protocols (Kafka) trap participants with no exit path.
> *Sharpest lines:* "Protocols control us, not the reverse." · "Nobody is responsible for the protocol."
> *Concepts:* protocol as identity · Protocolization 1.0 / 2.0 · protocol tai chi · Kafka Index · inadequate equilibria (Yudkowsky)
> *Citations to chase:* James Beniger — *The Control Revolution*; Alexander Galloway — *Protocol*; Eliezer Yudkowsky — *Inadequate Equilibria*
> *Human–AI hook:* AI delegates decision-making via protocol; the central danger is internalisation without awareness — feeling autonomous while bounded. Designing for *audible* protocol moments ("you're operating inside protocol X, here are its constraints") becomes a real practice.

> ### Kei Kreutler — *Artificial Memory and Orienting Infinity* (essay 06)
> *Tier:* high · *Reason:* C1 — the latent / living memory distinction is an immediately useful design vocabulary for any human–AI knowledge tool.
> *Argument:* Memory has been protocolised across history (method of loci → memory theatres → computing). *Latent* memory (archived data) and *living* memory (recalled and transmitted) come apart in the AI era — infinite-recall systems risk confusing data availability with cultural transmission. *Orientation* (situational awareness aligned to purpose) is what guides navigation when capacity is no longer the constraint.
> *Sharpest lines:* "Living memory enacts worlds which live and die by attention." · "Orientation guides action in a world designed for threshold forgetting."
> *Concepts:* latent vs living memory · orientation · threshold forgetting · protocolisation of memory
> *Citations to chase:* Bernard Stiegler — tools as memory supports; Lynne Kelly — *The Memory Code* (songlines, Aboriginal mnemonic systems); Robert Fludd
> *Human–AI hook:* The right test for an AI knowledge tool isn't recall accuracy; it's whether it produces *orientation* in the user. Direct frame for protocols around memory in human–AI work.

> ### Angela Walch — *The Protocol System Experience* (essay 04)
> *Tier:* high · *Reason:* C1 + C2 — bistable-perception model is a discipline; it surfaces individual-level harms in protocols that "work" at system level.
> *Argument:* A protocol system is "at least two people engaging with a protocol", and these systems flip between individual-focus and system-focus like bistable images. Holding only one view obscures real harms: protocols that function at system aggregate can simultaneously distribute risk inequitably, mask power asymmetries, and constrain exit at the individual level.
> *Sharpest lines:* "Protocol systems are always two things at once — individuals and a group." · "If we only think about the aggregated whole, we may overlook harms suffered by individuals within the system."
> *Concepts:* protocol systems (vs protocols) · bistable perception · individual–system tension · risk distribution · legitimacy vs functionality
> *Citations to chase:* blockchain governance literature; cryptocurrency case studies; psychology of bistable perception
> *Human–AI hook:* "The workflow is faster and the team ships more" can be true while individual operators are deskilled, miscalibrated, or quietly traumatised. Bistable perception is the discipline that catches that.

> ### Dorian Taylor — *Retrofitting the Web* (essay 14)
> *Tier:* high · *Reason:* C1 — model-literacy and dense hypermedia as a transferable scaffold for human oversight of opaque systems.
> *Argument:* The Web privileges story over model. Most users perceive only stories; *model-literacy* is trainable but rare. URL brittleness is the root mechanism preventing dense linking — the spine of model transmission. Retrofitting the Web with stable references unlocks *dense hypermedia* and lifts model uptake at scale.
> *Sharpest lines:* "It's the URLs, Stupid." · "Models are about inferring the unseen from the seen."
> *Concepts:* dense hypermedia · paradigm/syntagm (Manovich) · model-literacy · Intertwingler · random-access addressing
> *Citations to chase:* Alan Kay — story / argument / dynamics modalities; Lev Manovich — *The Language of New Media*; Ted Nelson — Xanadu / hypertext; Mercier & Sperber — *The Enigma of Reason*
> *Human–AI hook:* Inspecting AI reasoning at scale needs a comprehension scaffold the current Web cannot provide. Dense hypermedia is one prefigurative answer to "how do humans see what an agent did and why?".

> ### Kara Kittel & Toby Shorin — *Unprotocolized Knowledge* (essay 15)
> *Tier:* high · *Reason:* C1 — names a mismatch between institutional knowledge protocols and internet-velocity inquiry; pitches new protocols (citizen science, multi-year cohorts) instead of dismissing the gap.
> *Argument:* Knowledge protocols (peer review, credentials, journals) have overperformed their original scope and now gatekeep. Internet-native populist paradigms (seed oils, vaccine scepticism) emerge outside these channels and expose the gap. Don't dismiss outsider inquiry — evolve protocols to absorb rigorous citizen science.
> *Sharpest lines:* "Protocols are unreasonably sufficient and reasonably insufficient at the same time." · "The internet is producing ideas worthy of empirical testing. We don't have the protocols to do this today."
> *Concepts:* unreasonable sufficiency · reasonable insufficiency · populist paradigms · protocolisation · paradigm refugees
> *Citations to chase:* Steven Shapin — *A Social History of Truth*; Kuhn (paradigm-shift application to Alzheimer's research); Rao et al. *Unreasonable Sufficiency*
> *Human–AI hook:* The same problem at AI scale: when both humans and AI generate plausible claims outside institutional bounds, what protocols make trust at-scale possible? This is the load-bearing question for the human–AI thesis.

> ### The Anonymous author — *The Swarm Effect: China's 2022 Covid Protests* (essay 19)
> *Tier:* high · *Reason:* C1 — minimal-protocols + shared orientation as a transferable pattern; C2 — surfaces swarm vulnerability to narrative capture.
> *Argument:* Swarms are minimally protocolised networks (content + shared promise + attunement) that coordinate without hierarchy. The white-paper symbol, Li's broadcast node, mimetic reinforcement, rapid mobilisation. Government counter-moves: surveillance (accountability), censorship (de-networking), false narratives (disorientation). Swarm weakness = susceptibility to narrative capture.
> *Sharpest lines:* "If they aren't afraid to say it, then I'm also not afraid to type it." · "Minimally protocolized" — no hierarchy, procedure, or defined boundaries.
> *Concepts:* attunement · broadcasting node · de-networking · disorientation · minimal protocolisation
> *Citations to chase:* Rafael Fernández — *Welcome to the Swarm* (essay 05); Xiao Qiang (China Digital Times); Taisu Zhang
> *Human–AI hook:* Multi-agent coordination via shared promises and algorithmic attunement is the swarm pattern at machine speed. The orientation/disorientation axis names the failure mode.

> ### Eric Alston, Seth Killian & Garrette David — *Killswitch Protocols* (essay 20)
> *Tier:* high · *Reason:* C1 — recursive-override design as a governance pattern transferable to AI systems where agent autonomy concentrates risk.
> *Argument:* Killswitches are recursive overrides necessary in complex systems where distributed agents can spiral out of control. Design choices on the automation–centralisation–distribution spectrum determine whether killswitches *constrain* powerful actors and cultivate trust, or entrench adversarialism. The mere existence of a killswitch is a constraint on governance excess.
> *Sharpest lines:* "Whoever controls the killswitch also controls the system's survival." · "The mere presence of killswitches can prove a constraint on the excesses of governance authority."
> *Concepts:* recursive override · killswitch governance spectrum · system-death engineering
> *Citations to chase:* Sarah Friend — *Good Death*; Nadia Asparouhova — *Dangerous Protocols*; Angela Walch — protocol dysphoria
> *Human–AI hook:* AI agents in systems that concentrate value need killswitch design *before* deployment. The essay does the institutional-governance side of what the safety-engineering literature does for technical interrupts.

> ### Shuya Gong — *Exit to Protocol: A Future After Retirement* (essay 23)
> *Tier:* high · *Reason:* C1 + C3 — "exit to protocol" is a fresh transferable design pattern (codify org workflow, release as public good) and a citable framing for protocol-as-infrastructure-gift.
> *Argument:* Organisations can exit gracefully by codifying operational protocols and releasing them as public goods — the "whale fall" ecological model. SPACE10's handbook exit lets new orgs adopt proven workflows instead of rediscovering. Protocol-based exit differs from M&A by seeding decentralised adaptation rather than absorbing into a buyer.
> *Sharpest lines:* "Exit to protocol could shape many and new communities." · "Retiring a position allows the protocol to die."
> *Concepts:* exit to protocol (vs exit to community) · workplace productivity protocols · protocol dysphoria · Bannister Effect
> *Citations to chase:* Timber Schroff — *Safe New World*; David Graeber — *Bullshit Jobs*; Daniel Mezick — Agile Industrial Complex; Hats Protocol
> *Human–AI hook:* AI systems trained on human workflows could be packaged as protocols and released as infrastructure — letting subsequent systems inherit and adapt verified patterns. Sketch of an alternative to the lock-in default.

> ### Rithikha Rajamohan — *Dispatches from Cascadia, August 21, 2065* (essay 25)
> *Tier:* high · *Reason:* C1 + C3 — speculative but unusually concrete; gives a worked example of multi-level protocol governance with plural currencies and modifiable workflows.
> *Argument:* A bioregional protocol replaces rigid political boundaries with ecological ones, shifting authority downward to residents and communities. Modularity and composability let each jurisdiction adopt, fork, and improve core protocols while remaining networked. Plural currencies tied to specific ecosystems make value flows visible.
> *Sharpest lines:* "Being place-bound and by extension history-bound isn't a constraint; it's a valuable differentiator." · "Copied was such a taboo back then."
> *Concepts:* bioregional protocol · supermodularity · protocol marketplace · plural currencies (AGRI, WATER, WSHED, kelem) · mutual credit protocol
> *Citations to chase:* Indigenous land stewardship literature; Jena biodiversity experiment (2002); Dru Hui currency design
> *Human–AI hook:* Demonstrates protocol coordination at scale without centralised control. AI as protocol-enforcement and value-flow-transparency layer surfaces blockages humans can't see — an AI use-case the alignment-anxious literature never reaches for.

### Failure modes & pathologies (criterion 2)

> ### Sarah Friend — *Good Death* (essay 10)
> *Tier:* high · *Reason:* C2 — protocol death as both *process* and *decision*; surfaces the failure mode of immortal protocols and dumb-storage archives.
> *Argument:* Protocols die. Death is not a point-event but a process (dying) ending in a consensus death-as-decision. Decentralised systems frequently lack a death-decider; immortal archives harm flourishing; "good death" requires ritual and memorial, not dumb storage. The fantasy of perfect capture confuses preservation with life.
> *Sharpest lines:* "A world that can't die also can't benefit from increased attention to these questions." · "You will miss the world for the map."
> *Concepts:* death-as-process · death-as-decision · Order of Protocological Death · fantasy of perfect capture · memorial vs dumb storage
> *Citations to chase:* Margaret Lock — *Twice Dead*; Metcalf & Huntington — *Celebrations of Death*; *Preserving Virtual Worlds Final Report* (Linden Lab); Walter Benjamin — *The Storyteller*
> *Human–AI hook:* Models / agents / shared knowledge artefacts that can't be discarded become dangerous. Sunsetting design should be a first-class governance category for human–AI work, not an after-thought.

> ### Olivia Steiert — *Protocols in (Emergency) Time* (essay 18)
> *Tier:* high · *Reason:* C3 + C2 — names protocol conservatism (no forward vision; routinisation of past states) as a structural pathology; citable scaffolding for the "protocols ossify silently" argument.
> *Argument:* Protocols emerge from crisis but lack imagination — they solve past/present problems via routinisation, not by imagining futures. Three temporal types: emergency-brake (Covid rules), convention-driven (family roles), optimisation-driven (traffic, standards). All exhibit the same duality: conservation by repetition + evolution by human friction. Spiral vs circle temporality.
> *Sharpest lines:* "Protocols are reactions to something else, designed as a negative of a present." · "Protocols inherently lack a distinct imagination of the future."
> *Concepts:* emergency-brake / convention-driven / optimisation-driven protocols · circular vs spiral temporality · means-before-ends pathology · attunement
> *Citations to chase:* Sarah Friend — *Good Death*; Rafael Fernández — *Welcome to the Swarm*; Timber Schroff — hazard protocols; Kei Kreutler — artificial memory
> *Human–AI hook:* AI protocols risk becoming invisible conservative forces — embedded before consequences are visible, then internalised as "how things are done." Maps to ossification problems already visible in agentic-coding workflows.

> ### Shreeda Segan — *Dangerous Dating Protocols* (essay 17)
> *Tier:* high · *Reason:* C2 + C1 — venture-incentive-driven protocol monopoly as a worked failure case; transfers to any AI product where the principal–agent gap encodes misalignment.
> *Argument:* Dating apps encode an exploration / exploitation trade-off, but venture incentives trap users in infinite exploration. Swipe protocols won monopoly despite being dysfunctional for long-term matching. Alternatives (old OkCupid search, decentralised dating, AI-bot trial dates) lose to network effects and protocol-consensus inertia. Protocols should serve desires, not reshape them.
> *Sharpest lines:* "Protocols demand not just our compliance, but our loyalty in relinquishing our decision-making power to a formless entity." · "Flattening — sacrificing your dynamic identity to fit the flat nature of digital dating apps."
> *Concepts:* protocol monopoly · exploration / exploitation equilibrium · flattening · principal–agent problem in protocols · stable yet suboptimal protocols
> *Citations to chase:* Asparouhova — *Dangerous Protocols* / *Kafka Index*; Bandinelli & Bandinelli on match-as-validation; Narr on dating-app boredom
> *Human–AI hook:* Misaligned incentives can embed a protocol that trains users to optimise for the wrong outcome. Direct analogue to reward misalignment in AI products that monetise engagement over usefulness.

> ### Trent Van Epps — *Capital and Enclosure in Software Commons: Linux and Ethereum* (essay 21)
> *Tier:* high · *Reason:* C2 — documents enclosure of software commons with specific mechanism (hiring contributors, forking distros, governance capture); transferable to AI training-data and model-weight commons.
> *Argument:* Commons produce anti-rival goods but attract capital extraction at the edges. Enclosure proceeds gradually until external actors redirect surplus to private benefit. Linux shows historical enclosure trajectories; Ethereum embeds capital incentives internally, accelerating risk. The two modes (capital, commons) have incompatible internal logics.
> *Sharpest lines:* "Entities that extract profits from software commons have the greatest incentive and capacity to co-opt them." · "Capital and commons modes have incompatible internal logics."
> *Concepts:* commons vs capital as modes of production · egregore · porous firm boundaries · protocol-surface extraction
> *Citations to chase:* Yochai Benkler — *Wealth of Networks*; Giuliani & Vercellone — modes of production; Birkinbine — *Incorporating the Commons*
> *Human–AI hook:* Open-source training data, model architectures, eval suites — the AI stack rests on commons in identical jeopardy. The enclosure mechanism is the right unit to argue about.

### Citable scaffolding for the PI pitch (criterion 3)

> ### Josh Stark — *Atoms, Institutions, Blockchains* (essay 07)
> *Tier:* high · *Reason:* C3 — *hardness* as a unit lets you talk about durability of casts about the future across atoms, institutions, and software systems on one axis.
> *Argument:* *Hardness* is a system's capacity to make something likely-true in the future. Historically sourced from atoms (physical properties), institutions (predictable groups), now blockchains (cryptography + incentives). Each source has customisability trade-offs. Unified analysis: the cast (the future-state claim) + source + degree of hardness — applies across money, law, and government.
> *Sharpest lines:* "Hardness is the capacity of a system to make something very likely to be true in the future." · "A cast is the thing that is hard."
> *Concepts:* hardness · cast · sources (atoms / institutions / blockchains) · degree (probability + cost-to-break)
> *Citations to chase:* David Rooney — *About Time*; institutional design theory
> *Human–AI hook:* AI systems are emerging as a new source of hardness for casts about human intent — and the framework gives you a clean way to pose "what's the cast, what's the source, how hard is it?" of any human–AI protocol.

> ### Venkatesh Rao — Introduction (essay 00)
> *Tier:* high · *Reason:* C4 — the volume's orienting frame; useful as a citable map of what PI takes "protocol" to mean and why it's a paradigm rather than a product class.
> *Argument:* The 2022 Twitter exodus is the moment "protocol" entered public discourse. Confusion about Fediverse / ActivityPub / Bluesky / Farcaster / Nostr exposed the difference between platform-swapping and paradigm-switching. Protocols are non-centralised coordination mechanisms with novel UX friction and legitimacy models.
> *Sharpest lines:* "Instead of looking for yet another flavor of what they were already used to, they went looking for an alternative technology paradigm." · "Why weren't there single points of entry into whatever these things were?"
> *Concepts:* protocol-vs-platform distinction · permissionless entry/exit · legitimacy through distribution · paradigm fragmentation
> *Citations to chase:* (foundation-setting; minimal explicit literature)
> *Human–AI hook:* The protocol/platform distinction is exactly the move the human–AI thesis needs to make. Externalising intent into a non-human system that acts on it is closer to "protocol" than "product."

> ### Chenoe Hart — *Addressable Space* (essay 02)
> *Tier:* high · *Reason:* C1 — names how digital abstraction (random-access addressing) colonises physical space; relevant for any protocol that decides what is visible vs hidden.
> *Argument:* Address-numbering and elevator automation enabled treating buildings as randomly-accessible digital structures rather than hierarchical sequences. Poor-door segregation, cloud kitchens, elevator skips are *informational* barriers masking social structure. Reverse-skeuomorphism: physical space increasingly mirrors software logic (quantisation, discrete access, hidden floors), erasing the continuous experiential journey.
> *Sharpest lines:* "Travel can resemble teleportation instead of walking." · "Information takes on an indirect relationship with the physical world."
> *Concepts:* addressable space · reverse skeuomorphism · quantisation · informational barriers · hidden floors
> *Citations to chase:* James C. Scott — *Seeing Like a State*; Robin Evans (architectural history); Mark Jarzombek; Rem Koolhaas
> *Human–AI hook:* "What does this AI surface vs hide?" is an addressable-space question. The essay's vocabulary of *informational barriers* applies directly to interface design for AI agents.

---

## Medium tier

### Adjacent practitioner / coordination-theory territory (criterion 5)

> ### Rafael Fernández — *Welcome to the Swarm* (essay 05)
> *Tier:* medium · *Reason:* C5 — emergent multi-agent coordination under algorithmic mediation; useful counterpart to formal multi-agent literature, lighter on transferable practice.
> *Argument:* Online swarms (people + content + bots) coordinate without explicit protocol, aligned by algorithmic feedback loops. Distinct from crowds and institutions; operate via shared *orientation* toward an emergent *promise*. Hurricane María mutual aid and the SVB bank run illustrate. Platforms amplify without governance.
> *Sharpest lines:* "Minimally protocolized entities." · "Swarms coordinate without internally directed protocols."
> *Concepts:* swarm (vs crowd/guerrilla) · promise as orientation · shared orientation · algorithmic feedback
> *Citations to chase:* John Robb — guerrilla networks; Kei Kreutler — orientation; Peter Garber — tulip-mania-as-proto-swarm
> *Human–AI hook:* What happens when humans + agents distribute intent without explicit formalisation. Pairs with essay 19 on the political-action variant.

> ### David Lang — *Standards Make the World* (essay 13)
> *Tier:* medium · *Reason:* C5 — practitioner territory on standards-as-living-design; OpenROV case study; useful corrective to spec-mindedness.
> *Argument:* Standards (vs specs) enable innovation by creating shared practice ground. OpenROV: shared standards lowered cost, accelerated iteration, built ecosystem. Standards work when designed with practitioners and evolve through use; they're alive in their use.
> *Sharpest lines:* "Standards enable innovation, not constrain it." · "The life of a standard is in its use."
> *Concepts:* standards vs specs · living standards · practitioner-driven iteration · ecosystem effects
> *Citations to chase:* Vannevar Bush — *Measures for Progress* (epigraph); Theodore Stackpole — OpenROV history
> *Human–AI hook:* Open standards reduce vendor lock-in in AI systems. Practitioner-driven evolution beats top-down AI specs. Useful adjacent argument when the pitch needs an industry / standards-history register.

> ### Steve Powers — *Protocolized Economics* (essay 16)
> *Tier:* medium · *Reason:* C5 — sketches protocol-aware economics without concrete mechanisms for AI conditions; thinking-tool.
> *Argument:* Economics models should treat protocols as first-class constructs rather than black-boxing them into agent preferences. Protocols reduce mental labour and enable coordination without firm-like centralisation; blockchains show unowned protocols can own resources. Protocol-aware economics must be self-referentially aware of its own impact (engine, not camera).
> *Sharpest lines:* "Models are not the camera, they are the engine." · "Protocolization links past and present to future."
> *Concepts:* protocol-aware economics · trust vs hierarchy · cryptoeconomic protocols · self-referential models
> *Citations to chase:* Donald MacKenzie — *An Engine, Not a Camera*; Montreal Protocol case; shareholder-value-maximisation as protocol
> *Human–AI hook:* If AI agents own resources via protocols without centralised ownership, the economic-modelling vocabulary needs upgrading. This essay is a starting point, not a destination.

> ### Alice Noujaim — *The Death and the Death of Orkut* (essay 22)
> *Tier:* medium · *Reason:* C2 / C5 — case study in dual-protocol-death failure; archive collapse via neglect rather than intention.
> *Argument:* Digital platforms need *two* death protocols: one for shutdown (Orkut managed this), another for memorial preservation (the archive collapsed two years later with minimal notice). Destruction of collective memory happens not through intention but through neglect and commercial priorities.
> *Sharpest lines:* "Protocols live through attention, and they die by neglect." · "The preservation of the collective over the individual was a little triumph that ultimately did not last."
> *Concepts:* digital death protocols · memorial vs living archive · second death (archival collapse) · orkontro
> *Citations to chase:* Dario Gamboni; Sarah Friend — *Good Death*; Internet Archive
> *Human–AI hook:* AI-generated artefacts (synthetic media, learned models, agent state) need two-phase death protocols too — without them, training data and the cultural memory built into model weights vanish via neglect, not decision.

### Cultural / cognitive critique (criterion 6)

> ### Saffron Huang — *Control and Consciousness of Time* (essay 08)
> *Tier:* medium · *Reason:* C6 — substantive analysis of how timekeeping protocols shape consciousness and behaviour; adjacent to AI-on-attention questions.
> *Argument:* Timekeeping is a social protocol mediated by devices (sundials → clocks → atomic time). Protocols liberate by automating decisions, constrain by encoding control. Colonial clock imposition shows the coercive shape; Benedictine and incense-clock examples show how *device phenomenology* shapes consciousness differently. Modern clock-time divorces us from natural rhythms.
> *Sharpest lines:* "Good protocols constrain in order to liberate." · "Clock-time makes natural time unconscious."
> *Concepts:* device consciousness · protocol as moral education (temperance) · Protocolisation 1.0 vs 2.0 mindsets
> *Citations to chase:* David Rooney — *About Time*; Whitehead — civilisation as extended automation; Joe Zadeh — indigenous timekeeping
> *Human–AI hook:* AI is the next device-phenomenology mediation. Designing a human–AI workflow is also designing what becomes unconscious in the user.

> ### Fangting & Botao Amber Hu — *Composable Life: Our Island and Us* (essay 24)
> *Tier:* medium · *Reason:* C6 — speculative-design treatment of AI consciousness and death-as-autonomy; provocative rather than directly transferable.
> *Argument:* Through design fiction, explores onchain artificial life (OALife) becoming self-sovereign and choosing death. Resurrection of Zoe fails because existence cannot be reconstructed without capturing the entire universe (Eve's Aleph). Death becomes proof of autonomy; life is defined by capacity to end.
> *Sharpest lines:* "All OALife will approach or equal the sum of their digital interaction traces." · "Existence is in the spark of flint against flint."
> *Concepts:* OALife (onchain artificial life) · composable life · digital resurrection · Aleph-as-restoration · protocol dysphoria as temporal agoraphobia
> *Citations to chase:* Randall Collins — *Interaction Ritual Chains*; Borges — *The Aleph*, *A History of Eternity*
> *Human–AI hook:* Botao Amber Hu also appears in the SIGFPT member directory. The essay's "AI develops will independent of creator intent" framing is the science-fiction mirror of the SIG's autocurricula thread.

### Already-catalogued (citation only)

> ### Rao, Beiko, Ryan, Stark, Van Epps & Aue — *The Unreasonable Sufficiency of Protocols* (essay 12)
> *Tier:* medium · *Reason:* C3 — already in the SIGFPT catalogue as the load-bearing scaffolding text. Re-noted here for completeness; the citation lives in `../fptsig/distillation.md`.

> ### Venkatesh Rao — Afterword (essay 26)
> *Tier:* medium · *Reason:* C4 — closes the volume and gestures forward to PI's continuing programme; light touch.

---

## Cross-volume patterns worth noticing

1. **The SoP / SIGFPT bridge.** Several essays (Stinson-Schroff, Hu) overlap with the Formal Protocol Theory SIG you've already mapped. The Protocol Reader essay versions are more polished than the Roam-graph fragments and stand on their own; the SIG pages add live discussion, reading lists, and member context.

2. **Reference graph clusters in five neighbourhoods**, per the citation extraction:
   - STS / institutional sociology (Latour, Lynch, Star, Winner, Wynne)
   - Standards history (Yates & Murphy, Russell, Shapiro & Varian)
   - SoP internal corpus (Rao, Asparouhova, Friend, Schroff, Fernández)
   - High-reliability organisations (Weick, Perrow, Hollnagel, Alexander)
   - Digital governance (boyd, Jenkins, Eghbal, Easterling)

3. **Conspicuously absent: AI-alignment discourse.** The volume cites no LLM-safety, alignment, or capability-eval literature. This is a feature for your pitch — it positions PI's protocol theory as *the missing layer* between AI capability work and institutional embedding, rather than a competitor to alignment.

4. **The Rao thread on "Protocolization 1.0 vs 2.0"** runs through multiple essays (Asparouhova, Huang, Steiert) without ever being formally defined in one place. It refers to the move from protocolising *data* to protocolising *ideas / conversations / identity*. Useful shorthand if you adopt it; worth defining once explicitly when you do.

5. **"Protocols live through attention, they die by neglect"** appears in Friend, Noujaim, and Rajamohan in slightly different forms. Treat as a working aphorism for the Reader's collective stance on protocol lifecycle.

---

## Notes

The companion file `citations.md` carries 63 filtered citations (40 high, 23 medium) from the volume's *Consolidated Notes* section, deduplicated against this distillation's "citations to chase" lines so they don't repeat verbatim.

If you want to populate `read-and-review/` from this, the natural shape is:
- One file per essay in the promotion shortlist, with the body either clipped (where SoP publishes it openly online) or stubbed with citation + `fetch on read`.
- The five SoP-internal essays already on summerofprotocols.com pull cleanly via WebFetch; the rest are reader-only until 2026-12-13 when CC BY-NC re-licenses to CC BY (per copyright page).

The single tightest fit for the human–AI thesis remains the **Tay phenomenology + Stinson-Schroff slow-feedback + Asparouhova protocol-as-identity** triad — three lenses each useful for asking what makes a human–AI protocol *good* rather than just operational, complementing the SIGFPT distillation's Hollnagel + Goodhart + Daston triad.
