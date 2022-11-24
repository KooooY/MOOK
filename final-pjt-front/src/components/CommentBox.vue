<template>
  <div>
    <div v-for="comment in comments"
        :key="comment.id">
      <CommentItem
        v-if="review.id === comment.review"
        :comment="comment"
        />
    </div>
      <CommentCreate/>
    <!-- <CommentItem
      v-for="comment in comments"
      :key="comment.id"
      :comment="comment"
      />
    <div>
      <CommentCreate/>
    </div> -->
  </div>
</template>

<script>
import CommentItem from '@/components/CommentItem';
import CommentCreate from '@/components/CommentCreate';

export default {
  name: "CommentBox",
  components: {
    CommentItem,
    CommentCreate
  },
  props: {
    review: Object
  },
  created() {
    this.getComments()
  },
  methods: {
    getComments() {
      this.$store.dispatch('getComments')
    },
  },
  computed: {
    comments() {
      return this.$store.state.comments
    }
  },
}
</script>

<style>

</style>