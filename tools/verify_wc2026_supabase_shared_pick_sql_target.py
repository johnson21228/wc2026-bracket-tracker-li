#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

def read(path):
    p = ROOT / path
    if not p.exists():
        errors.append(f"missing {path}")
        return ""
    return p.read_text()

combined = "\n".join(read(path) for path in [
    "docs/backend/wc2026_supabase_shared_pick_sql_target.md",
    "source/sql/wc2026_supabase_shared_pick_schema_draft.sql",
    "source/sql/wc2026_supabase_shared_pick_rls_draft.sql",
    "cards/215_add_supabase_backend_schema_card.md",
    "cards/216_implement_supabase_remote_bracket_store_card.md",
    "cards/218_add_submit_lock_bracket_behavior_card.md",
    "cards/221_confirm_supabase_sql_readiness_card.md",
])

required_tokens = [
    "public.profiles",
    "public.user_brackets",
    "visibility",
    "submitted_at",
    "locked_at",
    "picks_json",
    "WRITE is private",
    "READ can be shared",
    "user_brackets_select_own_or_shared",
    "profiles_select_authenticated",
    "service role key",
]
for token in required_tokens:
    if token not in combined:
        errors.append(f"shared-pick Supabase target missing token: {token}")

schema = read("source/sql/wc2026_supabase_shared_pick_schema_draft.sql")
if "primary key (user_id, game_id)" not in schema:
    errors.append("user_brackets must be keyed by (user_id, game_id)")
if "status text" in schema:
    errors.append("schema draft must not use superseded status text column as DB authority")
if "references auth.users(id)" not in schema:
    errors.append("schema must reference auth.users(id)")

rls = read("source/sql/wc2026_supabase_shared_pick_rls_draft.sql")
for token in ["user_id = auth.uid()", "visibility = 'public'", "submitted_at is not null", "locked_at is not null", "and submitted_at is null", "and locked_at is null"]:
    if token not in rls:
        errors.append(f"RLS draft missing expected rule fragment: {token}")

readiness = read("cards/221_confirm_supabase_sql_readiness_card.md")
if "`status`" in readiness and "`submitted_at` and `locked_at`" not in readiness:
    errors.append("Card 221 should identify status-only DB authority as superseded")

makefile = read("Makefile")
if "python3 tools/verify_wc2026_supabase_shared_pick_sql_target.py" not in makefile:
    errors.append("Makefile verify target does not run shared-pick SQL target verifier")

if errors:
    print("WC2026 Supabase shared-pick SQL target verification failed:")
    for e in errors:
        print(f"- {e}")
    sys.exit(1)

print("OK: Supabase shared-pick SQL target is canonical before SQL execution.")
