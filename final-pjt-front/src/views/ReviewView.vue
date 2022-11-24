<template>
  <div>
    난 ReviewView
    <ReviewItem
      v-for="review in reviews"
      :key="review.id"
      :review="review"
      />
  </div>
</template>

<script>
import ReviewItem from '@/components/ReviewItem';

export default {
  name: "ReviewView",
  components: {
    ReviewItem,
  },
  created() {
    this.getReviews()
  },
  methods: {
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

<style>

</style>