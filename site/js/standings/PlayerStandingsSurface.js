import { areGroupStagePicksLocked, GROUP_STAGE_PICKS_LOCK_AT_MS, GROUP_STAGE_PICKS_LOCK_TIMER_MAX_MS, playerResultsHiddenUntilLockMessage } from "../config/gameLocks.js";

const STANDINGS_PANEL_OPEN_EVENT = "wc2026:standings-panel-opened";
const OFFICIAL_RESULTS_PLAYER_NAMES = new Set(["Admin_", "Official Results"]);

function isOfficialStandingsRow(row) {
  const bracketKind = String(row?.bracketKind || row?.bracket_kind || "").toLowerCase();
  const publicName = String(
    row?.publicPlayerName
      || row?.playerName
      || row?.displayName
      || ""
  ).trim();

  return bracketKind === "official" || OFFICIAL_RESULTS_PLAYER_NAMES.has(publicName);
}
const BOARD_VIEWER_GEOMETRY_URL = "data/geometry/gameboard_manifest.json";
const BOARD_VIEWER_TEAMS_URL = "data/model/teams.json";
const BOARD_VIEWER_LINEWORK_URL = "assets/playfield/uniform_pick_card_gameboard.svg";
const BOARD_VIEWER_DEFAULT_SCALE = 0.75;
const BOARD_VIEWER_MIN_SCALE = 0.5;
const BOARD_VIEWER_MAX_SCALE = 1.25;
const BOARD_VIEWER_SCALE_STEP = 0.25;

function numericScore(value) {
  const number = Number(value);
  return Number.isFinite(number) ? number : 0;
}

function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}

function safePublicPlayerName(row) {
  const name = String(
    row?.publicPlayerName
      || row?.playerName
      || row?.displayName
      || "Player"
  ).trim();

  return name || "Player";
}

function normalizeStandingsRow(row) {
  const groupPoints = Number.isFinite(Number(row?.score))
    ? numericScore(row.score)
    : numericScore(row?.groupPoints);
  const knockoutPoints = Number.isFinite(Number(row?.maxPossible))
    ? numericScore(row.maxPossible)
    : numericScore(row?.knockoutPoints);
  const tiebreakerScore = numericScore(row?.tiebreakerScore);
  const total = Number.isFinite(Number(row?.total))
    ? numericScore(row.total)
    : groupPoints;
  const picksBySlot = row?.picksBySlot && typeof row.picksBySlot === "object" && !Array.isArray(row.picksBySlot)
    ? row.picksBySlot
    : {};
  const picksCount = Number.isFinite(Number(row?.picksCount))
    ? numericScore(row.picksCount)
    : Object.keys(picksBySlot).length;

  const officialTruthPicksBySlot = row?.officialTruthPicksBySlot && typeof row.officialTruthPicksBySlot === "object" && !Array.isArray(row.officialTruthPicksBySlot)
    ? row.officialTruthPicksBySlot
    : {};

  return {
    userId: row?.userId || row?.user_id || row?.ownerUserId || row?.owner_user_id || row?.playerUserId || row?.player_user_id || "",
    publicPlayerName: safePublicPlayerName(row),
    picksBySlot,
    picksCount,
    groupPoints,
    knockoutPoints,
    score: groupPoints,
    maxPossible: knockoutPoints,
    tiebreakerScore,
    total,
    officialTruthPicksBySlot,
    officialResultsTruthSource: row?.officialResultsTruthSource || "",
    officialResultsTruthUserId: row?.officialResultsTruthUserId || "",
    bracketKind: row?.bracketKind || row?.bracket_kind || "player",
  };
}

export function sortPlayerStandingsRows(rows = []) {
  return rows
    .filter((row) => !isOfficialStandingsRow(row))
    .map(normalizeStandingsRow)
    .sort((a, b) => (
      (b.total - a.total)
      || ((b.maxPossible ?? b.knockoutPoints) - (a.maxPossible ?? a.knockoutPoints))
      || (b.tiebreakerScore - a.tiebreakerScore)
      || a.publicPlayerName.localeCompare(b.publicPlayerName)
    ));
}

function publicNameFromAuthState(authState, profileState = null) {
  return profileState?.display_name
    || profileState?.publicPlayerName
    || authState?.profile?.display_name
    || authState?.profile?.publicPlayerName
    || authState?.publicPlayerName
    || authState?.user?.publicPlayerName
    || authState?.user?.user_metadata?.public_player_name
    || authState?.user?.label
    || "Player";
}

function isSignedIn(authState) {
  return authState?.status === "signed-in" || Boolean(authState?.user?.id);
}

async function resolveCurrentProfile({ authState, profileStore }) {
  const userId = authState?.user?.id;
  if (!userId || !profileStore?.getProfile) return null;

  const { profile, error } = await profileStore.getProfile(userId);
  if (error) {
    console.warn("[PlayerStandingsSurface] profile unavailable", error);
    return null;
  }
  return profile || null;
}

function fallbackParticipationRows(authState, profileState = null) {
  if (!isSignedIn(authState)) return [];
  const publicPlayerName = publicNameFromAuthState(authState, profileState);
  if (OFFICIAL_RESULTS_PLAYER_NAMES.has(String(publicPlayerName).trim())) return [];
  return [{
    publicPlayerName,
    picksBySlot: {},
    picksCount: 0,
    groupPoints: 0,
    knockoutPoints: 0,
    tiebreakerScore: 0,
    total: 0,
  }];
}

function ensureStandingsButton(root) {
  let button = root.querySelector("[data-player-standings-open]");
  if (button) return button;

  let controls = root.querySelector("[data-player-standings-control]");
  if (!controls) {
    controls = document.createElement("div");
    controls.className = "player-standings-control";
    controls.setAttribute("data-player-standings-control", "");
    root.append(controls);
  }

  button = document.createElement("button");
  button.type = "button";
  button.className = "standings-icon-button";
  button.setAttribute("data-player-standings-open", "");
  button.setAttribute("aria-haspopup", "dialog");
  button.setAttribute("aria-controls", "player-standings-panel");
  button.setAttribute("aria-label", "Open Pool");
  button.textContent = "Pool";
  controls.append(button);
  return button;
}

function ensureStandingsPanel(root) {
  let panel = root.querySelector("[data-player-standings-panel]");
  if (panel) return panel;

  panel = document.createElement("section");
  panel.id = "player-standings-panel";
  panel.className = "player-standings-panel";
  panel.setAttribute("data-player-standings-panel", "");
  panel.setAttribute("role", "dialog");
  panel.setAttribute("aria-modal", "false");
  panel.setAttribute("aria-labelledby", "player-standings-title");
  panel.hidden = true;
  panel.innerHTML = `
    <div class="player-standings-card">
      <header class="player-standings-header">
        <div>
          <p class="player-standings-kicker">Pool</p>
          <h2 id="player-standings-title">Pool Standings</h2>
        </div>
        <button type="button" class="player-standings-close" data-player-standings-close aria-label="Close Pool Standings">×</button>
      </header>
      <div class="player-standings-body" data-player-standings-body>
        <p class="player-standings-status">Loading standings…</p>
      </div>
    </div>
  `;
  root.append(panel);
  return panel;
}

function ensurePlayerBoardViewerPanel(root) {
  let panel = root.querySelector("[data-player-board-viewer-panel]");
  if (panel) return panel;

  panel = document.createElement("section");
  panel.id = "player-board-viewer-panel";
  panel.className = "player-board-viewer-panel";
  panel.setAttribute("data-player-board-viewer-panel", "");
  panel.setAttribute("role", "dialog");
  panel.setAttribute("aria-modal", "false");
  panel.setAttribute("aria-labelledby", "player-board-viewer-title");
  panel.hidden = true;
  panel.innerHTML = `
    <div class="player-board-viewer-card">
      <header class="player-board-viewer-header">
        <div>
          <p class="player-board-viewer-kicker">Read-only</p>
          <h2 id="player-board-viewer-title" data-player-board-viewer-title>Viewing player picks</h2>
        </div>
        <div class="player-board-viewer-actions">
          <button type="button" class="player-board-viewer-zoom" data-player-board-viewer-zoom-out aria-label="Zoom out viewed board">−</button>
          <select class="player-board-viewer-zoom-select" data-player-board-viewer-zoom aria-label="Viewed board zoom">
            <option value="0.5">50%</option>
            <option value="0.75" selected>75%</option>
            <option value="1">100%</option>
            <option value="1.25">125%</option>
          </select>
          <button type="button" class="player-board-viewer-zoom" data-player-board-viewer-zoom-in aria-label="Zoom in viewed board">+</button>
          <button type="button" class="player-board-viewer-close" data-player-board-viewer-close>Back to my board</button>
        </div>
      </header>
      <p class="player-board-viewer-note">Read-only board viewer. Pan and zoom to inspect this player's public picks.</p>
      <div class="player-board-viewer-scroll" data-player-board-viewer-scroll>
        <div class="player-board-viewer-scale-frame" data-player-board-viewer-scale-frame>
          <div class="player-board-viewer-plane" data-player-board-viewer-plane>
            <p class="player-board-viewer-status">Loading board…</p>
          </div>
        </div>
      </div>
    </div>
  `;
  root.append(panel);
  return panel;
}

function renderStandingsRows(panel, rows, { authState = null, profileState = null } = {}) {
  const body = panel.querySelector("[data-player-standings-body]");
  const sortedRows = sortPlayerStandingsRows(rows);
  const currentUserId = authState?.user?.id || authState?.userId || profileState?.userId || profileState?.profile?.user_id || profileState?.id || null;

  if (!sortedRows.length) {
    body.innerHTML = `<p class="player-standings-status">No players yet</p>`;
    return [];
  }

  const rowMarkup = sortedRows.map((row, index) => {
    const canViewPicks = true;
    const nameMarkup = canViewPicks
      ? `<button type="button" class="player-standings-player-name player-standings-player-picks-button" data-player-standings-row="${index}" title="View ${escapeHtml(row.publicPlayerName)}'s picks">${escapeHtml(row.publicPlayerName)}</button>`
      : `<span class="player-standings-player-name">${escapeHtml(row.publicPlayerName)}</span>`;

    return `
    <tr>
      <td class="player-standings-rank">${index + 1}</td>
      <td class="player-standings-player">
        <div class="player-standings-player-summary">
          ${nameMarkup}
        </div>
      </td>
      <td class="player-standings-score">${row.score ?? row.groupPoints ?? 0}</td>
      <td class="player-standings-max-possible">${row.maxPossible ?? row.knockoutPoints ?? 0}</td>
    </tr>
  `;
  }).join("");

  body.innerHTML = `
    <table class="player-standings-table" aria-label="Player standings">
      <thead>
        <tr>
          <th scope="col">Rank</th>
          <th scope="col">Player</th>
          <th scope="col">Score</th>
          <th scope="col">Max Possible</th>
        </tr>
      </thead>
      <tbody>${rowMarkup}</tbody>
    </table>
  `;

  return sortedRows;
}

function clampBoardViewerScale(value) {
  const numeric = Number(value);
  if (!Number.isFinite(numeric)) return BOARD_VIEWER_DEFAULT_SCALE;
  return Math.max(BOARD_VIEWER_MIN_SCALE, Math.min(BOARD_VIEWER_MAX_SCALE, numeric));
}

function pickTeamIdFromRecord(record) {
  if (typeof record === "string") return record;
  if (!record || typeof record !== "object") return "";
  return record?.pick?.teamId || record?.teamId || record?.team_id || "";
}

function paddedSlotNumber(value) {
  return String(value).padStart(2, "0");
}

function feederSlotIdsForSlot(slotId) {
  const id = String(slotId || "").toUpperCase();

  let match = id.match(/^([LR])-R16-(\d{2})$/);
  if (match) {
    const side = match[1];
    const index = Number(match[2]);
    return [
      `${side}-R32-${paddedSlotNumber(index * 2 - 1)}`,
      `${side}-R32-${paddedSlotNumber(index * 2)}`,
    ];
  }

  match = id.match(/^([LR])-QF-(\d{2})$/);
  if (match) {
    const side = match[1];
    const index = Number(match[2]);
    return [
      `${side}-R16-${paddedSlotNumber(index * 2 - 1)}`,
      `${side}-R16-${paddedSlotNumber(index * 2)}`,
    ];
  }

  match = id.match(/^([LR])-SF-(\d{2})$/);
  if (match) {
    const side = match[1];
    const index = Number(match[2]);
    return [
      `${side}-QF-${paddedSlotNumber(index * 2 - 1)}`,
      `${side}-QF-${paddedSlotNumber(index * 2)}`,
    ];
  }

  if (id === "FINAL-LEFT") return ["L-SF-01", "L-SF-02"];
  if (id === "FINAL-RIGHT") return ["R-SF-01", "R-SF-02"];
  if (id === "CHAMPION") return ["FINAL-LEFT", "FINAL-RIGHT"];

  return [];
}

function canTeamStillReachSlot(teamId, slotId, officialTruthPicksBySlot, visiting = new Set()) {
  const candidateTeamId = String(teamId || "").trim();
  const currentSlotId = String(slotId || "").toUpperCase();

  if (!candidateTeamId || !currentSlotId) return false;
  if (visiting.has(currentSlotId)) return false;

  const officialTeamId = pickTeamIdFromRecord(officialTruthPicksBySlot?.[currentSlotId]);
  if (officialTeamId) return officialTeamId === candidateTeamId;

  const feederSlotIds = feederSlotIdsForSlot(currentSlotId);
  if (!feederSlotIds.length) return true;

  const nextVisiting = new Set(visiting);
  nextVisiting.add(currentSlotId);

  return feederSlotIds.some((feederSlotId) => (
    canTeamStillReachSlot(candidateTeamId, feederSlotId, officialTruthPicksBySlot, nextVisiting)
  ));
}


function normalizeBoardViewerTeam(teamId, teamById) {
  const id = String(teamId || "").trim();
  if (!id) return null;
  const team = teamById.get(id) || {};
  return {
    id,
    abbr: team.abbr || team.id || id,
    name: team.name || team.displayName || team.abbr || id,
    flag: team.flag || team.flagEmoji || "",
  };
}

function boardViewerOfficialTruthLabel(team) {
  if (!team) return "";
  return `${team.flag ? `${team.flag} ` : ""}${team.abbr || team.id}`.trim();
}

function playerFacingSlotLabel(slot) {
  if (slot?.displayLabel) return slot.displayLabel;
  const slotId = String(slot?.slotId || "");
  if (slotId === "CHAMPION") return "Champion";
  if (slotId === "THIRD-PLACE-WINNER") return "Third place";
  if (slot.round === "R32") return "Round of 32";
  if (slot.round === "R16") return "Round of 16";
  if (slot.round === "QF") return "Quarterfinal";
  if (slot.round === "SF") return "Semifinal";
  if (slot.round === "SF_WINNER") return "Finalist";
  return slotId || "Pick";
}

function installBoardViewerDragPan(scroll) {
  if (!scroll || scroll.dataset.playerBoardViewerPanInstalled === "true") return;
  scroll.dataset.playerBoardViewerPanInstalled = "true";

  let drag = null;

  function clearDrag() {
    if (!drag) return;
    scroll.classList.remove("is-drag-panning");
    scroll.classList.remove("is-drag-pan-armed");
    drag = null;
  }

  scroll.addEventListener("pointerdown", (event) => {
    if (!event.isPrimary || event.button !== 0) return;
    if (event.target?.closest?.("button, select, [data-player-board-viewer-close]")) return;
    drag = {
      pointerId: event.pointerId,
      startX: event.clientX,
      startY: event.clientY,
      scrollLeft: scroll.scrollLeft,
      scrollTop: scroll.scrollTop,
      active: false,
    };
    scroll.classList.add("is-drag-pan-armed");
  });

  scroll.addEventListener("pointermove", (event) => {
    if (!drag || event.pointerId !== drag.pointerId) return;
    const dx = event.clientX - drag.startX;
    const dy = event.clientY - drag.startY;
    if (!drag.active && Math.hypot(dx, dy) > 5) {
      drag.active = true;
      scroll.classList.add("is-drag-panning");
      scroll.setPointerCapture?.(event.pointerId);
    }
    if (!drag.active) return;
    event.preventDefault();
    scroll.scrollLeft = drag.scrollLeft - dx;
    scroll.scrollTop = drag.scrollTop - dy;
  });

  scroll.addEventListener("pointerup", clearDrag);
  scroll.addEventListener("pointercancel", clearDrag);
  scroll.addEventListener("lostpointercapture", clearDrag);
}

function buildBoardViewerAssets(payloads) {
  const geometry = payloads?.geometry || {};
  const teamsPayload = payloads?.teamsPayload || {};
  const nativeSize = geometry.nativeSizePx || { width: 1536, height: 1024 };
  const teamRecords = teamsPayload.teams && typeof teamsPayload.teams === "object" ? teamsPayload.teams : {};
  const teamById = new Map(Object.entries(teamRecords).map(([id, team]) => [id, { id, ...team }]));
  const slots = Array.isArray(geometry.slots)
    ? geometry.slots.filter((slot) => slot?.slotId && slot?.boundsPx && slot.slotId !== "CENTER-FINAL-FOUR")
    : [];
  return { nativeSize, teamById, slots };
}

function applyBoardViewerScale(panel, scale) {
  const frame = panel.querySelector("[data-player-board-viewer-scale-frame]");
  const plane = panel.querySelector("[data-player-board-viewer-plane]");
  const select = panel.querySelector("[data-player-board-viewer-zoom]");
  const nativeWidth = Number(panel.dataset.playerBoardNativeWidth || 1536);
  const nativeHeight = Number(panel.dataset.playerBoardNativeHeight || 1024);
  const nextScale = clampBoardViewerScale(scale);
  const renderWidth = Math.round(nativeWidth * nextScale);
  const renderHeight = Math.round(nativeHeight * nextScale);

  panel.dataset.playerBoardViewerScale = String(nextScale);
  for (const element of [frame, plane]) {
    if (!element) continue;
    element.style.setProperty("--player-board-w-px", `${nativeWidth}px`);
    element.style.setProperty("--player-board-h-px", `${nativeHeight}px`);
    element.style.setProperty("--player-board-render-scale", String(nextScale));
    element.style.setProperty("--player-board-render-w-px", `${renderWidth}px`);
    element.style.setProperty("--player-board-render-h-px", `${renderHeight}px`);
  }
  if (frame) {
    frame.style.width = `${renderWidth}px`;
    frame.style.height = `${renderHeight}px`;
  }
  if (select) select.value = String(nextScale);
}

function renderPlayerBoard(panel, { row, assets }) {
  const { nativeSize, teamById, slots } = assets;
  const plane = panel.querySelector("[data-player-board-viewer-plane]");
  const picksBySlot = row?.picksBySlot || {};
  const officialTruthPicksBySlot = row?.officialTruthPicksBySlot || {};
  const officialTruthSource = row?.officialResultsTruthSource || "";
  const nativeWidth = Number(nativeSize.width || nativeSize.w || 1536);
  const nativeHeight = Number(nativeSize.height || nativeSize.h || 1024);
  const slotMarkup = slots.map((slot) => {
    const bounds = slot.boundsPx;
    const playerTeamId = pickTeamIdFromRecord(picksBySlot[slot.slotId]);
    const officialTeamId = pickTeamIdFromRecord(officialTruthPicksBySlot[slot.slotId]);
    const team = normalizeBoardViewerTeam(playerTeamId || (slot.round === "R32" ? officialTeamId : null), teamById);
    const officialTeam = normalizeBoardViewerTeam(officialTeamId, teamById);
    const officialState = officialTeam && team
      ? (officialTeam.id === team.id ? "correct" : "incorrect")
      : "";
    const isUnreachablePick = Boolean(
      team
      && !officialTeam
      && !canTeamStillReachSlot(team.id, slot.slotId, officialTruthPicksBySlot)
    );
    const slotLabel = playerFacingSlotLabel(slot);
    const valueLabel = team ? `${team.flag ? `${team.flag} ` : ""}${team.abbr || team.id}`.trim() : "Unpicked";
    const fullLabel = team ? `${team.flag ? `${team.flag} ` : ""}${team.name || team.abbr || team.id}`.trim() : "Unpicked";
    const officialLabel = boardViewerOfficialTruthLabel(officialTeam);
    const officialMarkup = officialTeam
      ? `<span class="player-board-viewer-official-truth">Official: ${escapeHtml(officialLabel)}</span>`
      : "";
    const eliminatedMarkup = isUnreachablePick
      ? `<span class="player-board-viewer-eliminated-pick">Eliminated</span>`
      : "";
    const stateClass = [
      officialState ? `has-official-${officialState}-pick` : "",
      isUnreachablePick ? "is-unreachable-pick" : "",
    ].filter(Boolean).map((className) => ` ${className}`).join("");
    const ariaOfficial = officialTeam
      ? ` Official result from ${officialTruthSource || "Admin_/official"}: ${officialLabel}.`
      : (isUnreachablePick ? " This pick is eliminated because the team can no longer reach this slot." : "");
    return `
      <button type="button" class="player-board-viewer-pick ${team ? "has-pick" : "is-unpicked"}${stateClass}" data-player-board-viewer-slot="${escapeHtml(slot.slotId)}" data-official-result-state="${escapeHtml(officialState)}" disabled aria-label="${escapeHtml(`${slotLabel}: ${fullLabel}. Read-only.${ariaOfficial}`)}" style="left:${Number(bounds.x)}px;top:${Number(bounds.y)}px;width:${Number(bounds.width)}px;height:${Number(bounds.height)}px;">
        <span class="player-board-viewer-pick-label">${escapeHtml(slotLabel)}</span>
        <span class="player-board-viewer-pick-value">${escapeHtml(valueLabel)}</span>
        ${officialMarkup}
        ${eliminatedMarkup}
      </button>
    `;
  }).join("");

  panel.dataset.playerBoardNativeWidth = String(nativeWidth);
  panel.dataset.playerBoardNativeHeight = String(nativeHeight);
  plane.innerHTML = `
    <img class="player-board-viewer-linework" src="${BOARD_VIEWER_LINEWORK_URL}" alt="" aria-hidden="true">
    <div class="player-board-viewer-pick-layer" data-player-board-viewer-pick-layer>${slotMarkup}</div>
  `;
  applyBoardViewerScale(panel, Number(panel.dataset.playerBoardViewerScale || BOARD_VIEWER_DEFAULT_SCALE));
}

export function createPlayerStandingsSurface({
  root,
  authService,
  standingsStore,
  profileStore,
} = {}) {
  let currentAuthState = authService?.currentState?.() || null;
  let currentProfileState = null;
  let storageReady = false;
  let storageReadyChecked = false;
  let lastOpenButton = null;
  let currentStandingsRows = [];
  let lastPlayerBoardViewerButton = null;
  let boardViewerAssetsPromise = null;
  let groupStagePicksLockTimer = null;

  const button = ensureStandingsButton(root);
  const panel = ensureStandingsPanel(root);
  const boardViewerPanel = ensurePlayerBoardViewerPanel(root);
  const closeButton = panel.querySelector("[data-player-standings-close]");
  const boardViewerCloseButton = boardViewerPanel.querySelector("[data-player-board-viewer-close]");

  function syncStandingsButtonState() {
    const joined = isSignedIn(currentAuthState);
    const resultsVisible = areGroupStagePicksLocked();
    const canOpen = joined && storageReady && resultsVisible;
    button.hidden = !canOpen;
    button.disabled = !canOpen;
    button.classList.toggle("is-join-required", !joined);
    button.classList.toggle("is-results-locked", joined && !resultsVisible);
    button.classList.toggle("is-storage-unavailable", joined && resultsVisible && storageReadyChecked && !storageReady);
    button.title = !joined
      ? "Join to enter the pool."
      : !resultsVisible
        ? playerResultsHiddenUntilLockMessage()
        : storageReady
          ? "Open Pool"
          : "Pool standings unavailable until stored picks can be read.";
    button.setAttribute("aria-label", button.title);
  }

  function renderStatus(message) {
    const body = panel.querySelector("[data-player-standings-body]");
    body.innerHTML = `<p class="player-standings-status">${escapeHtml(message)}</p>`;
  }

  async function refreshStorageReady() {
    if (!isSignedIn(currentAuthState)) {
      storageReady = false;
      storageReadyChecked = true;
      syncStandingsButtonState();
      return false;
    }

    if (!areGroupStagePicksLocked()) {
      storageReady = false;
      storageReadyChecked = true;
      syncStandingsButtonState();
      return false;
    }

    try {
      storageReady = await standingsStore?.canReadStoredPicks?.() === true;
    } catch (error) {
      console.warn("[PlayerStandingsSurface] stored picks preflight failed", error);
      storageReady = false;
    }

    storageReadyChecked = true;
    syncStandingsButtonState();
    return storageReady;
  }

  function scheduleGroupStagePicksLockRefresh() {
    if (groupStagePicksLockTimer) {
      window.clearTimeout(groupStagePicksLockTimer);
      groupStagePicksLockTimer = null;
    }

    const msUntilLock = GROUP_STAGE_PICKS_LOCK_AT_MS - Date.now();
    if (
      Number.isFinite(msUntilLock)
      && msUntilLock > 0
      && msUntilLock < GROUP_STAGE_PICKS_LOCK_TIMER_MAX_MS
    ) {
      groupStagePicksLockTimer = window.setTimeout(() => {
        syncStandingsButtonState();
        refreshStorageReady();
      }, msUntilLock + 1000);
    }
  }

  function loadBoardViewerAssets() {
    if (!boardViewerAssetsPromise) {
      boardViewerAssetsPromise = Promise.all([
        fetch(BOARD_VIEWER_GEOMETRY_URL, { cache: "no-cache" }).then((response) => response.json()),
        fetch(BOARD_VIEWER_TEAMS_URL, { cache: "no-cache" }).then((response) => response.json()),
      ]).then(([geometry, teamsPayload]) => buildBoardViewerAssets({ geometry, teamsPayload }));
    }
    return boardViewerAssetsPromise;
  }

  async function loadStandingsRows() {
    renderStatus("Loading standings…");

    if (!areGroupStagePicksLocked()) {
      renderStatus(playerResultsHiddenUntilLockMessage());
      return;
    }

    if (!await refreshStorageReady()) {
      renderStatus("Pool standings unavailable until stored picks can be read.");
      return;
    }

    try {
      const storeRows = await standingsStore?.listPlayerStandings?.();
      currentProfileState = await resolveCurrentProfile({ authState: currentAuthState, profileStore });
      const playerRows = Array.isArray(storeRows)
        ? storeRows.filter((row) => !isOfficialStandingsRow(row))
        : [];

      const rows = playerRows.length
        ? playerRows
        : fallbackParticipationRows(currentAuthState, currentProfileState);

      if (!rows.length && !isSignedIn(currentAuthState)) {
        renderStatus("Join to enter the pool.");
        return;
      }

      currentStandingsRows = renderStandingsRows(panel, rows, { authState: currentAuthState, profileState: currentProfileState });
    } catch (error) {
      console.error("[PlayerStandingsSurface] standings unavailable", error);
      renderStatus("Standings unavailable");
    }
  }

  async function openPanel(event) {
    if (event?.currentTarget instanceof HTMLElement) {
      lastOpenButton = event.currentTarget;
    }
    if (!areGroupStagePicksLocked()) {
      syncStandingsButtonState();
      return;
    }
    if (!await refreshStorageReady()) return;
    panel.hidden = false;
    window.dispatchEvent(new CustomEvent(STANDINGS_PANEL_OPEN_EVENT));
    await loadStandingsRows();
    closeButton?.focus();
  }

  function closePlayerBoardViewer({ restoreFocus = true } = {}) {
    boardViewerPanel.hidden = true;
    boardViewerPanel.removeAttribute("data-viewing-public-player");
    if (restoreFocus) lastPlayerBoardViewerButton?.focus();
  }

  async function openPlayerBoardViewer(buttonNode) {
    const rowIndex = Number(buttonNode?.getAttribute("data-player-standings-row"));
    const row = Number.isInteger(rowIndex) ? currentStandingsRows[rowIndex] : null;
    if (!row) return;

    lastPlayerBoardViewerButton = buttonNode;
    const title = boardViewerPanel.querySelector("[data-player-board-viewer-title]");
    title.textContent = `Viewing ${row.publicPlayerName}'s picks`;
    boardViewerPanel.setAttribute("data-viewing-public-player", "true");
    boardViewerPanel.hidden = false;
    boardViewerPanel.querySelector("[data-player-board-viewer-plane]").innerHTML = `<p class="player-board-viewer-status">Loading read-only board…</p>`;

    try {
      const assets = await loadBoardViewerAssets();
      renderPlayerBoard(boardViewerPanel, { row, assets });
    } catch (error) {
      console.error("[PlayerStandingsSurface] board viewer unavailable", error);
      boardViewerPanel.querySelector("[data-player-board-viewer-plane]").innerHTML = `<p class="player-board-viewer-status">Board viewer unavailable</p>`;
    }

    boardViewerCloseButton?.focus();
  }

  function closePanel() {
    closePlayerBoardViewer({ restoreFocus: false });
    panel.hidden = true;
    lastOpenButton?.focus();
  }

  function start() {
    syncStandingsButtonState();
    refreshStorageReady();
    scheduleGroupStagePicksLockRefresh();
    installBoardViewerDragPan(boardViewerPanel.querySelector("[data-player-board-viewer-scroll]"));
    button.addEventListener("click", openPanel);
    closeButton?.addEventListener("click", closePanel);
    boardViewerCloseButton?.addEventListener("click", () => closePlayerBoardViewer());

    boardViewerPanel.querySelector("[data-player-board-viewer-zoom]")?.addEventListener("change", (event) => {
      applyBoardViewerScale(boardViewerPanel, event.target.value);
    });
    boardViewerPanel.querySelector("[data-player-board-viewer-zoom-out]")?.addEventListener("click", () => {
      applyBoardViewerScale(boardViewerPanel, Number(boardViewerPanel.dataset.playerBoardViewerScale || BOARD_VIEWER_DEFAULT_SCALE) - BOARD_VIEWER_SCALE_STEP);
    });
    boardViewerPanel.querySelector("[data-player-board-viewer-zoom-in]")?.addEventListener("click", () => {
      applyBoardViewerScale(boardViewerPanel, Number(boardViewerPanel.dataset.playerBoardViewerScale || BOARD_VIEWER_DEFAULT_SCALE) + BOARD_VIEWER_SCALE_STEP);
    });

    panel.addEventListener("click", (event) => {
      const picksButton = event.target instanceof HTMLElement
        ? event.target.closest("[data-player-standings-row]")
        : null;
      if (picksButton) {
        openPlayerBoardViewer(picksButton);
        return;
      }
      if (event.target === panel) closePanel();
    });

    boardViewerPanel.addEventListener("click", (event) => {
      if (event.target === boardViewerPanel) closePlayerBoardViewer();
    });

    document.addEventListener("keydown", (event) => {
      if (event.key !== "Escape") return;
      if (!boardViewerPanel.hidden) {
        closePlayerBoardViewer();
        return;
      }
      if (!panel.hidden) closePanel();
    });

    authService?.subscribe?.((state) => {
      currentAuthState = state;
      currentProfileState = null;
      storageReady = false;
      storageReadyChecked = false;
      syncStandingsButtonState();
      scheduleGroupStagePicksLockRefresh();
      refreshStorageReady().then((ready) => {
        if (ready && !panel.hidden) loadStandingsRows();
        if (!ready) {
          closePlayerBoardViewer({ restoreFocus: false });
          panel.hidden = true;
        }
      });
    });
  }

  return { start };
}
