#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
index = (ROOT / "site/index.html").read_text()
app_js = (ROOT / "site/js/app.js").read_text()
makefile = (ROOT / "Makefile").read_text()

errors = []

def require(condition, message):
    if not condition:
        errors.append(message)

for token in [
    "data-info-panel",
    "data-info-panel-open",
    "data-info-panel-close",
    "data-rules-panel",
    "data-rules-panel-open",
    "data-rules-panel-close",
    "Bracketeering Info",
    "World Cup Bracketeering Hub",
    "This is your World Cup Bracketeering Hub",
    "Navigate the game board like Google Maps",
    "The winner gets $50",
    "verification email may end up in your spam/junk folder",
    "Please, just have fun making picks",
    "Press the join button to play the game with others",
    "The game has two parts",
    "Part one results are used as a tiebreaker",
    "Group Stage Picks lock at 11:59 PM ET",
    "Knockout Stage picks are locked when the first knockout match begins",
    "16 points for correctly picking the World Cup champion",
]:
    require(token in index, f"missing Info panel token: {token}")

for token in [
    "Bracketeering Rules",
    "FIFA Bracketeering Hub",
    "official FIFA-supplied",
    "Development preview",
    "Developer note",
    "Game 1 Rules:",
    "Game 2 Preview",
]:
    require(token not in index, f"obsolete Rules/developer token remains: {token}")

for token in [
    "function setupInfoPanel",
    "data-info-panel-open",
    "data-info-panel-close",
    "data-rules-panel-open",
    "data-rules-panel-close",
    "openInfoPanel",
    "closeInfoPanel",
]:
    require(token in app_js, f"missing Info panel runtime token: {token}")

for token in [
    "function setupRulesPanel",
    "openRulesPanel",
    "closeRulesPanel",
    "Showing Game 1 rules",
    "Showing Game 2 rules",
]:
    require(token not in app_js, f"obsolete Rules runtime token remains: {token}")

require("tools/verify_wc2026_banner_rules_panel_ui.py" in makefile, "Makefile missing Info panel verifier")

if errors:
    print("Info panel UI verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: WC2026 Info panel is a single player-facing World Cup Bracketeering Hub info display.")
