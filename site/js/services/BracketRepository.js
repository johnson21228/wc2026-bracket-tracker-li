import { indexTeamsById } from "../model/TeamModel.js";
import { createEmptyUserBracket, hydrateOfficialR32Occupants, normalizeUserBracket } from "../model/UserBracketModel.js";
import { LocalStorageBracketStore } from "./LocalStorageBracketStore.js";
import { SupabaseBracketStore } from "./SupabaseBracketStore.js";
import { StaticJsonModelSource } from "./StaticJsonModelSource.js";

function usersById(usersModel) {
  return usersModel?.users || {};
}

function seedBracketForUser(seedModel, userId) {
  const brackets = seedModel?.brackets || {};
  return Object.values(brackets).find((bracket) => bracket.userId === userId) || null;
}

function staticOfficialR32Fallback(bundle) {
  if (!bundle?.officialRoundOf32) return null;
  return {
    ...bundle.officialRoundOf32,
    officialR32AuthoritySource: "StaticJsonFallback:official_round_of_32",
    source: "StaticJsonFallback:official_round_of_32",
    authority: "Admin_/official",
    fallbackOnly: true,
  };
}

class BracketRepository {
  constructor({
    modelSource = new StaticJsonModelSource(),
    bracketStore = new LocalStorageBracketStore(),
  } = {}) {
    this.modelSource = modelSource;
    this.bracketStore = bracketStore;
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

  async loadOfficialR32Source(bundle = null) {
    const modelBundle = bundle || await this.loadModelBundle();

    if (this.bracketStore && typeof this.bracketStore.loadOfficialR32BracketAuthority === "function") {
      try {
        const officialBracket = await this.bracketStore.loadOfficialR32BracketAuthority({
          tournamentId: this.tournamentId || "wc2026",
          gameId: this.gameId || "game1",
        });

        // Admin_/official is authoritative when the row exists, even while partial.
        // Static JSON only fills local/dev missing-admin-source cases.
        if (officialBracket) {
          return {
            ...officialBracket,
            userId: "Admin_/official",
            bracketKind: "official",
            officialR32AuthoritySource: "Supabase:Admin_/official",
            officialResultsTruthSource: "Supabase:Admin_/official",
            source: "Supabase:Admin_/official",
            authority: "Admin_/official",
          };
        }
      } catch (error) {
        console.warn("[WC2026 Official R32] Supabase Admin_/official bracket unavailable; using static fallback", error);
      }
    }

    return staticOfficialR32Fallback(modelBundle);
  }

  async loadUserBracket(userId) {
    const bundle = await this.loadModelBundle();
    const teamsById = indexTeamsById(bundle.teams?.teams || bundle.teams || {});

    const officialR32 = await this.loadOfficialR32Source(bundle);
    const stored = await this.bracketStore.loadUserBracket(userId);
    const seed = stored || seedBracketForUser(bundle.userBracketsSeed, userId);

    const bracket = seed || createEmptyUserBracket({
      userId,
      bracketId: `${userId}-wc2026`,
      bracketSlots: bundle.bracketSlots,
      teamsById,
      officialR32,
    });

    return normalizeUserBracket({
      bracket,
      bracketSlots: bundle.bracketSlots,
      teamsById,
      officialR32,
    });
  }

  async saveUserBracket(bracket) {
    const bundle = await this.loadModelBundle();
    const teamsById = indexTeamsById(bundle.teams?.teams || bundle.teams || {});
    const officialR32 = await this.loadOfficialR32Source(bundle);
    const hydratedBracket = hydrateOfficialR32Occupants({
      bracket,
      bracketSlots: bundle.bracketSlots,
      teamsById,
      officialR32,
    });
    return this.bracketStore.saveUserBracket(hydratedBracket);
  }
}

function createStaticBracketRepository() {
  return new BracketRepository({
    modelSource: new StaticJsonModelSource(),
    bracketStore: new LocalStorageBracketStore(),
  });
}


function createSupabaseBracketRepository(options = {}) {
  return new BracketRepository({
    modelSource: new StaticJsonModelSource(),
    bracketStore: new SupabaseBracketStore(options),
  });
}

export {
  BracketRepository,
  createStaticBracketRepository,
  createSupabaseBracketRepository,
};
