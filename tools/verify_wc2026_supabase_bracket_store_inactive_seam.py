#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read(path):
    return (ROOT / path).read_text()

def require(condition, message, errors):
    if not condition:
        errors.append(message)

def main():
    errors = []

    store_path = ROOT / "site/js/services/SupabaseBracketStore.js"
    require(store_path.exists(), "SupabaseBracketStore.js must exist", errors)
    store = store_path.read_text() if store_path.exists() else ""

    required_store_tokens = [
        'import { createClient } from "https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/+esm"',
        'import { WC2026_SUPABASE_PUBLIC_CONFIG } from "../config/supabase.public.js"',
        'import { normalizeBracketDocument } from "../model/UserBracketModel.js"',
        'const DEFAULT_TABLE_NAME = "user_brackets"',
        "class SupabaseBracketStore",
        "loadUserBracket(userId)",
        "saveUserBracket(bracketDocument)",
        ".select(\"picks_json\")",
        ".eq(\"user_id\", cleanId)",
        ".eq(\"game_id\", this.gameId)",
        "picks_json: documentToSave",
        "visibility: this.visibility",
        '.upsert(row, { onConflict: "user_id,game_id" })',
        "SupabaseBracketStore loadUserBracket failed",
        "SupabaseBracketStore saveUserBracket failed",
        "function createSupabaseBracketStore(options = {})",
        "export {",
        "SupabaseBracketStore",
        "createSupabaseBracketStore",
    ]

    for token in required_store_tokens:
        require(token in store, f"SupabaseBracketStore missing token: {token}", errors)

    runtime_paths_that_must_not_import_store = [
        "site/js/app.js",
        "site/js/services/BracketRepository.js",
        "site/js/mvc/view.js",
        "site/js/mvc/controller.js",
        "site/js/controllers/Game1R32PickController.js",
        "site/js/board/BoardShell.js",
        "site/js/board/R32PickMenuLayer.js",
    ]

    for rel in runtime_paths_that_must_not_import_store:
        text = read(rel)
        require(
            "SupabaseBracketStore" not in text,
            f"{rel} must not import or activate SupabaseBracketStore yet",
            errors,
        )

    bracket_repo = read("site/js/services/BracketRepository.js")
    require(
        "new LocalStorageBracketStore()" in bracket_repo,
        "BracketRepository must still default to LocalStorageBracketStore",
        errors,
    )
    require(
        "createLocalActiveBracketSession" in bracket_repo,
        "BracketRepository must still use local active session by default",
        errors,
    )

    contract_verifier = read("tools/verify_wc2026_supabase_remote_bracket_store_contract.py")
    require(
        "SupabaseBracketStore.js may now exist after the inactive-seam implementation CB" in contract_verifier,
        "remote store contract verifier must be updated so it no longer rejects the implementation file",
        errors,
    )

    makefile = read("Makefile")
    require(
        "python3 tools/verify_wc2026_supabase_bracket_store_inactive_seam.py" in makefile,
        "new inactive SupabaseBracketStore verifier must be included in make verify",
        errors,
    )

    combined_docs = "\n".join([
        read("li/world_cup/supabase_bracket_store_inactive_seam_rule.md"),
        read("docs/architecture/bracketeering_supabase_bracket_store_inactive_seam.md"),
        read("captures/CAPTURE_BACK_IMPLEMENT_SUPABASE_BRACKET_STORE_INACTIVE_SEAM.md"),
        read("cards/270_implement_supabase_bracket_store_inactive_seam_card.md"),
    ])
    for phrase in [
        "not active in public runtime",
        "local/browser storage",
        "one row per signed-in player/game",
        "full canonical `BracketDocument`",
        "View and Controller code must not call Supabase directly",
        "does not apply Supabase SQL",
        "does not change Supabase dashboard state",
        "does not merge to `main`",
    ]:
        require(phrase in combined_docs, f"inactive seam docs missing phrase: {phrase}", errors)

    if errors:
        print("WC2026 SupabaseBracketStore inactive seam verification failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("OK: WC2026 SupabaseBracketStore exists behind an inactive remote store seam while local runtime remains active.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
