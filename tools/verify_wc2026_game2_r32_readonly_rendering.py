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
require("site/js/mvc/view.js", "const readOnlyGame2R32Display = game2ResolvedR32Display;")
require("site/js/mvc/view.js", "const disabledByPickability = !slot.pickable && !readOnlyGame2R32Display;")
require("site/js/mvc/view.js", "const disabledByActiveGame = !enabledForActiveGame && !readOnlyGame2R32Display;")
require("site/js/mvc/view.js", "button.disabled = disabledByPickability || disabledByActiveGame;")
require("site/js/mvc/view.js", 'button.classList.add("has-game2-readonly-r32")')
require("site/js/mvc/view.js", 'button.dataset.game2ReadonlyR32 = "true"')
require("site/js/mvc/view.js", 'button.setAttribute("data-game2-readonly-r32", "true")')
require("site/js/mvc/view.js", 'button.setAttribute("data-game2-resolved-r32-source", slot.game2ResolvedSource || "unknown")')

if "button.disabled = !slot.pickable || !enabledForActiveGame" in view:
    raise SystemExit("Game 2 R32 read-only cells must not inherit the old unconditional disabled assignment")

resolved_start = view.index("if (game2ResolvedR32Display)")
resolved_end = view.index("if (!displayTeam) button.classList.add", resolved_start)
resolved_block = view[resolved_start:resolved_end]
if "has-game2-readonly-r32" not in resolved_block:
    raise SystemExit("Resolved Game 2 R32 block must add the read-only rendering class")
if "is-unpicked" in resolved_block:
    raise SystemExit("Resolved Game 2 R32 display block must not mark populated cells as unpicked")

disabled_start = view.index("const readOnlyGame2R32Display = game2ResolvedR32Display;")
disabled_end = view.index("button.dataset.pickDisabledByActiveGame", disabled_start)
disabled_block = view[disabled_start:disabled_end]
if "!readOnlyGame2R32Display" not in disabled_block:
    raise SystemExit("Disabled-state assignment must explicitly exempt read-only Game 2 R32 cells")

require("site/css/board.css", ".pick-slot-button.has-game2-readonly-r32")
require("site/css/board.css", "cursor: default")
require("site/css/board.css", "opacity: 1")
require("site/css/board.css", "filter: none")
if ".pick-slot-button.has-game2-readonly-r32:disabled" in css:
    raise SystemExit("Read-only Game 2 R32 styling must not depend on the disabled pseudo-class")

require("site/js/mvc/controller.js", "Game 2 starts after the Round of 32 field.")
require("site/js/mvc/controller.js", "function pickMenuNotReadyReason(slot)")
require("site/js/mvc/controller.js", "!slotAllowedForActiveGame(slot)")
require("site/js/mvc/controller.js", "model.setPick(slotId, teamId)")

slot_click = controller[controller.index("function onSlotClick"):controller.index("function onTeamPick")]
if "!slotAllowedForActiveGame(slot)" not in slot_click:
    raise SystemExit("Game 2 R32 menu opening must remain blocked by the active-game guard")
if "reportBlockedPick(slot)" not in slot_click:
    raise SystemExit("Blocked Game 2 R32 clicks must report the blocked/read-only state instead of opening a menu")

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

for forbidden in [
    "site/js/config/supabase.public.js",
    "site/js/services/SupabaseAuthService.js",
    "site/data/current/group_matches.json",
    "site/data/current/group_standings.json",
    "site/data/current/match_highlights.json",
]:
    if not (ROOT / forbidden).exists():
        continue

print("OK: Game 2 R32 resolved cells render as read-only populated entries without the HTML disabled state while controller guards keep them non-pickable.")
