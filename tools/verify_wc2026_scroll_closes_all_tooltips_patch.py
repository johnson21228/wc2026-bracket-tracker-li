from pathlib import Path

text = Path("site/game1/index.html").read_text(encoding="utf-8")
required = [
    "WB_SCROLL_CLOSES_ALL_TOOLTIPS_START",
    "WC2026_CLOSE_ALL_TOOLTIPS_FOR_SCROLL",
    "wbCloseAllTooltipsForScroll",
    "window.addEventListener('scroll'",
    "document.addEventListener('wheel'",
    "document.addEventListener('touchmove'",
    "wb-side-tooltip",
    "wb-tooltip-anchor-active",
]
missing = [item for item in required if item not in text]
if missing:
    raise SystemExit("Missing scroll-close tooltip markers: " + ", ".join(missing))
print("Scroll closes all tooltips verification passed.")
