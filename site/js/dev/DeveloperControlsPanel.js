function createCheckboxControl({ id, label, checked, disabled, stateText, onChange }) {
  const row = document.createElement("div");
  row.className = "dev-control-row";

  const labelElement = document.createElement("label");
  labelElement.setAttribute("for", id);

  const input = document.createElement("input");
  input.type = "checkbox";
  input.id = id;
  input.checked = Boolean(checked);
  input.disabled = Boolean(disabled);
  input.addEventListener("change", () => onChange?.(input.checked));

  const labelText = document.createElement("span");
  labelText.textContent = label;

  labelElement.append(input, labelText);

  const state = document.createElement("span");
  state.className = "dev-control-state";
  state.textContent = stateText;

  row.append(labelElement, state);
  return row;
}

function createResourceList(truthResources) {
  const list = document.createElement("dl");
  list.className = "dev-resource-list";

  const rows = [
    ["Background truth", truthResources.backgroundImage],
    ["Legacy source", truthResources.legacyDiscoveredBackgroundImage],
    ["SVG definition", truthResources.svgGameboardDefinition],
    ["Geometry manifest", truthResources.geometryManifest],
  ];

  for (const [term, value] of rows) {
    const row = document.createElement("div");
    row.className = "dev-resource-row";

    const dt = document.createElement("dt");
    dt.textContent = term;

    const dd = document.createElement("dd");
    dd.textContent = value || "not configured";

    row.append(dt, dd);
    list.appendChild(row);
  }

  return list;
}

function collectDiagnostics({ appMount, boardPlane }) {
  return {
    appMountPresent: Boolean(appMount),
    boardPlanePresent: Boolean(boardPlane),
    backgroundLayerPresent: Boolean(boardPlane?.querySelector("[data-layer-role='bottom-background-authority']")),
    backgroundVisible: boardPlane?.dataset.devBackgroundVisible !== "false",
    svgLayerPresent: Boolean(boardPlane?.querySelector("[data-layer-role='svg-gameboard-definition']")),
    pickIdsLayerPresent: Boolean(boardPlane?.querySelector("[data-layer-role='pick-id-debug']")),
  };
}

function renderDiagnostics(target, diagnostics) {
  target.textContent = JSON.stringify(diagnostics, null, 2);
}

function createDeveloperControlsPanel({ appMount, boardPlane, truthResources }) {
  const panel = document.createElement("section");
  panel.className = "dev-controls-panel";
  panel.dataset.module = "DeveloperControlsPanel";
  panel.setAttribute("aria-label", "Developer controls");

  const header = document.createElement("header");
  header.className = "dev-controls-header";

  const titleWrap = document.createElement("div");
  const title = document.createElement("h2");
  title.className = "dev-controls-title";
  title.textContent = "Developer controls";

  const subtitle = document.createElement("p");
  subtitle.className = "dev-controls-subtitle";
  subtitle.textContent = "Layer toggles and module diagnostics for the clean rebuild.";

  titleWrap.append(title, subtitle);

  const status = document.createElement("span");
  status.className = "dev-status-pill";
  status.textContent = boardPlane ? "board shell rendered" : "board shell missing";

  header.append(titleWrap, status);

  const grid = document.createElement("div");
  grid.className = "dev-controls-grid";

  const controlsSection = document.createElement("section");
  controlsSection.className = "dev-controls-section";
  const controlsTitle = document.createElement("h3");
  controlsTitle.textContent = "Layer controls";

  const diagnosticsBlock = document.createElement("pre");
  diagnosticsBlock.className = "dev-diagnostics";

  const refreshDiagnostics = () => {
    renderDiagnostics(diagnosticsBlock, collectDiagnostics({ appMount, boardPlane }));
  };

  const backgroundControl = createCheckboxControl({
    id: "dev-toggle-background",
    label: "Show background",
    checked: true,
    disabled: false,
    stateText: "active",
    onChange: (isVisible) => {
      if (boardPlane) {
        boardPlane.dataset.devBackgroundVisible = String(Boolean(isVisible));
      }
      refreshDiagnostics();
    },
  });

  const svgControl = createCheckboxControl({
    id: "dev-toggle-svg",
    label: "Show gameboard SVG",
    checked: false,
    disabled: true,
    stateText: "pending next layer",
  });

  const pickIdsControl = createCheckboxControl({
    id: "dev-toggle-pick-ids",
    label: "Show pick IDs",
    checked: false,
    disabled: true,
    stateText: "pending pick layer",
  });

  controlsSection.append(controlsTitle, backgroundControl, svgControl, pickIdsControl, diagnosticsBlock);

  const resourcesSection = document.createElement("section");
  resourcesSection.className = "dev-controls-section";
  const resourcesTitle = document.createElement("h3");
  resourcesTitle.textContent = "Board truth resources";
  resourcesSection.append(resourcesTitle, createResourceList(truthResources));

  grid.append(controlsSection, resourcesSection);
  panel.append(header, grid);

  refreshDiagnostics();

  return panel;
}

export { createDeveloperControlsPanel, collectDiagnostics };
