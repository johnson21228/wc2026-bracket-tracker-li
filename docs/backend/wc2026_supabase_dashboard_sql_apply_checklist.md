# WC2026 Supabase dashboard SQL apply checklist

This checklist prepares the future Supabase dashboard SQL application.

It does not apply SQL.
It does not activate remote mode.
It does not change public runtime behavior.

## Current source SQL drafts

Schema draft: source/sql/wc2026_supabase_shared_pick_schema_draft.sql

RLS draft: source/sql/wc2026_supabase_shared_pick_rls_draft.sql

Canonical target document: docs/backend/wc2026_supabase_shared_pick_sql_target.md

## Pre-apply requirements

Before SQL is pasted into the Supabase dashboard:

- make verify passes locally.
- SupabaseBracketStore remains inactive.
- RemoteStoreActivationGuard remains fail-closed.
- public runtime still defaults to LocalStorageBracketStore.
- View and Controller do not call Supabase.
- the feature branch has been pushed as a backup.
- main remains the public Pages release line.

## Dashboard application order

When intentionally applying SQL later:

1. Open the Supabase dashboard for the Bracketeering project.
2. Open the SQL editor.
3. Paste and run source/sql/wc2026_supabase_shared_pick_schema_draft.sql.
4. Confirm tables, functions, and triggers are created.
5. Paste and run source/sql/wc2026_supabase_shared_pick_rls_draft.sql.
6. Confirm RLS is enabled on public tables.
7. Confirm policies match the product invariant: WRITE is private. READ can be shared when game rules allow it.
8. Capture evidence in outputs/supabase/.
9. Run local verification again.
10. Only after SQL evidence is captured should a later CB consider remote-mode activation.

## Required evidence after SQL is applied later

Create an evidence file under outputs/supabase/.

Recommended filename: outputs/supabase/wc2026_supabase_sql_apply_evidence_YYYYMMDD.md

Evidence should include:

- date/time applied
- Supabase project id or project URL
- schema SQL source file path
- RLS SQL source file path
- confirmation that profiles exists
- confirmation that user_brackets exists
- confirmation that picks_json exists
- confirmation that primary key is (user_id, game_id)
- confirmation that RLS is enabled
- list of select/insert/update policies reviewed
- explicit note that no runtime remote mode was activated by SQL application

## Not part of this checklist

This checklist does not:

- paste SQL into Supabase
- execute SQL
- connect to Supabase
- create tables
- change RLS
- activate SupabaseBracketStore
- wire signed-in remote mode
- merge to main
- publish Pages
