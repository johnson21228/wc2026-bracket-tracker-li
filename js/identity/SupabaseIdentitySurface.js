export function createSupabaseIdentitySurface({ root, authService, profileStore = null }) {
  const surface = root?.querySelector?.("[data-supabase-identity-surface]");
  if (!surface || !authService) {
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
  let profileState = { status: "idle", profile: null, message: "" };
  let profileLoadUserId = "";

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
    if (state.status === "signed-in") return "Signed in";
    if (state.status === "checking") return "Checking sign-in";
    if (state.status === "sending") return "Sending link";
    if (state.status === "link-sent") return "Check email";
    if (state.status === "error") return "Sign-in needs attention";
    return "Sign in to save";
  }

  function persistenceLabel(state) {
    if (state.status === "not-configured") return "Local bracket · Supabase Auth not configured";
    return "Local bracket for now";
  }

  function panelMessage(state) {
    if (state.status === "signed-in") {
      return "This email is used for login. It is not your public player name.";
    }
    return state.message || "Sign in is identity-only for now. Bracket picks remain saved locally in this browser.";
  }

  function accountEmail(state) {
    return state.user?.email || "";
  }

  function compactIdentityTitle(state) {
    if (state.status !== "signed-in") {
      return statusLabel(state);
    }

    const publicName = profileDisplayName();
    const fallback = accountEmail(state) || "signed-in player";
    return `Signed in as: ${publicName || fallback}`;
  }

  function signedInUserId(state) {
    return state.user?.id || "";
  }

  function profileDisplayName() {
    return profileState.profile?.display_name || "";
  }

  function profileMessageHtml() {
    if (!profileStore) {
      return `<p>Your public player name will be stored in a Supabase-backed profile.</p>`;
    }
    if (profileState.status === "loading") {
      return `<p>Loading your public player name…</p>`;
    }
    if (profileState.status === "saving") {
      return `<p>Saving public player name…</p>`;
    }
    if (profileState.status === "error") {
      return `<p class="identity-panel-error">${escapeHtml(profileState.message || "Could not load public player name.")}</p>`;
    }
    if (profileState.status === "saved") {
      return `<p>${escapeHtml(profileState.message || "Public player name saved.")}</p>`;
    }
    if (profileDisplayName()) {
      return `<p>This is the public player name other players may see later.</p>`;
    }
    return `<p>Choose a public player name. Do not use your private email as your player name.</p>`;
  }

  async function loadProfileForState(state) {
    const userId = signedInUserId(state);
    if (!profileStore || state?.status !== "signed-in" || !userId) {
      profileLoadUserId = "";
      profileState = { status: "idle", profile: null, message: "" };
      return;
    }

    if (profileLoadUserId === userId && profileState.status !== "idle") return;

    profileLoadUserId = userId;
    profileState = { status: "loading", profile: null, message: "" };
    render(latestState);

    const { profile, error } = await profileStore.getProfile(userId);
    if (signedInUserId(latestState) !== userId) return;

    if (error) {
      profileState = { status: "error", profile: null, message: `Public player name load failed: ${error.message || String(error)}` };
    } else {
      profileState = { status: "ready", profile, message: "" };
    }
    render(latestState);
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
          <span class="identity-title">${escapeHtml(compactIdentityTitle(state))}</span>
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
      const signedInDetails = document.createElement("div");
      signedInDetails.className = "identity-panel-signed-in-details";
      signedInDetails.innerHTML = `
        <p><strong>Account:</strong> ${escapeHtml(accountEmail(state) || "Signed-in Supabase user")}</p>
        <p>This email is used for login. It is private account identity, not your public player name.</p>
        <div class="identity-panel-profile">
          <label for="identity-public-player-name"><strong>Public player name</strong></label>
          <input
            id="identity-public-player-name"
            type="text"
            maxlength="40"
            autocomplete="nickname"
            placeholder="Example: Steve"
            value="${escapeHtml(profileDisplayName())}"
            ${profileState.status === "loading" || profileState.status === "saving" ? "disabled" : ""}
          />
          <button type="button" class="identity-panel-primary-button" data-profile-save ${profileState.status === "loading" || profileState.status === "saving" ? "disabled" : ""}>
            Save player name
          </button>
          ${profileMessageHtml()}
        </div>
        <p><strong>Bracket saving:</strong> not enabled yet. This browser is still using local play.</p>
      `;
      actions.append(signedInDetails);

      actions.querySelector("[data-profile-save]")?.addEventListener("click", async () => {
        const userId = signedInUserId(latestState);
        const displayName = actions.querySelector("#identity-public-player-name")?.value || "";

        if (!profileStore) {
          profileState = { status: "error", profile: null, message: "Supabase profile store is not wired yet." };
          render(latestState);
          return;
        }

        profileState = { ...profileState, status: "saving", message: "Saving public player name…" };
        render(latestState);

        const { profile, error } = await profileStore.saveProfile({ userId, displayName });
        if (error) {
          profileState = { status: "error", profile: profileState.profile, message: `Public player name save failed: ${error.message || String(error)}` };
        } else {
          profileState = { status: "saved", profile, message: "Public player name saved." };
        }
        render(latestState);
      });

      const signOutButton = document.createElement("button");
      signOutButton.type = "button";
      signOutButton.className = "identity-panel-primary-button";
      signOutButton.textContent = "Sign out";
      signOutButton.addEventListener("click", () => authService.signOut());
      actions.append(signOutButton);

      scheduleCooldownTick();
      loadProfileForState(latestState);
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
    render(latestState);
  }

  return { start };
}
