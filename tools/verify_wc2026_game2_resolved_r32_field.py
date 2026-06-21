#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def text(path):
    return (ROOT / path).read_text()

def require(path, token):
    body = text(path)
    if token not in body:
        raise SystemExit(f"Missing {token!r} in {path}")

model = text("site/js/mvc/model.js")
view = text("site/js/mvc/view.js")
controller = text("site/js/mvc/controller.js")
makefile = text("Makefile")

require("site/js/mvc/model.js", "function resolvedGame2R32Team(slotId)")
require("site/js/mvc/model.js", "function game1R32FallbackTeam(slotId)")
require("site/js/mvc/model.js", "function resolvedGame2FeederTeam(slotId)")
require("site/js/mvc/model.js", "function fifaFinalR32Team(slotId)")
require("site/js/mvc/model.js", 'game2R32Source: "fifa_final_assignment"')
require("site/js/mvc/model.js", 'game2R32Source: "game1_r32_fallback"')
require("site/js/mvc/model.js", 'const game2ResolvedTeam = slot.round === "R32" ? resolvedGame2R32Team(slot.slotId) : null;')
require("site/js/mvc/model.js", "game2ResolvedTeam,")
require("site/js/mvc/model.js", "game2ResolvedSource: game2ResolvedTeam?.game2R32Source || null")
require("site/js/mvc/model.js", "const feederTeams = feeders.map((feederId) => teamForFeederPath(feederId));")

helper = model[model.index("function resolvedGame2R32Team"):model.index("function resolvedGame2FeederTeam")]
if helper.index("const fifaFinal = fifaFinalR32Team(slotId)") > helper.index("const fallback = game1R32FallbackTeam(slotId)"):
    raise SystemExit("Game 2 R32 resolution must prefer populated FIFA-final teams before Game 1 fallback")

feeder = model[model.index("function resolvedGame2FeederTeam"):model.index("function teamForFeederPath")]
if 'slot?.round === "R32"' not in feeder or "resolvedGame2R32Team(slotId)" not in feeder:
    raise SystemExit("Game 2 feeder seam must resolve R32 through the resolved Game 2 R32 field")

require("site/js/mvc/view.js", "function displayTeamForSlot(slot)")
require("site/js/mvc/view.js", 'activeGameValue() === "game-2" && slot.round === "R32" && slot.game2ResolvedTeam')
require("site/js/mvc/view.js", "const displayTeam = displayTeamForSlot(slot);")
require("site/js/mvc/view.js", "has-game2-resolved-r32")
require("site/js/mvc/view.js", "data-game2-resolved-r32-source")
require("site/js/mvc/view.js", "slotEnabledForActiveGame(slot)")
require("site/js/mvc/view.js", "const readOnlyGame2R32Display = game2ResolvedR32Display;")
require("site/js/mvc/view.js", "const disabledByPickability = !slot.pickable && !readOnlyGame2R32Display;")
require("site/js/mvc/view.js", "const disabledByActiveGame = !enabledForActiveGame && !readOnlyGame2R32Display;")
require("site/js/mvc/view.js", "button.disabled = disabledByPickability || disabledByActiveGame;")

require("site/js/mvc/controller.js", "Game 2 starts after the Round of 32 field.")
require("site/js/mvc/controller.js", "!slotAllowedForActiveGame(slot)")
require("site/js/mvc/controller.js", "model.setPick(slotId, teamId)")
team_pick = controller[controller.index("function onTeamPick"):controller.index("function onClearPick")]
if team_pick.index("!slotAllowedForActiveGame(slot)") > team_pick.index("model.setPick(slotId, teamId)"):
    raise SystemExit("Game 2 R32 writes must remain blocked before model.setPick")

if "verify_wc2026_game2_resolved_r32_field.py" not in makefile:
    raise SystemExit("Makefile verify target must include Game 2 resolved R32 field verifier")

print("OK: Game 2 resolves R32 display/feeders from FIFA-final source with Game 1 fallback while keeping R32 disabled.")
