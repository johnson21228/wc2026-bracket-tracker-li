# RESEARCH PENDING RESULT UPDATES JSON

Use the generated `outputs/research/pending_result_updates_*.json` file as the only candidate list.

For each candidate:

1. Inspect guardrail hits before web searching.
2. Search only for that match's final result and official/rightsholder highlight link.
3. Add evidence records into the candidate JSON.
4. Set classification to exactly one of `PATCH`, `WATCH`, `WAIT`, or `CONFLICT`.
5. Fill `proposedPatch` only for `PATCH` entries.
6. Do not modify repo data files yet.

Preferred score sources:

1. FIFA official scores / fixtures / match pages
2. FIFA official schedule / fixtures-results pages
3. ESPN World Cup fixtures/results pages
4. Reuters/AP-style match reports
5. FOX Sports match pages

Preferred highlight sources:

1. FIFA official
2. FOX Sports / FOX Soccer
3. official broadcaster or rights-holder channels
4. official tournament channel

Output the completed JSON plus a short summary table.
