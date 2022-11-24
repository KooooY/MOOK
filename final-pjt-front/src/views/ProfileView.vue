<template>
  <div id="profilecontainer">
      <div id="profileupper">
        <div id="personalinfo">
          <p v-if="this.$store.state.writer.username == this.$store.state.userName">안녕하세요, {{this.$store.state.writer.username}}님!</p>
          <p v-else>{{this.$store.state.writer.username}}님의 프로필</p>
          <div v-if="this.$store.state.writer.username == this.$store.state.userName">
            <router-link to="/mypage/settings">프로필 수정하기</router-link>
          </div>
          <div v-else>
            <button v-if="!follow_bool" @click= follow>
              + FOLLOW
            </button>
            <button v-if="follow_bool" @click = follow>
              - UNFOLLOW
            </button>
          </div>
          
          <div id="followcnt">
            <p>팔로우 {{followerCount}}명</p>
            <p>팔로잉 {{followingCount}}명</p>
          </div>
        </div>
        <div id="personalcomment">
          <GuestBox
            :ownerId="userId"/>
        </div>
      </div>
      <div id="personalarticle">
        <div class="empty">
        </div>
        <div id="reviews">
          <div v-for="review in reviews"
            :key="review.id">
            <ReviewCard
            v-if="review.user === userId"
            :review="review"
            id="reviewcards"
            style="margin-right:16px"
            />
          </div>
        </div>
      </div>
  </div>
</template>

<script>
import ReviewCard from '@/components/ReviewCard'
import GuestBox from '@/components/GuestBox'
import { authComputed } from '@/store/helpers.js'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: "ProfileView",
  computed: {
    ...authComputed,
    reviews() {
      return this.$store.state.reviews
    },
    users() {
      return this.$store.state.users
    },
    // guests() {
    //   return this.$store.state.guests
    // }
  },
  components: {
    ReviewCard,
    GuestBox
  },

  data() {
    return{
      userId: null,
      followerCount:null,
      followingCount:null,
      follow_bool:null,
    }
  },
  created() {
    // this.isMyProfile()
    this.getReviews()
    this.getUserId()
    this.countFollow()
    this.getUsers()
    // this.getGuests()
  },
  methods: {
    // isMyProfile() {
    //   if (this.$route.params.userName == this.$store.state.userName) {
    //     this.$router.push({ name:'mypage'})
    //   }
    // },
    follow() {
      // console.log(this.$route.params)
      // const userId = this.$store.state.userId
      axios({
        method: 'post',
        url: `${API_URL}/accounts/${this.$store.state.writer.id}/follow/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
      }).then(res =>(
      console.log(res),
      this.countFollow()      
      ))      
    },
    countFollow() {
      const userId = this.$store.state.userId
      console.log(userId)
      console.log(this.$store.state.writer.id)
      axios({
        method:'post',
        url: `${API_URL}/accounts/follow/${this.$store.state.writer.id}/`,
        data:{
          userId
        }
      }).then((res =>(
        console.log(res.data),
        this.followerCount= res.data['followers_count'],
        this.followingCount=res.data['followings_count'],
        this.follow_bool = res.data['follow_bull']
      ))
      )
    },
    getReviews() {
      this.$store.dispatch('getReviews')
    },
    // getGuests() {
    //   this.$store.dispatch('getGuests')
    // },
    getUserId() {
      this.userId = this.$store.state.writer.id
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
}

</script>

<style lang="scss">
@import "ProfileView";
</style>