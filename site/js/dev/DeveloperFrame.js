function createDeveloperFrame({ boardPlane }) {
  const frame = document.createElement("section");
  frame.className = "developer-frame";
  frame.dataset.module = "DeveloperFrame";
  frame.setAttribute("aria-label", "Developer controls");

  const title = document.createElement("h2");
  title.textContent = "Developer frame";

  const controlRow = document.createElement("label");
  controlRow.className = "developer-control-row";

  const toggle = document.createElement("input");
  toggle.type = "checkbox";
  toggle.checked = true;
  toggle.dataset.control = "toggle-pub-background";

  const label = document.createElement("span");
  label.textContent = "Show pub image";

  toggle.addEventListener("change", () => {
    if (!boardPlane) return;
    boardPlane.dataset.showPubBackground = toggle.checked ? "true" : "false";
  });

  controlRow.append(toggle, label);
  frame.append(title, controlRow);

  return frame;
}

export { createDeveloperFrame };
