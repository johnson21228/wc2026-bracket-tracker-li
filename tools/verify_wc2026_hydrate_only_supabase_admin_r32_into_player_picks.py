#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

app = (ROOT / "site/js/app.js").read_text()
model = (ROOT / "site/js/mvc/model.js").read_text()
controller = (ROOT / "site/js/mvc/controller.js").read_text()
store = (ROOT / "site/js/services/SupabaseBracketStore.js").read_text()

errors = []

def require(condition, message):
    if not condition:
        errors.append(message)

# Superseded verifier name retained for make verify continuity.
#
# Current LI:
# - Do not make player picks own R32 occupants.
# - R32 occupants are Admin_/official authority.
# - Admin_ physical Supabase row may be projected as semantic Admin_/official.
# - Normal players render R32 read-only and pick winners after R32.
# - Legacy hydration helpers may remain only as compatibility boundaries.
# - Unknown persisted team IDs are LI failures and are cleared before rendering.

require("createSupabaseBracketStore" in app, "app must create Supabase bracket store")
require("officialBracketStore" in app, "app must pass official/Admin authority store into model")
require('root.dataset.bracketeeringGame = "game1"' in app, "app must expose canonical single game")

require("ADMIN_OFFICIAL_SUPABASE_USER_ID" in store, "store must define physical Admin_ Supabase authority id")
require(".eq(\"user_id\", ADMIN_OFFICIAL_SUPABASE_USER_ID)" in store, "store must load Admin_ physical row")
require("loaded Admin_ player row as Admin_/official R32 authority" in store, "store must project Admin_ row as Admin_/official authority")
require("userId: ADMIN_OFFICIAL_USER_ID" in store, "store must expose semantic Admin_/official document")
require("admin-player-row" in store, "store must tag Admin_ row authority source")
require(".eq(\"user_id\", ADMIN_OFFICIAL_USER_ID)" not in store, "store must not query fake semantic Admin_/official user id")

require("function selectedTeam(slotId)" in model, "model must define selectedTeam renderer")
require("officialTeam(slotId)" in model, "selectedTeam must consult Admin_/official authority")
require("persistedPlayerTeam(slotId)" in model, "selectedTeam must only use canonical persisted player-team fallback where allowed")
require("clearUnknownTeamPicks" in model, "model must clear undefined canonical team IDs")
require("knownTeamForPersistedPick" in model, "model must only render known canonical teams")
require("WC2026 LI FAIL" in model, "model must loudly report canonical team ID violations")
require("failClosedAdminOfficialR32TruthDocument" in model, "model must fail closed when Admin_/official R32 truth is missing")

require("slotIsR32(slot)" in controller, "controller must recognize R32")
require("Round of 32 occupants are set by Admin_/official" in controller, "normal players must be blocked from R32 authoring")
require("if (adminOfficialEditorActive()) return \"\";" in controller, "Admin_/official editor must be allowed to author R32")

# Compatibility helpers are allowed, but must not reassert R32 as player-owned truth.
if "hydrateOnlySupabaseAdminR32IntoPlayerPicks" in model:
    require("officialTeam(slotId)" in model, "legacy hydration compatibility must still route display through official authority")

if errors:
    print("WC2026 Supabase-only Admin R32 hydration verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: Supabase Admin R32 hydration verifier aligned with Admin_/official authority, player R32 lockout, and canonical team IDs.")
