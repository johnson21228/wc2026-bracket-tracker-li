export function registerFloatingSurfaceDismissal({
  root = document,
  surfaceSelectors = [],
  ignoreSelectors = [],
  active = null,
  onDismiss = null,
} = {}) {
  const surfaces = Array.isArray(surfaceSelectors) ? surfaceSelectors.filter(Boolean) : [surfaceSelectors].filter(Boolean);
  const ignores = Array.isArray(ignoreSelectors) ? ignoreSelectors.filter(Boolean) : [ignoreSelectors].filter(Boolean);

  function targetElement(event) {
    return event?.target instanceof Element ? event.target : null;
  }

  function hasOpenSurface() {
    if (typeof active === "function") return Boolean(active());
    return surfaces.some((selector) => root.querySelector(selector));
  }

  function isInsideSelector(element, selectors) {
    if (!element) return false;
    return selectors.some((selector) => Boolean(element.closest(selector)));
  }

  function dismiss(event) {
    if (typeof onDismiss === "function") onDismiss(event);
  }

  function handlePointerDown(event) {
    if (!hasOpenSurface()) return;
    const element = targetElement(event);
    if (isInsideSelector(element, surfaces)) return;
    if (isInsideSelector(element, ignores)) return;
    dismiss(event);
  }

  function handleKeyDown(event) {
    if (event.key !== "Escape") return;
    if (!hasOpenSurface()) return;
    dismiss(event);
  }

  root.addEventListener("pointerdown", handlePointerDown, true);
  root.addEventListener("keydown", handleKeyDown, true);

  return function teardownFloatingSurfaceDismissal() {
    root.removeEventListener("pointerdown", handlePointerDown, true);
    root.removeEventListener("keydown", handleKeyDown, true);
  };
}
