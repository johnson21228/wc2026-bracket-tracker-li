from pathlib import Path
import re

ROOT = Path.cwd()
HTML = ROOT / "site/game1/index.html"

if not HTML.exists():
    raise SystemExit(f"Missing {HTML}")

text = HTML.read_text(encoding="utf-8")

STYLE_MARKER = "/* WB_TOOLTIP_SIDE_PLACEMENT_START */"
SCRIPT_MARKER = "// WB_TOOLTIP_SIDE_PLACEMENT_START"

css = r"""
/* WB_TOOLTIP_SIDE_PLACEMENT_START */
.wb-side-tooltip {
  position: fixed;
  z-index: 9999;
  max-width: min(320px, calc(100vw - 32px));
  padding: 10px 12px;
  border-radius: 10px;
  border: 1px solid rgba(255,255,255,.35);
  background: rgba(16, 22, 32, .94);
  color: #fff;
  font-size: 13px;
  line-height: 1.25;
  box-shadow: 0 10px 28px rgba(0,0,0,.35);
  pointer-events: auto;
  opacity: 0;
  transform: translateY(2px);
  transition: opacity .12s ease, transform .12s ease;
}
.wb-side-tooltip[data-open="true"] {
  opacity: 1;
  transform: translateY(0);
}
.wb-side-tooltip[hidden] {
  display: none;
}
.wb-side-tooltip-title {
  font-weight: 700;
  margin-bottom: 4px;
}
.wb-side-tooltip-body {
  opacity: .92;
}
.wb-side-tooltip-action {
  display: inline-block;
  margin-top: 8px;
  padding: 6px 8px;
  border-radius: 7px;
  background: rgba(255,255,255,.12);
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.wb-tooltip-anchor-active {
  outline: 2px solid rgba(255,255,255,.42);
  outline-offset: 2px;
}
/* WB_TOOLTIP_SIDE_PLACEMENT_END */
"""

js = r"""
// WB_TOOLTIP_SIDE_PLACEMENT_START
(function(){
  const existing = document.getElementById('wb-side-tooltip');
  if (existing) return;

  const tooltip = document.createElement('div');
  tooltip.id = 'wb-side-tooltip';
  tooltip.className = 'wb-side-tooltip';
  tooltip.hidden = true;
  tooltip.setAttribute('role', 'tooltip');
  tooltip.innerHTML = '<div class="wb-side-tooltip-title"></div><div class="wb-side-tooltip-body"></div><a class="wb-side-tooltip-action" hidden></a>';
  document.body.appendChild(tooltip);

  const titleEl = tooltip.querySelector('.wb-side-tooltip-title');
  const bodyEl = tooltip.querySelector('.wb-side-tooltip-body');
  const actionEl = tooltip.querySelector('.wb-side-tooltip-action');

  let activeTarget = null;
  let closeTimer = null;
  const GAP_BRIDGE = 20;

  function escText(v){
    return String(v == null ? '' : v);
  }

  function tooltipTextFor(el){
    if (!el) return '';
    return (
      el.getAttribute('data-tooltip') ||
      el.getAttribute('data-slot-tooltip') ||
      el.getAttribute('data-tip') ||
      el.getAttribute('aria-label') ||
      el.getAttribute('title') ||
      ''
    ).trim();
  }

  function tooltipTitleFor(el){
    return (
      el.getAttribute('data-tooltip-title') ||
      el.getAttribute('data-slot') ||
      el.getAttribute('data-slot-id') ||
      el.getAttribute('data-pick-id') ||
      ''
    ).trim();
  }

  function isCandidate(el){
    if (!el || el === document.body || el === document.documentElement) return false;
    if (tooltipTextFor(el)) return true;
    if (el.matches && el.matches('[data-slot-id], [data-slot], [data-pick-id], .pick, .pick-card, .slot, .slot-card, .bracket-slot, .r32-slot, .team-tile')) {
      return true;
    }
    return false;
  }

  function findCandidate(start){
    let el = start;
    while (el && el !== document.body && el !== document.documentElement) {
      if (isCandidate(el)) return el;
      el = el.parentElement;
    }
    return null;
  }

  function viewportPlacement(targetRect, tipRect){
    const margin = 12;
    const gap = 12;

    const canRight = targetRect.right + gap + tipRect.width <= window.innerWidth - margin;
    const canLeft = targetRect.left - gap - tipRect.width >= margin;

    let left;
    if (canRight) {
      left = targetRect.right + gap;
    } else if (canLeft) {
      left = targetRect.left - gap - tipRect.width;
    } else {
      left = Math.min(
        Math.max(margin, targetRect.left),
        window.innerWidth - margin - tipRect.width
      );
    }

    let top = targetRect.top + (targetRect.height - tipRect.height) / 2;
    top = Math.min(
      Math.max(margin, top),
      window.innerHeight - margin - tipRect.height
    );

    return {left, top};
  }

  function positionTooltip(){
    if (!activeTarget || tooltip.hidden) return;

    const targetRect = activeTarget.getBoundingClientRect();

    tooltip.style.left = '0px';
    tooltip.style.top = '0px';
    tooltip.hidden = false;
    const tipRect = tooltip.getBoundingClientRect();
    const pos = viewportPlacement(targetRect, tipRect);

    tooltip.style.left = Math.round(pos.left) + 'px';
    tooltip.style.top = Math.round(pos.top) + 'px';
  }

  function openTooltip(target){
    const body = tooltipTextFor(target);
    const title = tooltipTitleFor(target);

    if (!body && !title) return;

    clearTimeout(closeTimer);

    if (activeTarget && activeTarget !== target) {
      activeTarget.classList.remove('wb-tooltip-anchor-active');
    }

    activeTarget = target;
    activeTarget.classList.add('wb-tooltip-anchor-active');

    // Prevent native title tooltip from competing with side tooltip.
    if (target.hasAttribute('title')) {
      target.setAttribute('data-wb-native-title', target.getAttribute('title') || '');
      target.removeAttribute('title');
    }

    titleEl.textContent = escText(title || 'Pick detail');
    bodyEl.textContent = escText(body || title || '');

    const actionHref = target.getAttribute('data-tooltip-action-href');
    const actionLabel = target.getAttribute('data-tooltip-action-label') || 'Open';
    if (actionHref) {
      actionEl.hidden = false;
      actionEl.textContent = actionLabel;
      actionEl.setAttribute('href', actionHref);
    } else {
      actionEl.hidden = true;
      actionEl.removeAttribute('href');
    }

    tooltip.hidden = false;
    tooltip.dataset.open = 'true';
    positionTooltip();
  }

  function closeTooltipSoon(){
    clearTimeout(closeTimer);
    closeTimer = setTimeout(closeTooltip, 160);
  }

  function closeTooltip(){
    clearTimeout(closeTimer);

    if (activeTarget) {
      activeTarget.classList.remove('wb-tooltip-anchor-active');
      if (activeTarget.hasAttribute('data-wb-native-title')) {
        activeTarget.setAttribute('title', activeTarget.getAttribute('data-wb-native-title') || '');
        activeTarget.removeAttribute('data-wb-native-title');
      }
    }

    activeTarget = null;
    tooltip.dataset.open = 'false';
    tooltip.hidden = true;
  }

  function rectWithBridge(a, b){
    const left = Math.min(a.left, b.left) - GAP_BRIDGE;
    const right = Math.max(a.right, b.right) + GAP_BRIDGE;
    const top = Math.min(a.top, b.top) - GAP_BRIDGE;
    const bottom = Math.max(a.bottom, b.bottom) + GAP_BRIDGE;
    return {left, right, top, bottom};
  }

  function pointInside(rect, x, y){
    return x >= rect.left && x <= rect.right && y >= rect.top && y <= rect.bottom;
  }

  document.addEventListener('pointerover', function(e){
    const target = findCandidate(e.target);
    if (target) openTooltip(target);
  }, true);

  document.addEventListener('focusin', function(e){
    const target = findCandidate(e.target);
    if (target) openTooltip(target);
  }, true);

  document.addEventListener('pointermove', function(e){
    if (!activeTarget || tooltip.hidden) return;

    const targetRect = activeTarget.getBoundingClientRect();
    const tipRect = tooltip.getBoundingClientRect();
    const activeRect = rectWithBridge(targetRect, tipRect);

    if (pointInside(activeRect, e.clientX, e.clientY)) {
      clearTimeout(closeTimer);
    } else {
      closeTooltipSoon();
    }
  }, true);

  document.addEventListener('pointerdown', function(e){
    if (!activeTarget || tooltip.hidden) return;
    if (tooltip.contains(e.target) || activeTarget.contains(e.target)) return;
    closeTooltip();
  }, true);

  document.addEventListener('keydown', function(e){
    if (e.key === 'Escape') closeTooltip();
  });

  window.addEventListener('scroll', positionTooltip, true);
  window.addEventListener('resize', positionTooltip);

  tooltip.addEventListener('pointerenter', function(){
    clearTimeout(closeTimer);
  });

  tooltip.addEventListener('pointerleave', closeTooltipSoon);

  console.info('WB tooltip side placement and tracking installed');
})();
// WB_TOOLTIP_SIDE_PLACEMENT_END
"""

changed = False

if STYLE_MARKER not in text:
    if "</head>" in text:
        text = text.replace("</head>", f"<style>{css}\n</style>\n</head>", 1)
    else:
        text = f"<style>{css}\n</style>\n" + text
    changed = True

if SCRIPT_MARKER not in text:
    if "</body>" in text:
        text = text.replace("</body>", f"<script>\n{js}\n</script>\n</body>", 1)
    else:
        text = text + f"\n<script>\n{js}\n</script>\n"
    changed = True

if not changed:
    print("Tooltip side placement implementation already present.")
else:
    HTML.write_text(text, encoding="utf-8")
    print(f"Patched {HTML}")
