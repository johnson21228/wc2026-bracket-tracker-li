#!/usr/bin/env python3
from pathlib import Path


def require(condition, message, errors):
    if not condition:
        errors.append(message)


def read(path):
    return Path(path).read_text()


def main():
    errors = []

    capture = read("captures/CAPTURE_BACK_GAME1_GAME2_STATE_SEPARATION_NO_R16_PRESELECT_HIGHLIGHT.md")
    doc = read("docs/architecture/wc2026_game1_game2_state_separation_no_r16_preselect_highlight.md")
    rule = read("li/world_cup/game1_game2_state_separation_no_r16_preselect_highlight_rule.md")
    card = read("cards/281_game1_game2_state_separation_no_r16_preselect_highlight_card.md")
    makefile = read("Makefile")

    combined = "\n".join([capture, doc, rule, card])

    for token in [
        "Game 1",
        "Game 2",
        "R16+",
        "pre-select highlight",
        "directly opens or interacts",
        "Game 2 resolved state must not",
        "Lifecycle stage remains presentation-only",
    ]:
        require(token in combined, f"Missing state-separation LI token: {token}", errors)

    require("Game 1 owns player pick state" in rule,
            "LI rule must state that Game 1 owns player pick state.", errors)
    require("Game 2 owns FIFA-final read-only resolved state" in rule,
            "LI rule must state that Game 2 owns read-only resolved state.", errors)
    require("must not come from downstream inference" in rule,
            "LI rule must block downstream-inference highlight ownership.", errors)
    require("candidate resolution" in rule,
            "LI rule must block candidate-resolution highlight ownership.", errors)
    require("current lifecycle stage" in rule,
            "LI rule must block lifecycle-stage highlight ownership.", errors)
    require("Game 2 resolved bracket truth" in rule,
            "LI rule must block Game 2 truth from driving Game 1 highlight.", errors)

    require("python3 tools/verify_wc2026_game1_game2_state_separation_no_r16_preselect_highlight.py" in makefile,
            "Makefile verify must include the Game 1 / Game 2 state-separation verifier.", errors)

    if errors:
        print("WC2026 Game 1 / Game 2 state-separation LI verification failed: " + "; ".join(errors))
        return 1

    print("OK: WC2026 Game 1/Game 2 state separation blocks R16+ preselect highlight except direct interaction.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
