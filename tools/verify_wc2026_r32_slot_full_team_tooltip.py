#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
view = (ROOT / "site/js/mvc/view.js").read_text()

errors = []

def require(condition, message):
    if not condition:
        errors.append(message)

require('if (isR32Slot && displayTeam)' in view,
        "R32 display slots must get an explicit tooltip title when a team is shown")
require('button.title = fullTeamLabel(displayTeam);' in view,
        "R32 tooltip must use the full team label, not only the three-letter code")
require('button.title = `${fullTeamLabel(displayTeam)} — Open ${r32GroupShortcutLabel} panel`;' in view,
        "R32 group-panel shortcut tooltip must preserve the full team name while describing the action")
require('button.title = `Open ${r32GroupShortcutLabel} panel`;' not in view,
        "R32 shortcut tooltip must not hide the team name behind only the group-panel action")
require('${playerFacingSlotLabel(slot)}: ${fullTeamLabel(displayTeam)}' in view,
        "R32 accessibility label must continue to expose the full team name")

if errors:
    print("WC2026 R32 full-team tooltip verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: R32 slots expose full team names in native tooltips while preserving group-panel shortcuts.")
