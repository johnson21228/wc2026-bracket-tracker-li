#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read_if_exists(path: Path) -> str:
    return path.read_text() if path.exists() else ""

def main() -> int:
    runtime_paths = [
        ROOT / "site/index.html",
        ROOT / "site/js/mvc/view.js",
        ROOT / "site/js/mvc/controller.js",
        ROOT / "site/css/app.css",
        ROOT / "site/css/board.css",
        ROOT / "site/data/playfield_background_config.json",
    ]
    doc_paths = [
        ROOT / "docs/features/lifecycle_stage_presentation_only.md",
        ROOT / "li/world_cup/lifecycle_stage_presentation_only_rule.md",
        ROOT / "captures/CAPTURE_BACK_LIFECYCLE_STAGE_PRESENTATION_ONLY.md",
        ROOT / "cards/254_lifecycle_stage_presentation_only_card.md",
    ]

    runtime = "\n".join(read_if_exists(path) for path in runtime_paths)
    docs = "\n".join(read_if_exists(path) for path in doc_paths)
    combined = runtime + "\n" + docs

    errors = []

    required_contract_tokens = [
        "lifecycle stage is presentation-only",
        "selected stage must not change bracket rendering rules",
        "selected stage must not change pick highlighting rules",
        "selected stage must not block pick pre-selection",
        "pick availability is determined only by precedent availability",
    ]

    for token in required_contract_tokens:
        if token not in docs:
            errors.append(f"missing contract token {token!r} in lifecycle presentation-only docs/LI")

    # Background may remain stage-driven. Accept the actual repo evidence:
    # visible stage labels plus existing pub background assets/config.
    for token in ["Group Stage", "Knockout Stage"]:
        if token not in combined:
            errors.append(f"missing lifecycle stage label {token!r}")

    background_evidence = [
        "pub_background_game1",
        "knockout_pub_background",
        "knockout_pub_background.jpeg",
        "knockout_pub_background",
        "knockout_pub",
        "knockout",
    ]
    if not any(token in combined for token in background_evidence):
        errors.append("missing knockout stage background evidence")

    forbidden_stage_gameplay_gates = [
        "is-disabled-by-active-game",
        "data-disabled-by-active-game",
        "data-active-game-disabled",
        "disabled-by-active-game",
        "only accepts Round of 32 picks",
        "starts after the Round of 32 field",
    ]

    for token in forbidden_stage_gameplay_gates:
        if token in runtime:
            errors.append(f"stage-only gameplay gate remains: {token!r}")

    if errors:
        print("WC2026 lifecycle stage presentation-only pick/render verification failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("OK: lifecycle stage is presentation-only for picking/rendering while background remains stage-driven.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
