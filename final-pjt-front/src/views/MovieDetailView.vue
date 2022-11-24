<template>
  <div id="moviecontainer">
    <div class="upper">
      <section id="pstsection">
        <img id="poster" :src="movieUrl" alt="POSTER">
      </section>
      <aside>
        <MovieDetailContents />
          <router-link
          :to="{
            name: 'create',
            params: {
              movieId: this.$route.params.movieId
            }
          }">
            <div class="light-button button-wrapper">
              <div class="button">
                <span>
                  + Review
                </span>
              </div>  
            </div>
          </router-link>
      </aside>
    </div>
    <section id="moviereview">
      <div class="empty">
      </div>
      <div id="reviewitem">
        <div v-for="review in reviews"
            :key="review.id"
            >
          <ReviewItem
            v-if="review.movie === movieId"
            :review="review"
            style="margin-right:16px"
            />
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
import MovieDetailContents from '@/components/MovieDetailContents';
import ReviewItem from '@/components/ReviewItem';

export default {
  name: "MovieDetailView",
  components: {
    MovieDetailContents,
    ReviewItem,
  },
  data() {
    return {
      movieUrl: null,
      movieId: null
    }
  },
  created() {
    this.getMovieDetail()
    this.getReviews()
  },
  methods: {
    getMovieDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/api/movies/${this.$route.params.movieId}/`,
      })
        .then((res) => {
          this.movieUrl = `https://image.tmdb.org/t/p/original${res.data.poster_url}`
          this.movieId = res.data.id
        })
        .catch(err => console.log(err))
    },
    getReviews() {
      this.$store.dispatch('getReviews')
    }
  },
  computed: {
    reviews() {
      return this.$store.state.reviews
    }
  },
}
</script>

<style lang="scss">
@import "MovieDetailView";
</style>