async function fetchJson(path) {
  const response = await fetch(path);
  if (!response.ok) {
    throw new Error(`Could not load ${path}: ${response.status}`);
  }
  return response.json();
}

class StaticJsonModelSource {
  constructor({
    teamsPath = "data/model/teams.json",
    usersPath = "data/model/users.json",
    bracketSlotsPath = "data/model/bracket_slots.json",
    fifaR32SlotMapPath = "data/model/fifa_r32_slot_map.json",
    userBracketsSeedPath = "data/model/user_brackets_seed.json",
  } = {}) {
    this.paths = {
      teamsPath,
      usersPath,
      bracketSlotsPath,
      fifaR32SlotMapPath,
      userBracketsSeedPath,
    };
  }

  async loadTeams() {
    return fetchJson(this.paths.teamsPath);
  }

  async loadUsers() {
    return fetchJson(this.paths.usersPath);
  }

  async loadBracketSlots() {
    return fetchJson(this.paths.bracketSlotsPath);
  }

  async loadFifaR32SlotMap() {
    return fetchJson(this.paths.fifaR32SlotMapPath);
  }

  async loadUserBracketsSeed() {
    return fetchJson(this.paths.userBracketsSeedPath);
  }

  async loadModelBundle() {
    const [teams, users, bracketSlots, fifaR32SlotMap, userBracketsSeed] = await Promise.all([
      this.loadTeams(),
      this.loadUsers(),
      this.loadBracketSlots(),
      this.loadFifaR32SlotMap(),
      this.loadUserBracketsSeed(),
    ]);

    return {
      teams,
      users,
      bracketSlots,
      fifaR32SlotMap,
      userBracketsSeed,
    };
  }
}

export { StaticJsonModelSource, fetchJson };
