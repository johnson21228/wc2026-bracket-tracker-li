# Capture Back: Update All Missing Completed Group Results

## Decision

Update every completed group-stage match result that is missing from the site, rather than interviewing match-by-match.

This update pass should cover all completed matches currently missing from the local site data. It should not invent or pre-fill future matches that have not completed yet.

## Scope

The update pass is expected to patch completed missing finals through the currently completed groups and leave only the still-unplayed final Group J/K/L matches for a later pass.

## Remaining watch list

The final group-stage matches still needing completion/results are:

- Panama vs England
- Croatia vs Ghana
- Colombia vs Portugal
- DR Congo vs Uzbekistan
- Algeria vs Austria
- Jordan vs Argentina

## Implementation rule

For each completed missing match:

1. Patch the final score in `site/data/current/group_matches.json`.
2. Recompute affected group standings in `site/data/current/group_standings.json`.
3. Add or update evidence in `source/text/`.
4. Add a verifier for the result batch.
5. Run `make verify` and `make pack`.

Do not change R32/pick interaction behavior as part of this result update.
