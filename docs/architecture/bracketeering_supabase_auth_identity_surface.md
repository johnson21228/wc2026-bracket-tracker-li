# Bracketeering Supabase Auth identity surface

## Summary

The Bracketeering site has a visible upper-right identity/status surface that can connect to Supabase Auth before BracketDocument persistence is moved to Supabase/Postgres.

This is not a custom auth system. Supabase owns authentication, sessions, and the authenticated user id. The Pages site owns only the visible surface that lets a player know whether they are anonymous/local or signed in.

## Runtime sequence for this card

```text
Open site
→ Pages app starts
→ SupabaseAuthService checks public config
→ if configured, Supabase Auth session is read
→ identity surface renders signed-out or signed-in state
→ BracketDocument persistence remains localStorage
```

## Signed-out state

```text
[Sign in to save]
Local bracket
```

If Supabase config is not enabled yet, the surface reports that Supabase Auth is not configured and keeps the local bracket path active.

## Signed-in state before Postgres persistence

```text
Signed in
Local bracket for now
[Sign out]
```

This wording is deliberate. Auth can work before `user_brackets.picks_json` is wired. Until `SupabaseBracketStore` exists, a signed-in player is authenticated but their active BracketDocument still persists locally.

## Future signed-in state after SupabaseBracketStore

```text
Signed in
Saved to Supabase
Draft
```

## Boundary

```text
Supabase owns:
- Auth
- session
- current user id
- secure token handling

Pages owns:
- sign-in button placement
- signed-in/signed-out display
- status text
- sign-out action

BracketRepository owns:
- save/load boundary

LocalStorageBracketStore owns:
- current anonymous and pre-Postgres persistence
```

## Invariant

Same BracketDocument. Different store.

This card implements only the Auth/status surface. The store remains localStorage until the Postgres SQL/RLS has been applied and `SupabaseBracketStore` is implemented.

## Current Supabase public config

The Pages site is configured with the current Supabase browser-safe publishable key terminology.

Confirmed dashboard settings:

- Site URL: `https://johnson21228.github.io/wc2026-bracket-tracker-li/`
- Redirect URL: `https://johnson21228.github.io/wc2026-bracket-tracker-li/`

Configured site values:

- Project URL: `https://tkjqsegszveugdvoeits.supabase.co`
- Publishable key: browser-safe publishable key in `site/js/config/supabase.public.js`

Do not put service_role keys, database passwords, JWT secrets, or secret keys in site code.

This card still does not implement Supabase/Postgres bracket persistence. LocalStorage remains the active BracketDocument store until SupabaseBracketStore is implemented.
