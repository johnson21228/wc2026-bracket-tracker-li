const WORKFLOW_PANEL_TITLE = "Built with Workbench";

const WORKFLOW_PANEL_LEAD_SENTENCE =
  "This site was built in a new way.";

const WORKFLOW_PANEL_CLOSING_LINE =
  "The Bracketeering site is the product. The Workbench is the factory.";

const WORKFLOW_SECTIONS = Object.freeze([
  {
    heading: "The old way",
    paragraphs: [
      "Bracketeering could have been built the old way. A contractor, a senior full-stack developer, or a small product team could have taken the idea, written a specification, turned it into tickets, built the app, tested it, and deployed it. That path works, but it costs time, money, and coordination.",
    ],
  },
  {
    heading: "Raw AI assistance",
    paragraphs: [
      "It also could have been built with raw AI assistance. A tool like Copilot or ChatGPT can generate code quickly and produce an impressive first version. But without durable rules, source truth, tests, and memory, the project can slip. One fix can create another bug. The AI can follow the latest prompt instead of the lasting product model.",
    ],
  },
  {
    heading: "Workbench + AI",
    paragraphs: [
      "Bracketeering was built a third way.",
      "It was built with Workbench + AI.",
      "The Workbench turns plain-language intent into a disciplined production loop:",
    ],
    steps: [
      "Intent becomes a card.",
      "The card changes the artifact.",
      "The artifact is verified.",
      "The verifier protects the rule.",
      "The result is captured back into project memory.",
      "The next session starts from source truth.",
    ],
    after: [
      "For Bracketeering, the artifact was software: a real browser-based gameboard with picks, saved brackets, player standings, Supabase login, shared visibility rules, private-write permissions, publishing, verification, and repair loops.",
    ],
  },
  {
    heading: "Workbench thesis",
    paragraphs: [
      "AI can generate output, but generation is not enough.",
      "The Workbench is the missing layer between human intent and durable change. It gives AI a governed place to work: source truth, rules, tests, memory, verification, and product judgment.",
      "And Workbench is not just for coding. It is for any workflow where AI can help produce, revise, verify, and preserve artifacts: software, documents, designs, plans, research, operating procedures, business systems, learning materials, or creative work.",
      "The human stays in the role of owner, architect, tester, and judge. The AI helps execute. The Workbench keeps the system from drifting.",
      "The point is not that Bracketeering could not have been built another way.",
      "The point is that it was built in a new way.",
    ],
  },
]);

function paragraphsHtml(paragraphs = []) {
  return paragraphs.map((paragraph) => `<p>${paragraph}</p>`).join("");
}

function stepsHtml(steps = []) {
  if (!steps.length) return "";
  return `
    <ol class="workflow-panel-copy-list">
      ${steps.map((step) => `<li>${step}</li>`).join("")}
    </ol>
  `;
}

function sectionHtml(section) {
  return `
    <section class="workflow-panel-section workflow-panel-copy">
      <h3 class="workflow-panel-subheading">${section.heading}</h3>
      ${paragraphsHtml(section.paragraphs)}
      ${stepsHtml(section.steps)}
      ${paragraphsHtml(section.after)}
    </section>
  `;
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
        <h2>${WORKFLOW_PANEL_TITLE}</h2>
        <p class="workflow-panel-core">${WORKFLOW_PANEL_LEAD_SENTENCE}</p>
      </section>
      ${WORKFLOW_SECTIONS.map(sectionHtml).join("")}
      <section class="workflow-panel-section workflow-panel-copy">
        <p class="workflow-panel-closing">${WORKFLOW_PANEL_CLOSING_LINE}</p>
      </section>
      <figure class="workflow-panel-figure">
        <img
          src="assets/visuals/bracketeering_workflow/bracketeering_workflow_infographic.jpeg"
          alt="Bracketeering workflow infographic showing one chat, two roles, terminal verification, and durable product memory."
        />
        <figcaption>One ChatGPT conversation, two roles, one Bracketeering Workbench loop.</figcaption>
      </figure>
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
