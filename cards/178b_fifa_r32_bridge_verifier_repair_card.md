# Card 178b — Repair FIFA R32 bridge verifier integration

## Intent

Finish Card 178 by adding a dedicated verifier for the FIFA R32 logic-to-board bridge.

## Acceptance

- `tools/verify_wc2026_fifa_r32_bridge.py` exists.
- `make verify` runs the FIFA bridge verifier.
- The verifier confirms:
  - 32 unique FIFA R32 slots
  - bridge order matches logic order
  - every bridge geometry slot exists
  - every bridge geometry slot has bounds
  - runtime render layer is wired
  - developer toggle exists
  - CSS visibility rule exists
