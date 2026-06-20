-- Draft schema for Bracketeering Pub account-backed bracket storage.
-- Status: NOT APPLIED unless captured dashboard evidence says otherwise.
-- This finalizes the SQL target against the Pages-owned canonical BracketDocument.
-- Review before running. Contains no secrets.

create table if not exists public.profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  display_name text,
  avatar_url text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  constraint profiles_display_name_length_check check (
    display_name is null or char_length(display_name) between 1 and 80
  ),
  constraint profiles_avatar_url_length_check check (
    avatar_url is null or char_length(avatar_url) <= 2048
  )
);

create table if not exists public.user_brackets (
  user_id uuid not null references auth.users(id) on delete cascade,
  game_id text not null,
  picks_json jsonb not null,
  visibility text not null default 'private',
  submitted_at timestamptz,
  locked_at timestamptz,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  primary key (user_id, game_id),
  constraint user_brackets_game_id_check check (game_id in ('game1', 'game2')),
  constraint user_brackets_visibility_check check (visibility in ('private', 'public', 'room')),
  constraint user_brackets_picks_json_object_check check (jsonb_typeof(picks_json) = 'object'),
  constraint user_brackets_bracketdocument_required_fields_check check (
    picks_json ? 'schemaVersion'
    and picks_json ? 'gameId'
    and picks_json ? 'status'
    and picks_json ? 'expectedPickCount'
    and picks_json ? 'updatedAt'
    and picks_json ? 'picksBySlot'
  ),
  constraint user_brackets_bracketdocument_type_check check (
    jsonb_typeof(picks_json -> 'schemaVersion') = 'number'
    and jsonb_typeof(picks_json -> 'gameId') = 'string'
    and jsonb_typeof(picks_json -> 'status') = 'string'
    and jsonb_typeof(picks_json -> 'expectedPickCount') = 'number'
    and jsonb_typeof(picks_json -> 'picksBySlot') = 'object'
  ),
  constraint user_brackets_bracketdocument_game_match_check check (
    picks_json ->> 'gameId' = game_id
  ),
  constraint user_brackets_bracketdocument_status_check check (
    picks_json ->> 'status' in ('draft', 'submitted', 'locked')
  ),
  constraint user_brackets_locked_requires_submitted_check check (
    locked_at is null or submitted_at is not null
  )
);

create index if not exists user_brackets_game_id_idx
  on public.user_brackets (game_id);

create index if not exists user_brackets_visibility_idx
  on public.user_brackets (visibility);

create index if not exists user_brackets_submitted_at_idx
  on public.user_brackets (submitted_at);

create index if not exists user_brackets_locked_at_idx
  on public.user_brackets (locked_at);

create or replace function public.set_updated_at()
returns trigger
language plpgsql
as $$
begin
  new.updated_at = now();
  return new;
end;
$$;

create or replace function public.prevent_user_bracket_finalized_mutation()
returns trigger
language plpgsql
as $$
begin
  if old.locked_at is not null then
    raise exception 'locked brackets cannot be updated';
  end if;

  if new.locked_at is not null and new.submitted_at is null then
    new.submitted_at = coalesce(old.submitted_at, now());
  end if;

  if old.submitted_at is not null then
    if new.user_id is distinct from old.user_id then
      raise exception 'submitted bracket owner cannot change';
    end if;
    if new.game_id is distinct from old.game_id then
      raise exception 'submitted bracket game cannot change';
    end if;
    if new.picks_json is distinct from old.picks_json then
      raise exception 'submitted bracket picks_json cannot change';
    end if;
  end if;

  return new;
end;
$$;

drop trigger if exists set_profiles_updated_at on public.profiles;
create trigger set_profiles_updated_at
before update on public.profiles
for each row
execute function public.set_updated_at();

drop trigger if exists prevent_user_bracket_finalized_mutation on public.user_brackets;
create trigger prevent_user_bracket_finalized_mutation
before update on public.user_brackets
for each row
execute function public.prevent_user_bracket_finalized_mutation();

drop trigger if exists set_user_brackets_updated_at on public.user_brackets;
create trigger set_user_brackets_updated_at
before update on public.user_brackets
for each row
execute function public.set_updated_at();

alter table public.profiles enable row level security;
alter table public.user_brackets enable row level security;
