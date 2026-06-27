# Capture Back: Site-Owned Official Truth

## Outcome

Official tournament truth is now defined as site-owned data.

## Decision

R32 occupants and all official results will be stored in the site/repo.

The site will not use a Supabase Admin_/official entry row as the source of official truth.

## Boundary

Supabase remains for player data only:

- identity/profile
- joined player state
- player bracket picks

Standings are computed, not stored. Score, Max Possible, and rank are derived from player picks plus site-owned official truth.

## Follow-up

Remove conflicting LI and remove runtime code that loads official truth from a Supabase Admin_/official row.
