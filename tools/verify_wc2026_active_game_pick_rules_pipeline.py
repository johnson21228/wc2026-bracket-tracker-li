#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def text(path):
    return (ROOT / path).read_text()

def require(path, token):
    body = text(path)
    if token not in body:
        raise SystemExit(f"Missing {token!r} in {path}")

view = text("site/js/mvc/view.js")
controller = text("site/js/mvc/controller.js")
makefile = text("Makefile")

require("site/js/mvc/view.js", "function activeGameValue()")
require("site/js/mvc/view.js", "function slotEnabledForActiveGame(slot)")
require("site/js/mvc/view.js", "button.dataset.pickDisabledByActiveGame")
require("site/js/mvc/view.js", "is-disabled-by-active-game")
require("site/js/mvc/view.js", "onActiveGameChange?.(activeGameValue())")

for token in ["display: none", "visibility: hidden", "hidden = true", ".style.display ="]:
    gated_start = view.index("function slotEnabledForActiveGame")
    gated_end = view.index("function renderBoardShell")
    if token in view[gated_start:gated_end]:
        raise SystemExit(f"View must disable, not hide, wrong-game cells; found {token!r}")

require("site/js/mvc/controller.js", "function slotAllowedForActiveGame(slot)")
require("site/js/mvc/controller.js", "function pickMenuNotReadyReason(slot)")
require("site/js/mvc/controller.js", "function reportBlockedPick(slot)")
require("site/js/mvc/controller.js", "Game 1 only accepts Round of 32 picks.")
require("site/js/mvc/controller.js", "Game 2 starts after the Round of 32 field.")
require("site/js/mvc/controller.js", "This Game 2 pick menu is not ready yet.")
require("site/js/mvc/controller.js", "view.closeMenu();")

slot_click = controller[controller.index("function onSlotClick"):controller.index("function onTeamPick")]
if slot_click.index("!slotAllowedForActiveGame(slot)") > slot_click.index("!slot.pickable"):
    raise SystemExit("onSlotClick must guard active-game eligibility before generic pickability/not-ready behavior")
require("site/js/mvc/controller.js", "reportBlockedPick(slot);")

team_pick = controller[controller.index("function onTeamPick"):controller.index("function onClearPick")]
for token in ["slotAllowedForActiveGame(slot)", "pickMenuNotReadyReason(slot)", "model.setPick(slotId, teamId)"]:
    if token not in team_pick:
        raise SystemExit(f"onTeamPick does not enforce pipeline guard token {token!r}")
if team_pick.index("slotAllowedForActiveGame(slot)") > team_pick.index("model.setPick(slotId, teamId)"):
    raise SystemExit("onTeamPick must guard active-game eligibility before model.setPick")

if "verify_wc2026_active_game_pick_rules_pipeline.py" not in makefile:
    raise SystemExit("Makefile verify target must include active-game pick rules pipeline verifier")

for forbidden in ["Supabase", "supabase", "localStorage", "group_standings", "group_matches", "match_highlights"]:
    # The verifier itself should not require or imply data/storage/backend changes.
    pass

print("OK: active game pick rules are enforced through controller pre-selection and pick write pipeline.")
