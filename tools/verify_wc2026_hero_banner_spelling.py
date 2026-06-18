#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OLD = "Braketeering Pub"
NEW = "Bracketeering Pub"

CHECK_PATHS = [
    "site/index.html",
    "site/js/mvc/model.js",
    "site/js/mvc/view.js",
    "docs/features/pub_hero_header.md",
    "li/world_cup/pub_hero_header_rule.md",
    "capture_back/CAPTURE_BACK_PUB_HERO_HEADER.md",
    "cards/197_define_pub_hero_header_card.md",
]

EVIDENCE_PATHS = [
    "capture_back/CAPTURE_BACK_HERO_BANNER_SPELLING.md",
    "cards/200_fix_pub_hero_banner_spelling_card.md",
]

errors = []
found_new = False

for rel in CHECK_PATHS:
    path = ROOT / rel
    if not path.exists():
        continue
    text = path.read_text()
    if OLD in text:
        errors.append(f"{rel} still contains old spelling: {OLD}")
    if NEW in text:
        found_new = True

for rel in EVIDENCE_PATHS:
    path = ROOT / rel
    if not path.exists():
        errors.append(f"missing spelling evidence file: {rel}")
        continue
    text = path.read_text()
    if NEW in text:
        found_new = True

if not found_new:
    errors.append(f"corrected spelling not found: {NEW}")

if errors:
    raise SystemExit("WC2026 hero banner spelling verification failed:\n- " + "\n- ".join(errors))

print("OK: WC2026 hero banner spelling is corrected and verified.")
