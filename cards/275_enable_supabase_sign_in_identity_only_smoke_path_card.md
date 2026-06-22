# Card 275: Enable Supabase sign-in identity-only smoke path

## Status

Done.

## Goal

Turn on the sign-in UI so the authorization flow can be tested while preserving local bracket persistence.

## Acceptance

- Identity surface is no longer disabled by `data-auth-disabled="true"`.
- Magic-link sign-in and sign-out are available through the existing Supabase Auth service.
- Player-facing copy says sign-in is optional and local bracket remains active.
- `BracketRepository` still defaults to `LocalStorageBracketStore`.
- No public runtime path writes to `user_brackets`.
- Remote store activation guard remains fail-closed.
