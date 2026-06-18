#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
errors = []

def read(path):
    p = ROOT / path
    if not p.exists():
        errors.append(f"Missing {path}")
        return ""
    return p.read_text()

def require_contains(path, token):
    text = read(path)
    if token not in text:
        errors.append(f"{path} missing token: {token}")

for path in [
    "li/world_cup/pick_conflicts_warn_not_block_rule.md",
    "docs/features/pick_conflicts_warn_not_block.md",
    "cards/207_pick_conflicts_warn_not_block_card.md",
    "capture_back/CAPTURE_BACK_PICK_CONFLICTS_WARN_NOT_BLOCK.md",
]:
    require_contains(path, "conflict")

model = read("site/js/mvc/model.js")
require_contains("site/js/mvc/model.js", "Team is outside this slot's source scope.")
require_contains("site/js/mvc/model.js", "conflicts are rendered as warnings, not cleared as side effects")
require_contains("site/js/mvc/model.js", "return [];")
require_contains("site/js/mvc/model.js", "is already assigned to another Round of 32 slot")
require_contains("site/js/mvc/view.js", "has-invalid-pick")
require_contains("site/js/mvc/view.js", "picked-cell-warning")
require_contains("site/css/board.css", ".pick-slot-button.has-invalid-pick")
require_contains("site/css/board.css", ".picked-cell-warning")

validate_match = re.search(r"function validatePick\(slotId, teamId\) \{(?P<body>.*?)\n  \}\n\n  function cascadeClearInvalidDescendants", model, re.S)
if not validate_match:
    errors.append("Could not find validatePick block")
else:
    body = validate_match.group("body")
    if "already assigned to another Round of 32 slot" in body:
        errors.append("validatePick still blocks duplicate R32 picks instead of leaving them to rendering validity")
    if "duplicate" in body.lower():
        errors.append("validatePick still contains duplicate conflict logic")

cascade_match = re.search(r"function cascadeClearInvalidDescendants\(\) \{(?P<body>.*?)\n  \}\n\n  function setPick", model, re.S)
if not cascade_match:
    errors.append("Could not find cascadeClearInvalidDescendants block")
else:
    body = cascade_match.group("body")
    if "delete picks" in body:
        errors.append("cascadeClearInvalidDescendants still deletes picks")

makefile = read("Makefile")
if "tools/verify_wc2026_pick_conflicts_warn_not_block.py" not in makefile:
    errors.append("Makefile verify target does not run pick conflict verifier")

if errors:
    print("WC2026 pick conflicts warn-not-block verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: pick conflicts are preserved and rendered as warnings, not blocked.")
