#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MATCHES = ROOT / "site/data/current/group_matches.json"
HIGHLIGHTS = ROOT / "site/data/current/match_highlights.json"

matches = json.loads(MATCHES.read_text())
highlights = json.loads(HIGHLIGHTS.read_text())
store = highlights.get("highlights", {})

completed = [m for m in matches.get("matches", []) if str(m.get("status", "")).lower() in {"final", "complete", "completed"}]
missing = []
for match in completed:
    mid = str(match.get("matchId"))
    entry = store.get(mid)
    if not entry:
        missing.append(f"{mid} {match.get('summary')} missing highlight entry")
        continue
    for key in ["provider", "title", "url", "verifiedAt", "matchEvidence", "verificationNote"]:
        if not entry.get(key):
            missing.append(f"{mid} {match.get('summary')} missing {key}")
    url = entry.get("url", "")
    if not (url.startswith("https://www.foxsports.com/") or url.startswith("https://www.fox.com/") or url.startswith("https://www.youtube.com/")):
        missing.append(f"{mid} {match.get('summary')} has unsupported highlight URL: {url}")
    evidence = entry.get("matchEvidence", "")
    summary = match.get("summary", "")
    if summary and evidence != summary:
        missing.append(f"{mid} matchEvidence mismatch: expected {summary!r}, got {evidence!r}")

view = (ROOT / "site/js/mvc/view.js").read_text()
for term in ["target", "_blank", "noopener noreferrer"]:
    if term not in view:
        missing.append(f"site/js/mvc/view.js missing external link term: {term}")

if missing:
    raise SystemExit("WC2026 completed match highlight link verification failed:\n- " + "\n- ".join(missing))

print(f"WC2026 completed match highlight link verification passed. completed={len(completed)} linked={len(completed)}")
