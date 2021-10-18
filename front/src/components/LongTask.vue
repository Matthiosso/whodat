<template>
    <b-container>
      <b-button variant="info" @click="start_long_task">
                Start long task
      </b-button>
      <b-progress :max="progress.max" show-progress animated>
        <b-progress-bar :value="progress.value">
          <span><strong>{{ progress.value.toFixed(2) }}%</strong></span>
        </b-progress-bar>
      </b-progress>
       <div>{{progress.status}}</div>
    </b-container>
</template>

<script>
import axios from 'axios';

export default {
  name: 'LongTask',
  data() {
    return {
      progress: {
        value: 0,
        max: 100,
        status: 'Unknown...',
      },
      result: '',
    };
  },
  methods: {
    start_long_task() {
      const that = this;

      // send ajax POST request to start background job
      axios.post('http://localhost:5000/longtask', {})
        .then((response) => {
          const { data } = response;
          const statusUrl = data.status;
          console.log(statusUrl);
          that.updateProgress(`http://localhost:5000${statusUrl}`);
        }).catch((error) => {
          console.error('Unexpected error', error);
        });
    },
    updateProgress(statusUrl) {
      const that = this;

      // send GET request to status URL
      axios.get(statusUrl)
        .then((response) => {
          const { data } = response;
          // update UI
          that.progress.value = (data.current * 100) / data.total;
          that.progress.status = data.status;
          if (data.state !== 'PENDING' && data.state !== 'PROGRESS') {
            if ('result' in data) {
              // show result
              that.progress.status = `Result: ${data.result}`;
            } else {
              // something unexpected happened
              that.progress.status = `Result: ${data.state}`;
            }
          } else {
            // rerun in 2 seconds
            setTimeout(() => {
              that.updateProgress(statusUrl);
            }, 2000);
          }
        }).catch((error) => {
          console.log('Error', error);
        });
    },
  },
};
</script>

<style scoped>

</style>
