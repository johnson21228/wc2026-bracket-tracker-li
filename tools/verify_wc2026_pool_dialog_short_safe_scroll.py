from pathlib import Path

css_paths = [
    Path("site/css/styles.css"),
    Path("site/css/main.css"),
    Path("site/css/app.css"),
    Path("site/index.html"),
]

text = "\n".join(path.read_text() for path in css_paths if path.exists())

required = [
    "POOL_DIALOG_SHORT_SAFE_SCROLL",
    ".player-standings-card",
    "100dvh",
    "overflow-y: auto",
    "-webkit-overflow-scrolling: touch",
    "overscroll-behavior: contain",
    "touch-action: pan-y",
]

missing = [item for item in required if item not in text]
if missing:
    raise SystemExit("Missing Pool dialog short safe scroll contract: " + ", ".join(missing))

if "calc(100dvh - 240px)" not in text and "calc(100dvh - 210px)" not in text:
    raise SystemExit("Pool dialog does not reserve enough mobile browser chrome clearance.")

print("OK: Pool dialog is intentionally shorter and internally scrollable for mobile Safari browser chrome.")
