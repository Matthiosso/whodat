<template>
<div>
    <b-input-group class="mt-3" size="lg">
        <b-input-group-prepend is-text>
            <b-icon icon="display"></b-icon>
        </b-input-group-prepend>
        <b-input-group-append>
            <b-button variant="info" @click="updateSearch">
                Get Targets
            </b-button>
            <b-button variant="secondary" @click="showTable = !showTable">
                <template v-if="showTable">
                    <b-icon icon="arrow-bar-down" aria-hidden="true"></b-icon>
                </template>
                <template v-else>
                    <b-icon icon="arrow-bar-left" aria-hidden="true"></b-icon>
                </template>
            </b-button>
        </b-input-group-append>

    </b-input-group>
    <b-collapse v-model="showTable">
            <b-card>
                <b-card-body class="text-left overflow-auto">
                    <b-row>
                        <b-col>
                            <b-pagination v-model="currentPage"
                                          @input="updateSearch($event)"
                                          :total-rows="totalElements"
                                          :per-page="selectedMaxRow"
                                          aria-controls="targets-table" pills></b-pagination>
                        </b-col>
                        <b-col>
                            <b-form-group label="Taille" label-for="selectPaginationMaxRow"
                                          class="form-inline">
                                <b-form-select v-model="selectedMaxRow"
                                               class="ml-2"
                                               id="selectPaginationMaxRow"
                                               :options="[5, 10, 20, 50]"
                                               @input="updateSearch"
                                               size="sm"></b-form-select>
                            </b-form-group>
                        </b-col>
                        <b-col>
                            <b-badge variant="primary">
                              {{ totalElements }} {{ 'target' | pluralize(totalElements) }}
                            </b-badge>
                        </b-col>
                    </b-row>
                    <b-table  striped hover
                              class="mt-3"
                              id="targets-table"
                              :fields="fields"
                              :items="targets"
                              :total-rows="totalElements"
                              :current-page="currentPage"
                              :per-page="selectedMaxRow"
                              :sort-by="sortBy"
                              head-variant="dark">
                          <template slot="bottom-row" v-if="!totalElements">
                            <td :span="targets.order_columns">Aucun élément trouvé</td>
                          </template>
                          <template #cell(actions)="row">
<!--                            <UpdateTargetModal :taskid="row.item.id"></UpdateTargetModal>-->
                            <b-button variant="danger" size="sm"
                                      v-on:click="delTarget(row.item.id)">
                            Delete
                            </b-button>
                          </template>
                    </b-table>
                </b-card-body>
            </b-card>
        </b-collapse>
</div>
</template>

<script>
import { mapActions, mapState } from 'vuex';

export default {
  name: 'TargetsTable',
  data() {
    return {
      showTable: false,
      currentPage: 1,
      selectedMaxRow: 5,
      sortBy: 'id',
      sortDesc: false,
      fields: [
        {
          key: 'id',
          label: 'ID',
          sortable: true,
        },
        {
          key: 'json_doc',
          label: 'infos',
          sortable: false,
        },
        {
          key: 'actions',
          label: 'Actions',
        },
      ],
    };
  },
  methods: {
    emitNotify(message, type, isError) {
      this.$emit('notify', message, type, isError);
    },
    updateSearch() {
      this.getTargets(this.emitNotify).then(() => { this.showTable = true; });
    },
    delTarget(id) {
      // eslint-disable-next-line no-restricted-globals
      if (confirm('Do you really want to delete ?')) {
        this.deleteTarget({
          deleteTargetId: id,
          notifier: this.emitNotify,
        }).then(() => this.getTargets(this.emitNotify));
      }
    },
    ...mapActions([
      'getTargets',
      'deleteTarget',
    ]),
  },
  computed: {
    ...mapState({
      targets: (state) => state.targets,
    }),
    totalElements() {
      return this.targets.length ? this.targets.length : 0;
    },
  },
  filters: {
    contentify(content) {
      return content.length > 5 ? `${content.substr(0, 5)}...` : content;
    },
    pluralize(value, number) {
      return number > 1 ? `${value}s` : value;
    },
  },
};
</script>

<style scoped>

</style>
