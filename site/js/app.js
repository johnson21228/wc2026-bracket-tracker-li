import { createBracketModel } from "./mvc/model.js";
import { createBracketView } from "./mvc/view.js";
import { createBracketController } from "./mvc/controller.js";
import { createSupabaseAuthService } from "./services/SupabaseAuthService.js";
import { createSupabaseIdentitySurface } from "./identity/SupabaseIdentitySurface.js";


function setupRulesPanel(root) {
  const openButton = root.querySelector("[data-rules-panel-open]");
  const panel = root.querySelector("[data-rules-panel]");
  if (!openButton || !panel) return;

  const closeButton = panel.querySelector("[data-rules-panel-close]");
  const activeLabel = panel.querySelector("[data-rules-panel-active-label]");
  const sections = [...panel.querySelectorAll("[data-rules-panel-section]")];

  function selectedGameValue() {
    const selected = root.querySelector(".dev-game-selector-option input:checked");
    return selected?.value || "game-1";
  }

  function syncRulesPanel() {
    const active = selectedGameValue();
    sections.forEach((section) => {
      section.hidden = section.dataset.rulesPanelSection !== active;
    });
    if (activeLabel) {
      activeLabel.textContent = active === "game-1" ? "Showing Game 1 rules" : "Showing Game 2 rules";
    }
  }

  function openRulesPanel() {
    syncRulesPanel();
    panel.hidden = false;
    closeButton?.focus();
  }

  function closeRulesPanel() {
    panel.hidden = true;
    openButton.focus();
  }

  openButton.addEventListener("click", openRulesPanel);
  closeButton?.addEventListener("click", closeRulesPanel);

  panel.addEventListener("click", (event) => {
    if (event.target === panel) closeRulesPanel();
  });

  root.addEventListener("change", (event) => {
    if (event.target instanceof HTMLInputElement && event.target.closest(".dev-game-selector-option")) {
      syncRulesPanel();
    }
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && !panel.hidden) closeRulesPanel();
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

  setupRulesPanel(root);
  const model = await createBracketModel();
  const view = createBracketView(root);
  setupActiveGameBackground(root);
  const controller = createBracketController({ model, view });
  const authService = createSupabaseAuthService();
  const identitySurface = createSupabaseIdentitySurface({ root, authService });
  identitySurface.start();
  controller.start();
}

main().catch((error) => {
  console.error("WC2026 MVC runtime failed to start", error);
  const root = document.querySelector("[data-wc2026-app]");
  if (root) {
    root.innerHTML = `<main class="app-error"><h1>Site failed to start</h1><pre>${String(error?.message || error)}</pre></main>`;
  }
});
