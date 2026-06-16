# Capture Back — Accepted Behavior Preservation Registry Signal

## What changed

This CB captures the regression lesson from the WC2026 Game 1/Game 2 site work as durable LI and registry feedback.

## Why

Accepted runtime behavior was known in conversation but not sufficiently represented as a repo-level contract. Later overlays could therefore regress it.

## Files added

- `li/repo/accepted_behavior_preservation_rule.md`
- `li/workbench/registry_behavior_signal_rule.md`
- `docs/behavior_contracts/accepted_behavior_preservation.md`
- `docs/registry/wc2026_registry_product_feedback.md`
- `data/registry/wc2026_product_feedback_signal.json`
- `cards/052_capture_accepted_behavior_preservation_registry_signal_card.md`
- `capture_back/CAPTURE_BACK_ACCEPTED_BEHAVIOR_PRESERVATION_REGISTRY_SIGNAL.md`
- `prompts/review_registry_product_feedback_signals.md`

## Preserved behavior

This CB intentionally does not touch site runtime files, Game 1 behavior, Game 2 behavior, or the verifier.

## Product signal

Workbench Registry should track accepted capabilities and require CB overlays to preserve impacted behaviors, explicitly deprecate them, or fail verification.
