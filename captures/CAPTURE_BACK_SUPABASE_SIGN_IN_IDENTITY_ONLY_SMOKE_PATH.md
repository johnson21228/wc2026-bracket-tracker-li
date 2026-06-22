# Capture Back: Supabase sign-in identity-only smoke path

## Intent

Enable the existing Supabase sign-in UI so the authorization experience can be tested without activating remote bracket persistence.

## Applied change

Updated:

- `site/index.html`
- `site/js/identity/SupabaseIdentitySurface.js`
- `site/js/services/SupabaseAuthService.js`
- `Makefile`
- `MAP.md`

Added:

- `tools/verify_wc2026_supabase_sign_in_identity_only_smoke_path.py`
- `cards/275_enable_supabase_sign_in_identity_only_smoke_path_card.md`
- `docs/architecture/bracketeering_supabase_sign_in_identity_only_smoke_path.md`
- `li/world_cup/supabase_sign_in_identity_only_smoke_path_rule.md`

## Runtime boundary

This enables sign-in UI only.

It does not activate remote bracket persistence.

It does not route picks to `user_brackets`.

It keeps `BracketRepository` on `LocalStorageBracketStore`.

## Player-facing posture

Players may play without signing in.

Sign-in is optional while online save is prepared.

Signed-in players still use local browser bracket persistence until a later explicit remote-store activation CB.
