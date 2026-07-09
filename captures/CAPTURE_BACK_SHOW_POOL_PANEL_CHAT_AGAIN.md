# Capture Back: Show Pool Panel Chat Again

## Intent

Restore the Pool Chat entry point in the Pool panel after the temporary hiding patch.

## Decision

Show Pool Chat again on the public Bracketeering site.

## Why this is safe enough now

The existing chat implementation is session-scoped and presented as live broadcast chat. The current verifier guards that Pool Chat does not persist chat messages through Supabase tables.

## Boundary

This restores the visible Pool Chat surface. It does not add durable chat history, Supabase chat-table persistence, moderation tooling, or a broader public messaging contract.

## Verification expectation

- `make verify` should pass.
- The Pool panel should show the Chat button again.
- The Pool Chat verifier should return to checking the ephemeral live broadcast chat boundary.
