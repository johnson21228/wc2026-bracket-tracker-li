#!/usr/bin/env python3
"""Verify the empty pick-state storage LI refinement is captured."""
from pathlib import Path

REQUIRED = {
    "li/world_cup/canonical_pick_state_storage_model_rule.md": [
        "complete empty pick-state shell",
        "game1`: 32 Round-of-32 entrant slots",
        "game2`: 16 Round-of-32 winners",
        "A missing required slot is a model error",
        "An empty required slot is a valid draft value",
        "THIRD-PLACE-WINNER",
    ],
    "docs/architecture/wc2026_canonical_pick_state_storage_model.md": [
        "Empty-document invariant",
        "game1` always has 64 slot records",
        "game2` always has 32 slot records",
        "unpicked slot has `pick: null`",
        "third-place winner is an explicit stored pick",
        "LocalStorageBracketStore now",
    ],
    "cards/212_route_local_storage_through_canonical_pick_state_card.md": [
        "64 explicit required slots",
        "32 explicit required slots",
        "Unpicked slots must be represented as explicit empty values",
        "createEmptyPickState(gameId)",
        "Existing local pick data must not be discarded",
        "The site-running invariant wins",
    ],
    "captures/CAPTURE_BACK_EMPTY_PICK_STATE_STORAGE_MODEL.md": [
        "complete empty pick-state document",
        "Game 1: 64 explicit pick slots",
        "Game 2: 32 explicit pick slots",
    ],
}

missing = []
for path, needles in REQUIRED.items():
    p = Path(path)
    if not p.exists():
        missing.append(f"missing file: {path}")
        continue
    text = p.read_text()
    for needle in needles:
        if needle not in text:
            missing.append(f"{path}: missing phrase {needle!r}")

if missing:
    print("WC2026 empty pick-state storage LI verification failed:")
    for item in missing:
        print(f"- {item}")
    raise SystemExit(1)

print("OK: WC2026 empty pick-state storage LI refinement is captured and verified.")
