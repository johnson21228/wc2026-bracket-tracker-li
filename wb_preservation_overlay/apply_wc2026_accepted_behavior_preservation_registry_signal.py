#!/usr/bin/env python3
from pathlib import Path
import shutil

ROOT = Path.cwd()
OVERLAY = ROOT / "wb_preservation_overlay"

files = [
    "li/repo/accepted_behavior_preservation_rule.md",
    "li/workbench/registry_behavior_signal_rule.md",
    "docs/behavior_contracts/accepted_behavior_preservation.md",
    "docs/registry/wc2026_registry_product_feedback.md",
    "data/registry/wc2026_product_feedback_signal.json",
    "cards/052_capture_accepted_behavior_preservation_registry_signal_card.md",
    "capture_back/CAPTURE_BACK_ACCEPTED_BEHAVIOR_PRESERVATION_REGISTRY_SIGNAL.md",
    "prompts/review_registry_product_feedback_signals.md",
]

for rel in files:
    src = OVERLAY / rel
    dst = ROOT / rel
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)

print("Applied WC2026 accepted behavior preservation registry signal CB overlay.")
