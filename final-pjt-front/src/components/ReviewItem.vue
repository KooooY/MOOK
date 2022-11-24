<template>
  <div id="reviewcontainer">
    <router-link
      :to="{
      name:'reviewdetail',
      params:{
        // movieId: review.movie,
        // userId: review.user,
        review: review,
        reviewId: review.id,
      }
    }"
    style="text-decoration:none;">
    <div id="reviewbox" @click="saveReview">
      <p id="reviewboxtitle">{{ review.title }}</p>
      <p id="reviewboxcontent" v-if="isLogin">{{ review.content }}</p>
    </div>
    </router-link>
  </div>
</template>

<script>
import { authComputed } from '@/store/helpers.js'

export default {
  name:"ReviewItem",
  props:{
    review: Object,
  },
  methods:{
    saveReview() {
      console.log('나실행됨')
      const review = this.review
      this.$store.dispatch('saveReview', review)
    }
  },
  computed: {
    ...authComputed,
  },
}
</script>

<style lang="scss">
@import "ReviewItem";

</style>