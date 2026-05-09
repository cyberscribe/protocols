# Spec: Poet Dossier Generator

## 1. Purpose

Generate rich, internally consistent participant profiles ("dossiers") for use in Prufrock Protocol simulations. The dossier generator is a standalone component: it knows nothing about experiments, protocols, or poems. It produces people — with locations, voices, backgrounds, and behavioural tendencies — that downstream components (the experiment simulator, future casting tools) consume.

Separation rationale: the same dossier set should be reusable across different experiment configurations. A different experiment might want the same 28 profiles with a different protocol shape, or different profiles with the same protocol. The dossier generator is the stable input; the experiment simulator is the variable process.

## 2. Cohort types

The generator produces participants in named cohorts. Each cohort has a generation profile that governs the character of its members.

### Built-in cohort profiles

| Cohort key | Label | Character |
|---|---|---|
| `poet` | Serious poets | MFA-credentialed or equivalent, published, stylistically diverse. Literary influences are specific and nameable. Voice notes describe craft tendencies (compression, enjambment, imagism, confessional, etc.). |
| `layperson` | Laypeople | Mixed non-literary backgrounds. Voice notes describe how they naturally express themselves under pressure — not how they write poetry. Influences are life experiences, not literary traditions. |

### Custom cohorts

The generator should accept custom cohort profiles via config:

```yaml
cohorts:
  - key: scientist
    label: "Research scientists"
    character: >
      Working researchers across disciplines. Responses tend toward
      precision, metaphor drawn from their field, occasional jargon
      repurposed as imagery. Not trained writers but habitual explainers.
    influence_domain: "scientific fields and methodologies"
    voice_range: "precise to lyrical, field-specific metaphor"
```

## 3. Dossier schema

```yaml
ParticipantDossier:
  id: str                          # stable ID, e.g. "poet-07", "lay-03"
  cohort: str                      # cohort key
  name: str                        # generated, culturally plausible for location
  age: int                         # 22–75
  gender: str                      # for name/pronoun plausibility, not filtering
  location:
    city: str
    country: str
    region: str                    # state/province/county
    timezone: str                  # IANA timezone
    lat: float
    lon: float
    setting: str                   # "urban" | "suburban" | "rural" | "remote"
  language:
    primary: str                   # ISO 639-1
    additional: list[str]
    writes_in: str                 # language they'll compose in (usually primary)
  background: str                  # 2–3 sentence biography, naturalistic
  occupation: str                  # current or most recent
  education: str                   # brief, relevant to voice
  voice_notes: str                 # 2–3 sentences: how this person sounds on paper
  emotional_baseline: str          # temperament shorthand, e.g. "melancholic but wry"
  influences: list[str]            # 3–6 items: literary for poets, life for laypeople
  behavioural_traits:
    response_speed: str            # "impulsive" | "deliberate" | "erratic"
    verbosity: str                 # "terse" | "moderate" | "expansive"
    risk_tolerance: str            # "conservative" | "moderate" | "adventurous"
    forfeit_probability: float     # 0.0–0.15, base rate for missing a response window
  availability_window:
    start_hour: int                # local time, 0–23
    end_hour: int                  # local time, 0–23
    weekend_shift: int             # hours earlier/later on weekends, -3 to +3
  notes: str                       # any additional texture for the LLM generating responses
```

## 4. Generation constraints

### Geographic distribution

Per cohort of N participants:

- Minimum unique countries: `max(4, N // 3)`
- Minimum continents: `max(3, N // 5)`
- At least 1 participant in a rural or remote setting
- No more than 3 participants in the same country
- Timezone spread: standard deviation of UTC offsets ≥ 4 hours

### Demographic diversity

- Age range: at least one participant under 30, at least one over 60
- Gender: no more than 60% any single gender per cohort
- Names: culturally appropriate to location and age cohort
- Languages: at least 2 primary languages represented per cohort (participants still write in `writes_in`, but their background inflects their voice)

### Voice distinctiveness

Critical constraint: **no two participants in the same cohort should sound alike**. The generator must verify:

- No two `voice_notes` share more than 2 of the same descriptive adjectives
- No two `emotional_baseline` values are synonymous
- `influences` lists have ≤1 overlap within a cohort
- For poets: stylistic tendencies should span formalist ↔ experimental, lyric ↔ narrative, dense ↔ spare

### Internal consistency

Each dossier must be internally plausible:

- Education matches occupation matches background
- Location matches timezone matches cultural context of name
- Influences make sense for the person's age, location, and background
- Availability window is reasonable for their occupation and timezone
- Voice notes follow from background and influences, not contradict them

## 5. Generation process

### Step 1: Skeleton generation

Given cohort config and count, generate a distribution plan:

```
distribute_locations(count=14, min_countries=4, min_continents=3)
distribute_demographics(count=14, age_range=(22, 75), ...)
```

This produces a skeleton: 14 slots with assigned location, age bracket, and gender — ensuring constraints are met before filling in details.

### Step 2: Profile generation

For each skeleton slot, generate a complete dossier via LLM call with:

- The slot's assigned location, age, gender
- The cohort profile (character, influence domain, voice range)
- All previously generated dossiers in this cohort (to enforce distinctiveness)
- Explicit instruction to avoid overlapping voices

### Step 3: Distinctiveness validation

After all profiles are generated, run pairwise checks:

- Voice similarity score (lexical overlap in voice_notes + emotional_baseline)
- Influence overlap count
- Flag any pair scoring above threshold for regeneration

### Step 4: Output

Write dossier set to JSON.

## 6. Output format

```json
{
  "meta": {
    "generated_at": "2026-05-09T...",
    "generator_version": "0.1.0",
    "seed": 42,
    "config_hash": "abc123..."
  },
  "cohorts": [
    {
      "key": "poet",
      "label": "Serious poets",
      "count": 14,
      "participants": [
        {
          "id": "poet-01",
          "name": "Amara Osei",
          "cohort": "poet",
          "age": 34,
          "gender": "female",
          "location": {
            "city": "Accra",
            "country": "Ghana",
            "region": "Greater Accra",
            "timezone": "Africa/Accra",
            "lat": 5.6037,
            "lon": -0.1870,
            "setting": "urban"
          },
          "language": {
            "primary": "en",
            "additional": ["tw"],
            "writes_in": "en"
          },
          "background": "Published her first collection at 28 through a Ghanaian indie press. Teaches creative writing at the University of Ghana. Her work circles around migration within West Africa — not the diaspora narrative the international market expects.",
          "occupation": "Poet and lecturer",
          "education": "MFA, University of Michigan",
          "voice_notes": "Controlled intensity. Short declarative lines that build pressure through accumulation rather than imagery. Resists metaphor unless it earns its place. Influenced by Lucille Clifton's economy.",
          "emotional_baseline": "Watchful, deliberate warmth",
          "influences": ["Lucille Clifton", "Kofi Awoonor", "Warsan Shire", "highlife music lyrics"],
          "behavioural_traits": {
            "response_speed": "deliberate",
            "verbosity": "terse",
            "risk_tolerance": "moderate",
            "forfeit_probability": 0.03
          },
          "availability_window": {
            "start_hour": 6,
            "end_hour": 22,
            "weekend_shift": 1
          },
          "notes": "Likely to respond with a single, load-bearing line. Will not pad."
        }
      ]
    }
  ]
}
```

## 7. Implementation

### Stack

- Python 3.12+
- Pydantic models (shared with experiment simulator)
- Typer CLI
- LLM calls via `anthropic` or `openai` SDK
- YAML cohort config
- JSON output
- pytest + property-based tests for constraint validation

### CLI

```
dossier generate --cohort poet --count 14 --seed 42 --output data/dossiers-poets.json
dossier generate --cohort layperson --count 14 --seed 43 --output data/dossiers-lay.json
dossier generate --config custom-cohorts.yaml --seed 42 --output data/dossiers-all.json
dossier validate data/dossiers-poets.json
dossier compare data/dossiers-poets.json data/dossiers-lay.json  # cross-cohort distinctiveness
```

### Directory structure

```
poet-dossier/
  pyproject.toml
  config/
    cohorts/
      poet.yaml
      layperson.yaml
  poet_dossier/
    models.py            # Pydantic dossier schema
    distribution.py      # geographic/demographic skeleton planning
    generator.py         # LLM-based profile generation
    validation.py        # distinctiveness + consistency checks
    cli.py
  tests/
  data/
    dossiers-poets.json
    dossiers-lay.json
```

## 8. Acceptance criteria

1. Generate 14 distinct dossiers per cohort that pass all geographic and demographic constraints
2. No two participants in the same cohort have overlapping voice profiles (validated by pairwise check)
3. Every dossier is internally consistent (location ↔ timezone ↔ name ↔ background)
4. Custom cohort configs produce valid dossiers with appropriate character
5. Deterministic given seed: same seed + config = same output
6. Output JSON validates against schema
7. Dossiers are directly consumable by the experiment simulator without transformation
8. Generator logs constraint satisfaction metrics (diversity scores, pairwise distances)
