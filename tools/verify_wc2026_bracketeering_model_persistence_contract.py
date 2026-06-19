#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "captures/CAPTURE_BACK_BRACKETEERING_MODEL_PERSISTENCE_CONTRACT.md",
    "cards/222_confirm_bracketeering_model_persistence_contract_card.md",
    "docs/architecture/bracketeering_model_persistence_contract.md",
    "li/world_cup/bracketeering_model_persistence_contract_rule.md",
    "prompts/confirm_bracketeering_model_persistence_contract.md",
]

REQUIRED_TERMS = [
    "user_id",
    "game_id",
    "picks_json",
    "visibility",
    "submitted_at",
    "locked_at",
    "created_at",
    "updated_at",
    "WRITE is private",
    "READ can be shared",
    "draft",
    "submitted",
    "locked",
    "BracketStore",
]

errors = []
for rel in REQUIRED_FILES:
    path = ROOT / rel
    if not path.exists():
        errors.append(f"Missing required file: {rel}")
        continue
    text = path.read_text(encoding="utf-8")
    for term in REQUIRED_TERMS:
        if term not in text:
            errors.append(f"{rel} missing required term: {term}")

map_path = ROOT / "MAP.md"
if map_path.exists():
    map_text = map_path.read_text(encoding="utf-8")
    if "Bracketeering Model Persistence Contract" not in map_text:
        errors.append("MAP.md missing Bracketeering Model Persistence Contract entry")
else:
    errors.append("Missing MAP.md")

if errors:
    print("Bracketeering model persistence contract verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("Bracketeering model persistence contract verification passed.")
