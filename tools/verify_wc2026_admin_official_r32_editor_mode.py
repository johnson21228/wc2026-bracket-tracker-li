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
# - Admin_ editor mode is opened by URL/app flag.
# - Admin_ Supabase user row is the physical persisted authority during reset/migration.
# - Runtime projects Admin_ as semantic Admin_/official.
# - Admin_ may author R32 occupants.
# - Normal players may render R32 occupants but may not author them.
# - Saves must use physical signed-in Supabase user identity, not fake Admin_/official user_id.
# - Persisted team IDs must be canonical; invalid IDs are cleared/rejected before rendering.

require("adminOfficialEditor" in app, "app must pass Admin_/official editor flag")
require("adminOfficialEditorFromUrl" in model, "model must derive Admin_/official editor mode from URL/app flag")
require("adminOfficialEditorActive" in model, "model must expose Admin_/official editor active state")
require("adminOfficialR32EditorActive" in model, "model must expose Admin_/official R32 editor active state")

require("if (adminOfficialEditorActive()) return \"\";" in controller, "Admin_ editor must not be blocked from R32 picking")
require("Round of 32 occupants are set by Admin_/official" in controller, "normal players must be blocked from authoring R32")
require("slotIsR32(slot)" in controller, "controller must recognize R32 slots")

require("ADMIN_OFFICIAL_SUPABASE_USER_ID" in store, "store must define physical Admin_ Supabase authority id")
require(".eq(\"user_id\", ADMIN_OFFICIAL_SUPABASE_USER_ID)" in store, "store must load physical Admin_ row as authority")
require("loaded Admin_ player row as Admin_/official R32 authority" in store, "store must recognize Admin_ row as Admin_/official authority")
require("userId: ADMIN_OFFICIAL_USER_ID" in store, "store must project Admin_ row as semantic Admin_/official document")
require("persistedByUserId" in store, "store must preserve physical Supabase user id")
require(".eq(\"user_id\", ADMIN_OFFICIAL_USER_ID)" not in store, "store must not query fake semantic Admin_/official user id")

require("saveOfficialR32BracketAuthority" in store, "store must keep Admin_/official save boundary")
require('bracket_kind: "player"' in store, "Admin_/official R32 save must persist through the physical Admin_ player row")
require('bracket_kind: "official"' not in store, "Admin_/official R32 save must not write a physical official row")
require("const adminUser = await this.requireSignedInUser();" in store, "official save must use signed-in physical Supabase user")
require("bracket_kind: \"official\"" in store or "bracketKind: \"official\"" in store, "projected/saved Admin document must keep official semantic bracket kind")

require("clearUnknownTeamPicks" in model, "model must clear invalid canonical team IDs before rendering")
require("WC2026 LI FAIL" in model, "model must report canonical team ID violations")

if errors:
    print("WC2026 Admin_/official R32 editor mode verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: Admin_/official R32 editor uses Admin_ physical authority, semantic Admin_/official projection, canonical team IDs, and player R32 lockout.")
