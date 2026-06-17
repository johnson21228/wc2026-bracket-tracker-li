#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "site" / "index.html"

text = INDEX.read_text()
errors: list[str] = []

required = [
    "WC2026_GAME1_CANONICAL_PICK_STATE_MODEL_START",
    "WC2026_GAME1_CANONICAL_PICK_STATE_MODEL_END",
    "window.WC2026_GAME1_PICK_STATE",
    "wc2026.game1.bracketPicks",
    "wc2026-game1-canonical-pick-state-v1",
    "function load()",
    "function save(nextState)",
    "function clear()",
    "function getPick(slotId)",
    "function setPick(slotId, team, rule)",
    "function clearPick(slotId)",
    "function getSourceSlotIds(slotId)",
    "function isPickValid(slotId",
    "function isSlotPickable(slotId)",
    "function getRenderablePicks()",
    "function inspect()",
]

for token in required:
    if token not in text:
        errors.append(f"Missing required model token: {token}")

if text.count("WC2026_GAME1_CANONICAL_PICK_STATE_MODEL_START") != 1:
    errors.append("Expected exactly one canonical pick-state model start marker")

if "WC2026_HARD_RESET_RESIDUAL_RENDER_STATE" in text:
    errors.append("Late DOM hard-reset scrub must not be present for Card 154 model work")

if "WC2026_DISABLE_SHORT_TERM_R16_HOLD_FOR_CANONICAL_STATE" not in text and "WC2026_SHORT_TERM_R16_HOLD" in text:
    errors.append("Short-term R16 hardcoded hold exists without the canonical-state disable marker")

# Card 154 is model-only. Rendering reroute belongs to Card 155.
if "WC2026_ROUTE_GAME1_RENDERING_THROUGH_PICK_STATE_MODEL" in text:
    errors.append("Rendering reroute marker found; Card 154 should add the model only")

if errors:
    print("WC2026 Game 1 canonical pick-state model verification failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("WC2026 Game 1 canonical pick-state model verification passed.")
