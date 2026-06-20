#!/usr/bin/env python3
"""Check live GitHub Pages critical JSON freshness against local site/ source."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time
import urllib.request
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
SITE_DIR = REPO_ROOT / "site"
PAGES_URL = os.environ.get(
    "WC2026_PAGES_URL",
    "https://johnson21228.github.io/wc2026-bracket-tracker-li/",
).rstrip("/") + "/"
CRITICAL_JSON_PATHS = [
    "data/current/group_matches.json",
    "data/current/group_standings.json",
    "data/current/match_highlights.json",
]
CANARY_MATCHES = {
    "GS-2026-06-19-C3": ("Brazil 3-0 Haiti", "final", 3, 0),
    "66456934": ("Scotland 0-1 Morocco", "final", 0, 1),
    "66456946": ("Turkey 0-1 Paraguay", "final", 0, 1),
    "66456944": ("United States 2-0 Australia", "final", 2, 0),
}


def canonical_hash(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def read_source(path: str) -> Any:
    return json.loads((SITE_DIR / path).read_text(encoding="utf-8"))


def read_live(path: str, cache_buster: str) -> Any:
    url = f"{PAGES_URL}{path}?v={cache_buster}"
    request = urllib.request.Request(url, headers={"Cache-Control": "no-cache", "Pragma": "no-cache"})
    with urllib.request.urlopen(request, timeout=20) as response:
        return json.loads(response.read().decode("utf-8"))


def extract_matches(data: Any) -> list[dict[str, Any]]:
    if isinstance(data, list):
        return [item for item in data if isinstance(item, dict)]
    if isinstance(data, dict):
        for key in ("matches", "groupMatches", "items", "data"):
            value = data.get(key)
            if isinstance(value, list):
                return [item for item in value if isinstance(item, dict)]
        for value in data.values():
            if isinstance(value, list) and value and isinstance(value[0], dict):
                return value
    return []


def check_canaries(group_matches_data: Any) -> list[str]:
    matches = extract_matches(group_matches_data)
    by_id: dict[str, dict[str, Any]] = {}
    for match in matches:
        match_id = str(match.get("matchId", ""))
        espn_id = str(match.get("espnMatchId", ""))
        if match_id:
            by_id[match_id] = match
        if espn_id:
            by_id[espn_id] = match

    failures: list[str] = []
    for key, expected in CANARY_MATCHES.items():
        match = by_id.get(key)
        if not match:
            failures.append(f"{key}: missing live row")
            continue
        observed = (match.get("summary"), match.get("status"), match.get("homeScore"), match.get("awayScore"))
        if observed != expected:
            failures.append(f"{key}: expected {expected}, observed {observed}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify live Pages data matches local source JSON.")
    parser.add_argument("--attempts", type=int, default=int(os.environ.get("WC2026_PAGES_VERIFY_ATTEMPTS", "1")))
    parser.add_argument("--sleep", type=float, default=float(os.environ.get("WC2026_PAGES_VERIFY_SLEEP_SECONDS", "5")))
    args = parser.parse_args()

    cache_base = os.popen("git rev-parse --short=12 HEAD").read().strip() or str(int(time.time()))
    last_failures: list[str] = []
    for attempt in range(1, args.attempts + 1):
        failures: list[str] = []
        live_group_matches: Any | None = None
        for path in CRITICAL_JSON_PATHS:
            try:
                source = read_source(path)
                live = read_live(path, f"{cache_base}-{attempt}")
                if path == "data/current/group_matches.json":
                    live_group_matches = live
                source_hash = canonical_hash(source)
                live_hash = canonical_hash(live)
                if source_hash != live_hash:
                    failures.append(f"{path}: stale/mismatched live JSON source={source_hash[:12]} live={live_hash[:12]}")
                else:
                    print(f"OK: {path} live JSON matches source")
            except Exception as exc:  # noqa: BLE001 - report exact failure and fail closed
                failures.append(f"{path}: {exc}")

        if live_group_matches is not None:
            failures.extend(check_canaries(live_group_matches))

        if not failures:
            print("OK: live Pages critical JSON is fresh.")
            return 0

        last_failures = failures
        if attempt < args.attempts:
            print(f"Live Pages freshness attempt {attempt}/{args.attempts} failed; retrying...")
            time.sleep(args.sleep)

    print("FAIL: live Pages critical JSON is stale or mismatched.")
    for failure in last_failures:
        print(f"- {failure}")
    return 3


if __name__ == "__main__":
    raise SystemExit(main())
