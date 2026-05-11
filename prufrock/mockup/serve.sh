#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)/screenshots/v2/html"
PORT="${1:-8080}"

if ! command -v python3 &>/dev/null; then
  echo "python3 not found" >&2
  exit 1
fi

echo "Serving demo at http://localhost:$PORT/00-index.html"
echo "Press Ctrl-C to stop."

open "http://localhost:$PORT/00-index.html" 2>/dev/null || true

cd "$ROOT"
exec python3 -m http.server "$PORT"
