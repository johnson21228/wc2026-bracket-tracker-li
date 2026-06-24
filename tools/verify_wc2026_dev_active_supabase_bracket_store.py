#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8", errors="ignore")

def require(condition, message, errors):
    if not condition:
        errors.append(message)

def main():
    errors = []
    app = read("site/js/app.js")
    account = read("site/js/identity/AccountSaveActionSurface.js")
    model = read("site/js/mvc/model.js")
    controller = read("site/js/mvc/controller.js")
    view = read("site/js/mvc/view.js")
    store = read("site/js/services/SupabaseBracketStore.js")
    standings = read("site/js/standings/SupabasePlayerStandingsStore.js")

    require("devSupabaseBracketStore" not in app, "devSupabaseBracketStore query flag must be removed from production app wiring.", errors)
    require("devSupabaseBracketStoreOptions" not in app, "Dev-only Supabase store selector must be removed.", errors)
    require("shouldUseDevSupabaseBracketStore" not in app, "Dev-only store flag helper must be removed.", errors)
    require("createBracketModel()" in app, "Board model should start with normal local anonymous persistence.", errors)
    require("createAccountSaveActionSurface({" in app, "Joined-player save surface must be wired.", errors)
    require("remoteActive" not in app, "App must not bypass joined-player Supabase persistence through remoteActive.", errors)

    require("remoteActive" not in account, "Joined-player save surface must not bypass load/save behind remoteActive.", errors)
    require("new SupabaseBracketStore()" in account, "Joined-player save surface must use SupabaseBracketStore in production.", errors)
    require("bracketStore.loadUserBracket(playerUserId)" in account, "Joined-player save surface must load existing joined picks from Supabase.", errors)
    require("bracketStore.saveUserBracket(bracketDocument)" in account, "Joined-player save surface must save joined picks to Supabase.", errors)
    require("wc2026:picks-changed" in account and "scheduleAutosave" in account, "Joined picks must autosave after pick changes.", errors)
    require("Use saved picks" in account and "Keep this board" in account, "Joined-player conflict path must remain available.", errors)

    require("bracketStore = null" in model and 'persistenceMode = "local"' in model, "Model must preserve anonymous local browser play by default.", errors)
    require("saveToStorage(picks)" in model, "Local anonymous persistence must remain available.", errors)

    for rel, text in {
        "site/js/mvc/controller.js": controller,
        "site/js/mvc/view.js": view,
    }.items():
        require("Supabase" not in text and "user_brackets" not in text and "bracket_json" not in text, f"{rel} must not know about Supabase persistence.", errors)

    require("from(USER_BRACKETS_TABLE)" in standings, "Player Standings must read saved bracket rows.", errors)
    require("profileByUserId" in standings and "fetchProfilesByUserId" in standings, "Player Standings must join public profile names to bracket rows.", errors)
    require("teamsByIdFromPicksBySlot" in store, "SupabaseBracketStore must validate saved team picks from BracketDocument records.", errors)

    if errors:
        print("Production joined-player Supabase persistence verification failed: " + "; ".join(errors))
        return 1

    print("OK: joined players save/load picks through Supabase in production while anonymous browser play remains local.")

if __name__ == "__main__":
    raise SystemExit(main())
