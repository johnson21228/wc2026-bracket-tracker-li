#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8", errors="ignore")

def require(condition, message, errors):
    if not condition:
        errors.append(message)

def main():
    errors = []

    view = read("site/js/mvc/view.js")
    controller = read("site/js/mvc/controller.js")
    board_css = read("site/css/board.css")

    require("shouldSuppressPickFillForSlot" in view,
            "Existing Group Stage visual suppression gate must remain present.", errors)
    require("function shouldSuppressPickInteractionForSlot(slot)" in view,
            "View must expose the Group Stage interaction suppression function.", errors)
    require("&& !slot?.pickable" in view,
            "Presentation suppression must exempt pickable R16+ slots fed by official R32 teams.", errors)

    require("function slotAllowedForActiveGame(slot)" in controller,
            "Controller slot gate must remain present.", errors)
    require("if (slotIsR32(slot)) return false;" in controller,
            "Controller must make R32 occupants read-only for players.", errors)
    require("Round of 32 occupants are set by Admin_/official. Pick winners in the next round." in controller,
            "Controller must explain that players pick winners after official R32 occupants.", errors)

    require("return slotIsR32(slot);" not in controller,
            "Controller must not preserve stale Group Stage allow-only-R32 gating.", errors)
    require("Later-round picks open when Knockout Stage presentation is active." not in controller,
            "Controller must not preserve stale Group Stage R16+ blocking copy.", errors)

    require(".pick-slot-button.is-pick-interaction-suppressed" in board_css
            and ".final-four-pick-row.is-pick-interaction-suppressed" in board_css
            and "cursor: default !important" in board_css
            and "pointer-events: none" in board_css,
            "Suppressed non-pickable presentation cells must still override cursor and pointer events.", errors)

    if errors:
        print("Group Stage R16+ interaction gate compatibility verification failed: " + "; ".join(errors))
        return 1

    print("OK: lifecycle stage is presentation-only; official R32 occupants are read-only while pickable R16+ winner slots remain interactive.")

if __name__ == "__main__":
    raise SystemExit(main())
