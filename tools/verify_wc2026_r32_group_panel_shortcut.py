#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
view = (ROOT / "site/js/mvc/view.js").read_text()
css = (ROOT / "site/css/app.css").read_text()

errors = []

def require(condition, message):
    if not condition:
        errors.append(message)

require('const hasR32GroupShortcut = Boolean(r32GroupShortcutId);' in view,
        "missing explicit R32 shortcut interaction mode")
require('button.disabled = hasR32GroupShortcut ? false :' in view,
        "resolved R32 group shortcut buttons must not be disabled")
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
