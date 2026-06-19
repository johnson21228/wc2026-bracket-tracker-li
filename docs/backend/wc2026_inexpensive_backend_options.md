# WC2026 Inexpensive Backend Options

## Recommended first path

Use Supabase Auth + Supabase Postgres for the first invite-ready version.

Why:

- authentication and database are bundled
- Row Level Security can protect user-owned bracket rows
- no always-on custom server is required
- static frontend hosting can remain in place
- the browser can use the public anon key safely when RLS is correct

## MVP table

```sql
create table public.user_brackets (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users(id) on delete cascade,
  game_id text not null check (game_id in ('game1', 'game2')),
  status text not null default 'draft' check (status in ('draft', 'submitted', 'locked')),
  picks_json jsonb not null default '{}'::jsonb,
  submitted_at timestamptz,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  unique(user_id, game_id)
);
```

## Security posture

Enable Row Level Security. Users may read and write only their own draft brackets. Submitted or locked brackets must not be editable through the normal client path.

The service role key must never be committed. Never commit the Supabase service role key. The public anon key may be present in browser config only when RLS is correct.

## Alternatives

Firebase Auth + Firestore is viable and inexpensive for early usage, but the JSON document model and security rules differ.

Cloudflare Pages + Workers + D1 can be very inexpensive, but it requires more custom API/auth work and is therefore not the first choice for this repo.

## Cost posture

Start with free/low-cost hosted services. Upgrade only when real usage, production stability, backups, or support require it.
