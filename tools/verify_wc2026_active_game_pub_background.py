#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KNOCKOUT = "assets/board/knockout_pub_background.jpeg"
GROUP = "assets/board/pub_background_game1.jpeg"


def read(path):
    return (ROOT / path).read_text()


def require_file(path):
    if not (ROOT / path).exists():
        raise SystemExit(f"Missing required file: {path}")


def require(path, token):
    text = read(path)
    if token not in text:
        raise SystemExit(f"Missing {token!r} in {path}")


require_file("site/assets/board/knockout_pub_background.jpeg")
require_file("site/assets/board/pub_background_game1.jpeg")

require("site/js/services/assetPaths.js", f'backgroundImage: "{KNOCKOUT}"')
require("site/js/mvc/view.js", f'src="{KNOCKOUT}"')
require("site/index.html", f'href="{KNOCKOUT}"')

require("site/js/app.js", "ACTIVE_GAME_BACKGROUND_IMAGES")
require("site/js/app.js", '"game-1": "assets/board/knockout_pub_background.jpeg"')
require("site/js/app.js", '"game-2": "assets/board/knockout_pub_background.jpeg"')
require("site/js/app.js", "setupActiveGameBackground(root);")
require("site/js/app.js", "syncActiveGameBackground(root);")

for path in [
    "site/js/services/assetPaths.js",
    "site/js/mvc/view.js",
    "site/index.html",
]:
    text = read(path)
    if GROUP in text:
        raise SystemExit(f"Stale group-stage runtime background remains in {path}")

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
