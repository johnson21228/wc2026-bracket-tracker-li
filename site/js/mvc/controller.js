export function createBracketController({ model, view }) {
  let activeSlotId = null;

  function currentState() {
    return {
      slotModels: model.getSlotViewModels(),
      finalFour: model.getFinalFourViewModel(),
      groupRail: model.getGroupRail(),
      openPickMenu: activeSlotId ? model.getPickMenu(activeSlotId) : null,
      summary: model.getSummary(),
    };
  }

  function announcePicksChanged() {
    window.dispatchEvent(new CustomEvent("wc2026:picks-changed"));
  }

  function redraw() {
    view.render(currentState());
  }

  function slotModel(slotId) {
    const state = currentState();
    return state.slotModels.find((slot) => slot.slotId === slotId)
      || (state.finalFour?.picks || []).find((slot) => slot.slotId === slotId)
      || null;
  }

  function activeGameValue() {
    return view.activeGameValue?.() || "game-1";
  }

  function slotIsR32(slot) {
    const slotId = String(slot?.slotId || "").toUpperCase();
    return slot?.round === "R32" || slotId.startsWith("R32");
  }

  function adminOfficialEditorActive() {
    return Boolean(model.getSummary?.()?.adminOfficialEditorActive || model.getSummary?.()?.adminOfficialR32EditorActive);
  }

  function slotAllowedForActiveGame(slot) {
    if (adminOfficialEditorActive()) return true;
    if (activeGameValue() !== "game-1") return true;
    return slotIsR32(slot);
  }

  function disabledReasonForActiveGame(slot) {
    if (slotAllowedForActiveGame(slot)) return "";
    return "Later-round picks open when Knockout Stage presentation is active.";
  }

  function pickMenuNotReadyReason(slot) {
    return "";
}

  function reportBlockedPick(slot) {
    const activeGameReason = disabledReasonForActiveGame(slot);
    const notReadyReason = pickMenuNotReadyReason(slot);
    view.report(activeGameReason || notReadyReason || `${slot.slotId} is not ready for picking.`);
  }

  function onSlotClick(slotId) {
    const slot = slotModel(slotId);
    if (!slot) {
      view.report(`${slotId} is not available.`);
      return;
    }
    if (!slotAllowedForActiveGame(slot)) {
      reportBlockedPick(slot);
      return;
    }
    if (!slot.pickable) {
      view.report(pickMenuNotReadyReason(slot) || `${slotId} is waiting for its feeder picks.`);
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
    const slot = slotModel(slotId);
    if (!slot || !slotAllowedForActiveGame(slot) || pickMenuNotReadyReason(slot)) {
      if (slot) reportBlockedPick(slot);
      else view.report(`${slotId} is not available.`);
      redraw();
      return;
    }

    const result = model.setPick(slotId, teamId);
    if (!result.ok) {
      view.report(result.reason || "Pick was not accepted.");
      return;
    }
    announcePicksChanged();
    activeSlotId = null;
    redraw();
    if (result.cleared?.length) {
      view.report(`Pick saved. Cleared downstream picks: ${result.cleared.join(", ")}.`);
    }
  }

  function onClearPick(slotId) {
    const result = model.clearPick(slotId);
    announcePicksChanged();
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

  function onActiveGameChange(activeGame) {
    activeSlotId = null;
    view.closeMenu();
    redraw();
    view.report(activeGame === "game-2" ? "Knockout Stage presentation is active." : "Group Stage presentation is active.");
  }

  function onClearAll() {
    model.clearAll();
    announcePicksChanged();
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
    announcePicksChanged();
    activeSlotId = null;
    view.closeMenu();
    redraw();
    const skipped = result.skipped?.length ? ` Skipped ${result.skipped.length} invalid picks.` : "";
    view.report(`Imported ${result.imported} picks from ${fileName}.${skipped}`);
  }

  function start() {
    view.renderBoardShell(model.nativeSize);
    view.setHandlers({ onSlotClick, onFinalFourSlotClick: onSlotClick, onTeamPick, onClearPick, onClearAll, onExportPicks, onImportPicks, onCloseMenu, onGroupPanelOpen, onActiveGameChange });
    window.addEventListener("wc2026:account-picks-loaded", () => {
      activeSlotId = null;
      view.closeMenu();
      redraw();
      view.report("Loaded your joined picks.");
    });
    redraw();
  }

  return { start };
}
