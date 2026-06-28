(() => {
  const DEFAULT_PROPERTIES = Object.freeze({
    LockDown: false,
  });

  const state = {
    properties: { ...DEFAULT_PROPERTIES },
    loaded: false,
  };

  function isManualLockDownEnabled() {
    const value = state.properties.LockDown;
    return value === true || String(value).toLowerCase() === "true";
  }

  function isGlobalLocked() {
    return isManualLockDownEnabled();
  }

  function tokensFromInput(input, maybeTeamId) {
    if (input && typeof input === "object") {
      const dataset = input.dataset || {};
      return {
        slotId:
          input.slotId ||
          input.fifaSlotId ||
          input.pickSlotId ||
          dataset.slotId ||
          dataset.pickSlotId ||
          dataset.pickSlot ||
          dataset.slot ||
          input.getAttribute?.("data-slot-id") ||
          input.getAttribute?.("data-pick-slot-id") ||
          "",
        teamId:
          input.teamId ||
          input.abbr ||
          dataset.teamId ||
          dataset.pickTeamId ||
          input.getAttribute?.("data-team-id") ||
          input.getAttribute?.("data-pick-team-id") ||
          maybeTeamId ||
          "",
        text: input.text || input.textContent || "",
      };
    }

    return {
      slotId: input || "",
      teamId: maybeTeamId || "",
      text: "",
    };
  }

  function getLockedPickReasonForTokens(tokens) {
    if (!isGlobalLocked()) return { locked: false };

    return {
      locked: true,
      lockLevel: "LockDown",
      lockName: "Game lockdown",
      lockTime: "manual",
      slotId: tokens?.slotId || "",
      teamId: tokens?.teamId || "",
    };
  }

  function getLockedPickReason(input, maybeTeamId) {
    return getLockedPickReasonForTokens(tokensFromInput(input, maybeTeamId));
  }

  function isPickChangeAllowed(input, maybeTeamId) {
    return !getLockedPickReason(input, maybeTeamId).locked;
  }

  function assertPickChangeAllowed(input, maybeTeamId) {
    const reason = getLockedPickReason(input, maybeTeamId);
    if (!reason.locked) return true;

    const error = new Error(`${reason.lockName}: player picks are locked.`);
    error.name = "PickLockdownError";
    error.pickLockdownReason = reason;
    throw error;
  }

  function applyLockedState(root = document) {
    // Intentionally non-visual.
    // Lockdown must not change slot rendering, CSS classes, disabled state,
    // cursor behavior, board pan/zoom, official truth hydration, or standings.
    return root;
  }

  async function loadProperties() {
    try {
      const response = await fetch("data/current/site_properties.json", { cache: "no-store" });
      if (response.ok) {
        const json = await response.json();
        state.properties = { ...DEFAULT_PROPERTIES, ...json };
      }
    } catch (_error) {
      state.properties = { ...DEFAULT_PROPERTIES };
    } finally {
      state.loaded = true;
      applyLockedState(document);
    }
  }

  const api = {
    get properties() {
      return state.properties;
    },
    get loaded() {
      return state.loaded;
    },
    loadProperties,
    applyLockedState,
    tokensFromInput,
    getLockedPickReason,
    getLockedPickReasonForTokens,
    isGlobalLocked,
    isManualLockDownEnabled,
    isPickChangeAllowed,
    assertPickChangeAllowed,
  };

  window.BracketeeringPickLockdownPolicy = api;
  window.PickLockdownPolicy = api;

  document.addEventListener("DOMContentLoaded", () => {
    loadProperties();
  });
})();
