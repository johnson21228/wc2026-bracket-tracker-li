#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def text(path: str) -> str:
    p = ROOT / path
    if not p.exists():
        raise SystemExit(f"Missing required file: {path}")
    return p.read_text()

def require(path: str, token: str) -> None:
    if token not in text(path):
        raise SystemExit(f"Missing token in {path}: {token}")

def require_file(path: str) -> None:
    if not (ROOT / path).exists():
        raise SystemExit(f"Missing required file: {path}")

require_file("site/assets/board/pub_background_game1.jpeg")
require_file("site/assets/board/pub_background_game1.jpeg")

index = text("site/index.html")
view = text("site/js/mvc/view.js")

require("site/index.html", 'href="assets/board/pub_background_game1.jpeg"')
require("site/js/mvc/view.js", 'src="assets/board/pub_background_game1.jpeg"')

# Superseded: knockout pub background is now intentionally the active runtime image.
if 'href="assets/board/pub_background_game1.jpeg"' not in index:
    raise SystemExit("site/index.html must preload the knockout pub background as the active runtime image")
# Superseded: knockout pub background is now intentionally rendered by the board view.
if 'src="assets/board/pub_background_game1.jpeg"' not in view:
    raise SystemExit("site/js/mvc/view.js must render the knockout pub background as the active runtime image")

if (ROOT / "site/js/services/assetPaths.js").exists():
    require("site/js/services/assetPaths.js", "assets/board/pub_background_game1.jpeg")

for path, tokens in {
    "li/world_cup/runtime_pub_background_selection_rule.md": [
        "site/assets/board/pub_background_game1.jpeg",
        "group-stage planning surface",
        "knockout pub/calendar background remains retained",
    ],
    "docs/features/runtime_pub_background_selection.md": [
        "Active runtime asset",
        "site/assets/board/pub_background_game1.jpeg",
        "site/js/mvc/view.js",
    ],
    "cards/204_publish_group_stage_background_card.md": [
        "Card 204",
        "group-stage pub background",
    ],
    "capture_back/CAPTURE_BACK_GROUP_STAGE_BACKGROUND_RUNTIME.md": [
        "site/index.html",
        "site/js/mvc/view.js",
        "assets/board/pub_background_game1.jpeg",
    ],
}.items():
    for token in tokens:
        require(path, token)

require("Makefile", "python3 tools/verify_wc2026_group_stage_background_runtime.py")
print("OK: WC2026 legacy group-stage background verifier is superseded by knockout pub default background.")
