<template>
  <b-container>
    <b-form @submit="onSubmit" @reset="onReset" v-if="show" inline>
      <div v-for="item in fields" :key="item.field">
        <label class="mr-sm-2" :for="'input' + item.id">{{item.text}}</label>
        <b-form-input
          :id="'input' + item.id"
          v-model="item.value"
          type="text"
          class="mb-2 mr-sm-2 mb-sm-0"
          :placeholder="item.placeholder"
        ></b-form-input>
      </div>

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
      show: true,
      fields: [
        {
          id: 'twitterId',
          text: 'Twitter ID',
          value: '',
          placeholder: '1234',
        },
        {
          id: 'email',
          text: 'Email',
          value: '',
          placeholder: 'monmail@bmail.com',
        },
        {
          id: 'fullName',
          text: 'Full name',
          value: '',
          placeholder: 'John Doe',
        },
      ],
    };
  },
  methods: {
    onSubmit(event) {
      event.preventDefault();
      // alert(JSON.stringify(this.form));
      this.addTargetField({
        form: this.fields,
        notifier: this.emitNotify,
      });
    },
    onReset(event) {
      event.preventDefault();
      // Reset our form values
      this.fields = [
        {
          id: 'twitterId',
          text: 'Twitter ID',
          value: '',
          placeholder: '1234',
        },
        {
          id: 'email',
          text: 'Email',
          value: '',
          placeholder: 'monmail@bmail.com',
        },
        {
          id: 'fullName',
          text: 'Full name',
          value: '',
          placeholder: 'John Doe',
        },
      ];
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
