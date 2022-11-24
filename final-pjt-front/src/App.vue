<template>
  <div id="app">   
      <nav>
        <ul>
          <!-- <li><router-link :to="{name:'survey'}">서베이</router-link></li> -->
          <li><router-link :to="{name:'home'}">Home</router-link></li>
          <li v-if="!isLogin"><router-link :to="{name:'SignUpView'}">SignUp</router-link></li>
          <li v-if="!isLogin"><router-link :to="{name:'login'}" class="a">LogIn</router-link></li>
          <li v-if="isLogin">
            <router-link 
            :to="{
              name: 'profile',
              params: {
                userId: this.$store.state.userId,
                userName: this.$store.state.userName }}">MyPage</router-link></li>
          <li v-if="isLogin"><a class="a" @click="logout">Logout</a></li>
        </ul>       
      </nav>
      <div>
        <div id="appbody">
        <router-view/>
      </div>

      </div>
  </div>
</template>

<script>
import { authComputed } from '@/store/helpers.js'

export default {
  computed: {
    ...authComputed
  },
  methods: {
    logout() {
      this.$store.dispatch('logout')
    },
  },
}
</script>

<style lang="scss">
@import "App";
</style>
