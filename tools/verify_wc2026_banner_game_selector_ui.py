#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "site/index.html"
APP = ROOT / "site/js/app.js"
VIEW = ROOT / "site/js/mvc/view.js"

index = INDEX.read_text()
app = APP.read_text()
view = VIEW.read_text()

errors = []

def require(condition, message):
    if not condition:
        errors.append(message)

require('value="game-1"' in index, "legacy Group Stage radio hook must remain for compatibility")
require('value="game-2"' in index, "legacy Knockout Stage radio hook must remain for compatibility")
require('root.dataset.bracketeeringGame = "game1"' in app,
        "runtime must declare one canonical persisted Bracketeering game")
require('root.dataset.activeGame = "game-2"' in app,
        "runtime must default presentation to bracket-board alias game-2")
require('input[value="game-1"]' in app and "checked = false" in app,
        "runtime must not default stale Group Stage presentation")
require('input[value="game-2"]' in app and "checked = true" in app,
        "runtime must check bracket-board presentation alias")
require('return root.dataset.activeGame || "game-2";' in view,
        "view must default to bracket-board presentation")
require("function isGroupStagePresentationActive()" in view and "return false;" in view,
        "Group Stage presentation must not suppress the one-game bracket board")

if errors:
    print("Banner lifecycle Stage selector UI verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: legacy Stage selector hooks remain, but one-game runtime defaults to bracket-board presentation.")
