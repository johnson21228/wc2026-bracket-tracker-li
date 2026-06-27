import { SupabaseBracketStore } from "../services/SupabaseBracketStore.js";

const ACCOUNT_SAVE_STATE_ATTRIBUTE = "data-account-save-state";
const ACCOUNT_PICKS_LOADED_EVENT = "wc2026:account-picks-loaded";
const AUTOSAVE_DELAY_MS = 650;
const JOINED_PICKS_LOADED_MESSAGE = "Saved picks have been loaded.";
const NOT_JOINED_STARTUP_MESSAGE = "Playing Bracketeering requires you to join the pool. Tap the button with the person icon to join. Tap the button with the “i” to get information about playing the game.";

function pickFingerprintFromDocument(bracketDocument) {
  const picksBySlot = bracketDocument?.picksBySlot || {};
  return JSON.stringify(Object.entries(picksBySlot)
    .map(([slotId, record]) => {
      const teamId = record?.pick?.kind === "team" ? record.pick.teamId : record?.teamId;
      return [slotId, teamId || ""];
    })
    .filter(([, teamId]) => teamId)
    .sort(([left], [right]) => left.localeCompare(right)));
}

function ensureJoinLivePicksElement(root) {
  let element = root.querySelector("[data-join-live-picks]");
  if (element) return element;

  element = document.createElement("aside");
  element.className = "join-live-picks-status";
  element.setAttribute("data-join-live-picks", "");
  element.setAttribute(ACCOUNT_SAVE_STATE_ATTRIBUTE, "not-joined");
  element.setAttribute("aria-live", "polite");
  element.innerHTML = `
    <span class="join-live-picks-status-text" data-join-live-picks-status></span>
    <div class="join-live-picks-conflict" data-join-live-picks-conflict hidden></div>
  `;
  root.appendChild(element);
  return element;
}

function renderStatus(root, state, message) {
  const element = ensureJoinLivePicksElement(root);
  const status = element.querySelector("[data-join-live-picks-status]");
  element.setAttribute(ACCOUNT_SAVE_STATE_ATTRIBUTE, state);
  status.textContent = message || "";
}

function renderConflict(root, { onUseSaved, onKeepBoard }) {
  const element = ensureJoinLivePicksElement(root);
  const conflict = element.querySelector("[data-join-live-picks-conflict]");
  element.setAttribute(ACCOUNT_SAVE_STATE_ATTRIBUTE, "conflict");
  conflict.hidden = false;
  conflict.innerHTML = `
    <div class="join-live-picks-conflict-actions">
      <button type="button" data-use-saved-picks>Continue</button>
    </div>
  `;
  conflict.querySelector("[data-use-saved-picks]")?.addEventListener("click", onUseSaved);
  conflict.querySelector("[data-keep-board-picks]")?.addEventListener("click", onKeepBoard);
}

function renderNotice(root, state, message) {
  const element = ensureJoinLivePicksElement(root);
  const conflict = element.querySelector("[data-join-live-picks-conflict]");
  const status = element.querySelector("[data-join-live-picks-status]");
  element.setAttribute(ACCOUNT_SAVE_STATE_ATTRIBUTE, state);
  status.textContent = "";
  conflict.hidden = false;
  conflict.innerHTML = `
    <p>${message}</p>
    <div class="join-live-picks-conflict-actions">
      <button type="button" data-dismiss-join-live-picks-notice>Continue</button>
    </div>
  `;
  conflict.querySelector("[data-dismiss-join-live-picks-notice]")?.addEventListener("click", () => {
    clearConflict(root);
  });
}

function clearConflict(root) {
  const conflict = ensureJoinLivePicksElement(root).querySelector("[data-join-live-picks-conflict]");
  conflict.hidden = true;
  conflict.innerHTML = "";
}

function clearNotice(root, type) {
  if (!root) return;
  const notice = root.querySelector?.(`[data-account-save-notice="${type}"]`);
  if (notice) {
    notice.remove();
    return;
  }
  if (type === "not-joined" && root.textContent?.includes("Playing Bracketeering requires you to join the pool")) {
    root.replaceChildren();
  }
  if (type === "not-joined" && root.textContent?.includes("Playing Bracketeering requires you to join the Pool")) {
    root.replaceChildren();
  }
}

function createAccountSaveActionSurface({
  root,
  authService,
  model,
  bracketStore = new SupabaseBracketStore(),
} = {}) {
  if (!root) throw new Error("AccountSaveActionSurface requires a root element.");
  if (!model?.getAccountSaveBracketDocument || !model?.importAccountBracketDocument) {
    throw new Error("AccountSaveActionSurface requires canonical account bracket document methods.");
  }

  ensureJoinLivePicksElement(root);

  let joined = false;
  let playerUserId = "";
  let authSettled = false;
  let autosaveTimer = null;
  let retryTimer = null;
  let conflictActive = false;
  let loadedJoinedBracket = null;
  let lastJoinedPickFingerprint = "";

  async function refreshJoinState() {
    const state = await authService?.currentState?.();
    joined = state?.status === "signed-in" || Boolean(state?.user?.id);
    playerUserId = state?.user?.id || "";
    authSettled = Boolean(state?.status) && state.status !== "loading" && state.status !== "initializing";
    if (joined) {
      clearNotice(root, "not-joined");
    }
    return state;
  }

  function localPickCount() {
    return Number(model.getSummary?.().picked || 0);
  }

  function currentDocument() {
    return model.getAccountSaveBracketDocument({ userId: playerUserId || "local-player" });
  }

  function currentFingerprint() {
    return pickFingerprintFromDocument(currentDocument());
  }

  function dispatchLoadedPicks({ automatic = false, imported = 0 } = {}) {
    window.dispatchEvent(new CustomEvent(ACCOUNT_PICKS_LOADED_EVENT, {
      detail: { automatic, imported },
    }));
  }

  async function writeJoinedPicks({ retryOnFailure = true } = {}) {
    if (!joined || !playerUserId || conflictActive) return;

    if (retryTimer) {
      clearTimeout(retryTimer);
      retryTimer = null;
    }

    renderStatus(root, "saving", "Saving…");

    try {
      const bracketDocument = currentDocument();
      const saved = await bracketStore.saveUserBracket(bracketDocument);
      loadedJoinedBracket = saved || bracketDocument;
      lastJoinedPickFingerprint = pickFingerprintFromDocument(loadedJoinedBracket);
      renderStatus(root, "saved", "");
    } catch (error) {
      console.error("[JoinLivePicks] autosave failed", error);
      renderStatus(root, "retrying", "Could not save — retrying");
      if (retryOnFailure) {
        retryTimer = window.setTimeout(() => writeJoinedPicks({ retryOnFailure: true }), 2500);
      }
    }
  }

  function scheduleAutosave() {
    if (!joined || !playerUserId || conflictActive) return;

    if (autosaveTimer) clearTimeout(autosaveTimer);
    autosaveTimer = window.setTimeout(() => {
      autosaveTimer = null;
      if (currentFingerprint() !== lastJoinedPickFingerprint) {
        writeJoinedPicks();
      }
    }, AUTOSAVE_DELAY_MS);
  }

  async function useSavedPicks() {
    if (!loadedJoinedBracket) return;
    conflictActive = false;
    clearConflict(root);

    try {
      const result = model.importAccountBracketDocument(loadedJoinedBracket);
      if (!result?.ok) throw new Error(result?.reason || "Saved picks could not be used.");
      renderStatus(root, "loaded", JOINED_PICKS_LOADED_MESSAGE);

      lastJoinedPickFingerprint = pickFingerprintFromDocument(loadedJoinedBracket);
      renderStatus(root, "saved", "");
      dispatchLoadedPicks({ automatic: false, imported: result.imported || 0 });
    } catch (error) {
      console.error("[JoinLivePicks] load saved joined bracket failed", error);
      renderStatus(root, "retrying", "Could not save — retrying");
    }
  }

  async function keepThisBoard() {
    conflictActive = false;
    clearConflict(root);
    await writeJoinedPicks();
  }

  async function reconcileJoinedPicks({ automatic = false } = {}) {
    await refreshJoinState();


    if (!joined) {
      loadedJoinedBracket = null;
      lastJoinedPickFingerprint = "";
      conflictActive = false;
      clearConflict(root);
      if (authSettled) {
        renderNotice(root, "not-joined", NOT_JOINED_STARTUP_MESSAGE);
      }
      return;
    }

    renderStatus(root, "joining", "Joining…");

    try {
      loadedJoinedBracket = await bracketStore.loadUserBracket(playerUserId);
      const hasJoinedPicks = Boolean(
        loadedJoinedBracket?.picksBySlot && Object.keys(loadedJoinedBracket.picksBySlot).length
      );

      if (!hasJoinedPicks) {
        lastJoinedPickFingerprint = "";
        renderStatus(root, "joined", "Joined");
        if (localPickCount() > 0) scheduleAutosave();
        return;
      }

      lastJoinedPickFingerprint = pickFingerprintFromDocument(loadedJoinedBracket);

      if (localPickCount() === 0) {
        const result = model.importAccountBracketDocument(loadedJoinedBracket);
        if (!result?.ok) throw new Error(result?.reason || "Joined picks could not be loaded.");
        renderStatus(root, "loaded", JOINED_PICKS_LOADED_MESSAGE);
        renderStatus(root, "saved", "");
        dispatchLoadedPicks({ automatic, imported: result.imported || 0 });
        return;
      }

      if (currentFingerprint() !== lastJoinedPickFingerprint) {
        conflictActive = true;
        renderConflict(root, { onUseSaved: useSavedPicks, onKeepBoard: keepThisBoard });
        return;
      }

      renderStatus(root, "saved", "");
    } catch (error) {
      console.error("[JoinLivePicks] join reconcile failed", error);
      renderStatus(root, "retrying", "Could not save — retrying");
    }
  }

  async function start() {
    await reconcileJoinedPicks({ automatic: true });

    window.addEventListener("wc2026:picks-changed", scheduleAutosave);

    authService?.subscribe?.((state) => {
      joined = state?.status === "signed-in" || Boolean(state?.user?.id);
      playerUserId = state?.user?.id || "";
      authSettled = Boolean(state?.status) && state.status !== "loading" && state.status !== "initializing";
      if (joined) {
        clearNotice(root, "not-joined");
      }
      reconcileJoinedPicks({ automatic: true });
    });
  }

  return { start };
}

export {
  ACCOUNT_PICKS_LOADED_EVENT,
  AUTOSAVE_DELAY_MS,
  createAccountSaveActionSurface,
  pickFingerprintFromDocument,
};
