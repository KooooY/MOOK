<template>
  <div>
    <form @submit.prevent="createGuest">
      <label for="content"></label>
      <br>
      <textarea id="content" rows="1" v-model="content" style="width: 760px"></textarea>
      <input type="submit" id="submit" value="  O  ">
    </form>
    
    <!-- <button @click="postReview">작성</button> -->
  </div>
</template>

<script>
import axios from 'axios'
import router from '../router'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: "GuestCreate",
  data() {
    return {
      userId: null,      
      content: null,      
    }
  },
  props:{
    guest: Object,
  },
  methods: {
    // bindTitle(event) {
    //   this.title = event.target.value
    // },
    // bindContent(event) {
    //   this.content = event.target.value
    // },
    // bindScore(event) {
    //   this.userScore = event.target.value
    // },
    createGuest() {
      const guest = this.$store.state.userName
      // console.log(user)
      const owner = this.$route.params.ownerId
      
      const content = this.content
      console.log(this.$route.params)

      axios({
        method: 'post',
        url: `${API_URL}/api/guests_create/${this.$route.params.userId}/${this.$store.state.userId}/`, //리뷰아이디 어떻게 넣지..
        data: {
          guest,
          owner, 
          content,         
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
    })
      .then(res => {
        router.push({
          path:`/profile/${res.data.owner}`, 
          // params: {
          //   owner: res.data.owner,
          //   guest: res.data.guest,

          // }
        })
      })
      .catch(err => console.log(err))
    },
    getUserDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/users/${this.$route.params.userId}/`,
      })
        .then((res) => {
          console.log(res.data)
          this.userId = res.data
        })
        .catch(err => console.log(err))
    },
  },
    
}
</script>

<style>
  
</style>