# WC2026 Inexpensive Backend Options

## Recommended first path

Use Supabase Auth + Supabase Postgres for the first invite-ready version.

Why:

- authentication and database are bundled
- Row Level Security can protect user-owned bracket rows
- RLS can also allow shared read access when game rules allow it
- no always-on custom server is required
- static frontend hosting can remain in place
- the browser can use the public anon/publishable key safely when RLS is correct

## Canonical MVP table target

The current SQL target is not the older private-only `status` table sketch. The canonical target is documented in:

- `docs/backend/wc2026_supabase_shared_pick_sql_target.md`
- `source/sql/wc2026_supabase_shared_pick_schema_draft.sql`
- `source/sql/wc2026_supabase_shared_pick_rls_draft.sql`

The backend should include:

- `public.profiles` for display names without exposing raw auth emails
- `public.user_brackets` with one row per `(user_id, game_id)`
- `picks_json` for the canonical pick-state document
- `visibility` for future shared pick views
- `submitted_at` and `locked_at` for contest safety and shared-read eligibility

## Security posture

Enable Row Level Security. Users may write only their own unsubmitted/unlocked bracket rows. Owners may always read their own rows. Other signed-in users may read rows only when `visibility`, `submitted_at`, or `locked_at` allows it.

The service role key must never be committed. Never commit the Supabase service role key. The public anon/publishable key may be present in browser config only when RLS is correct.

Core invariant:

```text
WRITE is private.
READ can be shared when game rules allow it.
```

## Alternatives

Firebase Auth + Firestore is viable and inexpensive for early usage, but the JSON document model and security rules differ.

Cloudflare Pages + Workers + D1 can be very inexpensive, but it requires more custom API/auth work and is therefore not the first choice for this repo.

## Cost posture

Start with free/low-cost hosted services. Upgrade only when real usage, production stability, backups, or support require it.
