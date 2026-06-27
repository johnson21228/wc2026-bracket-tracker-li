#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

css = (ROOT / "site/css/board.css").read_text()
required = [
    ".board-background-layer",
    "opacity: .32;",
]
missing = [token for token in required if token not in css]
if missing:
    raise SystemExit("Knockout background deemphasis verification failed:\n- " + "\n- ".join(missing))

# Keep the runtime asset itself authoritative; deemphasis must be presentation-only.
for path in [
    "site/index.html",
    "site/js/mvc/view.js",
    "site/js/services/assetPaths.js",
]:
    text = (ROOT / path).read_text()
    if "assets/board/knockout_pub_background.jpeg" not in text:
        raise SystemExit(f"Missing knockout background runtime reference in {path}")

print("OK: knockout pub background is deemphasized through CSS opacity without changing the image asset.")
