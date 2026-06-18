export function createBracketController({ model, view }) {
  let activeSlotId = null;

  function currentState() {
    return {
      slotModels: model.getSlotViewModels(),
      groupRail: model.getGroupRail(),
      openPickMenu: activeSlotId ? model.getPickMenu(activeSlotId) : null,
      summary: model.getSummary(),
    };
  }

  function redraw() {
    view.render(currentState());
  }

  function slotModel(slotId) {
    return currentState().slotModels.find((slot) => slot.slotId === slotId) || null;
  }

  function onSlotClick(slotId) {
    const slot = slotModel(slotId);
    if (!slot?.pickable) {
      view.report(`${slotId} is waiting for its feeder picks.`);
      return;
    }
    activeSlotId = slotId;
    redraw();
  }

  function onCloseMenu() {
    activeSlotId = null;
    view.closeMenu();
    redraw();
  }

  function onTeamPick(slotId, teamId) {
    const result = model.setPick(slotId, teamId);
    if (!result.ok) {
      view.report(result.reason || "Pick was not accepted.");
      return;
    }
    activeSlotId = null;
    redraw();
    if (result.cleared?.length) {
      view.report(`Pick saved. Cleared downstream picks: ${result.cleared.join(", ")}.`);
    }
  }

  function onClearPick(slotId) {
    const result = model.clearPick(slotId);
    activeSlotId = slotId;
    redraw();
    if (result.cleared?.length) {
      view.report(`Pick cleared. Cleared downstream picks: ${result.cleared.join(", ")}.`);
    } else {
      view.report("Pick cleared.");
    }
  }

  function onGroupPanelOpen(groupId) {
    const groupContext = model.getGroupContext(groupId);
    view.openGroupPanel(groupContext);
    view.report(`Opened Group ${groupId} standings.`);
  }

  function onClearAll() {
    model.clearAll();
    activeSlotId = null;
    view.closeMenu();
    redraw();
    view.report("All picks cleared.");
  }

  function onExportPicks() {
    const snapshot = model.exportPicksSnapshot();
    const payload = JSON.stringify(snapshot, null, 2);
    const blob = new Blob([payload], { type: "application/json" });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    const date = new Date().toISOString().slice(0, 10);
    link.href = url;
    link.download = `braketeering-pub-picks-${date}.json`;
    document.body.append(link);
    link.click();
    link.remove();
    URL.revokeObjectURL(url);
    view.report("Exported picks JSON snapshot.");
  }

  function onImportPicks(text, fileName = "picks JSON") {
    let snapshot;
    try {
      snapshot = JSON.parse(text);
    } catch {
      view.report("Import failed: JSON could not be parsed.");
      return;
    }
    const result = model.importPicksSnapshot(snapshot);
    if (!result.ok) {
      view.report(result.reason || "Import failed.");
      return;
    }
    activeSlotId = null;
    view.closeMenu();
    redraw();
    const skipped = result.skipped?.length ? ` Skipped ${result.skipped.length} invalid picks.` : "";
    view.report(`Imported ${result.imported} picks from ${fileName}.${skipped}`);
  }

  function start() {
    view.renderBoardShell(model.nativeSize);
    view.setHandlers({ onSlotClick, onTeamPick, onClearPick, onClearAll, onExportPicks, onImportPicks, onCloseMenu, onGroupPanelOpen });
    redraw();
  }

  return { start };
}
