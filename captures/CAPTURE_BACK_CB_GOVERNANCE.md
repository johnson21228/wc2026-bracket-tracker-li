# Capture Back — Capture Back Governance

## Intent

Preserve Capture Back records in the repo's current capture hygiene location so future CB overlays are discoverable and do not create root-level churn.

## Decision

New Capture Back report markdown files belong in `captures/`.

Do not create new root-level `CAPTURE_BACK_*.md` files.

Do not write new Capture Back reports to `capture_back/` unless intentionally preserving or migrating legacy material.

## Apply-script behavior

Future CB apply scripts should:

- write report markdown to `captures/CAPTURE_BACK_*.md`
- print the written `captures/...` path during apply
- avoid root-level `CAPTURE_BACK_*.md` files
- leave `capture_back/` as legacy/history unless a migration card explicitly says otherwise

## Verification

The repo now includes `tools/verify_capture_back_governance.py`.

The verifier checks that:

- no root-level `CAPTURE_BACK_*.md` files exist
- `captures/` exists
- this CB report exists in `captures/`
- the CB governance LI rule exists
- the governance card exists
- `Makefile` runs the verifier
- `MAP.md` points users to the current CB location

## Site-running invariant

This governance change is documentation/tooling only. It must not change runtime site behavior.
