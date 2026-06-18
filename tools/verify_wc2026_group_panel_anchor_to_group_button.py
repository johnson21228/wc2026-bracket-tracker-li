#!/usr/bin/env python3
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]

def fail(message):
    print(f"FAIL: {message}")
    sys.exit(1)

view = ROOT / "site/js/mvc/view.js"
controller = ROOT / "site/js/mvc/controller.js"
css = ROOT / "site/css/board.css"
makefile = ROOT / "Makefile"
for p in [ROOT/"li/world_cup/group_panel_anchor_rule.md", ROOT/"docs/features/group_panel_anchor_to_group_button.md", ROOT/"cards/194_anchor_group_panel_to_group_button_card.md", ROOT/"capture_back/CAPTURE_BACK_GROUP_PANEL_ANCHOR_SAFE.md"]:
    if not p.exists(): fail(f"missing {p}")
view_text = view.read_text(); controller_text = controller.read_text(); css_text = css.read_text()
for needle, label in [
    ("let pendingGroupPanelAnchorBoundsPx = null;", "view-owned pending anchor"),
    ("function boardLocalBoundsForElement(element)", "board-local DOM bounds helper"),
    ("function placeGroupPanelOverAnchor(panel, anchorBoundsPx)", "safe panel placement helper"),
    ("pendingGroupPanelAnchorBoundsPx = boardLocalBoundsForElement(button);", "group rail button captures anchor"),
    ("placeGroupPanelOverAnchor(panel, anchorBoundsPx);", "panel placement after render"),
]:
    if needle not in view_text: fail(f"missing {label} in view")
if "function onGroupPanelOpen(groupId, anchorBoundsPx" in controller_text:
    fail("controller must not own DOM anchor bounds")
if "view.openGroupPanel(groupContext, anchorBoundsPx)" in controller_text:
    fail("controller must not pass DOM anchor bounds to view")
if "function onGroupPanelOpen(groupId)" not in controller_text:
    fail("controller should keep groupId-only group panel handler")
for needle, label in [
    ("Card 194: group panel anchors to launching group button", "CSS card marker"),
    (".board-group-panel-layer", "group panel layer CSS"),
    ("max-width: calc(100% - 28px);", "panel visible max width"),
    ("overflow: auto;", "panel internal scroll"),
]:
    if needle not in css_text: fail(f"missing {label} in CSS")
if "tools/verify_wc2026_group_panel_anchor_to_group_button.py" not in makefile.read_text():
    fail("Makefile does not run group panel anchor verifier")
print("OK: group panel anchor-to-button runtime is View-owned, board-clamped, and verified.")
