<template>
  <div id="cmtbox">
    <p>{{ user.username }}</p>
    <span
      :to="{
      name:'reviewdetail',
      params:{
        // movieId: review.movie,
        // userId: review.user,
        comment: comment,
        commentId: comment.id,
      }
    }" style="width:240px">
    {{ comment.content }}
    </span>
    <div v-if="this.user.username == this.$store.state.userName">
      <button @click="delReview">X</button>
    </div>
  </div>
</template>

<script>

import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'


export default {
  name:"CommentItem",
  props:{
    comment: Object,
  },
  data() {
    return {
      user: null,
    }
  },
  created() {
    this.getUserDetail()
  },
  methods:{
    getUserDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/users/${this.comment.user}/`,
      })
        .then((res) => {
          this.user = res.data
        })
        .catch(err => console.log(err))
    },
    delReview() {
      if (confirm('정말 삭제하시겠습니까?'))
      axios({
        method: 'delete',
        url: `${API_URL}/api/comments/${this.comment.id}/`,
      })
          .then(res => {
            console.log(res)
            // router.push({path:'/reviews'})
          })
          .catch(err => console.log(err))
    },

  }
}
</script>

<style>

</style>