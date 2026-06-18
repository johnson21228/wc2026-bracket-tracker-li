# Card 202: Capture Safe Group Result for Czechia South Africa

## Intent
Patch only the safe confirmed final group-stage result.

## Change
- Czechia 1-1 South Africa is marked final in current group matches.
- Group A standings are updated from confirmed final inputs.
- Switzerland vs Bosnia and Herzegovina remains unpatched because it was live/in-progress during the update decision.

## Acceptance
- Match 66456910 is final, 1-1.
- Match 66456922 is not patched as final by this card.
- Source evidence is stored in `source/text/group_result_evidence_20260618.json`.
- Verification is wired into `make verify`.
