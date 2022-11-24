<template>
  <div>
    <form @submit.prevent="createComment">
      <label for="content"></label>
      <textarea id="content" rows="1" v-model="content" style="width: 280px"></textarea>
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
  name: "CommentCreate",
  data() {
    return {
      userId: null,      
      content: null,      
    }
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
    createComment() {
      const user = this.$store.state.userName
      console.log(user)
      const review = this.$route.params.reviewId
      
      const content = this.content
      

      axios({
        method: 'post',
        url: `${API_URL}/api/reviews/comments/${review}/`, //리뷰아이디 어떻게 넣지..
        data: {
          user,
          review, 
          content,         
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
    })
      .then(res => {
        router.push({
          path:`/reviews/${res.data.review}`, 
          params: {reviewId: res.data.review}
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