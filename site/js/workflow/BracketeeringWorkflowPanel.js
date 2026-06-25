const WORKFLOW_PANEL_TITLE = "Built with Workbench";

const STORY_SECTIONS = Object.freeze([
  {
    heading: "The old way",
    paragraphs: [
      "This site was built in a new way.",
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

const WORKBENCH_PARAGRAPHS = Object.freeze([
  "Most AI tools are optimized for immediate output. They answer, draft, summarize, and generate.",
  "But much valuable human work does not begin as a clean prompt or end as a clean answer.",
  "It begins as a half-seen pattern, a fragment, a drawing, a sentence, a source excerpt, a question, or a recurring intuition.",
  "The Workbench preserves the middle: the movement from source to observation to mark to phrase to question to reflection to judgment.",
  "That makes Workbench larger than coding.",
  "Workbench is for any workflow where AI can help produce, revise, verify, and preserve artifacts: software, documents, designs, plans, research, operating procedures, business systems, learning materials, or creative work.",
  "AI is a companion, not the authority.",
  "The human stays in the role of owner, architect, tester, and judge. The AI helps execute. The Workbench keeps the system from drifting.",
  "A founder building with AI does not only need faster generation.",
  "They need continuity.",
  "The Workbench turns valuable language into durable infrastructure: customer insight, product judgment, source evidence, decision history, pitch language, implementation rules, and next action.",
  "The app implementation is not the memory.",
  "The Workbench is the memory.",
]);

const WORKBENCH_CLOSING_LINES = Object.freeze([
  "Prompts are the interface.",
  "Continuity is the product.",
  "Capture Back is the protocol.",
  "Language Infrastructure is the compounding business win.",
]);

const STORY_CLOSING_LINE =
  "The Bracketeering site is the product. The Workbench is the factory.";

const C64_WORKBENCH_LOOP_IMAGE_SRC = "./assets/workflow/c64_workbench_stage0_learning_loop.jpeg";
const C64_WORKBENCH_LOOP_TITLE = "The C64 Workbench Loop";
const C64_WORKBENCH_LOOP_PARAGRAPHS = Object.freeze([
  "This picture shows the workflow behind the Commodore 64 Learning Lab. The important idea is that the project is not just a folder of code examples. It is a repeatable learning loop.",
  "The loop starts in a conversation. The conversation is used to think through what the next small learning step should be: a C64 concept, a tiny program, an expected behavior, and a way to verify that the work was actually captured. In this project, the conversation is doing two jobs at once. It helps reason creatively about what to build next, and it also acts as a Workbench guide that keeps the project organized, durable, and re-enterable.",
  "From there, the work moves into the local repo. This is where the conversation becomes real project material: source code, lab folders, documentation, prompts, cards, captures, and verification scripts. The repo is the durable memory of the project. The conversation can suggest a change, but the repo is where that change becomes inspectable and reusable.",
  "Each C64 lab follows the same pattern. A lab teaches one machine idea, such as screen memory, color memory, PETSCII characters, keyboard input, sprites, or SID sound. The lab includes a small C program, an expected result, and a build target. The goal is not to make a large application all at once. The goal is to make one concept visible and runnable.",
  "The terminal is the handoff point between the idea and the machine. make verify checks that the Workbench structure still makes sense. make lab001, make lab002, and the other lab targets build real Commodore 64 .prg files using cc65. Then VICE runs those .prg files in an emulator, giving visible evidence that the lab works.",
  "That emulator evidence matters. It keeps the loop grounded. The project does not only say \u201cthis should work.\u201d It builds a real C64 program and runs it. The visible screen, color, sprite, sound, or interaction becomes the proof that the lesson is correct.",
  "Capture Back is the continuity layer. When a useful step is completed, it gets captured back into the Workbench as docs, cards, prompts, and verification rules. That means the project can be resumed later without depending on memory or on a single chat thread. The repo remembers the path.",
  "The result is a small learning system:",
  "Conversation \u2192 repo change \u2192 verification \u2192 C64 build \u2192 emulator evidence \u2192 capture back \u2192 next lab.",
  "That is the Workbench Loop. It lets a beginner-friendly C64 project grow one durable lesson at a time while preserving both the code and the reasoning behind it."
]);


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
