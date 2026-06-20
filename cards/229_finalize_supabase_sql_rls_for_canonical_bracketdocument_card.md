# Card 229: Finalize Supabase SQL/RLS for canonical BracketDocument persistence

## Context

Cards 227 and 228 cleared the runtime blockers for Supabase:

- Card 227 made the Pages runtime use the full canonical `BracketDocument` model.
- Card 228 made the site save that `BracketDocument` through the repository/localStorage seam before Supabase implementation.

Now the Supabase SQL/RLS target can be finalized against the actual model the site owns.

## Purpose

Finalize the draft Supabase schema and RLS policy files before any SQL is applied in the Supabase dashboard.

This card is still a repo-side readiness card. It does not connect the browser to Supabase.

## Product invariant

```text
WRITE is private.
READ can be shared when game rules allow it.
```

## Required decisions

Supabase stores the same canonical `BracketDocument` produced by the Pages runtime:

```text
user_brackets.picks_json = canonical BracketDocument
```

Supabase row metadata owns identity and sharing state:

- `user_id`
- `game_id`
- `visibility`
- `submitted_at`
- `locked_at`
- row timestamps

The `picks_json` document owns portable bracket state:

- `schemaVersion`
- `gameId`
- `status`
- `expectedPickCount`
- `updatedAt`
- `picksBySlot`

## RLS correction

The previous owner-update policy required `submitted_at is null` and `locked_at is null` in both `USING` and `WITH CHECK`. That blocks the normal lifecycle update that sets `submitted_at` or `locked_at`.

The finalized target must allow an owner to update their own unlocked row so the app can perform draft saves and submit/lock transitions, while still preventing post-finalization pick mutation.

The target shape is:

- RLS `USING`: owner can update their own row only while the existing row is not locked.
- RLS `WITH CHECK`: the resulting row must still belong to the owner.
- A trigger prevents changing `picks_json`, `user_id`, or `game_id` after the bracket has already been submitted, and prevents any update after it has already been locked.

This keeps submit/lock possible without allowing bracket rewriting after finality.

## Scope

Update or create:

- `source/sql/wc2026_supabase_shared_pick_schema_draft.sql`
- `source/sql/wc2026_supabase_shared_pick_rls_draft.sql`
- `docs/backend/wc2026_supabase_shared_pick_sql_target.md`
- `li/world_cup/supabase_sql_rls_finalization_rule.md`
- `tools/verify_wc2026_supabase_sql_rls_finalization.py`
- Makefile verify wiring

## Explicitly out of scope

- Do not apply SQL in the Supabase dashboard.
- Do not add Supabase browser client code.
- Do not add auth UI.
- Do not implement `SupabaseBracketStore`.
- Do not commit secrets, service role keys, DB passwords, direct connection strings, or JWT secrets.

## Acceptance

- SQL draft stores canonical `BracketDocument` in `user_brackets.picks_json`.
- SQL draft checks required top-level `BracketDocument` fields.
- SQL draft checks that `picks_json.gameId` matches row `game_id`.
- `profiles` exists for public display identity.
- `user_brackets` is keyed by `(user_id, game_id)`.
- RLS allows owner insert.
- RLS allows owner update only for own existing unlocked row.
- RLS `WITH CHECK` no longer blocks setting `submitted_at` or `locked_at`.
- A trigger blocks mutating `picks_json` after submitted and blocks any update after locked.
- Shared reads remain owner-or-shared: owner, public visibility, submitted, or locked.
- Docs/LI state that this SQL is still not applied.
- No Supabase browser client code is added.
- `make verify` passes.
- `make pack` completes.
