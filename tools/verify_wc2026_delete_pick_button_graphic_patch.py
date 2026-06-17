#!/usr/bin/env python3
from pathlib import Path

site = Path("site/index.html")
if not site.exists():
    raise SystemExit("site/index.html not found")
text = site.read_text()
required = [
    "WC2026_DELETE_PICK_BUTTON_GRAPHIC_INSTALLED",
    "WC2026_DELETE_PICK_BUTTON_GRAPHIC_JS",
    "wc2026DeletePickButtonGraphic",
    "wc2026DeletePickIcon",
    "Delete pick",
    "MutationObserver",
]
missing = [m for m in required if m not in text]
if missing:
    raise SystemExit("Delete pick button graphic verification failed: missing " + ", ".join(missing))
if "innerHTML = DELETE_HTML" not in text:
    raise SystemExit("Delete pick button graphic verification failed: visible label normalization missing")
print("Delete pick button graphic verification passed.")
