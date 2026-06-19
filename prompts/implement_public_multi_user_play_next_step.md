# Prompt: Implement Public Multi-User Play Next Step

Use this prompt after the public multi-user play LI is captured.

Read the current repo first. Then implement the next smallest card in order:

1. Card 211: define canonical public-play pick-state storage
2. Card 212: route local storage through canonical pick-state
3. Card 213: define remote bracket store contract
4. Card 214: add signed-in user UI shell
5. Card 215+: backend work only after local storage model is stable

Do not add Supabase or backend secrets until the local canonical storage path is verified.

Preserve the site-running invariant: the site must continue to load and work in anonymous local mode, and `make verify` plus `make pack` must pass.
