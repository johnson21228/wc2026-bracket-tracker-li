const STATUS_COPY = Object.freeze({
  GROUP_STAGE_OPEN: {
    eyebrow: "Game 1 · Group stage open",
    title: "Pick the bracket before FIFA locks it.",
    body: "Read the groups now. Your pre-lock Round of 32 projection stays as scoring evidence later.",
  },
  R32_PROJECTION_LIVE: {
    eyebrow: "Game 1 · Projection live",
    title: "Watch the groups reshape the board.",
    body: "Curated standings can move projected qualifiers while your own read remains preserved.",
  },
  FIFA_R32_LOCKED: {
    eyebrow: "Game 1 · FIFA R32 locked",
    title: "The official bracket is now frozen.",
    body: "Compare your pre-lock read against the official Round of 32, then continue the bracket.",
  },
  KNOCKOUT_PICKING_OPEN: {
    eyebrow: "Game 1 · Knockout picking open",
    title: "Now play the bracket as usual.",
    body: "Pick winners through the final from the official locked Round of 32.",
  },
  KNOCKOUT_LIVE: {
    eyebrow: "Game 1 · Knockout live",
    title: "See whether your read holds up.",
    body: "Official results now score both your pre-lock projection and knockout picks.",
  },
  COMPLETE: {
    eyebrow: "Game 1 · Complete",
    title: "Your tournament read is scored.",
    body: "Review the projection score, knockout score, and final bracket result.",
  },
});

function firstRecord(records) {
  if (!records || typeof records !== "object") return null;
  const firstKey = Object.keys(records)[0];
  return firstKey ? records[firstKey] : null;
}

function renderStatus(surface, state, lifecycleDefinition) {
  const copy = STATUS_COPY[state] || STATUS_COPY.GROUP_STAGE_OPEN;
  const promise = Array.isArray(lifecycleDefinition?.productPromise)
    ? lifecycleDefinition.productPromise
    : [
        "Pick the bracket before FIFA locks it.",
        "Watch the groups reshape the board.",
        "See whether your read of the tournament was right.",
      ];

  surface.dataset.lifecycleState = state;

  surface.innerHTML = `
    <div class="game1-lifecycle-status-card">
      <div class="game1-lifecycle-eyebrow">${copy.eyebrow}</div>
      <div class="game1-lifecycle-title">${copy.title}</div>
      <div class="game1-lifecycle-body">${copy.body}</div>
      <div class="game1-lifecycle-promise" aria-label="Game 1 promise">
        ${promise.map((line) => `<span>${line}</span>`).join("")}
      </div>
    </div>
  `;
}

function renderFallback(surface) {
  surface.dataset.lifecycleState = "UNKNOWN";
  surface.innerHTML = `
    <div class="game1-lifecycle-status-card">
      <div class="game1-lifecycle-eyebrow">Game 1 · Lifecycle unavailable</div>
      <div class="game1-lifecycle-title">Pick the bracket before FIFA locks it.</div>
      <div class="game1-lifecycle-body">Lifecycle data did not load, so the board is showing the default invitation.</div>
    </div>
  `;
}

async function hydrateLifecycleStatus(surface) {
  try {
    const [definitionResponse, seedResponse] = await Promise.all([
      fetch("data/model/game1_lifecycle.json", { cache: "no-cache" }),
      fetch("data/model/game1_lifecycle_seed.json", { cache: "no-cache" }),
    ]);

    if (!definitionResponse.ok || !seedResponse.ok) {
      renderFallback(surface);
      return;
    }

    const [definition, seed] = await Promise.all([
      definitionResponse.json(),
      seedResponse.json(),
    ]);

    const record = firstRecord(seed.records);
    const state = record?.lifecycleState || definition.initialState || "GROUP_STAGE_OPEN";

    renderStatus(surface, state, definition);
  } catch {
    renderFallback(surface);
  }
}

function createGame1LifecycleStatusSurface() {
  const surface = document.createElement("aside");
  surface.className = "board-layer game1-lifecycle-status-surface";
  surface.dataset.layerRole = "game1-lifecycle-status";
  surface.setAttribute("aria-label", "Game 1 lifecycle status");

  surface.innerHTML = `
    <div class="game1-lifecycle-status-card">
      <div class="game1-lifecycle-eyebrow">Game 1 · Loading</div>
      <div class="game1-lifecycle-title">Pick the bracket before FIFA locks it.</div>
    </div>
  `;

  hydrateLifecycleStatus(surface);
  return surface;
}

export { createGame1LifecycleStatusSurface };
