from pathlib import Path

html = Path("site/game1/index.html")
store = Path("site/data/game1_bracket_pick_store.js")
if not html.exists():
    raise SystemExit("Missing site/game1/index.html")
if not store.exists():
    raise SystemExit("Missing site/data/game1_bracket_pick_store.js")

text = html.read_text(encoding="utf-8")
store_text = store.read_text(encoding="utf-8")
required_html = [
    "../data/game1_bracket_pick_store.js",
    "WC2026_USE_SITE_PICK_STORE_RENDER_START",
    "wc2026.game1.bracketPicks",
    "wc2026StorePickForSlot",
    "renderR16PicksFromSitePickStore",
    "openR16MenuUsingSitePickStore",
    "menu.dataset.assignmentTargetSlotId",
    "api.migrateLegacy()",
]
required_store = [
    "WC2026_GAME1_BRACKET_PICK_STORE_API",
    "storageKey = \"wc2026.game1.bracketPicks\"",
    "L-R16-01",
    "sourceSlotIds",
    "migrateLegacy",
]
missing = [item for item in required_html if item not in text] + [item for item in required_store if item not in store_text]
if missing:
    raise SystemExit("Missing site pick store render markers: " + ", ".join(missing))
print("Site pick store render/hold verification passed.")
