import { createGame1R32PickController } from "../controllers/Game1R32PickController.js";
import { positionFloatingSurfaceNearAnchor } from "../services/FloatingSurfacePlacement.js";

function closeExistingMenu(layer) {
  layer.querySelectorAll(".r32-pick-menu-popover").forEach((node) => node.remove());
  layer.querySelectorAll(".r32-pick-slot-button[aria-expanded='true']").forEach((node) => {
    node.setAttribute("aria-expanded", "false");
  });
}

function renderPickText(button, pick) {
  const pickText = button.querySelector(".r32-pick-slot-current");
  if (!pickText) return;

  if (pick?.abbr) {
    pickText.textContent = `${pick.flagEmoji ? `${pick.flagEmoji} ` : ""}${pick.abbr}`;
    button.dataset.pickState = "picked";
    return;
  }

  pickText.textContent = "Pick";
  button.dataset.pickState = "empty";
}



function groupsFromLogicSlot(logicSlot = {}) {
  const rawGroups = Array.isArray(logicSlot.groups)
    ? logicSlot.groups
    : String(logicSlot.groups || logicSlot.eligibleGroups || "")
        .split(/[,\s/]+/)
        .filter(Boolean);

  return rawGroups
    .map((group) => String(group).trim().replace(/^Group\s+/i, "").toUpperCase())
    .filter((group) => /^[A-L]$/.test(group));
}

function qualifierKindFromLogicSlot(logicSlot = {}) {
  return String(
    logicSlot.qualifierKind ||
    logicSlot.sourceKind ||
    logicSlot.pickability ||
    logicSlot.kind ||
    ""
  ).toLowerCase();
}

function playerFacingSlotLabel(logicSlot = {}) {
  const kind = qualifierKindFromLogicSlot(logicSlot);
  const groups = groupsFromLogicSlot(logicSlot);
  const firstGroup = groups[0] || "";

  if ((kind.includes("winner") || kind.includes("group-winner")) && firstGroup) {
    return `Group ${firstGroup} winner`;
  }

  if ((kind.includes("runner") || kind.includes("second") || kind.includes("group-runner")) && firstGroup) {
    return `Group ${firstGroup} runner-up`;
  }

  if (kind.includes("third") || kind.includes("candidate")) {
    if (groups.length === 1) return `Third-place team from Group ${firstGroup}`;
    return "Third-place team";
  }

  if (kind.includes("knockout") || kind.includes("feeder")) {
    return "Possible winners";
  }

  const rawLabel = String(logicSlot.fifaLabel || logicSlot.label || "").trim();
  if (/^L-[A-Z0-9-]+$/i.test(rawLabel)) return "Pick possible winner";
  if (/^L-[A-Z0-9-]+\s*\/\s*L-[A-Z0-9-]+$/i.test(rawLabel)) return "Pick possible winner";
  return rawLabel || "Pick team";
}

function playerFacingMenuSubtitle(logicSlot = {}, fallback = "") {
  const kind = qualifierKindFromLogicSlot(logicSlot);
  const groups = groupsFromLogicSlot(logicSlot);
  const firstGroup = groups[0] || "";

  if (kind.includes("third") || kind.includes("candidate")) {
    if (groups.length === 1) return `Possible third-place teams from Group ${firstGroup}`;
    return "Possible third-place teams";
  }

  if (kind.includes("knockout") || kind.includes("feeder")) {
    return "Pick a possible winner";
  }

  if ((kind.includes("winner") || kind.includes("group-winner")) && firstGroup) {
    return `Pick the Group ${firstGroup} winner`;
  }

  if ((kind.includes("runner") || kind.includes("second") || kind.includes("group-runner")) && firstGroup) {
    return `Pick the Group ${firstGroup} runner-up`;
  }

  return scrubPlayerFacingText(fallback || "Pick team");
}

function scrubPlayerFacingText(text) {
  let cleaned = String(text || "");

  cleaned = cleaned.replace(/THIRD-PLACE-CANDIDATE-SET/gi, "Possible third-place teams");
  cleaned = cleaned.replace(/KNOCKOUT-FEEDER/gi, "Possible winners");
  cleaned = cleaned.replace(/\bFeeder choices\b/gi, "Possible winners");
  cleaned = cleaned.replace(/\bcandidate-set\b/gi, "possible teams");
  cleaned = cleaned.replace(/\bknockout-feeder\b/gi, "possible winners");
  cleaned = cleaned.replace(/\bfeeder\b/gi, "previous match");
  cleaned = cleaned.replace(/Winner from\s+L-[A-Z0-9-]+\s*\/\s*L-[A-Z0-9-]+/gi, "Winner from previous match");
  cleaned = cleaned.replace(/\bL-R32-\d+\s*\/\s*L-R32-\d+\b/gi, "previous matches");
  cleaned = cleaned.replace(/^\s*3\s+[A-L]+\s*$/i, "Possible third-place teams");

  return cleaned;
}

function scrubPlayerFacingTree(root) {
  const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
  const nodes = [];
  while (walker.nextNode()) nodes.push(walker.currentNode);

  for (const node of nodes) {
    node.nodeValue = scrubPlayerFacingText(node.nodeValue);
  }
}

function trackingPayloadFrom({ button, slotViewModel, phase }) {
  return {
    phase,
    fifaSlotId: button.dataset.fifaSlotId || slotViewModel.logicSlot?.fifaSlotId || "",
    fifaLabel: button.dataset.fifaLabel || slotViewModel.logicSlot?.fifaLabel || "",
    geometrySlotId: button.dataset.geometrySlotId || slotViewModel.bridgeSlot?.geometrySlotId || "",
    pickability: button.dataset.pickability || "unknown",
    candidateCount: button.dataset.candidateCount || String(slotViewModel.candidates?.length || 0),
    eligibleGroups: button.dataset.eligibleGroups || "",
    title: button.title || slotViewModel.title || "",
  };
}

function updateButtonTrackerChip(layer, payload) {
  const chip = layer.querySelector(".r32-pick-button-tracker-chip");
  if (!chip) return;
  if (!payload || payload.phase === "clear") {
    chip.textContent = `R32 buttons: ${layer.dataset.r32PickMenuEnabledCount || "0"}/${layer.dataset.r32PickMenuCount || "0"} pickable`;
    return;
  }
  chip.textContent = `${payload.phase}: ${payload.fifaLabel} · ${payload.pickability} · ${payload.candidateCount} candidates`;
}

function trackButton({ layer, button, slotViewModel, phase }) {
  layer.querySelectorAll(".r32-pick-slot-button.is-preselect-highlight").forEach((node) => {
    if (node !== button) node.classList.remove("is-preselect-highlight");
  });
  layer.querySelectorAll(".r32-pick-slot-button.is-active-selection").forEach((node) => {
    if (node !== button || phase !== "click") node.classList.remove("is-active-selection");
  });

  if (phase === "hover" || phase === "focus") {
    button.classList.add("is-preselect-highlight");
    button.dataset.preselectState = phase;
  }

  if (phase === "click") {
    button.classList.add("is-active-selection");
    button.dataset.preselectState = "active";
  }

  const payload = trackingPayloadFrom({ button, slotViewModel, phase });
  layer.dataset.r32TrackedPhase = payload.phase;
  layer.dataset.r32TrackedFifaSlotId = payload.fifaSlotId;
  layer.dataset.r32TrackedFifaLabel = payload.fifaLabel;
  layer.dataset.r32TrackedGeometrySlotId = payload.geometrySlotId;
  layer.dataset.r32TrackedPickability = payload.pickability;
  layer.dataset.r32TrackedCandidateCount = payload.candidateCount;
  updateButtonTrackerChip(layer, payload);

  window.dispatchEvent(new CustomEvent("wc2026:r32PickButtonTracked", { detail: payload }));
}

function clearButtonTracking({ layer, button }) {
  button.classList.remove("is-preselect-highlight");
  if (button.dataset.preselectState !== "active") button.dataset.preselectState = "idle";
  layer.dataset.r32TrackedPhase = "clear";
  updateButtonTrackerChip(layer, { phase: "clear" });
}

function createButtonTrackerChip() {
  const chip = document.createElement("div");
  chip.className = "r32-pick-button-tracker-chip";
  chip.textContent = "R32 buttons: loading";
  return chip;
}

function renderValidationMessage(popover, result) {
  let message = popover.querySelector(".r32-pick-menu-message");
  if (!message) {
    message = document.createElement("div");
    message.className = "r32-pick-menu-message";
    popover.insertBefore(message, popover.querySelector(".r32-pick-menu-actions"));
  }
  message.textContent = result?.reason || "That pick is not allowed for this slot.";
}

function createMenu({ layer, controller, button, slotViewModel }) {
  closeExistingMenu(layer);
  button.setAttribute("aria-expanded", "true");

  const { logicSlot, candidates, title } = slotViewModel;
  const popover = document.createElement("div");
  popover.className = "r32-pick-menu-popover";
  popover.dataset.fifaSlotId = logicSlot.fifaSlotId;
  popover.setAttribute("role", "dialog");
  popover.setAttribute("aria-label", playerFacingMenuSubtitle(logicSlot, title));

  popover.style.left = "0px";
  popover.style.top = "0px";

  const heading = document.createElement("div");
  heading.className = "r32-pick-menu-heading";

  const headingTitle = document.createElement("strong");
  headingTitle.textContent = playerFacingSlotLabel(logicSlot);

  const subtitle = document.createElement("span");
  subtitle.textContent = playerFacingMenuSubtitle(logicSlot, title);

  heading.append(headingTitle, subtitle);
  popover.append(heading);

  const list = document.createElement("div");
  list.className = "r32-pick-menu-list";

  for (const team of candidates) {
    const item = document.createElement("button");
    item.type = "button";
    item.className = "r32-pick-menu-item";
    item.dataset.teamId = team.id;
    item.dataset.teamAbbr = team.abbr;
    item.dataset.group = team.group;
    item.innerHTML = `
      <span class="r32-pick-menu-flag">${team.flagEmoji || ""}</span>
      <span class="r32-pick-menu-abbr">${team.abbr}</span>
      <span class="r32-pick-menu-name">${team.name}</span>
      <span class="r32-pick-menu-group">Group ${team.group}</span>
    `;
    item.addEventListener("click", () => {
      const result = controller.setPick({ fifaSlotId: logicSlot.fifaSlotId, teamId: team.id });
      if (!result.ok) {
        renderValidationMessage(popover, result);
        return;
      }
      renderPickText(button, result.pick);
      closeExistingMenu(layer);
    });
    list.append(item);
  }

  const clear = document.createElement("button");
  clear.type = "button";
  clear.className = "r32-pick-menu-clear";
  clear.textContent = "Clear pick";
  clear.addEventListener("click", () => {
    controller.clearPick({ fifaSlotId: logicSlot.fifaSlotId });
    renderPickText(button, null);
    closeExistingMenu(layer);
  });

  const close = document.createElement("button");
  close.type = "button";
  close.className = "r32-pick-menu-close";
  close.textContent = "Close";
  close.addEventListener("click", () => closeExistingMenu(layer));

  const actions = document.createElement("div");
  actions.className = "r32-pick-menu-actions";
  actions.append(clear, close);

  popover.append(list, actions);
  scrubPlayerFacingTree(popover);
  layer.append(popover);
  positionFloatingSurfaceNearAnchor({
    anchorEl: button,
    surfaceEl: popover,
    boardPlane: layer.closest("[data-board-plane]") || layer.parentElement,
    viewportEl: layer.closest(".game1-board-viewport") || layer.closest("[data-board-scroll]"),
    preferredPlacement: "right-then-left",
    bottomControlSelectors: ["[data-group-rail-layer]", ".board-group-rail-layer", ".group-rail", ".bottom-frame-controls"],
    margin: 12,
    gap: 10,
    minWidth: 270,
    maxWidth: 320,
    maxHeight: 520,
  });
}

function createSlotButton({ layer, controller, slotViewModel }) {
  const { logicSlot, bridgeSlot, bounds, candidates, enabled, disabledReason, pick, title } = slotViewModel;
  const button = document.createElement("button");
  button.type = "button";
  button.className = "r32-pick-slot-button is-preselectable";
  button.dataset.fifaSlotId = logicSlot.fifaSlotId;
  button.dataset.fifaLabel = logicSlot.fifaLabel;
  button.dataset.geometrySlotId = bridgeSlot.geometrySlotId;
  button.dataset.qualifierKind = logicSlot.qualifierKind;
  button.dataset.eligibleGroups = (logicSlot.groups || []).join("");
  button.dataset.candidateCount = String(candidates.length);
  button.dataset.pickEnabled = enabled ? "true" : "false";
  button.setAttribute("aria-haspopup", "dialog");
  button.setAttribute("aria-expanded", "false");

  button.style.left = `${bounds.x}px`;
  button.style.top = `${bounds.y}px`;
  button.style.width = `${bounds.width}px`;
  button.style.height = `${bounds.height}px`;

  const label = document.createElement("span");
  label.className = "r32-pick-slot-label";
  label.textContent = playerFacingSlotLabel(logicSlot);

  const current = document.createElement("span");
  current.className = "r32-pick-slot-current";

  button.append(label, current);
  renderPickText(button, pick);

  if (!enabled) {
    button.disabled = true;
    button.classList.add("is-not-pickable");
    button.title = disabledReason;
    return button;
  }

  button.title = playerFacingMenuSubtitle(logicSlot, title);
  button.addEventListener("pointerenter", () => trackButton({ layer, button, slotViewModel, phase: "hover" }));
  button.addEventListener("focus", () => trackButton({ layer, button, slotViewModel, phase: "focus" }));
  button.addEventListener("pointerleave", () => clearButtonTracking({ layer, button }));
  button.addEventListener("blur", () => clearButtonTracking({ layer, button }));
  button.addEventListener("click", () => {
    trackButton({ layer, button, slotViewModel, phase: "click" });
    createMenu({ layer, controller, button, slotViewModel });
  });
  return button;
}

async function createR32PickMenuLayer({
  logicSource = "data/model/fifa_r32_logical_slot_order.json",
  bridgeSource = "data/geometry/game1_fifa_slot_geometry_map.json",
  geometryManifest = "data/geometry/gameboard_manifest.json",
  lifecycleSource = "data/model/game1_lifecycle.json",
} = {}) {
  const layer = document.createElement("div");
  layer.className = "board-layer board-r32-pick-menu-layer";
  layer.dataset.layerRole = "r32-pick-menu";
  layer.dataset.r32PickMenuState = "loading";
  layer.dataset.r32PickButtonTracking = "enabled";

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") closeExistingMenu(layer);
  });

  try {
    const controller = await createGame1R32PickController({
      logicSource,
      bridgeSource,
      geometryManifest,
      lifecycleSource,
    });

    layer.controller = controller;
    const slotViewModels = controller.getSlotViewModels().filter((slot) => slot.logicSlot && slot.bounds);
    const trackerChip = createButtonTrackerChip();
    let enabled = 0;

    for (const slotViewModel of slotViewModels) {
      if (slotViewModel.enabled) enabled += 1;
      layer.append(createSlotButton({ layer, controller, slotViewModel }));
    }

    layer.addEventListener("click", (event) => {
      if (event.target === layer) closeExistingMenu(layer);
    });

    layer.dataset.r32PickMenuState = slotViewModels.length === 0 ? "empty" : "ready";
    layer.dataset.r32PickMenuCount = String(slotViewModels.length);
    layer.dataset.r32PickMenuEnabledCount = String(enabled);
    layer.dataset.pickableLifecycle = controller.isPickable ? "true" : "false";
    layer.dataset.lifecycleState = controller.lifecycleState || "unavailable";
    layer.append(trackerChip);
    updateButtonTrackerChip(layer, { phase: "clear" });
  } catch (error) {
    layer.dataset.r32PickMenuState = "error";
    layer.dataset.r32PickMenuError = error instanceof Error ? error.message : String(error);
  }

  return layer;
}

export { createR32PickMenuLayer };
