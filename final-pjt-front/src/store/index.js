import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'
import axios from 'axios'
import router from '../router'

const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    token: null,
    userName: null,
    movies:null,
    userId: null,
    mbtis: null,
    review: null,
    writer: null,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    },
  },
  mutations: {
    GET_MBTIS(state, mbtis) {
      state.mbtis = mbtis
    },
    GET_MOVIES(state, movies) {
      state.movies = movies
    },
    GET_USERS(state, users) {
      state.users = users
    },
    GET_REVIEWS(state, reviews) {
      state.reviews = reviews
    },
    GET_COMMENTS(state, comments) {
      state.comments = comments
    },
    GET_GUESTS(state, guests) {
      state.guests = guests
    },
    SIGN_UP(state, token) {
      state.token = token
    },
    SAVE_TOKEN(state,userData){
      state.token = userData.token
      state.userName = userData.username
      // this.dispatch('getUserProfile', state.userName)
    },
    GET_USER(state, userId){
      state.userId = userId
      router.push({name: "profile", params: {userId: userId, userName: state.userName}})
    },
    LOGOUT(state){
      state.token = null
      state.userName = null
      state.userId = null
      localStorage.removeItem('token')
      localStorage.removeItem('userName')
      localStorage.removeItem('userId')
      location.reload();
    },
    CLEAR_STATE(state){
      state.review = null
      state.writer = null
    },
    SAVE_REVIEW(state, review){
      state.review = review
    },
    SAVE_WRITER(state, writer){
      state.writer = writer
      console.log(state.writer)
    },
  },
  actions: {
    getMbtis(context){
      // const userId = this.$store.state.userId
      // console.log(this.$store.state.userId)
      axios({
        method: 'get',
        url: `${API_URL}/api/mbti/`,
        headers: {
          Authorization: `Token ${ context.state.token }`
        },
      })
        .then(res => {
          console.log('난',res.data),          
          context.commit('GET_MBTIS', res.data)})
        .catch(err => console.log(err))
    },
    getMovies(context) {
      // console.log(this.$store.state.userId)
      axios({
        method: 'get',
        url: `${API_URL}/api/movies/`,
      })
        .then(res =>
          context.commit('GET_MOVIES', res.data))
        .catch(err => console.log(err))
    },
    getUsers(context) {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/users/`,
        headers: {
          Authorization: `Token ${ context.state.token }`
        },
      })
        .then(res => {
          context.commit('GET_USERS', res.data)
        })
        .catch(err => console.log(err))
    },
    getReviews(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/reviews/`,
        headers: {
          Authorization: `Token ${ context.state.token }`
        },
      })
        .then(res => {
          console.log(res.data)
          context.commit('GET_REVIEWS', res.data)
        })
        .catch(err => console.log(err))
    },
    getGuests(context) {
      axios({
        method:'get',
        url: `${API_URL}/api/guests/`,
        headers: {
          Authorization: `Token ${ context.state.token }`
        },
      })
        .then(res => {
          console.log(res.data)
          context.commit('GET_GUESTS', res.data)
        })
        .catch(err => console.log(err))
    },
    getComments(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/comments/`,
        headers: {
          Authorization: `Token ${ context.state.token }`
        },
      })
        .then(res => {
          console.log(res.data)
          context.commit('GET_COMMENTS', res.data)
        })
        .catch(err => console.log(err))
    },
    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2
    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2
      }
    })
      .then(res => {
        console.log(res)
        const username = JSON.parse(res.config.data).username
        const token = res.data.key
        const userData = {
          username,
          token
        }
        context.commit('SAVE_TOKEN', userData)
        router.push({path:'/survey'})
      })
      .catch(err => {
        console.log(err)
        alert('입력 내용을 확인하세요')
      })
    },
    logIn(context, payload) {
      const username = payload.username
      const password = payload.password
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password,
      }
    })
      .then(res => {
        const username = JSON.parse(res.config.data).username
        const token = res.data.key
        const userData = {
          username,
          token
        }
        context.commit('SAVE_TOKEN', userData)
      })
      .then(res=> {
        console.log(res)
        this.dispatch('getUserProfile', username)
      })
      .catch(err => {
        console.log(err)
        alert('아이디와 비밀번호를 확인하세요.')
      })
    },
    logout({commit}) {
      commit('LOGOUT')
    },
    clearState({commit}) {
      commit('CLEARSTATE')
    },
    getUserProfile(context, payload) {
      const username = payload
      console.log(username)
      axios({
        method: 'get',
        url: `${API_URL}/accounts/profile/${username}`,
        headers: {
          Authorization: `Token ${ context.state.token }`
        },
      })
        .then(res => {
          console.log(res)
          const userId = res.data.id
          context.commit('GET_USER', userId)
        })
        .catch(err => console.log(err))
    },
    saveReview(context, payload) {
      console.log('리뷰저장',payload)
      context.commit('SAVE_REVIEW', payload)
    },
    saveWriter(context, payload) {
      console.log('작성자저장',payload)
      context.commit('SAVE_WRITER', payload)
    },


    createReview(context, payload) {
      const user = payload.userId
      const movie = payload.movieId
      const title = payload.title
      const content = payload.content
      // const userScore = payload.userScore
    axios({
      method: 'post',
      url: `${API_URL}/api/reviews/`,
      data: {
        user, movie, title, content, 
        // userScore
      }
    })
      .then(res => {
        console.log(res)
        // const username = JSON.parse(res.config.data).username
        // const token = res.data.key
        // const userData = {
        //   username,
        //   token
        // }
        // context.commit('SAVE_TOKEN', userData)
      })
      .catch(err => console.log(err))
    },
    // createComment(context, payload) {
    //   const user = payload.userId
    //   const review = payload.reviewId
    //   const content = payload.content
    //   // const userScore = payload.userScore
    // axios({
    //   method: 'post',
    //   url: `${API_URL}/api/reviews/`,
    //   data: {
    //     user, movie, title, content, 
    //     // userScore
    //   }
    // })
    //   .then(res => {
    //     console.log(res)
    //     // const username = JSON.parse(res.config.data).username
    //     // const token = res.data.key
    //     // const userData = {
    //     //   username,
    //     //   token
    //     // }
    //     // context.commit('SAVE_TOKEN', userData)
    //   })
    //   .catch(err => console.log(err))
    // },
  },
  modules: {
  }
})
