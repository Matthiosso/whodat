<template>
  <div class="home">
    <b-form-group label-cols-lg="3"
                      label="Target list"
                      label-size="lg"
                      label-class="font-weight-bold pt-0"
                      class="mb-0">
      <LongTask></LongTask>
      <AddTargetModal class="mt-3" @notify="notify"></AddTargetModal>
      <TargetsTable class="mt-3" @notify="notify"></TargetsTable>
    </b-form-group>
  </div>
</template>

<script>
import AddTargetModal from '@/components/AddTargetModal.vue';
import TargetsTable from '@/components/TargetsTable.vue';
import LongTask from '@/components/LongTask.vue';

export default {
  name: 'Home',
  components: { TargetsTable, AddTargetModal, LongTask },
  methods: {
    notify(message, type, isError = false) {
      this.$bvToast.toast(`${message}`, {
        title: `Notification ${type}`,
        autoHideDelay: 5000,
        variant: isError ? 'danger' : 'success',
        appendToast: true,
      });
    },
  },
};
</script>
