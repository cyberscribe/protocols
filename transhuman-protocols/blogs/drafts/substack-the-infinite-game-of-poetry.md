# The Infinite Game of Poetry

*Why I gave a talk on prosody to a room of protocol designers — and what poetry might still have to teach engineering.*

---

In July 2025, Venkat Rao asked if I would talk about poetry at his Protocol Town Hall. Protocol Town Hall is a weekly series convened by the Summer of Protocols community: technologists, researchers, and a few others thinking carefully about what *protocol* really means once you stop assuming it lives in an RFC.

The invitation arrived just before I left for a writing retreat in southwest Ireland, so I had a week of green and rain-soaked walks in which to think it over. The result is the talk embedded below; what follows is the argument in compressed form — for anyone not ready for an hour of video, and for those who have watched it and want the ideas in writing.

https://www.youtube.com/watch?v=fKqNSE9NmGU

## Three definitions, in increasing order of mischief

The Greek *protokollon* literally means "first glued" — the preface, the metatext that tells you how to read what follows. From there we get the standard sense: behavioural guidelines for repeatable outcomes (push down and twist), and then communication guidelines for interoperability (the P in HTTP, in TCP). I think of these as **first-order protocols** — the ones already in the dictionary.

In conversation with Venkat and the community, another definition kept coming up: the protocol as *engineered argument* — a thing that is not finished but always being negotiated. The internet's tension between distributed, asynchronous origins and our streaming demands for sequentiality and low latency is not a fixed protocol; it is an ongoing **protocoling**. RFCs are how that argument continues.

And running through both: **tension** — which I'll define here as *a compromise plus an added conflict*. Hold that one. It will do a lot of work later.

Poetry, I want to argue, is the second-order kind of protocol — protocoling, ongoing, opinionated, and built around a tension it has no intention of resolving.

## Poetry as compression algorithm

Years ago, as a young university student, I met Seamus Heaney when he came to read from his new translation of *Beowulf*. After a long opening litany of a leader's deeds, the verse arrives at a quietly emphatic verdict: *that was a good king*. The litany is a kind of preface — a protocolon, before we knew to call it one. And Old English verse, like much oral tradition, runs on alliteration. Alliteration, meter, rhyme — what they share is **concision**. They force the language to compress.

So one of my working definitions: poetry is one of our oldest living compression algorithms. Lynne Kelly's work on memory codes shows how indigenous song-lines pack ecological knowledge, ancestry, and identity into compressed verse. Werner Herzog has suggested that *homo spiritualis* might serve as a fitter title than *homo erectus* for our species — the reaching for the transcendent through art is just *that* common across the timeline. Heaney's own poem *Punishment*, written from inside the Northern Irish Troubles, looks at a bog body — a young woman ritually drowned — and finds in it what he calls "the exact and intimate tribal revenge." That is what compression does: it carries the past forward intact enough to indict the present.

Marvin Bell, who was my teacher and became something like a Heaney to me, put the move at the heart of it as cleanly as anyone: **poetry uses words to transcend words.** That is the line I keep returning to.

## Three nested infinite games

If poetry uses words to get beyond words, then the set of words plus the operation we call poetry is greater than the sum of its parts. That makes it a Gestalt system. True, but unremarkable on its own — there are many Gestalt systems.

More interesting is its **Gödelian** quality. In any formal axiomatic system there are truths that cannot be proven from within. Poetry, by definition, reaches for what its raw material — words — cannot quite contain. That makes it an *unwinnable, impossible, and important* game. Which is to say: an infinite game in James Carse's sense, or what Hermann Hesse called the Glass Bead Game. Magister Ludi: *No permanence is ours. We are the flood that flows to fit whatever form it finds.*

Three layers, then, each nested in the next:

- **Poetrying** — using words to get beyond words. The act.
- **Poeming** — making the artefact. A poem listens to itself as it goes; every line is informed by the line before it. (Not unlike how an LLM streams tokens — though where the model is autocompleting plausibility, the poem is autocompleting attention.) A poem is also a quarrel — a dialectic between selves, to which you keep adding third and fourth selves. Tension as compromise plus conflict, again.
- **Poeting** — being a poet every day. Noticing the inner environment, the outer environment, what you read and what you write, and synthesising it iteratively over a lifetime. Poetry as what Whitehead would call an operating system; a way of being.

## The fundamental algorithm

Marvin Bell distilled the craft to one rule:

> Learn the rules, break the rules, make up new rules, break the new rules.

It is head-recursive in the formal sense. And anything you can write recursively you can write iteratively, so for the engineers in the room:

`P(r, n) = B(B(L(r_{n-1}))) → r_n`

The interesting move is the breaking function. It is what lets the system address its own incompleteness, and it is the thing missing from many of the protocols we design for ourselves — corporate constitutions, governance structures, even some communication protocols. Without an explicit break-and-remake mechanism, systems calcify. With one, they evolve.

The two failure modes show up in the corpus as cleanly as anything I could have engineered.

When you *don't learn* the rules, you get William McGonagall's *Tay Bridge Disaster* — the actual 1879 bridge collapse rendered in verse so tone-deaf to its own gravity that it concludes, with a straight face, that we should build better houses. It has the trappings of poetic language and none of the listening.

When you *only learn* the rules and never break them, you get this — ChatGPT's response to *write one of the greatest poems of all time*:

> When the world forgets your name,
> 
> and time dissolves the edge of flame…

Clean rhyme, lofty diction, gestures at the eternal. ChatGPT scored itself 85–88 out of 100 against Mary Oliver, Jane Hirshfield, late Rilke. Michael Dalvean's poetry-assessor model — trained on Clark–Paivio word norms — scored it −0.6, closer to amateur than to pro. If a student handed it in, I'd say it suffers from **lofty abstraction**: ideas in the space of ideas, with rhetorical flourishes and a thin layer of music.

That gap between what an LLM has learned poetry *says* and what poetry *does* is precisely the gap *Dead Poets Society* is dramatising when Robin Williams's character has his students physically tear out the textbook preface — the protocolon that taught them to graph poems on a two-axis plot of importance against execution. The training data of the LLM is, in effect, what those students have been taught to unlearn. Ask it for one of the *worst* poems instead and you get *Ode to My Toaster* — *a dolphin in a sea of stew* — and Marvin's point holds: try to write a bad poem; you'll invariably find something interesting. The bar is low, and it is still hard to clear in the wrong direction.

## What this offers the protocol designer

Three things poetry hands the protocol designer.

**The breaking function is what most protocols leave out.** A protocol that can only learn its own rules eventually meets a Tay Bridge moment. A protocol that can break and remake them — visibly, with rules of engagement for doing so — has a chance at evolving without catastrophe. RFCs at their best are the breaking function for the internet.

**Constraint provokes presence.** The writing exercises in the talk impose absurd constraints — count the syllables of what you just wrote and use the same pattern again; give an object in the room the voice of someone you hate, then the voice of someone you admire. They feel impossible until you're inside them, at which point you've stopped narrating yourself and started noticing. Improv has the same property. So, often, do the best engineering specs — the ones tight enough to force real choices.

**Tension is the unit of generativity.** Compromise plus conflict. Resolve a quarrel between two selves and you've created the conditions for a third self to enter and complicate things. Paul Valéry: *a poem is never finished, only abandoned.* The same is true of any protocol whose users are still alive.

## The view from the window in Ireland

I want to leave you with the poem that taught me most clearly what *poeting* looks like as an operating system — Marvin Bell's *Wednesday*, which moves in a single sweep from gray rainwater on grass to *the palpable Sublime [flickering] as motes on broad leaves*, and then with a kind of whiplash to *a match-head in my thoughts* the next morning at work. The diction climbs and undercuts itself, climbs and undercuts itself. That is the poet's daily protocol — sublime, absurd, quotidian, all swept into one Gestalt — practiced, as Bell put it, every day.

Rilke said the purpose of life is to be defeated by greater and greater things, and also to *live in the question*. If the purpose of poetry is poems, and the purpose of poems is poets, then those are protocols too — and probably the ones we most need now, in a world increasingly fluent in chatter.

The full talk runs about an hour, including the writing exercises and a Q&A with Venkat that gets into orality, mannerism, and why even at his most existential Marvin Bell stayed unpretentious. If you've made it this far, that's the next step.

---

**Watch the full talk:** *The Infinite Game of Poetry: Protocols for Living, Listening, and Transcending the Rules* on the Protocol Town Hall channel — [YouTube](https://www.youtube.com/watch?v=fKqNSE9NmGU).

**Companion materials:** [handouts PDF](https://www.robertpeake.com/files/2025/07/poetry-protocols-handouts.pdf) · [full transcript at robertpeake.com](https://www.robertpeake.com/archives/103816-the-infinite-game-of-poetry.html) · further reading on [Mnemosyne's Tango](https://gatomonodesign.de/wordpress/mnemosynes-tango-poetry-film-and-the-dance-of-memory/).
