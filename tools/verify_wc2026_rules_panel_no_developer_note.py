#!/usr/bin/env python3
from pathlib import Path

html = Path("site/index.html").read_text()
errors = []

for token in [
    "Bracketeering Rules",
    "FIFA Bracketeering Hub",
    "official FIFA-supplied",
    "Developer note",
    "Game selector is currently UI-only",
    "Development preview",
    "Game 1 Rules:",
    "Game 2 Preview",
]:
    if token in html:
        errors.append(f"forbidden Info panel text remains: {token}")

for token in [
    "Bracketeering Info",
    "World Cup Bracketeering Hub",
    "How to play",
    "Navigate the game board like Google Maps",
    "Press the join button to play the game with others",
    "The winner gets $50",
    "Part one results are used as a tiebreaker",
    "Group Stage Picks lock at 11:59 PM ET",
    "Knockout Stage picks are locked when the first knockout match begins",
    "16 points for correctly picking the World Cup champion",
]:
    if token not in html:
        errors.append(f"expected Info panel token missing: {token}")

if errors:
    print("Info panel developer note verification failed: " + "; ".join(errors))
    raise SystemExit(1)

print("OK: WC2026 Info panel is single-display, player-facing, and exposes no developer-only caveats.")
