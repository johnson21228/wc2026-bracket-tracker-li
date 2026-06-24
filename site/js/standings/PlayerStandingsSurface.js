const STANDINGS_PANEL_OPEN_EVENT = "wc2026:standings-panel-opened";

function numericScore(value) {
  const number = Number(value);
  return Number.isFinite(number) ? number : 0;
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
  const groupPoints = numericScore(row?.groupPoints);
  const knockoutPoints = numericScore(row?.knockoutPoints);
  const tiebreakerScore = numericScore(row?.tiebreakerScore);
  const total = Number.isFinite(Number(row?.total))
    ? numericScore(row.total)
    : groupPoints + knockoutPoints;
  const picksBySlot = row?.picksBySlot && typeof row.picksBySlot === "object" && !Array.isArray(row.picksBySlot)
    ? row.picksBySlot
    : {};
  const picksCount = Number.isFinite(Number(row?.picksCount))
    ? numericScore(row.picksCount)
    : Object.keys(picksBySlot).length;

  return {
    publicPlayerName: safePublicPlayerName(row),
    picksBySlot,
    picksCount,
    groupPoints,
    knockoutPoints,
    tiebreakerScore,
    total,
  };
}

export function sortPlayerStandingsRows(rows = []) {
  return rows
    .map(normalizeStandingsRow)
    .sort((a, b) => (
      (b.total - a.total)
      || (b.knockoutPoints - a.knockoutPoints)
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
  return [{
    publicPlayerName: publicNameFromAuthState(authState, profileState),
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
  button.setAttribute("aria-label", "Open Standings");
  button.textContent = "Standings";
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
          <h2 id="player-standings-title">Standings</h2>
        </div>
        <button type="button" class="player-standings-close" data-player-standings-close aria-label="Close Standings">×</button>
      </header>
      <div class="player-standings-body" data-player-standings-body>
        <p class="player-standings-status">Loading standings…</p>
      </div>
    </div>
  `;
  root.append(panel);
  return panel;
}

function renderStandingsRows(panel, rows) {
  const body = panel.querySelector("[data-player-standings-body]");
  const sortedRows = sortPlayerStandingsRows(rows);

  if (!sortedRows.length) {
    body.innerHTML = `<p class="player-standings-status">No players yet</p>`;
    return;
  }

  const rowMarkup = sortedRows.map((row, index) => `
    <tr>
      <td class="player-standings-rank">${index + 1}</td>
      <td class="player-standings-player">${row.publicPlayerName}</td>
      <td class="player-standings-group-count">${row.groupPoints}</td>
      <td class="player-standings-knockout-count">${row.knockoutPoints}</td>
    </tr>
  `).join("");

  body.innerHTML = `
    <table class="player-standings-table" aria-label="Player standings">
      <thead>
        <tr>
          <th scope="col">Rank</th>
          <th scope="col">Player</th>
          <th scope="col">Group</th>
          <th scope="col">Knockout</th>
        </tr>
      </thead>
      <tbody>${rowMarkup}</tbody>
    </table>
  `;
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

  const button = ensureStandingsButton(root);
  const panel = ensureStandingsPanel(root);
  const closeButton = panel.querySelector("[data-player-standings-close]");

  function syncStandingsButtonState() {
    const joined = isSignedIn(currentAuthState);
    const canOpen = joined && storageReady;
    button.hidden = !canOpen;
    button.disabled = !canOpen;
    button.classList.toggle("is-join-required", !joined);
    button.classList.toggle("is-storage-unavailable", joined && storageReadyChecked && !storageReady);
    button.title = !joined
      ? "Join to enter standings."
      : storageReady
        ? "Open Standings"
        : "Standings unavailable until stored picks can be read.";
    button.setAttribute("aria-label", button.title);
  }

  function renderStatus(message) {
    const body = panel.querySelector("[data-player-standings-body]");
    body.innerHTML = `<p class="player-standings-status">${message}</p>`;
  }

  async function refreshStorageReady() {
    if (!isSignedIn(currentAuthState)) {
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

  async function loadStandingsRows() {
    renderStatus("Loading standings…");

    if (!await refreshStorageReady()) {
      renderStatus("Standings unavailable until stored picks can be read.");
      return;
    }

    try {
      const storeRows = await standingsStore?.listPlayerStandings?.();
      currentProfileState = await resolveCurrentProfile({ authState: currentAuthState, profileStore });
      const rows = Array.isArray(storeRows) && storeRows.length
        ? storeRows
        : fallbackParticipationRows(currentAuthState, currentProfileState);

      if (!rows.length && !isSignedIn(currentAuthState)) {
        renderStatus("Join to enter standings.");
        return;
      }

      renderStandingsRows(panel, rows);
    } catch (error) {
      console.error("[PlayerStandingsSurface] standings unavailable", error);
      renderStatus("Standings unavailable");
    }
  }

  async function openPanel(event) {
    if (event?.currentTarget instanceof HTMLElement) {
      lastOpenButton = event.currentTarget;
    }
    if (!await refreshStorageReady()) return;
    panel.hidden = false;
    window.dispatchEvent(new CustomEvent(STANDINGS_PANEL_OPEN_EVENT));
    await loadStandingsRows();
    closeButton?.focus();
  }

  function closePanel() {
    panel.hidden = true;
    lastOpenButton?.focus();
  }

  function start() {
    syncStandingsButtonState();
    refreshStorageReady();
    button.addEventListener("click", openPanel);
    closeButton?.addEventListener("click", closePanel);

    panel.addEventListener("click", (event) => {
      if (event.target === panel) closePanel();
    });

    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape" && !panel.hidden) closePanel();
    });

    authService?.subscribe?.((state) => {
      currentAuthState = state;
      currentProfileState = null;
      storageReady = false;
      storageReadyChecked = false;
      syncStandingsButtonState();
      refreshStorageReady().then((ready) => {
        if (ready && !panel.hidden) loadStandingsRows();
        if (!ready) panel.hidden = true;
      });
    });
  }

  return { start };
}
