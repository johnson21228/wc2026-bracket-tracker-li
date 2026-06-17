#!/usr/bin/env python3
from pathlib import Path

root = Path.cwd()
index = root / "site" / "game1" / "index.html"
text = index.read_text(encoding="utf-8")
required = [
    "WC2026_GAME1_KNOCKOUT_CHOICE_MENU_RUNTIME_WIRING",
    "function wc2026KnockoutAlternateSlotKeys",
    "function wc2026ResolvedKnockoutContestants",
    "function wc2026OpenResolvedKnockoutMenu",
    "r16CandidateTeams = function wc2026RuntimeR16CandidateTeams",
    "advancementCandidateTeams = function wc2026RuntimeAdvancementCandidateTeams",
    "openR16Menu = function wc2026OpenRuntimeR16Menu",
    "openAdvancementMenu = function wc2026OpenRuntimeAdvancementMenu",
]
missing = [s for s in required if s not in text]
if missing:
    raise SystemExit("Missing Game 1 knockout runtime wiring markers: " + ", ".join(missing))

for rel in [
    "cards/115_wire_game1_knockout_choice_menu_runtime_card.md",
    "docs/features/game1_knockout_choice_menu_runtime_wiring.md",
    "li/world_cup/game1_knockout_choice_menu_runtime_wiring_rule.md",
    "prompts/repair_game1_knockout_choice_menu_runtime_wiring.md",
    "capture_back/CAPTURE_BACK_GAME1_KNOCKOUT_CHOICE_MENU_RUNTIME_WIRING.md",
]:
    if not (root / rel).exists():
        raise SystemExit(f"Missing expected file: {rel}")

print("WC2026 Game 1 knockout choice menu runtime wiring checks passed.")
