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

require_file("site/assets/board/pub_background.jpeg")
require_file("site/assets/board/knockout_pub_background.jpeg")

index = text("site/index.html")
view = text("site/js/mvc/view.js")

require("site/index.html", 'href="assets/board/pub_background.jpeg"')
require("site/js/mvc/view.js", 'src="assets/board/pub_background.jpeg"')

if 'href="assets/board/knockout_pub_background.jpeg"' in index:
    raise SystemExit("site/index.html still preloads the knockout pub background as the active runtime image")
if 'src="assets/board/knockout_pub_background.jpeg"' in view:
    raise SystemExit("site/js/mvc/view.js still renders the knockout pub background as the active runtime image")

if (ROOT / "site/js/services/assetPaths.js").exists():
    require("site/js/services/assetPaths.js", "assets/board/pub_background.jpeg")

for path, tokens in {
    "li/world_cup/runtime_pub_background_selection_rule.md": [
        "site/assets/board/pub_background.jpeg",
        "group-stage planning surface",
        "knockout pub/calendar background remains retained",
    ],
    "docs/features/runtime_pub_background_selection.md": [
        "Active runtime asset",
        "site/assets/board/pub_background.jpeg",
        "site/js/mvc/view.js",
    ],
    "cards/204_publish_group_stage_background_card.md": [
        "Card 204",
        "group-stage pub background",
    ],
    "capture_back/CAPTURE_BACK_GROUP_STAGE_BACKGROUND_RUNTIME.md": [
        "site/index.html",
        "site/js/mvc/view.js",
        "assets/board/pub_background.jpeg",
    ],
}.items():
    for token in tokens:
        require(path, token)

require("Makefile", "python3 tools/verify_wc2026_group_stage_background_runtime.py")
print("OK: WC2026 runtime board background uses the group-stage pub image and is verified.")
