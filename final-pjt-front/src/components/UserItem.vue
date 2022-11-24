<template>
  <div>
    <div id="homecontainer">
         <router-link
          :to="{
          name: 'profile',
          params: { 
            userId: user.id,
            userName: user.username }
          }"
        >
          {{user.username}}
        </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: "TempTest",
  props: {
    user: Object,
  },
  created() {
    
  }
}
</script>

<style>
</style>