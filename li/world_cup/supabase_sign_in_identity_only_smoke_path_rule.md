# Supabase sign-in identity-only smoke path rule

Supabase sign-in may be enabled before remote bracket persistence.

During this phase:

- login is optional
- Supabase Auth may identify the player
- sign-out must remain available
- bracket persistence must remain local browser storage
- `BracketRepository` must not instantiate `SupabaseBracketStore`
- public runtime must not write to `user_brackets`
- remote store activation guard must remain fail-closed

This phase tests authorization UX only.
