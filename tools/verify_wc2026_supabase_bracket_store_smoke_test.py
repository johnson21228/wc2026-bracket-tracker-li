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

    smoke = read("site/js/dev/SupabaseBracketStoreSmokeTest.js")
    app = read("site/js/app.js")
    repo = read("site/js/services/BracketRepository.js")
    view = read("site/js/mvc/view.js")
    controller = read("site/js/mvc/controller.js")
    r32_controller = read("site/js/controllers/Game1R32PickController.js")

    require("DEV_SMOKE_QUERY_FLAG" in smoke and '"devSupabaseBracketSmoke"' in smoke, "smoke test must define the dev query flag.", errors)
    require("shouldRunSupabaseBracketStoreSmokeTest" in smoke, "smoke test must expose query-flag gating.", errors)
    require('params.get(DEV_SMOKE_QUERY_FLAG) === "1"' in smoke, "smoke test must only run when devSupabaseBracketSmoke=1.", errors)
    require('import { SupabaseBracketStore } from "../services/SupabaseBracketStore.js";' in smoke, "smoke test must import SupabaseBracketStore directly.", errors)
    require("new SupabaseBracketStore" in smoke, "smoke test must instantiate SupabaseBracketStore.", errors)
    require("store.requireSignedInUser()" in smoke, "smoke test must require a signed-in Supabase user.", errors)
    require("store.saveUserBracket(smokeBracket)" in smoke, "smoke test must save through SupabaseBracketStore.saveUserBracket.", errors)
    require("store.loadUserBracket(user.id" in smoke, "smoke test must load through SupabaseBracketStore.loadUserBracket.", errors)
    require("verifyRoundTrip" in smoke and "picksBySlot" in smoke, "smoke test must verify the round-trip picksBySlot payload.", errors)
    require("[SupabaseBracketStoreSmokeTest] PASS" in smoke, "smoke test must log a clear PASS.", errors)
    require("[SupabaseBracketStoreSmokeTest] FAIL" in smoke, "smoke test must log a clear FAIL.", errors)

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
        require(f'"{key}"' in smoke, f"smoke test must build/verify canonical BracketDocument field {key}.", errors)

    require('new URLSearchParams(window.location.search).get("devSupabaseBracketSmoke") === "1"' in app, "app startup must gate smoke test import behind devSupabaseBracketSmoke=1.", errors)
    require('new URL("js/dev/SupabaseBracketStoreSmokeTest.js", document.baseURI).href' in app and "import(smokeModuleUrl)" in app, "app must dynamically import the smoke test only when gated without old ./dev runtime imports.", errors)

    require("bracketStore: new LocalStorageBracketStore()" in repo, "default static repository must remain local-only.", errors)
    require("createSupabaseBracketRepository" in repo, "remote repository must remain available only through explicit seam.", errors)
    require("createSupabaseBracketRepository" not in app, "normal app startup must not switch to Supabase repository.", errors)
    require("SupabaseBracketStoreSmokeTest" in app and "./dev/" not in app, "app may reference smoke test only through gated dynamic import without old ./dev runtime imports.", errors)

    forbidden_runtime_files = {
        "site/js/mvc/view.js": view,
        "site/js/mvc/controller.js": controller,
        "site/js/controllers/Game1R32PickController.js": r32_controller,
    }
    for rel, text in forbidden_runtime_files.items():
        require("SupabaseBracketStore" not in text, f"{rel} must not know SupabaseBracketStore.", errors)
        require("devSupabaseBracketSmoke" not in text, f"{rel} must not own the dev smoke flag.", errors)
        require(".from(\"user_brackets\")" not in text and ".from('user_brackets')" not in text, f"{rel} must not call user_brackets directly.", errors)
        require("bracket_json" not in text, f"{rel} must not know the Supabase bracket_json column.", errors)

    require("localStorage" not in smoke, "smoke test must not migrate or read localStorage.", errors)
    require("LocalStorageBracketStore" not in smoke, "smoke test must not dual-write local storage.", errors)
    require("save button" not in smoke.lower() and "load button" not in smoke.lower(), "smoke test must not add gameplay save/load controls.", errors)

    if errors:
        print("SupabaseBracketStore smoke test verification failed: " + "; ".join(errors))
        return 1

    print("OK: SupabaseBracketStore dev-only smoke test is query-gated and does not enable gameplay remote save.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
