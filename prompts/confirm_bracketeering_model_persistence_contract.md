# Prompt: Confirm Bracketeering Model Persistence Contract

Use this prompt before applying Supabase SQL or implementing RemoteBracketStore.

```text
Confirm the Bracketeering Model Persistence Contract in the wc2026-bracket-tracker-li Workbench.

Context:
- Bracketeering is served from GitHub Pages.
- Pages owns View, Controller, and runtime JavaScript game state.
- Supabase/Postgres should provide durable Model persistence.
- No Supabase SQL has been applied yet.
- Shared pick visibility is a future requirement.

Task:
Confirm the saved bracket model that moves between the Pages runtime and durable storage. Keep the board/controller behind the BracketStore boundary.

Core invariant:
WRITE is private.
READ can be shared when game rules allow it.

Scope:
- Identify the canonical bracketState JSON shape.
- Identify required persisted fields:
  - user_id
  - game_id
  - picks_json
  - visibility
  - submitted_at
  - locked_at
  - created_at
  - updated_at
- Confirm draft vs submitted vs locked meaning.
- Confirm draft data is private by default.
- Confirm shared reads only when visibility/submission/lock rules allow.

Acceptance:
- The Bracketeering WB has a clear durable model contract.
- The Supabase SQL target matches that contract.
- No private-only owner-read assumption remains as the final target.
- The implementation remains a narrow model-persistence seam task.
```
