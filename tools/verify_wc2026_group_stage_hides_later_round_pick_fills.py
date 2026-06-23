#!/usr/bin/env python3
from pathlib import Path

view = Path("site/js/mvc/view.js").read_text()
errors = []

required_tokens = [
    "function isGroupStagePresentationActive()",
    'return activeGameValue() === "game-1";',
    "function shouldSuppressPickFillForSlot(slot)",
    'slot?.round !== "R32"',
    '!slotId.startsWith("R32")',
    "if (shouldSuppressPickFillForSlot(slot))",
    "return null;",
    "const displayTeam = displayTeamForSlot(slot);",
]

for token in required_tokens:
    if token not in view:
        errors.append(f"missing token in view.js: {token}")

game2_token = 'activeGameValue() === "game-2" && slot.round === "R32" && slot.game2ResolvedTeam'
suppress_token = "if (shouldSuppressPickFillForSlot(slot))"

if game2_token in view and suppress_token in view:
    if view.index(game2_token) > view.index(suppress_token):
        errors.append("Game 2 resolved R32 display must be handled before group-stage suppression.")
else:
    errors.append("Could not confirm Game 2 R32 display ordering.")

if "button.disabled = shouldSuppressPickFillForSlot" in view:
    errors.append("Suppression must remain rendering-only and must not disable pick buttons.")

if errors:
    raise SystemExit("WC2026 group-stage later-round fill suppression verification failed: " + "; ".join(errors))

print("OK: Group Stage presentation hides filled pick rendering after R32 while preserving stored picks and Knockout Stage rendering.")
