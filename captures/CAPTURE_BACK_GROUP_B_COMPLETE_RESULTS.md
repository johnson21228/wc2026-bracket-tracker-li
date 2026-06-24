# Capture Back: Group B Complete Results

## Intent
Capture the completed Group B final matchday results from June 24, 2026.

## Results captured
- Group B: Switzerland 2-1 Canada
- Group B: Bosnia-Herzegovina 3-1 Qatar

## Data updates
- `site/data/current/group_matches.json` marks the two June 24 Group B rows final and fills scores and player-facing summaries.
- `site/data/current/group_standings.json` recalculates Group B and refreshes the provisional third-place table.
- `source/text/group_b_result_evidence_20260624.json` records public score evidence URLs.

## Group B table after capture
1. Switzerland — 7 points, +4 goal difference
2. Canada — 4 points, +5 goal difference
3. Bosnia and Herzegovina — 4 points, -1 goal difference
4. Qatar — 1 point, -8 goal difference

## Boundary
This capture intentionally does not add YouTube highlight links. It is a score-only result catch-up.

## ID note
The existing checked-in `espnMatchId` values were preserved. Current ESPN evidence IDs are stored in `currentEvidenceMatchId` to avoid casually rewriting fixture IDs.
