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

    required_paths = [
        "docs/backend/wc2026_supabase_dashboard_sql_apply_checklist.md",
        "outputs/supabase/wc2026_supabase_sql_apply_evidence_template.md",
        "outputs/supabase/.gitkeep",
        "captures/CAPTURE_BACK_SUPABASE_SQL_DASHBOARD_APPLY_CHECKLIST_WITHOUT_APPLYING_SQL.md",
        "cards/273_add_supabase_sql_dashboard_apply_checklist_without_applying_sql_card.md",
        "li/world_cup/supabase_sql_dashboard_apply_checklist_rule.md",
    ]

    for rel in required_paths:
        require((ROOT / rel).exists(), f"missing required checklist artifact: {rel}", errors)

    combined = "\n".join(read(rel) for rel in required_paths if (ROOT / rel).exists())

    for token in [
        "source/sql/wc2026_supabase_shared_pick_schema_draft.sql",
        "source/sql/wc2026_supabase_shared_pick_rls_draft.sql",
        "docs/backend/wc2026_supabase_shared_pick_sql_target.md",
        "It does not apply SQL",
        "It does not activate remote mode",
        "WRITE is private",
        "READ can be shared when game rules allow it",
        "outputs/supabase/",
        "picks_json",
        "primary key is (user_id, game_id)",
        "RemoteStoreActivationGuard",
        "LocalStorageBracketStore",
        "View and Controller do not call Supabase",
        "main remains the public Pages release line",
    ]:
        require(token in combined, f"checklist artifacts missing token: {token}", errors)

    schema_sql = read("source/sql/wc2026_supabase_shared_pick_schema_draft.sql")
    rls_sql = read("source/sql/wc2026_supabase_shared_pick_rls_draft.sql")
    require("create table" in schema_sql.lower(), "schema draft SQL must remain present", errors)
    require("picks_json" in schema_sql, "schema draft SQL must still define picks_json", errors)
    require("create policy" in rls_sql.lower() or "alter table" in rls_sql.lower(), "RLS draft SQL must remain present", errors)

    runtime_paths = [
        "site/js/app.js",
        "site/js/services/BracketRepository.js",
        "site/js/mvc/view.js",
        "site/js/mvc/controller.js",
        "site/js/controllers/Game1R32PickController.js",
    ]
    for rel in runtime_paths:
        text = read(rel)
        require("wc2026_supabase_dashboard_sql_apply_checklist" not in text, f"{rel} must not import checklist artifacts", errors)
        require("supabase_sql_apply_evidence" not in text, f"{rel} must not import evidence artifacts", errors)

    repo_text = read("site/js/services/BracketRepository.js")
    require("new LocalStorageBracketStore()" in repo_text, "BracketRepository must still default to LocalStorageBracketStore", errors)
    require("SupabaseBracketStore" not in repo_text, "BracketRepository must not activate SupabaseBracketStore", errors)

    guard_text = read("site/js/services/RemoteStoreActivationGuard.js")
    require("remoteStoreEnabled: false" in guard_text, "RemoteStoreActivationGuard must remain fail-closed", errors)

    makefile = read("Makefile")
    require(
        "python3 tools/verify_wc2026_supabase_sql_dashboard_apply_checklist.py" in makefile,
        "SQL dashboard apply checklist verifier must be included in make verify",
        errors,
    )

    if errors:
        print("WC2026 Supabase SQL dashboard apply checklist verification failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("OK: WC2026 Supabase SQL dashboard apply checklist is captured without applying SQL or activating remote mode.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
