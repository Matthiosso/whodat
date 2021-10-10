<template>
    <b-input-group class="mt-3" size="lg">
        <b-button @click="showModal = !showModal" variant="danger">Add Target</b-button>
        <b-modal v-model="showModal"
                 @ok="handleOk"
                 title="Add Target">
            <b-form @submit.stop.prevent="handleSubmit">
                <b-form-group label="Formulaire">
                    <b-container fluid>
                        <div v-for="(colVal, colName) in target" :key="colName">
                            <b-row class="my-1">
                                <b-col sm="3">
                                    <label :for="colName">{{colName}}</label>
                                </b-col>
                                <template v-if="colName in options">
                                    <b-col sm="10">
                                        <b-form-select :id="colName" v-model="target[colName]"
                                                       :options="options[colName]"></b-form-select>
                                    </b-col>
                                </template>
                                <template v-else>
                                    <b-col sm="10">
                                        <b-form-input :id="colName"
                                                      v-model="target[colName]"></b-form-input>
                                    </b-col>
                                </template>
                            </b-row>
                        </div>
                    </b-container>
                </b-form-group>
            </b-form>
        </b-modal>
    </b-input-group>
</template>

<script>
import { mapActions, mapState } from 'vuex';

export default {
  name: 'AddTargetModal',
  data() {
    return {
      showModal: false,
      options: {
        asset_type: { FxSpot: 'FxSpot', Futur: 'Futur' },
        frequency_high: {
          1: '1m', 3: '3m', 5: '5m', 30: '30m', 60: '1h', 240: '4h', 1440: '1d',
        },
        frequency_low: {
          0: 'NA', 1: '1m', 3: '3m', 5: '5m', 30: '30m', 60: '1h', 240: '4h', 1440: '1d',
        },
        strategy: {
          EMA: 'EMA', MACD: 'MACD', NC_MACD: 'NC_MACD', NC_EMA: 'NC_EMA',
        },
      },
    };
  },
  methods: {
    handleOk(bvModalEvt) {
      // Prevent modal from closing
      bvModalEvt.preventDefault();
      // Trigger submit handler
      this.handleSubmit();
    },
    handleSubmit() {
      this.addTarget({
        newTarget: this.reformatJSON(),
        notifier: this.emitNotify,
      }).then(() => this.getTargets(this.emitNotify));

      this.$nextTick(() => {
        this.showModal = false;
      });
    },
    reformatJSON() {
      const json = this.target;
      return {
        email: json.email,
        first_name: json.first_name,
        family_name: json.family_name,
        phone_number: json.phone_number,
      };
    },
    emitNotify(message, type, isError) {
      this.$emit('notify', message, type, isError);
    },
    fetchData() {
      this.getTargets(this.emitNotify);
    },
    ...mapActions([
      'addTarget',
      'getTarget',
      'getTargets',
    ]),
  },
  computed: {
    ...mapState({
      target: (state) => state.targetModel,
    }),
  },
  mounted() {
    this.fetchData();
  },
};
</script>

<style scoped>

</style>
