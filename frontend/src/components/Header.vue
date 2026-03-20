<template>
  <header>
    <p>Hello</p>
    <p>{{ groups }}</p>
    <p>{{ username }}</p>
  </header>
</template>

<script>
  export default {
    props: ["user"],
    computed: {
      groups() {
        if (this.user.authenticated === true) {
          const cleaned_group_list = this.user.userinfo.groups.map(group => group.slice(1))
          return cleaned_group_list
        }

        else {
          return null
        }
      },

      username() {
        return this.user.authenticated === true ? this.user.userinfo.preferred_username : null
      }
    }
  }
</script>

<style scoped>
  header {
    background-color: red;
    height: 5vh;
  }
</style>
