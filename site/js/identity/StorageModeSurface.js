const DEV_SUPABASE_STORE_FLAG = "devSupabaseBracketStore";

function isDevSupabaseBracketStoreRequested(locationSearch = window.location.search) {
  return new URLSearchParams(locationSearch).get(DEV_SUPABASE_STORE_FLAG) === "1";
}

function storageModeStatus({ signedIn = false, remoteRequested = false, remoteActive = false } = {}) {
  if (remoteActive) {
    return {
      mode: "remote-test",
      label: "Remote save test mode",
      detail: "Signed-in picks are saving to Supabase for this browser test.",
    };
  }

  if (remoteRequested && !signedIn) {
    return {
      mode: "local",
      label: "Playing locally",
      detail: "Remote save test mode was requested, but no signed-in session is active.",
    };
  }

  if (signedIn) {
    return {
      mode: "local",
      label: "Playing locally",
      detail: "You are signed in, but account save is not enabled for normal gameplay yet.",
    };
  }

  return {
    mode: "local",
    label: "Playing locally",
    detail: "Your picks are saved in this browser on this device.",
  };
}

function ensureStorageModeElement(root) {
  let element = root.querySelector("[data-storage-mode-status]");
  if (element) return element;

  element = document.createElement("aside");
  element.className = "storage-mode-status";
  element.setAttribute("data-storage-mode-status", "");
  element.setAttribute("aria-live", "polite");
  element.innerHTML = `
    <span class="storage-mode-status-dot" aria-hidden="true"></span>
    <span class="storage-mode-status-copy">
      <strong data-storage-mode-label></strong>
      <small data-storage-mode-detail></small>
    </span>
  `;

  root.appendChild(element);
  return element;
}

function renderStorageModeStatus(root, status) {
  const element = ensureStorageModeElement(root);
  const label = element.querySelector("[data-storage-mode-label]");
  const detail = element.querySelector("[data-storage-mode-detail]");

  element.dataset.storageMode = status.mode;
  label.textContent = status.label;
  detail.textContent = status.detail;
}

function createStorageModeSurface({ root, authService, remoteActive = false } = {}) {
  if (!root) throw new Error("StorageModeSurface requires a root element.");

  async function start() {
    let signedIn = false;

    try {
      const state = await authService?.currentState?.();
      signedIn = state?.status === "signed-in" || Boolean(state?.user?.id);
    } catch {
      signedIn = false;
    }

    renderStorageModeStatus(root, storageModeStatus({
      signedIn,
      remoteRequested: isDevSupabaseBracketStoreRequested(),
      remoteActive,
    }));
  }

  return { start };
}

export {
  createStorageModeSurface,
  isDevSupabaseBracketStoreRequested,
  storageModeStatus,
};
