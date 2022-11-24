<template>
  <div>
    <p>임시로 만든 유저목록~</p>
    <UserItem
    v-for="user in users"
    :key="user.id"
    :user="user"
    />
  </div>
</template>

<script>
import UserItem from '@/components/UserItem';
import { authComputed } from '@/store/helpers.js'

export default {
  name: "TempMembersView",
  components: {
    UserItem
},
  created() {
    this.getUsers()
  },
  methods: {
    getUsers() {
      if (this.isLogin) {
      this.$store.dispatch('getUsers')
    } else {
      alert('로그인하세요!')
      this.$router.push({ name:'login'})
    }
  },
  },
  computed: {
    users() {
      return this.$store.state.users
    },
    ...authComputed,
  },
}
</script>

<style>
</style>