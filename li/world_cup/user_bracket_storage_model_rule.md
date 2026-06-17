# User bracket storage model rule

WC2026 bracket picks are stored as complete user bracket records.

Requirements:

- `Team.id` is the uppercase three-letter code.
- `PickValue.kind` is either `unpicked` or `team`.
- `teamId` values must be uppercase and match an existing `Team.id`.
- Every user bracket must include every `sitePickId`.
- Unpicked is explicit, not a missing key.
- FIFA bracket display order is a separate mapping layer.
