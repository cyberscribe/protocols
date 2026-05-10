# SIGFPT Reference Catalogue

Sources extracted from the Formal Protocol Theory SIG Roam graph (`fptsig-roam/`),
filtered for material plausibly useful to research on protocols for human–AI
collaboration. Junk excluded: Discord/Zoom links, image CDNs, Excalidraw rooms,
shared Granola/ChatGPT/Claude chats, bare daily-note dailies.

Structure: grouped by relevance to the human–AI protocols thesis, then by domain.
Each entry lists the source SIG page so you can dive back in for context.
Items marked **★** are the highest-priority leads for the pitch.

---

## 1. Multi-agent learning, emergent coordination, autocurricula

The most direct intellectual neighbour of "protocols for human–AI collaboration":
formal models of how agents (silicon or otherwise) develop shared coordination.

- **★ Leibo et al., *Autocurricula and the Emergence of Innovation from Social Interaction: A Manifesto for Multi-Agent Intelligence Research*** — DeepMind manifesto. arXiv:1903.00742. Core reading for the SIG's April 3 session.
  → *Autocurricula.md*
- OpenAI, *Emergent Tool Use from Multi-Agent Autocurricula* (hide-and-seek). https://openai.com/index/emergent-tool-use/
  → *Autocurricula.md*
- DeepMind blog, *Understanding Agent Cooperation* + arXiv:2012.08630.
  → *Autocurricula.md*
- **★ Manheim & Garrabrant, *Categorizing Variants of Goodhart's Law*** — arXiv:1803.04585. Direct hit on alignment / metric-gaming risk in protocolised systems.
  → *Integration Jigsaw.md*
- Federated Learning literature pile (cluster cited together): arXiv 1912.04977, 2310.19201, 2106.15691, 2311.13714; IEEE 9039606. Likely on cooperative learning / privacy-preserving agent coordination.
  → *Atomic Protocol Questions.md*
- **★ Herbert Gintis, *The Bounds of Reason: Game Theory and the Unification of the Behavioral Sciences*** — flagged inside SIG as foundational for agent-protocol thinking.
  → *Autocurricula.md*
- Robert Axelrod, *The Complexity of Cooperation* (~1999) — "GOFAI equivalent in game theory"; iterated PD, tit-for-tat as proto-protocol.
  → *Autocurricula.md*

## 2. Actor model / agent communication — the original "protocolised computation"

Mike Travers' Dec 12 lightning talk and follow-on work read this lineage as
*the* prototype for protocol thinking. Tightly relevant to how AI agents are
architected today (MCP servers, agent supervision trees, etc.).

- **★ Carl Hewitt's actor model** — body of work; Mike Travers' annotated index at https://hyperphor.com/ammdi/Carl-Hewitt#54454
  → *Ontology and Politics.md*, *Actor Models.md*
- **★ Mike Travers, *Protocols* (and *Protocols∕Actors*, *Protocols∕Ideas*)** — https://hyperphor.com/ammdi/Protocols — Travers' own protocol thinking, "the more human side of protocols (rituals, social interaction, procedural epistemology)."
  → *SIGFPT Member Directory.md*, *Actor Models.md*
- Gul Agha, *An Overview of Actor Languages*. https://dl.acm.org/doi/pdf/10.1145/323648.323743
  → *Actor Models.md*
- Kornfeld & Hewitt, *The Scientific Community Metaphor* (MIT AI Memo 641). Computational systems modelled on how science works — proposals, confirmation, no central authority.
  → *Actor Models.md*, *Actor Models Dec 12 session transcript.md*
- *Offices Are Open Systems* (Hewitt) — orgs as actor systems; coordination tech for organisations.
  → *Actor Models Dec 12 session transcript.md*
- *Agoric Open Systems* (Eric Drexler & Mark Miller) — market-oriented computing; institutional abstraction boundaries. Influential on crypto.
  → *Actor Models Dec 12 session transcript.md*
- Carolyn Talcott (ed.), 2001 actor-systems volume; "43 Years of Actors" survey (2016).
  → *Actor Models Dec 12 session transcript.md*
- Carl Hewitt's late paper extending actors beyond Turing computation (nondeterminism).
  → *Actor Models Dec 12 session transcript.md*

## 3. Process calculi & formal communication models

The August 2025 process-calculi sessions amassed a deep reading list. These are
the formal substrate for "what is a protocol, mathematically?"

- *A Very Gentle Introduction to Multiparty Session Types* — http://mrg.doc.ic.ac.uk/publications/a-very-gentle-introduction-to-multiparty-session-types/main.pdf
- Hüttel, Lanese et al., *Foundations of Session Types and Behavioural Contracts*. https://pure.itu.dk/ws/portalfiles/portal/82370304/huttel.lanese.etal_fondations_session_types.pdf
- *Session Types and Behavioral Contracts* — https://dl.acm.org/doi/pdf/10.1145/2873052
- C.A.R. Hoare, *Communicating Sequential Processes*. http://web.eecs.umich.edu/~movaghar/cspbook.pdf
- Mantis H.M. Cheng, *Calculus of Communicating Systems: A Synopsis*. CiteSeerX d6566bd.
- Samson Abramsky, *Robin Milner's Work on Concurrency: An Appreciation*. arXiv:2206.09250
- *The Polyadic π-Calculus: a tutorial*. https://www.lix.polytechnique.fr/~fvalenci/papers/intro-ppi.pdf
- *Process Calculi as a tool for studying coordination, contracts, and session types*. https://inria.hal.science/hal-03102438/document
- *A Brief History of Process Algebra*. https://pure.tue.nl/ws/files/2154050/200402.pdf
- *The Variety of Process Algebras*. https://pure.tue.nl/ws/portalfiles/portal/4437128/589774.pdf
- *A Gentle Introduction to Process Algebra*. https://www.pst.ifi.lmu.de/Lehre/fruhere-semester/sose-2013/formale-spezifikation-und-verifikation/intro-to-pa.pdf
- *FAQ on π-calculus*. CiteSeerX fac9fca.
- *Pi Calculus vs Petri Nets*. http://www.workflowpatterns.com/documentation/documents/bptrendsPiHype.pdf
- *Bigraphs by Example* + *Practical Modeling with Bigraphs* (arXiv:2405.20745).
- *Modeling MultiAgent Systems as Labeled Transitions Systems*. CiteSeerX 34435136.
- *Foundations of Concurrency* (UNSW lecture slides). https://cgi.cse.unsw.edu.au/~cs3151/22T2/Week%2008/Wednesday%20Slides.pdf
- ScienceDirect S030439752200177 — distributability vs parallel composition.
  → all in *Process Calculi.md*, *Integration Jigsaw.md*

## 4. Stigmergy & indirect coordination

Most recent SIG topic (May 1, 2026). Direct relevance to AI agents leaving traces
in shared environments — file systems, codebases, knowledge graphs.

- **★ Theraulaz & Bonabeau, *A Brief History of Stigmergy*.** https://www.researchgate.net/publication/12680033 — primary reference; Grassé's concept resolving the superorganism vs individualist debate.
- **★ Parunak, *A Survey of Environments and Mechanisms for Human-Human Stigmergy*.** https://www.abcresearch.org/abc/papers/E4MAS05HHS.pdf — generalises insect-origin concept to human systems including Wikipedia, markets, web.
- Francis Heylighen, *Stigmergy: the most important concept you've never heard of*. https://francisheylighen.substack.com/p/stigmergy-the-most-important-concept
- Heylighen, *Stigmergy as a Universal Coordination Mechanism*. https://pespmc1.vub.ac.be/Papers/Stigmergy-varieties.pdf
  → all in *Stigmergy.md*

## 5. Protocols as a research field — the canonical Summer-of-Protocols corpus

Venkatesh Rao's programme, which the SIG largely operates inside.

- **★ *The Unreasonable Sufficiency of Protocols*** — https://summerofprotocols.com/research/the-unreasonable-sufficiency-of-protocols
  → *Design Principles for Protocols.md*
- **Nadia Asparouhova, *The Kafka Index*** — checklist for assessing protocols. https://summerofprotocols.com/wp-content/uploads/2024/04/Kafka-Index-Nadia-Asparouhova-1.pdf
  → *Protocols and Drift.md*
- *One Tension to Rule Them All* — https://protocolized.summerofprotocols.com/p/one-tension-to-rule-them-all
  → *Woodenman Group 1.md*
- Venkatesh Rao, *Hysteresis and the Mark Makers* (Bourdieu lens). https://contraptions.venkateshrao.com/p/hysteresis-and-the-mark-makers
- Venkatesh Rao, *Welcome to the Cosmopolis*. https://contraptions.venkateshrao.com/p/welcome-to-the-cosmopolis
  → *Amsterdam Talk.md*

## 6. Protocols, rules, and the social-theoretic frame

Closest to the "human protocols" half of Robert's thesis.

- **★ Lorraine Daston, *Rules: A Short History of What We Live By*** — Princeton UP. https://press.princeton.edu/books/hardcover/9780691156989/rules — thick vs thin distinction; foundational vocabulary for protocol design.
  → *Design Principles for Protocols.md*
- **Michael Lynch (2002)** — protocols as proxies for practice, always open to interpretation. (Ethnomethodological stance.)
  → *Woodenman Group 2.md*
- David Chambliss, *The Mundanity of Excellence*. https://academics.hamilton.edu/documents/themundanityofexcellence.pdf — the "design-for-mundanity" principle.
  → *Design Principles for Protocols.md*
- Bruno Latour, Actor Network Theory — discussed by Travers as protocol-relevant; bottom-up emergence of social structures.
  → *Actor Models Dec 12 session transcript.md*
- Wikipedia, *Ethnomethodology*. https://en.wikipedia.org/wiki/Ethnomethodology
  → *Group 6 Insights.md*
- David Crouch, *The Chivalric Turn* — early-medieval code as protocol case study.
  → *Early Medieval Code.md*
- Rem Koolhaas, *Junkspace* — handshakes losing meaning under runaway protocols.
  → *Group 2 insights.md*
- Lewis Woodside, *Lost Modernities* — flagged as next-step reading from Protocol School.
  → *List of projects | Protocol School.md*
- Christopher Alexander, *A Pattern Language* (Wikipedia entry as anchor).
  → *Incentive Patterns.md*
- "Software design patterns" lineage. https://en.wikipedia.org/wiki/Software_design_pattern
  → *Incentive Patterns.md*

## 7. Notation, modelling, observability

- **★ Iverson, *Notation as a Tool of Thought*.** https://www.eecg.utoronto.ca/~jzhu/csc326/readings/iverson.pdf — Turing Award lecture; central to the SIG's notation session.
- **Allen's Interval Algebra** — temporal coordination primitives; widely cited in protocol-homework. https://en.wikipedia.org/wiki/Allen%27s_interval_algebra
- **Region Connection Calculus** — spatial reasoning. https://en.wikipedia.org/wiki/Region_connection_calculus
- Probabilistic Graphical Models — https://en.wikipedia.org/wiki/Graphical_model + Stanford CS228 notes https://ermongroup.github.io/cs228/
- Causal Loop Diagrams — https://en.wikipedia.org/wiki/Causal_loop_diagram
- Feynman Diagrams — https://en.wikipedia.org/wiki/Feynman_diagram
- BPMN — https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation
- Karlheinz Stockhausen's *Prozession* — meta-notation for qualitative transformation. https://stockhausenspace.blogspot.com/search?q=+prozession
- Inform 7 — natural-language fiction language with state/rule notation. https://ganelson.github.io/inform-website/
- Affordances (HCI) — https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/affordances
- HyperLTL / hyperproperties — properties holding across runs (relevant for protocol verification).
  → *Tension-encoding notations.md*
  → all above mostly in *Notation.md*

## 8. Witsenhausen, control & impossibility

- **Witsenhausen Counterexample** — wikipedia + slide deck *Game Theory with Information: Introducing the Witsenhausen Intrinsic Model*. https://cermics.enpc.fr/~delara/exposes/Game_models_with_information.pdf
- *Open Problems in Communication and Computation* (Witsenhausen et al., 1987). https://raganwald.com/assets/fractran/open-problems-in-communication-and-computation-1987.pdf
- **Hilbert's 23 Problems** — analogue for the SIG's "Atomic Protocol Questions" framing. https://www.aemea.org/math/Hilbert_23_Mathematical_Problems_1900.pdf
- Fair-cake-cutting unsolved problems. https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_fair_division
  → *Impossibilities and Symmetries.md*, *Atomic Protocol Questions.md*

## 9. Maneuver Automata / autonomous-driving protocol stack

Compact bibliography of formal motion-protocol theory. Strong analogue for
"protocol primitives + composition rules" thinking in agent design.

- **★ Frazzoli, Dahleh, Feron, *Maneuver-based motion planning for nonlinear systems with symmetries*** (IEEE T-RO, 2005). https://web.mit.edu/dahleh/www/pubs/2005.1.pdf — canonical formalisation.
- Pedrosa et al., *Designing Maneuver Automata of Motion Primitives for Autonomous Driving* (Springer, 2024).
- *A Survey on Hybrid Motion Planning Methods for Autonomous Driving* (arXiv:2406.05575, 2024).
- Frazzoli, *Real-Time Motion Planning for Agile Autonomous Vehicles* (2001).
- Sanfelice & Frazzoli, *A Hybrid Control Framework for Robust Maneuver-Based Motion Planning*.
- Hess, *Formal Verification of Maneuver Automata for Parameterized Motion Primitives* (TUM, 2014).
- Vukosavljev et al., *A Modular Framework for Motion Planning using Safe-by-Design Maneuver Automata* (IEEE T-RO, 2019).
- *Improving the Maneuver Automaton with Maneuver Interruption* (AIAA, 2023).
- Kesting, Treiber, Helbing, *General Lane-Changing Model MOBIL for Car-Following Models* (Transportation Research Record, 2007).
  → *Maneuver Automata.md*, *Simulating Driving Protocol.md*

## 10. Agent-based modelling / collective behaviour

- **Sugarscape** + Epstein & Axtell, *Growing Artificial Societies: Social Science from the Bottom Up*. https://archive.org/details/growingartificia00epst
- Couzin et al., *Collective Memory and Spatial Sorting in Animal Groups*. https://jmvidal.cse.sc.edu/library/couzin02a.pdf
- Konstanz collective-animal-behaviour paper. https://kops.uni-konstanz.de/server/api/core/bitstreams/34931617-ddb1-4d42-8388-687a1df0fa3d/content
- *Symmetry and Collective Fluctuations in Evolutionary Games*. https://iopscience.iop.org/book/mono/978-0-7503-1137-3.pdf
- *Intrinsic and extrinsic thermodynamics for stochastic population processes…* arXiv:2008.01260
- Eric Smith & Harold Morowitz, *The Origin and Nature of Life on Earth* (Cambridge UP) + James Giammona's review.
- Massimo Pigliucci (2008), *Is evolvability evolvable?* Nature Reviews Genetics 9:75–82.
  → *Woodenman Group 1.md*, *James's talk - Robustness.md*, *Lightning talks.md*, *Evolving evolvability.md*

## 11. Causality & counterfactuals

- Judea Pearl, *Causality* — https://en.wikipedia.org/wiki/Causality_(book)
- Pearl, do-calculus tutorial paper. https://ftp.cs.ucla.edu/pub/stat_ser/r402.pdf
- Andrew Heiss, *Do-Calculus and Backdoors*. https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/
  → *Do-Calculus.md*

## 12. Cross-disciplinary "thick" references (long-form / cultural)

- David Shields, *Reality Hunger: A Manifesto* — flagged for lyric-essay form on archival time.
- Amitav Ghosh, *The Great Derangement: Climate Change and the Unthinkable* — literary fiction's failure to model archetypes.
- Sanjay Subrahmanyam-style "rules as practice" — Lynch (2002) above.
- Sanjay Krishnan "*Mesofication*" — Protocol School commencement speech.
- Hao Guang Tse — poetry references (Tse Hao Guang on grottojournal.net, basketmagazine.co.uk, miserytourism.com). Connect to Robert's poetry-protocols frame.
- David Foster Wallace, *This Is Water* — opening epigraph in PFW intro.
- Sanjoy Mahajan, *The Art of Insight in Science and Engineering* (MIT Press) + Street-Fighting Mathematics OCW course (recommended math-level calibration for the SIG).
  → *Protocol Foundations Workshop.md*, *Talk — Towards a Formal Theory of Protocols.md*, *List of projects | Protocol School.md*

## 12a. Resilience engineering & error tolerance

- **★ Erik Hollnagel, *The ETTO Principle: Efficiency-Thoroughness Trade-Off*** — surfaced in Group 4 insights as the operative trade-off for protocol design. Direct human-AI-collab parallel: agents constantly choose between thoroughness and throughput, and protocols negotiate that.
  → *Group 4 insights.md*
- Chang (2011), "grammar-first science" — frame for protocol-as-shared-grammar.
  → *Group 5 Insights.md*

## 12b. Methodological / pedagogical references

- **Fermi estimation + "Dyson design"** — Venkatesh Rao's Paper-Napkin-Math session. Methodological frame: "quick and dirty mathematics of protocols", order-of-magnitude shifts as design moves. Notebooks of Fermi estimates and Dyson designs as practice.
  → *Paper Napkin Math.md*
- Sanjoy Mahajan, *Street-Fighting Mathematics* (already in §12) — the math-level calibration recommended for the SIG.

## 13. Adjacent / curiosity (lower priority but worth a note)

- Boyle/Hooke/Wren — "Invisible College" (1640s) as proto-protocol institution.
  → *Inventory of Progress amid Conflict.md*
- Civilized by Television — sports as protocol case study.
  → *Civilized by Television.md*
- I²C protocol tutorials (hardware-protocol pedagogy). SparkFun + PlayWithCircuit.
  → *Lightning talks.md*
- Hao Guang Tse poetry venues — Robert-relevant cluster.
- *Cascade Network — Meshes of the Ata Hapara* (Meshtastic Haiku readiness protocol). https://cascadenetwork.gitbook.io/meshes-of-the-ata-hapara — eco-poetics + protocol crossover.
  → *List of projects | Protocol School.md*
- *Hierarchies of Agency* / Brian Skinner protocol-phase-change talk.
  → *Group 3: Formalizing Protocol Failure.md*

---

## SIG members directory (people-as-references)

Where Robert may want to follow individual threads. From `SIGFPT Member Directory.md`:

- **Mike Travers** — actor-model + Latour bridge; index at hyperphor.com/ammdi.
- **James Giammona** — robustness, evolutionary games, origin of life.
- **Patrick Nast** — process calculi sessions lead.
- **Venkatesh Rao** — Summer of Protocols overall.
- **Brian Skinner** — protocol phase change.
- **Timber Schroff** — emergent behavior, Git as protocol.
- (See file for full list including Sachin Benny, Jenna Dixon, Giovanni Merlino, Orpheas Katsikis, Seth Killian, Botao 'Amber' Hu, Chris Reid, Austin Jacobs, Ivo, maparent.)

---

## Files of unusually high reference density

If a deeper pass is needed, these are the highest-yield SIG pages:

| Page | Size | Why it matters |
|---|---|---|
| Protocol Homework Problem Sets | 78KB | Member-submitted problems with worked references — likely contains many citations not yet surfaced |
| Stigmergy | 38KB | Full reading set + extensive glossary |
| Autocurricula | 48KB | Manifesto + transcript + Q&A; paper list at top |
| Protocolizing Agent Space | 54KB | Discussion-starter doc, agent-system framing |
| Notation | 13KB | Iverson + multiple notation traditions |
| Talk — Towards a Formal Theory of Protocols | 13KB | The big SIG framing talk |
| Process Calculi | 12KB | Full reading list |
| Raw Transcript Observability / Paper Napkin / Process Calculi | 45–59KB each | Transcripts; harder to mine but contain cited material |

---

*Catalogue assembled 2026-05-08 from the Roam SIGFPT export. URL list with full
context preserved at* `outputs/refs/urls_with_context.txt`.
