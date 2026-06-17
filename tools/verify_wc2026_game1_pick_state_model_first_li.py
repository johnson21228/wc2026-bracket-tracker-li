#!/usr/bin/env python3
from pathlib import Path

required = {
    "li/world_cup/game1_pick_state_model_first_rule.md": [
        "The UI is not the authority.",
        "WC2026_GAME1_PICK_STATE",
        "No render layer may render a downstream pick directly from localStorage.",
        "Do not add another late DOM scrub",
    ],
    "docs/features/game1_pick_state_model_first.md": [
        "The bracket bugs are not primarily visual bugs. They are state-authority bugs.",
        "const pick = storedPickForSlot(rule.slotId);",
        "const pick = model.getPick(slotId);",
    ],
    "cards/153_capture_game1_pick_state_model_first_insight_card.md": [
        "Card 153",
        "Build the data model first.",
        "window.WC2026_GAME1_PICK_STATE",
    ],
    "MAP.md": [
        "Game 1 Pick State Model-First Capture",
        "game1_pick_state_model_first_rule.md",
    ],
}

missing = []
for rel, needles in required.items():
    path = Path(rel)
    if not path.exists():
        missing.append(f"missing file: {rel}")
        continue
    text = path.read_text()
    for needle in needles:
        if needle not in text:
            missing.append(f"{rel}: missing marker {needle!r}")

if missing:
    print("WC2026 Game 1 pick-state model-first LI verification failed:")
    for item in missing:
        print(f"- {item}")
    raise SystemExit(1)

print("WC2026 Game 1 pick-state model-first LI verification passed.")
