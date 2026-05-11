"""Tests for the random fire-time generator."""

from datetime import date, time
from zoneinfo import ZoneInfo

import pytest

from prufrock.scheduler.fire_window import random_fire_time

TZ = ZoneInfo("Europe/London")
START = time(9, 0)
END = time(22, 0)
REF = date(2026, 5, 11)


def test_fire_time_within_window():
    dt = random_fire_time(START, END, TZ, REF)
    assert dt.hour >= 9
    # Allow 21:59:59
    assert dt.hour < 22 or (dt.hour == 22 and dt.minute == 0 and dt.second == 0)


def test_fire_time_is_tz_aware():
    dt = random_fire_time(START, END, TZ, REF)
    assert dt.tzinfo is not None


def test_fire_time_distribution(runs=2000):
    """Draws should span the full 13-hour window, not cluster at the start."""
    times = [random_fire_time(START, END, TZ, REF) for _ in range(runs)]
    hours = [t.hour for t in times]
    # Every hour from 9 to 21 should appear at least once in 2000 draws
    for h in range(9, 22):
        assert h in hours, f"Hour {h} never appeared in {runs} draws"


def test_fire_time_invalid_window_raises():
    with pytest.raises(ValueError):
        random_fire_time(END, START, TZ, REF)  # end before start


def test_fire_time_on_reference_date():
    dt = random_fire_time(START, END, TZ, REF)
    assert dt.date() == REF
