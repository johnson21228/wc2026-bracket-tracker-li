import { normalizeTeamId } from "./TeamModel.js";

const UNPICKED = Object.freeze({ kind: "unpicked" });

function unpickedPickValue() {
  return { ...UNPICKED };
}

function teamPickValue(teamId) {
  return {
    kind: "team",
    teamId: normalizeTeamId(teamId),
  };
}

function normalizePickValue(value) {
  if (!value || value.kind === "unpicked") {
    return unpickedPickValue();
  }

  if (value.kind === "team") {
    return teamPickValue(value.teamId);
  }

  throw new Error(`Unsupported pick value kind: ${value.kind}`);
}

function validatePickValue(value, teamsById) {
  const normalized = normalizePickValue(value);

  if (normalized.kind === "team" && !teamsById[normalized.teamId]) {
    throw new Error(`Pick references unknown team id: ${normalized.teamId}`);
  }

  return normalized;
}

export {
  normalizePickValue,
  teamPickValue,
  unpickedPickValue,
  validatePickValue,
};
