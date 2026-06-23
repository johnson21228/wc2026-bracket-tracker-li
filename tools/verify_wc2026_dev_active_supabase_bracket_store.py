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
    model = read("site/js/mvc/model.js")
    controller = read("site/js/mvc/controller.js")
    view = read("site/js/mvc/view.js")
    store = read("site/js/services/SupabaseBracketStore.js")
    smoke = read("site/js/dev/SupabaseBracketStoreSmokeTest.js")

    require('"devSupabaseBracketStore"' in app, "App must expose a dev-only Supabase bracket store query flag.", errors)
    require("new SupabaseBracketStore()" in app, "App must instantiate SupabaseBracketStore only from the dev store selector.", errors)
    require('persistenceMode: "supabase"' in app, "App must pass explicit supabase persistence mode to the model.", errors)
    require("createBracketModel(await devSupabaseBracketStoreOptions(authService))" in app, "Model creation must receive dev-selected store options.", errors)

    require("bracketStore = null" in model and 'persistenceMode = "local"' in model, "Model must default to local persistence.", errors)
    require('remotePersistenceActive = persistenceMode === "supabase" && bracketStore' in model, "Model must gate remote persistence behind explicit supabase mode and a store.", errors)
    require("bracketStore.loadUserBracket(userId)" in model, "Model must load remote picks through the BracketStore seam.", errors)
    require("bracketStore.saveUserBracket(bracketDocument)" in model, "Model must save remote picks through the BracketStore seam.", errors)
    require("if (!remotePersistenceActive)" in model and "saveToStorage(picks)" in model, "LocalStorage writes must be skipped while remote persistence is active.", errors)
    require("legacyPicksFromRemoteBracketDocument" in model and 'record?.pick?.kind === "team"' in model, "Model must hydrate visible picks from remote picksBySlot records.", errors)

    for rel, text in {
        "site/js/mvc/controller.js": controller,
        "site/js/mvc/view.js": view,
    }.items():
        require("Supabase" not in text and "user_brackets" not in text and "bracket_json" not in text, f"{rel} must not know about Supabase persistence.", errors)

    require("teamsByIdFromPicksBySlot" in store, "SupabaseBracketStore must validate saved team picks from BracketDocument records.", errors)
    require('pick: { kind: "team", teamId: "FRA" }' in smoke, "Smoke test must exercise a real team pick value, not only slot presence.", errors)

    if errors:
        print("Dev active Supabase bracket store verification failed: " + "; ".join(errors))
        return 1

    print("OK: dev-only active SupabaseBracketStore selection saves real gameplay picks without changing normal local gameplay.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
