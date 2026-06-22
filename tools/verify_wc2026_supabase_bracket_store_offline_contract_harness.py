#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read(path):
    return (ROOT / path).read_text(encoding="utf-8", errors="ignore")

def require(condition, message, errors):
    if not condition:
        errors.append(message)

def main():
    errors = []

    harness_path = ROOT / "tools/run_wc2026_supabase_bracket_store_offline_contract_harness.js"
    require(harness_path.exists(), "offline SupabaseBracketStore contract harness is missing", errors)
    harness = read("tools/run_wc2026_supabase_bracket_store_offline_contract_harness.js") if harness_path.exists() else ""

    for token in [
        "FakeSupabaseClient",
        "FakeSupabaseQuery",
        "SupabaseBracketStore",
        "createSupabaseBracketStore",
        "loadUserBracket",
        "saveUserBracket",
        "user_brackets",
        "picks_json",
        ".upsert(",
        "picksBySlot",
        "RemoteStoreActivationGuard",
    ]:
        require(token in harness, f"offline harness missing token: {token}", errors)

    for token in [
        "https://tkjqsegszveugdvoeits.supabase.co",
        "sb_publishable_wWTMppX8T5nOplM4s_HA7A_bgUn337M",
        "service_role",
        "fetch(",
        "XMLHttpRequest",
    ]:
        require(token not in harness, f"offline harness must not contain real network/secret token: {token}", errors)

    require(
        "https://offline-harness.supabase.invalid" in harness,
        "offline harness must use invalid offline Supabase URL sentinel",
        errors,
    )

    runtime_paths = [
        "site/js/app.js",
        "site/js/services/BracketRepository.js",
        "site/js/mvc/view.js",
        "site/js/mvc/controller.js",
        "site/js/controllers/Game1R32PickController.js",
    ]
    for rel in runtime_paths:
        text = read(rel)
        require("SupabaseBracketStore" not in text, f"{rel} must not import or activate SupabaseBracketStore", errors)
        require("RemoteStoreActivationGuard" not in text, f"{rel} must not import or activate RemoteStoreActivationGuard", errors)

    makefile = read("Makefile")
    require(
        "node tools/run_wc2026_supabase_bracket_store_offline_contract_harness.js" in makefile,
        "offline harness must be included in make verify",
        errors,
    )
    require(
        "python3 tools/verify_wc2026_supabase_bracket_store_offline_contract_harness.py" in makefile,
        "offline harness verifier must be included in make verify",
        errors,
    )

    combined_docs = "\n".join([
        read("captures/CAPTURE_BACK_SUPABASE_BRACKET_STORE_OFFLINE_CONTRACT_HARNESS.md"),
        read("cards/272_add_supabase_bracket_store_offline_contract_harness_card.md"),
        read("docs/architecture/bracketeering_supabase_bracket_store_offline_contract_harness.md"),
        read("li/world_cup/supabase_bracket_store_offline_contract_harness_rule.md"),
    ])
    for phrase in [
        "fake in-memory Supabase client",
        "does not activate remote mode",
        "does not call the real Supabase network",
        "does not apply SQL",
        "Local browser storage remains the active public path",
        "does not merge to `main`",
    ]:
        require(phrase in combined_docs, f"offline harness docs missing phrase: {phrase}", errors)

    if errors:
        print("WC2026 SupabaseBracketStore offline contract harness verification failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("OK: WC2026 SupabaseBracketStore offline contract harness verifies adapter shape without activating remote mode.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
