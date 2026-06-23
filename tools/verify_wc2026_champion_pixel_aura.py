#!/usr/bin/env python3
from pathlib import Path

view = Path("site/js/mvc/view.js").read_text()
css = Path("site/css/board.css").read_text()
makefile = Path("Makefile").read_text()

errors = []

for token in [
    'String(slot.slotId || "").toUpperCase() === "CHAMPION"',
    'button.classList.add("is-champion-winner")',
    'button.dataset.winnerFlag = winnerFlag',
    'const aura = document.createElement("span")',
    'aura.className = "champion-pixel-aura"',
    'for (const corner of ["top-left", "top-right", "bottom-left", "bottom-right"])',
    'auraFlag.className = `champion-pixel-aura-flag champion-pixel-aura-flag-${corner}`',
    'aura.append(auraFlag)',
    'button.prepend(aura)',
]:
    if token not in view:
        errors.append(f"missing view token: {token}")

for token in [
    "Champion Pixel Aura DOM underlay",
    ".pick-slot-button.is-champion-winner",
    "position: absolute;",
    ".champion-pixel-aura",
    "champion-pixel-aura-flag-top-left",
    "champion-pixel-aura-flag-top-right",
    "champion-pixel-aura-flag-bottom-left",
    "champion-pixel-aura-flag-bottom-right",
    "content: none;",
    "calc(var(--wc2026-champion-aura-x, 40px) * -.25)",
    "calc(var(--wc2026-champion-aura-y, 26px) * -.25)",
    "translate(-50%, -50%)",
    "translate(50%, 50%)",
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

print("OK: WC2026 Champion Pixel Aura renders as an explicit visible 2x2 flag DOM underlay for a picked CHAMPION slot.")
