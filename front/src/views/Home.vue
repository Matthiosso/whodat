<template>
  <div class="home">
    <b-form-group label-cols-lg="3"
                      class="mb-0">
      <Form class="mt-3" @notify="notify"></Form>
      <LongTask class="mt-3" @notify="notify"></LongTask>
      <AddTargetModal class="mt-3" @notify="notify"></AddTargetModal>
      <TargetsTable class="mt-3" @notify="notify"></TargetsTable>
    </b-form-group>
  </div>
</template>

<script>
import AddTargetModal from '@/components/AddTargetModal.vue';
import TargetsTable from '@/components/TargetsTable.vue';
import LongTask from '@/components/LongTask.vue';
import Form from '@/components/Form.vue';

export default {
  name: 'Home',
  components: {
    Form,
    TargetsTable,
    AddTargetModal,
    LongTask,
  },
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
