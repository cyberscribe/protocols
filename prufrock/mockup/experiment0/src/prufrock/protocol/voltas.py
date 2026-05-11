import hashlib
import json
import logging
import re
import urllib.request
from pathlib import Path
from typing import TypedDict

logger = logging.getLogger(__name__)

GUTENBERG_URL = "https://www.gutenberg.org/files/1041/1041-0.txt"

# Sonnet 99 has 15 lines; we drop the extra opening line.
SONNET_99_ID = 99
# Sonnet 126 has 12 lines and no closing couplet; excluded from the pool.
SONNET_126_ID = 126


class SonnetData(TypedDict):
    id: int
    title: str
    source: str
    full_text: str
    line_12: str
    line_13: str
    excluded: bool
    exclusion_reason: str | None


def fetch_gutenberg_text(url: str = GUTENBERG_URL) -> str:
    logger.info("Fetching sonnets from %s", url)
    req = urllib.request.Request(url, headers={"User-Agent": "prufrock/0.1"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8")


def _strip_boilerplate(text: str) -> str:
    # Find the start of the sonnets proper
    start_match = re.search(r"THE SONNETS", text)
    if start_match is None:
        raise ValueError("Could not locate 'THE SONNETS' heading in Gutenberg text")
    end_match = re.search(r"\*\*\* END OF THE PROJECT GUTENBERG", text)
    return text[start_match.start() : (end_match.start() if end_match else len(text))]


def _roman_to_int(roman: str) -> int:
    vals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100}
    total, prev = 0, 0
    for ch in reversed(roman.upper()):
        v = vals.get(ch, 0)
        if v >= prev:
            total += v
        else:
            total -= v
        prev = v
    return total


def parse_sonnets(raw_text: str) -> list[SonnetData]:
    body = _strip_boilerplate(raw_text)

    # Roman-numeral headings appear on their own line, optionally indented
    pattern = re.compile(r"^\s{0,4}([IVXLC]+)\s*$", re.MULTILINE)
    headings = list(pattern.finditer(body))

    if len(headings) < 154:
        raise ValueError(
            f"Expected at least 154 sonnet headings, found {len(headings)}. "
            "The Gutenberg file format may have drifted — try --regenerate."
        )

    sonnets: list[SonnetData] = []
    for i, match in enumerate(headings[:154]):
        number = _roman_to_int(match.group(1).strip())
        chunk_start = match.end()
        chunk_end = headings[i + 1].start() if i + 1 < len(headings) else len(body)
        chunk = body[chunk_start:chunk_end]

        lines = [ln.strip() for ln in chunk.splitlines() if ln.strip()]

        excluded = False
        exclusion_reason: str | None = None

        if number == SONNET_126_ID:
            excluded = True
            exclusion_reason = (
                "Sonnet 126 has only 12 lines (no closing couplet); excluded from the pool."
            )
        elif number == SONNET_99_ID and len(lines) == 15:
            # Drop the supernumerary opening line; use the standard 14
            lines = lines[1:]

        if not excluded:
            if len(lines) != 14:
                logger.warning(
                    "Sonnet %d has %d lines (expected 14); proceeding with available lines.",
                    number,
                    len(lines),
                )
            line_12 = lines[11] if len(lines) > 11 else ""
            line_13 = lines[12] if len(lines) > 12 else ""
        else:
            line_12 = ""
            line_13 = ""

        sonnets.append(
            SonnetData(
                id=number,
                title=f"Sonnet {number}",
                source="Project Gutenberg #1041",
                full_text="\n".join(lines),
                line_12=line_12,
                line_13=line_13,
                excluded=excluded,
                exclusion_reason=exclusion_reason,
            )
        )

    sonnets.sort(key=lambda s: s["id"])
    return sonnets


def load_sonnets_json(path: Path) -> list[SonnetData]:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def save_sonnets_json(sonnets: list[SonnetData], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(sonnets, f, indent=2, ensure_ascii=False)
    logger.info("Saved %d sonnet records to %s.", len(sonnets), path)


def sha256_line(line: str) -> str:
    return hashlib.sha256(line.encode()).hexdigest()
