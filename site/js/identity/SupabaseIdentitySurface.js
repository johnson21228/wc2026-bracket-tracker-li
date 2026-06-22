export function createSupabaseIdentitySurface({ root, authService }) {
  const surface = root.querySelector("[data-supabase-identity-surface]");
  if (!surface) {
    return { start() {} };
  }

  const authSignIn = authService?.signInWithMagicLink || authService?.signInWithEmail;
  let panelOpen = false;
  let emailDraft = "";
  let latestState = authService?.currentState?.() || {
    configured: false,
    status: "not-configured",
    user: null,
    message: "Supabase Auth is not configured yet.",
  };
  let cooldownUntil = 0;
  let cooldownTimer = null;

  function escapeHtml(value) {
    return String(value || "")
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#39;");
  }

  function cooldownRemainingSeconds() {
    return Math.max(0, Math.ceil((cooldownUntil - Date.now()) / 1000));
  }

  function scheduleCooldownTick() {
    if (cooldownTimer) {
      clearTimeout(cooldownTimer);
      cooldownTimer = null;
    }
    if (cooldownRemainingSeconds() > 0) {
      cooldownTimer = window.setTimeout(() => render(latestState), 1000);
    }
  }

  function statusLabel(state) {
    if (state.status === "signed-in") return state.user?.label || "Signed in";
    if (state.status === "checking") return "Checking sign-in";
    if (state.status === "sending") return "Sending link";
    if (state.status === "link-sent") return "Check email";
    if (state.status === "error") return "Sign-in needs attention";
    return "Sign in to save";
  }

  function persistenceLabel(state) {
    if (state.status === "signed-in") return "Local bracket for now";
    if (state.status === "not-configured") return "Local bracket · Supabase Auth not configured";
    return "Local bracket for now";
  }

  function panelMessage(state) {
    return state.message || "Sign in is identity-only for now. Bracket picks remain saved locally in this browser.";
  }

  function render(state = latestState) {
    latestState = state;
    const isSignedIn = state.status === "signed-in";
    const isBusy = state.status === "checking" || state.status === "sending";
    const cooldownSeconds = cooldownRemainingSeconds();
    const canAttemptSignIn = Boolean(state.configured && !isSignedIn && authSignIn);
    const canSubmit = canAttemptSignIn && !isBusy && cooldownSeconds === 0;
    const panelId = "supabase-identity-panel";

    surface.innerHTML = `
      <div class="identity-card identity-compact-card" data-auth-state="${escapeHtml(state.status)}">
        <button type="button" class="identity-status-button" data-identity-panel-open aria-haspopup="dialog" aria-controls="${panelId}" aria-expanded="${panelOpen ? "true" : "false"}">
          <span class="identity-title">${escapeHtml(statusLabel(state))}</span>
          <span class="identity-detail">${escapeHtml(persistenceLabel(state))}</span>
        </button>
      </div>
      <div class="identity-panel-backdrop" data-identity-panel-backdrop ${panelOpen ? "" : "hidden"}>
        <section class="identity-panel" id="${panelId}" role="dialog" aria-modal="true" aria-labelledby="supabase-identity-panel-title">
          <div class="identity-panel-header">
            <div>
              <p class="identity-kicker">Bracketeering identity</p>
              <h2 id="supabase-identity-panel-title">Sign in to Bracketeering Hub</h2>
            </div>
            <button type="button" class="identity-panel-close" data-identity-panel-close aria-label="Close sign-in panel">×</button>
          </div>
          <p class="identity-panel-intro">Play locally without signing in, or sign in to test identity before online bracket saving is enabled.</p>
          <p class="identity-local-note"><strong>Bracket persistence:</strong> local browser storage remains active. Supabase bracket writes are not enabled yet.</p>
          <div class="identity-panel-state" data-auth-state="${escapeHtml(state.status)}">
            <strong>${escapeHtml(statusLabel(state))}</strong>
            <span>${escapeHtml(panelMessage(state))}</span>
          </div>
          <div class="identity-panel-actions"></div>
        </section>
      </div>
    `;

    surface.querySelector("[data-identity-panel-open]")?.addEventListener("click", () => {
      panelOpen = true;
      render(latestState);
      window.setTimeout(() => surface.querySelector("#supabase-auth-email-panel")?.focus(), 0);
    });

    surface.querySelector("[data-identity-panel-close]")?.addEventListener("click", () => {
      panelOpen = false;
      render(latestState);
    });

    surface.querySelector("[data-identity-panel-backdrop]")?.addEventListener("click", (event) => {
      if (event.target === event.currentTarget) {
        panelOpen = false;
        render(latestState);
      }
    });

    const actions = surface.querySelector(".identity-panel-actions");
    if (!actions) {
      scheduleCooldownTick();
      return;
    }

    if (isSignedIn) {
      const signOutButton = document.createElement("button");
      signOutButton.type = "button";
      signOutButton.className = "identity-panel-primary-button";
      signOutButton.textContent = "Sign out";
      signOutButton.addEventListener("click", () => authService.signOut());
      actions.append(signOutButton);
      scheduleCooldownTick();
      return;
    }

    const form = document.createElement("form");
    form.className = "identity-panel-form";
    form.innerHTML = `
      <label for="supabase-auth-email-panel">Email address</label>
      <input id="supabase-auth-email-panel" type="email" inputmode="email" autocomplete="email" placeholder="you@example.com" value="${escapeHtml(emailDraft)}" ${canAttemptSignIn ? "" : "disabled"}>
      <button type="submit" class="identity-panel-primary-button" ${canSubmit ? "" : "disabled"}>${cooldownSeconds > 0 ? `Wait ${cooldownSeconds}s` : "Email magic link"}</button>
    `;
    form.querySelector("input")?.addEventListener("input", (event) => {
      emailDraft = event.target.value;
    });
    form.addEventListener("submit", (event) => {
      event.preventDefault();
      const email = form.querySelector("input")?.value || "";
      emailDraft = email;
      if (!canSubmit) return;
      cooldownUntil = Date.now() + 20000;
      authSignIn.call(authService, email);
      render({ ...latestState, status: "sending", message: "Sending Supabase magic link…" });
    });
    actions.append(form);
    scheduleCooldownTick();
  }

  function onKeydown(event) {
    if (event.key === "Escape" && panelOpen) {
      panelOpen = false;
      render(latestState);
    }
  }

  function start() {
    window.addEventListener("keydown", onKeydown);
    authService.subscribe(render);
    authService.start();
  }

  return { start };
}
