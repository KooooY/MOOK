<template>
  <div id="prime">
    <div id="randomMovie" >
      <router-link
          :to="{
          name: 'movieDetail',
          params: {
            movieId: randomMovie.id}
          }">
          <img id="randomposter" data-wow-delay="0.1s" style="visibility: visible; -webkit-animation-delay: 0.1s; -moz-animation-delay: 0.1s; animation-delay: 0.1s;"
          :src="randomMovieUrl" alt="POSTER">
      </router-link>
      <div id="moviedetail">
        <p id="movietitle">{{ randomMovie.title }}</p>
        <p id="movieoverview">{{ randomMovie.overview }}</p>
      </div>
    </div>
    <!-- <div id="sec1" data-aos="fade">
	<h1>웹 개발자 김정훈입니다.</h1>
    </div> -->
    <div>
      <div v-if="isLogin">
        <p class="recomtext">{{this.$store.state.userName}}님의 무VTI 기반 추천 영화!</p>
        <div id="home-container">
          <div id="test-slide" class="swiper-container">
            <ul class="swiper-wrapper">
              <li class="swiper-slide" 
                v-for="mbtiMovie in mbtiMovies"
                :key="mbtiMovie.id">
                <HomeItem 
                :movie="mbtiMovie"
                id="movieitem" data-wow-delay="0.1s" style="visibility: visible; -webkit-animation-delay: 0.1s; -moz-animation-delay: 0.1s; animation-delay: 0.1s;"
                />
              </li>
            </ul>
          </div>
          <div class="pagination"></div>
          <div class=".swiper-button-next" style="z-index: index 2000;">o</div>
          <div class=".swiper-button-prev">o</div>
        </div>
      </div>
      <div v-else>
        <p class="recomtext">Guest 영화 추천</p>
        <div id="home-container">
          <HomeItem 
            v-for="movie in movies"
            :key="movie.id"
            :movie="movie"
            id="movieitem" data-wow-delay="0.1s" style="visibility: visible; -webkit-animation-delay: 0.1s; -moz-animation-delay: 0.1s; animation-delay: 0.1s;"
            />
        </div>
      </div>
    </div>  
    <p class="recomtext">2번 라인</p>
    <div id="home-container">
        <HomeItem 
        v-for="movie in movies"
        :key="movie.id"
        :movie="movie"
        id="movieitem" data-wow-delay="0.1s" style="visibility: visible; -webkit-animation-delay: 0.1s; -moz-animation-delay: 0.1s; animation-delay: 0.1s;"
        />
    </div>
    <p class="recomtext">3번 라인</p>
    <div id="home-container">
        <HomeItem 
        v-for="movie in movies"
        :key="movie.id"
        :movie="movie"
        id="movieitem" data-wow-delay="0.1s" style="visibility: visible; -webkit-animation-delay: 0.1s; -moz-animation-delay: 0.1s; animation-delay: 0.1s;"
        />
    </div>
  </div>
</template>

<script src="https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.20/lodash.min.js"></script>
<script>
import HomeItem from '@/components/HomeItem';
import _ from "lodash"
import axios from 'axios'
import { authComputed } from '@/store/helpers.js'
 import Swiper from 'swiper';

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: "HomeView",
  components: {
    HomeItem,
  },
  data() {
    return {
      randomMovie: null,
      randomMovieUrl: null,
      mbtiMovies: null,
    }
  },
  created() {
    this.$store.dispatch('getMovies')
    this.$store.dispatch('getMbtis')
    this.getRandomMovie()
    this.getMbtiMovie()
  },
  methods: {
    getRandomMovie() {
      const randomMovie = _.sample(this.movies)
      this.randomMovie = randomMovie
      this.randomMovieUrl = `https://image.tmdb.org/t/p/original${randomMovie.poster_url}`
    },
    getMbtiMovie() {
      axios({
        method: 'get',
        url: `${API_URL}/api/mbti/${this.$store.state.userId}`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
      })
      .then((res) => {
          console.log('성공',res)
          this.mbtiMovies = res.data
        })
        .catch(err => console.log('에러',err))
    },
    getUsers() {
      if (this.isLogin) {
      this.$store.dispatch('getUsers')
    } else {
      alert('로그인하세요!')
      this.$router.push({ name:'login'})
    }
  },
    clearState() {
      this.$store.dispatch('clearState')
    },
  },
  computed: {
    movies() {
      return this.$store.state.movies
    },
    users() {
      return this.$store.state.users
    },
    ...authComputed,
    // mbtis() {
    //   return this.$store.state.mbtis
    // }
  },
}

const slide = new Swiper('#test-slide', {
  // 다양한 옵션 설정, 
  // 아래에서 설명하는 옵션들은 해당 위치에 들어갑니다!!
  slidesPerView : 6,
  spaceBetween : 6,
  loop: true,
  observer: true,
  observeParents: true,
  pagination : {   // 페이저 버튼 사용자 설정
  el : '.pagination',  // 페이저 버튼을 담을 태그 설정
  clickable : true,
  },
  navigation: {   // 버튼
          nextEl: ".swiper-button-next",
          prevEl: ".swiper-button-prev",
        },
      });
//     // 버튼 클릭 여부
//   type : 'bullets', // 버튼 모양 결정 "bullets", "fraction" 
//   renderBullet : function (index, pagination) {  // className이 기본값이 들어가게 필수 설정
//     return '<a href="#" class="' + pagination + '">' + (index + 1) + '</a>'
//   },
//   renderFraction: function (currentClass, totalClass) { // type이 fraction일 때 사용
//     return '<span class="' + currentClass + '"></span>' +
//            '<span class="' + totalClass + '"></span>';
//   }
// }})
</script>



<style lang="scss">
@import "HomeView" 
</style>