import { SupabaseBracketStore } from "../services/SupabaseBracketStore.js";

const ACCOUNT_SAVE_STATE_ATTRIBUTE = "data-account-save-state";

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
    <span class="account-save-action-status" data-account-save-status></span>
  `;
  root.appendChild(element);
  return element;
}

function accountSavePresentation({ signedIn = false, remoteActive = false, state = "idle" } = {}) {
  if (remoteActive) {
    return {
      state: "remote-test",
      buttonText: "Remote Test Active",
      statusText: "Dev Supabase mode",
      disabled: true,
    };
  }

  if (!signedIn) {
    return {
      state: "signed-out",
      buttonText: "Save Picks",
      statusText: "Sign in to save",
      disabled: true,
    };
  }

  if (state === "saving") {
    return {
      state: "saving",
      buttonText: "Saving…",
      statusText: "Saving to account",
      disabled: true,
    };
  }

  if (state === "saved") {
    return {
      state: "saved",
      buttonText: "Save Picks",
      statusText: "Saved to account",
      disabled: false,
    };
  }

  if (state === "error") {
    return {
      state: "error",
      buttonText: "Try Save Again",
      statusText: "Save failed; local picks remain safe",
      disabled: false,
    };
  }

  return {
    state: "ready",
    buttonText: "Save Picks",
    statusText: "Save to account",
    disabled: false,
  };
}

function renderAccountSaveAction(root, presentation) {
  const element = ensureAccountSaveElement(root);
  const button = element.querySelector("[data-account-save-button]");
  const status = element.querySelector("[data-account-save-status]");

  element.setAttribute(ACCOUNT_SAVE_STATE_ATTRIBUTE, presentation.state);
  button.textContent = presentation.buttonText;
  button.disabled = presentation.disabled;
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
  if (!model?.getAccountSaveBracketDocument) {
    throw new Error("AccountSaveActionSurface requires model.getAccountSaveBracketDocument.");
  }

  const element = ensureAccountSaveElement(root);
  const button = element.querySelector("[data-account-save-button]");
  let signedIn = false;
  let accountUserId = "";
  let saveState = "idle";

  async function refresh(nextSaveState = saveState) {
    saveState = nextSaveState;
    const state = await authService?.currentState?.();
    signedIn = state?.status === "signed-in" || Boolean(state?.user?.id);
    accountUserId = state?.user?.id || "";
    renderAccountSaveAction(root, accountSavePresentation({ signedIn, remoteActive, state: saveState }));
  }

  async function savePicksToAccount() {
    if (remoteActive || !signedIn) return;

    await refresh("saving");
    try {
      const bracketDocument = model.getAccountSaveBracketDocument({ userId: accountUserId });
      await bracketStore.saveUserBracket(bracketDocument);
      await refresh("saved");
    } catch (error) {
      console.error("[AccountSaveActionSurface] Save Picks failed", error);
      await refresh("error");
    }
  }

  async function start() {
    await refresh("idle");

    authService?.subscribe?.((state) => {
      signedIn = state?.status === "signed-in" || Boolean(state?.user?.id);
      accountUserId = state?.user?.id || "";
      saveState = signedIn ? saveState : "idle";
      renderAccountSaveAction(root, accountSavePresentation({ signedIn, remoteActive, state: saveState }));
    });
  }

  button.addEventListener("click", savePicksToAccount);

  return { start };
}

export {
  accountSavePresentation,
  createAccountSaveActionSurface,
};
