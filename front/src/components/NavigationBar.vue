<template>
    <b-navbar toggleable="lg" type="dark" variant="dark">
        <b-navbar-brand to="/">
            <b-icon-person-square></b-icon-person-square>
            WhoDat
        </b-navbar-brand>

        <b-navbar-nav>
            <b-nav-item v-for="route in routes" v-bind:key="route.text" :to="`${route.page}`">
              {{ route.text }}
            </b-nav-item>
        </b-navbar-nav>

    </b-navbar>
</template>

<script>
export default {
  name: 'NavigationBar',
  data() {
    return {
      routes: [
        {
          text: 'Home',
          page: '/',
        },
        {
          text: 'About',
          page: '/about',
        },
      ],
    };
  },
};
</script>

<style scoped>

</style>
