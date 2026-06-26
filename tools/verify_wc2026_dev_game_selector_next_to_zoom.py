#!/usr/bin/env python3
from pathlib import Path

index = Path("site/index.html").read_text()
app = Path("site/js/app.js").read_text()
view = Path("site/js/mvc/view.js").read_text()

errors = []

# Superseded rule:
# The old dev Game/Stage selector was once required next to zoom controls.
# The current one-game runtime uses game1 as persistence authority and may keep
# legacy game-1/game-2 hooks only for presentation/cache compatibility.
# Do not require Group Stage / Knockout Stage copy or a checked game-1 UI.

if "board-zoom-controls" not in index:
    errors.append("Zoom controls must remain present.")

if 'root.dataset.bracketeeringGame = "game1"' not in app:
    errors.append("Runtime must expose canonical bracketeeringGame=game1.")

if 'root.dataset.activeGame = "game-2"' not in app:
    errors.append("Runtime must default presentation to bracket-board activeGame=game-2.")

if "selectedDevGameValue" not in app:
    errors.append("Legacy active-game compatibility helper must remain available.")

if "game-1" not in app or "game-2" not in app:
    errors.append("Legacy game-1/game-2 compatibility hooks must remain in app.js during migration.")

if "game-1" in view and ".dev-game-selector-option input:checked" in view:
    errors.append("View must not derive current gameplay authority from old checked dev selector.")

if errors:
    print("WC2026 lifecycle Stage selector placement verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: legacy dev Stage selector verifier superseded; one-game runtime keeps zoom controls and compatibility hooks without old selector authority.")
