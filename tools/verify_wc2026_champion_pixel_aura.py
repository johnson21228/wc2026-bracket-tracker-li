#!/usr/bin/env python3
from pathlib import Path

view = Path("site/js/mvc/view.js").read_text()
css = Path("site/css/board.css").read_text()
makefile = Path("Makefile").read_text()

errors = []

for token in [
    'String(slot.slotId || "").toUpperCase() === "CHAMPION"',
    'button.classList.add("is-champion-winner")',
    'button.dataset.winnerFlag = displayTeam.flag || ""',
    '--wc2026-champion-aura-x',
    '--wc2026-champion-aura-y',
]:
    if token not in view:
        errors.append(f"missing view token: {token}")

for token in [
    "Champion Pixel Aura",
    ".pick-slot-button.is-champion-winner",
    "content:",
    'attr(data-winner-flag) " " attr(data-winner-flag) "\\A"',
    'attr(data-winner-flag) " " attr(data-winner-flag);',
    "white-space: pre;",
    "filter:",
    "box-shadow:",
    "drop-shadow",
    "pointer-events: none",
]:
    if token not in css:
        errors.append(f"missing CSS token: {token}")

if "tools/verify_wc2026_champion_pixel_aura.py" not in makefile:
    errors.append("Makefile missing champion pixel aura verifier")

if errors:
    print("Champion Pixel Aura verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: WC2026 Champion Pixel Aura renders only for a picked CHAMPION slot using a fuzzy glowing 2x2 flag underlay.")
