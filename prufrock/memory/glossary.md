# Glossary

Project-specific terms, abbreviations, and references that come up in the Prufrock Protocol work.

## Protocol terms

| Term | Meaning |
|------|---------|
| **adjacent_pair_rotation** | The selection rule used by the Sonnet Trial. Each interruption presents two chronologically adjacent lines from one poem to a participant who is not the nominal author of that poem; the participant writes the next line. |
| **antithesis (in the dialectic)** | The disruption presented at the moment of interruption — currently `(Lₙ, Lₙ₊₁)` in the sonnet trial, but `PromptType` allows other forms (haiku, image, audio, location, none). |
| **assignment matrix 𝒜** | A pre-committed Latin rectangle that maps (day, participant) → poem during the response phase. No fixed points; balanced exposure. |
| **chosen_rotation** | Legacy single-spine selection rule. Each day a single chosen poet's line cascades to all responders. Superseded by adjacent_pair_rotation for the v1 trial. |
| **cohort** | A run of the protocol with a specific configuration. v1 sonnet trial runs 2 cohorts in parallel (poets, laypeople) from the same shared seed. |
| **𝓛*** | The poem-ledger — the append-only set of all valid contributions committed under the protocol. |
| **Latin rectangle** | The combinatorial structure underlying the assignment matrix. For the sonnet trial: 13 rows × 14 poems with no fixed point per row. |
| **nominal poem** | The poem associated with a given participant. In the v1 sonnet trial, each poet seeds line 1 of their nominal poem on day 1; they never write for it again during days 2–14. |
| **PromptType** | The form of the disruption presented as `Π*`. Values: `contributions`, `external_form`, `media`, `location_anchor`, `none`. |
| **response medium** | The medium of the contribution `x`. Values: `text`, `audio`, `image`, `video`, `mixed`. |
| **self-exclusion** | Protocol invariant: a participant is never prompted with their own prior contributions. |
| **prompt anonymity** | Protocol invariant: the participant's view of the prompt does not include the public key, name, or attributable identity of the prompt's author(s). |
| **seed** | The genesis pair — for the sonnet trial, two adjacent lines extracted from a public-domain source poem's volta (lines 12–13). Shared across all 14 poems in the cohort. |
| **synthesis (in the dialectic)** | The participant's signed contribution `ℓ`, in response to the antithesis and informed by their thesis (situated experience). |
| **thesis (in the dialectic)** | The participant's situated inner and outer state at the moment of interruption — intentionally not formally captured (this is the protocol's deliberate negative space). |
| **Θ (parent tuple)** | The ordered tuple of `k` parent hashes recorded in each contribution. `Θ = ⊥` for genesis contributions. |
| **φ (permutation)** | Generic symbol for permutations in the formalisation (replacing the more conventional π, which clashes with the constant). |

## Cryptographic primitives

| Term | Meaning |
|------|---------|
| **Ed25519** | The protocol's fixed digital signature scheme (over Curve25519). EUF-CMA-secure. |
| **EUF-CMA** | Existential Unforgeability under Chosen-Message Attack — the security property required of the signature scheme. |
| **H3** | Uber's hexagonal hierarchical geospatial indexing system. Protocol fixes resolution 5 (~252 km²) for participant locations — coarse enough to preserve privacy, fine enough for analytical utility. |
| **Hash commitment** | The mechanism for committing to a value (the assignment matrix, the chosen-poet rotation) before an experiment without revealing it; revealed at experiment close. |
| **Merkle DAG / authenticated append-only log** | Acceptable ledger backings. Protocol does not require proof-of-work or specific consensus; only append-only authenticated storage. |
| **SHA-256** | The protocol's fixed cryptographic hash function. |

## Long Now references

| Term | Meaning |
|------|---------|
| **10,000-Year Clock** | Long Now Foundation's flagship long-duration project, located in Nevada. |
| **Centuries of the Bristlecone** | Jonathon Keats's project marking time through bristlecone pine growth. |
| **Cosmic Calendar** | A visualisation that compresses ~13.8 billion years into one calendar year. |
| **Doomsday Clock** | Symbolic clock representing humanity's proximity to existential catastrophe. |
| **Future Library** | Katie Paterson's 100-year writing capsule (2014–2114), opened beyond the contributing authors' lifetimes. |
| **Long Bets** | Long Now's public registry for predictions and bets resolved over long durations. |
| **Long Now Zero** | The convention of writing years with a leading zero (02026, 02100, etc.) to make explicit a 10,000-year frame. |
| **Pace Layers** | Stewart Brand's framework of nested timescales: fashion · commerce · infrastructure · governance · culture · nature. |
| **Rosetta Disk** | Long Now's micro-etched nickel disk containing thousands of human-language samples for ten-thousand-year readability. The "decennial spine etching" in the Prufrock artefact spec is conceived as Rosetta-class. |
| **The Interval** | Long Now's San Francisco venue; proposed as the public unveiling site for *Continual Proof: Volume I*. |

## People (referenced in source materials)

| Person | Why they appear |
|--------|-----------------|
| **Marvin Bell** | American poet (1937–2020). Source of the recursive rule-learning algorithm at the heart of Robert's "Infinite Game of Poetry" talk: *"Learn the rules, break the rules, make up new rules, break the new rules."* Also "A poem listens to itself as it goes along," "Be a poet every day." Photographed with Robert in the talk's closing slide. |
| **Marianne Moore** | American modernist poet. Her poem *"The Fish"* is the close-reading anchor of Robert's talk — its syllabic pattern (1, 3, 9, 6, 8) demonstrates protocol embodied in form. |
| **Stephen Dunn** | American poet. His line *"Bring to me, it said, continual proof / you've been alive"* (from "Different Hours") supplies the title for the proposed Prufrock artefact, *Continual Proof: Volume I*. |
| **Stewart Brand** | Co-founder of the Long Now Foundation; originator of the Pace Layers framework; coined "Civilization is revving itself into a pathologically short attention span" (01999). |
| **T. S. Eliot** | "The Love Song of J. Alfred Prufrock" — namesake of the protocol; epigraph *"I have measured out my life in coffee spoons."* |
| **William McGonagall** | Scottish poet (1825–1902). His *"Tay Bridge Disaster"* appears in Robert's talk as the negative exemplar `¬L(r)` — what poetic form looks like when one *hasn't* learned the rules. |

## Past poetry-on-blockchain precedents

Comparative review in `poetry-blockchain-precedents.md`. In brief:

| Project | Position in the field |
|---------|----------------------|
| **Po.et** (2017–2020) | Registry/licensing layer for creative works. Strong technical precedent; weak durable poetry market. |
| **Mirror** (2020–) | Web3-native publishing infrastructure. High infrastructure success; indirect for poetry. |
| **Etherpoems** (2021–) | Fully on-chain poetry collective. Strong artistic precedent; modest market traction. |
| **theVERSEverse** (2021/2022–) | Curated poetry-NFT gallery. The most successful niche poetry-blockchain institution to date. |
| **POEM** (2021–) | Tokenised poetry book with physical redemption. Conceptually novel; commercially unproven. |
| **TECHNELEGY** (2021–) | Sasha Stiles's artist-led AI/blockchain poetry programme. High critical, moderate market success. |
| ***Cord*** (2024) | Ana María Caballero's single-poem Bitcoin Ordinal sold at Sotheby's for $11,430. Symbolic milestone. |

## Other terms

| Term | Meaning |
|------|---------|
| **Bitcoin Ordinals** | The protocol for inscribing arbitrary content directly onto individual satoshis on Bitcoin. Proposed as the per-line on-chain anchor in the Prufrock artefact spec. |
| **Continual Proof** | Working title for the proposed Prufrock artefact (a hand-bound print codex). From Stephen Dunn. |
| **Exquisite corpse** | Surrealist collaborative writing/drawing exercise where each participant adds to a piece without seeing the whole. The Prufrock Protocol's adjacent-pair-rotation generalises this with cryptographic authentication and combinatorial dispersion. |
| **Volta** | The "turn" in a sonnet (typically lines 8–9 in Petrarchan, between the octave and sestet; or lines 12–13 in Shakespearean, before the closing couplet). The v1 trial extracts the volta couplet of a public-domain sonnet as the shared seed. |

## Project-specific framings (load-bearing)

| Term | Meaning |
|------|---------|
| **Long-now form** | Poetry, in this project's framing — a four-thousand-year-old form that binds the *long* (timeless themes) to the *now* (concrete individual moments) in a single act. The human timepiece that predates the clock. Foundation of the pitch's central claim. |
| **Regression to the mean** | What generative AI does to human concerns: averages them toward statistical centroids, producing anonymous probability-weighted text. The directional opposite of what the Prufrock Protocol is designed to do. |
| **Specificity to the timeless** | What poetry does (and what the Prufrock Protocol amplifies): expands what is compressed in humanity in aggregate into specific, signed, dated, located instances of individual consciousness expressing itself. |
| **Infinite game of using words to transcend words** | Marvin Bell's phrasing for poetry's distinctive work, threaded through Robert's "Infinite Game of Poetry" talk and through the Prufrock pitch. The design language at the project's heart. |
| **Anti-poetic AI** | The pitch's term for the present hegemony — generative systems that compress human meaning anonymously and statistically, sacrificing the named, dated, located moment that poetry is built to preserve. The Prufrock Protocol situates itself as antidote, not substitute. |
