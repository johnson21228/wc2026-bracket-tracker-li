const WORKFLOW_PANEL_CORE_SENTENCE =
  "The game evolves because the Workbench keeps code, intent, and verification aligned.";

const WORKFLOW_PITCH_PARAGRAPHS = Object.freeze([
  "Bracketeering is not just a World Cup bracket site. It is a live example of a Workbench-driven product build: one conversation, one repo, one evolving game system, and a verification loop that turns decisions into durable product memory.",
  "The Bracketeering workflow uses the Workbench as the product owner and continuity layer. The human sets direction, approves changes, and decides what becomes durable. The Intelligence Interface proposes implementation steps, edits the product surface, captures decisions, and updates verifiers. The terminal executes the durable part of the loop: code changes, data updates, verification, packaging, commits, pushes, and GitHub Pages publication.",
  "What makes this workflow different is that the repo does not merely collect code. It collects intent. Every meaningful product decision becomes language infrastructure: cards, captures, docs, rules, prompts, data contracts, and verification scripts. Those scripts become executable memory. When the product changes, the Workbench does not just patch code; it refines the rules that keep the product aligned.",
  "The Supabase profile step shows the loop clearly. At first, the repo blocked all Supabase writes because bracket persistence was not ready. Once public player names became real, the invariant evolved: profile writes were allowed through SupabaseProfileStore, while remote bracket writes remained blocked until the future bracket store. The verifiers caught the stale rule, and the Workbench updated the executable LI to match the new architecture.",
  "That is the Bracketeering advantage: product intent, implementation, verification, and continuity move together.",
  "Bracketeering is a bracket game, but the deeper product is the workflow: a repeatable way to build adaptive, data-driven, multi-user tournament software without losing control of the architecture as the system grows.",
]);

function paragraphHtml() {
  return WORKFLOW_PITCH_PARAGRAPHS.map((paragraph) => `<p>${paragraph}</p>`).join("");
}

export function setupBracketeeringWorkflowPanel(root) {
  const openButtons = Array.from(root.querySelectorAll("[data-workflow-panel-open]"));
  const panel = root.querySelector("[data-workflow-panel]");
  if (!openButtons.length || !panel) return;

  const closeButton = panel.querySelector("[data-workflow-panel-close]");
  const body = panel.querySelector("[data-workflow-panel-body]");
  let lastOpenButton = openButtons[0];

  if (body && !body.dataset.workflowPanelHydrated) {
    body.dataset.workflowPanelHydrated = "true";
    body.innerHTML = `
      <section class="workflow-panel-section workflow-panel-hero">
        <p class="workflow-panel-kicker">Workbench Easter Egg</p>
        <h2>Bracketeering Workflow</h2>
        <p class="workflow-panel-core">${WORKFLOW_PANEL_CORE_SENTENCE}</p>
      </section>
      <figure class="workflow-panel-figure">
        <img
          src="assets/visuals/bracketeering_workflow/bracketeering_workflow_infographic.jpeg"
          alt="Bracketeering workflow infographic showing one chat, two roles, terminal verification, and durable product memory."
        />
        <figcaption>One ChatGPT conversation, two roles, one Bracketeering Workbench loop.</figcaption>
      </figure>
      <section class="workflow-panel-section workflow-panel-copy">
        <h3>The pitch</h3>
        ${paragraphHtml()}
      </section>
    `;
  }

  function openWorkflowPanel(event) {
    if (event?.currentTarget instanceof HTMLElement) {
      lastOpenButton = event.currentTarget;
    }
    panel.hidden = false;
    closeButton?.focus();
  }

  function closeWorkflowPanel() {
    panel.hidden = true;
    lastOpenButton?.focus();
  }

  openButtons.forEach((button) => button.addEventListener("click", openWorkflowPanel));
  closeButton?.addEventListener("click", closeWorkflowPanel);

  panel.addEventListener("click", (event) => {
    if (event.target === panel) closeWorkflowPanel();
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && !panel.hidden) closeWorkflowPanel();
  });
}
