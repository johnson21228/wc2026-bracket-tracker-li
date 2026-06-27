#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
view = (ROOT / "site/js/mvc/view.js").read_text()
css = (ROOT / "site/css/app.css").read_text()
makefile = (ROOT / "Makefile").read_text()

errors = []

def require(condition, message):
    if not condition:
        errors.append(message)

require('const r32GroupShortcutId = isR32Slot && displayTeam?.group' in view,
        "resolved R32 cells must derive a group shortcut from selected/display team group")
require('&& !r32GroupShortcutId' in view,
        "resolved R32 group shortcut cells must not stay disabled solely because R32 is not pickable")
require('button.classList.add("has-r32-group-shortcut")' in view,
        "resolved R32 group shortcut cells need a class hook")
require('button.dataset.r32GroupShortcut = r32GroupShortcutId' in view,
        "resolved R32 group shortcut cells need a data hook")
require('pendingGroupPanelAnchorBoundsPx = boardLocalBoundsForElement(button);' in view,
        "R32 group shortcut must anchor the group panel to the tapped cell")
require('pendingGroupPanelAnchorElement = button;' in view,
        "R32 group shortcut must track tapped cell as the panel anchor")
require('handlers.onGroupPanelOpen?.(r32GroupShortcutId);' in view,
        "R32 group shortcut must reuse existing group panel open handler")
require('handlers.onSlotClick?.(slot.slotId)' in view,
        "normal non-R32 pick slots must retain existing pick click handler")
require('.pick-slot-button.has-r32-group-shortcut' in css,
        "R32 group shortcut needs CSS cursor affordance")
require('python3 tools/verify_wc2026_r32_group_panel_shortcut.py' in makefile,
        "Makefile must run R32 group panel shortcut verifier")

if errors:
    print("WC2026 R32 group panel shortcut verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: resolved R32 cells open their team group panel without restoring R32 pick editing.")


# R32 group-panel shortcut must be a real tap/preselect target without restoring R32 pick editing.
view = (ROOT / "site/js/mvc/view.js").read_text()
shortcut_checks = {
    'function teamGroupShortcutId(team)': "must derive group shortcut through helper",
    'team?.group || team?.groupId || team?.groupName || team?.pool': "must tolerate multiple team group field names",
    'const r32GroupShortcutId = isR32Slot && displayTeam ? teamGroupShortcutId(displayTeam) : "";': "R32 shortcut must derive from rendered team",
    'const disabledByPickability = !slot.pickable && !readOnlyGame2R32Display && !r32GroupShortcutId;': "R32 shortcut must keep resolved R32 button enabled",
    'button.classList.add("has-r32-group-shortcut")': "R32 shortcut class must be present",
    'button.dataset.r32GroupShortcut = r32GroupShortcutId;': "R32 group id dataset must be present",
    'handlers.onGroupPanelOpen?.(r32GroupShortcutId);': "R32 shortcut must open group panel",
    'if ((slot.pickable || r32GroupShortcutId) && !pickInteractionSuppressed) button.classList.add("is-pickable");': "R32 shortcut must get pickable/preselect visual affordance",
}
for token, message in shortcut_checks.items():
    require(token in view, message)
require('handlers.onSlotClick?.(slot.slotId)' in view, "normal non-R32 pick editing path must remain")
require('if (r32GroupShortcutId)' in view, "R32 shortcut must branch before normal slot click")
