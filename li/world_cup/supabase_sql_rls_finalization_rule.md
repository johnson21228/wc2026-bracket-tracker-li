# Supabase SQL/RLS finalization rule

Bracketeering Supabase SQL must be finalized against the Pages-owned canonical `BracketDocument` before any dashboard SQL is applied.

## Invariant

```text
Runtime model first. Supabase persistence second.
```

Supabase persists the document the site already owns. It does not define bracket geometry, menu rules, controller behavior, advancement logic, or rendering.

## Storage target

`public.user_brackets.picks_json` stores the same canonical `BracketDocument` used by local runtime and localStorage.

Required top-level document fields:

- `schemaVersion`
- `gameId`
- `status`
- `expectedPickCount`
- `updatedAt`
- `picksBySlot`

The row owns identity and sharing metadata:

- `user_id`
- `game_id`
- `visibility`
- `submitted_at`
- `locked_at`
- timestamps

## RLS/finality rule

Owner writes are private. Shared reads are allowed only when visibility or lifecycle rules allow them.

RLS must not block the ordinary submit/lock transition. Therefore owner update RLS may check that the existing row is owned by the user and not already locked, but the `WITH CHECK` must not require the resulting row to remain unsubmitted/unlocked.

Post-submit and post-lock immutability is enforced by trigger:

- after a row is submitted, `picks_json`, `user_id`, and `game_id` must not change
- after a row is locked, no update is allowed
- setting `locked_at` implies `submitted_at`

## Out of scope

This rule does not authorize applying SQL, adding Supabase client code, adding Auth UI, or implementing `SupabaseBracketStore`.
