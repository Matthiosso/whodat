import Vue from 'vue';
import Vuex from 'vuex';

import api from '@/utils/backend-api';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    targets: [],
    targetModel: {
      email: '',
      first_name: '',
      family_name: '',
      phone_number: '',
    },
  },
  mutations: {
    updateTargets(state, targets) {
      state.targets = targets;
    },
  },
  actions: {
    getTargets({ commit }, notifier) {
      return api.getTargets()
        .then((resp) => resp.data)
        .then((targets) => { commit('updateTargets', targets); })
        .catch((err) => { notifier(err, 'getTargets', true); });
    },
    deleteTarget(context, { deleteTargetId, notifier }) {
      return api.deleteTarget(deleteTargetId)
        .then(() => { notifier('Target deleted', 'deleteTarget'); })
        .catch((err) => { notifier(err, 'deleteTarget', true); });
    },
    addTarget(context, { newTarget, notifier }) {
      return api.addTarget(newTarget)
        .then(() => notifier('New Target added', 'addTarget'))
        .catch((err) => notifier(err, 'addTarget', true));
    },
  },
  modules: {
  },
});
