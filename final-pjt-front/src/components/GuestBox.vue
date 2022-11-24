<template>
  <div>
      <GuestCreate
      :guest="guest"/>
    <div v-for="guest in guests"
        :key="guest.id">
      <GuestItem
        v-if="ownerId === guest.owner"
        :guest="guest"
        />
    </div>
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
import GuestItem from '@/components/GuestItem';
import GuestCreate from '@/components/GuestCreate';

export default {
  name: "GuestBox",
  components: {
    GuestItem,
    GuestCreate
  },
  props: {
    ownerId: Number,
  },
  created() {
    this.getGuests()
  },
  methods: {
    getGuests() {
      this.$store.dispatch('getGuests')
    },
  },
  computed: {
    guests() {
      return this.$store.state.guests
    }
  },
}
</script>

<style>
  
</style>