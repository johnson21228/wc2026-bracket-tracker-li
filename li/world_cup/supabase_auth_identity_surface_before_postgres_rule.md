# Supabase Auth identity surface before Postgres persistence rule

The Bracketeering site may implement a real Supabase Auth sign-in/sign-out surface before Supabase/Postgres BracketDocument persistence is implemented.

This surface must be honest:

```text
Signed in
Local bracket for now
```

until `SupabaseBracketStore` writes the canonical BracketDocument to `user_brackets.picks_json`.

Supabase Auth can be connected before Postgres persistence. The site must not imply that picks are saved to Supabase until the remote store is implemented and verified.

The board, pick menu, and controller must not call Supabase directly. Auth surface code may talk to Supabase Auth. Bracket persistence must remain behind BracketRepository/store boundaries.
