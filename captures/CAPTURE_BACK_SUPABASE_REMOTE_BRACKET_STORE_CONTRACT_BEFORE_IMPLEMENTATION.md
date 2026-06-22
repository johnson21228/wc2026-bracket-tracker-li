# Capture Back: Supabase remote bracket store contract before implementation

This capture defines the contract for the future Supabase-backed remote bracket store.

It confirms:

- no `SupabaseBracketStore` is implemented by this CB
- no Supabase SQL is applied
- no public Supabase dashboard state is changed
- no runtime site behavior is changed
- View and Controller remain site-owned
- Supabase/Postgres provides durable Model persistence only
- future remote persistence must sit behind the bracket store/repository/session seam
- future remote store uses `loadUserBracket(userId)` and `saveUserBracket(bracketDocument)`
- only the active store is authoritative
- local and remote modes are separate storage modes
- one `user_brackets` row per player/game stores the full canonical `BracketDocument` in `picks_json`
- R32 lock must be preserved client-side and server-side
- View/Controller code must not call Supabase directly
