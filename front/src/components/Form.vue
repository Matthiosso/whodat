<template>
  <b-container>
    <b-form @submit="onSubmit" @reset="onReset" v-if="show" inline>
      <b-form-select
        id="input-3"
        v-model="form.field"
        :options="fields"
        class="mb-2 mr-sm-2 mb-sm-0"
        required></b-form-select>
      <b-form-input
        id="input-1"
        v-model="form.value"
        type="text"
        class="mb-2 mr-sm-2 mb-sm-0"
        :placeholder="`Enter ${form.field}`"
        required
      ></b-form-input>
      <b-button type="submit" variant="primary">Submit</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
    </b-form>
    <b-card class="mt-3" header="Form Data Result">
      <pre class="m-0">{{ targetModel }}</pre>
    </b-card>
  </b-container>
</template>

<script>
import { mapState, mapActions } from 'vuex';

export default {
  data() {
    return {
      form: {
        field: 'twitterId',
        value: '',
      },
      show: true,
      fields: [
        {
          value: 'twitterId',
          text: 'Twitter ID',
        },
        {
          value: 'email',
          text: 'Email',
        },
        {
          value: 'fullName',
          text: 'Full name',
        },
      ],
    };
  },
  methods: {
    onSubmit(event) {
      event.preventDefault();
      // alert(JSON.stringify(this.form));
      this.addTargetField({
        form: this.form,
        notifier: this.emitNotify,
      });
    },
    onReset(event) {
      event.preventDefault();
      // Reset our form values
      this.form.field = 'twitterId';
      this.form.value = '';
      // Trick to reset/clear native browser form validation state
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    },
    emitNotify(message, type, isError) {
      this.$emit('notify', message, type, isError);
    },
    ...mapActions([
      'addTargetField',
    ]),
  },
  computed: {
    ...mapState({
      targetModel: (state) => state.targetModel,
    }),
  },
};
</script>
