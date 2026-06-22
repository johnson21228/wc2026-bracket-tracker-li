const REMOTE_STORE_DISABLED_REASON = "Remote bracket store is not enabled for this build.";

const DEFAULT_REMOTE_STORE_ACTIVATION = Object.freeze({
  remoteStoreEnabled: false,
  source: "build-default",
  reason: REMOTE_STORE_DISABLED_REASON,
});

function normalizeRemoteStoreActivation(input = {}) {
  return Object.freeze({
    remoteStoreEnabled: input.remoteStoreEnabled === true,
    source: String(input.source || DEFAULT_REMOTE_STORE_ACTIVATION.source),
    reason: String(input.reason || DEFAULT_REMOTE_STORE_ACTIVATION.reason),
  });
}

function createRemoteStoreActivationGuard(input = {}) {
  const activation = normalizeRemoteStoreActivation(input);

  return Object.freeze({
    get remoteStoreEnabled() {
      return activation.remoteStoreEnabled;
    },

    get source() {
      return activation.source;
    },

    get reason() {
      return activation.reason;
    },

    assertRemoteStoreEnabled() {
      if (!activation.remoteStoreEnabled) {
        throw new Error(activation.reason);
      }
      return true;
    },

    describe() {
      return {
        remoteStoreEnabled: activation.remoteStoreEnabled,
        source: activation.source,
        reason: activation.reason,
      };
    },
  });
}

const DEFAULT_REMOTE_STORE_ACTIVATION_GUARD = createRemoteStoreActivationGuard();

export {
  DEFAULT_REMOTE_STORE_ACTIVATION,
  DEFAULT_REMOTE_STORE_ACTIVATION_GUARD,
  REMOTE_STORE_DISABLED_REASON,
  createRemoteStoreActivationGuard,
  normalizeRemoteStoreActivation,
};
