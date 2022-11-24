<template>
  <div id="cmtbox">
    <p>{{ this.user.username }}</p>
    <span
      :to="{
      name:'profile',
      params:{
        // movieId: review.movie,
        // userId: review.user,
        guest: guest.guest,
        owner: guest.owner,
        guestId: guest.id,
      }
    }"
    id="guestcmt">
    {{ guest.content }}
    </span>
    <div v-if="this.user.username == this.$store.state.userName">
      <button @click="delReview">X</button>
    </div>
  </div>
</template>

<script>

import axios from 'axios'
import router from '../router'

const API_URL = 'http://127.0.0.1:8000'


export default {
  name:"GusetItem",
  props:{
    guest: Object,
  },
  data() {
    return {
      user: null,
    }
  },
  created() {
    this.getUserDetail()
  },
  methods:{
    getUserDetail() {
      axios({
        
        method: 'get',
        url: `${API_URL}/accounts/users/${this.guest.guest}/`,
      })
        .then((res) => {
          console.log('guestguggggg',this.guest.guest),
          this.user = res.data
        })
        .catch(err => console.log(err))
    },
    delReview() {
      const a = this.guest.id
      console.log(a)
      if (confirm('정말 삭제하시겠습니까?'))
      axios({
        method: 'delete',
        url: `${API_URL}/api/guests_detail/${this.guest.owner}/${this.guest.guest}/`,
        data:{
          a
        }
      })
          .then(res => {
            console.log(res)
            router.push({path:`/profile/${this.guest.owner}/`})
          })
          .catch(err => console.log(err))
    },

  }
}
</script>

<style lang="scss">
@import "GuestItem";

</style>