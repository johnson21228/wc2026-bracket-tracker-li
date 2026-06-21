# Card 235: Capture June 20/21 Results and Highlights

## Intent
Capture the user-provided June 20/21 Group E/F final scores and highlight URLs without changing unrelated runtime behavior.

## Change
- Marked Netherlands 5-1 Sweden final.
- Marked Germany 2-1 Côte d’Ivoire final.
- Marked Ecuador 0-0 Curaçao final.
- Marked Tunisia 0-4 Japan final.
- Added the four corresponding YouTube highlight links.
- Refreshed Group E/F standings and the third-place table from current checked-in results.
- Stored evidence at `source/text/group_result_evidence_20260621.json`.

## Acceptance
- The four target match rows are final with the expected scores.
- The four target ESPN match IDs have highlight entries with HTTPS URLs.
- Existing IDs and canonical team keys are preserved.
- Verification is wired into `make verify`.
