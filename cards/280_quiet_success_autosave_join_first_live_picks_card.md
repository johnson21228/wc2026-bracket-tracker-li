# Card 280: Quiet Success Autosave for Join-first Live Picks

## Intent

Remove persistent “Picks saved” UI from the Join-first live-picks flow.

## Why

The Join-first product model is:

Join → make picks → picks are live.

A persistent “Picks saved” message risks reintroducing manual save-state thinking.

## Acceptance

- Successful autosave clears quietly.
- “Saving…” remains available during active save.
- “Could not save — retrying” remains visible on failure.
- Save Picks / Load Saved controls do not return.
- Verification and pack pass.
