const MAX_MESSAGES = 80;
const messages = [];
const listeners = new Set();

function nowStamp() {
  return new Date().toLocaleTimeString();
}

function normalizeDetail(detail) {
  if (detail instanceof Error) {
    return detail.stack || detail.message;
  }

  if (detail === undefined || detail === null) {
    return "";
  }

  if (typeof detail === "string") {
    return detail;
  }

  try {
    return JSON.stringify(detail, null, 2);
  } catch {
    return String(detail);
  }
}

function emit(level, message, detail) {
  messages.push({
    level,
    message,
    detail: normalizeDetail(detail),
    time: nowStamp(),
  });

  while (messages.length > MAX_MESSAGES) {
    messages.shift();
  }

  listeners.forEach((listener) => listener([...messages]));
}

function debugLog(message, detail) {
  emit("log", message, detail);
}

function debugWarn(message, detail) {
  emit("warn", message, detail);
}

function debugError(message, detail) {
  emit("error", message, detail);
}

function installGlobalDebugConsole() {
  if (window.__wc2026DebugConsoleInstalled) return;
  window.__wc2026DebugConsoleInstalled = true;

  window.addEventListener("error", (event) => {
    debugError("window.error", event.error || event.message);
  });

  window.addEventListener("unhandledrejection", (event) => {
    debugError("unhandledrejection", event.reason);
  });

  debugLog("debug console installed");
}

function renderMessages(container, currentMessages) {
  container.replaceChildren();

  currentMessages.forEach((entry) => {
    const row = document.createElement("div");
    row.className = `developer-console-row developer-console-row-${entry.level}`;

    const meta = document.createElement("span");
    meta.className = "developer-console-meta";
    meta.textContent = `${entry.time} ${entry.level.toUpperCase()}`;

    const message = document.createElement("span");
    message.className = "developer-console-message";
    message.textContent = entry.message;

    row.append(meta, message);

    if (entry.detail) {
      const detail = document.createElement("pre");
      detail.className = "developer-console-detail";
      detail.textContent = entry.detail;
      row.append(detail);
    }

    container.append(row);
  });

  container.scrollTop = container.scrollHeight;
}

function createDebugConsole({ title = "Developer console" } = {}) {
  const panel = document.createElement("section");
  panel.className = "developer-console";
  panel.dataset.module = "DebugConsole";
  panel.setAttribute("aria-label", title);

  const heading = document.createElement("h2");
  heading.textContent = title;

  const body = document.createElement("div");
  body.className = "developer-console-body";

  panel.append(heading, body);

  const listener = (currentMessages) => renderMessages(body, currentMessages);
  listeners.add(listener);
  listener([...messages]);

  return panel;
}

export {
  createDebugConsole,
  debugError,
  debugLog,
  debugWarn,
  installGlobalDebugConsole,
};
