# WC2026 Supabase SQL apply evidence template

Status: template only. SQL not applied by this file.

## Apply metadata

Date applied:

Supabase project id or URL:

Applied by:

Feature branch commit:

## SQL source files

Schema source: source/sql/wc2026_supabase_shared_pick_schema_draft.sql

RLS source: source/sql/wc2026_supabase_shared_pick_rls_draft.sql

Canonical target: docs/backend/wc2026_supabase_shared_pick_sql_target.md

## Schema confirmation

- profiles table exists:
- user_brackets table exists:
- user_brackets.user_id exists:
- user_brackets.game_id exists:
- user_brackets.picks_json exists:
- user_brackets.visibility exists:
- user_brackets.submitted_at exists:
- user_brackets.locked_at exists:
- primary key is (user_id, game_id):
- game_id allows game1 and game2:

## RLS confirmation

- RLS enabled on profiles:
- RLS enabled on user_brackets:
- owner can read own bracket:
- shared readable policy exists:
- owner can insert own row:
- owner can update own unlocked row:
- policy review preserves WRITE private / READ shareable invariant:

## Runtime confirmation

- SupabaseBracketStore still inactive after SQL apply:
- RemoteStoreActivationGuard still fail-closed:
- BracketRepository still defaults to LocalStorageBracketStore:
- View and Controller still do not call Supabase:
- public Pages main not merged/published from this branch:

## Notes

