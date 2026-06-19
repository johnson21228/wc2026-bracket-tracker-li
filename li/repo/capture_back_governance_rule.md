# Capture Back Governance Rule

## Rule

All new Capture Back report markdown files must be written to `captures/`.

New root-level `CAPTURE_BACK_*.md` files are not allowed.

The legacy `capture_back/` folder may remain as historical material, but new CB reports should not be written there unless an explicit migration/preservation card says so.

## Apply script requirements

Every CB overlay apply script should:

1. write the CB report to `captures/CAPTURE_BACK_*.md`
2. print the written `captures/...` path during apply
3. avoid creating root-level `CAPTURE_BACK_*.md` files
4. avoid writing new CB reports into `capture_back/` by default

## Verifier requirements

The repo verifier should fail when:

- a root-level `CAPTURE_BACK_*.md` file exists
- the expected current CB report for a CB overlay is missing from `captures/`
- the governance LI/card files are missing
- `Makefile` no longer runs the CB governance verifier

## Rationale

Capture Back is repo memory. Keeping current CB reports in one current location makes them discoverable while avoiding root churn and preserving legacy history separately.
