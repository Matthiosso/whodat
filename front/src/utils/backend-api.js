import axios from 'axios';

export default {
  axiosInstance: axios.create({
    baseURL: 'http://localhost:5000/',
  }),
  hello() {
    return this.axiosInstance.get('/ping');
  },
  getTargets() {
    return this.axiosInstance.get('/targets');
  },
  getTarget(targetId) {
    return this.axiosInstance.get(`/target/${targetId}`);
  },
  addTarget(newTarget) {
    return this.axiosInstance.post('/target/insert', newTarget);
  },
  updateTarget(updateTargetid, updateTarget) {
    return this.axiosInstance.put(`/target/update/${updateTargetid}`, updateTarget);
  },
  deleteTarget(deleteTargetid) {
    console.log(`Deleting ${deleteTargetid}`);
    return this.axiosInstance.delete(`/target/delete/${deleteTargetid}`);
  },
};
