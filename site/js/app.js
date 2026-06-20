import { createBracketModel } from "./mvc/model.js";
import { createBracketView } from "./mvc/view.js";
import { createBracketController } from "./mvc/controller.js";
import { createSupabaseAuthService } from "./services/SupabaseAuthService.js";
import { createSupabaseIdentitySurface } from "./identity/SupabaseIdentitySurface.js";

async function main() {
  const root = document.querySelector("[data-wc2026-app]");
  if (!root) {
    throw new Error("Missing [data-wc2026-app] site root.");
  }

  const model = await createBracketModel();
  const view = createBracketView(root);
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
