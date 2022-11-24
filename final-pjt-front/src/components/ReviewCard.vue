<template>
  <div>
    <div id="posetercard">
      <router-link
        :to="{
        name:'reviewdetail',
        params:{
          // movieId: review.movie,
          // userId: review.user,
          review: review,
          reviewId: review.id,
        }
      }">
        <img id="reviewposter" :src="movieUrl" alt="POSTER" @click="saveReview">
      </router-link>
      <div id="carddetail">
        <p id="reviewtitle">{{ review.title }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name:"ReviewCard",
  props:{
    review: Object,
  },
  data(){
    return{
      movie: null,
      movieUrl: null,
    }
  },
  created() {
    this.getMovieDetail()
  },
  methods:{
    getMovieDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/api/movies/${this.review.movie}/`,
      })
        .then((res) => {
          this.movie = res.data
          this.movieUrl = `https://image.tmdb.org/t/p/w300${res.data.poster_url}`
        })
        .catch(err => console.log(err))
    },
    saveReview() {
      console.log('나실행됨')
      const review = this.review
      this.$store.dispatch('saveReview', review)
    }
  },
}
</script>

<style lang="scss">
@import "ReviewCard"
</style>