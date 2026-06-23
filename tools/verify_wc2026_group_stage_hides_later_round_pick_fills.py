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
    "const pickFillSuppressed = shouldSuppressPickFillForSlot(slot);",
    'pickFillSuppressed\n            ? `${playerFacingSlotLabel(slot)}: pick hidden during Group Stage`',
    "if (!pickFillSuppressed) {",
    'button.classList.add("is-pick-fill-suppressed")',
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

non_suppressed_branch = "if (!pickFillSuppressed) {"
unpicked_label = "unpicked-cell-label"
button_append = "button.append(label, value);"

if non_suppressed_branch not in view:
    errors.append("suppressed later-round slots must skip all visible label/value rendering.")
else:
    branch_start = view.index(non_suppressed_branch)
    if view.find(unpicked_label, branch_start) < 0:
        errors.append("unpicked-cell-label should remain only in the non-suppressed render branch.")
    if view.find(button_append, branch_start) < 0:
        errors.append("label/value append should happen only in the non-suppressed render branch.")

if "button.disabled = shouldSuppressPickFillForSlot" in view:
    errors.append("Suppression must remain rendering-only and must not disable pick buttons.")

if "activeGameValue() === \"game-1\"" in view and "activeGameValue() === \"game-2\"" in view:
    pass
else:
    errors.append("Verifier expects Group Stage suppression and Knockout/Game 2 display to remain separate.")

if errors:
    raise SystemExit("WC2026 group-stage frame-only later-round verification failed: " + "; ".join(errors))

print("OK: Group Stage renders later-round pick slots as frame-only, while Knockout Stage restores fills, labels, and team rendering.")
