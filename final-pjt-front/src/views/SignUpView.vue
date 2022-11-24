<template>
  <div class="container">
    <div class = "row">
      <div id="signdiv" class="col" @submit.prevent="SignUp">
        <div id="signwrap">
          <p class="title">SIGN UP</p>
          <label for="username">username</label>
          <input type="text" id="username" v-model="username">
          <label for="password1">password</label>
          <input type="password" id="password1" v-model="password1">
          <label for="password2">password confirmation</label>
          <input type="password" id="password2" v-model="password2">
          <div class="light-button button-wrapper" @click="signUp">
            <div class="button">
              <span>
                가입하기
              </span>
            </div>  
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SignUpView",
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username, password1, password2,
      }
      this.$store.dispatch('signUp', payload)
    }
  },

}
</script>

<style lang="scss">
@import "SignUpView"
</style>