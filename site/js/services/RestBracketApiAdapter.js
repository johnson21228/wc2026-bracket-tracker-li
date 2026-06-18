function trimTrailingSlash(value) {
  return String(value || "").replace(/\/+$/, "");
}

class RestBracketApiAdapter {
  constructor({ baseUrl = "/api" } = {}) {
    this.baseUrl = trimTrailingSlash(baseUrl);
  }

  async request(path, options = {}) {
    const response = await fetch(`${this.baseUrl}${path}`, {
      headers: {
        "content-type": "application/json",
        ...(options.headers || {}),
      },
      ...options,
    });

    if (!response.ok) {
      throw new Error(`REST request failed ${response.status}: ${path}`);
    }

    if (response.status === 204) return null;
    return response.json();
  }

  async loadTeams() {
    return this.request("/teams");
  }

  async loadUsers() {
    return this.request("/users");
  }

  async loadBracketSlots() {
    return this.request("/bracket-slots");
  }

  async loadFifaR32SlotMap() {
    return this.request("/fifa-r32-slot-map");
  }

  async loadUserBracket(userId) {
    return this.request(`/users/${encodeURIComponent(userId)}/bracket`);
  }

  async saveUserBracket(bracket) {
    return this.request(`/users/${encodeURIComponent(bracket.userId)}/bracket`, {
      method: "PUT",
      body: JSON.stringify(bracket),
    });
  }

  async createUser(user) {
    return this.request("/users", {
      method: "POST",
      body: JSON.stringify(user),
    });
  }
}

export { RestBracketApiAdapter };
