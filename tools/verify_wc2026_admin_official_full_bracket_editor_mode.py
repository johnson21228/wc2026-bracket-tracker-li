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
# - There is one canonical persisted game: game1.
# - Admin_ physical Supabase row is accepted as Admin_/official authority
#   during reset/migration.
# - Runtime projects Admin_ as semantic Admin_/official.
# - Admin_/official editor mode may author R32 occupants.
# - Normal players cannot author R32 occupants.
# - Later knockout picks remain normal player-authored winner picks.
# - Unknown persisted team IDs are cleared before rendering.
# - Do not require a separate physical "Admin_/official" user_id row.

require('const DEFAULT_GAME_ID = "game1";' in store, "store must define canonical game1")
require("function canonicalGameId()" in store, "store must canonicalize persisted game id")
require(".eq(\"game_id\", gameId)" in store, "store loaders must query canonical game id")

require("ADMIN_OFFICIAL_SUPABASE_USER_ID" in store, "store must define physical Admin_ Supabase authority id")
require(".eq(\"user_id\", ADMIN_OFFICIAL_SUPABASE_USER_ID)" in store, "store must load Admin_ physical row as authority")
require("loaded Admin_ player row as Admin_/official R32 authority" in store, "store must recognize Admin_ row as Admin_/official authority")
require("userId: ADMIN_OFFICIAL_USER_ID" in store, "store must project Admin_ physical row as semantic Admin_/official")
require("persistedByUserId" in store, "store must preserve physical persisted user id")
require(".eq(\"user_id\", ADMIN_OFFICIAL_USER_ID)" not in store, "store must not query fake semantic Admin_/official user id")

require("adminOfficialEditor" in app, "app must wire Admin_/official editor flag")
require("adminOfficialEditorFromUrl" in model, "model must derive Admin_/official editor flag from URL/app")
require("adminOfficialEditorActive" in model, "model must expose Admin_/official editor active state")
require("adminOfficialR32EditorActive" in model, "model must expose Admin_/official R32 editor active state")

require("function selectedTeam(slotId)" in model, "model must define selectedTeam renderer")
require("officialTeam(slotId)" in model, "selectedTeam must consult Admin_/official authority")
require("persistedPlayerTeam(slotId)" in model, "selectedTeam must use canonical persisted player team fallback only where allowed")
require("clearUnknownTeamPicks" in model, "model must clear undefined canonical team IDs")
require("knownTeamForPersistedPick" in model, "model must only render known canonical team IDs")
require("WC2026 LI FAIL" in model, "model must loudly report canonical team ID violations")

require("slotIsR32(slot)" in controller, "controller must recognize R32")
require("Round of 32 occupants are set by Admin_/official" in controller, "normal players must be blocked from R32 authoring")
require("if (adminOfficialEditorActive()) return \"\";" in controller, "Admin_/official editor must not be blocked from R32 authoring")

require("saveOfficialR32BracketAuthority" in store, "store must keep Admin_/official save boundary")
require("await this.requireSignedInUser()" in store, "save boundary must require signed-in Supabase session")
require("adminUser.id !== ADMIN_OFFICIAL_SUPABASE_USER_ID" in store, "save boundary must require the physical Admin_ Supabase user")
require(".update(rowPayload)" in store, "Admin_/official save must update the existing physical Admin_ row when present")
require(".insert(rowPayload)" in store, "Admin_/official save may insert only the physical Admin_ row when missing")
require('bracket_kind: "player"' in store, "Admin_/official durable save must keep the physical row bracket_kind as player")
require('bracket_kind: "official"' not in store, "Admin_/official durable save must not write a physical official row")
require('bracketKind: "official"' in store, "projected Admin_/official document must retain semantic official bracket kind")
require('persistedBracketKind: "player"' in store, "projected Admin_/official document must remember physical player row kind")

if errors:
    print("WC2026 Admin_/official full bracket editor mode verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: Admin_/official full editor verifier aligned with single-game Admin_ authority, semantic projection, player R32 lockout, and canonical team IDs.")
