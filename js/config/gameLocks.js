// Shared player-facing lock schedule for Bracketeering picks/results.
// Thursday, June 25, 2026 at 11:59 PM ET.
export const GROUP_STAGE_PICKS_LOCK_AT = "2026-06-25T23:59:00-04:00";
export const GROUP_STAGE_PICKS_LOCK_AT_MS = Date.parse(GROUP_STAGE_PICKS_LOCK_AT);
export const GROUP_STAGE_PICKS_LOCK_TIMER_MAX_MS = 2147483647;

export function areGroupStagePicksLocked(now = new Date()) {
  const nowMs = now instanceof Date ? now.getTime() : Date.parse(now);
  return Number.isFinite(GROUP_STAGE_PICKS_LOCK_AT_MS)
    && Number.isFinite(nowMs)
    && nowMs >= GROUP_STAGE_PICKS_LOCK_AT_MS;
}

export function groupStagePicksLockedMessage() {
  return "Group Stage Picks are locked.";
}

export function playerResultsHiddenUntilLockMessage() {
  return "Standings open after Group Stage Picks lock.";
}
