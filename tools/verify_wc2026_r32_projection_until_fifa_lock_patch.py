#!/usr/bin/env python3
from pathlib import Path

required = [
    Path("capture_back/CAPTURE_BACK_R32_PROJECTION_UNTIL_FIFA_LOCK.md"),
    Path("cards/134_define_r32_projection_until_fifa_lock_card.md"),
    Path("docs/features/r32_projection_until_fifa_lock.md"),
    Path("li/world_cup/r32_projection_until_fifa_lock_rule.md"),
    Path("prompts/define_r32_projection_until_fifa_lock.md"),
]
missing = [str(p) for p in required if not p.exists()]
if missing:
    raise SystemExit("Missing files: " + ", ".join(missing))

store = Path("site/data/game1_bracket_pick_store.js").read_text()
for token in [
    "WC2026_R32_PROJECTION_UNTIL_FIFA_LOCK_STORE_START",
    "wc2026.game1.r32.assignmentState",
    "loadR32AssignmentState",
    "saveR32AssignmentState",
    "canEditR32",
]:
    if token not in store:
        raise SystemExit(f"Missing store token: {token}")

index = Path("site/game1/index.html").read_text()
for token in [
    "WC2026_R32_PROJECTION_UNTIL_FIFA_LOCK_UI_START",
    "WC2026_R32_PROJECTION_UNTIL_FIFA_LOCK_RUNTIME_START",
    "WC2026_R32_ASSIGNMENT_PHASE",
    "R32 projection: editable until FIFA lock",
]:
    if token not in index:
        raise SystemExit(f"Missing index token: {token}")

print("WC2026 R32 projection-until-FIFA-lock patch verified.")
