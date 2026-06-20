import { normalizeBracketDocument } from "../model/UserBracketModel.js";
import { BracketStorageAdapter } from "./BracketStorageAdapter.js";

const DEFAULT_NAMESPACE = "wc2026.bracket";

function keyFor(namespace, userId) {
  return `${namespace}.userBracket.${userId}`;
}

class LocalStorageBracketStore extends BracketStorageAdapter {
  constructor({ namespace = DEFAULT_NAMESPACE } = {}) {
    super();
    this.namespace = namespace;
  }

  async loadUserBracket(userId) {
    const raw = window.localStorage.getItem(keyFor(this.namespace, userId));
    return raw ? JSON.parse(raw) : null;
  }

  async saveUserBracket(bracket) {
    if (!bracket?.picksBySlot) {
      throw new Error("LocalStorageBracketStore.saveUserBracket requires canonical BracketDocument picksBySlot");
    }
    const canonicalBracketDocument = normalizeBracketDocument({
      bracket,
      bracketSlots: { canonicalPickSlots: Object.values(bracket.picksBySlot || {}) },
      teamsById: {},
      userId: bracket.userId,
      gameId: bracket.gameId || "game1",
    });
    window.localStorage.setItem(
      keyFor(this.namespace, canonicalBracketDocument.userId),
      JSON.stringify(canonicalBracketDocument, null, 2)
    );
    return canonicalBracketDocument;
  }

  async listUsers() {
    const prefix = `${this.namespace}.userBracket.`;
    return Object.keys(window.localStorage)
      .filter((key) => key.startsWith(prefix))
      .map((key) => key.slice(prefix.length));
  }
}

export { LocalStorageBracketStore };
