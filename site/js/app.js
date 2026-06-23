import { createBracketModel } from "./mvc/model.js?v=final-four-scope-fix-1300269";
import { createBracketView } from "./mvc/view.js";
import { createBracketController } from "./mvc/controller.js";
import { createSupabaseAuthService } from "./services/SupabaseAuthService.js";
import { createSupabaseProfileStore } from "./services/SupabaseProfileStore.js";
import { SupabaseBracketStore } from "./services/SupabaseBracketStore.js";
import { createSupabaseIdentitySurface } from "./identity/SupabaseIdentitySurface.js";
import { createStorageModeSurface } from "./identity/StorageModeSurface.js";
import { setupBracketeeringWorkflowPanel } from "./workflow/BracketeeringWorkflowPanel.js";


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
  "game-1": "assets/board/pub_background_game1.jpeg",
  "game-2": "assets/board/knockout_pub_background.jpeg",
});

function selectedDevGameValue(root) {
  const selected = root.querySelector(".dev-game-selector-option input:checked");
  return selected?.value || "game-1";
}

function syncActiveGameBackground(root) {
  const background = root.querySelector(".board-background-layer");
  if (!background) return;

  const active = selectedDevGameValue(root);
  const nextBackground =
    ACTIVE_GAME_BACKGROUND_IMAGES[active] || ACTIVE_GAME_BACKGROUND_IMAGES["game-1"];

  const current = background.getAttribute("src") || "";
  if (current !== nextBackground) {
    background.setAttribute("src", nextBackground);
  }
}

function shouldUseDevSupabaseBracketStore(locationSearch = window.location.search) {
  return new URLSearchParams(locationSearch).get("devSupabaseBracketStore") === "1";
}

async function devSupabaseBracketStoreOptions(authService) {
  if (!shouldUseDevSupabaseBracketStore()) return { remoteActive: false };

  const state = await authService.start();
  const userId = state?.user?.id || "";
  if (!userId) {
    console.warn("[WC2026 SupabaseBracketStore] dev remote store requested but no signed-in user is available. Local storage remains active.");
    return { remoteActive: false };
  }

  console.info("[WC2026 SupabaseBracketStore] dev remote bracket store enabled", { userId });
  return {
    bracketStore: new SupabaseBracketStore(),
    userId,
    persistenceMode: "supabase",
    remoteActive: true,
  };
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

async function main() {
  const root = document.querySelector("[data-wc2026-app]");
  if (!root) {
    throw new Error("Missing [data-wc2026-app] site root.");
  }

  setupInfoPanel(root);
  setupBracketeeringWorkflowPanel(root);
  const authService = createSupabaseAuthService();
  const bracketStoreOptions = await devSupabaseBracketStoreOptions(authService);
  const model = await createBracketModel(bracketStoreOptions);
  const view = createBracketView(root);
  setupActiveGameBackground(root);
  const controller = createBracketController({ model, view });
  const profileStore = createSupabaseProfileStore();
  const identitySurface = createSupabaseIdentitySurface({ root, authService, profileStore });
  identitySurface.start();
  createStorageModeSurface({
    root,
    authService,
    remoteActive: bracketStoreOptions.remoteActive === true,
  }).start();
  controller.start();
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
