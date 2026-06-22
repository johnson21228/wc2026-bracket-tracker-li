#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main() -> int:
    view = (ROOT / "site/js/mvc/view.js").read_text()
    controller = (ROOT / "site/js/mvc/controller.js").read_text() if (ROOT / "site/js/mvc/controller.js").exists() else ""

    combined = view + "\n" + controller

    required_docs = [
        ROOT / "docs/features/lifecycle_stage_presentation_only.md",
        ROOT / "li/world_cup/lifecycle_stage_presentation_only_rule.md",
    ]
    doc_text = "\n".join(path.read_text() for path in required_docs if path.exists())

    errors = []

    for token in [
        "lifecycle stage is presentation-only",
        "pick availability is determined only by precedent availability",
        "selected stage must not block pick pre-selection",
    ]:
        if token not in doc_text:
            errors.append(f"missing presentation-only contract token: {token}")

    for token in [
        "is-disabled-by-active-game",
        "data-disabled-by-active-game",
        "data-active-game-disabled",
        "only accepts Round of 32 picks",
        "starts after the Round of 32 field",
    ]:
        if token in combined:
            errors.append(f"stage-only controller/view gate remains: {token}")

    if errors:
        print("WC2026 lifecycle stage presentation-only pick pipeline verification failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("OK: lifecycle stage no longer blocks pick pre-selection or pick write pipeline.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
