# Capture Back — June 27 final Group J/K/L results

## Intent

Update the checked-in World Cup 2026 group-stage data after the final Group J/K/L matchday, without changing bracket interaction behavior, R32 truth, pick locking, Supabase, or site UI code.

## Public score evidence applied

- Group J: Algeria 3-3 Austria.
- Group J: Jordan 1-3 Argentina.
- Group K: Colombia 0-0 Portugal.
- Group K: Congo DR 3-1 Uzbekistan.
- Group L: Panama 0-2 England.
- Group L: Croatia 2-1 Ghana.

## Files changed

- `site/data/current/group_matches.json` — six scheduled fixtures moved to `final` with checked scores and result source metadata.
- `site/data/current/group_standings.json` — Groups J/K/L and the contextual third-place table recomputed from final checked-in match evidence.
- `source/text/group_result_evidence_20260628.json` — compact source ledger for this data patch.
- `tools/verify_wc2026_june_27_final_group_results.py` — focused verifier for the match results, standings, and capture/card governance.

## Boundaries

- Do not change R32/pick interaction behavior.
- Do not update `official_truth.json` in this data-only patch.
- Do not infer FIFA R32 slot allocation from the contextual third-place table.
