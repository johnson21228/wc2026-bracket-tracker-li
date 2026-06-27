# Capture Back: Info Panel Copy Polish

## Intent

Polish the player-facing Info panel copy for grammar and readability without changing gameplay, scoring, persistence, or official truth behavior.

## Runtime change

The Info panel now says:

- “First, register to join the “Pool.””
- “Using Google sign-in helps you avoid having to find an email that might go to your spam folder.”
- “You will need to choose your player name.”
- “There is no tiebreaker at the moment.”

## Boundary

This is copy-only. The bracket model, R32 official truth, Supabase-backed player standings, scoring weights, and pick behavior are unchanged.

## Verification

The existing Info panel verifiers are updated to require the polished copy and reject stale two-part/group-stage player instructions.
