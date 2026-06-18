export function createBracketController({ model, view }) {
  function currentState() {
    return {
      slotModels: model.getSlotViewModels(),
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
    view.openMenu(slot);
  }

  function onTeamPick(slotId, teamId) {
    const result = model.setPick(slotId, teamId);
    if (!result.ok) {
      view.report(result.reason || "Pick was not accepted.");
      return;
    }
    view.closeMenu();
    redraw();
    if (result.cleared?.length) {
      view.report(`Pick saved. Cleared downstream picks: ${result.cleared.join(", ")}.`);
    }
  }

  function onClearPick(slotId) {
    const result = model.clearPick(slotId);
    view.closeMenu();
    redraw();
    if (result.cleared?.length) {
      view.report(`Pick cleared. Cleared downstream picks: ${result.cleared.join(", ")}.`);
    }
  }

  function onClearAll() {
    model.clearAll();
    view.closeMenu();
    redraw();
    view.report("All picks cleared.");
  }

  function start() {
    view.renderBoardShell(model.nativeSize);
    view.setHandlers({ onSlotClick, onTeamPick, onClearPick, onClearAll });
    redraw();
  }

  return { start };
}
