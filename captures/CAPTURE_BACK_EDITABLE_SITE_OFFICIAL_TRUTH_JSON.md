# Capture Back: Editable Site Official Truth JSON

## Outcome

The official results data workflow is now captured.

## Rule

The site will store official R32 occupants and official knockout results in:

`site/data/current/official_truth.json`

## Contract

The file keeps the old Admin_/official row payload shape:

- `tournamentId`
- `gameId`
- `picksBySlot`

The migration is source-only:

- old: Supabase Admin_/official `picks_json.picksBySlot`
- new: site JSON `picksBySlot`

## Tournament workflow

The JSON is edited as the tournament progresses.

- Add R32 occupants as they are decided.
- Add R16 winners when R32 games finish.
- Add R8/QF winners when R16 games finish.
- Add R4/SF winners when QF games finish.
- Add R2/Final-side winners when SF games finish.
- Add Champion when the final is complete.

## Standings

Player standings are computed from:

- Supabase player picks
- site-owned official truth

Standings rows, Score, Max Possible, and rank are not stored as authority.
