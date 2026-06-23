#!/usr/bin/env python3
from pathlib import Path


def require(condition, message, errors):
    if not condition:
        errors.append(message)


def read(path):
    return Path(path).read_text()


def main():
    errors = []

    css = read("site/css/board.css")
    capture = read("captures/CAPTURE_BACK_PICK_SLOT_BUTTON_LABEL_CENTERING.md")
    doc = read("docs/features/pick_slot_button_label_centering.md")
    rule = read("li/world_cup/pick_slot_button_label_centering_rule.md")
    card = read("cards/282_pick_slot_button_label_centering_card.md")
    makefile = read("Makefile")

    combined = "\n".join([capture, doc, rule, card])

    require("Pick Slot Button Label Centering" in combined,
            "LI capture/docs/card must name pick-slot button label centering.", errors)
    require("presentation-only" in rule,
            "LI rule must state this is presentation-only.", errors)
    require("must not" in rule and "preselect" in rule and "Game 1 / Game 2" in rule,
            "LI rule must preserve state-separation and preselect constraints.", errors)

    require("Card 282: pick-slot button labels must remain visually centered." in css,
            "Runtime CSS must include the Card 282 centering block.", errors)
    require(".pick-slot-button .pick-slot-label" in css,
            "Runtime CSS must target pick-slot labels.", errors)
    require(".pick-slot-button .pick-slot-value" in css,
            "Runtime CSS must target pick-slot values.", errors)
    require(".pick-slot-button .unpicked-cell-label" in css,
            "Runtime CSS must target unpicked cell labels.", errors)
    require("text-align: center;" in css,
            "Runtime CSS must center text alignment.", errors)
    require("align-items: center;" in css and "justify-content: center;" in css,
            "Runtime CSS must flex-center pick-slot values.", errors)
    require(".pick-slot-button.is-pickable[data-round=\"R32\"]:hover" in css,
            "R16+ generic preselect hover suppression must remain intact.", errors)
    require(".pick-slot-button.is-pickable:hover" not in css,
            "Generic pickable hover must not return for R16+ cells.", errors)

    require("python3 tools/verify_wc2026_pick_slot_button_label_centering.py" in makefile,
            "Makefile verify must include pick-slot label centering verifier.", errors)

    if errors:
        print("WC2026 pick-slot button label centering verification failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("OK: WC2026 pick-slot button labels and values are centered without changing pick/preselect state.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
