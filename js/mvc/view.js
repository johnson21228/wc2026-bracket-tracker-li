import { positionFloatingSurfaceNearAnchor } from "../services/FloatingSurfacePlacement.js";
import { registerFloatingSurfaceDismissal } from "../services/FloatingSurfaceDismissal.js";

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

function groupEntries(groupContext) {
  return groupContext?.standings?.entries || [];
}

export function createBracketView(root) {
  const boardPlane = root.querySelector("[data-board-plane]");
  const boardScroll = root.querySelector("[data-board-scroll]");
  const boardScaleFrame = root.querySelector("[data-board-scale-frame]");
  const boardZoomSelect = root.querySelector("[data-board-zoom]");
  const statusPanel = root.querySelector("[data-status-panel]");
  const clearAllButton = root.querySelector('[data-action="clear-all"]');
  let handlers = {};
  let pendingGroupPanelAnchorBoundsPx = null;
  let pendingGroupPanelAnchorElement = null;
  let boardScale = Number(boardZoomSelect?.value || 1) || 1;
  let boardNativeSize = { width: 1536, height: 1024 };
  const BOARD_MIN_SCALE = 0.5;
  const BOARD_MAX_SCALE = 1.25;
  const BOARD_WHEEL_ZOOM_STEP = 0.08;
  const BOARD_DRAG_PAN_THRESHOLD_PX = 5;
  const BOARD_DOUBLE_CLICK_ZOOM_STEP = 0.18;
  let teardownFloatingSurfaceDismissal = null;

  function activeGameValue() {
    const selected = root.querySelector(".dev-game-selector-option input:checked");
    return selected?.value || root.dataset.activeGame || "game-1";
  }

  function slotEnabledForActiveGame(slot) {
    const activeGame = activeGameValue();
    if (activeGame === "game-1") return slot.round === "R32";
    if (activeGame === "game-2") return slot.round !== "R32";
    return true;
  }

  function disabledReasonForActiveGame(slot) {
    const activeGame = activeGameValue();
    if (activeGame === "game-1" && slot.round !== "R32") {
      return "Game 1 only accepts Round of 32 picks.";
    }
    if (activeGame === "game-2" && slot.round === "R32") {
      return "Game 2 starts after the Round of 32 field.";
    }
    return "";
  }


  function clampBoardScale(value) {
    const numeric = Number(value);
    if (!Number.isFinite(numeric)) return 1;
    return Math.max(BOARD_MIN_SCALE, Math.min(BOARD_MAX_SCALE, numeric));
  }

  function applyBoardRenderScale(nextScale = boardScale) {
    boardScale = clampBoardScale(nextScale);
    const renderWidth = Math.round(boardNativeSize.width * boardScale);
    const renderHeight = Math.round(boardNativeSize.height * boardScale);

    for (const element of [boardScaleFrame, boardPlane]) {
      if (!element) continue;
      element.style.setProperty("--board-w-px", `${boardNativeSize.width}px`);
      element.style.setProperty("--board-h-px", `${boardNativeSize.height}px`);
      element.style.setProperty("--board-render-scale", String(boardScale));
      element.style.setProperty("--board-render-w-px", `${renderWidth}px`);
      element.style.setProperty("--board-render-h-px", `${renderHeight}px`);
    }

    if (boardScaleFrame) {
      boardScaleFrame.style.width = `${renderWidth}px`;
      boardScaleFrame.style.height = `${renderHeight}px`;
    }

    syncBoardZoomSelect();
  }

  function syncBoardZoomSelect() {
    if (!boardZoomSelect) return;
    const existingOptions = Array.from(boardZoomSelect.options || []);
    const matchingOption = existingOptions.find((option) => Math.abs(Number(option.value) - boardScale) < 0.001);
    if (matchingOption) {
      boardZoomSelect.value = matchingOption.value;
      return;
    }

    let customOption = boardZoomSelect.querySelector("option[data-board-zoom-custom]");
    if (!customOption) {
      customOption = document.createElement("option");
      customOption.setAttribute("data-board-zoom-custom", "true");
      boardZoomSelect.appendChild(customOption);
    }
    const percent = Math.round(boardScale * 100);
    customOption.value = String(boardScale);
    customOption.textContent = `${percent}%`;
    boardZoomSelect.value = customOption.value;
  }

  function zoomBoardAroundPoint(nextScale, clientX, clientY) {
    const viewport = boardScroll || boardPlane.parentElement || boardPlane;
    const nextBoardScale = clampBoardScale(nextScale);
    if (Math.abs(nextBoardScale - boardScale) < 0.001) return;

    const viewportRect = viewport.getBoundingClientRect();
    const pointerX = clientX - viewportRect.left;
    const pointerY = clientY - viewportRect.top;
    const nativeX = ((viewport.scrollLeft || 0) + pointerX) / boardScale;
    const nativeY = ((viewport.scrollTop || 0) + pointerY) / boardScale;

    applyBoardRenderScale(nextBoardScale);

    viewport.scrollLeft = Math.max(0, (nativeX * boardScale) - pointerX);
    viewport.scrollTop = Math.max(0, (nativeY * boardScale) - pointerY);
    handlers.onCloseMenu?.();
  }

  function floatingSurfaceIsOpen() {
    return Boolean(boardPlane?.querySelector(".pick-menu-popover, .group-panel-popover"));
  }

  function dismissFloatingSurfaces() {
    if (!floatingSurfaceIsOpen()) return;
    handlers.onCloseMenu?.();
    renderMenu(null);
    renderGroupPanel(null);
  }



  function isBoardPanInteractiveTarget(target) {
    const element = target?.closest?.(`
      button,
      a,
      select,
      input,
      textarea,
      [role="button"],
      [data-action],
      [data-board-zoom],
      [data-rules-panel],
      [data-rules-panel-open],
      [data-game-selector],
      [data-game-selector-button],
      [data-dev-game-selector],
      [data-pick-button],
      [data-pick-slot-button],
      [data-r32-pick-button],
      .r32-pick-slot-button,
      .group-rail-button,
      .group-button,
      .pick-menu-popover,
      .r32-pick-menu-popover,
      .group-panel-popover,
      .rules-panel,
      .banner-game-selector,
      .board-zoom-controls,
      [data-menu-layer],
      [data-pick-menu-layer],
      [data-group-panel-layer]
    `);
    return Boolean(element);
  }

  function installMouseBoardDragPan() {
    if (!boardScroll || boardScroll.dataset.mouseDragPanInstalled === "true") return;
    boardScroll.dataset.mouseDragPanInstalled = "true";

    let dragState = null;

    function clearDragState() {
      if (!dragState) return;
      boardScroll.classList.remove("is-drag-panning");
      boardScroll.classList.remove("is-drag-pan-armed");
      dragState = null;
    }

    boardScroll.addEventListener("pointerdown", (event) => {
      if (event.pointerType === "touch") return;
      if (event.pointerType && event.pointerType !== "mouse") return;
      if (!event.isPrimary) return;
      if (event.button !== 0) return;
      if (isBoardPanInteractiveTarget(event.target)) return;

      dragState = {
        pointerId: event.pointerId,
        startClientX: event.clientX,
        startClientY: event.clientY,
        startScrollLeft: boardScroll.scrollLeft || 0,
        startScrollTop: boardScroll.scrollTop || 0,
        dragging: false,
      };
      boardScroll.classList.add("is-drag-pan-armed");
      boardScroll.setPointerCapture?.(event.pointerId);
    });

    boardScroll.addEventListener("pointermove", (event) => {
      if (!dragState || event.pointerId !== dragState.pointerId) return;
      if (event.pointerType === "touch") return;

      const deltaX = event.clientX - dragState.startClientX;
      const deltaY = event.clientY - dragState.startClientY;
      const movedEnough = Math.hypot(deltaX, deltaY) >= BOARD_DRAG_PAN_THRESHOLD_PX;
      if (!dragState.dragging && !movedEnough) return;

      dragState.dragging = true;
      boardScroll.classList.add("is-drag-panning");
      event.preventDefault();
      boardScroll.scrollLeft = dragState.startScrollLeft - deltaX;
      boardScroll.scrollTop = dragState.startScrollTop - deltaY;
    });

    boardScroll.addEventListener("pointerup", (event) => {
      if (!dragState || event.pointerId !== dragState.pointerId) return;
      clearDragState();
    });

    boardScroll.addEventListener("pointercancel", (event) => {
      if (!dragState || event.pointerId !== dragState.pointerId) return;
      clearDragState();
    });

    boardScroll.addEventListener("lostpointercapture", (event) => {
      if (!dragState || event.pointerId !== dragState.pointerId) return;
      clearDragState();
    });
  }


  function installMouseBoardDoubleClickZoom() {
    if (!boardScroll || boardScroll.dataset.mouseDoubleClickZoomInstalled === "true") return;
    boardScroll.dataset.mouseDoubleClickZoomInstalled = "true";

    let lastBoardPointerDownType = "";

    boardScroll.addEventListener("pointerdown", (event) => {
      lastBoardPointerDownType = event.pointerType || "mouse";
    }, { passive: true });

    boardScroll.addEventListener("dblclick", (event) => {
      if (lastBoardPointerDownType === "touch") return;
      if (lastBoardPointerDownType && lastBoardPointerDownType !== "mouse") return;
      if (isBoardPanInteractiveTarget(event.target)) return;

      event.preventDefault();
      zoomBoardAroundPoint(boardScale + BOARD_DOUBLE_CLICK_ZOOM_STEP, event.clientX, event.clientY);
    }, { passive: false });
  }

  function setHandlers(nextHandlers) {
    handlers = nextHandlers;
    if (!teardownFloatingSurfaceDismissal) {
      teardownFloatingSurfaceDismissal = registerFloatingSurfaceDismissal({
        root: document,
        surfaceSelectors: [".pick-menu-popover", ".group-panel-popover"],
        active: floatingSurfaceIsOpen,
        onDismiss: dismissFloatingSurfaces,
      });
    }
    clearAllButton?.addEventListener("click", () => handlers.onClearAll?.());
    root.addEventListener("change", (event) => {
      if (
        event.target instanceof HTMLInputElement &&
        event.target.closest(".dev-game-selector-option")
      ) {
        handlers.onActiveGameChange?.(activeGameValue());
      }
    });
    boardZoomSelect?.addEventListener("change", () => {
      applyBoardRenderScale(boardZoomSelect.value);
      handlers.onCloseMenu?.();
    });
    installMouseBoardDragPan();
    installMouseBoardDoubleClickZoom();
    boardScroll?.addEventListener("wheel", (event) => {
      const wantsBoardZoom = event.ctrlKey || event.metaKey;
      if (!wantsBoardZoom) return;
      event.preventDefault();
      const direction = event.deltaY > 0 ? -1 : 1;
      zoomBoardAroundPoint(boardScale + (direction * BOARD_WHEEL_ZOOM_STEP), event.clientX, event.clientY);
    }, { passive: false });
    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape") {
        dismissFloatingSurfaces();
      }
    });
  }

  function renderBoardShell(nativeSize) {
    boardNativeSize = nativeSize;
    applyBoardRenderScale(boardScale);
    boardPlane.innerHTML = `
      <img class="board-background-layer" src="assets/board/pub_background_game1.jpeg" alt="" aria-hidden="true">
      <img class="board-linework-layer" src="assets/board/gameboard.svg" alt="" aria-hidden="true">
      <div class="board-pick-layer" data-pick-layer></div>
      <div class="board-final-four-layer" data-final-four-layer></div>
      <div class="board-menu-layer" data-menu-layer></div>
      <div class="board-group-rail-layer" data-group-rail-layer></div>
      <div class="board-group-panel-layer" data-group-panel-layer></div>
    `;
  }


  function unpickedSlotDisplayText(slot) {
    return playerFacingEmptyPickText(slot);
  }


  function displayTeamForSlot(slot) {
    if (activeGameValue() === "game-2" && slot.round === "R32" && slot.game2ResolvedTeam) {
      return slot.game2ResolvedTeam;
    }
    return slot.selectedTeam;
  }

  function isGame2ResolvedR32Display(slot, displayTeam) {
    return activeGameValue() === "game-2" && slot.round === "R32" && Boolean(displayTeam) && Boolean(slot.game2ResolvedTeam);
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
      const enabledForActiveGame = slotEnabledForActiveGame(slot);
      const activeGameDisabledReason = disabledReasonForActiveGame(slot);
      const displayTeam = displayTeamForSlot(slot);
      const game2ResolvedR32Display = isGame2ResolvedR32Display(slot, displayTeam);
      const readOnlyGame2R32Display = game2ResolvedR32Display;
      const disabledByPickability = !slot.pickable && !readOnlyGame2R32Display;
      const disabledByActiveGame = !enabledForActiveGame && !readOnlyGame2R32Display;
      button.disabled = disabledByPickability || disabledByActiveGame;
      button.dataset.pickDisabledByActiveGame = enabledForActiveGame ? "false" : "true";
      button.setAttribute(
        "aria-label",
        displayTeam
          ? `${playerFacingSlotLabel(slot)}: ${fullTeamLabel(displayTeam)}`
          : `${playerFacingSlotLabel(slot)}: ${slot.pickable && enabledForActiveGame ? "choose team" : activeGameDisabledReason || "waiting for earlier picks"}`
      );
      applyBounds(button, slot.boundsPx);

      const label = document.createElement("span");
      label.className = "pick-slot-label";
      label.textContent = slot.label;

      const value = document.createElement("span");
      value.className = "pick-slot-value";

      if (displayTeam) {
        const identity = document.createElement("span");
        identity.className = "picked-cell-identity";

        const flag = document.createElement("span");
        flag.className = "picked-cell-flag";
        flag.textContent = displayTeam.flag || "";
        flag.setAttribute("aria-hidden", "true");

        if (slot.boundsPx?.height) {
          flag.style.fontSize = `${Math.max(18, Math.floor(slot.boundsPx.height - 8))}px`;
        }

        const code = document.createElement("span");
        code.className = "picked-cell-code";
        code.textContent = displayTeam.abbr || displayTeam.id || "";

        identity.append(flag, code);
        if (slot.selectedTeam && slot.pickValidity?.state === "invalid") {
          const warning = document.createElement("span");
          warning.className = "picked-cell-warning";
          warning.textContent = "!";
          warning.setAttribute("aria-label", slot.pickValidity.reason || "Invalid pick");
          identity.append(warning);
        }
        value.append(identity);
      } else {
        const unpickedLabel = document.createElement("span");
        unpickedLabel.className = "unpicked-cell-label";
        unpickedLabel.textContent = unpickedSlotDisplayText(slot);
        value.append(unpickedLabel);
      }

      button.append(label, value);
      if (displayTeam) button.classList.add("has-pick");
      if (game2ResolvedR32Display) {
        button.classList.add("has-game2-resolved-r32");
        button.classList.add("has-game2-readonly-r32");
        button.dataset.game2ReadonlyR32 = "true";
        button.setAttribute("data-game2-readonly-r32", "true");
        button.dataset.game2ResolvedR32Source = slot.game2ResolvedSource || "unknown";
        button.setAttribute("data-game2-resolved-r32-source", slot.game2ResolvedSource || "unknown");
      }
      if (!displayTeam) button.classList.add("is-unpicked");
      if (slot.pickValidity?.state === "invalid") {
        button.classList.add("has-invalid-pick");
        button.title = slot.pickValidity.reason || "This pick is invalid under the current standings.";
        button.setAttribute("aria-label", `${slot.label}: invalid pick. ${button.title}`);
      }
      if (slot.pickable && enabledForActiveGame) button.classList.add("is-pickable");
      if (!enabledForActiveGame) {
        button.classList.add("is-disabled-by-active-game");
        button.title = activeGameDisabledReason;
      }
      button.addEventListener("click", () => handlers.onSlotClick?.(slot.slotId));
      layer.append(button);
    }
  }

  function renderFinalFourPanel(finalFourModel) {
    const layer = boardPlane.querySelector("[data-final-four-layer]");
    if (!layer) return;
    layer.innerHTML = "";
    if (!finalFourModel?.boundsPx) return;

    const panel = document.createElement("section");
    panel.className = "final-four-panel";
    panel.dataset.slotId = finalFourModel.slotId;
    panel.setAttribute("aria-label", "Final Four picks");
    applyBounds(panel, finalFourModel.boundsPx);

    const title = document.createElement("h2");
    title.className = "final-four-title";
    title.textContent = finalFourModel.title || "Final Four";
    panel.append(title);

    const semifinalSummary = document.createElement("div");
    semifinalSummary.className = "final-four-semis";
    for (const row of finalFourModel.semifinalRows || []) {
      const line = document.createElement("div");
      line.className = "final-four-semi-row";
      const teams = (row.teams || []).map((team) => team.abbr || team.id).join(" / ") || "waiting";
      const winner = row.winner ? `${row.winner.flag || ""} ${row.winner.abbr || row.winner.id}`.trim() : "pick";
      line.textContent = `${row.label}: ${teams} → ${winner}`;
      semifinalSummary.append(line);
    }
    panel.append(semifinalSummary);

    const list = document.createElement("div");
    list.className = "final-four-pick-list";

    for (const pick of finalFourModel.picks || []) {
      const enabledForActiveGame = slotEnabledForActiveGame(pick);
      const button = document.createElement("button");
      button.type = "button";
      button.className = "final-four-pick-row";
      button.dataset.slotId = pick.slotId;
      button.dataset.round = pick.round;
      button.disabled = !(pick.pickable && enabledForActiveGame);
      button.addEventListener("click", () => handlers.onFinalFourSlotClick?.(pick.slotId));

      const label = document.createElement("span");
      label.className = "final-four-pick-label";
      label.textContent = pick.label;

      const value = document.createElement("span");
      value.className = "final-four-pick-value";
      if (pick.selectedTeam) {
        value.textContent = `${pick.selectedTeam.flag || ""} ${pick.selectedTeam.abbr || pick.selectedTeam.id}`.trim();
        button.classList.add("has-pick");
      } else {
        value.textContent = pick.pickable && enabledForActiveGame ? "Pick" : "Waiting";
        button.classList.add("is-unpicked");
      }

      button.append(label, value);
      list.append(button);
    }

    panel.append(list);
    layer.append(panel);
  }

  function isPlayerFacingPickMenuSourceLabel(text) {
    const value = String(text || "").trim();
    if (!value) return false;
    if (/\bFEEDER\b|^KNOCKOUT-/i.test(value)) return false;
    if (/^[A-Z0-9]+(?:-[A-Z0-9]+)+$/.test(value)) return false;
    return true;
  }


  function isInternalPickSlotId(text) {
    const value = String(text || "").trim();
    return /^(?:[LR]-)?(?:R32|R16|QF|SF|FINAL|CHAMPION|THIRD-PLACE|CENTER-FINAL-FOUR)(?:-\d+)?$/i.test(value)
      || /^KNOCKOUT-/i.test(value);
  }

  function playerFacingSlotLabel(slot) {
    const label = String(slot?.label || slot?.displayLabel || "").trim();
    if (label && !isInternalPickSlotId(label) && isPlayerFacingPickMenuSourceLabel(label)) return label;

    const round = String(slot?.round || "").toUpperCase();
    if (round === "R32") return "Round of 32 pick";
    if (round === "R16") return "Round of 16 pick";
    if (round === "QF") return "Quarterfinal pick";
    if (round === "SF") return "Semifinal pick";
    if (round === "FINAL") return "Final pick";

    const slotId = String(slot?.slotId || "").toUpperCase();
    if (slotId === "CHAMPION") return "Champion pick";
    if (slotId === "THIRD-PLACE-WINNER") return "Third-place pick";

    return "Bracket pick";
  }


  function playerFacingEmptyPickText(slot) {
    return "Choose Team";
  }

  function playerFacingPickMenuTitle(menu, slot) {
    const title = String(menu?.title || "").trim();
    if (title && !isInternalPickSlotId(title) && isPlayerFacingPickMenuSourceLabel(title)) {
      return title;
    }
    return "Make your pick";
  }

  function visibleBoardViewport() {
    const viewport = boardScroll || boardPlane.parentElement || boardPlane;
    return {
      left: (viewport.scrollLeft || 0) / boardScale,
      top: (viewport.scrollTop || 0) / boardScale,
      width: (viewport.clientWidth || boardPlane.clientWidth) / boardScale,
      height: (viewport.clientHeight || boardPlane.clientHeight) / boardScale,
    };
  }



  function boardLocalBoundsForElement(element) {
    const viewport = boardScroll || boardPlane.parentElement || boardPlane;
    const boardRect = boardPlane.getBoundingClientRect();
    const rect = element.getBoundingClientRect();
    return {
      x: (rect.left - boardRect.left + (viewport.scrollLeft || 0)) / boardScale,
      y: (rect.top - boardRect.top + (viewport.scrollTop || 0)) / boardScale,
      width: rect.width / boardScale,
      height: rect.height / boardScale,
    };
  }

  function placeGroupPanelOverAnchor(panel, anchorBoundsPx) {
    // Card 233: shared 50% zoom safe placement uses rendered screen coordinates.
    const anchorElement = pendingGroupPanelAnchorElement;
    positionFloatingSurfaceNearAnchor({
      anchorEl: anchorElement,
      anchorBoundsPx,
      surfaceEl: panel,
      boardPlane,
      viewportEl: boardScroll || boardPlane.parentElement,
      preferredPlacement: "above-then-below",
      bottomControlSelectors: ["[data-group-rail-layer]", ".board-group-rail-layer", ".group-rail", ".bottom-frame-controls"],
      margin: 14,
      gap: 12,
      minWidth: 280,
      maxWidth: 520,
      maxHeight: 640,
    });
  }

  function placePickMenu(popover, anchorBoundsPx, anchorElement = null) {
    // Placement is board-attached; the menu scrolls with the game board.
    // Card 233: shared 50% zoom safe placement uses rendered screen coordinates.
    positionFloatingSurfaceNearAnchor({
      anchorEl: anchorElement,
      anchorBoundsPx,
      surfaceEl: popover,
      boardPlane,
      viewportEl: boardScroll || boardPlane.parentElement,
      preferredPlacement: "right-then-left",
      bottomControlSelectors: ["[data-group-rail-layer]", ".board-group-rail-layer", ".group-rail", ".bottom-frame-controls"],
      margin: 12,
      gap: 10,
      minWidth: 292,
      maxWidth: 340,
      maxHeight: 560,
    });
  }


  function renderGroupRail(groupRail) {
    const layer = boardPlane.querySelector("[data-group-rail-layer]");
    if (!layer) return;
    layer.innerHTML = "";

    const rail = document.createElement("nav");
    rail.className = "group-rail";
    rail.setAttribute("aria-label", "World Cup group panels");

    for (const group of groupRail || []) {
      const button = document.createElement("button");
      button.type = "button";
      button.className = "group-rail-tile";
      button.setAttribute("data-group-rail-button", "true");
      button.dataset.groupId = group.groupId;
      button.setAttribute("aria-label", group.accessibleLabel || `Open ${group.label} panel`);
      button.addEventListener("click", () => {
        pendingGroupPanelAnchorBoundsPx = boardLocalBoundsForElement(button);
        pendingGroupPanelAnchorElement = button;
        handlers.onGroupPanelOpen?.(group.groupId);
      });

      const label = document.createElement("span");
      label.className = "group-rail-label";
      label.textContent = group.label;

      const flagGrid = document.createElement("span");
      flagGrid.className = "group-rail-flag-grid";
      flagGrid.setAttribute("aria-hidden", "true");

      for (const team of (group.teams || []).slice(0, 4)) {
        const flag = document.createElement("span");
        flag.className = "group-rail-flag";
        flag.title = team.name || team.abbr || team.id;
        flag.textContent = team.flag || team.abbr || team.id;
        flagGrid.append(flag);
      }

      button.append(label, flagGrid);
      rail.append(button);
    }

    layer.append(rail);
  }

  function renderMenu(menuModel) {
    const layer = boardPlane.querySelector("[data-menu-layer]");
    layer.innerHTML = "";
    if (!menuModel || !menuModel.pickable) return;

    const popover = document.createElement("section");
    popover.className = "pick-menu-popover pick-menu-runtime-v2";
    popover.dataset.slotId = menuModel.slotId;
    popover.style.left = "0px";
    popover.style.top = "0px";

    const topbar = document.createElement("div");
    topbar.className = "pick-menu-topbar";

    const titleBlock = document.createElement("div");
    titleBlock.className = "pick-menu-title-block";

    const title = document.createElement("h2");
    title.className = "pick-menu-title";
    title.textContent = playerFacingPickMenuTitle(menuModel, menuModel);

    const source = document.createElement("div");
    source.className = "pick-menu-source-label";
    const sourceLabel = String(menuModel.sourceLabel || "").trim();
    const shouldRenderSourceLabel =
      sourceLabel
      && !isInternalPickSlotId(sourceLabel)
      && !/^[123][A-L]$/i.test(sourceLabel)
      && isPlayerFacingPickMenuSourceLabel(sourceLabel);
    if (shouldRenderSourceLabel) {
      source.textContent = sourceLabel;
      titleBlock.append(title, source);
    } else {
      titleBlock.append(title);
    }

    const close = document.createElement("button");
    close.type = "button";
    close.className = "pick-menu-close-button";
    close.textContent = "× Close";
    close.addEventListener("click", () => handlers.onCloseMenu?.());

    topbar.append(titleBlock, close);
    popover.append(topbar);

    if (menuModel.currentPick) {
      const current = document.createElement("div");
      current.className = "pick-menu-current-pick";
      current.textContent = `Current pick: ${fullTeamLabel(menuModel.currentPick)}`;
      popover.append(current);
    }

    if (menuModel.canClear) {
      const clear = document.createElement("button");
      clear.type = "button";
      clear.className = "pick-menu-clear-top";
      clear.textContent = "Clear this pick";
      clear.addEventListener("click", () => handlers.onClearPick?.(menuModel.slotId));
      popover.append(clear);
    }

    const sections = document.createElement("div");
    sections.className = "pick-menu-group-sections";

    for (const group of menuModel.groups || []) {
      const section = document.createElement("section");
      section.className = "pick-menu-group-section";

      const groupHeader = document.createElement("div");
      groupHeader.className = "pick-menu-group-header";

      if (group.panelAvailable && group.groupId) {
        const groupButton = document.createElement("button");
        groupButton.type = "button";
        groupButton.className = "pick-menu-group-label";
        groupButton.setAttribute("data-group-panel-action", "open");
        groupButton.dataset.groupId = group.groupId;
        groupButton.textContent = group.label;
        groupButton.addEventListener("click", (event) => {
          event.stopPropagation();
          pendingGroupPanelAnchorBoundsPx = boardLocalBoundsForElement(groupButton);
          pendingGroupPanelAnchorElement = groupButton;
          handlers.onGroupPanelOpen?.(group.groupId);
        });
        groupHeader.append(groupButton);

        if (isPlayerFacingPickMenuSourceLabel(group.sourceRole)) {
          const sourceRole = document.createElement("span");
          sourceRole.className = "pick-menu-group-role";
          sourceRole.textContent = group.sourceRole;
          groupHeader.append(sourceRole);
        }

        section.append(groupHeader);
      }

      const list = document.createElement("div");
      list.className = "pick-menu-list";
      for (const team of group.choices || []) {
        const item = document.createElement("button");
        item.type = "button";
        item.className = "pick-menu-item";
        if (menuModel.currentPick?.id === team.id) item.classList.add("is-current");
        item.textContent = fullTeamLabel(team);
        item.addEventListener("click", () => handlers.onTeamPick?.(menuModel.slotId, team.id));
        list.append(item);
      }
      section.append(list);
      sections.append(section);
    }

    popover.append(sections);
    layer.append(popover);
    const anchorElement = Array.from(boardPlane.querySelectorAll("[data-slot-id]")).find((node) => node.dataset.slotId === menuModel.slotId) || null;
    placePickMenu(popover, menuModel.anchorBoundsPx, anchorElement);
  }


  function formatKickoff(match) {
    if (!match?.kickoffLocal) return "Time TBD";
    try {
      return new Date(match.kickoffLocal).toLocaleString([], {
        month: "short",
        day: "numeric",
        hour: "numeric",
        minute: "2-digit",
      });
    } catch {
      return match.kickoffLocal;
    }
  }

  function isCompletedMatch(match) {
    return match?.evidenceStatus === "completed" || match?.status === "final" || match?.status === "complete" || match?.status === "completed";
  }

  function matchResultText(match) {
    if (isCompletedMatch(match)) {
      return `${match.homeTeamName || match.homeTeamId} ${match.homeScore ?? ""}–${match.awayScore ?? ""} ${match.awayTeamName || match.awayTeamId}`;
    }
    return `${match.homeTeamName || match.homeTeamId} vs ${match.awayTeamName || match.awayTeamId}`;
  }

  function qualificationText(entry) {
    return String(entry.qualificationContext || "group context").replaceAll("-", " ");
  }

  function highlightUrl(match) {
    return match?.highlight?.url || match?.highlightUrl || "";
  }

  function highlightLabel(match) {
    return match?.highlight?.label || "Highlights ↗";
  }

  function renderMatchEvidence(panel, titleText, matches, emptyText) {
    const section = document.createElement("section");
    section.className = "group-panel-matches";

    const heading = document.createElement("h3");
    heading.textContent = titleText;
    section.append(heading);

    if (!matches?.length) {
      const empty = document.createElement("p");
      empty.className = "group-panel-empty";
      empty.textContent = emptyText;
      section.append(empty);
      panel.append(section);
      return;
    }

    for (const match of matches) {
      const completed = isCompletedMatch(match);
      const url = completed ? highlightUrl(match) : "";
      const card = url ? document.createElement("a") : document.createElement("article");
      card.className = url ? "group-panel-match-card group-panel-highlight-action" : "group-panel-match-card";
      if (url) {
        card.href = url;
        card.target = "_blank";
        card.rel = "noopener noreferrer";
        card.setAttribute("aria-label", `${matchResultText(match)} highlights`);
      }

      const status = document.createElement("div");
      status.className = "group-panel-status-pill";
      status.textContent = completed ? "result" : (match.status || match.evidenceStatus || "scheduled");

      const line = document.createElement("div");
      line.className = "group-panel-match-line";
      line.textContent = matchResultText(match);

      const meta = document.createElement("div");
      meta.className = "group-panel-match-time";
      meta.textContent = completed ? "Completed" : formatKickoff(match);

      card.append(status, line, meta);

      if (url) {
        const linkLabel = document.createElement("span");
        linkLabel.className = "group-panel-highlight-link";
        linkLabel.textContent = highlightLabel(match);
        card.append(linkLabel);
      }

      section.append(card);
    }

    panel.append(section);
  }

  function renderGroupPanel(groupContext) {
    const layer = boardPlane.querySelector("[data-group-panel-layer]");
    layer.innerHTML = "";
    if (!groupContext) return;

    const panel = document.createElement("aside");
    panel.className = "group-panel-popover group-panel-runtime-v1";

    const topbar = document.createElement("div");
    topbar.className = "group-panel-topbar";

    const titleBlock = document.createElement("div");
    titleBlock.className = "group-panel-title-block";

    const title = document.createElement("h2");
    title.textContent = groupContext.label || `Group ${groupContext.groupId}`;

    const sourceStatus = document.createElement("p");
    sourceStatus.className = "group-panel-source-status";
    sourceStatus.textContent = groupContext.sourceSummary || "Local checked-in standings snapshot.";

    titleBlock.append(title, sourceStatus);

    const close = document.createElement("button");
    close.type = "button";
    close.className = "group-panel-close-button";
    close.textContent = "× Close";
    close.addEventListener("click", () => renderGroupPanel(null));

    topbar.append(titleBlock, close);
    panel.append(topbar);

    const table = document.createElement("table");
    table.className = "group-panel-table group-panel-standings";
    table.innerHTML = `<thead><tr><th>Rank</th><th>Team</th><th>MP</th><th>W</th><th>D</th><th>L</th><th>GF</th><th>GA</th><th>GD</th><th>Pts</th></tr></thead>`;
    const body = document.createElement("tbody");
    for (const entry of groupContext.entries || groupEntries(groupContext)) {
      const row = document.createElement("tr");
      row.innerHTML = `<td>${entry.rank ?? ""}</td><td>${entry.name || entry.abbr}</td><td>${entry.played ?? ""}</td><td>${entry.wins ?? ""}</td><td>${entry.draws ?? ""}</td><td>${entry.losses ?? ""}</td><td>${entry.goalsFor ?? ""}</td><td>${entry.goalsAgainst ?? ""}</td><td>${entry.goalDifference ?? ""}</td><td>${entry.points ?? ""}</td>`;
      body.append(row);
    }
    table.append(body);
    panel.append(table);

    renderMatchEvidence(panel, "Completed matches", groupContext.completedMatches || [], "No completed matches in the local snapshot yet.");
    renderMatchEvidence(panel, "Upcoming matches", groupContext.upcomingMatches || [], "No upcoming matches in the local snapshot.");

    const source = document.createElement("p");
    source.className = "group-panel-source";
    source.textContent = "Local checked-in model data only. Runtime does not scrape ESPN.";
    panel.append(source);

    layer.append(panel);

    const anchorBoundsPx = pendingGroupPanelAnchorBoundsPx;
    const anchorElement = pendingGroupPanelAnchorElement;
    pendingGroupPanelAnchorBoundsPx = null;
    pendingGroupPanelAnchorElement = null;
    placeGroupPanelOverAnchor(panel, anchorBoundsPx);
  }

  function render(state) {
    renderSlots(state.slotModels);
    renderFinalFourPanel(state.finalFour);
    renderGroupRail(state.groupRail);
    renderMenu(state.openPickMenu);
    statusPanel.textContent = `${state.summary.picked} picks made. ${state.summary.pickable} slots are currently pickable.`;
  }

  function closeMenu() {
    renderMenu(null);
  }

  function openGroupPanel(groupContext) {
    renderGroupPanel(groupContext);
  }

  function report(message) {
    statusPanel.textContent = message;
  }

  return { setHandlers, renderBoardShell, render, closeMenu, openGroupPanel, report, activeGameValue };
}
