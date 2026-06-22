#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

checks = {
    "site/js/mvc/model.js": [
        "completedMatches",
        "upcomingMatches",
        "getMatchHighlights",
        "sourceSummary",
        "thirdPlaceTable",
    ],
    "site/js/mvc/view.js": [
        "group-panel-standings",
        "group-panel-matches",
        "group-panel-match-card",
        "group-panel-status-pill",
        "renderMatchEvidence",
        "isCompletedMatch",
        "matchResultText",
        "target",
        "_blank",
        "noopener noreferrer",
        "group-panel-highlight-action",
        "Time TBD",
    ],
    "site/css/board.css": [
        "group-panel-runtime-v1",
        "board-group-panel-layer",
        "group-panel-standings",
        "group-panel-matches",
        "group-panel-match-card",
        "group-panel-highlight-action",
    ],
    "docs/features/group_panel_runtime_v1.md": [
        "No runtime scraping",
        "completed match card as an external link",
        "target=\"_blank\"",
        "rel=\"noopener noreferrer\"",
        "Third-place source-slot semantics are intentionally out of scope",
    ],
    "capture_back/CAPTURE_BACK_GROUP_PANEL_RUNTIME_V1.md": [
        "Group Panel Runtime v1",
        "checked-in model data only",
        "target=\"_blank\"",
        "does not change third-place menu semantics",
    ],
    "cards/188_implement_group_panel_runtime_v1_card.md": [
        "Card 188",
        "Group Panel Runtime v1",
        "Do not change third-place source-slot semantics",
    ],
}

errors = []
for rel, terms in checks.items():
    path = ROOT / rel
    if not path.exists():
        errors.append(f"Missing required file: {rel}")
        continue
    text = path.read_text()
    missing = [term for term in terms if term not in text]
    if missing:
        errors.append(f"{rel} is missing required terms: {missing}")

makefile = ROOT / "Makefile"
if makefile.exists():
    body = makefile.read_text()
    if "tools/verify_wc2026_group_panel_runtime_v1.py" not in body:
        errors.append("Makefile does not run verify_wc2026_group_panel_runtime_v1.py")
else:
    errors.append("Missing Makefile")

if errors:
    print("WC2026 group panel runtime v1 verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("WC2026 group panel runtime v1 verification passed.")
