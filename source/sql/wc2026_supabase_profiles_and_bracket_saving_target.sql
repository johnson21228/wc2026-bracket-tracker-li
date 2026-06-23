-- WC2026 Bracketeering Supabase public player name + bracket saving target
--
-- Status:
--   Target SQL only. Do not apply until reviewed in the Supabase dashboard.
--
-- Product boundary:
--   - Supabase Auth owns private login identity.
--   - public.profiles owns public player display names.
--   - public.user_brackets owns durable canonical BracketDocument JSON.
--   - Browser local play remains supported when signed out.
--   - The site pick abstraction is unchanged: BracketDocument / picksBySlot remain canonical.
--
-- Security invariant:
--   WRITE is private.
--   READ can be shared only when game rules and row visibility allow it.

create extension if not exists pgcrypto with schema extensions;

create table if not exists public.profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  display_name text not null,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),

  constraint profiles_display_name_length
    check (char_length(btrim(display_name)) between 2 and 40),

  constraint profiles_display_name_no_control_chars
    check (display_name !~ '[[:cntrl:]]')
);

comment on table public.profiles is
  'Public Bracketeering player identity. Does not store private auth email.';

comment on column public.profiles.id is
  'Matches auth.users.id. This is not an email and must not be shown as the player name.';

comment on column public.profiles.display_name is
  'Public player name visible in shared pick views and leaderboards.';

create table if not exists public.user_brackets (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users(id) on delete cascade,
  tournament_id text not null,
  game_id text not null,
  bracket_json jsonb not null,
  visibility text not null default 'private',
  status text not null default 'draft',
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),

  constraint user_brackets_unique_user_tournament_game
    unique (user_id, tournament_id, game_id),

  constraint user_brackets_visibility_allowed
    check (visibility in ('private', 'public')),

  constraint user_brackets_status_allowed
    check (status in ('draft', 'submitted', 'locked', 'archived')),

  constraint user_brackets_document_shape
    check (
      jsonb_typeof(bracket_json) = 'object'
      and bracket_json ? 'schemaVersion'
      and bracket_json ? 'tournamentId'
      and bracket_json ? 'gameId'
      and bracket_json ? 'picksBySlot'
      and jsonb_typeof(bracket_json -> 'picksBySlot') = 'object'
    )
);

comment on table public.user_brackets is
  'Durable Bracketeering bracket documents. One row per user/tournament/game.';

comment on column public.user_brackets.bracket_json is
  'Canonical BracketDocument JSON. The picksBySlot abstraction remains unchanged.';

create or replace function public.set_updated_at()
returns trigger
language plpgsql
security invoker
set search_path = public
as $$
begin
  new.updated_at = now();
  return new;
end;
$$;

drop trigger if exists profiles_set_updated_at on public.profiles;
create trigger profiles_set_updated_at
before update on public.profiles
for each row
execute function public.set_updated_at();

drop trigger if exists user_brackets_set_updated_at on public.user_brackets;
create trigger user_brackets_set_updated_at
before update on public.user_brackets
for each row
execute function public.set_updated_at();

alter table public.profiles enable row level security;
alter table public.user_brackets enable row level security;

drop policy if exists "profiles are readable as public player identity" on public.profiles;
create policy "profiles are readable as public player identity"
on public.profiles
for select
to anon, authenticated
using (true);

drop policy if exists "users can insert their own profile" on public.profiles;
create policy "users can insert their own profile"
on public.profiles
for insert
to authenticated
with check ((select auth.uid()) = id);

drop policy if exists "users can update their own profile" on public.profiles;
create policy "users can update their own profile"
on public.profiles
for update
to authenticated
using ((select auth.uid()) = id)
with check ((select auth.uid()) = id);

drop policy if exists "users can delete their own profile" on public.profiles;
create policy "users can delete their own profile"
on public.profiles
for delete
to authenticated
using ((select auth.uid()) = id);

drop policy if exists "users can read their own brackets" on public.user_brackets;
create policy "users can read their own brackets"
on public.user_brackets
for select
to authenticated
using ((select auth.uid()) = user_id);

drop policy if exists "public can read submitted public brackets" on public.user_brackets;
create policy "public can read submitted public brackets"
on public.user_brackets
for select
to anon, authenticated
using (
  visibility = 'public'
  and status in ('submitted', 'locked')
);

drop policy if exists "users can insert their own brackets" on public.user_brackets;
create policy "users can insert their own brackets"
on public.user_brackets
for insert
to authenticated
with check ((select auth.uid()) = user_id);

drop policy if exists "users can update their own brackets" on public.user_brackets;
create policy "users can update their own brackets"
on public.user_brackets
for update
to authenticated
using ((select auth.uid()) = user_id)
with check ((select auth.uid()) = user_id);

drop policy if exists "users can delete their own brackets" on public.user_brackets;
create policy "users can delete their own brackets"
on public.user_brackets
for delete
to authenticated
using ((select auth.uid()) = user_id);
