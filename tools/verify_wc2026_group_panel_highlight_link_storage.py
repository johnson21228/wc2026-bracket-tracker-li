#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]

highlights_path = ROOT / "site/data/current/match_highlights.json"
view_path = ROOT / "site/js/mvc/view.js"

missing = []

if not highlights_path.exists():
    missing.append("missing site/data/current/match_highlights.json")
else:
    data = json.loads(highlights_path.read_text())
    highlights = data.get("highlights")

    if not isinstance(highlights, dict):
        missing.append("match_highlights.json must contain a highlights object")
    else:
        # Sentinel: prove at least one verified completed-match highlight is stored.
        arg = highlights.get("66457018")
        if not arg:
            missing.append("missing Argentina 3-0 Algeria highlight entry 66457018")
        elif not isinstance(arg, dict):
            missing.append("Argentina 3-0 Algeria highlight entry 66457018 must be an object")
        elif not str(arg.get("url", "")).startswith("https://"):
            missing.append("Argentina 3-0 Algeria highlight entry must use an https URL")

        for match_id, entry in highlights.items():
            if not isinstance(entry, dict):
                missing.append(f"highlight entry {match_id} must be an object")
                continue

            url = entry.get("url", "")
            if url and not str(url).startswith("https://"):
                missing.append(f"highlight entry {match_id} must use an https highlight URL")

            if url:
                for term in ["provider", "title", "verifiedAt", "matchEvidence"]:
                    if term not in entry:
                        missing.append(f"highlight entry {match_id} is missing {term}")

if not view_path.exists():
    missing.append("missing site/js/mvc/view.js")
else:
    view = view_path.read_text()
    for term in [
        "highlightUrl",
        "group-panel-highlight-action",
        'target = "_blank"',
        "noopener noreferrer",
    ]:
        if term not in view:
            missing.append(f"site/js/mvc/view.js is missing required term: {term}")

if missing:
    raise SystemExit(
        "WC2026 group panel highlight link storage verification failed:\n- "
        + "\n- ".join(missing)
    )

print("WC2026 group panel highlight link storage verification passed.")
