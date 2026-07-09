#!/usr/bin/env python3
from pathlib import Path
import re
import sys

errors = []

css = Path("site/css/board.css").read_text()
controller = Path("site/js/mvc/controller.js").read_text()
view = Path("site/js/mvc/view.js").read_text()

expected_rule = ".board-background-layer { z-index: 0; opacity: .20; }"
if expected_rule not in css:
    errors.append("shared board background layer opacity must be softened to .20")

if ".board-background-layer { z-index: 0; opacity: .72; }" in css:
    errors.append("old .72 board background opacity must not remain")

for path in [
    "li/world_cup/lifecycle_background_softening_rule.md",
    "docs/features/lifecycle_background_softening.md",
    "captures/CAPTURE_BACK_LIFECYCLE_BACKGROUND_SOFTENING.md",
    "cards/255_soften_lifecycle_stage_backgrounds_card.md",
]:
    if not Path(path).exists():
        errors.append(f"missing lifecycle background softening artifact: {path}")

for token in [
    'activeGame === "game-1" && slot.round !== "R32"',
    'activeGame === "game-2" && slot.round === "R32"',
    "Round of 32 picking is disabled",
    "Game 1 Round of 32 picking is active",
    "Game 2 pick menu is not ready",
]:
    if token in controller or token in view:
        errors.append(f"stage-gated pick/menu token must not return: {token}")

if errors:
    print("Lifecycle background softening verification failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("OK: lifecycle-stage backgrounds are softened through the shared presentation-only background layer without restoring pick/menu gating.")
