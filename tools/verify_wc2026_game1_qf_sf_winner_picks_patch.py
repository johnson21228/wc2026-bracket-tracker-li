#!/usr/bin/env python3
from pathlib import Path

root = Path.cwd()
index = root / "site" / "game1" / "index.html"
text = index.read_text()
required = [
    "WC2026_GAME1_QF_SF_WINNER_PICKS",
    "const ADVANCEMENT_STORAGE_KEY",
    "function advancementSlotRulesFromManifest",
    'round === "QF"',
    'round === "SF"',
    "sourceSlotIdsForAdvancementRule",
    "openAdvancementMenu",
    "assignAdvancementWinner",
    "renderAdvancementPicks",
    "createAdvancementHotspots",
]
missing = [s for s in required if s not in text]
if missing:
    raise SystemExit("Missing Game 1 QF/SF winner-pick marker(s): " + ", ".join(missing))

for rel in [
    "cards/113_add_game1_qf_sf_winner_picks_card.md",
    "docs/features/game1_qf_sf_winner_picks.md",
    "li/world_cup/game1_qf_sf_winner_pick_rule.md",
    "prompts/add_game1_qf_sf_winner_picks.md",
    "capture_back/CAPTURE_BACK_GAME1_QF_SF_WINNER_PICKS.md",
]:
    if not (root / rel).exists():
        raise SystemExit(f"Missing expected artifact: {rel}")

print("WC2026 Game 1 QF/SF winner-pick checks passed.")
