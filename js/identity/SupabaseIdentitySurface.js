export function createSupabaseIdentitySurface({ root, authService }) {
  const surface = root.querySelector("[data-supabase-identity-surface]");
  if (!surface) {
    return { start() {} };
  }

  if (surface.dataset.authDisabled === "true") {
    surface.innerHTML = `
      <div class="identity-card" data-auth-state="disabled">
        <div class="identity-summary">
          <span class="identity-kicker">Player</span>
          <strong class="identity-title">Local bracket active</strong>
          <span class="identity-detail">Sign-in paused</span>
        </div>
        <p class="identity-message" aria-live="polite">Local bracket remains active.</p>
      </div>
    `;
    return { start() {} };
  }

  let latestState = authService?.currentState?.() || {
    configured: false,
    status: "not-configured",
    user: null,
    message: "Supabase Auth is not configured yet.",
  };

  function statusLabel(state) {
    if (state.status === "signed-in") return state.user?.label || "Signed in";
    if (state.status === "checking") return "Checking sign-in";
    if (state.status === "sending") return "Sending link";
    if (state.status === "link-sent") return "Check email";
    return "Sign in to save";
  }

  function persistenceLabel(state) {
    if (state.status === "signed-in") return "Local bracket for now";
    if (state.status === "not-configured") return "Local bracket · Supabase Auth not configured";
    return "Local bracket";
  }

  function render(state = latestState) {
    latestState = state;
    const isSignedIn = state.status === "signed-in";
    const isBusy = state.status === "checking" || state.status === "sending";
    const canAttemptSignIn = state.configured && !isSignedIn;

    surface.innerHTML = `
      <div class="identity-card" data-auth-state="${state.status}">
        <div class="identity-summary">
          <span class="identity-kicker">Player</span>
          <strong class="identity-title">${statusLabel(state)}</strong>
          <span class="identity-detail">${persistenceLabel(state)}</span>
        </div>
        <div class="identity-actions"></div>
        <p class="identity-message" aria-live="polite">${state.message || ""}</p>
      </div>
    `;

    const actions = surface.querySelector(".identity-actions");
    if (!actions) return;

    if (isSignedIn) {
      const signOutButton = document.createElement("button");
      signOutButton.type = "button";
      signOutButton.className = "identity-button";
      signOutButton.textContent = "Sign out";
      signOutButton.addEventListener("click", () => authService.signOut());
      actions.append(signOutButton);
      return;
    }

    const form = document.createElement("form");
    form.className = "identity-signin-form";
    form.innerHTML = `
      <label class="visually-hidden" for="supabase-auth-email">Email address</label>
      <input id="supabase-auth-email" type="email" inputmode="email" autocomplete="email" placeholder="email" ${canAttemptSignIn ? "" : "disabled"}>
      <button type="submit" class="identity-button" ${canAttemptSignIn && !isBusy ? "" : "disabled"}>Sign in</button>
    `;
    form.addEventListener("submit", (event) => {
      event.preventDefault();
      const email = form.querySelector("input")?.value || "";
      authService.signInWithEmail(email);
    });
    actions.append(form);
  }

  function start() {
    authService.subscribe(render);
    authService.start();
  }

  return { start };
}
