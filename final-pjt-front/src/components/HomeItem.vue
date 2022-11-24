<template>
  <div>
    <div id="homecontainer">
      <div data-aos="fade-left">
         <router-link
          :to="{
          name: 'movieDetail',
          params: {
            movieId: movie.id}
            // movie: movie}
          }">
          <img id="mainposter" :src="posterUrl" alt="POSTER">
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomeItem",
  props: {
    movie: Object,
  },
  computed: {
    posterUrl () {
      return `https://image.tmdb.org/t/p/original${this.movie.poster_url}`
    }
  },
}
</script>

<style lang="scss">
@import "HomeItem"
</style>