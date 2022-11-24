<template>
  <div>
    <div id=content>
      <p id="movie_title">{{movie?.title}}</p>
      <p>개봉 {{ movie?.release_date}}</p>
      <p>전체평점 {{ movie?.tmdb_score}}</p>
      <p>줄거리</p>
      <p id="movie_overview">{{ movie?.overview}}</p>
      <br>
      <div id="likeheart">
        <img src="https://upload.wikimedia.org/wikipedia/commons/3/35/Emoji_u2665.svg" alt="My Image"
        v-if="like_bool" @click = like class="heartimg">
        <img src="https://upload.wikimedia.org/wikipedia/commons/3/35/Emoji_u2665.svg" alt="My Image"
        v-if="!like_bool" @click = like class="heartimg">
        <span>{{likes}}</span>
      <!-- <button v-if="like_bool" @click = like>좋아요 취소</button>
      <button v-if="!like_bool" @click = like>좋아요</button> -->
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieDetailContents',
  data() {
    return{
      movie: null,
      likes:null,
      like_bool:null
    }
  },
  created() {
    this.getMovieDetail()
    this.likeShow()
  },
  methods: {
    getMovieDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/api/movies/${this.$route.params.movieId}/`,
      })
        .then((res) => {
          this.movie = res.data
        })
        .catch(err => console.log(err))
    },

    like() {
      // const userId = this.$store.state.userId
      axios({
        method: 'post',
        url: `${API_URL}/api/movies/${this.$route.params.movieId}/like/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
      }).then(res => (
        console.log(res.data),
        this.likeShow()
      ))
      
    },
    likeShow() {
      const userId = this.$store.state.userId
      // const userId = this.$route.params.userId
      console.log(this.$store.state.userId)      
      axios({
        method: 'post',
        url: `${API_URL}/api/like/${this.$route.params.movieId}/`,
        data:{
          userId
        }
      }).then(res => (
        console.log(res.data),
        // console.log(this.$store.state.userId),
        this.likes = res.data['likes_count'],
        this.like_bool=res.data['like_bool']

      ))
    }
  },
}
</script>

<style lang="scss">
@import "MovieDetailContents";
</style>