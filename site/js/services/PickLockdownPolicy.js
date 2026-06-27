(() => {
  const DEFAULT_PROPERTIES = {
    LockDown: false,
    LockDownName: "All player picks locked",
    LockDownTimeZone: "America/New_York",
    LockDownTime2: "2026-06-29T13:00:00-04:00",
    LockDownTime2Name: "All remaining picks lock",
  };

  const state = {
    properties: { ...DEFAULT_PROPERTIES },
    loaded: false,
    loadPromise: null,
  };

  function parseTime(value) {
    const ms = Date.parse(String(value || ""));
    return Number.isFinite(ms) ? ms : Number.POSITIVE_INFINITY;
  }

  function nowMs(now) {
    if (now instanceof Date) return now.getTime();
    if (now) {
      const parsed = Date.parse(String(now));
      if (Number.isFinite(parsed)) return parsed;
    }
    return Date.now();
  }

  function isGlobalLocked(now) {
    return Boolean(state.properties.LockDown) || nowMs(now) >= parseTime(state.properties.LockDownTime2);
  }

  function elementTokens(element) {
    const dataset = element?.dataset || {};
    return {
      slotId:
        dataset.slotId ||
        dataset.pickSlotId ||
        dataset.pickSlot ||
        dataset.slot ||
        dataset.fifaSlotId ||
        dataset.geometrySlotId ||
        element?.getAttribute?.("data-slot-id") ||
        element?.getAttribute?.("data-pick-slot-id") ||
        element?.getAttribute?.("data-pick-slot") ||
        element?.getAttribute?.("data-slot") ||
        element?.getAttribute?.("data-fifa-slot-id") ||
        element?.getAttribute?.("data-geometry-slot-id") ||
        "",
      teamId:
        dataset.teamId ||
        dataset.pickTeamId ||
        element?.getAttribute?.("data-team-id") ||
        element?.getAttribute?.("data-pick-team-id") ||
        "",
      text: element?.textContent || "",
    };
  }

  function tokensFromInput(input, maybeTeamId = "") {
    if (input && typeof input === "object" && input.nodeType === 1) {
      return elementTokens(input);
    }

    if (input && typeof input === "object") {
      return {
        slotId:
          input.slotId ||
          input.pickSlotId ||
          input.fifaSlotId ||
          input.geometrySlotId ||
          "",
        teamId:
          input.teamId ||
          input.pickTeamId ||
          maybeTeamId ||
          "",
        text:
          input.text ||
          input.label ||
          input.title ||
          "",
      };
    }

    return {
      slotId: input,
      teamId: maybeTeamId,
      text: "",
    };
  }

  function getLockedPickReasonForTokens(tokens = {}, now) {
    if (isGlobalLocked(now)) {
      return {
        locked: true,
        lockLevel: "LockDownTime2",
        lockName: state.properties.LockDown
          ? state.properties.LockDownName || "All player picks locked"
          : state.properties.LockDownTime2Name || "All remaining picks lock",
        lockTime: state.properties.LockDown ? "manual LockDown" : state.properties.LockDownTime2,
      };
    }

    return { locked: false };
  }

  function getLockedPickReason(slotOrElement, maybeTeamId, now) {
    return getLockedPickReasonForTokens(tokensFromInput(slotOrElement, maybeTeamId), now);
  }

  function isPickChangeAllowed(input, maybeTeamId, now) {
    return !getLockedPickReason(input, maybeTeamId, now).locked;
  }

  function assertPickChangeAllowed(input, maybeTeamId, now) {
    const reason = getLockedPickReason(input, maybeTeamId, now);
    if (!reason.locked) {
      return { ok: true, locked: false };
    }

    return {
      ok: false,
      locked: true,
      reason: `${reason.lockName}: locked after ${reason.lockTime}`,
      lockLevel: reason.lockLevel,
      lockName: reason.lockName,
      lockTime: reason.lockTime,
    };
  }

  function nearestPickElement(target) {
    return target?.closest?.([
      "[data-slot-id]",
      "[data-pick-slot-id]",
      "[data-pick-slot]",
      "[data-slot]",
      "[data-fifa-slot-id]",
      "[data-geometry-slot-id]",
      ".pick-slot-button",
      ".pick-cell",
      ".bracket-slot",
    ].join(","));
  }

  function applyLockedState(root = document) {
    // Lockdown is intentionally non-visual.
    // Picks render exactly as they did before lockdown.
    // Enforcement happens only when a player attempts to change a pick.
    return root;
  }

  function blockLockedInteraction(event) {
    const element = nearestPickElement(event?.target);
    if (!element) return;

    const reason = getLockedPickReason(element);
    if (!reason.locked) return;

    event.preventDefault();
    event.stopPropagation();
    if (typeof event.stopImmediatePropagation === "function") {
      event.stopImmediatePropagation();
    }

    window.dispatchEvent(new CustomEvent("bracketeering:pick-lockdown-blocked", {
      detail: reason,
    }));
  }

  function installInteractionBlocker(root = document) {
    if (!root || !root.addEventListener) return;
    [
      "click",
      "dblclick",
      "pointerdown",
      "pointerup",
      "mousedown",
      "mouseup",
      "touchstart",
      "touchend",
      "keydown",
      "change",
      "input",
      "submit",
    ].forEach((eventName) => {
      root.addEventListener(eventName, blockLockedInteraction, true);
    });
  }

  async function loadProperties() {
    if (state.loadPromise) return state.loadPromise;

    state.loadPromise = fetch("data/current/site_properties.json", { cache: "no-store" })
      .then((response) => {
        if (!response.ok) throw new Error(`site_properties load failed: ${response.status}`);
        return response.json();
      })
      .then((properties) => {
        state.properties = { ...DEFAULT_PROPERTIES, ...properties };
        state.loaded = true;
        return state.properties;
      })
      .catch(() => {
        state.properties = { ...DEFAULT_PROPERTIES };
        state.loaded = false;
        return state.properties;
      });

    return state.loadPromise;
  }

  installInteractionBlocker(document);
  loadProperties();

  window.BracketeeringPickLockdownPolicy = {
    get properties() {
      return state.properties;
    },
    get loaded() {
      return state.loaded;
    },
    loadProperties,
    applyLockedState,
    installInteractionBlocker,
    getLockedPickReason,
    getLockedPickReasonForTokens,
    tokensFromInput,
    isPickChangeAllowed,
    assertPickChangeAllowed,
    isGlobalLocked,
  };
})();
