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
  const statusPanel = root.querySelector("[data-status-panel]");
  const clearAllButton = root.querySelector('[data-action="clear-all"]');
  let handlers = {};
  let pendingGroupPanelAnchorBoundsPx = null;

  function setHandlers(nextHandlers) {
    handlers = nextHandlers;
    clearAllButton?.addEventListener("click", () => handlers.onClearAll?.());
    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape") {
        handlers.onCloseMenu?.();
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
      <div class="board-group-rail-layer" data-group-rail-layer></div>
      <div class="board-group-panel-layer" data-group-panel-layer></div>
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

  function visibleBoardViewport() {
    const viewport = boardPlane.parentElement || boardPlane;
    return {
      left: viewport.scrollLeft || 0,
      top: viewport.scrollTop || 0,
      width: viewport.clientWidth || boardPlane.clientWidth,
      height: viewport.clientHeight || boardPlane.clientHeight,
    };
  }



  function boardLocalBoundsForElement(element) {
    const viewport = boardPlane.parentElement || boardPlane;
    const boardRect = boardPlane.getBoundingClientRect();
    const rect = element.getBoundingClientRect();
    return {
      x: rect.left - boardRect.left + (viewport.scrollLeft || 0),
      y: rect.top - boardRect.top + (viewport.scrollTop || 0),
      width: rect.width,
      height: rect.height,
    };
  }

  function placeGroupPanelOverAnchor(panel, anchorBoundsPx) {
    const viewport = visibleBoardViewport();
    const margin = 14;
    const visibleRight = viewport.left + viewport.width;
    const visibleBottom = viewport.top + viewport.height;
    const maxPanelWidth = Math.max(280, Math.min(520, viewport.width - margin * 2));
    const maxPanelHeight = Math.max(240, viewport.height - margin * 2);

    panel.style.width = `${Math.round(maxPanelWidth)}px`;
    panel.style.maxHeight = `${Math.round(maxPanelHeight)}px`;

    const panelWidth = panel.offsetWidth || maxPanelWidth;
    const panelHeight = Math.min(panel.scrollHeight || 420, maxPanelHeight);

    let left = viewport.left + margin;
    let top = viewport.top + margin;

    if (anchorBoundsPx) {
      left = anchorBoundsPx.x + anchorBoundsPx.width / 2 - panelWidth / 2;
      top = anchorBoundsPx.y - panelHeight - margin;
      if (top < viewport.top + margin) {
        top = anchorBoundsPx.y + anchorBoundsPx.height + margin;
      }
    }

    left = Math.max(viewport.left + margin, Math.min(left, visibleRight - panelWidth - margin));
    top = Math.max(viewport.top + margin, Math.min(top, visibleBottom - panelHeight - margin));

    panel.style.left = `${Math.round(left)}px`;
    panel.style.top = `${Math.round(top)}px`;
  }

  function placePickMenu(popover, anchorBoundsPx) {
    // Placement is board-attached; the menu scrolls with the game board.
    const viewport = visibleBoardViewport();
    const margin = 12;
    const width = popover.offsetWidth || 292;
    const height = popover.offsetHeight || 420;
    const visibleRight = viewport.left + viewport.width;
    const visibleBottom = viewport.top + viewport.height;

    let left = anchorBoundsPx.x + anchorBoundsPx.width + margin;
    if (left + width > visibleRight - margin) {
      left = anchorBoundsPx.x - width - margin;
    }
    left = Math.max(viewport.left + margin, Math.min(left, visibleRight - width - margin));

    let top = anchorBoundsPx.y;
    top = Math.max(viewport.top + margin, Math.min(top, visibleBottom - height - margin));

    popover.style.left = `${Math.round(left)}px`;
    popover.style.top = `${Math.round(top)}px`;
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
    title.textContent = menuModel.title;

    const source = document.createElement("div");
    source.className = "pick-menu-source-label";
    source.textContent = menuModel.sourceLabel;

    titleBlock.append(title, source);

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
          handlers.onGroupPanelOpen?.(group.groupId);
        });
        groupHeader.append(groupButton);
      } else {
        const groupLabel = document.createElement("span");
        groupLabel.className = "pick-menu-group-label-static";
        groupLabel.textContent = group.label;
        groupHeader.append(groupLabel);
      }

      const sourceRole = document.createElement("span");
      sourceRole.className = "pick-menu-group-role";
      sourceRole.textContent = group.sourceRole || "source";
      groupHeader.append(sourceRole);
      section.append(groupHeader);

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
    placePickMenu(popover, menuModel.anchorBoundsPx);
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
    table.innerHTML = `<thead><tr><th>Rank</th><th>Team</th><th>MP</th><th>W</th><th>D</th><th>L</th><th>GF</th><th>GA</th><th>GD</th><th>Pts</th><th>Context</th></tr></thead>`;
    const body = document.createElement("tbody");
    for (const entry of groupContext.entries || groupEntries(groupContext)) {
      const row = document.createElement("tr");
      const context = qualificationText(entry);
      row.innerHTML = `<td>${entry.rank ?? ""}</td><td>${entry.name || entry.abbr}</td><td>${entry.played ?? ""}</td><td>${entry.wins ?? ""}</td><td>${entry.draws ?? ""}</td><td>${entry.losses ?? ""}</td><td>${entry.goalsFor ?? ""}</td><td>${entry.goalsAgainst ?? ""}</td><td>${entry.goalDifference ?? ""}</td><td>${entry.points ?? ""}</td><td><span class="group-panel-qualification">${context}</span></td>`;
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
    pendingGroupPanelAnchorBoundsPx = null;
    placeGroupPanelOverAnchor(panel, anchorBoundsPx);
  }

  function render(state) {
    renderSlots(state.slotModels);
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

  return { setHandlers, renderBoardShell, render, closeMenu, openGroupPanel, report };
}
