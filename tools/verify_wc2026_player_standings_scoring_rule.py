#!/usr/bin/env python3
from pathlib import Path

paths = {
    "rule": Path("li/world_cup/player_standings_scoring_rule.md"),
    "docs": Path("docs/features/player_standings_scoring.md"),
    "card": Path("cards/292_player_standings_scoring_rule_card.md"),
    "capture": Path("captures/CAPTURE_BACK_PLAYER_STANDINGS_SCORING_RULE.md"),
}

errors = []

for label, path in paths.items():
    if not path.exists():
        errors.append(f"Missing {label}: {path}")

texts = {label: path.read_text() for label, path in paths.items() if path.exists()}
combined = "\n".join(texts.values())

required_tokens = [
    "R16 correct pick: 1 point",
    "R8 correct pick: 2 points",
    "R4 correct pick: 4 points",
    "R2 correct pick: 8 points",
    "Champion/Winner correct pick: 16 points",
    "Total perfect score: 56 points",
    "earned points",
    "maximum possible points",
    "Admin_/official",
    "canonical team ID",
    "Unresolved official slots",
    "eliminated",
]

for token in required_tokens:
    if token not in combined:
        errors.append(f"Missing scoring rule token: {token}")

makefile = Path("Makefile").read_text()
if "python3 tools/verify_wc2026_player_standings_scoring_rule.py" not in makefile:
    errors.append("Makefile verify must include player standings scoring rule verifier.")

if errors:
    print("WC2026 Player Standings scoring rule verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: Player Standings scoring rule defines earned points, max possible points, round weights, and Admin_/official truth.")
