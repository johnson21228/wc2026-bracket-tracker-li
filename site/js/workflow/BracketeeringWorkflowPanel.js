const WORKFLOW_PANEL_TITLE = "Built with Workbench";

const STORY_SECTIONS = Object.freeze([
  {
    heading: "This site was built in a new way.",
    paragraphs: [
      "Bracketeering looks like a playful World Cup bracket site. Underneath, it is also a small experiment in how software can be made with AI without letting the work drift.",
      "The old way would have been familiar: write a spec, make tickets, assign developers, build, test, fix, and deploy.",
      "Raw AI can move faster than that. A prompt can become code in minutes. But fast is not the same as trustworthy. Without memory, rules, tests, and source truth, the project can lose its shape.",
      "Bracketeering was built a third way: Workbench + AI.",
      "The AI helped make things. The Workbench kept the work coherent.",
    ],
  },
]);

const WORKBENCH_PARAGRAPHS = Object.freeze([
  "Most AI tools are built for the moment. They answer, draft, summarize, and generate.",
  "But serious work does not usually begin as a perfect prompt or end as a perfect answer.",
  "It starts as a hunch, a sketch, a source, a question, a half-finished idea, or something you keep returning to.",
  "Workbench keeps the middle from disappearing.",
  "It remembers the source truth, decisions, tests, captures, and reasons behind the work.",
  "It lets AI help without making AI the authority.",
  "A founder, learner, builder, or project keeper does not only need faster generation.",
  "They need continuity.",
]);

const WORKBENCH_CLOSING_LINES = Object.freeze([
  "Prompts are the interface.",
  "Continuity is the product.",
  "Capture Back is the protocol.",
  "Language Infrastructure is the compounding win.",
]);

const STORY_CLOSING_LINE =
  "The site is the product. The Workbench is the factory.";

const C64_WORKBENCH_LOOP_IMAGE_SRC = "./assets/workflow/c64_workbench_stage0_learning_loop.jpeg";
const C64_WORKBENCH_LOOP_TITLE = "The C64 Workbench Loop";
const C64_WORKBENCH_LOOP_PARAGRAPHS = Object.freeze([
  "The Commodore 64 makes the Workbench idea easy to see. The machine is small. The rules are visible. A tiny change has to become a real program that the emulator can prove.",
  "The loop starts with a conversation: what should this little program teach, what should it do on the screen, and how will we know it worked?",
  "Then the idea becomes a repo change: source files, lab notes, cards, captures, and verification rules.",
  "The terminal builds the program. The emulator shows the result. The evidence comes back into the Workbench.",
  "Conversation -> repo change -> verification -> C64 build -> emulator evidence -> Capture Back -> next lab.",
  "The C64 is not the point. It is just a tiny world where the rules are visible.",
]);

const PERSONAL_BEAROCRAT_TITLE = "Your Personal Bearocrat";
const PERSONAL_BEAROCRAT_SUBHEAD = "Every Inference Interface needs one.";
const PERSONAL_BEAROCRAT_PARAGRAPHS = Object.freeze([
  "The C64 shows the loop in miniature: language becomes code, code becomes machine behavior, and the emulator proves whether the claim is real.",
  "But this is not really about retro computing, or even about coding. Coding is just a concrete example.",
  "The same loop shows up across a life of learning and work. Language becomes decisions. Decisions become artifacts. Artifacts create consequences. Memory has to be kept.",
  "Your work is full of projects, sources, evidence, health observations, family context, creative drafts, repos, domains, unfinished ideas, and promises to your future self.",
  "A WB is your personal bearocrat: the continuity layer that curates authority, memory, evidence, approvals, and Capture Back so any Inference Interface can reason safely without becoming the authority.",
]);

const PERSONAL_BEAROCRAT_LOOP_LINES = Object.freeze([
  "Inference Interface asks.",
  "WB Loop curates.",
  "Registry routes.",
  "Target WB proves.",
  "Owner approves.",
  "Capture Back remembers.",
]);


function paragraphsHtml

function paragraphsHtml(paragraphs = []) {
  return paragraphs.map((paragraph) => `<p>${paragraph}</p>`).join("");
}

function stepsHtml(steps = []) {
  if (!steps.length) return "";
  return `<ol class="workflow-panel-copy-list">${steps.map((step) => `<li>${step}</li>`).join("")}</ol>`;
}

function storySectionHtml(section) {
  return `
    <section class="workflow-panel-section workflow-panel-copy">
      <h3 class="workflow-panel-subheading">${section.heading}</h3>
      ${paragraphsHtml(section.paragraphs)}
      ${stepsHtml(section.steps)}
      ${paragraphsHtml(section.after)}
    </section>
  `;
}

function tabButtonHtml({ id, label, selected }) {
  return `
    <button
      type="button"
      class="workflow-panel-tab"
      role="tab"
      id="workflow-tab-${id}"
      aria-selected="${selected ? "true" : "false"}"
      aria-controls="workflow-tabpanel-${id}"
      data-workflow-tab="${id}"
    >${label}</button>
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
      </section>

      <div class="workflow-panel-tabs" role="tablist" aria-label="Workbench Easter egg tabs">
        ${tabButtonHtml({ id: "story", label: "Story", selected: true })}
        ${tabButtonHtml({ id: "workbench", label: "Workbench", selected: false })}
        ${tabButtonHtml({ id: "c64-loop", label: "C64 Loop", selected: false })}
        ${tabButtonHtml({ id: "personal-bearocrat", label: "Personal Bearocrat", selected: false })}
      </div>

      <section
        class="workflow-panel-tabpanel"
        role="tabpanel"
        id="workflow-tabpanel-story"
        aria-labelledby="workflow-tab-story"
        data-workflow-tabpanel="story"
      >
        ${STORY_SECTIONS.map(storySectionHtml).join("")}
        <section class="workflow-panel-section workflow-panel-copy">
          <p class="workflow-panel-closing">${STORY_CLOSING_LINE}</p>
        </section>
      </section>

      <section
        class="workflow-panel-tabpanel"
        role="tabpanel"
        id="workflow-tabpanel-workbench"
        aria-labelledby="workflow-tab-workbench"
        data-workflow-tabpanel="workbench"
        hidden
      >
        <section class="workflow-panel-section workflow-panel-copy">
          <h3 class="workflow-panel-subheading">Workbench is the memory</h3>
          ${paragraphsHtml(WORKBENCH_PARAGRAPHS)}
          <p class="workflow-panel-closing">${WORKBENCH_CLOSING_LINES.join("<br>")}</p>
        </section>
      </section>

      <section
        class="workflow-panel-tabpanel"
        role="tabpanel"
        id="workflow-tabpanel-c64-loop"
        aria-labelledby="workflow-tab-c64-loop"
        data-workflow-tabpanel="c64-loop"
        hidden
      >
        <section class="workflow-panel-section workflow-panel-copy workflow-panel-c64-loop">
          <h3 class="workflow-panel-subheading">${C64_WORKBENCH_LOOP_TITLE}</h3>
          <figure class="workflow-panel-figure">
            <img
              src="${C64_WORKBENCH_LOOP_IMAGE_SRC}"
              alt="C64 Workbench Stage 0 learning loop showing conversation, terminal capture back, and VICE emulator evidence."
              loading="lazy"
            >
          </figure>
          ${paragraphsHtml(C64_WORKBENCH_LOOP_PARAGRAPHS)}
        </section>
      </section>

      <section
        class="workflow-panel-tabpanel"
        role="tabpanel"
        id="workflow-tabpanel-personal-bearocrat"
        aria-labelledby="workflow-tab-personal-bearocrat"
        data-workflow-tabpanel="personal-bearocrat"
        hidden
      >
        <section class="workflow-panel-section workflow-panel-copy workflow-panel-personal-bearocrat">
          <h3 class="workflow-panel-subheading">${PERSONAL_BEAROCRAT_TITLE}</h3>
          <p class="workflow-panel-kicker">${PERSONAL_BEAROCRAT_SUBHEAD}</p>
          ${paragraphsHtml(PERSONAL_BEAROCRAT_PARAGRAPHS)}
          <p class="workflow-panel-closing">${PERSONAL_BEAROCRAT_LOOP_LINES.join("<br>")}</p>
        </section>
      </section>

    `;
  }

  const tabButtons = Array.from(panel.querySelectorAll("[data-workflow-tab]"));
  const tabPanels = Array.from(panel.querySelectorAll("[data-workflow-tabpanel]"));

  function activateTab(tabId) {
    tabButtons.forEach((button) => {
      const selected = button.dataset.workflowTab === tabId;
      button.setAttribute("aria-selected", selected ? "true" : "false");
      button.tabIndex = selected ? 0 : -1;
    });
    tabPanels.forEach((tabPanel) => {
      tabPanel.hidden = tabPanel.dataset.workflowTabpanel !== tabId;
    });
  }

  tabButtons.forEach((button, index) => {
    button.addEventListener("click", () => activateTab(button.dataset.workflowTab));
    button.addEventListener("keydown", (event) => {
      if (!["ArrowLeft", "ArrowRight", "Home", "End"].includes(event.key)) return;
      event.preventDefault();
      const lastIndex = tabButtons.length - 1;
      let nextIndex = index;
      if (event.key === "ArrowLeft") nextIndex = index === 0 ? lastIndex : index - 1;
      if (event.key === "ArrowRight") nextIndex = index === lastIndex ? 0 : index + 1;
      if (event.key === "Home") nextIndex = 0;
      if (event.key === "End") nextIndex = lastIndex;
      const nextButton = tabButtons[nextIndex];
      activateTab(nextButton.dataset.workflowTab);
      nextButton.focus();
    });
  });

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
