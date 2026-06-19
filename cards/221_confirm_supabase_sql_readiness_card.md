# Card 221: Confirm Supabase SQL Readiness and Return Point

## Intent

Create a Workbench checkpoint before running the Supabase SQL setup for hosted Bracketeering Pub bracket storage.

This card exists so the Supabase dashboard action can be paused, checked against LI, and resumed without losing the intended setup path.

## Context

The Supabase project has been created and appears healthy in the Supabase dashboard.

The Bracketeering Pub site remains a static frontend. Supabase is being introduced only as the hosted account + canonical bracket JSON storage backend.

This card precedes the SQL action for Card 215 and the implementation work for Card 216.

The old private-only `user_brackets` assumption is superseded. Bracketeering players should eventually be able to see other players' picks when game rules allow.

## Product invariant

```text
WRITE is private.
READ can be shared when visibility/submission/lock rules allow.
```

## Related Cards

- Card 211: Define canonical public-play pick-state storage
- Card 212: Route local storage through canonical pick-state
- Card 213: Define remote bracket store contract
- Card 214: Add signed-in user UI shell
- Card 215: Add Supabase backend schema and RLS setup
- Card 216: Implement Supabase remote bracket store
- Card 217: Add save/load/sync status and local-to-account migration
- Card 218: Add submit/lock bracket behavior
- Card 219: Add invite-ready public play verification

## Pre-SQL Readiness Checklist

Before running SQL in Supabase, confirm:

- Supabase project exists.
- Project status is healthy.
- Region is acceptable for expected players.
- Data API is enabled.
- The site remains static-hosted.
- No custom server is required for this step.
- No service role key is copied into the repo.
- No database password is copied into the repo.
- No direct Postgres connection string is copied into the repo.
- Browser code will eventually use only the Supabase project URL and anon/publishable key.
- The SQL action creates only the intended public-play bracket storage tables and policies.
- No raw auth email is exposed as a public player display name.

## Intended SQL Objects

The SQL setup should create:

- `public.profiles`
- `public.user_brackets`
- indexes for game/shared-read lookup
- `public.set_updated_at()`
- updated-at triggers for `profiles` and `user_brackets`
- Row Level Security enabled on both tables
- RLS policies for authenticated profile read / own profile insert/update
- RLS policies for owner-only bracket insert/update
- RLS policy for owner-or-shared bracket select

## Intended Storage Model

Supabase stores one canonical pick-state JSON document per user per game:

- `user_id`
- `game_id`
- `picks_json`
- `visibility`
- `submitted_at`
- `locked_at`

The `picks_json` document is the same canonical bracket state used by:

- localStorage
- export/import
- future Supabase save/load
- future submit/lock
- future scoring
- future shared pick views

## SQL Source of Truth

Review these repo files before opening the Supabase SQL editor:

- `docs/backend/wc2026_supabase_shared_pick_sql_target.md`
- `source/sql/wc2026_supabase_shared_pick_schema_draft.sql`
- `source/sql/wc2026_supabase_shared_pick_rls_draft.sql`

## Security Invariant

Never commit or expose:

- Supabase service role key
- database password
- direct Postgres connection string
- JWT secret

Allowed for browser/runtime configuration:

- Supabase project URL
- Supabase anon/publishable key

The safety boundary depends on Row Level Security being enabled and correct.

## Return Point

After this card is confirmed, return to the Supabase dashboard and review the SQL setup for Card 215.

After SQL succeeds, confirm:

- `public.profiles` appears in Table Editor.
- `public.user_brackets` appears in Table Editor.
- RLS is enabled on both tables.
- Policies exist for profile select/insert/update.
- Policies exist for bracket select/insert/update.
- The bracket select policy is owner-or-shared, not owner-only.
- No real player data has been inserted yet.
- The project URL and anon/publishable key can be copied later for Card 216 implementation.

## Acceptance

- The Supabase SQL action has a named Workbench checkpoint.
- The setup can be resumed from the Supabase dashboard without relying on chat memory.
- The repo records that SQL setup is a backend readiness step, not the frontend implementation itself.
- The repo no longer names `status` as the database authority for submit/lock; database authority is `submitted_at` and `locked_at`.
- Secrets remain outside the repo.

- The SQL action creates only the intended public-play bracket storage table and policies.
- The SQL target matches the Bracketeering Model Persistence Contract before any SQL is applied.
