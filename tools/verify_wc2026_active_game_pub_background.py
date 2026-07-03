#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ACTIVE_BACKGROUND = "assets/board/pub_background_game1.jpeg"
STALE_BACKGROUND = "assets/board/knockout_pub_background.jpeg"


def read(path):
    return (ROOT / path).read_text()


def require_file(path):
    if not (ROOT / path).exists():
        raise SystemExit(f"Missing required file: {path}")


def require(path, token):
    text = read(path)
    if token not in text:
        raise SystemExit(f"Missing {token!r} in {path}")


require_file("site/assets/board/pub_background_game1.jpeg")
require_file("site/assets/board/pub_background_game1.jpeg")

require("site/js/services/assetPaths.js", f'backgroundImage: "{ACTIVE_BACKGROUND}"')
require("site/js/mvc/view.js", f'src="{ACTIVE_BACKGROUND}"')
require("site/index.html", f'href="{ACTIVE_BACKGROUND}"')

require("site/js/app.js", "ACTIVE_GAME_BACKGROUND_IMAGES")
require("site/js/app.js", '"game-1": "assets/board/pub_background_game1.jpeg"')
require("site/js/app.js", '"game-2": "assets/board/pub_background_game1.jpeg"')
require("site/js/app.js", "setupActiveGameBackground(root);")
require("site/js/app.js", "syncActiveGameBackground(root);")

for path in [
    "site/js/services/assetPaths.js",
    "site/js/mvc/view.js",
    "site/index.html",
]:
    text = read(path)
    if STALE_BACKGROUND in text:
        raise SystemExit(f"Stale pre-Game-1 runtime background remains in {path}")

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

print("OK: WC2026 site defaults to the knockout pub background image without changing gameplay logic.")
