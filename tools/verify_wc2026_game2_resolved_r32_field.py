#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read(path: str) -> str:
    return (ROOT / path).read_text()

def main() -> int:
    errors = []

    view = read("site/js/mvc/view.js")
    data = read("site/data/game2_fifa_final_r32_assignments.json")

    required_view_tokens = [
        "game2ResolvedTeam",
        "game2ResolvedSource",
        "readOnlyGame2R32Display",
        "data-game2-readonly-r32",
        "data-game2-resolved-r32-source",
        "slotEnabledByPrecedent(slot)",
    ]

    for token in required_view_tokens:
        if token not in view:
            errors.append(f"Missing {token!r} in site/js/mvc/view.js")

    required_data_tokens = [
        "fifa_final_truth_target",
        "game1_r32_picks",
    ]

    for token in required_data_tokens:
        if token not in data:
            errors.append(f"Missing {token!r} in site/data/game2_fifa_final_r32_assignments.json")

    forbidden_tokens = [
        "slotEnabledForActiveGame",
        "enabledForActiveGame",
        "disabledByActiveGame",
        "is-disabled-by-active-game",
        "data-disabled-by-active-game",
        "data-active-game-disabled",
        "Group Stage only accepts Round of 32 picks.",
        "Knockout Stage starts after the Round of 32 field.",
    ]

    for token in forbidden_tokens:
        if token in view:
            errors.append(f"Stale active-game gameplay gate remains in view.js: {token!r}")

    if errors:
        for error in errors:
            print(error)
        return 1

    print("OK: Game 2 resolved R32 field renders FIFA-final assignments with Game 1 fallback while lifecycle stage does not gate picks.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
