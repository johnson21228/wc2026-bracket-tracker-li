function makeToggle({ label, checked, controlName, onChange }) {
  const row = document.createElement("label");
  row.className = "developer-control-row";

  const toggle = document.createElement("input");
  toggle.type = "checkbox";
  toggle.checked = checked;
  toggle.dataset.control = controlName;

  const text = document.createElement("span");
  text.textContent = label;

  toggle.addEventListener("change", () => onChange(toggle.checked));

  row.append(toggle, text);
  return row;
}

function makeRangeControl({ label, value, min, max, step, controlName, onInput }) {
  const row = document.createElement("label");
  row.className = "developer-control-row developer-control-row-range";

  const text = document.createElement("span");
  text.textContent = label;

  const slider = document.createElement("input");
  slider.type = "range";
  slider.min = min;
  slider.max = max;
  slider.step = step;
  slider.value = value;
  slider.dataset.control = controlName;

  const valueText = document.createElement("span");
  valueText.className = "developer-control-value";
  valueText.textContent = value;

  slider.addEventListener("input", () => {
    valueText.textContent = slider.value;
    onInput(slider.value);
  });

  row.append(text, slider, valueText);
  return row;
}

function makeSelectControl({ label, value, controlName, options, onChange }) {
  const row = document.createElement("label");
  row.className = "developer-control-row developer-control-row-select";

  const text = document.createElement("span");
  text.textContent = label;

  const select = document.createElement("select");
  select.dataset.control = controlName;

  options.forEach((option) => {
    const item = document.createElement("option");
    item.value = option.value;
    item.textContent = option.label;
    item.selected = option.value === value;
    select.appendChild(item);
  });

  select.addEventListener("change", () => onChange(select.value));

  row.append(text, select);
  return row;
}

function cssValue(boardPlane, name, fallback) {
  return boardPlane?.style.getPropertyValue(name) || fallback;
}

function buildDeveloperPropertiesSnapshot({ boardPlane }) {
  const svgLayer = boardPlane?.querySelector(".board-svg-gameboard-layer");

  return {
    schemaVersion: 1,
    purpose: "copyable developer properties for WC2026 visual defaults",
    boardPlane: {
      dataset: {
        boardPlane: boardPlane?.dataset.boardPlane || null,
        nativeWidth: boardPlane?.dataset.nativeWidth || null,
        nativeHeight: boardPlane?.dataset.nativeHeight || null,
        showPubBackground: boardPlane?.dataset.showPubBackground || null,
        showGameboard: boardPlane?.dataset.showGameboard || null,
        showGeometryFrames: boardPlane?.dataset.showGeometryFrames || null,
        showPickIndex: boardPlane?.dataset.showPickIndex || null,
      },
      presentation: {
        gameboardOpacity: cssValue(boardPlane, "--gameboard-opacity", "0.52"),
        gameboardLineColor: cssValue(boardPlane, "--gameboard-line-color", "rgba(255, 255, 255, 0.98)"),
        gameboardLineWidth: cssValue(boardPlane, "--gameboard-line-width", "1.5"),
        gameboardLineGlow: cssValue(boardPlane, "--gameboard-line-glow", "0.05"),
      },
      truthResources: {
        svgGameboardDefinition: boardPlane?.dataset.truthSvgGameboardDefinition || null,
        geometryManifest: boardPlane?.dataset.truthGeometryManifest || null,
      },
      runtime: {
        svgState: svgLayer?.dataset.svgState || null,
      },
    },
  };
}

function createCopyablePropertiesPanel({ boardPlane }) {
  const panel = document.createElement("section");
  panel.className = "developer-properties-panel";
  panel.dataset.module = "copyable developer properties";

  const title = document.createElement("h3");
  title.textContent = "Copyable developer properties";

  const hint = document.createElement("p");
  hint.className = "developer-properties-hint";
  hint.textContent = "Tune controls, copy this JSON, and paste it back to define site defaults.";

  const textarea = document.createElement("textarea");
  textarea.className = "copyable-defaults-json";
  textarea.dataset.control = "copyable-defaults-json";
  textarea.readOnly = true;
  textarea.rows = 14;

  const buttonRow = document.createElement("div");
  buttonRow.className = "developer-properties-actions";

  const refreshButton = document.createElement("button");
  refreshButton.type = "button";
  refreshButton.textContent = "Refresh properties";

  const copyButton = document.createElement("button");
  copyButton.type = "button";
  copyButton.textContent = "Copy properties";

  const status = document.createElement("span");
  status.className = "developer-properties-copy-status";

  function refresh() {
    textarea.value = JSON.stringify(
      buildDeveloperPropertiesSnapshot({ boardPlane }),
      null,
      2
    );
  }

  refreshButton.addEventListener("click", () => {
    refresh();
    status.textContent = "refreshed";
  });

  copyButton.addEventListener("click", async () => {
    refresh();
    textarea.focus();
    textarea.select();

    try {
      await navigator.clipboard.writeText(textarea.value);
      status.textContent = "copied";
    } catch {
      document.execCommand("copy");
      status.textContent = "selected for manual copy";
    }
  });

  buttonRow.append(refreshButton, copyButton, status);
  panel.append(title, hint, textarea, buttonRow);

  panel.refreshDeveloperProperties = refresh;
  refresh();

  return panel;
}

function createDeveloperFrame({ boardPlane }) {
  const frame = document.createElement("section");
  frame.className = "developer-frame";
  frame.dataset.module = "DeveloperFrame";
  frame.setAttribute("aria-label", "Developer controls");

  const title = document.createElement("h2");
  title.textContent = "Developer frame";

  const propertiesPanel = createCopyablePropertiesPanel({ boardPlane });

  const controls = document.createElement("div");
  controls.className = "developer-controls";

  function afterChange() {
    propertiesPanel.refreshDeveloperProperties?.();
  }

  controls.append(
    makeToggle({
      label: "Show pub image",
      checked: boardPlane?.dataset.showPubBackground !== "false",
      controlName: "toggle-pub-background",
      onChange: (checked) => {
        if (boardPlane) boardPlane.dataset.showPubBackground = checked ? "true" : "false";
        afterChange();
      },
    }),
    makeToggle({
      label: "Show gameboard",
      checked: boardPlane?.dataset.showGameboard !== "false",
      controlName: "toggle-gameboard",
      onChange: (checked) => {
        if (boardPlane) boardPlane.dataset.showGameboard = checked ? "true" : "false";
        afterChange();
      },
    }),
    makeRangeControl({
      label: "Gameboard opacity",
      value: cssValue(boardPlane, "--gameboard-opacity", "0.52"),
      min: "0",
      max: "1",
      step: "0.02",
      controlName: "gameboard-opacity",
      onInput: (value) => {
        if (boardPlane) boardPlane.style.setProperty("--gameboard-opacity", value);
        afterChange();
      },
    }),
    makeSelectControl({
      label: "Gameboard line color",
      value: cssValue(boardPlane, "--gameboard-line-color", "rgba(255, 255, 255, 0.98)"),
      controlName: "gameboard-line-color",
      options: [
        { label: "Gold", value: "rgba(255, 255, 255, 0.98)" },
        { label: "White", value: "rgba(255, 255, 255, 0.98)" },
        { label: "Cyan", value: "rgba(100, 235, 255, 0.98)" },
        { label: "Green", value: "rgba(120, 255, 160, 0.98)" },
        { label: "Red", value: "rgba(255, 105, 105, 0.98)" },
      ],
      onChange: (value) => {
        if (boardPlane) boardPlane.style.setProperty("--gameboard-line-color", value);
        afterChange();
      },
    }),
    makeRangeControl({
      label: "Gameboard line width",
      value: cssValue(boardPlane, "--gameboard-line-width", "1.5"),
      min: "1",
      max: "8",
      step: "0.5",
      controlName: "gameboard-line-width",
      onInput: (value) => {
        if (boardPlane) boardPlane.style.setProperty("--gameboard-line-width", value);
        afterChange();
      },
    }),
    makeRangeControl({
      label: "Gameboard glow",
      value: cssValue(boardPlane, "--gameboard-line-glow", "0.05"),
      min: "0",
      max: "1",
      step: "0.05",
      controlName: "gameboard-line-glow",
      onInput: (value) => {
        if (boardPlane) boardPlane.style.setProperty("--gameboard-line-glow", value);
        afterChange();
      },
    })
  );

  const status = document.createElement("p");
  status.className = "developer-status";
  const svgState = boardPlane?.querySelector(".board-svg-gameboard-layer")?.dataset.svgState;
  status.textContent = `Gameboard outline: ${svgState || "unavailable"}`;

  controls.append(
    makeToggle({
      label: "Show pick identifiers",
      checked: boardPlane?.dataset.showPickIdentifiers !== "false",
      controlName: "toggle-pick-identifiers",
      onChange: (checked) => {
        if (boardPlane) boardPlane.dataset.showPickIdentifiers = checked ? "true" : "false";
        afterChange();
      },
    })
  );

  frame.append(title, controls, status, propertiesPanel);
  return frame;
}

export { buildDeveloperPropertiesSnapshot, createDeveloperFrame };
