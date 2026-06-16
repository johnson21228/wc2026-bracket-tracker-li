from pathlib import Path

root = Path.cwd()
html = root / "site/game1/index.html"
store = root / "site/data/game1_bracket_pick_store.js"
schema = root / "site/data/schema/game1_bracket_pick_store_schema.json"

for path in [html, store, schema]:
    if not path.exists():
        raise SystemExit(f"Missing required file: {path}")

html_text = html.read_text(encoding="utf-8")
store_text = store.read_text(encoding="utf-8")

required_html = [
    "../data/game1_bracket_pick_store.js",
]
required_store = [
    "wc2026.game1.bracketPicks",
    "WC2026_GAME1_BRACKET_PICK_STORE",
    "WC2026_GAME1_BRACKET_PICK_STORE_API",
    "L-R32-01",
    "L-R16-01",
    "L-QF-01",
    "L-SF-01",
    "CENTER-FINAL-FOUR",
    "migrateLegacy",
]

missing = [item for item in required_html if item not in html_text]
missing += [item for item in required_store if item not in store_text]
if missing:
    raise SystemExit("Missing site bracket pick store markers: " + ", ".join(missing))

print("Site bracket pick store verification passed.")
