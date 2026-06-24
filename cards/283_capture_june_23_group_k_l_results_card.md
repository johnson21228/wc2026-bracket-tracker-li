# Card 283: Capture June 23 Group K/L Results

## Goal
Patch the current data for played June 23 matches that still appeared scheduled in the tracker.

## Scope
- Portugal 5-0 Uzbekistan
- England 0-0 Ghana
- Panama 0-1 Croatia
- Colombia 1-0 Congo DR

## Acceptance
- The four match rows are `status: final`.
- Scores and summaries match public evidence.
- Groups K and L standings reflect two played matches per team.
- The third-place table reflects Croatia as Group L third and the updated Group K third-place state.
- The pack keeps fixture IDs stable and records current evidence IDs separately.

## Verification
Run:

```bash
python3 tools/verify_wc2026_june_23_group_k_l_results.py
make verify
```
