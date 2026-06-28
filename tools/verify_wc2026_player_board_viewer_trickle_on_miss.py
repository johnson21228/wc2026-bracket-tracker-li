#!/usr/bin/env python3
from pathlib import Path

surface = Path("site/js/standings/PlayerStandingsSurface.js").read_text()
model = Path("site/js/mvc/model.js").read_text()
view = Path("site/js/mvc/view.js").read_text()
css = Path("site/css/app.css").read_text()
li = Path("li/world_cup/player_board_viewer_trickle_on_miss_rule.md").read_text()

required = {
    "surface": [
        "function canTeamStillReachSlot(",
        "function feederSlotIdsForSlot(",
        "const isUnreachablePick = Boolean(",
        "is-unreachable-pick",
        "player-board-viewer-eliminated-pick",
        "Eliminated",
    ],
    "model": [
        "function canTeamStillReachSlot(",
        'state: "unreachable"',
    ],
    "view": [
        "picked-cell-eliminated-truth",
        'data-official-pick-state", "unreachable"',
    ],
    "css": [
        ".player-board-viewer-pick.is-unreachable-pick",
        ".pick-slot-button.is-unreachable-pick",
        ".player-board-viewer-eliminated-pick",
        ".picked-cell-eliminated-truth",
        "text-decoration: line-through",
    ],
    "li": [
        "trickle-on miss",
        "Eliminated",
        "Pool player board viewer",
    ],
}

errors = []
for name, tokens in required.items():
    text = {"surface": surface, "model": model, "view": view, "css": css, "li": li}[name]
    for token in tokens:
        if token not in text:
            errors.append(f"{name} missing: {token}")

if errors:
    print("WC2026 trickle-on miss verification failed:")
    for err in errors:
        print(f"- {err}")
    raise SystemExit(1)

print("OK: player board viewer marks trickle-on misses as eliminated.")
