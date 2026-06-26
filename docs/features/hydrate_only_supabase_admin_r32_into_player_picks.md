# Hydrate only Supabase Admin R32 into player picks

## Goal

Restore player-site R16++ preselection by materializing Supabase Admin_/official R32 occupants into each player BracketDocument, while copying no Admin later-round truth.

## Rule

Copy ONLY R32 entrant slots from Supabase Admin_/official into player picks.

Do not copy Admin_/official R16, QF, SF, Final, Champion, or third-place truth into a player bracket. Player R16++ picks remain player-owned and must survive hydration.

## Source boundary

The only valid copy source is Supabase Admin_/official. R32 must not be copied from localStorage, static JSON, bundled data, or stale player documents.

If Supabase Admin R32 is missing or unreadable, player R32 remains unset/fail-closed and R16++ preselection remains unavailable.

## Runtime behavior

On player load, login/join, import, save, or first local BracketDocument creation:

1. Strip stale player/local R32 values from player picks.
2. Load the Supabase Admin_/official official bracket document.
3. Copy only Admin R32 entrant slots into the player picks map.
4. Mark copied R32 entries with `source: "Admin_/official"`, `authority: "Admin_/official"`, `playerAuthored: false`, and `hydratedFrom: "Supabase:Admin_/official"`.
5. Preserve player-owned R16++ picks.

Rendering and R16++ preselection may then read from the hydrated player picks map for compatibility with the existing site path.
