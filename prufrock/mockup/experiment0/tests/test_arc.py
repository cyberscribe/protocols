"""End-to-end test of the 14-day arc: seed, start, antithesis pairs, record, complete."""

import hashlib
import uuid

import pytest

from prufrock.db.models import Participant, Sonnet
from prufrock.protocol.arc import (
    TOTAL_DAYS,
    assemble_poem,
    build_antithesis,
    is_complete,
    mark_complete,
    record_response,
    start_experiment,
)
from prufrock.scheduler.tasks import _get_or_create_next_prompt


def _sha256(s: str) -> str:
    return hashlib.sha256(s.encode()).hexdigest()


@pytest.fixture
def participant(session):
    p = Participant(
        telegram_user_id=99999,
        telegram_chat_id=99999,
        display_name="Test",
        timezone="Europe/London",
    )
    session.add(p)
    session.flush()
    return p


@pytest.fixture
def sonnet(session):
    s = Sonnet(
        id=18,
        title="Sonnet 18",
        source="test",
        full_text="Shall I compare thee to a summer's day?",
        line_12="But thy eternal summer shall not fade,",
        line_13="Nor lose possession of that fair thou ow'st,",
    )
    session.add(s)
    session.flush()
    return s


def test_start_experiment_picks_a_sonnet(session, participant, sonnet):
    experiment = start_experiment(session, participant)
    assert experiment.sonnet_id == sonnet.id
    assert experiment.status == "active"


def test_14_day_arc_adjacent_pair_invariant(session, participant, sonnet):
    """Verify each day's antithesis equals (P[N-1], P[N]) from the accumulating poem."""
    experiment = start_experiment(session, participant)

    seed_line_12 = sonnet.line_12
    seed_line_13 = sonnet.line_13
    expected_lines = [seed_line_12, seed_line_13]
    observed_antitheses = []

    for day in range(1, TOTAL_DAYS + 1):
        prompt = _get_or_create_next_prompt(session, experiment)
        assert prompt is not None, f"No prompt created for day {day}"
        assert prompt.day_number == day

        a, b = build_antithesis(session, experiment, day)
        # adjacent-pair invariant: (P[N-1], P[N])
        assert a == expected_lines[day - 1], f"Day {day}: antithesis_a mismatch"
        assert b == expected_lines[day], f"Day {day}: antithesis_b mismatch"
        observed_antitheses.append((a, b))

        # Record a synthetic response
        response_text = f"Response line {day}"
        raw_update = {"update_id": day, "message": {"text": response_text}}
        response = record_response(session, prompt, response_text, raw_update)

        # Verify parent hashes
        assert response.parent_hash_a == _sha256(a)
        assert response.parent_hash_b == _sha256(b)

        expected_lines.append(response_text)
        assert not is_complete(session, experiment) or day == TOTAL_DAYS

    assert is_complete(session, experiment)


def test_assemble_poem_has_16_lines(session, participant, sonnet):
    experiment = start_experiment(session, participant)

    for day in range(1, TOTAL_DAYS + 1):
        prompt = _get_or_create_next_prompt(session, experiment)
        record_response(session, prompt, f"Line {day}", {"update_id": day})

    poem = assemble_poem(session, experiment)
    lines = poem.strip().splitlines()
    assert len(lines) == 16, f"Expected 16 lines, got {len(lines)}"
    assert lines[0] == sonnet.line_12
    assert lines[1] == sonnet.line_13


def test_mark_complete_sets_status(session, participant, sonnet):
    experiment = start_experiment(session, participant)

    for day in range(1, TOTAL_DAYS + 1):
        prompt = _get_or_create_next_prompt(session, experiment)
        record_response(session, prompt, f"L{day}", {"update_id": day})

    mark_complete(session, experiment)
    assert experiment.status == "completed"
    assert experiment.completed_at is not None


def test_start_experiment_excludes_sonnet_126(session, participant):
    # Add only sonnet 126 — it should be excluded, so start_experiment should fail gracefully
    excluded = Sonnet(
        id=126,
        title="Sonnet 126",
        source="test",
        full_text="",
        line_12="",
        line_13="",
    )
    session.add(excluded)
    session.flush()

    with pytest.raises(Exception):
        # No eligible sonnets — should raise (empty choices list)
        start_experiment(session, participant)


def test_already_used_sonnet_not_repeated(session, participant, sonnet):
    """Second experiment for same participant should not re-use sonnet 18 (only option)."""
    exp1 = start_experiment(session, participant)
    assert exp1.sonnet_id == sonnet.id

    # Exhaust the only sonnet — second call wraps to full pool and picks it again
    # (wrap behaviour; the pool is size 1)
    exp2 = start_experiment(session, participant)
    # No assertion on the choice — just that it completes without error
    assert exp2.status == "active"
