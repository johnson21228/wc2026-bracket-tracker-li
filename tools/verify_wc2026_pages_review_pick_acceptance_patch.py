from pathlib import Path
html = Path("site/index.html")
if not html.exists():
    html = Path("site/game1/index.html")
text = html.read_text(encoding="utf-8")
required = [
    "WC2026_PAGES_REVIEW_PICK_ACCEPTANCE_START",
    "wc2026.game1.bracketPicks",
    "wc2026.game1.r32.picks",
    "wc2026.game1.r16.winnerPicks",
    "persistPick",
    "reviewAcceptanceContract",
    "wc2026:review-pick-accepted",
]
missing = [item for item in required if item not in text]
if missing:
    raise SystemExit("Missing Pages review pick acceptance markers: " + ", ".join(missing))
print("Pages review pick acceptance patch verification passed.")
