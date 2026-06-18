# Group-stage full match time model

This capture fills the full 72-match group-stage schedule with explicit kickoff time fields.

The previous model had times for the currently active subset but did not have times in the poster-derived 72-match schedule. That allowed future group panel rows to render `Time TBD` even when schedule evidence existed.

The model now carries:

- `kickoffLocal`
- `kickoffET`
- `timezone`
- `timeSource`
- `timeSourceUrl`
- `timeConfidence`
- `espnMatchId`

The source evidence is stored in `source/text/group_match_time_evidence_20260618.json`.
