(() => {
  const DEFAULT_PROPERTIES = Object.freeze({
    LockDownTimeZone: "America/New_York",
    LockDownTime1: "2026-06-28T15:00:00-04:00",
    LockDownTime2: "2026-06-29T13:00:00-04:00",
    LockDownTime1Name: "Canada vs South Africa pick lock",
    LockDownTime2Name: "All remaining picks lock",
    LockDownTime1SlotIds: ["R-R32-01"],
    LockDownTime1TeamIds: ["CAN", "RSA"],
  });

  const state = {
    properties: { ...DEFAULT_PROPERTIES },
    loaded: false,
  };

  function parseTime(value) {
    const time = Date.parse(String(value || ""));
    return Number.isFinite(time) ? time : Number.POSITIVE_INFINITY;
  }

  function nowMs(now) {
    if (now instanceof Date) return now.getTime();
    if (typeof now === "number") return now;
    return Date.now();
  }

  function normalize(value) {
    return String(value || "").trim();
  }

  function tokenMatch(value, allowed) {
    const normalized = normalize(value);
    if (!normalized) return false;
    return (allowed || []).map(normalize).includes(normalized);
  }

  function isGlobalLocked(now) {
    return nowMs(now) >= parseTime(state.properties.LockDownTime2);
  }

  function isLockdown1Active(now) {
    return nowMs(now) >= parseTime(state.properties.LockDownTime1);
  }

  function isLockdown1SlotToken(slotId, teamId, text) {
    if (tokenMatch(slotId, state.properties.LockDownTime1SlotIds)) return true;
    if (tokenMatch(teamId, state.properties.LockDownTime1TeamIds)) return true;

    const lower = String(text || "").toLowerCase();
    return (
      (lower.includes("canada") || lower.includes("can")) &&
      (lower.includes("south africa") || lower.includes("rsa"))
    );
  }

  function elementTokens(element) {
    const dataset = element?.dataset || {};
    return {
      slotId:
        dataset.slotId ||
        dataset.pickSlotId ||
        dataset.pickSlot ||
        dataset.slot ||
        element?.getAttribute?.("data-slot-id") ||
        element?.getAttribute?.("data-pick-slot-id") ||
        element?.getAttribute?.("data-pick-slot") ||
        element?.getAttribute?.("data-slot") ||
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

  function getLockedPickReasonForTokens(tokens, now) {
    if (isGlobalLocked(now)) {
      return {
        locked: true,
        lockLevel: "LockDownTime2",
        lockName: state.properties.LockDownTime2Name,
        lockTime: state.properties.LockDownTime2,
      };
    }

    if (
      isLockdown1Active(now) &&
      isLockdown1SlotToken(tokens.slotId, tokens.teamId, tokens.text)
    ) {
      return {
        locked: true,
        lockLevel: "LockDownTime1",
        lockName: state.properties.LockDownTime1Name,
        lockTime: state.properties.LockDownTime1,
      };
    }

    return { locked: false };
  }

  function getLockedPickReason(slotOrElement, maybeTeamId, now) {
    if (slotOrElement && typeof slotOrElement === "object" && slotOrElement.nodeType === 1) {
      return getLockedPickReasonForTokens(elementTokens(slotOrElement), maybeTeamId);
    }

    return getLockedPickReasonForTokens({
      slotId: slotOrElement,
      teamId: maybeTeamId,
      text: "",
    }, now);
  }

  function nearestPickElement(target) {
    if (!target || !target.closest) return null;
    return target.closest([
      "[data-slot-id]",
      "[data-pick-slot-id]",
      "[data-pick-slot]",
      "[data-slot]",
      ".pick-slot-button",
      ".pick-cell",
      ".bracket-slot",
    ].join(","));
  }

  function markElement(element, reason) {
    if (!element) return;
    element.classList.toggle("is-pick-locked", Boolean(reason.locked));

    if (reason.locked) {
      element.setAttribute("aria-disabled", "true");
      element.setAttribute("data-pick-locked", reason.lockLevel);
      element.setAttribute("title", `${reason.lockName}: locked after ${reason.lockTime}`);
      if ("disabled" in element) element.disabled = true;
    }
  }

  function applyLockedState(root = document) {
    if (!root || !root.querySelectorAll) return;

    root.querySelectorAll([
      "[data-slot-id]",
      "[data-pick-slot-id]",
      "[data-pick-slot]",
      "[data-slot]",
      ".pick-slot-button",
      ".pick-cell",
      ".bracket-slot",
    ].join(",")).forEach((element) => {
      markElement(element, getLockedPickReason(element));
    });
  }

  function blockLockedInteraction(event) {
    const pickElement = nearestPickElement(event.target);
    if (!pickElement) return;

    const reason = getLockedPickReason(pickElement);
    if (!reason.locked) return;

    markElement(pickElement, reason);
    event.preventDefault();
    event.stopPropagation();

    if (typeof event.stopImmediatePropagation === "function") {
      event.stopImmediatePropagation();
    }

    window.dispatchEvent(new CustomEvent("bracketeering:pick-lockdown-blocked", {
      detail: {
        lockLevel: reason.lockLevel,
        lockName: reason.lockName,
        lockTime: reason.lockTime,
      },
    }));
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

  window.BracketeeringPickLockdownPolicy = {
    get properties() {
      return state.properties;
    },
    get loaded() {
      return state.loaded;
    },
    loadProperties,
    applyLockedState,
    getLockedPickReason,
    getLockedPickReasonForTokens,
    isGlobalLocked,
    isLockdown1Active,
    isLockdown1SlotToken,
  };

  document.addEventListener("pointerdown", blockLockedInteraction, true);
  document.addEventListener("click", blockLockedInteraction, true);
  document.addEventListener("keydown", (event) => {
    if (event.key !== "Enter" && event.key !== " ") return;
    blockLockedInteraction(event);
  }, true);

  document.addEventListener("DOMContentLoaded", () => {
    loadProperties();
    setInterval(() => applyLockedState(document), 30000);
  });
})();
