#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def main() -> None:
    errors: list[str] = []

    required_files = [
        "cards/227_normalize_runtime_to_full_canonical_bracket_document_card.md",
        "docs/architecture/bracketeering_canonical_bracket_document_runtime.md",
        "docs/architecture/wc2026_canonical_pick_state_storage_model.md",
        "docs/architecture/bracketeering_model_persistence_contract.md",
        "docs/backend/wc2026_supabase_shared_pick_sql_target.md",
        "li/world_cup/canonical_bracket_document_runtime_rule.md",
        "li/world_cup/canonical_pick_state_storage_model_rule.md",
        "site/data/model/bracket_slots.json",
        "site/js/model/UserBracketModel.js",
        "site/js/services/LocalStorageBracketStore.js",
    ]
    for path in required_files:
        if not (ROOT / path).exists():
            errors.append(f"missing required file: {path}")

    if errors:
        fail("\n".join(errors))

    docs_blob = "\n".join(
        read(path)
        for path in [
            "cards/227_normalize_runtime_to_full_canonical_bracket_document_card.md",
            "docs/architecture/bracketeering_canonical_bracket_document_runtime.md",
            "docs/architecture/wc2026_canonical_pick_state_storage_model.md",
            "docs/architecture/bracketeering_model_persistence_contract.md",
            "docs/backend/wc2026_supabase_shared_pick_sql_target.md",
            "li/world_cup/canonical_bracket_document_runtime_rule.md",
            "li/world_cup/canonical_pick_state_storage_model_rule.md",
        ]
    )

    for token in [
        "BracketDocument",
        "picksBySlot",
        "expectedPickCount",
        "Runtime model first. Supabase persistence second.",
        "CHAMPION",
        "THIRD-PLACE-WINNER",
        "Game 1 expected total: 64",
        "Game 2 expected total: 32",
        "user_brackets.picks_json",
    ]:
        if token not in docs_blob:
            errors.append(f"docs/LI missing canonical runtime token: {token}")

    slots = json.loads(read("site/data/model/bracket_slots.json"))
    canonical_slots = slots.get("canonicalPickSlots")
    if not isinstance(canonical_slots, list):
        errors.append("site/data/model/bracket_slots.json must define canonicalPickSlots")
        canonical_slots = []

    slot_by_id = {slot.get("slotId") or slot.get("sitePickId"): slot for slot in canonical_slots if isinstance(slot, dict)}
    game_counts = slots.get("canonicalPickCounts") or {}

    if game_counts.get("game1") != 64:
        errors.append("canonicalPickCounts.game1 must be 64")
    if game_counts.get("game2") != 32:
        errors.append("canonicalPickCounts.game2 must be 32")
    if len(canonical_slots) != 64:
        errors.append(f"canonicalPickSlots must contain 64 game1 slots, found {len(canonical_slots)}")

    for slot_id in ["CHAMPION", "THIRD-PLACE-WINNER"]:
        if slot_id not in slot_by_id:
            errors.append(f"canonicalPickSlots missing first-class slot: {slot_id}")

    champion = slot_by_id.get("CHAMPION", {})
    third = slot_by_id.get("THIRD-PLACE-WINNER", {})
    if champion.get("kind") != "winner" or champion.get("round") not in {"CHAMPION", "FINAL"}:
        errors.append("CHAMPION canonical slot must be a winner/final slot")
    if third.get("kind") != "winner" or third.get("round") != "THIRD_PLACE":
        errors.append("THIRD-PLACE-WINNER canonical slot must be a THIRD_PLACE winner slot")

    model_js = read("site/js/model/UserBracketModel.js")
    for token in [
        "createEmptyBracketDocument",
        "normalizeBracketDocument",
        "picksBySlot",
        "expectedPickCount",
        "canonicalPickSlotsFromModel",
        "legacyPicksFromPicksBySlot",
    ]:
        if token not in model_js:
            errors.append(f"UserBracketModel.js missing canonical runtime token: {token}")

    local_store_js = read("site/js/services/LocalStorageBracketStore.js")
    for token in ["normalizeBracketDocument", "saveUserBracket", "picksBySlot"]:
        if token not in local_store_js:
            errors.append(f"LocalStorageBracketStore.js missing canonical storage token: {token}")

    makefile = read("Makefile")
    if "verify_wc2026_full_canonical_bracket_document_runtime.py" not in makefile:
        errors.append("Makefile must wire verify_wc2026_full_canonical_bracket_document_runtime.py into make verify")

    forbidden = ["@supabase/supabase-js", "createClient(", "SUPABASE_URL", "SUPABASE_ANON_KEY"]
    runtime_blob = "\n".join(
        read(path)
        for path in [
            "site/js/model/UserBracketModel.js",
            "site/js/services/LocalStorageBracketStore.js",
            "site/js/services/BracketRepository.js",
        ]
    )
    for token in forbidden:
        if token in runtime_blob:
            errors.append(f"Card 227 must not introduce Supabase runtime dependency: {token}")

    if errors:
        fail("\n".join(errors))

    print("OK: WC2026 runtime uses full canonical BracketDocument model before Supabase persistence.")


if __name__ == "__main__":
    main()
