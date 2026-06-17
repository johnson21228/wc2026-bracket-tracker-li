from pathlib import Path

html = Path("site/game1/index.html")
text = html.read_text(encoding="utf-8")

required = [
    "WB_TOOLTIP_SIDE_PLACEMENT_START",
    "wb-side-tooltip",
    "viewportPlacement",
    "rectWithBridge",
    "data-tooltip-action-href",
    "pointermove",
    "tooltip.contains",
    "activeTarget.contains",
]

missing = [item for item in required if item not in text]
if missing:
    raise SystemExit("Missing tooltip side-placement implementation markers: " + ", ".join(missing))

print("Tooltip side placement implementation verification passed.")
