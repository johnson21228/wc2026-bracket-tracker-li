function forceOutlineOnly(svgElement) {
  svgElement.classList.add("gameboard-outline-svg");
  svgElement.setAttribute("aria-label", "WC2026 gameboard outline");
  svgElement.setAttribute("role", "img");

  svgElement.querySelectorAll("*").forEach((node) => {
    const tagName = node.tagName.toLowerCase();

    if (tagName === "svg" || tagName === "defs" || tagName === "clipPath") {
      return;
    }

    node.setAttribute("fill", "none");
    node.style.fill = "none";

    if (!node.getAttribute("stroke") || node.getAttribute("stroke") === "none") {
      node.setAttribute("stroke", "rgba(255,255,255,0.72)");
    }

    if (!node.getAttribute("stroke-width")) {
      node.setAttribute("stroke-width", "1.5");
    }

    node.setAttribute("vector-effect", "non-scaling-stroke");
  });

  return svgElement;
}

async function createSvgGameboardLayer({ svgGameboardDefinition }) {
  const layer = document.createElement("div");
  layer.className = "board-layer board-svg-gameboard-layer";
  layer.dataset.layerRole = "gameboard-svg-outline-authority";

  try {
    const response = await fetch(svgGameboardDefinition);
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }

    const svgText = await response.text();
    const documentSvg = new DOMParser().parseFromString(svgText, "image/svg+xml");
    const svgElement = documentSvg.querySelector("svg");

    if (!svgElement) {
      throw new Error("SVG document did not contain an <svg> root");
    }

    layer.append(forceOutlineOnly(document.importNode(svgElement, true)));
    layer.dataset.svgState = "outline-ready";
  } catch (error) {
    layer.dataset.svgState = "error";
    layer.dataset.svgError = error instanceof Error ? error.message : String(error);
    layer.textContent = "Gameboard outline unavailable";
  }

  return layer;
}

export { createSvgGameboardLayer };
