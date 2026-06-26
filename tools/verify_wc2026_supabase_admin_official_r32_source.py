#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
store = (ROOT / "site/js/services/SupabaseBracketStore.js").read_text()
model = (ROOT / "site/js/mvc/model.js").read_text()
account = (ROOT / "site/js/identity/AccountSaveActionSurface.js").read_text()

errors = []

def require(condition, message):
    if not condition:
        errors.append(message)

# Current one-game Admin_/official authority model:
# - game1 is canonical.
# - Admin_ Supabase user row is accepted as Admin_/official R32 authority during migration/reset.
# - Runtime projects Admin_ persisted row as Admin_/official.
# - Missing source row fails closed.
# - Unknown persisted team IDs are LI failures and are cleared before rendering.
# - Joined play uses Supabase authority; local draft picks are ignored.

require('const DEFAULT_GAME_ID = "game1";' in store, "store must define single canonical game")
require("function canonicalGameId()" in store, "store must canonicalize game id")
require('.eq("game_id", gameId)' in store, "loaders must query canonical game")

require("ADMIN_OFFICIAL_SUPABASE_USER_ID" in store, "store must define canonical Admin_ Supabase user id")
require('.eq("user_id", ADMIN_OFFICIAL_SUPABASE_USER_ID)' in store, "official loader must load Admin_ Supabase row")
require("loaded Admin_ player row as Admin_/official R32 authority" in store, "loader must log Admin_ row as Admin_/official authority")
require("admin-player-row" in store, "loader must tag Admin_ row authority source")

require("function hasR32Picks(bracket)" in store, "loader must validate R32 picks exist")
require("adminPlayerHasR32Picks" in store, "loader must report Admin_ row R32-pick absence")
require("no Admin_/official R32 source row found" in store, "loader must fail closed when no Admin_ source row exists")

require('userId: ADMIN_OFFICIAL_USER_ID' in store, "loader must project Admin_ row as Admin_/official document")
require('bracketKind: "official"' in store, "loader must project source as official bracket document")
require('authority: "Admin_/official"' in store, "loader must mark projected source as Admin_/official authority")
require("persistedByUserId" in store, "projected official document must preserve physical Supabase user id")

require("failClosedAdminOfficialR32TruthDocument" in model, "model must keep fail-closed document")
require("clearUnknownTeamPicks" in model, "model must clear undefined canonical team IDs before rendering")
require("WC2026 LI FAIL" in model, "model must loudly report canonical team ID violations")
require("knownTeamForPersistedPick" in model, "model must only render known canonical persisted teams")

require("Local draft picks are ignored for joined play" in account, "joined play must ignore local draft picks")
require("Keep this board" not in account, "joined play must not offer Keep this board")
require("Use saved picks" not in account, "joined play must not offer stale Use saved picks choice")

# Guard against regressing to fake semantic user id queries.
require('.eq("user_id", ADMIN_OFFICIAL_USER_ID)' not in store, "must not query fake Admin_/official user_id")

if errors:
    print("WC2026 Supabase Admin_/official R32 source verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: one-game Supabase Admin_/official R32 source uses Admin_ migration authority, strict canonical team IDs, and joined Supabase-only play.")
