from pathlib import Path

root = Path(__file__).resolve().parents[1]
index = root / "site" / "game1" / "index.html"
text = index.read_text()
required = [
    "WC2026_BRACKET_PICK_FINALITY_VALIDATION_START",
    "WC2026_VALIDATE_BRACKET_PICK_FINALITY",
    "WC2026_VALIDATE_ALL_BRACKET_PICK_FINALITY",
    "data-choice-can-remain-final",
    "duplicateR32Locations",
]
missing = [item for item in required if item not in text]
if missing:
    raise SystemExit("Missing finality validation markers: " + ", ".join(missing))

for rel in [
    "cards/135_define_bracket_pick_finality_validation_card.md",
    "docs/features/bracket_pick_finality_validation.md",
    "li/world_cup/bracket_pick_finality_validation_rule.md",
]:
    if not (root / rel).exists():
        raise SystemExit(f"Missing {rel}")

print("WC2026 bracket pick finality validation patch verified.")
