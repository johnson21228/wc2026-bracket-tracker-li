# Capture Back: June 23 Group K/L Results

## Intent
Capture all June 23, 2026 group-stage matches in the uploaded tracker pack that had already been played but still had missing results.

## Results captured
- Group K: Portugal 5-0 Uzbekistan
- Group K: Colombia 1-0 Congo DR
- Group L: England 0-0 Ghana
- Group L: Panama 0-1 Croatia

## Data updates
- `site/data/current/group_matches.json` marks the four rows final and fills home/away scores and summaries.
- `site/data/current/group_standings.json` recalculates Groups K/L and the live third-place table from checked-in final matches.
- `source/text/group_result_evidence_20260624.json` records public score evidence URLs.

## Boundary
This capture intentionally does not add YouTube highlight links. It is a score-only result catch-up.

## ID note
The existing checked-in `espnMatchId` values were preserved. Current ESPN report/match evidence IDs are stored in `currentEvidenceMatchId` to avoid casually rewriting fixture IDs.
