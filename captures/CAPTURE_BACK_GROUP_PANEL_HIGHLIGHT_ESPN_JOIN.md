# Capture Back: Repair group panel highlight ESPN join

## Context

June 20/21 match results and highlight links are already captured, verified, committed, pushed, and published.
Live browser checks confirmed that `data/current/match_highlights.json` loads from the actual Pages site and contains the four new highlight records keyed by ESPN match ID.

## Problem

The group panel UI showed updated scores but did not render highlight links for the newly completed matches.
The data join worked manually in the browser when using `group_matches.json` `espnMatchId` to index `match_highlights.json`.

## Diagnosis

`site/js/mvc/model.js` loaded the highlight map correctly, but attached highlights to group match records with a matchId-only lookup.
That failed for current highlight records because `match_highlights.json` is keyed by ESPN IDs such as `66456972`, while the Workbench match IDs are strings such as `GS-2026-06-20-F3`.

## Change

The model now resolves match highlights by:

1. `match.espnMatchId`
2. fallback to `match.matchId`

The View remains unchanged: it renders `match.highlight.url` when the model supplies it.

## Acceptance

- June 20/21 completed match cards can receive highlight links through ESPN IDs.
- Existing matchId-keyed highlight records remain supported through fallback.
- Scores, standings, match IDs, and highlight JSON shape are unchanged.
- `make verify` includes a dedicated verifier for the ESPN-ID join.
