#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]

def fail(msg):
    raise SystemExit(msg)

html = ROOT / "site/game1/index.html"
text = html.read_text()
required = [
    "--r32-pick-card-font-size: 14px",
    "--r32-pick-card-line-height: 14px",
    "--r32-pick-card-flag-width: 34px",
    "--r32-pick-card-flag-height: 32px",
    "function r32CardDisplayName(team)",
    "R32_CARD_NAME_BREAKS",
    "pickName.textContent = r32CardDisplayName(pick)",
]
for needle in required:
    if needle not in text:
        fail(f"Missing expected Game 1 fixed metric patch marker: {needle}")

if "fontSize" in text and "fit" in text[text.find("fontSize")-200:text.find("fontSize")+200].lower():
    fail("Found suspicious per-card font-size fit logic near fontSize marker")

metrics_path = ROOT / "site/data/r32_pick_card_font_metrics.json"
if not metrics_path.exists():
    fail("Missing site/data/r32_pick_card_font_metrics.json")
metrics = json.loads(metrics_path.read_text())
if metrics["teamName"]["fontSizePx"] != 14:
    fail("Unexpected team-name font size in metric data")
if metrics["teamName"]["maxLines"] != 2:
    fail("Expected maxLines 2 in metric data")
if metrics["compactCardShowsSlotRule"] is not False:
    fail("Compact card should not show slot rule")

for path in [
    "li/world_cup/r32_pick_card_font_metrics_rule.md",
    "docs/features/r32_pick_card_fixed_font_metrics.md",
    "cards/083_define_r32_pick_card_fixed_font_metrics_card.md",
]:
    if not (ROOT / path).exists():
        fail(f"Missing expected LI/doc/card file: {path}")

print("WC2026 R32 pick-card fixed font metrics patch checks passed.")
