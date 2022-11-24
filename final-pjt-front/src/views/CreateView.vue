<template>
  <div class="container">
    <div class = "row">
      <div id="creatediv" class="col" @submit.prevent="createReview">
          <div id="createwrap">
            <p class="title">리뷰 작성</p>
            <label for="title">제목</label>
            <input type="text" id="title" v-model="title">
            <label for="content">내용</label>
            <textarea id="content" rows="10" v-model="content"></textarea>
            <div class="light-button button-wrapper" @click="createReview">
              <div class="button">
                <span>
                  작성
                </span>
              </div>  
            </div>
          </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import router from '../router'
import { authComputed } from '@/store/helpers.js'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: "CreateView",
  data() {
    return {
      userId: null,
      title: null,
      content: null,
      userScore: null,
    }
  },
  created() {
    this.getUsers()
  },
  methods: {
    bindTitle(event) {
      this.title = event.target.value
    },
    bindContent(event) {
      this.content = event.target.value
    },
    bindScore(event) {
      this.userScore = event.target.value
    },
    createReview() {
      const user = this.$store.state.userName
      const movie = this.$route.params.movieId
      const title = this.title
      const content = this.content
      // const userScore = this.userScore

      axios({
        method: 'post',
        url: `${API_URL}/api/reviews/`,
        data: {
          user, movie, title, content, 
        // userScore,  
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
    })
      .then(res => {
        router.push({path:`/movies/${res.data.movie}`, params: {movieId: res.data.movie}})
      })
      .catch(err => console.log(err))
    },
    getUserDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/users/${this.$route.params.userId}/`,
      })
        .then((res) => {
          console.log(res.data)
          this.userId = res.data
        })
        .catch(err => console.log(err))
    },
    getUsers() {
      if (this.isLogin) {
      this.$store.dispatch('getUsers')
    } else {
      alert('로그인하세요!')
      this.$router.push({ name:'login'})
    }
  },
  },
  computed: {
    users() {
      return this.$store.state.users
    },
    ...authComputed,
  },
    //   const payload = {
    //     userId, movieId, title, content, userScore,
    //   }
    //   this.$store.dispatch('createReview', payload)
    // }
  // watch: {
  //   number(val){
  //     const reg = /[ㄱ-ㅎ|ㅏ-ㅣ|가-힣|a-z]/;

  //     if(reg.exec(val)!==null) this.userScore = val.replace(/[^0-9]/g,'');
  //     if(isNaN(parseFloat(val))) this.userScore = '';
  //   }
  // },
}
</script>

<style lang="scss">
@import "CreateView";
</style>