# Card 1001: Polish signed-in identity UI without profile store

## Context

Bracketeering Supabase Auth now works end-to-end.

The site currently recognizes a signed-in Supabase session and changes the upper-right control from “Sign in to save” to “Signed in”.

The current signed-in UI is correct but too generic. It does not help the player understand which account is active or what the current storage state means.

## Scope

This is a UI-only identity polish.

Do not add Supabase profile SQL.
Do not add `ProfileStore`.
Do not change `BracketStore`, `RemoteBracketStore`, `SupabaseBracketStore`, `BracketDocument`, or `picksBySlot`.
Do not enable remote bracket writes.
Do not change game data, pick data, match data, bracket slot data, or pick validity behavior.

## Design target

When signed out:

- upper-right control remains “Sign in to save”

When signed in:

- upper-right control should show a clearer compact signed-in state
- the account panel should show the signed-in email as private account identity
- the panel should clearly explain that bracket saving is not enabled yet
- the panel should avoid implying that the email is the public player name
- the panel may mention that public player names will be added later through a Supabase-backed profile

## Suggested copy

Compact signed-in button:

- “Signed in”

Account panel signed-in content:

- “Signed in”
- “Account: {email}”
- “This email is used for login.”
- “Your public player name will be added later.”
- “Bracket saving is not enabled yet; this browser is still using local play.”
- “Sign out”

## Boundary

`SupabaseAuthService` remains responsible for session/auth state.

`SupabaseIdentitySurface` remains the site-owned UI shell for sign-in/sign-out and session display.

No profile persistence is introduced in this card.

No bracket persistence is introduced in this card.

## Acceptance checks

- Anonymous/local play still works.
- Existing Supabase sign-in still works.
- Existing Supabase sign-out still works.
- After refresh with an active Supabase session, the UI still renders signed-in state.
- Signed-in panel shows the private account email only as account/login identity.
- Signed-in panel does not label email as public player name.
- Signed-in panel says bracket saving is not enabled yet.
- `BracketStore` / `BracketDocument` / pick write pipeline are unchanged.
- `make verify` passes.
- `make pack` passes.
