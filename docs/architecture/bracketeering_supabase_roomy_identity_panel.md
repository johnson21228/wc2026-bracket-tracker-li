# Bracketeering Supabase Roomy Identity Panel

The sign-in surface is intentionally identity-only. It proves Supabase Auth wiring without changing the bracket persistence authority.

The player-facing model is:

1. Play locally without signing in.
2. Use the compact Sign in button to open an identity panel.
3. Request an email magic link from the panel.
4. Continue using local bracket persistence until the remote store is explicitly activated in a later card.

The panel gives enough room for email entry, status text, errors, and later signed-in profile actions. It also disables repeated magic-link submission briefly to avoid accidental Supabase email rate-limit loops.
