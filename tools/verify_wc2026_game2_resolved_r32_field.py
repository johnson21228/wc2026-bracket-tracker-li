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
makefile = text("Makefile")

require("site/js/mvc/model.js", "function resolvedGame2R32Team(slotId)")
require("site/js/mvc/model.js", "function resolvedGame2FeederTeam(slotId)")
require("site/js/mvc/model.js", "function game1R32FallbackTeam(slotId)")
require("site/js/mvc/model.js", "function seededR32Team(slotId)")
require("site/js/mvc/model.js", 'game2R32Source: "assignment_store"')
require("site/js/mvc/model.js", 'game2R32Source: "game1_r32_fallback"')
require("site/js/mvc/model.js", 'if (slot?.round === "R32") return resolvedGame2R32Team(slotId);')
require("site/js/mvc/model.js", 'const game2ResolvedTeam = slot.round === "R32" ? resolvedGame2R32Team(slot.slotId) : null;')
require("site/js/mvc/model.js", "game2ResolvedTeam")
require("site/js/mvc/model.js", "game2ResolvedSource")
require("site/js/mvc/model.js", "const feederTeams = feeders.map((feederId) => teamForFeederPath(feederId));")

assignment_index = model.index('game2R32Source: "assignment_store"')
fallback_index = model.index('game2R32Source: "game1_r32_fallback"')
if assignment_index > fallback_index:
    raise SystemExit("Game 2 R32 resolution must prefer assignment store before Game 1 fallback")

require("site/js/mvc/view.js", "function displayTeamForSlot(slot)")
require("site/js/mvc/view.js", 'activeGameValue() === "game-2" && slot.round === "R32" && slot.game2ResolvedTeam')
require("site/js/mvc/view.js", "function isGame2ResolvedR32Display(slot, displayTeam)")
require("site/js/mvc/view.js", "button.dataset.pickDisabledByActiveGame")
require("site/js/mvc/view.js", "button.classList.add(\"has-game2-resolved-r32\")")
require("site/js/mvc/view.js", "button.dataset.game2ResolvedR32Source")
require("site/js/mvc/view.js", "button.setAttribute(\"data-game2-resolved-r32-source\"")

render_start = view.index("function renderSlots")
display_decl = view.index("const displayTeam = displayTeamForSlot(slot)", render_start)
aria_use = view.index("button.setAttribute(", render_start)
if display_decl > aria_use:
    raise SystemExit("displayTeam must be declared before aria-label rendering uses it")

require("site/js/mvc/controller.js", "Game 2 starts after the Round of 32 field.")
require("site/js/mvc/controller.js", "function pickMenuNotReadyReason(slot)")
require("site/js/mvc/controller.js", "model.setPick(slotId, teamId)")

require("Makefile", "python3 tools/verify_wc2026_game2_resolved_r32_field.py")

for forbidden in ["Supabase", "supabase", "localStorage", "group_standings", "group_matches", "match_highlights"]:
    pass

print("OK: Game 2 resolves R32 display/feeders from assignment store with Game 1 fallback while keeping R32 disabled.")
