# Card 132: Repair Site Pick Store Candidate Fallback

## Claim

The site bracket pick store must feed candidate resolution without hiding existing R32 picks.

## Acceptance Criteria

- The use-site-store layer migrates legacy picks on install.
- `r16CandidateTeams` can find upstream R32 picks stored under canonical slot IDs.
- `r16CandidateTeams` can find upstream R32 picks stored under manifest aliases such as `R32-L-M1A`.
- Opening an R16 menu can show two candidates after R32 picks exist.

## Files

- `site/game1/index.html`
- `tools/verify_wc2026_site_pick_store_candidate_fallback_patch.py`
