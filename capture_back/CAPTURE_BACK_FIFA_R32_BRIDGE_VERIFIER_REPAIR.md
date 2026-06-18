# Capture Back — FIFA R32 bridge verifier repair

## Problem

Card 178 content and runtime wiring landed, but the repair script could not patch `tools/verify_wc2026_bracket_tracker.py` because the expected insertion anchor was not present.

## Decision

Add a separate verifier:

```text
tools/verify_wc2026_fifa_r32_bridge.py
```

and wire it into `make verify`.

## Scope

This verifies the already-applied Card 178 files:

- source image
- extraction markdown/json
- FIFA logical R32 order
- FIFA-to-geometry bridge
- board manifest compatibility
- `BoardShell` runtime layer wiring
- developer toggle
- CSS visibility rules

It does not change the extracted FIFA logic or board geometry.
