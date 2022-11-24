<template>
  <div>
    <div v-if="movieURL != null && movieURL != undefined">
      <img :src="movieURL" alt="POSTER">
    </div>
    <p id="mvtitle">{{movie?.title}}</p>
    <p id="rvtitle">{{this.$store.state.review.title}}</p>
    <div id="wrt">
    <span class="wrtcon">작성자 </span>
    <router-link
          :to="{
          name: 'profile',
          params: { 
            userId: user.id,
            userName: user.username }
          }"
          class="wrtcon"
        >
          <p @click="saveWriter">{{user.username}}</p>
        </router-link>
    </div>
    <p id="rvcontent">{{review?.content}}</p>
    <div v-if="this.user.username == this.$store.state.userName" id="udbutton">
      <button @click="upReview">수정</button>
      <button @click="delReview">삭제</button>
    </div>
    <CommentBox
      :review="review" />
  </div>
</template>

<script>
import axios from 'axios'
import router from '../router'
const API_URL = 'http://127.0.0.1:8000'
import CommentBox from '@/components/CommentBox'
import { authComputed } from '@/store/helpers.js'

export default {
  name: "ReviewDetailView",
  components:{
    CommentBox
  },
  data() {
    return{
      review: this.$route.params.review,
      movie: null,
      user: null,
      userId: null,
      movieURL: null,
    }
  },

  created() {
    this.getReviewDetail()
    this.getMovieDetail()
    this.getUserDetail()
    this.getUsers()
  },
  computed: {
    ...authComputed,
  },
  methods: {
    getReviewDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/api/reviews/${this.$store.state.review.id}/`,
        headers:{
          Authorization: `Token ${this.$store.state.token}`
        },
      })
        .then((res) => {
          this.review = res.data
        })
        .catch(err => console.log(err))
    },
    getMovieDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/api/movies/${this.$store.state.review.movie}/`,
      })
        .then((res) => {
          this.movie = res.data
          this.movieURL = `https://image.tmdb.org/t/p/w300${res.data.poster_url}`
        })
        .catch(err => console.log(err))
    },
    getUserDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/users/${this.$store.state.review.user}/`,
      })
        .then((res) => {
          this.user = res.data
          this.userId = res.data.id
        })
        .catch(err => console.log(err))
    },
    delReview() {
      if (confirm('정말 삭제하시겠습니까?'))
      axios({
        method: 'delete',
        url: `${API_URL}/api/reviews/${this.$store.state.review.id}/`,
        headers:{
          Authorization: `Token ${this.$store.state.token}`
        },
      })
          .then(res => {
            console.log(res)
            router.push({name: "profile", params: { userId: this.user.id,
            userName: this.user.username }})
          })
          // .catch(err => console.log(err))
    },
    upReview() {
      router.push({
        path:`/update/${this.$store.state.review.id}`,
        params: {review:this.$store.state.review}
      })
    },
    saveWriter() {
      console.log('작성자',this.user)

      const writer = this.user
      this.$store.dispatch('saveWriter', writer)
    },
    getUsers() {
      if (this.isLogin) {
      this.$store.dispatch('getUsers')
    } else {
      alert('로그인하세요')
      this.$router.push({ name:'login'})
    }
  },
  },
  // computed: {
  //   posterUrl () {
  //     console.log(this.movie.poster_url)
  //     console.log(`https://image.tmdb.org/t/p/w300${this.movie.poster_url}`)
  //     return `https://image.tmdb.org/t/p/w300${this.movie.poster_url}`
  //   },
  // }
}
</script>

<style lang="scss">
@import "ReviewDetailView"
</style>