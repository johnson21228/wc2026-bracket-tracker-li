class BracketStorageAdapter {
  async loadUserBracket(_userId) {
    throw new Error("loadUserBracket must be implemented by a storage adapter");
  }

  async saveUserBracket(_bracket) {
    throw new Error("saveUserBracket must be implemented by a storage adapter");
  }

  async listUsers() {
    throw new Error("listUsers must be implemented by a storage adapter");
  }
}

export { BracketStorageAdapter };
