# UPDATE RESULTS Workflow

Use `prompts/update_results_from_web.md` when the user says `UPDATE RESULTS`.

The workflow is intentionally status-gated:

- `PATCH` means final score confirmed by a reliable source.
- `WATCH` means live/in progress; do not patch as final.
- `WAIT` means no reliable final source yet.
- `CONFLICT` means sources disagree; do not patch.

The prompt starts from repo data, searches only stale/missing candidate matches, and patches only confirmed finals.
