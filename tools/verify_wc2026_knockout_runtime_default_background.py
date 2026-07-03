#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ACTIVE_BACKGROUND = "assets/board/pub_background_game1.jpeg"
STALE_BACKGROUND = "assets/board/knockout_pub_background.jpeg"


def text(path):
    return (ROOT / path).read_text()


def require_file(path):
    if not (ROOT / path).exists():
        raise SystemExit(f"Missing required file: {path}")


def require(path, token):
    value = text(path)
    if token not in value:
        raise SystemExit(f"Missing {token!r} in {path}")


require_file("site/assets/board/pub_background_game1.jpeg")
require_file("source/images/wc2026_knockout_pub_calendar_background.jpeg")

if (ROOT / "site/assets/board/pub_background_game1.jpeg").read_bytes() != (ROOT / "source/images/wc2026_knockout_pub_calendar_background.jpeg").read_bytes():
    raise SystemExit("source and runtime knockout pub background images must match byte-for-byte")

for path in [
    "site/js/services/assetPaths.js",
    "site/js/mvc/view.js",
    "site/index.html",
]:
    require(path, ACTIVE_BACKGROUND)
    if STALE_BACKGROUND in text(path):
        raise SystemExit(f"{path} still boots/preloads the stale pre-Game-1 background")

require("site/js/app.js", '"game-1": "assets/board/pub_background_game1.jpeg"')
require("site/js/app.js", '"game-2": "assets/board/pub_background_game1.jpeg"')
require("li/world_cup/knockout_runtime_default_background_rule.md", "single-game Bracketeering runtime must boot with the knockout pub background")
require("docs/features/knockout_runtime_default_background.md", "site/assets/board/pub_background_game1.jpeg")
require("captures/CAPTURE_BACK_KNOCKOUT_RUNTIME_DEFAULT_BACKGROUND.md", "default board background")
require("cards/1023_knockout_runtime_default_background_card.md", "Runtime asset")

print("OK: WC2026 runtime default background is the knockout pub calendar asset.")
