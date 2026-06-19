-- Draft RLS policies for Bracketeering Pub shared player pick visibility.
-- Status: NOT APPLIED unless captured dashboard evidence says otherwise.
-- This supersedes the earlier private-only owner-select policy.
-- Review before running. Contains no secrets.

alter table public.profiles enable row level security;
alter table public.user_brackets enable row level security;

drop policy if exists "profiles_select_authenticated" on public.profiles;
create policy "profiles_select_authenticated"
on public.profiles
for select
to authenticated
using (true);

drop policy if exists "profiles_insert_own" on public.profiles;
create policy "profiles_insert_own"
on public.profiles
for insert
to authenticated
with check (id = auth.uid());

drop policy if exists "profiles_update_own" on public.profiles;
create policy "profiles_update_own"
on public.profiles
for update
to authenticated
using (id = auth.uid())
with check (id = auth.uid());

drop policy if exists "user_brackets_select_own_or_shared" on public.user_brackets;
create policy "user_brackets_select_own_or_shared"
on public.user_brackets
for select
to authenticated
using (
  user_id = auth.uid()
  or visibility = 'public'
  or submitted_at is not null
  or locked_at is not null
);

drop policy if exists "user_brackets_insert_own" on public.user_brackets;
create policy "user_brackets_insert_own"
on public.user_brackets
for insert
to authenticated
with check (user_id = auth.uid());

drop policy if exists "user_brackets_update_own_unsubmitted" on public.user_brackets;
create policy "user_brackets_update_own_unsubmitted"
on public.user_brackets
for update
to authenticated
using (
  user_id = auth.uid()
  and submitted_at is null
  and locked_at is null
)
with check (
  user_id = auth.uid()
  and submitted_at is null
  and locked_at is null
);

-- Delete is intentionally omitted for the MVP.
-- Add only after an explicit account bracket reset/delete behavior is designed.
