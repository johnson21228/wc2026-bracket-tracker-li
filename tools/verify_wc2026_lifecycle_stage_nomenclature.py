#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def read(rel: str) -> str:
    path = ROOT / rel
    if not path.exists():
        raise SystemExit(f"Missing required file: {rel}")
    return path.read_text(encoding="utf-8")


def main() -> int:
    errors = []
    index = read("site/index.html")
    view = read("site/js/mvc/view.js")
    makefile = read("Makefile")
    capture = read("captures/CAPTURE_BACK_LIFECYCLE_STAGE_NOMENCLATURE.md")
    card = read("cards/253_lifecycle_stage_nomenclature_card.md")
    doc = read("docs/features/lifecycle_stage_nomenclature.md")
    rule = read("li/world_cup/lifecycle_stage_nomenclature_rule.md")

    combined_li = "\n".join([capture, card, doc, rule])

    required_li_tokens = [
        "gameLifecycle.stage",
        "group_stage",
        "knockout",
        "Group Stage",
        "Knockout Stage",
        "Stage selector",
        "legacy game1/game2",
        "WRITE is private",
    ]
    for token in required_li_tokens:
        if token not in combined_li:
            errors.append(f"missing lifecycle-stage LI token: {token}")

    if "python3 tools/verify_wc2026_lifecycle_stage_nomenclature.py" not in makefile:
        errors.append("Makefile verify target must run lifecycle stage nomenclature verifier")

    # Player-facing Info panel now uses one-game Bracketeering copy.
    if "This is your World Cup Bracketeering Hub." not in index:
        errors.append("site/index.html should expose current Bracketeering Hub info copy")
    if "There is no tiebreaker at the moment." not in index:
        errors.append("site/index.html should expose current knockout scoring copy")
    stale_info_terms = [
        "The game has two parts",
        "Group Stage Picks",
        "Knockout Round Picks",
        "Group Stage points:",
    ]
    for token in stale_info_terms:
        if token in index:
            errors.append(f"site/index.html still exposes stale Info panel copy: {token}")

    forbidden_index_terms = ["Game selector", "Game View", "DEV GAME VIEW"]
    for token in forbidden_index_terms:
        if token in index:
            errors.append(f"player-facing index still contains old game-modality wording: {token}")

    # New lifecycle-stage hooks are allowed to coexist with legacy game-selector hooks during migration.
    if "data-game-selector" in index and "data-lifecycle-stage-selector" not in index:
        errors.append("banner selector should add data-lifecycle-stage-selector beside legacy data-game-selector")
    if "data-game-selector-button" in index and "data-lifecycle-stage-button" not in index:
        errors.append("banner selector buttons should add data-lifecycle-stage-button beside legacy game button hooks")

    if "[data-game-selector]," in view and "[data-lifecycle-stage-selector]," not in view:
        errors.append("board gesture exclusion list should recognize data-lifecycle-stage-selector")
    if "[data-game-selector-button]," in view and "[data-lifecycle-stage-button]," not in view:
        errors.append("board gesture exclusion list should recognize data-lifecycle-stage-button")

    # If a stage translation layer is present, require the canonical enum values.
    if "GAME_LIFECYCLE_STAGES" in view:
        for token in ['GROUP_STAGE: "group_stage"', 'KNOCKOUT: "knockout"', "LIFECYCLE_STAGE_BY_GAME_ID"]:
            if token not in view:
                errors.append(f"view stage translation missing token: {token}")

    if errors:
        print("WC2026 lifecycle stage nomenclature verification failed: " + "; ".join(errors))
        return 1

    print("OK: WC2026 banner/game modality nomenclature is now lifecycle-stage based while preserving legacy game hooks during migration.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
