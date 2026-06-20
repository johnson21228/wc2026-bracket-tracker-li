# Card 231: Implement Supabase Auth identity UI surface before Postgres persistence

## Intent

Make the Bracketeering site visibly capable of signing a player in and out with Supabase Auth before Postgres BracketDocument persistence is connected.

This card implements the first runtime step after the identity surface definition:

1. Implement Supabase Auth identity UI surface.
2. Apply Postgres SQL/RLS.
3. Implement SupabaseBracketStore save/load.
4. Change signed-in status from `Local bracket for now` to `Saved to Supabase`.

## Scope

- Add a visible upper-right identity/status surface.
- Add a Supabase browser Auth service seam.
- Add a public Supabase config seam for GitHub Pages.
- Support email magic-link sign-in through Supabase Auth.
- Detect the current Supabase session at startup.
- Listen for Supabase Auth state changes.
- Support sign-out.
- Keep localStorage as the active BracketDocument store.
- Show honest status text: `Local bracket for now` while Postgres persistence is not connected.

## Explicitly out of scope

- Do not add `SupabaseBracketStore` yet.
- Do not write to `user_brackets` yet.
- Do not read from `profiles` yet.
- Do not build a custom login system.
- Do not build full profile/account management.
- Do not build public player-pick views.
- Do not let board/menu/controller code call Supabase.

## Acceptance

- The site shows an upper-right `[Sign in to save]` identity surface.
- When Supabase config is missing, the surface reports configuration needed and local play continues.
- When Supabase config is present, the surface can request a Supabase magic link.
- On a valid Supabase session, the surface shows signed-in status.
- Sign-out clears the Supabase session.
- Status remains honest: signed-in still says `Local bracket for now` until `SupabaseBracketStore` is implemented.
- `make verify` passes.
