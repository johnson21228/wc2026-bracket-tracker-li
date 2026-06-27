# Rule: Editable Site Official Truth JSON

Official WC2026 tournament truth is edited as versioned site JSON.

## File

The canonical site-owned official truth file is:

`site/data/current/official_truth.json`

## Contract

The file must preserve the same effective payload contract previously supplied by the Supabase `Admin_/official` official row:

- `tournamentId`
- `gameId`
- `picksBySlot`

Runtime migration should replace the source of the official payload, not invent a second official truth model.

Old source:

- Supabase Admin_/official row
- `picks_json.picksBySlot`

New source:

- `site/data/current/official_truth.json`
- `picksBySlot`

## Partial truth

The file may be partial.

Not all R32 occupants are known at first. Not all knockout winners are known at first.

Unknown or pending truth may be represented by:

- an absent slot record, or
- a slot record with no usable `teamId`

The scorer and board must treat missing official `teamId` as unresolved, not as player-owned truth.

## R32 occupants

R32 occupant records are official input records.

Normal players read R32 occupants from site-owned official truth. Normal players do not author R32 occupants.

R32 occupant records use canonical R32 slot IDs such as:

- `L-R32-01`
- `L-R32-02`
- `R-R32-01`

## Knockout results

Official knockout result records use the same canonical winner slot IDs used by player picks and scoring:

- `L-R16-01`
- `L-QF-01`
- `L-SF-01`
- `FINAL-LEFT`
- `FINAL-RIGHT`
- `CHAMPION`

A resolved official result record should expose the winning team through the same record shape already understood by the runtime, especially `teamId`.

## Standings

Player standings are computed, not stored.

The standings computation reads:

- player picks from Supabase
- official truth from `site/data/current/official_truth.json`

Then it computes:

- Score
- Max Possible
- rank
- standings rows

## Operating workflow

As the tournament progresses:

1. Edit `site/data/current/official_truth.json`.
2. Add newly known R32 occupants.
3. Add newly resolved R16/R8/R4/R2/Champion winners.
4. Run verification.
5. Commit and publish.

This replaces the old Admin Supabase editor workflow with a Git-versioned official truth data workflow.
