#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors = []

def read(rel):
    path = ROOT / rel
    if not path.exists():
        errors.append(f"missing file: {rel}")
        return ""
    return path.read_text(encoding="utf-8")

li = read("li/world_cup/editable_site_official_truth_json_rule.md")
doc = read("docs/features/editable_site_official_truth_json.md")
card = read("cards/298_editable_site_official_truth_json_card.md")
capture = read("captures/CAPTURE_BACK_EDITABLE_SITE_OFFICIAL_TRUTH_JSON.md")
makefile = read("Makefile")
combined = "\n".join([li, doc, card, capture])

required_text = [
    "site/data/current/official_truth.json",
    "picksBySlot",
    "same effective payload contract previously supplied by the Supabase `Admin_/official` official row",
    "The file may be partial",
    "R32 occupant records are official input records",
    "Official knockout result records use the same canonical winner slot IDs used by player picks and scoring",
    "Player standings are computed, not stored",
    "player picks from Supabase",
    "official truth from `site/data/current/official_truth.json`",
]

for token in required_text:
    if token not in combined:
        errors.append(f"missing editable official truth LI token: {token}")

truth_path = ROOT / "site/data/current/official_truth.json"
if not truth_path.exists():
    errors.append("missing site/data/current/official_truth.json")
else:
    try:
        truth = json.loads(truth_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"official_truth.json is invalid JSON: {exc}")
        truth = {}

    for key in ["schemaVersion", "tournamentId", "gameId", "picksBySlot"]:
        if key not in truth:
            errors.append(f"official_truth.json missing key: {key}")

    if truth.get("tournamentId") != "wc2026":
        errors.append("official_truth.json tournamentId must be wc2026")

    if truth.get("gameId") != "game1":
        errors.append("official_truth.json gameId must be game1")

    if not isinstance(truth.get("picksBySlot"), dict):
        errors.append("official_truth.json picksBySlot must be an object")

    for key in ["standings", "score", "maxPossible", "rank"]:
        if key in truth:
            errors.append(f"official_truth.json must not store computed standings authority: {key}")

if "python3 tools/verify_wc2026_editable_site_official_truth_json.py" not in makefile:
    errors.append("Makefile verify must include editable site official truth JSON verifier")

if errors:
    print("WC2026 editable site official truth JSON verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: Editable site official truth JSON contract is captured and initialized.")
