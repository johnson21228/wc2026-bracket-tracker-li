# BracketDocument save seam before Supabase rule

Bracketeering must learn to save the canonical `BracketDocument` before live Supabase persistence is implemented.

Required sequence:

1. Pages runtime updates the canonical `BracketDocument`.
2. Pages runtime saves through `BracketRepository` or an equivalent repository boundary.
3. The current concrete store is `LocalStorageBracketStore`.
4. A future signed-in store may be `SupabaseBracketStore`.

Controllers and board views must not call Supabase directly. They should not contain `supabase.from(...).upsert(...)` or similar backend persistence calls.

The runtime invariant is: Same BracketDocument. Different store.

Out of scope: Supabase client code, Supabase Auth UI, dashboard SQL execution, RLS policies, and live remote persistence.
