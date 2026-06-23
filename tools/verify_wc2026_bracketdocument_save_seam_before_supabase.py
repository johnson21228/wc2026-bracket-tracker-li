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

    bracket_repo = read("site/js/services/BracketRepository.js")
    local_store = read("site/js/services/LocalStorageBracketStore.js")
    supabase_store_path = ROOT / "site/js/services/SupabaseBracketStore.js"

    require("LocalStorageBracketStore" in bracket_repo, "BracketRepository must preserve the local store seam.", errors)
    require("bracketStore = new LocalStorageBracketStore()" in bracket_repo, "Static/default repository must remain local-only for anonymous play.", errors)
    require("localStorage" in local_store, "LocalStorageBracketStore must remain the local anonymous persistence path.", errors)

    require(supabase_store_path.exists(), "SupabaseBracketStore is now the intentional remote bracket persistence boundary.", errors)
    if supabase_store_path.exists():
        supabase_store = supabase_store_path.read_text(encoding="utf-8", errors="ignore")
        require('.from(TABLE_NAME)' in supabase_store and 'const TABLE_NAME = "user_brackets"' in supabase_store, "SupabaseBracketStore must own user_brackets access.", errors)
        require("bracket_json" in supabase_store, "SupabaseBracketStore must write canonical bracket_json.", errors)

    app = read("site/js/app.js")
    view = read("site/js/mvc/view.js")
    controller = read("site/js/mvc/controller.js")
    for rel, text in {
        "site/js/app.js": app,
        "site/js/mvc/view.js": view,
        "site/js/mvc/controller.js": controller,
    }.items():
        require(".from(\"user_brackets\")" not in text and ".from('user_brackets')" not in text, f"{rel} must not make direct Supabase bracket writes.", errors)

    if errors:
        print("BracketDocument save seam verification failed: " + "; ".join(errors))
        return 1

    print("OK: bracket save seam now has local anonymous persistence plus an explicit SupabaseBracketStore remote boundary.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
