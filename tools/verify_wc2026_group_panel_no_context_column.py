#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

def read(rel: str) -> str:
    p = ROOT / rel
    if not p.exists():
        print(f"Missing expected file: {rel}")
        sys.exit(1)
    return p.read_text()

view = read("site/js/mvc/view.js")
css = read("site/css/board.css")
errors = []

if '<th>Context</th>' in view:
    errors.append("group panel still renders a Context table header")
if 'group-panel-qualification' in view:
    errors.append("group panel still renders qualification/context badge cells")
if 'group-panel-qualification' in css:
    errors.append("board CSS still contains unused group-panel-qualification badge styling")
for phrase in ["Group Winner", "Runner Up", "Third Place Candidate", "Fourth Place"]:
    if phrase in view:
        errors.append(f"player-facing view still contains context phrase: {phrase}")

required_header = '<th>Rank</th><th>Team</th><th>MP</th><th>W</th><th>D</th><th>L</th><th>GF</th><th>GA</th><th>GD</th><th>Pts</th>'
if required_header not in view:
    errors.append("group panel no longer renders the expected standings stat columns")

required_row_tokens = [
    '${entry.rank ?? ""}',
    '${entry.name || entry.abbr}',
    '${entry.played ?? ""}',
    '${entry.wins ?? ""}',
    '${entry.draws ?? ""}',
    '${entry.losses ?? ""}',
    '${entry.goalsFor ?? ""}',
    '${entry.goalsAgainst ?? ""}',
    '${entry.goalDifference ?? ""}',
    '${entry.points ?? ""}',
]
for token in required_row_tokens:
    if token not in view:
        errors.append(f"group panel row is missing expected token: {token}")

for token in ["renderMatchEvidence(panel, \"Completed matches\"", "highlightUrl(match)", "group-panel-highlight-link"]:
    if token not in view:
        errors.append(f"completed match/highlight rendering token missing: {token}")

runtime_verifier = read("tools/verify_wc2026_group_panel_runtime_v1.py")
if "group-panel-qualification" in runtime_verifier:
    errors.append("runtime verifier still requires the removed qualification badge class")

makefile = read("Makefile")
if "tools/verify_wc2026_group_panel_no_context_column.py" not in makefile:
    errors.append("Makefile does not include the no-context-column verifier")

if errors:
    print("Group panel no-context-column verification failed:")
    for err in errors:
        print(f"- {err}")
    sys.exit(1)

print("OK: WC2026 group panel no longer renders the player-facing Context column while preserving standings stats and match highlights.")
