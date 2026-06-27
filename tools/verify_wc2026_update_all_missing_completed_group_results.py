#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

capture = ROOT / "captures" / "CAPTURE_BACK_UPDATE_ALL_MISSING_COMPLETED_GROUP_RESULTS.md"
card = ROOT / "cards" / "299_update_all_missing_completed_group_results_card.md"

def require(condition, message):
    if not condition:
        raise SystemExit(f"WC2026 update-all-missing-results CB verification failed: {message}")

capture_text = capture.read_text() if capture.exists() else ""
card_text = card.read_text() if card.exists() else ""

for token in [
    "Update every completed group-stage match result",
    "still-unplayed final Group J/K/L matches",
    "Panama vs England",
    "Croatia vs Ghana",
    "Colombia vs Portugal",
    "DR Congo vs Uzbekistan",
    "Algeria vs Austria",
    "Jordan vs Argentina",
    "Do not change R32/pick interaction behavior",
]:
    require(token in capture_text, f"capture missing token: {token}")

for token in [
    "data/results update only",
    "R32 pick behavior",
    "preselection behavior",
    "Verification passes",
]:
    require(token in card_text, f"card missing token: {token}")

print("OK: update-all-missing-completed-group-results CB is captured and bounded.")
