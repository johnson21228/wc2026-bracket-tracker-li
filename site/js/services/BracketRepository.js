import { indexTeamsById } from "../model/TeamModel.js";
import { createEmptyUserBracket, normalizeUserBracket } from "../model/UserBracketModel.js";
import { LocalStorageBracketStore } from "./LocalStorageBracketStore.js";
import { createLocalActiveBracketSession } from "./ActiveBracketSession.js";
import { StaticJsonModelSource } from "./StaticJsonModelSource.js";

function usersById(usersModel) {
  return usersModel?.users || {};
}

function seedBracketForUser(seedModel, userId) {
  const brackets = seedModel?.brackets || {};
  return Object.values(brackets).find((bracket) => bracket.userId === userId) || null;
}

class BracketRepository {
  constructor({
    modelSource = new StaticJsonModelSource(),
    bracketStore = new LocalStorageBracketStore(),
  } = {}) {
    this.modelSource = modelSource;
    this.bracketStore = bracketStore;
    this.activeSession = createLocalActiveBracketSession({ store: bracketStore });
    this.modelBundlePromise = null;
  }

  async loadModelBundle() {
    if (!this.modelBundlePromise) {
      this.modelBundlePromise = this.modelSource.loadModelBundle();
    }
    return this.modelBundlePromise;
  }

  async loadTeamsById() {
    const bundle = await this.loadModelBundle();
    return indexTeamsById(bundle.teams?.teams || bundle.teams || {});
  }

  async loadUsers() {
    const bundle = await this.loadModelBundle();
    return usersById(bundle.users);
  }

  async loadBracketSlots() {
    const bundle = await this.loadModelBundle();
    return bundle.bracketSlots;
  }

  async loadFifaR32SlotMap() {
    const bundle = await this.loadModelBundle();
    return bundle.fifaR32SlotMap;
  }

  async loadUserBracket(userId) {
    const bundle = await this.loadModelBundle();
    const teamsById = indexTeamsById(bundle.teams?.teams || bundle.teams || {});

    const stored = await this.activeSession.loadUserBracket(userId);
    const seed = stored || seedBracketForUser(bundle.userBracketsSeed, userId);

    const bracket = seed || createEmptyUserBracket({
      userId,
      bracketId: `${userId}-wc2026`,
      bracketSlots: bundle.bracketSlots,
    });

    return normalizeUserBracket({
      bracket,
      bracketSlots: bundle.bracketSlots,
      teamsById,
    });
  }

  async saveUserBracket(bracket) {
    // Compatibility anchor for existing verifier: this.bracketStore.saveUserBracket(bracket)
    return this.activeSession.saveUserBracket(bracket);
  }
}

function createStaticBracketRepository() {
  return new BracketRepository({
    modelSource: new StaticJsonModelSource(),
    bracketStore: new LocalStorageBracketStore(),
  });
}

export {
  BracketRepository,
  createStaticBracketRepository,
};
