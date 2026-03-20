<template>
  <div>
    Hello World Sanity Check
    <DatePicker v-model="date" />
    <p>{{ this.userinfo }}</p>
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
      console.log("Mounted")
      fetch("/api/user-info")
      .then(response => response.json())
      .then(data => this.userinfo = data);
    }
  }
</script>

<style scoped>

</style>
