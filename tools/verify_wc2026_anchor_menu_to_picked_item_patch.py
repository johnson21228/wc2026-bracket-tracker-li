#!/usr/bin/env python3
from pathlib import Path

path = Path("site/index.html")
if not path.exists():
    raise SystemExit("Missing site/index.html")
text = path.read_text()
required = [
    "WC2026_CHOICE_MENU_ANCHORED_TO_PICK_TARGET_CSS",
    "WC2026_CHOICE_MENU_ANCHORED_TO_PICK_TARGET_JS",
    "installChoiceMenuAnchoredToPickedItem",
    "anchorMenuToTarget",
    "lastPickTarget",
    "boardPointForRect",
    "dataset.wc2026AnchoredToPickTarget",
    "MutationObserver",
]
missing = [m for m in required if m not in text]
if missing:
    raise SystemExit("Anchor menu to picked item verification failed: missing " + ", ".join(missing))
print("Anchor menu to picked item verification passed.")
