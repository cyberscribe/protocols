#!/usr/bin/env python3
"""
Combinatrix validator for §9.1 (Sonnet Trial).

Generates and validates the 13-row × 14-column authorship-rotation matrix A.

Definitions (n = 14):
  rows    — days 2..14 of the rotation (13 rows total)
  cols    — participants p ∈ {0..13}
  A[d][p] — index of the poem that participant p writes a line for on day d+2

Required properties (derived from formalisation.md §9.1):
  1. Shape: 13 × 14.
  2. No fixed points (no self-adjacency): A[d][p] ≠ p for every (d, p).
  3. Row property: each row is a derangement permutation of {0..13}
     (each poem advances by exactly one line per day).
  4. Column property: across the 13 rows, column p contains each of
     the 13 values in {0..13}\\{p} exactly once
     (each participant writes for each non-nominal poem exactly once).

Sampling is random across the space of valid matrices, per the project
decision to render the assignment as a random combinatrix rather than a
cyclic-shift Latin square (which would be a single deterministic family).
"""

import argparse
import random
import sys
from typing import List, Optional

N = 14
DAYS = 13  # rotation days (days 2..14)


def generate(rng: random.Random) -> Optional[List[List[int]]]:
    """Random Latin-rectangle derangement; returns None on dead end (caller retries)."""
    col_used: List[set[int]] = [set() for _ in range(N)]
    rows: List[List[int]] = []
    for _ in range(DAYS):
        row_used: set[int] = set()
        row = [-1] * N
        # Process columns in a random order so the search isn't biased.
        cols = list(range(N))
        rng.shuffle(cols)
        # Heuristic: process most-constrained columns first by re-sorting on
        # candidate-set size as we go (MRV). For n=14 this is overkill but
        # makes the failure rate negligible.
        remaining = set(cols)
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
            assert best_j is not None and best_cands is not None
            v = rng.choice(best_cands)
            row[best_j] = v
            row_used.add(v)
            col_used[best_j].add(v)
            remaining.remove(best_j)
        rows.append(row)
    return rows


def sample(seed: int, max_attempts: int = 1000) -> List[List[int]]:
    rng = random.Random(seed)
    for attempt in range(max_attempts):
        result = generate(rng)
        if result is not None:
            return result
    raise RuntimeError(f"Failed to sample a valid matrix after {max_attempts} attempts")


def validate(matrix: List[List[int]]) -> List[str]:
    errors: List[str] = []
    if len(matrix) != DAYS:
        errors.append(f"shape: expected {DAYS} rows, got {len(matrix)}")
    for d, row in enumerate(matrix):
        if len(row) != N:
            errors.append(f"row {d}: expected {N} cols, got {len(row)}")
        if sorted(row) != list(range(N)):
            errors.append(f"row {d}: not a permutation of 0..{N-1}: {row}")
        for p, v in enumerate(row):
            if v == p:
                errors.append(f"row {d} col {p}: fixed point (A[{d}][{p}] = {p})")
    for p in range(N):
        col = [matrix[d][p] for d in range(DAYS)]
        expected = sorted(v for v in range(N) if v != p)
        if sorted(col) != expected:
            errors.append(f"col {p}: expected each of {expected} once, got {sorted(col)}")
    return errors


def render_table(matrix: List[List[int]]) -> str:
    """Render as a human-readable table. Rows = days 2..14, cols = participants P0..P13."""
    out = []
    header = "Day  | " + " ".join(f"P{p:>2}" for p in range(N))
    out.append(header)
    out.append("-" * len(header))
    for d, row in enumerate(matrix, start=2):
        out.append(f"d={d:>2} | " + " ".join(f"P{v:>2}" for v in row))
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--seed", type=int, default=42, help="RNG seed (default 42)")
    ap.add_argument("--samples", type=int, default=1,
                    help="Number of independent matrices to generate and validate")
    ap.add_argument("--quiet", action="store_true", help="Suppress matrix print")
    args = ap.parse_args()

    all_ok = True
    for i in range(args.samples):
        seed = args.seed + i
        matrix = sample(seed)
        errors = validate(matrix)
        if errors:
            all_ok = False
            print(f"[seed={seed}] FAIL — {len(errors)} error(s):")
            for e in errors:
                print(f"  - {e}")
        else:
            print(f"[seed={seed}] OK — 13×14 derangement Latin rectangle, no fixed points.")
            if not args.quiet and args.samples == 1:
                print()
                print(render_table(matrix))

    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
