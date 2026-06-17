#!/usr/bin/env python3
from pathlib import Path
html = Path("site/index.html")
if not html.exists():
    raise SystemExit("Missing site/index.html")
text = html.read_text(encoding="utf-8")
required = [
    "WC2026_OPAQUE_MENU_PUB_BACKGROUND_START",
    "--wc2026-pub-wood-opaque: rgb(26, 17, 10);",
    ".tapMenu",
    "background: var(--wc2026-pub-wood-opaque) !important;",
    "opacity: 1 !important;",
    "WC2026_OPAQUE_MENU_PUB_BACKGROUND_END",
]
missing = [item for item in required if item not in text]
if missing:
    raise SystemExit("Missing opaque menu background patch content: " + ", ".join(missing))
if "rgba(26, 17, 10, .65)" in text and "--wc2026-pub-wood-opaque" not in text:
    raise SystemExit("Pick background exists, but opaque menu background variable missing")
print("Opaque menu pub background patch verification passed.")
