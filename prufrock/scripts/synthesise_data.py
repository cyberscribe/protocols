#!/usr/bin/env python3
"""
Prufrock Protocol — Data Synthesis Script

Generates simulation output JSON for Sonnet Trial Alpha.
Output: data/sim-output.json (schema per mockup/spec/simulation.md)

Usage:
    python3 scripts/synthesise_data.py [--seed 42] [--output data/sim-output.json]
    python3 scripts/synthesise_data.py --dry-run   # no API calls; deterministic placeholders

Uses `claude -p` (Claude Code CLI) for generation — no API key required.
"""

import argparse
import json
import math
import random
import subprocess
import sys
from pathlib import Path
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Optional

# ---------------------------------------------------------------------------
# SEED POEM
# ---------------------------------------------------------------------------

SEED_POEM = {
    "title": "Sonnet 18",
    "author": "William Shakespeare",
    "full_text": (
        "Shall I compare thee to a summer's day?\n"
        "Thou art more lovely and more temperate:\n"
        "Rough winds do shake the darling buds of May,\n"
        "And summer's lease hath all too short a date:\n"
        "Sometime too hot the eye of heaven shines,\n"
        "And often is his gold complexion dimm'd;\n"
        "And every fair from fair sometime declines,\n"
        "By chance, or nature's changing course untrimm'd;\n"
        "But thy eternal summer shall not fade,\n"
        "Nor lose possession of that fair thou ow'st;\n"
        "Nor shall death brag thou wander'st in his shade,\n"
        "When in eternal lines to time thou grow'st:\n"
        "So long as men can breathe, or eyes can see,\n"
        "So long lives this, and this gives life to thee."
    ),
    "seed_line_numbers": [10, 11],  # 0-indexed: the volta couplet lines
    "author_birth_year": 1564,
    "author_death_year": 1616,
    "publication_year": 1609,
    "location": {"city": "London", "country": "England", "lat": 51.5074, "lon": -0.1278},
    "rights_status": "global_pd_confident",
}

SEED_LINES_TEXT = [
    "Nor shall death brag thou wander'st in his shade,",
    "When in eternal lines to time thou grow'st:",
]

# ---------------------------------------------------------------------------
# DOSSIERS — 14 poets, geographically and stylistically diverse
# ---------------------------------------------------------------------------

DOSSIERS = [
    {
        "id": "poet-01",
        "cohort": "poet",
        "name": "Amara Osei",
        "age": 34,
        "gender": "female",
        "location": {
            "city": "Accra", "country": "Ghana", "region": "Greater Accra",
            "timezone": "Africa/Accra", "lat": 5.6037, "lon": -0.1870, "setting": "urban",
        },
        "language": {"primary": "en", "additional": ["tw"], "writes_in": "en"},
        "background": (
            "Published her first collection at 28 through a Ghanaian indie press; "
            "teaches creative writing at the University of Ghana. Her work circles "
            "migration within West Africa — not the diaspora narrative the international market expects."
        ),
        "occupation": "Poet and lecturer",
        "education": "MFA, University of Michigan",
        "voice_notes": (
            "Controlled intensity. Short declarative lines that build pressure through "
            "accumulation rather than imagery. Resists metaphor unless it earns its place."
        ),
        "emotional_baseline": "Watchful, deliberate warmth",
        "influences": ["Lucille Clifton", "Kofi Awoonor", "Warsan Shire", "highlife music"],
        "behavioural_traits": {
            "response_speed": "deliberate", "verbosity": "terse",
            "risk_tolerance": "moderate", "forfeit_probability": 0.03,
        },
        "availability_window": {"start_hour": 6, "end_hour": 22, "weekend_shift": 1},
        "notes": "Likely to respond with a single load-bearing line. Will not pad.",
    },
    {
        "id": "poet-02",
        "cohort": "poet",
        "name": "Hiroshi Tanaka",
        "age": 58,
        "gender": "male",
        "location": {
            "city": "Kyoto", "country": "Japan", "region": "Kyoto Prefecture",
            "timezone": "Asia/Tokyo", "lat": 35.0116, "lon": 135.7681, "setting": "urban",
        },
        "language": {"primary": "ja", "additional": ["en"], "writes_in": "en"},
        "background": (
            "Former architectural draughtsman who began writing poetry in English at forty. "
            "Three collections published in Japan; translated into six languages. "
            "His English retains the grammatical compressions of Japanese thought."
        ),
        "occupation": "Poet and translator",
        "education": "BA Architecture, Kyoto University",
        "voice_notes": (
            "Imagist precision with a haiku-like respect for the unsaid. Spatial. "
            "White space is load-bearing. The line ends before the thought finishes."
        ),
        "emotional_baseline": "Serene attention, sudden grief",
        "influences": ["Matsuo Bashō", "Yosa Buson", "Gary Snyder", "stone garden geometry"],
        "behavioural_traits": {
            "response_speed": "deliberate", "verbosity": "terse",
            "risk_tolerance": "conservative", "forfeit_probability": 0.02,
        },
        "availability_window": {"start_hour": 5, "end_hour": 21, "weekend_shift": -1},
        "notes": "Will sometimes respond with a line that appears to non-sequitur the prompt; it never does.",
    },
    {
        "id": "poet-03",
        "cohort": "poet",
        "name": "Valentina Cruz",
        "age": 29,
        "gender": "female",
        "location": {
            "city": "Oaxaca", "country": "Mexico", "region": "Oaxaca",
            "timezone": "America/Mexico_City", "lat": 17.0732, "lon": -96.7266, "setting": "urban",
        },
        "language": {"primary": "es", "additional": ["en", "zapotec"], "writes_in": "en"},
        "background": (
            "Born in a Zapotec-speaking village; moved to Oaxaca city at fifteen. "
            "Her first English-language collection won the Mexican National Poetry Prize at 27. "
            "Her work insists on the body as a political site."
        ),
        "occupation": "Poet and textile artist",
        "education": "BA Literature, UNAM",
        "voice_notes": (
            "Earthy surrealism rooted in pre-Columbian cosmology. Concrete nouns — maize, bone, smoke. "
            "Lines are sensory before they are intellectual."
        ),
        "emotional_baseline": "Volcanic, intermittently tender",
        "influences": ["Rosario Castellanos", "Natalia Toledo", "César Vallejo", "Zapotec oral poetry"],
        "behavioural_traits": {
            "response_speed": "erratic", "verbosity": "moderate",
            "risk_tolerance": "adventurous", "forfeit_probability": 0.08,
        },
        "availability_window": {"start_hour": 9, "end_hour": 23, "weekend_shift": 2},
        "notes": "May write with unusual line breaks that challenge conventions.",
    },
    {
        "id": "poet-04",
        "cohort": "poet",
        "name": "Björn Lindqvist",
        "age": 45,
        "gender": "male",
        "location": {
            "city": "Gothenburg", "country": "Sweden", "region": "Västra Götaland",
            "timezone": "Europe/Stockholm", "lat": 57.7089, "lon": 11.9746, "setting": "urban",
        },
        "language": {"primary": "sv", "additional": ["en", "no"], "writes_in": "en"},
        "background": (
            "Academic poet and university lecturer in comparative literature. "
            "His English work is quieter than his Swedish — as if the foreign language "
            "requires more of him. Six collections, a Nordic Council Literature Prize shortlist."
        ),
        "occupation": "Poet and academic",
        "education": "PhD Comparative Literature, Uppsala University",
        "voice_notes": (
            "Tranströmer's long pause stretched further. Spare, Nordic reticence. "
            "The image arrives and recedes without explanation. Trusts the reader."
        ),
        "emotional_baseline": "Melancholic but anchored",
        "influences": ["Tomas Tranströmer", "Lars Gustafsson", "Seamus Heaney", "boreal winters"],
        "behavioural_traits": {
            "response_speed": "deliberate", "verbosity": "terse",
            "risk_tolerance": "moderate", "forfeit_probability": 0.04,
        },
        "availability_window": {"start_hour": 7, "end_hour": 22, "weekend_shift": -2},
        "notes": "Will write one exact line after long consideration.",
    },
    {
        "id": "poet-05",
        "cohort": "poet",
        "name": "Priya Subramaniam",
        "age": 37,
        "gender": "female",
        "location": {
            "city": "Chennai", "country": "India", "region": "Tamil Nadu",
            "timezone": "Asia/Kolkata", "lat": 13.0827, "lon": 80.2707, "setting": "urban",
        },
        "language": {"primary": "ta", "additional": ["en", "hi"], "writes_in": "en"},
        "background": (
            "Scholar of classical Tamil Sangam poetry who writes English verse from the inside "
            "of that tradition. Her work bridges akam (interior love poetry) and the contemporary. "
            "Twice shortlisted for the DSC Prize."
        ),
        "occupation": "Poet and Sanskrit scholar",
        "education": "PhD Tamil Literature, University of Madras",
        "voice_notes": (
            "Precision that feels ancient. Classical imagery repurposed without nostalgia. "
            "The line is measured — not in syllables but in emotional weight per word."
        ),
        "emotional_baseline": "Exacting, capable of sudden lyricism",
        "influences": ["Akananuru", "A.K. Ramanujan", "Kamala Das", "monsoon acoustics"],
        "behavioural_traits": {
            "response_speed": "deliberate", "verbosity": "terse",
            "risk_tolerance": "conservative", "forfeit_probability": 0.03,
        },
        "availability_window": {"start_hour": 6, "end_hour": 21, "weekend_shift": 0},
        "notes": "Will find a way to make the abstract concrete.",
    },
    {
        "id": "poet-06",
        "cohort": "poet",
        "name": "Cormac Ó Briain",
        "age": 63,
        "gender": "male",
        "location": {
            "city": "Clifden", "country": "Ireland", "region": "Connaught",
            "timezone": "Europe/Dublin", "lat": 53.4894, "lon": -10.0190, "setting": "rural",
        },
        "language": {"primary": "ga", "additional": ["en"], "writes_in": "en"},
        "background": (
            "Connemara-born, Irish-first. Has lived on the same headland for forty years. "
            "Writes in English as a second language — it shows, in the best sense: "
            "the syntax tilts toward Gaelic. Award-winning poet and sometime farmer."
        ),
        "occupation": "Poet and smallholder",
        "education": "BA Gaelic Studies, NUI Galway",
        "voice_notes": (
            "Oral tradition running under the English surface. Rhythms that feel like "
            "they were sung before they were written. The land is always present, never decorative."
        ),
        "emotional_baseline": "Stoic, wrily elegiac",
        "influences": ["Nuala Ní Dhomhnaill", "Seamus Heaney", "Patrick Kavanagh", "Atlantic weather"],
        "behavioural_traits": {
            "response_speed": "deliberate", "verbosity": "moderate",
            "risk_tolerance": "conservative", "forfeit_probability": 0.05,
        },
        "availability_window": {"start_hour": 6, "end_hour": 20, "weekend_shift": 0},
        "notes": "The pastoral is never escapism in his work.",
    },
    {
        "id": "poet-07",
        "cohort": "poet",
        "name": "Leila Ahmadi",
        "age": 41,
        "gender": "female",
        "location": {
            "city": "Toronto", "country": "Canada", "region": "Ontario",
            "timezone": "America/Toronto", "lat": 43.6532, "lon": -79.3832, "setting": "urban",
        },
        "language": {"primary": "fa", "additional": ["en", "fr"], "writes_in": "en"},
        "background": (
            "Born in Tehran; arrived in Toronto at nineteen. Trained in Persian classical metrics "
            "before switching to English. Her diaspora work is neither nostalgic nor bitter — "
            "it simply insists the past is load-bearing, not luggage."
        ),
        "occupation": "Poet and literary translator",
        "education": "MFA Poetry, University of Toronto",
        "voice_notes": (
            "Persian ghazal architecture informing English free verse — the couplet autonomy, "
            "the turn toward a beloved that is always also the self. "
            "Formally aware without being formally bound."
        ),
        "emotional_baseline": "Restrained longing, precise grief",
        "influences": ["Hafez", "Forugh Farrokhzad", "Ocean Vuong", "the Alborz mountains"],
        "behavioural_traits": {
            "response_speed": "deliberate", "verbosity": "moderate",
            "risk_tolerance": "moderate", "forfeit_probability": 0.04,
        },
        "availability_window": {"start_hour": 7, "end_hour": 23, "weekend_shift": 1},
        "notes": "Will translate emotion before she translates image.",
    },
    {
        "id": "poet-08",
        "cohort": "poet",
        "name": "Marcus Webb",
        "age": 52,
        "gender": "male",
        "location": {
            "city": "New Orleans", "country": "USA", "region": "Louisiana",
            "timezone": "America/Chicago", "lat": 29.9511, "lon": -90.0715, "setting": "urban",
        },
        "language": {"primary": "en", "additional": [], "writes_in": "en"},
        "background": (
            "Grew up in the Tremé; plays trumpet with several local jazz outfits alongside writing. "
            "His fourth collection won the Kingsley Tufts Award. "
            "He writes fast, revises never, trusts the first heat."
        ),
        "occupation": "Poet and jazz musician",
        "education": "BA English, Tulane University",
        "voice_notes": (
            "Jazz-inflected: the line breathes in syncopation. Vernacular without being "
            "merely colloquial. The city's heat, water, and memory are never far. "
            "Improvisational but never careless."
        ),
        "emotional_baseline": "Jubilant grief — knows both simultaneously",
        "influences": ["Yusef Komunyakaa", "Sonia Sanchez", "Miles Davis", "second-line music"],
        "behavioural_traits": {
            "response_speed": "impulsive", "verbosity": "moderate",
            "risk_tolerance": "adventurous", "forfeit_probability": 0.07,
        },
        "availability_window": {"start_hour": 10, "end_hour": 24, "weekend_shift": 3},
        "notes": "Likely to respond immediately after the interruption.",
    },
    {
        "id": "poet-09",
        "cohort": "poet",
        "name": "Nadia Petersen",
        "age": 26,
        "gender": "female",
        "location": {
            "city": "Copenhagen", "country": "Denmark", "region": "Capital Region",
            "timezone": "Europe/Copenhagen", "lat": 55.6761, "lon": 12.5683, "setting": "urban",
        },
        "language": {"primary": "da", "additional": ["en", "de"], "writes_in": "en"},
        "background": (
            "The youngest in the cohort. Debut collection at 24, written while completing "
            "a mathematics degree. Her formal experiments treat the poem as combinatorial object "
            "without losing the lyric core."
        ),
        "occupation": "Poet and mathematics postgraduate",
        "education": "BSc Mathematics, University of Copenhagen (MSc in progress)",
        "voice_notes": (
            "Inger Christensen's systemic rigour meeting Celan's linguistic pressure. "
            "Interested in constraint as generative rather than limiting. "
            "Dense, playful, exact."
        ),
        "emotional_baseline": "Curious, with an undertow of existential unease",
        "influences": ["Inger Christensen", "Paul Celan", "Christian Bok", "set theory"],
        "behavioural_traits": {
            "response_speed": "erratic", "verbosity": "terse",
            "risk_tolerance": "adventurous", "forfeit_probability": 0.06,
        },
        "availability_window": {"start_hour": 8, "end_hour": 24, "weekend_shift": 2},
        "notes": "May respond at unexpected hours. Will bring mathematical thinking to image-making.",
    },
    {
        "id": "poet-10",
        "cohort": "poet",
        "name": "Yaw Asante",
        "age": 33,
        "gender": "male",
        "location": {
            "city": "Bristol", "country": "UK", "region": "England",
            "timezone": "Europe/London", "lat": 51.4545, "lon": -2.5879, "setting": "urban",
        },
        "language": {"primary": "en", "additional": ["tw"], "writes_in": "en"},
        "background": (
            "Second-generation Ghanaian-British. Emerged from the Bristol spoken-word scene "
            "before crossing to the page. His work is politically precise without being didactic. "
            "Two collections; frequent BBC Radio 4 contributor."
        ),
        "occupation": "Poet and arts educator",
        "education": "BA English Literature, Bristol University",
        "voice_notes": (
            "The spoken word origin is audible as controlled breath, not performance. "
            "Clear and furious by turns. Finds the systemic in the personal."
        ),
        "emotional_baseline": "Alert, corrective anger worn lightly",
        "influences": ["Kae Tempest", "Claudia Rankine", "Linton Kwesi Johnson", "grime and drill music"],
        "behavioural_traits": {
            "response_speed": "impulsive", "verbosity": "moderate",
            "risk_tolerance": "adventurous", "forfeit_probability": 0.06,
        },
        "availability_window": {"start_hour": 8, "end_hour": 23, "weekend_shift": 2},
        "notes": "Will use vernacular strategically, not accidentally.",
    },
    {
        "id": "poet-11",
        "cohort": "poet",
        "name": "Camille Okonkwo",
        "age": 48,
        "gender": "female",
        "location": {
            "city": "Lyon", "country": "France", "region": "Auvergne-Rhône-Alpes",
            "timezone": "Europe/Paris", "lat": 45.7640, "lon": 4.8357, "setting": "urban",
        },
        "language": {"primary": "fr", "additional": ["en", "yo"], "writes_in": "en"},
        "background": (
            "Nigerian-French; grew up between Lagos and Lyon. Writes in English as a neutral "
            "third language — neither her mother's tongue nor her father's. "
            "Known for essays as much as poems; a public intellectual in France."
        ),
        "occupation": "Poet and cultural critic",
        "education": "Agrégation de Lettres, ENS Lyon",
        "voice_notes": (
            "Code-switching as aesthetic: Yoruba proverb structure inside French lyric form "
            "inside English syntax. The voice is expansive, always three things at once."
        ),
        "emotional_baseline": "Expansive, intellectually restless",
        "influences": ["Aimé Césaire", "Wole Soyinka", "Edouard Glissant", "Yoruba praise poetry"],
        "behavioural_traits": {
            "response_speed": "deliberate", "verbosity": "expansive",
            "risk_tolerance": "moderate", "forfeit_probability": 0.04,
        },
        "availability_window": {"start_hour": 8, "end_hour": 22, "weekend_shift": -1},
        "notes": "May write a line that is also a question.",
    },
    {
        "id": "poet-12",
        "cohort": "poet",
        "name": "Dmitri Volkov",
        "age": 55,
        "gender": "male",
        "location": {
            "city": "Novosibirsk", "country": "Russia", "region": "Novosibirsk Oblast",
            "timezone": "Asia/Novosibirsk", "lat": 54.9885, "lon": 82.9207, "setting": "urban",
        },
        "language": {"primary": "ru", "additional": ["en", "de"], "writes_in": "en"},
        "background": (
            "Trained in Leningrad in the 1980s Soviet tradition; now writes in English "
            "from Siberia, which he has not left. Formalist roots: he counts syllables "
            "even when writing free verse. Six collections; Prix Apollinaire shortlist."
        ),
        "occupation": "Poet and librarian",
        "education": "Degree in Philology, Leningrad State University",
        "voice_notes": (
            "Brodsky without the show. The formal training is structural, not ornamental. "
            "English used as a cold instrument. Time and cold are not metaphors — they are the subject."
        ),
        "emotional_baseline": "Stoic, with dark wit",
        "influences": ["Joseph Brodsky", "Anna Akhmatova", "Paul Celan", "Siberian geography"],
        "behavioural_traits": {
            "response_speed": "deliberate", "verbosity": "moderate",
            "risk_tolerance": "conservative", "forfeit_probability": 0.03,
        },
        "availability_window": {"start_hour": 7, "end_hour": 21, "weekend_shift": -1},
        "notes": "Will find the minimum number of syllables required.",
    },
    {
        "id": "poet-13",
        "cohort": "poet",
        "name": "Ana Folau",
        "age": 31,
        "gender": "female",
        "location": {
            "city": "Wellington", "country": "New Zealand", "region": "Wellington Region",
            "timezone": "Pacific/Auckland", "lat": -41.2866, "lon": 174.7756, "setting": "urban",
        },
        "language": {"primary": "en", "additional": ["mi"], "writes_in": "en"},
        "background": (
            "Māori and Tongan heritage; grew up in Wellington. Works in te ao Māori alongside "
            "contemporary poetics. Her debut won the Ockham NZ Book Awards. "
            "The ocean is not a metaphor in her work — it is the condition of all thought."
        ),
        "occupation": "Poet and te reo Māori teacher",
        "education": "BA Creative Writing, Victoria University of Wellington",
        "voice_notes": (
            "Indigenous ecological attentiveness: the nonhuman is always a speaker, never a backdrop. "
            "Whakapapa (genealogy, connection) structures the poem beneath the surface. "
            "The line reaches rather than arrives."
        ),
        "emotional_baseline": "Grounded, oceanic patience",
        "influences": ["Hone Tuwhare", "Selina Tusitala Marsh", "Joy Harjo", "Māori oral tradition"],
        "behavioural_traits": {
            "response_speed": "deliberate", "verbosity": "moderate",
            "risk_tolerance": "moderate", "forfeit_probability": 0.04,
        },
        "availability_window": {"start_hour": 7, "end_hour": 22, "weekend_shift": 0},
        "notes": "Will situate the image in a specific landform or water body.",
    },
    {
        "id": "poet-14",
        "cohort": "poet",
        "name": "Roberto Benítez",
        "age": 68,
        "gender": "male",
        "location": {
            "city": "Buenos Aires", "country": "Argentina", "region": "Buenos Aires",
            "timezone": "America/Argentina/Buenos_Aires", "lat": -34.6037, "lon": -58.3816, "setting": "urban",
        },
        "language": {"primary": "es", "additional": ["en", "fr", "it"], "writes_in": "en"},
        "background": (
            "The elder of the cohort; published his first collection in Buenos Aires at 24. "
            "Has translated Borges into English and Shakespeare into Argentine Spanish. "
            "His English poetry is a lifetime of self-translation compressed into a line."
        ),
        "occupation": "Poet, translator, and retired professor",
        "education": "PhD Comparative Literature, UBA",
        "voice_notes": (
            "Borgesian meta-poetics worn lightly; wit without irony-as-defence. "
            "The labyrinth is real. History — Argentine history especially — is "
            "always present without being explicitly named."
        ),
        "emotional_baseline": "Wry, deeply patient",
        "influences": ["Jorge Luis Borges", "Alejandra Pizarnik", "John Donne", "Buenos Aires itself"],
        "behavioural_traits": {
            "response_speed": "deliberate", "verbosity": "expansive",
            "risk_tolerance": "moderate", "forfeit_probability": 0.05,
        },
        "availability_window": {"start_hour": 9, "end_hour": 21, "weekend_shift": -1},
        "notes": "Will find the infinite in the specific detail.",
    },
]

# ---------------------------------------------------------------------------
# LATIN SQUARE — adapted from combinatrix-validator.py
# Day 1: poet i → poem i (identity, 0-indexed)
# Days 2–14: 13×14 derangement Latin rectangle, no fixed points
# ---------------------------------------------------------------------------

N = 14
DAYS = 14


def _generate_rotation(rng: random.Random):
    """Generate one row: a derangement permutation of 0..N-1 not in col_used."""
    col_used: list = [set() for _ in range(N)]
    rows = []
    for _ in range(13):  # days 2..14
        row_used: set = set()
        row = [-1] * N
        remaining = set(range(N))
        while remaining:
            best_j, best_cands = None, None
            for j in remaining:
                cands = [v for v in range(N)
                         if v != j and v not in col_used[j] and v not in row_used]
                if not cands:
                    return None
                if best_cands is None or len(cands) < len(best_cands):
                    best_j, best_cands = j, cands
                    if len(cands) == 1:
                        break
            v = rng.choice(best_cands)
            row[best_j] = v
            row_used.add(v)
            col_used[best_j].add(v)
            remaining.remove(best_j)
        rows.append(row)
    return rows


def build_assignment(seed: int) -> list[list[int]]:
    """
    Return 14×14 assignment matrix.
    assignment[day][poet] = poem_index (0-indexed)
    Day 0: identity. Days 1..13: derangement Latin rectangle.
    """
    rng = random.Random(seed)
    for _ in range(1000):
        rotation = _generate_rotation(rng)
        if rotation is not None:
            return [list(range(N))] + rotation
    raise RuntimeError("Could not generate valid assignment matrix")


# ---------------------------------------------------------------------------
# WEATHER — simple lookup by month + hemisphere + setting
# ---------------------------------------------------------------------------

_WEATHER_N_SUMMER = ["clear, 28°C", "humid, 31°C, building clouds", "sunny, 25°C, light breeze"]
_WEATHER_N_WINTER = ["overcast, 4°C", "grey, 7°C, intermittent drizzle", "cold, 2°C, wind from the north"]
_WEATHER_N_SPRING = ["mild, 16°C, patchy cloud", "breezy, 14°C, bright intervals", "crisp, 12°C, clear"]
_WEATHER_TROPICAL = ["30°C, scattered showers", "humid, 32°C, overcast", "27°C, dry harmattan haze"]
_WEATHER_SOUTHERN = {  # inverted seasons
    "summer": _WEATHER_N_WINTER,
    "winter": _WEATHER_N_SUMMER,
    "spring": _WEATHER_N_SPRING,
}


def _season(month: int, southern: bool) -> str:
    if southern:
        month = (month + 6 - 1) % 12 + 1
    if month in (12, 1, 2):
        return "winter"
    if month in (3, 4, 5):
        return "spring"
    if month in (6, 7, 8):
        return "summer"
    return "autumn"


def generate_weather(poet: dict, date: datetime, rng: random.Random) -> str:
    lat = poet["location"]["lat"]
    southern = lat < -10
    tropical = abs(lat) < 15
    if tropical:
        pool = _WEATHER_TROPICAL
    else:
        s = _season(date.month, southern)
        pool = {"summer": _WEATHER_N_SUMMER, "winter": _WEATHER_N_WINTER,
                "spring": _WEATHER_N_SPRING, "autumn": _WEATHER_N_SPRING}[s]
    return rng.choice(pool)


# ---------------------------------------------------------------------------
# MOMENT CONTEXT — brief situational phrase from occupation + time of day
# ---------------------------------------------------------------------------

_MORNING_CONTEXTS = [
    "at the kitchen table, coffee cooling beside the notebook",
    "in the garden before the day's work begins",
    "walking to work, phone in hand",
    "at the desk before the household wakes",
]
_AFTERNOON_CONTEXTS = [
    "between meetings, office door closed",
    "in a café near the university",
    "at the library reference desk, a quiet moment",
    "in the studio, brushes soaking",
]
_EVENING_CONTEXTS = [
    "after dinner, at the window",
    "on the sofa, children asleep upstairs",
    "in the courtyard as the city quiets",
    "at the kitchen table, wine glass half empty",
]
_LATE_CONTEXTS = [
    "at the desk, city entirely dark outside",
    "in bed, light low",
    "in the study at midnight, unable to sleep",
]


def generate_moment_context(local_hour: int, rng: random.Random) -> str:
    if 5 <= local_hour < 12:
        return rng.choice(_MORNING_CONTEXTS)
    if 12 <= local_hour < 18:
        return rng.choice(_AFTERNOON_CONTEXTS)
    if 18 <= local_hour < 22:
        return rng.choice(_EVENING_CONTEXTS)
    return rng.choice(_LATE_CONTEXTS)


# ---------------------------------------------------------------------------
# POSITIONAL GUIDANCE
# ---------------------------------------------------------------------------

def positional_guidance(line_number: int, poem_length: int = 14) -> str:
    if line_number == 1:
        return "opening — this is the poem's first step beyond its seed"
    if line_number <= 4:
        return "early development — the poem is finding its voice"
    if line_number <= 7:
        return "mid-poem — build on the established momentum"
    if line_number <= 10:
        return "deepening — the poem's centre of gravity"
    if line_number <= 12:
        return "turning — begin to move toward resolution"
    if line_number == poem_length - 1:
        return "penultimate — maximum tension before close"
    return "final line — land it; this is the last thing said"


# ---------------------------------------------------------------------------
# DRY-RUN PLACEHOLDER LINES — thematically resonant with mortality / time
# ---------------------------------------------------------------------------

_PLACEHOLDER_LINES = [
    "the hour holds its breath before it turns",
    "a door that opens both ways at once",
    "what the water keeps is not what it shows",
    "we number our losses the way we number our years",
    "the shadow knows the shape before the hand does",
    "I inherit the light from those who are gone",
    "all the clocks agree: now is always leaving",
    "the stone that outlasts the hand that carved it",
    "morning again, and the world still requiring us",
    "the name you gave it does not make it yours",
    "under the ice, the river has not forgotten its way",
    "someone will love this after we have stopped",
    "the echo precedes the sound in memory",
    "the seed is patient in a way the flower cannot be",
    "to be witnessed is not the same as being understood",
    "the tree counts its rings in the dark",
    "what we called silence was only distance",
    "the hand that once reached for mine still reaches",
    "all testimony is partial and necessary",
    "we leave by the same door we entered, changed",
    "the lamp's flame does not remember the match",
    "time does not pass through us — we pass through it",
    "the body knows what the mind refuses",
    "the poem is the only country that survives its borders",
    "I have outlived so many versions of the sky",
    "wherever you are, the same stars",
    "the tide returns, indifferent and faithful",
    "language is the wound and also the bandage",
    "who remembers the first word ever spoken",
    "the century turns and the question stays",
]


def placeholder_line(poet_id: str, poem_index: int, line_number: int, rng: random.Random) -> str:
    idx = rng.randint(0, len(_PLACEHOLDER_LINES) - 1)
    return _PLACEHOLDER_LINES[idx]


# ---------------------------------------------------------------------------
# LINE GENERATION — Anthropic API
# ---------------------------------------------------------------------------

def _claude(prompt: str, max_words: int = 30) -> str:
    """Call `claude -p` and return stdout, stripping surrounding whitespace."""
    result = subprocess.run(
        ["claude", "-p", prompt, "--model", "claude-haiku-4-5-20251001"],
        capture_output=True, text=True, timeout=60,
    )
    if result.returncode != 0:
        raise RuntimeError(f"claude -p failed: {result.stderr.strip()}")
    return result.stdout.strip()


def generate_line_api(
    poet: dict,
    prompt_lines: list[dict],
    line_number: int,
    date: datetime,
    moment: dict,
) -> str:
    influences = ", ".join(poet["influences"])
    profile = (
        f"Name: {poet['name']}\n"
        f"Background: {poet['background']}\n"
        f"Voice: {poet['voice_notes']}\n"
        f"Emotional baseline: {poet['emotional_baseline']}\n"
        f"Influences: {influences}"
    )
    prompt_text = "\n".join(f'  "{pl["text"]}"' for pl in prompt_lines)
    guidance = positional_guidance(line_number)
    date_str = date.strftime("%A, %d %B %Y")

    user_prompt = (
        f"POET PROFILE (private):\n{profile}\n\n"
        f"THE MOMENT:\n"
        f"It is {moment['local_time']} on {date_str}. "
        f"You are in {poet['location']['city']}, {poet['location']['country']}.\n"
        f"Weather: {moment['weather']}. You are {moment['context']}.\n\n"
        f"THE TWO LINES YOU HAVE BEEN GIVEN (from a poem in progress — you did not write these):\n"
        f"{prompt_text}\n\n"
        f"Write the next line of this poem. Your line will be line {line_number} of 14.\n"
        f"Rules:\n"
        f"- One line only\n"
        f"- Write in your own voice (see profile) — but in response to the momentum above\n"
        f"- This is line {line_number} of 14 — {guidance}\n"
        f"- Do not repeat words from the given lines unless deliberately echoing for effect\n\n"
        f"Respond with the line only, no explanation, no quotation marks."
    )

    return _claude(user_prompt).strip('"').strip("'")


# ---------------------------------------------------------------------------
# CONCERN TAGGING
# ---------------------------------------------------------------------------

CONCERN_TAXONOMY = [
    "mortality", "love_unrequited", "love_present", "nature_seasons",
    "social_anxiety", "memory", "power", "solitude", "wonder", "domestic",
    "grief", "identity", "time", "freedom", "faith", "body", "language",
]


def tag_seed_concerns(seed_poem_text: str) -> list[dict]:
    lines_numbered = "\n".join(
        f"{i+1}: {line}" for i, line in enumerate(seed_poem_text.split("\n"))
    )
    taxonomy_list = ", ".join(CONCERN_TAXONOMY)
    prompt = (
        f"Given this poem, identify the timeless human concerns it engages with.\n"
        f"For each concern, cite which line numbers carry it (1-indexed) and rate intensity 0.0–1.0.\n"
        f"Use only concerns from: {taxonomy_list}\n\n"
        f"Poem:\n{lines_numbered}\n\n"
        f"Return JSON only — a list of objects: "
        f'[{{"concern": str, "intensity": float, "line_numbers": [int]}}]'
    )
    raw = _claude(prompt)
    if "```" in raw:
        raw = raw.split("```")[1].replace("json", "").strip()
    try:
        return json.loads(raw)
    except Exception:
        return [{"concern": "mortality", "intensity": 0.9, "line_numbers": [10, 11, 12]},
                {"concern": "time", "intensity": 0.8, "line_numbers": [3, 11, 12, 13]},
                {"concern": "love_present", "intensity": 0.7, "line_numbers": [1, 2, 8, 9]}]


def tag_poem_concerns(poem_lines: list[str], seed_concerns: list[dict]) -> dict:
    numbered = "\n".join(f"{i+1}: {line}" for i, line in enumerate(poem_lines))
    seed_concern_names = [c["concern"] for c in seed_concerns]
    taxonomy_list = ", ".join(CONCERN_TAXONOMY)
    prompt = (
        f"This poem was written line-by-line over 14 days, each line by a different poet "
        f"responding anonymously to the preceding two lines.\n\n"
        f"Identify the timeless human concerns it engages with.\n"
        f"For each concern:\n"
        f'- Rate intensity 0.0–1.0\n'
        f"- Cite which line numbers carry it (1-indexed)\n"
        f'- Note origin: "inherited" if also present in seed, "introduced" otherwise\n'
        f"Seed poem concerns for reference: {', '.join(seed_concern_names)}\n"
        f"Use only concerns from: {taxonomy_list}\n\n"
        f"Poem:\n{numbered}\n\n"
        f"Return JSON only — a list: "
        f'[{{"concern": str, "intensity": float, "line_numbers": [int], "origin": "inherited"|"introduced"}}]'
    )
    raw = _claude(prompt)
    if "```" in raw:
        raw = raw.split("```")[1].replace("json", "").strip()
    try:
        concerns = json.loads(raw)
    except Exception:
        concerns = [
            {"concern": "mortality", "intensity": 0.7, "line_numbers": [3, 8, 14], "origin": "inherited"},
            {"concern": "time", "intensity": 0.6, "line_numbers": [1, 7, 13], "origin": "inherited"},
            {"concern": "memory", "intensity": 0.5, "line_numbers": [2, 6, 11], "origin": "introduced"},
        ]

    # Per-line: top concern for each line
    line_concerns = []
    concern_by_line: dict[int, list] = {}
    for c in concerns:
        for ln in c.get("line_numbers", []):
            concern_by_line.setdefault(ln, []).append(c)
    for ln in range(1, len(poem_lines) + 1):
        best = sorted(concern_by_line.get(ln, []), key=lambda c: c["intensity"], reverse=True)
        entry = {"line_number": ln, "concerns": []}
        for c in best[:2]:
            entry["concerns"].append({"concern": c["concern"], "intensity": c["intensity"]})
        line_concerns.append(entry)

    return {"concerns": concerns, "line_concerns": line_concerns}


def placeholder_concerns(poem_index: int, seed_concerns: list[dict]) -> dict:
    inherited = seed_concerns[:2] if seed_concerns else []
    concerns = []
    for c in inherited:
        concerns.append({
            "concern": c["concern"],
            "intensity": round(c["intensity"] * 0.8, 2),
            "line_numbers": [1, 7, 14],
            "origin": "inherited",
        })
    concerns.append({
        "concern": CONCERN_TAXONOMY[(poem_index * 3 + 5) % len(CONCERN_TAXONOMY)],
        "intensity": 0.55,
        "line_numbers": [3, 9, 12],
        "origin": "introduced",
    })
    line_concerns = [
        {"line_number": i + 1, "concerns": [{"concern": concerns[0]["concern"], "intensity": 0.5}]}
        for i in range(14)
    ]
    return {"concerns": concerns, "line_concerns": line_concerns}


# ---------------------------------------------------------------------------
# SIMULATION RUNNER
# ---------------------------------------------------------------------------

def utc_offset_hours(tz_name: str) -> float:
    """Rough UTC offset for known timezones in this dataset."""
    offsets = {
        "Africa/Accra": 0, "Asia/Tokyo": 9, "America/Mexico_City": -6,
        "Europe/Stockholm": 1, "Asia/Kolkata": 5.5, "Europe/Dublin": 0,
        "America/Toronto": -5, "America/Chicago": -6, "Europe/Copenhagen": 1,
        "Europe/London": 0, "Europe/Paris": 1, "Asia/Novosibirsk": 7,
        "Pacific/Auckland": 12, "America/Argentina/Buenos_Aires": -3,
    }
    return offsets.get(tz_name, 0)


def simulate(seed: int = 42, dry_run: bool = False) -> dict:
    rng = random.Random(seed)
    start_date = datetime(2026, 6, 1, tzinfo=timezone.utc)
    assignment = build_assignment(seed)
    poet_by_id = {p["id"]: p for p in DOSSIERS}

    # Poet index → poet
    poets = DOSSIERS  # 14 poets, 0-indexed

    print(f"  Assignment matrix: {len(assignment)}×{len(assignment[0])}")

    # Tag seed concerns
    print("  Tagging seed poem concerns...")
    if dry_run:
        seed_concerns = [
            {"concern": "mortality", "intensity": 0.9, "line_numbers": [11, 12]},
            {"concern": "time", "intensity": 0.85, "line_numbers": [4, 12, 13]},
            {"concern": "love_present", "intensity": 0.7, "line_numbers": [1, 2, 8, 9]},
            {"concern": "nature_seasons", "intensity": 0.65, "line_numbers": [1, 3, 4, 5]},
            {"concern": "language", "intensity": 0.5, "line_numbers": [12, 13, 14]},
        ]
    else:
        seed_concerns = tag_seed_concerns(SEED_POEM["full_text"])

    # Initialise 14 poems — each will accumulate lines
    poems: list[dict] = []
    for poem_idx in range(N):
        poems.append({"id": f"poem-{poem_idx+1:02d}", "lines": []})

    # Track forfeits per poem for prompt resolution
    # poem_lines[poem_idx] = list of (line_text, author_id) or None (forfeit)
    poem_line_texts: list[list] = [[] for _ in range(N)]

    def get_prompt_lines(poem_idx: int, day_0: int) -> list[dict]:
        """Return the 2-line prompt for a poet writing on this day into this poem."""
        if day_0 == 0:
            return [
                {"ref": "seed:10", "text": SEED_LINES_TEXT[0], "author": "William Shakespeare"},
                {"ref": "seed:11", "text": SEED_LINES_TEXT[1], "author": "William Shakespeare"},
            ]
        existing = [l for l in poem_line_texts[poem_idx] if l is not None]
        if len(existing) < 2:
            filled = existing + [
                {"text": SEED_LINES_TEXT[i], "author_id": "seed", "line_number": 10 + i}
                for i in range(2 - len(existing))
            ]
            existing = filled
        last_two = existing[-2:]
        result = []
        for e in last_two:
            if e.get("author_id") == "seed":
                ln = e["line_number"]
                result.append({
                    "ref": f"seed:{ln}",
                    "text": e["text"],
                    "author": "William Shakespeare",
                })
            else:
                # find which poem line this is
                poem_lines_so_far = poems[poem_idx]["lines"]
                matching = [l for l in poem_lines_so_far if l.get("text") == e.get("text")]
                ref_ln = matching[0]["line_number"] if matching else "?"
                result.append({
                    "ref": f"poem-{poem_idx+1:02d}:{ref_ln}",
                    "text": e["text"],
                    "author": poet_by_id.get(e["author_id"], {}).get("name", e["author_id"]),
                })
        return result

    # Day-by-day simulation
    for day_0 in range(DAYS):
        day_num = day_0 + 1
        date = start_date + timedelta(days=day_0)
        print(f"  Day {day_num}/14...", end=" ", flush=True)

        for poet_idx, poet in enumerate(poets):
            poem_idx = assignment[day_0][poet_idx]
            poem = poems[poem_idx]

            # Interruption time: sample within availability window
            tz_offset = utc_offset_hours(poet["location"]["timezone"])
            avail_start = poet["availability_window"]["start_hour"]
            avail_end = poet["availability_window"]["end_hour"]
            if avail_end <= avail_start:
                avail_end = avail_start + 12
            local_hour = avail_start + rng.random() * (avail_end - avail_start)
            utc_hour = local_hour - tz_offset
            prompt_utc = date + timedelta(hours=utc_hour % 24)

            # Moment context
            weather = generate_weather(poet, date, rng)
            context = generate_moment_context(int(local_hour), rng)
            moment = {
                "local_time": f"{int(local_hour):02d}:{int((local_hour % 1) * 60):02d}",
                "weather": weather,
                "context": context,
            }

            # Forfeit?
            forfeited = rng.random() < poet["behavioural_traits"]["forfeit_probability"]

            # Prompt lines
            prompt_lines = get_prompt_lines(poem_idx, day_0)

            line_number = day_num  # one line per day, in order

            # Latency
            speed = poet["behavioural_traits"]["response_speed"]
            base = {"impulsive": 600, "deliberate": 1800, "erratic": 1200}[speed]
            sigma = 0.8 if speed == "erratic" else 0.4
            latency = int(min(
                math.exp(math.log(base) + rng.gauss(0, sigma)),
                4 * 3600,
            ))
            response_utc = prompt_utc + timedelta(seconds=latency)

            # Line text
            if forfeited:
                line_text = None
                poem_line_texts[poem_idx].append(None)
            else:
                if dry_run:
                    line_text = placeholder_line(poet["id"], poem_idx, line_number, rng)
                else:
                    try:
                        line_text = generate_line_api(poet, prompt_lines, line_number, date, moment)
                    except Exception as e:
                        print(f"\n    [warn] generation failed for {poet['id']} day {day_num}: {e}")
                        line_text = placeholder_line(poet["id"], poem_idx, line_number, rng)
                poem_line_texts[poem_idx].append({
                    "text": line_text,
                    "author_id": poet["id"],
                    "line_number": line_number,
                })

            line_entry = {
                "line_number": line_number,
                "day": day_num,
                "author_id": poet["id"],
                "text": line_text,
                "prompt_lines": prompt_lines,
                "prompt_delivered_utc": prompt_utc.strftime("%Y-%m-%dT%H:%M:%SZ"),
                "response_utc": response_utc.strftime("%Y-%m-%dT%H:%M:%SZ") if not forfeited else None,
                "latency_seconds": latency if not forfeited else None,
                "location": {
                    "city": poet["location"]["city"],
                    "country": poet["location"]["country"],
                    "lat": poet["location"]["lat"],
                    "lon": poet["location"]["lon"],
                },
                "moment": moment if not forfeited else None,
                "forfeited": forfeited,
            }
            poem["lines"].append(line_entry)

        print("done")

    # Concern tagging per poem
    print("  Tagging poem concerns...")
    for poem_idx, poem in enumerate(poems):
        completed_lines = [l["text"] for l in poem["lines"] if not l["forfeited"] and l["text"]]
        if dry_run:
            tagged = placeholder_concerns(poem_idx, seed_concerns)
        else:
            try:
                tagged = tag_poem_concerns(completed_lines, seed_concerns)
            except Exception as e:
                print(f"    [warn] concern tagging failed for poem {poem_idx+1}: {e}")
                tagged = placeholder_concerns(poem_idx, seed_concerns)
        poem["concerns"] = tagged["concerns"]
        poem["line_concerns"] = tagged["line_concerns"]

    # Concern continuity metrics
    def concern_metrics(poems_list: list[dict]) -> dict:
        seed_concern_names = {c["concern"] for c in seed_concerns}
        inheritance_rates = []
        introduction_counts = []
        for poem in poems_list:
            poem_concerns = {c["concern"] for c in poem.get("concerns", [])}
            inherited = poem_concerns & seed_concern_names
            introduced = poem_concerns - seed_concern_names
            inheritance_rates.append(len(inherited) / max(len(seed_concern_names), 1))
            introduction_counts.append(len(introduced))
        return {
            "mean_inheritance_rate": round(sum(inheritance_rates) / len(inheritance_rates), 3),
            "mean_introduction_count": round(sum(introduction_counts) / len(introduction_counts), 2),
        }

    metrics = concern_metrics(poems)

    # Build full output JSON
    output = {
        "meta": {
            "experiment_name": "sonnet-trial-alpha",
            "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "random_seed": seed,
            "dry_run": dry_run,
            "seed_poem": {
                **SEED_POEM,
                "seed_lines": [
                    {"line_number": 10, "text": SEED_LINES_TEXT[0]},
                    {"line_number": 11, "text": SEED_LINES_TEXT[1]},
                ],
                "concerns": seed_concerns,
            },
            "config": {
                "poet_count": N,
                "poem_count": N,
                "poem_length": DAYS,
                "duration_days": DAYS,
                "seed_line_count": 2,
                "prompt_line_count": 2,
                "response_window_hours": 4,
                "interruption_mode": "uniform",
                "poem_assignment": "latin_square_derangement",
                "start_date": "2026-06-01",
            },
            "concern_metrics": metrics,
        },
        "cohorts": [
            {
                "id": "run_a",
                "cohort": "poet",
                "participants": DOSSIERS,
                "poem_assignment": assignment,
                "poems": poems,
            }
        ],
    }
    return output


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--output", default="data/sim-output.json")
    ap.add_argument("--dry-run", action="store_true",
                    help="Skip API calls; generate structure + placeholder lines only")
    args = ap.parse_args()

    mode = "dry-run (placeholder lines)" if args.dry_run else "live (claude -p)"
    print(f"Prufrock Protocol — Data Synthesis [{mode}]")
    print(f"  Seed: {args.seed}   Output: {args.output}")

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    result = simulate(seed=args.seed, dry_run=args.dry_run)

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    poem_count = len(result["cohorts"][0]["poems"])
    total_lines = sum(
        sum(1 for l in p["lines"] if not l["forfeited"])
        for p in result["cohorts"][0]["poems"]
    )
    forfeit_count = sum(
        sum(1 for l in p["lines"] if l["forfeited"])
        for p in result["cohorts"][0]["poems"]
    )
    print(f"\nDone. {poem_count} poems, {total_lines} lines, {forfeit_count} forfeits.")
    print(f"Output: {out_path}")


if __name__ == "__main__":
    main()
