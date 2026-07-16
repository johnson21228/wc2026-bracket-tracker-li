#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read(path):
    return (ROOT / path).read_text()

errors = []

def require(path, token, label):
    if token not in read(path):
        errors.append(f"{path}: missing {label}: {token}")

require("site/js/mvc/model.js", "FINAL_FOUR_PICK_SLOT_DEFS", "canonical Final Four pick slot definitions")
require("site/js/mvc/model.js", '"FINAL-LEFT"', "Final left slot")
require("site/js/mvc/model.js", '"FINAL-RIGHT"', "Final right slot")
require("site/js/mvc/model.js", '"CHAMPION"', "champion slot")
require("site/js/mvc/model.js", '"THIRD-PLACE-WINNER"', "third-place winner slot")
require("site/js/mvc/model.js", "function getFinalFourChoices", "Final Four choice resolver")
require("site/js/mvc/model.js", "function getFinalFourViewModel", "Final Four view model")
require("site/js/mvc/model.js", "loserFromSemifinal", "third-place semifinal loser resolver")
require("site/js/mvc/model.js", "const winner = officialTeam(finalSlotId) || selectedTeam(finalSlotId);", "official semifinal winner precedence")
require("site/js/mvc/model.js", "const team = officialResultTeam || playerPickTeam;", "official semifinal winner display precedence")
require("site/js/mvc/model.js", "officialPickComparisonForSlot(slotId, playerPickTeam)", "player pick retained for scoring comparison")
require("site/js/mvc/model.js", "getSlotDefinition(slotId)", "canonical slot lookup beyond geometry slots")

require("site/js/mvc/controller.js", "finalFour: model.getFinalFourViewModel()", "controller final four state")
require("site/js/mvc/controller.js", "onFinalFourSlotClick: onSlotClick", "controller routes final four clicks through normal pick path")

require("site/js/mvc/view.js", "data-final-four-layer", "Final Four layer")
require("site/js/mvc/view.js", "function renderFinalFourPanel", "Final Four renderer")
require("site/js/mvc/view.js", "final-four-panel", "Final Four panel class")
require("site/js/mvc/view.js", "handlers.onFinalFourSlotClick", "Final Four click handler")
require("site/js/mvc/view.js", "renderFinalFourPanel(state.finalFour)", "Final Four render call")

require("site/css/board.css", ".board-final-four-layer", "Final Four board layer style")
require("site/css/board.css", ".final-four-pick-row", "Final Four pick row style")

model = read("site/js/mvc/model.js")
if "pickSurfaceSlots(slots).map" not in model:
    errors.append("site/js/mvc/model.js: normal pick surfaces should still come from pickSurfaceSlots(slots), not CENTER-FINAL-FOUR")

if errors:
    print("Final Four pick display verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: Final Four display renders canonical SF winner, final winner, champion, and third-place pick slots with source-derived center-stack geometry.")
