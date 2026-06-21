#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def fail(message: str) -> None:
    raise SystemExit(f"WC2026 group panel highlight ESPN join verification failed: {message}")


def main() -> int:
    model_path = ROOT / "site/js/mvc/model.js"
    model = model_path.read_text()

    required_snippets = [
        "function getMatchHighlights(match)",
        "currentHighlightsByMatchId.get(String(match.espnMatchId || \"\"))",
        "currentHighlightsByMatchId.get(String(match.matchId || \"\"))",
        "const highlight = getMatchHighlights(match);",
    ]
    for snippet in required_snippets:
        if snippet not in model:
            fail(f"missing model snippet: {snippet}")

    forbidden_snippets = [
        "function getMatchHighlights(matchId)",
        "const highlight = getMatchHighlights(match.matchId);",
    ]
    for snippet in forbidden_snippets:
        if snippet in model:
            fail(f"stale matchId-only lookup remains: {snippet}")

    match_payload = json.loads((ROOT / "site/data/current/group_matches.json").read_text())
    highlight_payload = json.loads((ROOT / "site/data/current/match_highlights.json").read_text())
    matches = match_payload.get("matches", [])
    highlights = highlight_payload.get("highlights", {})

    expected = {
        "66456972": "Netherlands 5-1 Sweden",
        "66457074": "Germany 2-1 Côte d’Ivoire",
        "66457076": "Ecuador 0-0 Curaçao",
        "66456974": "Tunisia 0-4 Japan",
    }

    by_espn = {str(match.get("espnMatchId")): match for match in matches if match.get("espnMatchId")}
    for espn_id, evidence in expected.items():
        match = by_espn.get(espn_id)
        if not match:
            fail(f"missing group match with espnMatchId {espn_id}")
        highlight = highlights.get(espn_id)
        if not highlight:
            fail(f"missing highlight keyed by ESPN match ID {espn_id}")
        if not highlight.get("url"):
            fail(f"highlight {espn_id} has no url")
        if evidence not in (highlight.get("matchEvidence") or ""):
            fail(f"highlight {espn_id} evidence mismatch; expected {evidence}")
        if str(match.get("matchId", "")).startswith("664"):
            fail(f"matchId for {espn_id} unexpectedly looks like ESPN id; fallback case is not being exercised")

    makefile = (ROOT / "Makefile").read_text()
    if "python3 tools/verify_wc2026_group_panel_highlight_espn_join.py" not in makefile:
        fail("Makefile verify target does not run ESPN highlight join verifier")

    print("OK: WC2026 group panel joins highlight links by ESPN match ID with matchId fallback.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
