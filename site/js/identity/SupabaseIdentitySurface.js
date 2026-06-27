
function identityIconSvg(kind) {
  if (kind === "person-add") {
    return `
      <svg class="identity-icon-svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false">
        <path d="M15 19.5v-1.2c0-2.1-2.2-3.8-5-3.8s-5 1.7-5 3.8v1.2" />
        <circle cx="10" cy="8" r="3.3" />
        <path d="M18 8v6" />
        <path d="M15 11h6" />
      </svg>
    `;
  }
  if (kind === "person-check") {
    return `
      <svg class="identity-icon-svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false">
        <path d="M15 19.5v-1.2c0-2.1-2.2-3.8-5-3.8s-5 1.7-5 3.8v1.2" />
        <circle cx="10" cy="8" r="3.3" />
        <path d="M15.5 12.2l2 2 4-4" />
      </svg>
    `;
  }
  return "";
}

const IDENTITY_ICON_BUTTON_ACCESSIBILITY_TOKENS = [
  'aria-label="Join Bracketeering"',
  'title="Join Bracketeering"',
  'aria-label="Profile"',
  'title="Profile"',
];

function decorateIdentityRoundIconButtons(surface) {
  const buttons = Array.from(surface?.querySelectorAll?.("button") || []);
  for (const button of buttons) {
    const visibleText = (button.textContent || "").trim().toLowerCase();
    const classText = String(button.className || "");

    const isJoinButton =
      visibleText === "join" ||
      visibleText.includes("join") ||
      classText.includes("join-button") ||
      classText.includes("account-save-action");

    const isProfileButton =
      visibleText === "profile" ||
      visibleText.includes("profile") ||
      classText.includes("profile-control") ||
      classText.includes("profile-button");

    if (isJoinButton) {
      button.classList.add("identity-icon-button");
      button.setAttribute("aria-label", "Join Bracketeering");
      button.setAttribute("title", "Join Bracketeering");
      button.innerHTML = identityIconSvg("person-add");
    }

    if (isProfileButton) {
      button.classList.add("identity-icon-button");
      button.setAttribute("aria-label", "Profile");
      button.setAttribute("title", "Profile");
      button.innerHTML = identityIconSvg("person-check");
    }
  }
}

export function createSupabaseIdentitySurface({ root, authService, profileStore = null }) {
  const surface = root?.querySelector?.("[data-supabase-identity-surface]");
  if (surface) {
    const identityRoundIconObserver = new MutationObserver(() => decorateIdentityRoundIconButtons(surface));
    identityRoundIconObserver.observe(surface, { childList: true, subtree: true });
    decorateIdentityRoundIconButtons(surface);
  }

  if (!surface || !authService) {
    return { start() {} };
  }

  const authSignIn = authService?.signInWithMagicLink || authService?.signInWithEmail;
  const authGoogleSignIn = authService?.signInWithGoogle;
  let panelOpen = false;
  let emailDraft = "";
  let latestState = authService?.currentState?.() || {
    configured: false,
    status: "not-configured",
    user: null,
    message: "Join is not available yet.",
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
    if (state.status === "signed-in") return "Joined";
    if (state.status === "checking") return "Checking join";
    if (state.status === "sending") return "Joining…";
    if (state.status === "link-sent") return "Check email";
    if (state.status === "error") return "Join needs attention";
    return "Join";
  }

  function persistenceLabel(state) {
    if (state.status === "not-configured") return "Join unavailable";
    return state.status === "signed-in" ? `Joined as ${profileDisplayName() || "Player"}` : "Join to enter standings.";
  }

  function panelMessage(state) {
    if (state.status === "signed-in") {
      return "Edit the public player name shown in standings.";
    }
    return state.message || "Join the game to keep picks live and enter standings.";
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
    return "Profile";
  }

  function signedInUserId(state) {
    return state.user?.id || "";
  }

  function profileDisplayName() {
    return profileState.profile?.display_name || "";
  }

  function profileMessageHtml() {
    if (!profileStore) {
      return `<p>Your public player name is shown in standings.</p>`;
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
    const canAttemptGoogleSignIn = Boolean(state.configured && !isSignedIn && authGoogleSignIn);
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
              <p class="identity-kicker">Bracketeering player</p>
              <h2 id="supabase-identity-panel-title">${isSignedIn ? "Profile" : "Join Bracketeering Hub"}</h2>
            </div>
            <button type="button" class="identity-panel-close" data-identity-panel-close aria-label="Close player panel">×</button>
          </div>
          <p class="identity-panel-intro">${isSignedIn ? "Edit your public player name." : "Join to keep picks live and enter standings. You can still explore the board before joining. Continue with Google, email yourself a sign-in link, or keep playing locally on this browser."}</p>
          <p class="identity-local-note">${isSignedIn ? "Your picks are live." : "Before joining, this board is temporary browser play. No account needed for local play. Your picks are saved only on this browser until you join."}</p>
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
        <p><strong>Joined status:</strong> Joined</p>
        <p>Your public player name is what other players see.</p>
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
            Update player name
          </button>
          ${profileMessageHtml()}
        </div>
        <p><strong>Picks:</strong> live after joining.</p>
      `;
      actions.append(signedInDetails);

      actions.querySelector("[data-profile-save]")?.addEventListener("click", async () => {
        const userId = signedInUserId(latestState);
        const displayName = actions.querySelector("#identity-public-player-name")?.value || "";

        if (!profileStore) {
          profileState = { status: "error", profile: null, message: "Player profile is not available yet." };
          render(latestState);
          return;
        }

        profileState = { ...profileState, status: "saving", message: "Updating public player name…" };
        render(latestState);

        const { profile, error } = await profileStore.saveProfile({ userId, displayName });
        if (error) {
          profileState = { status: "error", profile: profileState.profile, message: `Player name update failed: ${error.message || String(error)}` };
        } else {
          profileState = { status: "saved", profile, message: "Player name updated." };
        }
        render(latestState);
      });

      const signOutButton = document.createElement("button");
      signOutButton.type = "button";
      signOutButton.className = "identity-panel-primary-button";
      signOutButton.textContent = "Leave joined session";
      signOutButton.addEventListener("click", () => authService.signOut());
      actions.append(signOutButton);

      scheduleCooldownTick();
      loadProfileForState(latestState);
      return;
    }


    const googleButton = document.createElement("button");
    googleButton.type = "button";
    googleButton.className = "identity-panel-primary-button";
    googleButton.textContent = "Continue with Google";
    googleButton.disabled = !canAttemptGoogleSignIn || isBusy;
    googleButton.dataset.googleSignIn = "true";
    googleButton.addEventListener("click", () => {
      if (!canAttemptGoogleSignIn || isBusy) return;
      authGoogleSignIn.call(authService);
    });
    actions.append(googleButton);

    const emailDivider = document.createElement("p");
    emailDivider.className = "identity-panel-divider";
    emailDivider.textContent = "or";
    actions.append(emailDivider);

    const form = document.createElement("form");
    form.className = "identity-panel-form";
    form.innerHTML = `
      <label for="supabase-auth-email-panel">Email address</label>
      <input id="supabase-auth-email-panel" type="email" inputmode="email" autocomplete="email" placeholder="you@example.com" value="${escapeHtml(emailDraft)}" ${canAttemptSignIn ? "" : "disabled"}>
      <button type="submit" class="identity-panel-primary-button" ${canSubmit ? "" : "disabled"}>${cooldownSeconds > 0 ? `Wait ${cooldownSeconds}s` : "Email me a sign-in link"}</button>
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
      render({ ...latestState, status: "sending", message: "Sending join link…" });
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
