#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read(rel):
    path = ROOT / rel
    if not path.exists():
        raise AssertionError(f"Missing required file: {rel}")
    return path.read_text(encoding="utf-8", errors="ignore")

def require(condition, message, errors):
    if not condition:
        errors.append(message)

def main():
    errors = []

    store = read("site/js/services/SupabaseBracketStore.js")
    repo = read("site/js/services/BracketRepository.js")
    local_store = read("site/js/services/LocalStorageBracketStore.js")
    app = read("site/js/app.js")
    view = read("site/js/mvc/view.js")
    mvc_controller = read("site/js/mvc/controller.js")
    r32_controller = read("site/js/controllers/Game1R32PickController.js")

    require("class SupabaseBracketStore extends BracketStorageAdapter" in store, "SupabaseBracketStore must implement the BracketStorageAdapter seam.", errors)
    require("createSupabaseBracketStore" in store, "SupabaseBracketStore factory must be exported.", errors)
    require(("config.supabaseUrl" in store and "config.supabasePublishableKey" in store) or "requireSharedSupabaseClient(this.config)" in store, "SupabaseBracketStore must use the canonical shared Supabase config/client boundary.", errors)
    require("supabase.auth.getUser()" in store, "SupabaseBracketStore must require the authenticated Supabase user.", errors)
    require("throw new Error(\"SupabaseBracketStore requires a signed-in Supabase user.\")" in store, "SupabaseBracketStore must fail closed when signed out.", errors)
    require('const TABLE_NAME = "user_brackets"' in store and ".from(TABLE_NAME)" in store, "SupabaseBracketStore must be the only user_brackets table access point.", errors)
    require("bracket_json" in store, "SupabaseBracketStore must persist canonical BracketDocument JSON in bracket_json.", errors)
    require(".upsert(" in store and 'onConflict: "user_id,tournament_id,game_id"' in store, "SupabaseBracketStore must upsert one row per user/tournament/game.", errors)
    require(".eq(\"user_id\", user.id)" in store and ".eq(\"tournament_id\", tournamentId)" in store and ".eq(\"game_id\", gameId)" in store, "SupabaseBracketStore must load only the signed-in user/tournament/game row.", errors)

    required_keys = [
        "schemaVersion",
        "userId",
        "tournamentId",
        "gameId",
        "status",
        "lifecycleState",
        "phaseLocks",
        "picksBySlot",
        "createdAt",
        "updatedAt",
        "submittedAt",
        "lockedAt",
        "visibility",
    ]
    for key in required_keys:
        require(f'"{key}"' in store, f"SupabaseBracketStore must preserve BracketDocument field {key}.", errors)

    require("localStorage" not in store, "SupabaseBracketStore must not read or migrate localStorage.", errors)
    require("LocalStorageBracketStore" not in store, "SupabaseBracketStore must not cross-read or dual-write the local store.", errors)
    require("email" not in store.lower(), "SupabaseBracketStore must not persist or expose raw auth email.", errors)

    require("bracketStore = new LocalStorageBracketStore()" in repo, "Default static repository must remain local-only.", errors)
    require("function createSupabaseBracketRepository" in repo, "BracketRepository must expose an explicit Supabase repository factory.", errors)
    require("bracketStore: new SupabaseBracketStore(options)" in repo, "Remote persistence must be selected only through the store seam.", errors)
    require("localStorage" in local_store, "Local anonymous play must remain backed by LocalStorageBracketStore.", errors)

    forbidden_runtime_files = {
        "site/js/app.js": app,
        "site/js/mvc/view.js": view,
        "site/js/mvc/controller.js": mvc_controller,
        "site/js/controllers/Game1R32PickController.js": r32_controller,
    }
    for rel, text in forbidden_runtime_files.items():
        require(".from(\"user_brackets\")" not in text and ".from('user_brackets')" not in text, f"{rel} must not make scattered Supabase bracket calls.", errors)
        require("bracket_json" not in text, f"{rel} must not know the Supabase bracket_json column.", errors)

    require("createSupabaseBracketRepository" not in app, "Gameplay UI startup must not switch to remote persistence automatically.", errors)
    require("SupabaseBracketStore" not in view and "SupabaseBracketStore" not in mvc_controller, "View/Controller must not own Supabase bracket persistence.", errors)

    if errors:
        print("SupabaseBracketStore seam verification failed: " + "; ".join(errors))
        return 1

    print("OK: SupabaseBracketStore is behind the BracketStore seam without changing gameplay UI or local anonymous persistence.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
