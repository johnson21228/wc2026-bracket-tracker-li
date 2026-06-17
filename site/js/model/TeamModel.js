function normalizeTeamId(value) {
  return String(value || "").trim().toUpperCase();
}

function assertTeam(record) {
  const id = normalizeTeamId(record?.id);
  if (!/^[A-Z]{3}$/.test(id)) {
    throw new Error(`Invalid team id: ${record?.id}`);
  }

  return {
    id,
    name: String(record?.name || id),
    flag: String(record?.flag || ""),
  };
}

function indexTeamsById(teams) {
  const entries = Array.isArray(teams) ? teams : Object.values(teams || {});
  return Object.fromEntries(entries.map((team) => {
    const normalized = assertTeam(team);
    return [normalized.id, normalized];
  }));
}

export { assertTeam, indexTeamsById, normalizeTeamId };
