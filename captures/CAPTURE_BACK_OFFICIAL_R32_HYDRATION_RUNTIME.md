# Capture Back: Official R32 Hydration Runtime Boundary

## Change
Implemented the runtime/model boundary for official R32 hydration.

## Runtime/model only
This CB is runtime/model only. No UI copy cleanup: it does not perform UI copy cleanup, does not remove group-prediction language, and does not remove or rename Game 1/Game 2 labels.

## Behavior
- `Admin_/official` is the authority for R32 occupants.
- Non-admin player BracketDocuments may contain hydrated R32 occupant records.
- Hydrated R32 occupant records are marked with official source/authority and `playerAuthored: false`.
- The canonical model setter blocks non-admin player authoring of R32 entrant slots.
- Player-owned picks begin with R32 match winners and continue through later knockout rounds.
- Existing player knockout winner picks are preserved during hydration.

## Boundaries
Hydration is wired through creation, load, import, and save boundaries:
- creation via `createEmptyBracketDocument`
- load via `BracketRepository.loadUserBracket`
- import via the account import path ignoring R32 entrant authoring
- save via `BracketRepository.saveUserBracket` and the MVC Supabase autosave document builder

## Persistence
BracketDocument remains the persistence container.

Supabase row-per-user-per-game remains valid because each player row still stores one BracketDocument. The R32 occupant subfield is hydrated official data; the player-owned subfield remains knockout winner picks.

## Verification
- `python3 tools/verify_wc2026_official_r32_hydration_runtime.py`
- `make verify`
- `make pack`
