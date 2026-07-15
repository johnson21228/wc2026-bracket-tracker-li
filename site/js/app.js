import { createBracketModel } from "./mvc/model.js?v=remove-old-saved-board-choice-1782492355";
import { createBracketView } from "./mvc/view.js?v=remove-old-saved-board-choice-1782492355";
import { createBracketController } from "./mvc/controller.js?v=remove-old-saved-board-choice-1782492355";
import { createSupabaseAuthService } from "./services/SupabaseAuthService.js?v=remove-old-saved-board-choice-1782492355";
import { createSupabaseProfileStore } from "./services/SupabaseProfileStore.js?v=remove-old-saved-board-choice-1782492355";
import { createSupabaseIdentitySurface } from "./identity/SupabaseIdentitySurface.js?v=remove-old-saved-board-choice-1782492355";
import { createAccountSaveActionSurface } from "./identity/AccountSaveActionSurface.js?v=remove-old-saved-board-choice-1782492355";
import { setupBracketeeringWorkflowPanel } from "./workflow/BracketeeringWorkflowPanel.js?v=remove-old-saved-board-choice-1782492355";
import { createPlayerStandingsSurface } from "./standings/PlayerStandingsSurface.js?v=pool-close-fix-20260710";
import { createSupabasePlayerStandingsStore } from "./standings/SupabasePlayerStandingsStore.js?v=remove-old-saved-board-choice-1782492355";
import { createSupabaseBracketStore } from "./services/SupabaseBracketStore.js?v=remove-old-saved-board-choice-1782492355";


function setupInfoPanel(root) {
  const openButtons = Array.from(root.querySelectorAll("[data-info-panel-open], [data-rules-panel-open]"));
  const panel = root.querySelector("[data-info-panel]") || root.querySelector("[data-rules-panel]");
  if (!openButtons.length || !panel) return;

  const closeButton = panel.querySelector("[data-info-panel-close]") || panel.querySelector("[data-rules-panel-close]");
  let lastOpenButton = openButtons[0];

  function openInfoPanel(event) {
    if (event?.currentTarget instanceof HTMLElement) {
      lastOpenButton = event.currentTarget;
    }
    panel.hidden = false;
    closeButton?.focus();
  }

  function closeInfoPanel() {
    panel.hidden = true;
    lastOpenButton?.focus();
  }

  openButtons.forEach((button) => button.addEventListener("click", openInfoPanel));
  closeButton?.addEventListener("click", closeInfoPanel);

  panel.addEventListener("click", (event) => {
    if (event.target === panel) closeInfoPanel();
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && !panel.hidden) closeInfoPanel();
  });
}


const ACTIVE_GAME_BACKGROUND_IMAGES = Object.freeze({
  // Bracketeering is now a knockout-only single-game runtime. Keep the
  // legacy presentation aliases on the same accepted knockout pub calendar
  // so no boot path falls back to the old group-stage background.
  "game-1": "assets/board/pub_background_game1.jpeg",
  "game-2": "assets/board/pub_background_game1.jpeg",
});

function selectedDevGameValue(root) {
  return root.dataset.activeGame || "game-2";
}

function syncActiveGameBackground(root) {
  const background = root.querySelector(".board-background-layer");
  if (!background) return;

  const active = selectedDevGameValue(root);
  const nextBackground =
    ACTIVE_GAME_BACKGROUND_IMAGES[active] || ACTIVE_GAME_BACKGROUND_IMAGES["game-2"];

  const current = background.getAttribute("src") || "";
  if (current !== nextBackground) {
    background.setAttribute("src", nextBackground);
  }
}


function setupActiveGameBackground(root) {
  syncActiveGameBackground(root);

  root.addEventListener("change", (event) => {
    if (
      event.target instanceof HTMLInputElement &&
      event.target.closest(".dev-game-selector-option")
    ) {
      syncActiveGameBackground(root);
    }
  });
}

function ensureAccountSaveMount(appRoot) {
  if (!appRoot) return null;
  let mount = appRoot.querySelector("[data-account-save-action-surface]");
  if (!mount) {
    mount = document.createElement("div");
    mount.className = "account-save-action-surface";
    mount.setAttribute("data-account-save-action-surface", "");
    appRoot.prepend(mount);
  }
  return mount;
}

async function main() {
  const root = document.querySelector("[data-wc2026-app]");
  if (!root) {
    throw new Error("Missing [data-wc2026-app] site root.");
  }

  console.info("[WC2026 startup] root found");
  setupInfoPanel(root);
  setupBracketeeringWorkflowPanel(root);
  const urlParams = new URLSearchParams(window.location.search);
  const adminOfficialEditor = urlParams.get("adminOfficialEditor") === "1" || urlParams.get("adminOfficial") === "1";
  const adminOfficialR32Editor = adminOfficialEditor || urlParams.get("adminOfficialR32Editor") === "1";

  // Current LI: Bracketeering is one game. Legacy game-2 is only the bracket-board presentation alias.
  root.dataset.bracketeeringGame = "game1";
  root.dataset.activeGame = "game-2";
  root.dataset.adminOfficialR32Editor = adminOfficialR32Editor ? "true" : "false";
  root.querySelectorAll('.dev-game-selector-option input[value="game-1"]').forEach((input) => { input.checked = false; });
  root.querySelectorAll('.dev-game-selector-option input[value="game-2"]').forEach((input) => { input.checked = true; });
  console.info("[WC2026 startup] creating Supabase services");
  const authService = createSupabaseAuthService();
  const officialBracketStore = createSupabaseBracketStore();
  console.info("[WC2026 startup] creating model");
  const model = await createBracketModel({
    officialBracketStore,
    adminOfficialR32Editor,
    adminOfficialEditor,
  });
  console.info("[WC2026 startup] creating view");
  const view = createBracketView(root);
  setupActiveGameBackground(root);
  const controller = createBracketController({ model, view });
  const profileStore = createSupabaseProfileStore();
  const identitySurface = createSupabaseIdentitySurface({ root, authService, profileStore });
  identitySurface.start();
  const standingsStore = createSupabasePlayerStandingsStore();
  const standingsSurface = createPlayerStandingsSurface({ root, authService, profileStore, standingsStore });
  standingsSurface.start();
  createAccountSaveActionSurface({
    root: ensureAccountSaveMount(root),
    authService,
    model,
  }).start();
  console.info("[WC2026 startup] starting controller");
  controller.start();
  console.info("[WC2026 startup] controller started");
}

main().catch((error) => {
  console.error("WC2026 MVC runtime failed to start", error);
  const root = document.querySelector("[data-wc2026-app]");
  if (root) {
    root.innerHTML = `<main class="app-error"><h1>Site failed to start</h1><pre>${String(error?.message || error)}</pre></main>`;
  }
});


if (new URLSearchParams(window.location.search).get("devSupabaseBracketSmoke") === "1") {
  const smokeModuleUrl = new URL("js/dev/SupabaseBracketStoreSmokeTest.js", document.baseURI).href;
  import(smokeModuleUrl)
    .then(({ installSupabaseBracketStoreSmokeTest }) => {
      installSupabaseBracketStoreSmokeTest();
    })
    .catch((error) => {
      console.error("[SupabaseBracketStoreSmokeTest] module load failed", error);
    });
}


