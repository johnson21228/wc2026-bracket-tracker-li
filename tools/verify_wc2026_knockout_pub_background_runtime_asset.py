#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return (ROOT / path).read_text()


def require_file(path):
    p = ROOT / path
    if not p.exists():
        raise SystemExit(f"Missing required file: {path}")
    return p


def require(path, token):
    text = read(path)
    if token not in text:
        raise SystemExit(f"Missing {token!r} in {path}")


image = require_file("site/assets/board/pub_background_game1.jpeg")
if image.stat().st_size < 100_000:
    raise SystemExit("Generated knockout background image looks too small to be the accepted runtime asset.")
if not image.read_bytes()[:3] == bytes([0xFF, 0xD8, 0xFF]):
    raise SystemExit("Generated knockout background image is not a JPEG.")

manifest_path = require_file("source/text/knockout_pub_background_generated_manifest.json")
manifest = json.loads(manifest_path.read_text())

if manifest.get("outputPath") != "site/assets/board/pub_background_game1.jpeg":
    raise SystemExit("Generated manifest must target the runtime knockout background image path.")

style = manifest.get("styleRule", "")
for token in [
    "preserve the base calendar/poster composition",
    "render unresolved TBD tiny/subtle",
    "render vs tiny/subtle",
    "dim upper-left light bulb/neon sign",
    "do not draw row frames or row boxes",
    "do not draw footer/caption/provenance text",
]:
    if token not in style:
        raise SystemExit(f"Generated manifest missing style guardrail: {token}")

require("site/js/app.js", '"game-2": "assets/board/pub_background_game1.jpeg"')
require("site/js/app.js", 'root.dataset.activeGame = "game-2";')
require("prompts/update_knockout_pub_background_image.md", "Use the current runtime image as the base/reference image")
require("prompts/update_knockout_pub_background_image.md", "Replace only `TBD` rows whose teams are now authoritative")
require("prompts/update_knockout_pub_background_image.md", "Do not add any footer, caption, provenance line")
require("prompts/update_knockout_pub_background_image.md", "The `vs` between flags must be tiny, quiet, subtle")
require("prompts/update_knockout_pub_background_image.md", "The `TBD` text must be tiny, quiet, and subtle")
require("prompts/update_knockout_pub_background_image.md", "Do not brighten the upper-left bulb or neon sign again")
require("docs/workflows/update_knockout_pub_background_image.md", "latest accepted runtime image")
require("li/world_cup/knockout_pub_background_image_prompt_rule.md", "Future `UPDATE KNOCKOUT PUB BACKGROUND IMAGE` runs must use the latest accepted runtime image")
require("cards/1022_knockout_pub_background_runtime_asset_card.md", "Use Generated Knockout Pub Background as Runtime Asset")
require("captures/CAPTURE_BACK_KNOCKOUT_PUB_BACKGROUND_RUNTIME_ASSET.md", "latest generated knockout pub calendar image is promoted")

print("OK: knockout pub background runtime asset and next-update prompt are captured and verified.")
