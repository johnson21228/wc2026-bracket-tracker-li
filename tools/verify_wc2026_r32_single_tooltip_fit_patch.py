#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
html = ROOT / "site/game1/index.html"
text = html.read_text(encoding="utf-8")
required = [
    "r32PickDetails",
    "showPickDetails",
    "hidePickDetails",
    "fitPickCardName",
    "computePickCardBox",
    "R32 pick-card single tooltip/name-fit",
]
missing = [s for s in required if s not in text]
if missing:
    raise SystemExit("Missing Game 1 single tooltip/name-fit markers: " + ", ".join(missing))
for bad in ["card.title", "setAttribute(\"title\"", "setAttribute('title'"]:
    if bad in text:
        raise SystemExit(f"Native title tooltip marker remains in Game 1 pick cards: {bad}")
for path in [
    ROOT / "li/world_cup/r32_pick_card_single_details_surface_rule.md",
    ROOT / "docs/features/r32_pick_card_single_tooltip_and_name_fit.md",
    ROOT / "cards/081_tune_r32_pick_card_single_tooltip_and_name_fit_card.md",
]:
    if not path.exists():
        raise SystemExit(f"Missing expected LI artifact: {path.relative_to(ROOT)}")
print("WC2026 R32 single tooltip/name-fit checks passed.")
