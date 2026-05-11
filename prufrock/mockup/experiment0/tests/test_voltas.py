"""Tests for the Gutenberg sonnet parser."""

import textwrap
from pathlib import Path

import pytest

from prufrock.protocol.voltas import (
    SONNET_126_ID,
    SONNET_99_ID,
    parse_sonnets,
)


def _make_sonnet_block(number: str, lines: list[str]) -> str:
    body = "\n".join(lines)
    return f"\n{number}\n{body}\n"


def _roman(n: int) -> str:
    """Minimal int-to-Roman for test fixture generation."""
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    sym = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    result = ""
    for v, s in zip(val, sym):
        while n >= v:
            result += s
            n -= v
    return result


def _standard_lines(n: int) -> list[str]:
    return [f"Line {n}.{i+1} with some words to fill space" for i in range(14)]


def _build_fixture_text(overrides: dict[int, list[str]] | None = None) -> str:
    """Build a minimal Gutenberg-style text with 154 sonnet blocks."""
    overrides = overrides or {}
    parts = ["THE SONNETS\n"]
    for n in range(1, 155):
        lines = overrides.get(n, _standard_lines(n))
        parts.append(_make_sonnet_block(_roman(n), lines))
    parts.append("\n*** END OF THE PROJECT GUTENBERG")
    return "\n".join(parts)


# ── basic parse ───────────────────────────────────────────────────────────────

def test_parse_returns_154_entries():
    sonnets = parse_sonnets(_build_fixture_text())
    assert len(sonnets) == 154


def test_parse_all_ids_present():
    sonnets = parse_sonnets(_build_fixture_text())
    ids = {s["id"] for s in sonnets}
    assert ids == set(range(1, 155))


def test_standard_sonnet_has_correct_lines():
    sonnets = parse_sonnets(_build_fixture_text())
    s = next(s for s in sonnets if s["id"] == 1)
    lines = _standard_lines(1)
    assert s["line_12"] == lines[11]
    assert s["line_13"] == lines[12]
    assert not s["excluded"]


# ── sonnet 99 exception ───────────────────────────────────────────────────────

def test_sonnet_99_15_lines_handled():
    extra_line = "An extra opening line for sonnet 99"
    lines_99 = [extra_line] + _standard_lines(99)  # 15 lines
    assert len(lines_99) == 15
    sonnets = parse_sonnets(_build_fixture_text({99: lines_99}))
    s99 = next(s for s in sonnets if s["id"] == 99)
    assert not s99["excluded"]
    # After dropping the extra opening line, line_12 is lines_99[12] (index 11 of the 14)
    assert s99["line_12"] == lines_99[12]
    assert s99["line_13"] == lines_99[13]


def test_sonnet_99_standard_14_lines_unchanged():
    """If sonnet 99 already has 14 lines, no adjustment should be made."""
    sonnets = parse_sonnets(_build_fixture_text())
    s99 = next(s for s in sonnets if s["id"] == 99)
    expected = _standard_lines(99)
    assert s99["line_12"] == expected[11]
    assert s99["line_13"] == expected[12]


# ── sonnet 126 exclusion ──────────────────────────────────────────────────────

def test_sonnet_126_excluded():
    sonnets = parse_sonnets(_build_fixture_text())
    s126 = next(s for s in sonnets if s["id"] == 126)
    assert s126["excluded"] is True
    assert s126["exclusion_reason"] is not None
    assert s126["line_12"] == ""
    assert s126["line_13"] == ""


def test_eligible_pool_size():
    """153 sonnets should be eligible (154 minus sonnet 126)."""
    sonnets = parse_sonnets(_build_fixture_text())
    eligible = [s for s in sonnets if not s["excluded"]]
    assert len(eligible) == 153


# ── source attribution ────────────────────────────────────────────────────────

def test_source_is_gutenberg():
    sonnets = parse_sonnets(_build_fixture_text())
    for s in sonnets:
        assert "Gutenberg" in s["source"]


# ── missing header raises ─────────────────────────────────────────────────────

def test_missing_header_raises():
    with pytest.raises(ValueError, match="THE SONNETS"):
        parse_sonnets("No header here\n\nI\nSome line\n")
