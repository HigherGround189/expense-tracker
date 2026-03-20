<template>
  <div>
    <Header :user="this.userinfo"/>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        userinfo: null
      }
    },

    mounted() {
      fetch("/api/user-info")
      .then(response => response.json())
      .then(data => this.userinfo = data);
    }
  }
</script>

<style scoped>

</style>
