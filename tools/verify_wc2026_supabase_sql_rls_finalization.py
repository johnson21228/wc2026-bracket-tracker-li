#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

def read(path: str) -> str:
    p = ROOT / path
    if not p.exists():
        errors.append(f"missing {path}")
        return ""
    return p.read_text()

schema = read("source/sql/wc2026_supabase_shared_pick_schema_draft.sql")
rls = read("source/sql/wc2026_supabase_shared_pick_rls_draft.sql")
doc = read("docs/backend/wc2026_supabase_shared_pick_sql_target.md")
li = read("li/world_cup/supabase_sql_rls_finalization_rule.md")
card = read("cards/229_finalize_supabase_sql_rls_for_canonical_bracketdocument_card.md")
makefile = read("Makefile")
combined = "\n".join([schema, rls, doc, li, card])

for token in [
    "public.profiles",
    "public.user_brackets",
    "picks_json",
    "schemaVersion",
    "gameId",
    "status",
    "expectedPickCount",
    "updatedAt",
    "picksBySlot",
    "primary key (user_id, game_id)",
    "visibility in ('private', 'public', 'room')",
    "picks_json ->> 'gameId' = game_id",
    "picks_json ->> 'status' in ('draft', 'submitted', 'locked')",
    "locked_at is null or submitted_at is not null",
    "prevent_user_bracket_finalized_mutation",
    "submitted bracket picks_json cannot change",
    "locked brackets cannot be updated",
    "WRITE is private",
    "READ can be shared",
]:
    if token not in combined:
        errors.append(f"SQL/RLS finalization missing token: {token}")

if "default '{}'::jsonb" in schema:
    errors.append("user_brackets.picks_json should not default to an invalid non-canonical empty object")

if "user_brackets_update_own_unsubmitted" in rls and "drop policy if exists \"user_brackets_update_own_unsubmitted\"" not in rls:
    errors.append("superseded unsubmitted update policy should only appear as a dropped legacy policy")

if "create policy \"user_brackets_update_own_unlocked\"" not in rls:
    errors.append("RLS must create owner-unlocked update policy")

policy_start = rls.find("create policy \"user_brackets_update_own_unlocked\"")
policy = rls[policy_start:] if policy_start != -1 else rls
with_check_start = policy.find("with check")
with_check = policy[with_check_start:] if with_check_start != -1 else ""
if "submitted_at is null" in with_check or "locked_at is null" in with_check:
    errors.append("RLS WITH CHECK must not require submitted_at/locked_at to remain null")

for token in [
    "user_id = auth.uid()",
    "visibility = 'public'",
    "submitted_at is not null",
    "locked_at is not null",
    "with check (\n  user_id = auth.uid()\n)",
]:
    if token not in rls:
        errors.append(f"RLS draft missing expected finalized fragment: {token}")

if "python3 tools/verify_wc2026_supabase_sql_rls_finalization.py" not in makefile:
    errors.append("Makefile verify target does not run SQL/RLS finalization verifier")

if "do not apply SQL" not in combined.lower() and "not applied" not in combined.lower():
    errors.append("docs/card must state SQL is not applied by this card")

if errors:
    print("WC2026 Supabase SQL/RLS finalization verification failed:")
    for e in errors:
        print(f"- {e}")
    sys.exit(1)

print("OK: WC2026 Supabase SQL/RLS is finalized against canonical BracketDocument before dashboard application.")
