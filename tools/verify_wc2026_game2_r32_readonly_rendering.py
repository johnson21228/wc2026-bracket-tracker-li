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
model = text("site/js/mvc/model.js")
css = text("site/css/board.css")
makefile = text("Makefile")

require("site/js/mvc/view.js", "function displayTeamForSlot(slot)")
require("site/js/mvc/view.js", "const displayTeam = displayTeamForSlot(slot);")
require("site/js/mvc/view.js", "function isGame2ResolvedR32Display(slot, displayTeam)")
require("site/js/mvc/view.js", 'activeGameValue() === "game-2" && slot.round === "R32" && Boolean(displayTeam) && Boolean(slot.game2ResolvedTeam)')
require("site/js/mvc/view.js", 'button.classList.add("has-game2-readonly-r32")')
require("site/js/mvc/view.js", 'button.dataset.game2ReadonlyR32 = "true"')
require("site/js/mvc/view.js", 'button.setAttribute("data-game2-readonly-r32", "true")')
require("site/js/mvc/view.js", 'button.setAttribute("data-game2-resolved-r32-source", slot.game2ResolvedSource || "unknown")')
require("site/js/mvc/view.js", "button.disabled = !slot.pickable || !enabledForActiveGame")

resolved_block = view[view.index("if (game2ResolvedR32Display)"):view.index("if (!displayTeam) button.classList.add", view.index("if (game2ResolvedR32Display)"))]
if "has-game2-readonly-r32" not in resolved_block:
    raise SystemExit("Resolved Game 2 R32 block must add the read-only rendering class")
if "is-unpicked" in resolved_block:
    raise SystemExit("Resolved Game 2 R32 display block must not mark populated cells as unpicked")

require("site/css/board.css", ".pick-slot-button.has-game2-readonly-r32:disabled")
require("site/css/board.css", "opacity: 1")
require("site/css/board.css", "cursor: default")

css_block = css[css.index(".pick-slot-button.has-game2-readonly-r32:disabled"):]
if "opacity: 1" not in css_block:
    raise SystemExit("Read-only Game 2 R32 cells must override disabled opacity")

require("site/js/mvc/controller.js", "Game 2 starts after the Round of 32 field.")
require("site/js/mvc/controller.js", "function pickMenuNotReadyReason(slot)")
require("site/js/mvc/controller.js", "!slotAllowedForActiveGame(slot)")
require("site/js/mvc/controller.js", "model.setPick(slotId, teamId)")

team_pick = controller[controller.index("function onTeamPick"):controller.index("function onClearPick")]
if team_pick.index("!slotAllowedForActiveGame(slot)") > team_pick.index("model.setPick(slotId, teamId)"):
    raise SystemExit("Game 2 R32 writes must remain blocked before model.setPick")

knockout = model[model.index("function getKnockoutChoices"):model.index("function getChoices")]
if "teamForFeederPath" not in knockout:
    raise SystemExit("Later Game 2 menus must derive candidates from resolved feeder teams")
if "getR32Choices" in knockout:
    raise SystemExit("Game 2 knockout choices must not fall back to Game 1 R32 pick menus")

if "python3 tools/verify_wc2026_game2_r32_readonly_rendering.py" not in makefile:
    raise SystemExit("Makefile verify target must include Game 2 R32 read-only rendering verifier")

for forbidden in ["site/js/config/supabase.public.js", "site/js/services/SupabaseAuthService.js", "site/data/current/group_matches.json", "site/data/current/group_standings.json", "site/data/current/match_highlights.json"]:
    if not (ROOT / forbidden).exists():
        continue

print("OK: Game 2 R32 resolved cells render as read-only populated entries without disabled-looking opacity while remaining non-pickable.")
