# Card 274: Add guarded Supabase remote smoke path without changing public runtime

## Status

Done.

## Goal

Allow a manual developer smoke test against Supabase after SQL application while preserving the public runtime boundary.

## Acceptance

- A terminal-only smoke harness exists.
- It requires explicit environment opt-in.
- It is not run by normal `make verify`.
- It is not imported by public runtime.
- Remote mode remains inactive unless a future CB explicitly activates it.
