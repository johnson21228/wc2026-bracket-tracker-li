#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read(path):
    return (ROOT / path).read_text()

def require_file(path):
    if not (ROOT / path).exists():
        raise SystemExit(f"Missing required file: {path}")

def require(path, token):
    text = read(path)
    if token not in text:
        raise SystemExit(f"Missing {token!r} in {path}")

def forbid(path, token):
    text = read(path)
    if token in text:
        raise SystemExit(f"Forbidden stale token {token!r} remains in {path}")

require_file("site/assets/board/pub_background_game1.jpeg")
require_file("site/assets/board/knockout_pub_background.jpeg")

require("site/js/services/assetPaths.js", "assets/board/pub_background_game1.jpeg")
require("site/js/mvc/view.js", 'src="assets/board/pub_background_game1.jpeg"')
require("site/index.html", 'href="assets/board/pub_background_game1.jpeg"')

require("site/js/app.js", "ACTIVE_GAME_BACKGROUND_IMAGES")
require("site/js/app.js", '"game-1": "assets/board/pub_background_game1.jpeg"')
require("site/js/app.js", '"game-2": "assets/board/knockout_pub_background.jpeg"')
require("site/js/app.js", "setupActiveGameBackground(root);")
require("site/js/app.js", "const view = createBracketView(root);\n  setupActiveGameBackground(root);")
require("site/js/app.js", "syncActiveGameBackground(root);")

# Stale default runtime references should be gone from active runtime files.
for path in [
    "site/js/services/assetPaths.js",
    "site/js/mvc/view.js",
    "site/index.html",
]:
    forbid(path, "assets/board/pub_background.jpeg")

# Keep this visual-only: selector changes background only, not gameplay/storage.
app = read("site/js/app.js")
start = app.index("function setupActiveGameBackground")
end = app.index("async function main()")
segment = app[start:end]
for forbidden in [
    "createBracketModel",
    "createBracketController",
    "localStorage",
    "Supabase",
    "score",
    "route",
    "fetch(",
]:
    if forbidden in segment:
        raise SystemExit(
            "Active-game background switch must remain presentation-only; "
            f"found {forbidden!r} in setupActiveGameBackground segment."
        )

print("OK: WC2026 active game selector switches pub background image as presentation-only UI.")
