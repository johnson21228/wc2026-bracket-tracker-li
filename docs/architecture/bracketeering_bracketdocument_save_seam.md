# Bracketeering BracketDocument save seam

Bracketeering persists user picks by saving the canonical runtime `BracketDocument` through a repository/store boundary.

```text
User makes pick
→ update canonical BracketDocument
→ BracketRepository.saveUserBracket(document)
→ LocalStorageBracketStore.saveUserBracket(document)
```

The later signed-in flow keeps the same runtime document and changes only the store:

```text
User makes pick
→ update canonical BracketDocument
→ BracketRepository.saveUserBracket(document)
→ SupabaseBracketStore.saveUserBracket(document)
→ user_brackets.picks_json
```

UI and controller code should not know whether persistence is local browser storage or Supabase/Postgres. That choice belongs behind the repository/store seam.

Before Supabase implementation, anonymous play persists through `LocalStorageBracketStore`.

`LocalStorageBracketStore` stores the canonical `BracketDocument` fields: `schemaVersion`, `gameId`, `status`, `expectedPickCount`, `updatedAt`, and `picksBySlot`.

After Supabase setup, signed-in users will route the same document to `SupabaseBracketStore`, where it becomes `user_brackets.picks_json`.

Supabase must not own board rendering, pick menu rules, advancement behavior, or runtime model mutation.

Key invariant: Same BracketDocument. Different store.
