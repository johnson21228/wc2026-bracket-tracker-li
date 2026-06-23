# Card 1000: Improve signed-in UI and introduce player display name profile target

## Context

Bracketeering Supabase Auth now works end-to-end for a verified-domain test account.

Confirmed chain:

- Bracketeering sign-in UI submits email to Supabase /otp
- Supabase Auth accepts the request
- Postmark delivers the confirmation email
- Email link redirects back to the site
- Browser stores the Supabase auth token
- The upper-right control changes to Signed in

## Current UX issue

The signed-in control only shows a generic “Signed in” state. That proves identity exists, but it does not yet help the player understand which account is active or how their player identity will appear to others.

## Product requirement

Players should eventually have a public player name/display name for Bracketeering. This display name should be the public identity shown in shared picks, standings, and leaderboard-style surfaces.

## Design decision

Player display name is a Supabase-backed profile field, not merely localStorage.

Reason:

- Supabase Auth email is private identity.
- Public player name is game/social identity.
- Other players will need to see display names when shared picks are enabled.
- Local storage may cache or stage the name, but must not be the durable source of truth.

## Target model

- auth.users owns private login identity.
- public.profiles or equivalent owns public player profile:
  - user_id references auth.users(id)
  - display_name text
  - created_at
  - updated_at
- bracket/pick rows later join or reference user_id and display profile name for shared read views.

## UI target

When signed out:

- upper-right control says “Sign in to save”

When signed in and profile display_name exists:

- upper-right control shows “Signed in: {display_name}” or compact equivalent
- account panel shows:
  - signed-in email, treated as private/account info
  - player name, treated as public display name
  - sign out action

When signed in and no profile display_name exists:

- upper-right control should invite setup, for example:
  - “Set player name”
  - or “Signed in”
- account panel should ask for a player name before shared/remote play is considered complete.

## Important UX copy

Make clear that:

- email is used for login
- player name is what other players may see
- bracket saving is not enabled until the RemoteBracketStore/Supabase persistence step is implemented

## Implementation boundary

- Pages site still owns View and Controller behavior.
- Supabase owns durable Model persistence for profile and later bracket data.
- Do not scatter Supabase profile calls through view code.
- Add or reuse a small profile/store seam such as ProfileStore or SupabaseProfileStore.
- Keep anonymous localStorage play intact.
- Do not enable remote bracket writes as part of this UI-only/profile-target change unless explicitly scoped.

## Acceptance checks

- Existing anonymous play still works.
- Existing sign-in flow still works.
- Signed-in state remains visible after refresh when Supabase session exists.
- Signed-in control no longer provides only a generic ambiguous state.
- UI copy distinguishes private email from public player name.
- No raw auth email is used as public display identity unless explicitly labeled as fallback/private.
- make verify passes.
- make pack passes.
