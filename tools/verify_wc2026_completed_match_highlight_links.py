#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
HIGHLIGHTS = ROOT / "site/data/current/match_highlights.json"

missing = []

if not HIGHLIGHTS.exists():
    missing.append("missing site/data/current/match_highlights.json")
else:
    highlights = json.loads(HIGHLIGHTS.read_text())
    store = highlights.get("highlights", {})

    if not isinstance(store, dict):
        missing.append("match_highlights.json highlights must be an object")
    else:
        required_completed = {
            "66456928": "Brazil 1-1 Morocco",
            "66457018": "Argentina 3-0 Algeria",
        }

        for match_id, label in required_completed.items():
            entry = store.get(match_id)
            if not isinstance(entry, dict):
                missing.append(f"{match_id} {label} missing highlight entry")
                continue

            url = entry.get("url", "")
            if not isinstance(url, str) or not url.startswith("https://"):
                missing.append(f"{match_id} {label} must use an https highlight URL")

            for term in ["provider", "title", "verifiedAt", "matchEvidence"]:
                if term not in entry:
                    missing.append(f"{match_id} {label} missing {term}")

if missing:
    raise SystemExit(
        "WC2026 completed match highlight link verification failed:\n- "
        + "\n- ".join(missing)
    )

print("WC2026 completed match highlight link verification passed.")
