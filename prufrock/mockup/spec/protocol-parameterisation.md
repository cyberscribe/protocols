# Spec: Prufrock Protocol Parameterisation

## 1. Purpose

Rework the Prufrock Protocol from a protocol-with-one-experiment into a generic protocol framework where specific experiments are named instantiations with different configuration variables. The sonnet trial becomes one experiment definition among many.

This spec defines the parameter space, the experiment definition format, the formal constraints each parameter introduces, and a set of candidate experiment definitions beyond the sonnet trial.

## 2. Relationship to existing documents

- **`formalisation.md`** already treats the sonnet trial as a "concrete instantiation" (§5). This spec makes that parameterisation explicit and comprehensive, replacing the hardcoded sonnet values with a configuration schema.
- **`README.md`** (the thread's public landing, formerly `pitch.md`) already frames sonnets as "The First Experiment: Poetry" with the protocol itself being form-agnostic ("Beyond Sonnets"). The form-agnostic framing is in place; this spec gives it teeth.
- **`simulation.md`** and **`dossier-generator.md`** already accept config files. This spec defines the canonical config schema they consume.

After this rework, `formalisation.md` §5 becomes a library of experiment definitions, not a single trial.

## 3. Protocol invariants (what never changes)

Regardless of experiment configuration, the Prufrock Protocol always:

1. **Interrupts** — participants receive prompts at moments not of their choosing
2. **Confronts** — the prompt is someone else's contribution, not the participant's own
3. **Records** — response, timestamp, location, and lineage are captured
4. **Authenticates** — contributions are cryptographically signed
5. **Preserves lineage** — every contribution traces its parentage back to the seed

These are the protocol's identity. Everything else is parameterised.

## 4. Parameter space

### 4.1 Seed parameters

| Parameter | Type | Description | Sonnet default |
|---|---|---|---|
| `seed_source` | enum | `corpus` (from scraper), `manual`, `generated` | `corpus` |
| `seed_work_type` | str | Form of the source work | `"sonnet"` |
| `seed_line_extraction` | enum | Which lines to extract: `last_n`, `first_n`, `volta`, `couplet`, `random`, `custom` | `volta` |
| `seed_line_count` | int | Number of lines extracted as the initial prompt | `2` |
| `seed_min_age_years` | int \| null | Minimum age of source work (years since publication) | `100` |
| `seed_language` | str | ISO 639-1 language code | `"en"` |
| `seed_rights_status` | str | Minimum rights tier required | `"global_pd_confident"` |

### 4.2 Cohort parameters

| Parameter | Type | Description | Sonnet default |
|---|---|---|---|
| `cohort_count` | int | Number of parallel cohorts running the same seed | `2` |
| `poet_count` | int | Participants per cohort (= number of collaborative poems built in parallel) | `14` |
| `cohort_profiles` | list[str] | Cohort type keys (from dossier generator) | `["poet", "layperson"]` |
| `cross_cohort_visibility` | bool | Can cohorts see each other's contributions? | `false` |

### 4.3 Prompt parameters

| Parameter | Type | Description | Sonnet default |
|---|---|---|---|
| `prompt_line_count` | int | Consecutive lines shown per round (always from the assigned poem) | `2` |
| `prompt_source` | enum | `sequential_pair_from_assigned_poem`, `random_peer`, `weighted_peer` | `sequential_pair_from_assigned_poem` |
| `prompt_attribution` | enum | `anonymous`, `attributed`, `delayed_attribution` | `anonymous` |

Note: `prompt_includes_own` is structurally impossible when `prompt_source` is `sequential_pair_from_assigned_poem` — the Latin square guarantees no participant is ever assigned the same poem twice in a row, so they cannot receive their own prior lines as a prompt.

### 4.4 Response parameters

| Parameter | Type | Description | Sonnet default |
|---|---|---|---|
| `response_unit` | enum | `line`, `couplet`, `stanza`, `free_block` | `line` |
| `response_count` | int | Number of units produced per round | `1` |
| `response_max_length` | int \| null | Character or word limit per unit (null = unconstrained) | `null` |
| `response_window_hours` | float | Time allowed to respond | `4` |
| `allow_revision` | bool | Can participant revise before window closes? | `false` |
| `allow_media` | bool | Can response include image/audio/video? | `false` |

### 4.5 Structure parameters

| Parameter | Type | Description | Sonnet default |
|---|---|---|---|
| `poem_length` | int | Total contributed lines per poem (= duration_days when rounds_per_day is 1) | `14` |
| `duration_days` | int | Calendar days the experiment runs | `14` |
| `rounds_per_day` | int | Interruptions per participant per day | `1` |
| `interruption_mode` | enum | `uniform`, `poisson`, `scheduled` | `uniform` |
| `poem_assignment` | enum | How participants are assigned to poems each round: `latin_square`, `random`, `round_robin` | `latin_square` |

`latin_square` ensures every participant contributes exactly once to every poem, and no participant is assigned the same poem on consecutive days (maximising authorial diversity per poem). Other modes relax these guarantees for shorter or pilot experiments.

### 4.6 Form constraints (optional)

| Parameter | Type | Description | Sonnet default |
|---|---|---|---|
| `form_constraint` | str \| null | Named poetic form, or null for free | `null` |
| `form_rules` | FormRules \| null | Structural rules derived from form | `null` |

#### FormRules schema

```yaml
FormRules:
  name: str                        # e.g. "sonnet", "ghazal", "sestina"
  total_lines: int                 # enforced poem length
  stanza_structure: list[int]      # lines per stanza, e.g. [4, 4, 3, 3] for Petrarchan
  rhyme_scheme: str | null         # e.g. "ABAB CDCD EFEF GG"
  refrain_rules: RefrainRules | null
  end_word_rules: EndWordRules | null  # for sestina
  meter: str | null                # e.g. "iambic pentameter" (advisory, not enforced)
  couplet_close: bool              # does the form end with a couplet?
  volta_position: int | null       # line number of expected turn
  additional_constraints: str | null  # free text for unusual forms
```

## 5. Experiment definition format

An experiment is a named, versioned configuration file:

```yaml
experiment:
  name: "sonnet-trial-alpha"
  version: "1.0"
  description: >
    14 poets × 14 collaborative sonnets × 14 days.
    Two cohorts (poets, laypeople) run in parallel from the same
    Shakespearean seed (Sonnet 18, lines 11–12). A Latin square
    assigns each poet to a different poem each day; every poem
    receives exactly one line per day from a different author.
    Each poet's prompt is always the last 2 consecutive lines of
    their assigned poem (anonymous). No poem belongs to any
    individual; maximum authorial diversity per poem is enforced
    by the Latin square structure.

  seed:
    source: corpus
    work_type: sonnet
    line_extraction: volta
    line_count: 2
    min_age_years: 100
    language: en
    rights_status: global_pd_confident

  cohorts:
    count: 2
    poet_count: 14
    profiles: [poet, layperson]
    cross_cohort_visibility: false

  prompt:
    line_count: 2
    source: sequential_pair_from_assigned_poem
    attribution: anonymous

  response:
    unit: line
    count: 1
    max_length: null
    window_hours: 4
    allow_revision: false
    allow_media: false

  structure:
    poem_length: 14
    duration_days: 14
    rounds_per_day: 1
    interruption_mode: uniform
    poem_assignment: latin_square

  form:
    constraint: sonnet
    rules:
      name: sonnet
      total_lines: 14
      stanza_structure: [4, 4, 4, 2]
      rhyme_scheme: null           # not enforced in this experiment
      meter: null                  # not enforced
      couplet_close: true
      volta_position: 9
```

## 6. Candidate experiment definitions

### 6.1 Ghazal experiment

```yaml
experiment:
  name: "ghazal-trial"
  description: >
    The ghazal's form — autonomous couplets linked by a refrain (radif)
    and rhyme (qafia) — maps naturally to the protocol's call-and-response.
    Each round produces a couplet. The refrain phrase is set by the seed.

  seed:
    source: corpus
    work_type: ghazal
    line_extraction: last_n
    line_count: 2                  # final couplet (maqta) of a classical ghazal
    min_age_years: 200
    language: en                   # English translations of Rumi, Hafiz, Ghalib

  cohorts:
    count: 1
    size: 7
    profiles: [poet]

  prompt:
    line_count: 2
    source: chosen_rotation
    attribution: anonymous

  response:
    unit: couplet
    count: 1
    window_hours: 6

  structure:
    poem_length: 7                 # 7 couplets (sher)
    duration_days: 7
    rounds_per_day: 1
    rotation_mode: round_robin

  form:
    constraint: ghazal
    rules:
      name: ghazal
      total_lines: 14
      stanza_structure: [2, 2, 2, 2, 2, 2, 2]
      rhyme_scheme: "AA BA CA DA EA FA GA"
      refrain_rules:
        type: radif
        phrase: null               # extracted from seed's final couplet
        position: end_of_second_line
      meter: null
      couplet_close: true
      volta_position: null
      additional_constraints: >
        Each couplet is thematically self-contained.
        The final couplet (maqta) traditionally contains
        the poet's name or pen-name — in this experiment,
        the participant's first name.
```

### 6.2 Sestina experiment

```yaml
experiment:
  name: "sestina-trial"
  description: >
    The sestina's rotating end-words are a natural fit for the protocol's
    lineage tracking. Six participants, six stanzas, six end-words that
    permute through a fixed pattern. The protocol enforces the rotation;
    the participants supply the lines.

  seed:
    source: corpus
    work_type: sestina
    line_extraction: custom
    line_count: 3                  # the envoi (final tercet)
    min_age_years: 100

  cohorts:
    count: 1
    size: 6

  prompt:
    line_count: 1                  # one line — the previous stanza's final line
    source: round_robin

  response:
    unit: stanza                   # 6-line stanza
    count: 1
    window_hours: 8

  structure:
    poem_length: 6                 # 6 stanzas + envoi
    duration_days: 7               # 6 stanzas + 1 day for envoi
    rotation_mode: permutation

  form:
    constraint: sestina
    rules:
      name: sestina
      total_lines: 39              # 6×6 + 3
      stanza_structure: [6, 6, 6, 6, 6, 6, 3]
      end_word_rules:
        words: null                # extracted from seed
        rotation: [6, 1, 5, 2, 4, 3]  # standard sestina spiral
      meter: null
      couplet_close: false
      volta_position: null
```

### 6.3 Free-form micro experiment

```yaml
experiment:
  name: "haiku-relay"
  description: >
    Minimal experiment: 5 participants, 3 rounds, 1 line shown.
    No form constraint. Useful as a quick pilot or onboarding exercise.

  seed:
    source: manual
    line_extraction: last_n
    line_count: 1
    min_age_years: null

  cohorts:
    count: 1
    size: 5

  prompt:
    line_count: 1
    source: random_peer
    attribution: delayed_attribution

  response:
    unit: line
    count: 1
    window_hours: 2

  structure:
    poem_length: 3
    duration_days: 3
    rotation_mode: random

  form:
    constraint: null
```

### 6.4 Long-form open experiment

```yaml
experiment:
  name: "open-chain-90"
  description: >
    90-day open experiment. One line per day, large cohort,
    no form constraint. Tests the protocol's durability and
    the evolution of voice over extended collaboration.

  seed:
    source: corpus
    line_extraction: last_n
    line_count: 2
    min_age_years: 500

  cohorts:
    count: 3
    size: 30
    profiles: [poet, layperson, scientist]

  prompt:
    line_count: 2
    source: weighted_peer
    attribution: anonymous

  response:
    unit: line
    count: 1
    window_hours: 12

  structure:
    poem_length: 90
    duration_days: 90
    rotation_mode: weighted

  form:
    constraint: null
```

## 7. Impact on existing documents

### formalisation.md

- §1 Domain: already parameterised — add explicit references to the config schema
- §5 Sonnet Trial: reframe as "§5 Experiment Definitions" with the sonnet as definition 5.1
- Add new §: "Form Constraint System" formalising how `FormRules` interact with the line validity predicate
- The line tuple $\ell$ may need an additional field for `response_unit` when units are larger than a single line

### pitch.md

- Frame the sonnet as the opening experiment, not the protocol itself
- Add a paragraph on the protocol's generality: ghazal, sestina, free-form, and forms not yet invented
- The pitch becomes stronger: this isn't a sonnet project, it's a protocol for distributed poetic composition that can instantiate any form

### simulation.md

- Already parameterised — ensure config schema matches this spec exactly
- Add form constraint handling: when `form_rules` is present, pass structural requirements to the response generator (rhyme scheme, end-words, refrain)
- Response generation prompt must adapt to response_unit (line vs couplet vs stanza)

### dossier-generator.md

- No changes needed — dossier generator is form-agnostic by design (correct separation)

### visualisation.md

- Poem view must adapt to variable stanza structures (not always 14 single lines)
- Timeline view: rounds_per_day > 1 means multiple cells per day
- Form constraint overlay: optionally show rhyme scheme, end-word rotation, refrain highlighting

### scraper.md

- Add seed extraction rules for non-sonnet forms (ghazal couplets, sestina envois)
- `seed_line_extraction` modes need corresponding extraction logic

## 8. Implementation priority

1. **Define the canonical config schema** as a Pydantic model (shared across simulator and visualisation)
2. **Refactor `simulation.md`** to consume the full config (most work is already done)
3. **Update `formalisation.md`** §5 to be a config library
4. **Build the sonnet experiment config** as the first named definition
5. **Build one non-sonnet config** (ghazal is the most tractable — couplet-based, clear rules)
6. **Update visualisation** to handle variable stanza structures
7. **Update pitch** last — once we can demonstrate two different experiment types

## 9. Acceptance criteria

1. Protocol config schema can express sonnet, ghazal, sestina, free-form, and 90-day open experiments without code changes
2. Simulator accepts any valid config and produces structurally correct output
3. Form constraints (when present) are passed to response generation and validated in output
4. Formalisation document treats experiments as named instantiations of the parameterised protocol
5. At least two experiment definitions (sonnet + one other) are fully specified and simulatable
6. Visualisation adapts layout to variable poem structures (stanza size, round count, response unit)
