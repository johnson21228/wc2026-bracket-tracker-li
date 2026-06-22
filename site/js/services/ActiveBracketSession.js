const ACTIVE_BRACKET_MODES = Object.freeze({
  LOCAL: "local",
  REMOTE: "remote",
});

function normalizeActiveBracketMode(mode) {
  return mode === ACTIVE_BRACKET_MODES.REMOTE ? ACTIVE_BRACKET_MODES.REMOTE : ACTIVE_BRACKET_MODES.LOCAL;
}

class ActiveBracketSession {
  constructor({ mode = ACTIVE_BRACKET_MODES.LOCAL, store, bracketDocument = null } = {}) {
    this.mode = normalizeActiveBracketMode(mode);
    this.store = store || null;
    this.bracketDocument = bracketDocument;
  }

  get isLocalMode() {
    return this.mode === ACTIVE_BRACKET_MODES.LOCAL;
  }

  get isRemoteMode() {
    return this.mode === ACTIVE_BRACKET_MODES.REMOTE;
  }

  async loadUserBracket(userId) {
    if (!this.store?.loadUserBracket) {
      throw new Error(`ActiveBracketSession ${this.mode} mode requires a loadUserBracket store method.`);
    }
    this.bracketDocument = await this.store.loadUserBracket(userId);
    return this.bracketDocument;
  }

  async saveUserBracket(bracketDocument) {
    if (!this.store?.saveUserBracket) {
      throw new Error(`ActiveBracketSession ${this.mode} mode requires a saveUserBracket store method.`);
    }
    this.bracketDocument = await this.store.saveUserBracket(bracketDocument);
    return this.bracketDocument;
  }
}

function createLocalActiveBracketSession({ store, bracketDocument = null } = {}) {
  return new ActiveBracketSession({
    mode: ACTIVE_BRACKET_MODES.LOCAL,
    store,
    bracketDocument,
  });
}

function createRemoteActiveBracketSessionPlaceholder() {
  return new ActiveBracketSession({
    mode: ACTIVE_BRACKET_MODES.REMOTE,
    store: null,
    bracketDocument: null,
  });
}

export {
  ACTIVE_BRACKET_MODES,
  ActiveBracketSession,
  createLocalActiveBracketSession,
  createRemoteActiveBracketSessionPlaceholder,
  normalizeActiveBracketMode,
};
