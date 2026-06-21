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

if errors:
    print("Knockout pick menu no-feeder-language verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: knockout pick menus suppress internal feeder labels and use player-facing winner language.")
