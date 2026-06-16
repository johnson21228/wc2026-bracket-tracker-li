# Capture Back: Rebuild Verifier After Patch Drift

## Why
The verifier accumulated patch fragments and duplicate/incorrect indentation, causing Python `IndentationError` before repo verification could run.

## Change
Rebuild `tools/verify_wc2026_bracket_tracker.py` as one clean verifier aligned with the current site architecture:

- deployable site lives in `site/`
- Game 1 uses layered board assets and visible hit targets
- Game 2 may be in foundation/progressive-seed development
- Game 2 official seed + Game 1 tiebreaker LI is required once captured
- root overlay working directories are residue and should be cleaned before verification

## Verification
`python3 -m py_compile tools/verify_wc2026_bracket_tracker.py`
`make verify`
`make pack`
