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

function accountSavePresentation({ signedIn = false, remoteActive = false } = {}) {
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

  return {
    state: "ready",
    buttonText: "Save Picks",
    statusText: "Account save target",
    disabled: true,
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

function createAccountSaveActionSurface({ root, authService, remoteActive = false } = {}) {
  if (!root) throw new Error("AccountSaveActionSurface requires a root element.");

  async function start() {
    let signedIn = false;

    try {
      const state = await authService?.currentState?.();
      signedIn = state?.status === "signed-in" || Boolean(state?.user?.id);
    } catch {
      signedIn = false;
    }

    renderAccountSaveAction(root, accountSavePresentation({ signedIn, remoteActive }));
  }

  return { start };
}

export {
  accountSavePresentation,
  createAccountSaveActionSurface,
};
