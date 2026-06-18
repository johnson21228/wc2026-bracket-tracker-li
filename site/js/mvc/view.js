function teamLabel(team) {
  if (!team) return "";
  return `${team.flag ? `${team.flag} ` : ""}${team.abbr || team.id}`;
}

function fullTeamLabel(team) {
  if (!team) return "";
  return `${team.flag ? `${team.flag} ` : ""}${team.name || team.abbr || team.id}`;
}

function applyBounds(element, bounds) {
  element.style.left = `${bounds.x}px`;
  element.style.top = `${bounds.y}px`;
  element.style.width = `${bounds.width}px`;
  element.style.height = `${bounds.height}px`;
}

export function createBracketView(root) {
  const boardPlane = root.querySelector("[data-board-plane]");
  const statusPanel = root.querySelector("[data-status-panel]");
  const clearAllButton = root.querySelector('[data-action="clear-all"]');
  let handlers = {};
  let openSlotId = null;

  function setHandlers(nextHandlers) {
    handlers = nextHandlers;
    clearAllButton?.addEventListener("click", () => handlers.onClearAll?.());
    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape") {
        openSlotId = null;
        renderMenu(null);
      }
    });
  }

  function renderBoardShell(nativeSize) {
    boardPlane.style.setProperty("--board-w-px", `${nativeSize.width}px`);
    boardPlane.style.setProperty("--board-h-px", `${nativeSize.height}px`);
    boardPlane.innerHTML = `
      <img class="board-background-layer" src="assets/board/pub_background.jpeg" alt="" aria-hidden="true">
      <img class="board-linework-layer" src="assets/board/gameboard.svg" alt="" aria-hidden="true">
      <div class="board-pick-layer" data-pick-layer></div>
      <div class="board-menu-layer" data-menu-layer></div>
    `;
  }

  function renderSlots(slotModels) {
    const layer = boardPlane.querySelector("[data-pick-layer]");
    layer.innerHTML = "";
    for (const slot of slotModels) {
      const button = document.createElement("button");
      button.type = "button";
      button.className = "pick-slot-button";
      button.dataset.slotId = slot.slotId;
      button.dataset.round = slot.round;
      button.disabled = !slot.pickable;
      button.setAttribute("aria-label", slot.selectedTeam ? `${slot.slotId}: ${fullTeamLabel(slot.selectedTeam)}` : `${slot.slotId}: ${slot.pickable ? "choose team" : "waiting for feeder picks"}`);
      applyBounds(button, slot.boundsPx);

      const label = document.createElement("span");
      label.className = "pick-slot-label";
      label.textContent = slot.label;

      const value = document.createElement("span");
      value.className = "pick-slot-value";
      value.textContent = slot.selectedTeam ? teamLabel(slot.selectedTeam) : slot.pickable ? "Pick" : "";

      button.append(label, value);
      if (slot.selectedTeam) button.classList.add("has-pick");
      if (slot.pickable) button.classList.add("is-pickable");
      button.addEventListener("click", () => handlers.onSlotClick?.(slot.slotId));
      layer.append(button);
    }
  }

  function renderMenu(slotModel) {
    const layer = boardPlane.querySelector("[data-menu-layer]");
    layer.innerHTML = "";
    if (!slotModel || !slotModel.pickable) return;

    const popover = document.createElement("section");
    popover.className = "pick-menu-popover";
    popover.dataset.slotId = slotModel.slotId;
    const bounds = slotModel.boundsPx;
    popover.style.left = `${Math.min(bounds.x + bounds.width + 8, 1260)}px`;
    popover.style.top = `${Math.max(20, Math.min(bounds.y, 820))}px`;

    const title = document.createElement("h2");
    title.textContent = `${slotModel.label} choices`;
    popover.append(title);

    const list = document.createElement("div");
    list.className = "pick-menu-list";
    for (const team of slotModel.choices) {
      const item = document.createElement("button");
      item.type = "button";
      item.className = "pick-menu-item";
      item.textContent = fullTeamLabel(team);
      item.addEventListener("click", () => handlers.onTeamPick?.(slotModel.slotId, team.id));
      list.append(item);
    }
    popover.append(list);

    if (slotModel.selectedTeam) {
      const clear = document.createElement("button");
      clear.type = "button";
      clear.className = "pick-menu-clear";
      clear.textContent = "Clear this pick";
      clear.addEventListener("click", () => handlers.onClearPick?.(slotModel.slotId));
      popover.append(clear);
    }

    const close = document.createElement("button");
    close.type = "button";
    close.className = "pick-menu-close";
    close.textContent = "Close";
    close.addEventListener("click", () => {
      openSlotId = null;
      renderMenu(null);
    });
    popover.append(close);
    layer.append(popover);
  }

  function render(state) {
    renderSlots(state.slotModels);
    if (openSlotId) {
      renderMenu(state.slotModels.find((slot) => slot.slotId === openSlotId));
    } else {
      renderMenu(null);
    }
    statusPanel.textContent = `${state.summary.picked} picks made. ${state.summary.pickable} slots are currently pickable.`;
  }

  function openMenu(slotModel) {
    openSlotId = slotModel?.slotId || null;
    renderMenu(slotModel);
  }

  function closeMenu() {
    openSlotId = null;
    renderMenu(null);
  }

  function report(message) {
    statusPanel.textContent = message;
  }

  return { setHandlers, renderBoardShell, render, openMenu, closeMenu, report };
}
