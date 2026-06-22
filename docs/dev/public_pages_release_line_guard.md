# Public Pages release-line guard

This document captures the release-line guard for keeping the public Bracketeering Pub GitHub Pages site stable while Supabase/Auth/storage preparation continues.

# Public Pages release-line guard for Supabase prep

The public GitHub Pages site must remain stable while Supabase/Auth/storage work is prepared.

## Core invariant

`main` is the public Pages release line.

Supabase/Auth/storage preparation work must happen on feature branches until intentionally approved and merged.

A Supabase prep branch is an integration/prep lane, not a public release lane.

## Current Supabase prep branch

`feature/supabase-prep-active-store-boundary` is the current Supabase preparation branch.

This branch may prepare language infrastructure, documents, verifiers, BracketDocument seams, active store seams, auth seams, and future storage seams.

It must not accidentally publish unfinished Supabase/Auth/storage behavior to the public Pages site.

## Merge and publish readiness

Do not merge Supabase-prep work to `main` until all of these are true:

1. `python3 tools/clean_repo_hygiene.py` passes.
2. `make verify` passes.
3. `make pack` passes.
4. Browser smoke test passes.
5. Local/browser play still works without Supabase.
6. Identity surface remains intentionally configured for the target release posture.
7. Supabase SQL/dashboard state is intentionally ready for the release, or explicitly not part of the release.
8. The public Pages publish risk is explicitly accepted.

## Publish tooling guard

`tools/force_pages_publish.py`, Pages snapshot tooling, or equivalent publish paths must not be used from Supabase prep branches unless that publish action is explicitly scoped and approved.

The existence of a browser-safe Supabase publishable key is not a release signal.

The release signal is the intentional combination of:

- active store posture
- identity surface posture
- local-mode fallback posture
- Supabase SQL/dashboard readiness, if included in the release
- passed verification
- passed browser smoke test
- explicit public Pages publish approval

## Local-mode invariant

Public Pages should keep local/browser play working until remote persistence is intentionally released.

Supabase SQL must not be applied merely because a Pages prep branch exists.

Supabase dashboard changes are separate explicit actions and must be captured as such.

## Runtime boundary

This rule does not change runtime site behavior.

This rule does not implement `SupabaseBracketStore`.

This rule does not apply Supabase SQL.

This rule does not change public Supabase dashboard state.

This rule does not merge to `main`.
