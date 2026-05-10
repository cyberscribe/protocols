# The Prufrock Protocol

> "I have measured out my life in coffee spoons"
>     -T.S. Eliot, "The Love Song of J. Alfred Prufrock"

## The Problem

In a world forever changed by generative AI, where words and images can be synthesised from aggregations quickly, easily, and at scale, how can we continue to record authentic moments of human expression over time?

One answer is to retreat to private and analogue approaches — a handwritten diary, a face-to-face conversation, a photograph taken on film. Though more verifiable and incorruptible, these methods abandon the advances that digitisation and network distribution afford us for communicating quickly, globally, and for archiving artefacts at scale.

The Prufrock Protocol takes a different position. Rather than retreating from digital infrastructure, it defines a minimal protocol for **distributed authenticated expression** — a set of invariants that, when satisfied, produce a verifiable record of situated human experience across a network of participants over time. The protocol is medium-agnostic: its first domain is poetry, but its formal structure applies wherever the goal is to interrupt, confront, record, authenticate, and preserve lineage across a distributed set of human contributors.

## The Protocol

The Prufrock Protocol is defined by five invariants, all of which are protocol constants — they hold across every instantiation, regardless of domain or medium:

1. **Interrupts.** The protocol reaches into a participant's ongoing experience at a moment not of their choosing. The interruption is the protocol's temporal anchor: it binds the contribution to a specific moment in a specific life.

2. **Confronts.** The interruption carries a payload: a prior contribution from someone else in the network. The participant does not respond to a blank prompt or to their own prior work. They are confronted with another person's authenticated moment — a thesis against which their present experience becomes antithesis.

3. **Records.** The participant's response is captured as a signed contribution tuple: content, parent hash(es), author key, prompt timestamp, response timestamp, coarse geolocation, and cryptographic signature. What is not recorded — the participant's full mental state, the alternatives they considered, the texture of the moment beyond what they chose to express — is the protocol's **negative space**, preserved by design.

4. **Authenticates.** Every contribution is cryptographically signed and hash-chained to its parents. The signature binds content to identity; the timestamps bind it to a moment; the geolocation binds it to a place; the parent hashes bind it to lineage. Together, these produce a contribution that is not merely stored but *situated* — authenticated not just as "from someone" but as "from this person, here, now, in response to that."

5. **Preserves lineage.** Each contribution commits to specific ancestors via cryptographic hash reference. The result is a directed acyclic graph of authenticated moments — a structure in which every node knows its parents and any tampering with an ancestor invalidates every descendant. The graph is the protocol's memory; it cannot be silently revised.

These five invariants define what makes something a Prufrock interaction. Everything else is parameterised.

## Protocol and Experiment

The Prufrock Protocol is parameterised. Its formal specification distinguishes **protocol constants** [P] from **experiment variables** [E]: the constants define the protocol's identity; the variables define a specific instantiation.

The constants are structural: the signature scheme (Ed25519), the hash function (SHA-256), the clock domain (UTC), geographic resolution (H3 level 5), append-only ledger structure, self-exclusion (you are never prompted with your own work), prompt anonymity (you respond to contributions, not to people), and forfeit recording (absence is data — the ledger does not pretend silence didn't happen).

The variables are configurational: cohort size, response window, response medium (text, audio, image, video, mixed), response unit, prompt depth, interruption timing, selection rule, form constraints, seed source. A specific combination of these variables defines an **experiment** — a concrete instantiation of the protocol with a defined population, duration, and output form.

This separation matters. It means the protocol can be studied as a formal object independent of any particular experiment, while experiments can be compared as points in a shared parameter space. It also means the protocol can migrate across domains without losing its identity: a Prufrock experiment using sonnets and a Prufrock experiment using field recordings of birdsong satisfy the same five invariants and produce the same kind of authenticated, lineage-preserving record.

## The First Domain: Poetry

The first experiments use poetry — specifically, the sonnet — as their response medium. This is not arbitrary.

Poetry is perhaps our oldest compression algorithm. It distills subjective moments of individual reflection into form: originally into prescribed structures (meter, rhyme, stanza), now by recalling their echoes. A line of poetry compresses an experience into language shaped by constraint, and in doing so creates space — negative space — for the reader's inference and interpretation.

Generative AI models also compress human culture, but do so statistically and anonymously, deriving patterns of association from past human artefacts. Both compression methodologies lose fidelity along the way. The question is *what* each chooses to preserve and *what* it sacrifices.

The moment — the situated, timestamped, geolocated instant of individual experience — is precisely what generative models discard in favour of associational patterns. A timestamp or a person's name is just another optional variable in a probability distribution. In poetry, the moment is the central element preserved. The tradeoffs run in the opposite direction: poetry creates space for inference and interpretation within the consciousness of the reader. This is the space that generative models attempt to fill with statistically quantifiable certainty, whereas poetry attempts to preserve its framing as negative space.

The Prufrock Protocol juxtaposes these forms of compression as complementary, situating itself as a third thing — neither the raw private experience nor its synthetic statistical ghost, but an authenticated, situated, human-originated cultural artefact that stands against both.

## Beyond Sonnets

The sonnet trial is the first experiment, not the last. The protocol's parameterisation supports:

- **Ghazal**: couplet-based response units, radif (refrain) constraints, round-robin selection — testing the protocol with a form built around repetition and variation rather than progressive argument.
- **Sestina**: stanza-level response units, end-word spiral rotation — testing whether the protocol's interruption mechanism can sustain a form that demands extraordinary constraint memory across contributions.
- **Free-form**: no form constraints, the protocol reduced to its five invariants alone — isolating the contribution of structure from the contribution of the protocol itself.
- **Non-textual media**: audio, image, or video as response medium. The protocol's authentication, lineage, and tamper-evidence properties hold uniformly regardless of medium — a photograph, cryptographically signed and hash-chained to a prior photograph, satisfies the same invariants as a line of verse.

Each experiment is a point in the protocol's parameter space. Comparing across experiments reveals which properties emerge from the protocol's constants and which from the experiment's variables — a question that is, at heart, a question about what the protocol *is* versus what it *does in a particular instance*.

## The Ledger

Most cryptographic ledgers attempt to solve issues of financial trust. Prufrock explores their use in authenticating expressions of situated human experience. The need is, ironically, more urgent: the collapse of centralised banking systems remains theoretical; the collapse of our trust in words and images has arrived.

The poem-ledger is an append-only authenticated log. When prompt depth is one, the parent relation forms a directed forest; when greater, a directed acyclic graph. Chains through the graph are poems — maximal paths from genesis seed to terminal contribution, each node a verified moment of confrontation and response.

The ledger records what happened. It also records what didn't: forfeits are permanently inscribed. The protocol insists that silence is data, not absence of data. This is a design decision about the relationship between a protocol and the world it observes — a decision to choose thoroughness over the efficiency of quietly moving on.

## An Enduring Artefact

Each completed chain — each poem, each sequence of authenticated contributions — becomes a novel cultural artefact. It records a dialectical progression: a prior contribution (thesis) meets a participant's situated moment (antithesis) and produces a new contribution (synthesis). It does so globally and longitudinally through verified responses to micro-moments over time.

Although inspired by collaborative writing exercises such as the "exquisite corpse," the introduction of randomised interruption, forced confrontation with another's authenticated expression, and cryptographic verification of human authorship transcends this lineage. It is an experiment in marking time through moments of attention, reflection, and response — and a timely counterpoise to the erosion of authenticity in digital shared experience.

The artefacts are not merely the poems. The artefact is the ledger itself — a cryptographically authenticated record of how human beings, distributed across geography and timezone, responded to each other's moments over time. It is, in a precise sense, a protocol for making shared memory durable in an era that has learned to fabricate memory at scale.

## For Protocol Theorists

The Prufrock Protocol is small, fully specified, parameterised, and simulatable. It is a protocol that can actually be implemented and studied — distinguishing it from the usual examples in protocol theory (climate treaties, blockchain governance) that are too large to experiment with.

It offers several contributions to protocol theory proper:

The **compression-fidelity trade** names a property every protocol possesses but few make explicit: the relationship between what a protocol records and what it must discard. Prufrock's contribution tuple — seven fields per contribution — is a compression specification. The unrecorded remainder is the protocol's negative space. This trade can be analysed, compared across protocols, and potentially nondimensionalised.

**Negative space as design category** inverts the usual analytical frame. Protocol theory studies what protocols do — their rules, states, transitions, observables. Prufrock introduces a formal concept for what protocols *don't do* and argues this is equally important. The unrecorded dimensions of an interaction are the space in which participants exercise judgement, agency, and meaning-making. A protocol's negative space may determine its susceptibility to drift: too large, and participants fill it with uncoordinated practices that diverge; too small, and the protocol becomes brittle.

**Aesthetic enforcement** names a class of constraint with no enforcement mechanism in the traditional sense but enormous structuring power. A sonnet's rhyme scheme or a ghazal's radif are not enforced by punishment, consensus, or cryptography. They are enforced by visible commitment — violations are apparent to subsequent participants through the stigmergic surface of the poem-in-progress. This is coordination without consensus, and it may generalise beyond aesthetic domains.

**Situated authentication** extends authentication from binding content to identity to binding content to a specific moment and place. Most protocols authenticate *actions*. Prufrock authenticates *situated moments of human experience* — the fact that a specific person, in a specific place, at a specific time, was confronted with another's expression and responded.

## The Overarching Question

The Prufrock Protocol asks whether, in an era of synthetic media and accelerated attention, we might still construct durable shared memory from small moments of authentic human expression — interrupted, confronted, recorded, authenticated, and woven into lineage.

It asks this not as a poetic conceit but as a protocol-theoretic proposition: that the five invariants, applied across domains, produce a class of cultural artefact that is neither private journal nor public broadcast nor synthetic generation, but something else — a third thing, authenticated and situated, that resists the specific failure mode of our moment.

The poetry is where it begins. The protocol is what it is.
