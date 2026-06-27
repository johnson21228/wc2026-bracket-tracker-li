#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
view = (ROOT / "site/js/mvc/view.js").read_text()
css = (ROOT / "site/css/app.css").read_text()

errors = []

def require(condition, message):
    if not condition:
        errors.append(message)

require('function buildTeamGroupShortcutLookup(groupRail)' in view,
        "R32 shortcut must build fallback group lookup from rendered group rail")
require('function teamGroupShortcutIdFromLookup(team, lookup)' in view,
        "R32 shortcut must derive group id from team id/abbr/name when display team lacks group field")
require('renderSlots(state.slotModels, state.groupRail);' in view,
        "render must pass group rail into slot rendering for R32 group shortcut fallback")
require('teamGroupShortcutId(displayTeam) || teamGroupShortcutIdFromLookup(displayTeam, teamGroupShortcutLookup)' in view,
        "R32 shortcut must use direct team group first, then group rail lookup fallback")
require('const interactionMode = hasR32GroupShortcut' in view,
        "R32 shortcut must use explicit interaction mode")
require('button.dataset.interactionMode = interactionMode;' in view,
        "R32 shortcut must expose interaction mode for DOM/debugging")
require('button.disabled = interactionMode === "none";' in view,
        "only non-interactive cells may be disabled")
require('interactionMode === "readonly-group-panel"' in view,
        "resolved R32 cells must be readonly group-panel buttons, not pickable buttons")
require('interactionMode === "editable-pick"' in view,
        "editable pick cells must remain a separate interaction mode")
require('button.classList.add("is-readonly-inspectable");' in view,
        "resolved R32 cells must have explicit readonly inspectable styling hook")
require('const hasR32GroupShortcut = Boolean(r32GroupShortcutId);' in view,
        "missing explicit R32 shortcut interaction mode")
require('button.disabled = interactionMode === "none";' in view,
        "resolved R32 group shortcut buttons must not be disabled")
require('function openR32GroupPanelFromButton(button)' in view,
        "R32 shortcut must have a shared opener function")
require('boardPlane.addEventListener("click", (event)' in view,
        "R32 shortcut must have a delegated board-plane click fallback")
require('[data-r32-group-panel-shortcut=\'true\']' in view or '[data-r32-group-panel-shortcut="true"]' in view,
        "R32 delegated fallback must target the explicit shortcut marker")
require('const slotId = button?.dataset?.slotId || "";' in view,
        "R32 group-panel shortcut must read the clicked slot id")
require('if (slotId) handlers.onSlotClick?.(slotId);' in view,
        "R32 group-panel shortcut must reuse the normal slot preselection path")
require('openR32GroupPanelFromButton(shortcutButton);' in view,
        "R32 delegated fallback must open the group panel from the clicked shortcut button")
require('button.dataset.r32GroupPanelShortcut = "true";' in view,
        "missing R32 group panel shortcut dataset marker")
require('button.setAttribute("data-r32-group-panel-shortcut", "true");' in view,
        "missing DOM attribute marker for R32 group panel shortcut")
require('button.classList.add("is-pickable");' in view,
        "resolved R32 shortcut must get pickable/preselect affordance class")
require('button.addEventListener("click", openR32GroupPanel);' in view,
        "resolved R32 shortcut must open group panel on click/tap")
require('button.addEventListener("keydown"' in view,
        "resolved R32 shortcut must support keyboard activation")
require('handlers.onSlotClick?.(slot.slotId)' in view,
        "normal non-R32 pick editing path must remain")

require(".pick-slot-button.has-r32-group-shortcut:hover" in css,
        "resolved R32 shortcut must have hover/preselect styling")
require(".pick-slot-button.has-r32-group-shortcut:focus-visible" in css,
        "resolved R32 shortcut must have keyboard focus styling")
require("pointer-events: auto;" in css,
        "resolved R32 shortcut must allow pointer events")

if errors:
    print("WC2026 R32 group panel shortcut verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: resolved R32 cells are enabled read-only tap/hover targets that open their team group panel without restoring R32 pick editing.")
