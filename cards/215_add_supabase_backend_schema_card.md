# Card 215: Add Supabase Backend Schema and RLS Setup

## Intent

Capture the inexpensive hosted backend setup for public play before any SQL is applied.

This card now targets the shared-pick Supabase contract, not the superseded private-only `user_brackets` draft.

## Product invariant

```text
WRITE is private.
READ can be shared when game rules allow it.
```

## Scope

- Supabase project setup notes
- `public.profiles` table for public display names without exposing raw auth email
- `public.user_brackets` table for canonical pick-state JSON per player per game
- `visibility`, `submitted_at`, and `locked_at` columns for future shared views and contest safety
- Row Level Security policies
- public anon/publishable key config pattern
- explicit warning to never commit service role keys, database passwords, direct Postgres URLs, or JWT secrets

## Intended SQL target

The canonical draft lives in:

- `docs/backend/wc2026_supabase_shared_pick_sql_target.md`
- `source/sql/wc2026_supabase_shared_pick_schema_draft.sql`
- `source/sql/wc2026_supabase_shared_pick_rls_draft.sql`

## RLS target

- Owners can insert only their own bracket rows.
- Owners can update only their own unsubmitted/unlocked bracket rows.
- Owners can read their own rows at any time.
- Other signed-in users can read rows when `visibility = 'public'`, `submitted_at is not null`, or `locked_at is not null`.
- Anonymous users cannot read or write remote bracket rows for MVP.

## Acceptance

- Backend setup docs are sufficient to create a test Supabase project.
- Supabase SQL target matches the Bracketeering Model Persistence Contract.
- The repo no longer points Card 215 at the private-only owner-read table model.
- The SQL target includes `profiles`, `visibility`, `submitted_at`, and `locked_at` before dashboard execution.
- No private-only owner-read assumption remains as the final target.
- No secret keys are committed.
- Static frontend hosting remains the frontend posture.

