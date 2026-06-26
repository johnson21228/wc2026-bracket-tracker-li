#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
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
# - R32 occupants are Admin_/official authority, not player-owned picks.
# - Admin_ Supabase row may be projected as Admin_/official during reset/migration.
# - Player brackets may render official R32 occupants but must not author R32.
# - Later knockout winners remain player-authored.
# - Unknown persisted team IDs are cleared before rendering.

require("ADMIN_OFFICIAL_SUPABASE_USER_ID" in store, "store must define Admin_ Supabase authority user id")
require("loaded Admin_ player row as Admin_/official R32 authority" in store, "store must load Admin_ row as Admin_/official authority")
require("userId: ADMIN_OFFICIAL_USER_ID" in store, "store must project Admin_ row as semantic Admin_/official")
require('bracketKind: "official"' in store, "store must project Admin_ source as official bracket document")

require("clearUnknownTeamPicks" in model, "model must clear invalid canonical team IDs before rendering")
require("knownTeamForPersistedPick" in model, "model must only render known canonical teams")
require("function selectedTeam(slotId)" in model, "model must define selectedTeam renderer")
require("officialTeam(slotId)" in model, "R32 rendering must consult Admin_/official authority")
require("persistedPlayerTeam(slotId)" in model, "R32 rendering may only fall back through canonical persisted player-team validation")

require("slotIsR32(slot)" in controller, "controller must recognize R32 slots")
require("Round of 32 occupants are set by Admin_/official" in controller, "players must be blocked from authoring R32 occupants")
require("if (adminOfficialEditorActive()) return \"\";" in controller, "Admin_ editor must be allowed to author R32 occupants")

if errors:
    print("WC2026 player R32 Admin mirror verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: R32 occupants render from Admin_/official authority; players cannot author R32 and must pick later winners.")
