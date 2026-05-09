# Spec: Prufrock Protocol Experiment Simulator

## 1. Purpose

Simulate a complete run of the Prufrock Protocol given a set of participant dossiers (from the dossier generator — see `dossier-generator.md`) and an experiment configuration. The simulator executes the protocol mechanics: seed selection, schedule generation, interruption timing, prompt routing, response generation, lineage tracking, and forfeit handling.

The simulator knows the protocol. The dossier generator knows the people. This spec covers only the protocol execution.

The sonnet experiment runs 14 poets × 14 poems × 14 days. Each poem is collectively authored: every poet contributes exactly one line to each poem over the course of the experiment, via a Latin-square assignment that maximises authorial diversity per poem. No poet owns any poem; all poems have the most varied possible mix of contributors. The simulator is parameterised to support other configurations.

## 2. Inputs

### Required

1. **Dossier file(s)** — JSON output from the dossier generator. One file per cohort, or a combined file with multiple cohorts.
2. **Experiment config** — YAML file specifying protocol parameters.
3. **Seed poem config** — YAML file specifying the historical poem and which lines to extract as prompts.

### Experiment config schema

```yaml
experiment:
  name: "sonnet-trial-alpha"
  poet_count: 14                 # participants per cohort
  poem_count: 14                 # collaborative poems built in parallel (= poet_count)
  poem_length: 14                # contributed lines per poem (excludes seed lines)
  duration_days: 14
  seed_line_count: 2             # lines extracted from historical poem; shared initial prompt for all poems
  prompt_line_count: 2           # consecutive lines shown to each poet (always the last 2 of assigned poem)
  response_window_hours: 4
  interruption_mode: uniform     # uniform | poisson
  poem_assignment: latin_square  # assignment of poets to poems each day; maximises authorial diversity
  start_date: "2026-06-01"      # simulated start date

protocol_variants:
  allow_media: false
  allow_revision: false
  line_length_max: null
  form_constraint: null          # "sonnet" | "free" | null

runs:
  - id: run_a
    cohort: poet                 # matches cohort key in dossier file
    dossier_file: data/dossiers-poets.json
  - id: run_b
    cohort: layperson
    dossier_file: data/dossiers-lay.json
```

### Seed poem config schema

```yaml
seed:
  title: "Sonnet 18"
  author: "William Shakespeare"
  full_text: |
    Shall I compare thee to a summer's day?
    Thou art more lovely and more temperate:
    Rough winds do shake the darling buds of May,
    And summer's lease hath all too short a date:
    Sometime too hot the eye of heaven shines,
    And often is his gold complexion dimm'd;
    And every fair from fair sometime declines,
    By chance, or nature's changing course untrimm'd;
    But thy eternal summer shall not fade,
    Nor lose possession of that fair thou ow'st;
    Nor shall death brag thou wander'st in his shade,
    When in eternal lines to time thou grow'st:
    So long as men can breathe, or eyes can see,
    So long lives this, and this gives life to thee.
  seed_line_numbers: [10, 11]    # 0-indexed; lines 12-13 (before couplet)
  author_birth_year: 1564
  author_death_year: 1616
  publication_year: 1609
  location:
    city: London
    country: England
    lat: 51.5074
    lon: -0.1278
  rights_status: global_pd_confident
```

## 3. Protocol execution

### 3.1 Poem assignment generation

For each run, generate a 14×14 Latin square assigning poets to poems: `assignment[day][poet_index] = poem_index`. Each poet writes into exactly one poem per day, and each poem receives exactly one line per day. Over 14 days, every poet contributes to every poem exactly once — the maximum possible authorial diversity.

The Latin square is derived from the random seed (seeded cyclic shift: row `d` is a rotation of row `d-1` by an offset determined by the seed). It is committed before the experiment begins and recorded in the output.

### 3.2 Day-by-day execution

For each day `d` in `1..duration_days`, for each poet `p`:

1. **Look up poem assignment**:
   - `assigned_poem = assignment[d][p]`
   - The poet is contributing line `d` to `assigned_poem` (their `d`-th contribution across the experiment)

2. **Determine prompt lines**:
   - Day 1: both seed lines (shared by all poems on day 1 — divergence begins on day 2 as line 1 of each poem differs by author)
   - Day 2+: the last two consecutive non-forfeited lines of `assigned_poem` (lines `d-2` and `d-1`, or seed lines if `d-1` is forfeited, working backwards until two lines are found)
   - The poet never sees their own prior contributions in the prompt (the Latin square guarantees a poet does not return to any poem they already wrote)

3. **Generate interruption time**:
   - Sample within poet's availability window (from dossier)
   - Mode: uniform or Poisson per config
   - Record as UTC timestamp using poet's timezone

4. **Generate moment context**:
   - Time of day (derived from interruption time + timezone)
   - Weather: plausible for location + season (derived from start_date + day offset)
   - Situational context: brief phrase generated from poet's dossier (occupation, setting)

5. **Check for forfeit**:
   - Roll against poet's `forfeit_probability` (from dossier)
   - If forfeit: record line slot as forfeited (a gap in that poem); the poem's prompt on the next day steps back to the last two non-forfeited lines

6. **Generate response** (if not forfeited):
   - LLM call with structured prompt (see §4)
   - Record response text, response timestamp (interruption + latency), location

7. **Record lineage**:
   - Parent line references: always the two prompt lines — either `seed:{line_number}` or `{poem_id}:{line_number}`
   - Author of each parent line recorded

### 3.3 Poem assembly

After all days complete, assemble each of the 14 collaborative poems:
- Ordered sequence of 14 lines (or fewer if forfeits created gaps)
- Each line annotated with: day, author ID, prompt lines received, timestamps, location, moment
- No poem is attributed to any single poet; all are purely collective works

## 4. Response generation

### LLM prompt structure

```
You are simulating a poet in a distributed poetry protocol experiment.

POET PROFILE (private — not visible to others):
{dossier fields: background, voice_notes, emotional_baseline, influences}

THE MOMENT:
It is {local_time} on {date}. You are in {city}, {country}.
Weather: {weather}. You are {situational_context}.

THE TWO LINES YOU HAVE BEEN GIVEN (from a poem in progress — you did not write these):
{prompt_line_1}
{prompt_line_2}

Write the next line of this poem. Your line will be line {line_number} of {poem_length}.
Rules:
- One line only
- Write in your own voice (see profile) — but in response to the momentum of the pair above
- This is line {line_number} of {poem_length} — {positional_guidance}
- Do not repeat words from the given lines unless deliberately echoing for effect

Respond with the line only, no explanation.
```

### Positional guidance

- Line 1: "opening — this is the poem's first step beyond its seed"
- Lines 2–4: "early development — the poem is finding its voice"
- Lines 5–7: "mid-poem — build on the established momentum"
- Lines 8–10: "deepening — the poem's centre of gravity"
- Lines 11–12: "turning — begin to move toward resolution"
- Line 13: "penultimate — maximum tension before close"
- Line 14: "final line — land it; this is the last thing said"

### Quality controls

- Generate 3 candidates per response
- Score each for:
  - Voice consistency with this poet's dossier (voice_notes, emotional_baseline)
  - Lexical distance from the two prompt lines (reject >80% overlap)
  - Lexical distance from all other lines already written in this poem (avoid repetition within the collaborative work)
- Select highest-scoring candidate
- Log all candidates and scores for debugging

## 5. Response latency model

```python
def generate_latency(participant: ParticipantDossier, line_number: int) -> int:
    """Returns latency in seconds."""
    base_median = {
        "impulsive": 600,     # 10 min
        "deliberate": 1800,   # 30 min
        "erratic": 1200       # 20 min, but high variance
    }[participant.behavioural_traits.response_speed]

    # Line 14 takes longer (closing pressure)
    position_factor = 1.0 + (0.3 if line_number >= 13 else 0.0)

    # Erratic participants have higher variance
    sigma = 0.8 if participant.behavioural_traits.response_speed == "erratic" else 0.4

    latency = lognormal(log(base_median * position_factor), sigma)
    return min(int(latency), response_window_hours * 3600)
```

## 6. Output schema

Single JSON file, directly consumable by the visualisation SPA (see `visualisation.md`).

Primary output entities are **poems** (the 14 collaborative works). Poets appear as a lookup table and via per-line author attribution.

```json
{
  "meta": {
    "experiment_name": "sonnet-trial-alpha",
    "seed_poem": { "...seed config fields..." },
    "config": { "...experiment config..." },
    "generated_at": "2026-05-09T...",
    "random_seed": 42
  },
  "cohorts": [
    {
      "id": "run_a",
      "cohort": "poet",
      "dossier_hash": "sha256:...",
      "participants": [ "...full dossiers, embedded, keyed by id..." ],
      "poem_assignment": [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
        [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,  1],
        "...14 rows, one per day; value = poem index assigned to that poet on that day..."
      ],
      "poems": [
        {
          "id": "poem-01",
          "lines": [
            {
              "line_number": 1,
              "day": 1,
              "author_id": "poet-07",
              "text": "The summer I remember had no owner",
              "prompt_lines": [
                { "ref": "seed:11", "text": "Nor shall death brag thou wander'st in his shade,", "author": "William Shakespeare" },
                { "ref": "seed:12", "text": "When in eternal lines to time thou grow'st:", "author": "William Shakespeare" }
              ],
              "prompt_delivered_utc": "2026-06-01T14:23:00Z",
              "response_utc": "2026-06-01T14:41:00Z",
              "latency_seconds": 1080,
              "location": { "city": "Accra", "country": "Ghana", "lat": 5.6037, "lon": -0.1870 },
              "moment": {
                "local_time": "14:23",
                "weather": "humid, 31°C, building clouds",
                "context": "office, between student consultations"
              },
              "candidates_generated": 3,
              "selection_score": 0.87,
              "forfeited": false
            }
          ]
        }
      ]
    }
  ]
}
```

To reconstruct a single poet's contributions across all poems: query `poem_assignment` for every `(day, poem)` where `poet_index = p`, then look up that `poem.lines[day]` entry. This produces the poet's 14-line "authorial trail" across the corpus.

## 7. Thematic concern tagging

### Purpose

The protocol's intended lifespan spans centuries. To make visible the continuity of human concerns across that timescale — from seed poems written hundreds of years ago through to responses written today — the simulator applies AI-driven thematic analysis to both the seed and every completed poem.

This data powers the Concerns View in the visualisation (see `visualisation.md` §4.6).

### Concern taxonomy

A controlled but extensible vocabulary of timeless human concerns:

| Concern | Description |
|---|---|
| `mortality` | Impermanence, death, the finite |
| `love_unrequited` | Longing, desire without return |
| `love_present` | Connection, intimacy, tenderness |
| `nature_seasons` | Relationship to natural world, seasonal cycles |
| `social_anxiety` | Performance of self, fear of judgement |
| `memory` | Remembering, forgetting, nostalgia |
| `power` | Domination, subjugation, resistance |
| `solitude` | Alienation, aloneness (chosen or imposed) |
| `wonder` | Awe, the numinous, beauty |
| `domestic` | Routine, home, the everyday |
| `grief` | Loss, mourning, absence |
| `identity` | Selfhood, becoming, masks |
| `time` | Ageing, duration, the clock |
| `freedom` | Constraint and liberation |
| `faith` | Belief, doubt, the transcendent |
| `body` | Embodiment, sensation, physicality |
| `language` | Words themselves, communication, silence |

The taxonomy is extensible: the tagger may propose new concerns if a poem's content doesn't fit existing tags, but should prefer existing tags where possible.

### Tagging process

#### Seed poem tagging

At experiment initialisation, the full seed poem is analysed:

```
LLM prompt:
  Given this poem, identify which timeless human concerns it engages with.
  For each concern, cite the specific line(s) that carry it and rate intensity (0.0–1.0).
  Use only concerns from the provided taxonomy unless the poem genuinely introduces one not covered.
  
  Poem: {full seed poem text}
  Taxonomy: {concern list}
  
  Return: list of { concern, intensity, line_numbers[] }
```

#### Collaborative poem tagging

After all 14 lines of a collaborative poem are generated, the completed poem is tagged as a whole:

```
LLM prompt:
  Given this poem (written line by line over 14 days, each line by a different poet
  responding to the preceding pair), identify which timeless human concerns it engages with.
  For each concern:
    - Rate intensity (0.0–1.0)
    - Cite which line(s) carry it most strongly
    - Note whether this concern was inherited from the seed prompt or introduced in the collaborative chain
  
  Seed poem concerns for reference: {seed_concerns}
  Collaborative poem: {full poem text with line numbers}
  Taxonomy: {concern list}
  
  Return: list of { concern, intensity, line_numbers[], origin: "inherited" | "introduced" }
```

#### Per-line tagging (optional, for drill-down)

For finer granularity, each line can be tagged individually during generation. This is lighter-weight — just the top 1–2 concerns per line:

```
After generating a line, tag:
  { line_number, concerns: [{ concern, intensity }] }
```

### Output schema additions

The simulation output JSON gains concern data at two levels:

```json
{
  "meta": {
    "seed_poem": {
      "...existing fields...",
      "concerns": [
        { "concern": "mortality", "intensity": 0.9, "line_numbers": [10, 11, 12] },
        { "concern": "love_present", "intensity": 0.7, "line_numbers": [1, 2, 3, 14] },
        { "concern": "time", "intensity": 0.6, "line_numbers": [4, 5, 12, 13] }
      ]
    }
  },
  "runs": [
    {
      "poems": [
        {
          "...existing fields...",
          "concerns": [
            { "concern": "mortality", "intensity": 0.7, "line_numbers": [3, 8, 14], "origin": "inherited" },
            { "concern": "solitude", "intensity": 0.6, "line_numbers": [1, 5, 9], "origin": "introduced" },
            { "concern": "memory", "intensity": 0.5, "line_numbers": [2, 7, 11], "origin": "introduced" }
          ],
          "line_concerns": [
            { "line_number": 1, "concerns": [{ "concern": "solitude", "intensity": 0.8 }] },
            { "line_number": 2, "concerns": [{ "concern": "memory", "intensity": 0.7 }] }
          ]
        }
      ]
    }
  ]
}
```

### Concern continuity metrics

The simulator computes and exports:

- **Inheritance rate**: what proportion of the seed's concerns appear in each collaborative poem?
- **Introduction rate**: how many new concerns are introduced across the 14-poet chain?
- **Concern drift**: how do concerns shift line by line as different poets contribute?
- **Cohort divergence**: do the 14 poet-cohort poems and 14 layperson-cohort poems gravitate toward different concerns from the same seed?
- **Temporal projection**: given a seed from year X and responses from year Y, which concerns bridge the gap?

These metrics appear in the `prufsim stats` output and feed the visualisation's Concerns View.

---

## 8. Implementation

### Stack

- Python 3.12+
- Pydantic (shared models with dossier generator)
- Typer CLI
- `anthropic` or `openai` SDK for response generation
- YAML configs
- JSON output
- pytest

### CLI

```
prufsim run --config config/sonnet-trial.yaml --seed 42 --output data/sim-output.json
prufsim validate data/sim-output.json
prufsim show-lineage data/sim-output.json --participant poet-01 --run run_a
prufsim export-prompts data/sim-output.json --format jsonl
prufsim stats data/sim-output.json   # summary: forfeit rate, latency distribution, voice scores
```

### Directory structure

```
pruf-sim/
  pyproject.toml
  config/
    sonnet-trial.yaml        # experiment config
    seeds/
      shakespeare-18.yaml
      keats-chapman.yaml
      shelley-ozymandias.yaml
  pruf_sim/
    models.py                # shared Pydantic schemas (imports dossier models)
    protocol.py              # rotation, prompt routing, forfeit handling
    timeline.py              # interruption timing, latency generation
    moments.py               # weather, situational context generation
    responses.py             # LLM-based line generation + quality scoring
    concerns.py              # thematic concern tagging + continuity metrics
    lineage.py               # parent tracking, poem assembly
    output.py                # JSON serialisation
    cli.py
  tests/
  data/
    dossiers-poets.json      # input from dossier generator
    dossiers-lay.json
    sim-output.json          # output for visualisation
```

## 8. Relationship to other components

```
scraper.md ──────→ poem corpus (historical seeds)
                         │
                         ▼
dossier-generator.md ──→ participant dossiers
                         │
                         ▼
simulation.md ──────────→ experiment output JSON
(this spec)              │
                         ▼
                   visualisation.md ──→ SPA demo
```

## 9. Acceptance criteria

1. Accepts dossier files from the dossier generator without transformation
2. Accepts experiment config as YAML — changing `poet_count`, `poem_length`, `duration_days` produces valid shorter/longer runs
3. Generates a valid 14×14 Latin square: each poet appears exactly once per row (day) and exactly once per column (poem); no poet writes consecutive lines in the same poem
4. Each poet's prompt on Day 2+ is always the last 2 consecutive non-forfeited lines of their assigned poem; no poet ever receives lines they authored
5. Generates plausible response lines differentiated by participant voice
6. Latency model produces realistic distributions (not uniform)
7. Forfeits leave a gap in the poem; subsequent assigned poet receives the last 2 non-forfeited lines before their position
8. Every line has correct lineage metadata: exactly 2 parent refs (seed lines or preceding poem lines), tracing back to the seed
9. Output JSON validates against schema and is directly consumable by the visualisation SPA; `poem_assignment` matrix is included
10. Deterministic: same seed + same dossiers + same config = same output
11. Stats command reports meaningful quality metrics (forfeit rate, latency percentiles, voice distinctiveness scores, authorial diversity per poem)
12. Every completed collaborative poem has concern tags with intensities and origin (inherited/introduced)
13. Seed poem has concern tags that are traceable through to collaborative poems
14. Concern continuity metrics (inheritance rate, introduction rate, cohort divergence) are computed and exported
