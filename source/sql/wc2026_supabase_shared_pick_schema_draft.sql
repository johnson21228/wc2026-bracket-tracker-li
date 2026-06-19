-- Draft schema for Bracketeering Pub account-backed bracket storage.
-- Status: NOT APPLIED unless captured dashboard evidence says otherwise.
-- This supersedes the earlier private-only user_brackets/status-only target.
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
  picks_json jsonb not null default '{}'::jsonb,
  visibility text not null default 'private',
  submitted_at timestamptz,
  locked_at timestamptz,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  primary key (user_id, game_id),
  constraint user_brackets_game_id_check check (game_id in ('game1', 'game2')),
  constraint user_brackets_visibility_check check (visibility in ('private', 'public', 'room')),
  constraint user_brackets_picks_json_object_check check (jsonb_typeof(picks_json) = 'object')
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

drop trigger if exists set_profiles_updated_at on public.profiles;
create trigger set_profiles_updated_at
before update on public.profiles
for each row
execute function public.set_updated_at();

drop trigger if exists set_user_brackets_updated_at on public.user_brackets;
create trigger set_user_brackets_updated_at
before update on public.user_brackets
for each row
execute function public.set_updated_at();

alter table public.profiles enable row level security;
alter table public.user_brackets enable row level security;
