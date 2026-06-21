# Capture Back: June 20/21 Results and Highlight Links

## Change
Captured the June 20/21 FIFA World Cup 2026 Group E/F final-score and highlight-link update batch.

## Results captured
- Netherlands 5-1 Sweden — https://youtu.be/IRllRLrG7Sg
- Germany 2-1 Côte d’Ivoire — https://www.youtube.com/watch?v=xHtIzadh4Lg&pp=ygUHZ2VybWFueQ%3D%3D
- Ecuador 0-0 Curaçao — https://youtu.be/_JQLeADlzXM
- Tunisia 0-4 Japan — https://youtu.be/ATmlGGfCyBA

## Safety boundary
- Patched only the relevant Group E/F match records, highlight entries, standings refresh, and evidence/capture files.
- Preserved existing match IDs, ESPN IDs, team IDs, fixture fields, schedule fields, and local data shape.
- Preserved local canonical display spelling where the current match data already used `Côte d’Ivoire` and `Curaçao`.
- Did not change bracket logic, pick logic, Supabase work, board UI, or unrelated matches.

## Verification
Added `tools/verify_wc2026_june_20_21_results_and_highlights.py` and wired it into `make verify`.
