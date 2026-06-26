# Hydrate only Supabase Admin R32 into player picks rule

Copy ONLY R32 entrant slots from Supabase Admin_/official into player BracketDocument picks.

Player-visible R32 may be stored in player `picksBySlot` for rendering, scoring, and R16++ preselection compatibility, but it is not player-authored. Hydrated R32 records must carry Admin_/official source/authority metadata and `playerAuthored: false`.

Do not copy Admin_/official R16, QF, SF, Final, Champion, or third-place picks into player documents. Player R16++ picks remain player-owned.

Do not copy R32 from localStorage, static JSON, bundled data, or stale player documents. If Supabase Admin R32 is missing, keep player R32 unset/fail-closed.
