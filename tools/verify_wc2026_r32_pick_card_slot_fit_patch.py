#!/usr/bin/env python3
from pathlib import Path

root = Path(__file__).resolve().parents[1]
required = [
    root / "li/world_cup/r32_pick_card_slot_fit_rule.md",
    root / "docs/features/r32_pick_card_slot_fit.md",
    root / "cards/082_tune_r32_pick_card_slot_fit_card.md",
    root / "prompts/tune_r32_pick_card_slot_fit.md",
    root / "capture_back/CAPTURE_BACK_R32_PICK_CARD_SLOT_FIT.md",
]
missing = [str(p.relative_to(root)) for p in required if not p.exists()]
if missing:
    raise SystemExit("Missing R32 pick-card slot fit files:\n- " + "\n- ".join(missing))
html = (root / "site/game1/index.html").read_text(encoding="utf-8")
needles = [
    "r32-pick-card-slot-fit-overrides",
    "enforceR32PickCardSlotFit",
    "fitR32PickCardNames",
    "card.dataset.r32SlotFit",
    "rule.boundsPx",
]
missing_needles = [n for n in needles if n not in html]
if missing_needles:
    raise SystemExit("Game 1 page missing slot-fit patch markers:\n- " + "\n- ".join(missing_needles))
print("WC2026 R32 pick-card slot fit checks passed.")
