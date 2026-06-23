import { SupabaseBracketStore } from "../services/SupabaseBracketStore.js";

const ACCOUNT_SAVE_STATE_ATTRIBUTE = "data-account-save-state";
const ACCOUNT_PICKS_LOADED_EVENT = "wc2026:account-picks-loaded";

function ensureAccountSaveElement(root) {
  let element = root.querySelector("[data-account-save-action]");
  if (element) return element;

  element = document.createElement("aside");
  element.className = "account-save-action";
  element.setAttribute("data-account-save-action", "");
  element.setAttribute("aria-live", "polite");
  element.innerHTML = `
    <button class="account-save-action-button" type="button" data-account-save-button disabled>
      Save Picks
    </button>
    <button class="account-save-action-button" type="button" data-account-load-button hidden>
      Load Saved
    </button>
    <span class="account-save-action-status" data-account-save-status></span>
  `;
  root.appendChild(element);
  return element;
}

function accountSavePresentation({
  signedIn = false,
  remoteActive = false,
  state = "idle",
  hasSavedAccountPicks = false,
} = {}) {
  if (remoteActive) {
    return {
      state: "remote-test",
      saveText: "Remote Test Active",
      loadText: "Load Saved",
      statusText: "Dev Supabase mode",
      saveDisabled: true,
      loadHidden: true,
      loadDisabled: true,
    };
  }

  if (!signedIn) {
    return {
      state: "signed-out",
      saveText: "Save Picks",
      loadText: "Load Saved",
      statusText: "Sign in to save and load picks",
      saveDisabled: true,
      loadHidden: true,
      loadDisabled: true,
    };
  }

  if (state === "checking") {
    return {
      state: "checking",
      saveText: "Save Picks",
      loadText: "Load Saved",
      statusText: "Checking account picks…",
      saveDisabled: true,
      loadHidden: true,
      loadDisabled: true,
    };
  }

  if (state === "loading") {
    return {
      state: "loading",
      saveText: "Save Picks",
      loadText: "Loading…",
      statusText: "Loading saved picks",
      saveDisabled: true,
      loadHidden: false,
      loadDisabled: true,
    };
  }

  if (state === "loaded") {
    return {
      state: "loaded",
      saveText: "Save Picks",
      loadText: "Load Saved",
      statusText: "Loaded saved account picks",
      saveDisabled: false,
      loadHidden: true,
      loadDisabled: true,
    };
  }

  if (state === "remote-found") {
    return {
      state: "remote-found",
      saveText: "Save Picks",
      loadText: "Load Saved",
      statusText: "Saved account picks found",
      saveDisabled: false,
      loadHidden: false,
      loadDisabled: false,
    };
  }

  if (state === "saving") {
    return {
      state: "saving",
      saveText: "Saving…",
      loadText: "Load Saved",
      statusText: "Saving to account",
      saveDisabled: true,
      loadHidden: !hasSavedAccountPicks,
      loadDisabled: true,
    };
  }

  if (state === "saved") {
    return {
      state: "saved",
      saveText: "Save Picks",
      loadText: "Load Saved",
      statusText: "Saved to account",
      saveDisabled: false,
      loadHidden: true,
      loadDisabled: true,
    };
  }

  if (state === "error") {
    return {
      state: "error",
      saveText: "Try Save Again",
      loadText: "Load Saved",
      statusText: "Account persistence failed; local picks remain safe",
      saveDisabled: false,
      loadHidden: !hasSavedAccountPicks,
      loadDisabled: !hasSavedAccountPicks,
    };
  }

  return {
    state: "ready",
    saveText: "Save Picks",
    loadText: "Load Saved",
    statusText: hasSavedAccountPicks ? "Saved account picks available" : "Account persistence ready",
    saveDisabled: false,
    loadHidden: !hasSavedAccountPicks,
    loadDisabled: !hasSavedAccountPicks,
  };
}

function renderAccountSaveAction(root, presentation) {
  const element = ensureAccountSaveElement(root);
  const saveButton = element.querySelector("[data-account-save-button]");
  const loadButton = element.querySelector("[data-account-load-button]");
  const status = element.querySelector("[data-account-save-status]");

  element.setAttribute(ACCOUNT_SAVE_STATE_ATTRIBUTE, presentation.state);
  saveButton.textContent = presentation.saveText;
  saveButton.disabled = presentation.saveDisabled;
  loadButton.textContent = presentation.loadText;
  loadButton.hidden = presentation.loadHidden;
  loadButton.disabled = presentation.loadDisabled;
  status.textContent = presentation.statusText;
}

function createAccountSaveActionSurface({
  root,
  authService,
  model,
  remoteActive = false,
  bracketStore = new SupabaseBracketStore(),
} = {}) {
  if (!root) throw new Error("AccountSaveActionSurface requires a root element.");
  if (!model?.getAccountSaveBracketDocument || !model?.importAccountBracketDocument) {
    throw new Error("AccountSaveActionSurface requires account save/load model methods.");
  }

  const element = ensureAccountSaveElement(root);
  const saveButton = element.querySelector("[data-account-save-button]");
  const loadButton = element.querySelector("[data-account-load-button]");
  let signedIn = false;
  let accountUserId = "";
  let saveState = "idle";
  let savedAccountBracket = null;
  let hasSavedAccountPicks = false;

  function localPickCount() {
    return Number(model.getSummary?.().picked || 0);
  }

  function render(nextSaveState = saveState) {
    saveState = nextSaveState;
    renderAccountSaveAction(root, accountSavePresentation({
      signedIn,
      remoteActive,
      state: saveState,
      hasSavedAccountPicks,
    }));
  }

  async function refreshAuthState() {
    const state = await authService?.currentState?.();
    signedIn = state?.status === "signed-in" || Boolean(state?.user?.id);
    accountUserId = state?.user?.id || "";
    return state;
  }

  async function loadSavedPicksFromAccount({ automatic = false } = {}) {
    if (remoteActive || !signedIn || !savedAccountBracket) return;

    render("loading");
    try {
      const result = model.importAccountBracketDocument(savedAccountBracket);
      if (!result?.ok) {
        throw new Error(result?.reason || "Saved account picks could not be loaded.");
      }

      hasSavedAccountPicks = true;
      render("loaded");
      window.dispatchEvent(new CustomEvent(ACCOUNT_PICKS_LOADED_EVENT, {
        detail: { automatic, imported: result.imported || 0 },
      }));
    } catch (error) {
      console.error("[AccountSaveActionSurface] Load Saved Picks failed", error);
      render("error");
    }
  }

  async function checkSavedAccountPicks({ automatic = false } = {}) {
    await refreshAuthState();

    if (remoteActive) {
      render("remote-test");
      return;
    }

    if (!signedIn) {
      savedAccountBracket = null;
      hasSavedAccountPicks = false;
      render("signed-out");
      return;
    }

    render("checking");

    try {
      savedAccountBracket = await bracketStore.loadUserBracket(accountUserId);
      hasSavedAccountPicks = Boolean(savedAccountBracket?.picksBySlot && Object.keys(savedAccountBracket.picksBySlot).length);

      if (hasSavedAccountPicks && localPickCount() === 0) {
        await loadSavedPicksFromAccount({ automatic });
        return;
      }

      if (hasSavedAccountPicks) {
        render("remote-found");
        return;
      }

      render("ready");
    } catch (error) {
      console.error("[AccountSaveActionSurface] Account persistence check failed", error);
      render("error");
    }
  }

  async function savePicksToAccount() {
    if (remoteActive) return;

    await refreshAuthState();
    if (!signedIn) {
      render("signed-out");
      return;
    }

    render("saving");
    try {
      const bracketDocument = model.getAccountSaveBracketDocument({ userId: accountUserId });
      savedAccountBracket = await bracketStore.saveUserBracket(bracketDocument);
      hasSavedAccountPicks = true;
      render("saved");
    } catch (error) {
      console.error("[AccountSaveActionSurface] Save Picks failed", error);
      render("error");
    }
  }

  async function start() {
    await checkSavedAccountPicks({ automatic: true });

    authService?.subscribe?.((state) => {
      signedIn = state?.status === "signed-in" || Boolean(state?.user?.id);
      accountUserId = state?.user?.id || "";
      if (!signedIn) {
        savedAccountBracket = null;
        hasSavedAccountPicks = false;
        render("signed-out");
        return;
      }
      checkSavedAccountPicks({ automatic: true });
    });
  }

  saveButton.addEventListener("click", savePicksToAccount);
  loadButton.addEventListener("click", () => loadSavedPicksFromAccount({ automatic: false }));

  return { start };
}

export {
  ACCOUNT_PICKS_LOADED_EVENT,
  accountSavePresentation,
  createAccountSaveActionSurface,
};
