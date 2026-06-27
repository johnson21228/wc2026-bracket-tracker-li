#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KNOCKOUT = "assets/board/knockout_pub_background.jpeg"
GROUP = "assets/board/pub_background_game1.jpeg"


def text(path):
    return (ROOT / path).read_text()


def require_file(path):
    if not (ROOT / path).exists():
        raise SystemExit(f"Missing required file: {path}")


def require(path, token):
    value = text(path)
    if token not in value:
        raise SystemExit(f"Missing {token!r} in {path}")


require_file("site/assets/board/knockout_pub_background.jpeg")
require_file("source/images/wc2026_knockout_pub_calendar_background.jpeg")

if (ROOT / "site/assets/board/knockout_pub_background.jpeg").read_bytes() != (ROOT / "source/images/wc2026_knockout_pub_calendar_background.jpeg").read_bytes():
    raise SystemExit("source and runtime knockout pub background images must match byte-for-byte")

for path in [
    "site/js/services/assetPaths.js",
    "site/js/mvc/view.js",
    "site/index.html",
]:
    require(path, KNOCKOUT)
    if GROUP in text(path):
        raise SystemExit(f"{path} still boots/preloads the group-stage background")

require("site/js/app.js", '"game-1": "assets/board/knockout_pub_background.jpeg"')
require("site/js/app.js", '"game-2": "assets/board/knockout_pub_background.jpeg"')
require("li/world_cup/knockout_runtime_default_background_rule.md", "single-game Bracketeering runtime must boot with the knockout pub background")
require("docs/features/knockout_runtime_default_background.md", "site/assets/board/knockout_pub_background.jpeg")
require("captures/CAPTURE_BACK_KNOCKOUT_RUNTIME_DEFAULT_BACKGROUND.md", "default board background")
require("cards/1023_knockout_runtime_default_background_card.md", "Runtime asset")

print("OK: WC2026 runtime default background is the knockout pub calendar asset.")
