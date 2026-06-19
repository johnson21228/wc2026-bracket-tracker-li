# Pending Result Updates JSON Workflow

This workflow separates result discovery from result patching.

Instead of asking an LLM to search the web and patch repo data in one step, generate a review artifact first:

```text
outputs/research/pending_result_updates_YYYYMMDD_HHMMSS.json
```

The generated JSON includes only matches that:

1. exist in `site/data/current/group_matches.json`,
2. are missing a final result,
3. have kickoff times far enough in the past to be likely completed, and
4. need research before patching.

The artifact includes candidate match ids, current repo state, missing fields, suggested searches, guardrail verifier hits, empty evidence slots, and a `proposedPatch` placeholder.

## Generate

```bash
cd /Users/stevejohnson/Developer/wc2026-bracket-tracker-li

python3 tools/generate_pending_result_updates.py
```

Optional repeatable run:

```bash
cd /Users/stevejohnson/Developer/wc2026-bracket-tracker-li

python3 tools/generate_pending_result_updates.py \
  --now 2026-06-19T08:00:00-04:00 \
  --likely-complete-minutes 150
```

## Research

Give the generated JSON to an LLM/web research pass. The research pass should fill `evidence`, classify each candidate as `PATCH`, `WATCH`, `WAIT`, or `CONFLICT`, and fill `proposedPatch` only for `PATCH` candidates.

## Patch

Patch only confirmed `PATCH` entries. Do not patch direct from the candidate generator. Repo verifier guardrails win unless the task is explicitly to revise the guardrail.
