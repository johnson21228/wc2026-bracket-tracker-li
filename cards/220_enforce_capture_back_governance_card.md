# Card 220 — Enforce Capture Back Governance

## Intent

Make future Capture Back overlays place report markdown where the user can find it, without creating root-level report churn.

## Problem

The repo has both current and legacy capture locations:

- `captures/` for current root-level Capture Back reports
- `capture_back/` for older accumulated/legacy capture material

Without an explicit governance rule and verifier, a CB overlay can be applied successfully while the user cannot easily find the report markdown.

## Implementation target

- Add durable LI for Capture Back governance.
- Add a repo doc explaining current and legacy CB locations.
- Add a verifier that fails on root-level `CAPTURE_BACK_*.md` files.
- Require this overlay's CB report to exist in `captures/`.
- Ensure `Makefile` runs the governance verifier.
- Update `MAP.md` so the current capture location is visible.

## Acceptance criteria

- `captures/CAPTURE_BACK_CB_GOVERNANCE.md` exists.
- `li/repo/capture_back_governance_rule.md` exists.
- `docs/repo/capture_back_governance.md` exists.
- `tools/verify_capture_back_governance.py` exists and passes.
- `make verify` runs `tools/verify_capture_back_governance.py`.
- No root-level `CAPTURE_BACK_*.md` files exist.
- The runtime site is unchanged.
