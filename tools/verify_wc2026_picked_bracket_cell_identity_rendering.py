#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

checks = {
    "site/js/mvc/view.js": [
        "picked-cell-identity",
        "picked-cell-flag",
        "picked-cell-code",
        "displayTeam.flag",
        "flag.style.fontSize",
        "displayTeam.abbr || displayTeam.id",
        "identity.append(flag, code)",
        "value.append(identity)",
    ],
    "site/css/board.css": [
        "Card 201: picked bracket cell compact identity rendering",
        ".pick-slot-button.has-pick .pick-slot-label",
        "display: none",
        ".picked-cell-identity",
        ".picked-cell-flag",
        ".picked-cell-code",
        "height: 100%",
    ],
    "li/world_cup/picked_bracket_cell_identity_rendering_rule.md": [
        "compact identity token",
        "flag visual",
        "canonical three-letter display code",
        "must not visibly render the full team name",
        "Emoji flags are scaled with font size",
    ],
    "docs/features/picked_bracket_cell_identity_rendering.md": [
        "[flag visual] [3-letter code]",
        "do not visibly show the full team name",
        "emoji flags",
    ],
    "cards/201_define_picked_bracket_cell_identity_rendering_card.md": [
        "Card 201",
        "flag visual",
        "three-letter code",
    ],
    "capture_back/CAPTURE_BACK_PICKED_BRACKET_CELL_IDENTITY_RENDERING.md": [
        "Picked Bracket Cell Identity Rendering",
        "[flag visual] [3-letter code]",
    ],
}

errors = []

for rel, needles in checks.items():
    path = ROOT / rel
    if not path.exists():
        errors.append(f"missing file: {rel}")
        continue
    text = path.read_text()
    for needle in needles:
        if needle not in text:
            errors.append(f"{rel} missing token: {needle}")

view = (ROOT / "site/js/mvc/view.js").read_text()

bad_visible_name_patterns = [
    "value.textContent = slot.selectedTeam ? teamLabel(slot.selectedTeam)",
    "code.textContent = slot.selectedTeam.name",
]

for pattern in bad_visible_name_patterns:
    if pattern in view:
        errors.append(f"picked-cell visible rendering still uses full team name pattern: {pattern}")

if errors:
    raise SystemExit("WC2026 picked bracket cell identity rendering verification failed:\n- " + "\n- ".join(errors))

print("OK: WC2026 picked bracket cell compact identity rendering is captured and verified.")
