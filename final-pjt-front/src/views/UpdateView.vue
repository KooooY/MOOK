<template>
  <div class="container">
    <div class = "row">
      <div id="creatediv" class="col" @submit.prevent="updateReview">
          <div id="createwrap">
            <p class="title">리뷰 수정</p>
            <label for="title">제목</label>
            <input type="text" id="title" v-model="title">
            <label for="content">내용</label>
            <textarea id="content" rows="10" v-model="content"></textarea>
            <div class="light-button button-wrapper" @click="updateReview">
              <div class="button">
                <span>
                  수정
                </span>
              </div>  
            </div>
          </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import router from '../router'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: "UpdateView",
  data() {
    return {
      // userId: null,
      review: null,
      title: null,
      content: null,
      id: null,
      created_at: null,
      movie: null,
      user: null,
      // userScore: null,
    }
  },
  created() {
    this.getReviewDetail()
  },

  methods: {
    bindTitle(event) {
      this.title = event.target.value
    },
    bindContent(event) {
      this.content = event.target.value
    },
    bindScore(event) {
      this.userScore = event.target.value
    },
    updateReview() {
      const title = this.title
      const content = this.content
      const id = this.id
      const created_at = this.created_at
      const movie = this.movie
      const user = this.user
      // const userScore = this.userScore

      axios({
        method: 'put',
        url: `${API_URL}/api/reviews/${this.$route.params.reviewId}/`,
        data: {
          title, content, id, created_at, movie, user,
        // userScore,  
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
    })
      .then(res => {
        console.log(res.data)
        console.log(this.id)
        router.push({name: "reviewdetail", params: {review: res.data, reviewId: res.data.id,}})
      })
      .catch(err => console.log(err))
    },
    getUserDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/users/${this.$route.params.userId}/`,
      })
        .then((res) => {
          console.log('겟유저', res.data)
          console.log(res.data)
          this.userId = res.data
        })
        .catch(err => console.log(err))
    },
    getReviewDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/api/reviews/${this.$route.params.reviewId}/`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        },
      })
        .then((res) => {
          // console.log('겟리뷰', res.data)
          this.review = res.data
          this.title = res.data.title
          this.content = res.data.content
          this.id = res.data.id
          this.created_at = res.data.created_at
          this.movie = res.data.movie
          this.user = res.data.user
        })
        .catch(err => console.log(err))
    },
  },
    //   const payload = {
    //     userId, movieId, title, content, userScore,
    //   }
    //   this.$store.dispatch('createReview', payload)
    // }
  // watch: {
  //   number(val){
  //     const reg = /[ㄱ-ㅎ|ㅏ-ㅣ|가-힣|a-z]/;

  //     if(reg.exec(val)!==null) this.userScore = val.replace(/[^0-9]/g,'');
  //     if(isNaN(parseFloat(val))) this.userScore = '';
  //   }
  // },
}
</script>

<style lang="scss">
@import "UpdateView"
</style>