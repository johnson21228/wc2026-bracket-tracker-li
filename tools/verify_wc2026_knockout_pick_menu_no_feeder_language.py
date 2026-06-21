#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

model = (ROOT / "site/js/mvc/model.js").read_text()
view = (ROOT / "site/js/mvc/view.js").read_text()

errors = []

if "Feeder choices" in model or "Feeder choices" in view:
    errors.append("player-facing pick menu title still exposes 'Feeder choices'")

if "function isPlayerFacingPickMenuSourceLabel" not in view:
    errors.append("view does not define player-facing source-label guard")

if "FEEDER" not in view or "KNOCKOUT-" not in view:
    errors.append("view guard does not explicitly suppress internal FEEDER/KNOCKOUT source labels")

if "Pick winner" not in model and "Winner choices" not in model:
    errors.append("model does not expose a player-facing knockout winner menu phrase")


if "function isInternalPickSlotId" not in view:
    errors.append("view does not define an internal pick-slot ID guard")

if "function playerFacingPickMenuTitle" not in view:
    errors.append("view does not define a player-facing pick menu title helper")

if "title.textContent = playerFacingPickMenuTitle(" not in view:
    errors.append("pick menu title is not routed through the player-facing title helper")

if "title.textContent = playerFacingPickMenuTitle(menuModel, menuModel)" not in view:
    errors.append("pick menu title helper must use the resolved menu model, not undefined menu/slot variables")

if "title.textContent = menu.title" in view or "title.textContent = slot.slotId" in view:
    errors.append("pick menu title can still expose internal menu title or slot ID")

if "`${slot.slotId}:" in view:
    errors.append("player-facing aria labels still expose internal slot IDs")

if 'groupLabel.textContent = group.label || "Choices"' in view:
    errors.append("non-group knockout menus still render generic section labels such as Winner choices")


if "source.textContent = menuModel.sourceLabel" in view:
    errors.append("pick menu source label still directly exposes menuModel.sourceLabel")

if "titleBlock.append(title, source)" in view and "!isInternalPickSlotId(sourceLabel)" not in view:
    errors.append("pick menu source label append is not guarded against internal/backend IDs")

if 'pick-menu-group-label-static' in view:
    errors.append("non-group static pick-menu group header class is still rendered")

if "groupLabel.textContent = group.label" in view:
    errors.append("non-group knockout menus still render generic section labels such as Winner choices")

if "if (group.panelAvailable && group.groupId)" not in view:
    errors.append("group header rendering is not limited to real group-backed sections")


if "!/^[123][A-L]$/i.test(sourceLabel)" not in view:
    errors.append("short seed/source labels such as 2B are not hidden from pick menu chrome")

if "/^[A-Z0-9]+(?:-[A-Z0-9]+)+$/.test(value)" not in view:
    errors.append("enum-style source roles such as GROUP-RUNNER-UP are not hidden from player UI")


if "function playerFacingEmptyPickText" not in view:
    errors.append("view does not define player-facing empty pick text for blank bracket cells")

visible_slot_id_patterns = [
    "text.textContent = slot.slotId",
    "label.textContent = slot.slotId",
    "name.textContent = slot.slotId",
    "cell.textContent = slot.slotId",
    "button.textContent = slot.slotId",
    "slot.label || slot.slotId",
]
for pattern in visible_slot_id_patterns:
    if pattern in view:
        errors.append(f"visible bracket-cell rendering can still expose internal slot ID via {pattern}")

if "playerFacingEmptyPickText(slot)" not in view:
    errors.append("empty bracket-cell rendering is not routed through player-facing placeholder text")


unpicked_start = view.find("function unpickedSlotDisplayText(slot)")
if unpicked_start == -1:
    errors.append("view does not define unpickedSlotDisplayText")
else:
    unpicked_end = view.find("\n  function ", unpicked_start + 1)
    unpicked_block = view[unpicked_start:unpicked_end if unpicked_end != -1 else len(view)]
    if "return playerFacingEmptyPickText(slot);" not in unpicked_block:
        errors.append("unpickedSlotDisplayText is not routed through playerFacingEmptyPickText")
    if "slot.slotId" in unpicked_block:
        errors.append("unpickedSlotDisplayText still includes slot.slotId")
    if "slot.label" in unpicked_block:
        errors.append("unpickedSlotDisplayText still includes raw slot.label")

if errors:
    print("Knockout pick menu no-feeder-language verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: knockout pick menus suppress internal feeder labels and use player-facing winner language.")
