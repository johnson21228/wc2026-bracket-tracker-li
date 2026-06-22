# Bracketeering Supabase sign-in identity-only smoke path

This step turns on Supabase Auth in the player-facing UI without changing bracket persistence.

## Why this comes before remote persistence

Authentication and persistence are separate concerns.

This allows the authorization experience to be tested first:

- email magic-link request
- email redirect back to the site
- session detection
- signed-in display
- sign out

All while bracket picks continue to save locally in the browser.

## Runtime boundary

Current identity-only path:

```text
player picks -> BracketRepository -> ActiveBracketSession(local) -> LocalStorageBracketStore -> browser localStorage
```

Future remote path, not activated by this step:

```text
signed-in player picks -> BracketRepository -> ActiveBracketSession(remote) -> SupabaseBracketStore -> public.user_brackets
```

## Player-facing copy

Players may play without signing in.

Sign-in is optional while online bracket saving is prepared.

Signed-in players should see that their bracket still saves locally for now.
