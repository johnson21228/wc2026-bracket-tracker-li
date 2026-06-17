# Legacy snapshots

This directory contains frozen legacy runtime snapshots for LI extraction only.

These files are evidence, not runtime authority.

Use them to inspect behavior that may need to be captured as Living Intent, tests, or canonical model/controller modules.

Do not:
- import these files into `site/index.html`
- use these files as generated release input
- preserve legacy localStorage keys as render truth
- add runtime fallback paths from canonical code into these snapshots

Current runtime truth should move to the canonical multiplayer pool model:

- `wc2026.pool.model.v1`
- player identity by hidden UUID
- rendered screen names are display metadata, not identity
- all picks keyed by player UUID
