#!/usr/bin/env python3
from pathlib import Path

paths = [
    Path("li/world_cup/player_standings_max_possible_reachability_rule.md"),
    Path("docs/features/player_standings_max_possible_reachability.md"),
    Path("cards/295_player_standings_max_possible_reachability_card.md"),
    Path("captures/CAPTURE_BACK_PLAYER_STANDINGS_MAX_POSSIBLE_REACHABILITY.md"),
]

errors = []

for path in paths:
    if not path.exists():
        errors.append(f"Missing file: {path}")

combined = "\n".join(path.read_text() for path in paths if path.exists())

required_tokens = [
    "Admin empty/unresolved is necessary but not sufficient",
    "could still become `Admin_/official` truth",
    "can still reach that slot",
    "already eliminated",
    "prior resolved `Admin_/official` truth",
    "Resolved matching picks count toward both Score and Max Possible",
    "Resolved mismatches count toward neither",
    "`Admin_/official` is the only source of elimination and scoring truth",
]

for token in required_tokens:
    if token not in combined:
        errors.append(f"Missing reachability rule token: {token}")

makefile = Path("Makefile").read_text()
if "python3 tools/verify_wc2026_player_standings_max_possible_reachability_rule.py" not in makefile:
    errors.append("Makefile verify must include max possible reachability verifier.")

if errors:
    print("WC2026 Player Standings max possible reachability rule verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: Player Standings Max Possible is defined as reachability-aware, not merely unresolved.")
