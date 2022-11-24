<template>
  <div>
    <div id="surcontainer">
      <p class="title">무VTI</p>
      <section class="buttonArea">
        <div class="buttonRow">
          <div class=mvtiwrap>
          <div class="btn" :class="{selected:eClicked}" @click="eClick">
            <span class="type">D</span>
            <span>다큐멘터리</span>
          </div>
          </div>
          <div class=mvtiwrap>
          <div class="btn" :class="{selected:iClicked}" @click="iClick">
            <span class="type">F</span>
            <span>판타지</span>
          </div>
          </div>
        </div>
        <div class="buttonRow">
          <div class=mvtiwrap>
          <div class="btn" :class="{selected:sClicked}" @click="sClick">
            <span class="type">A</span>
            <span>액션</span>
          </div>
          </div>
          <div class=mvtiwrap>
          <div class="btn" :class="{selected:nClicked}" @click="nClick">
            <span class="type">R</span>
            <span>로맨스</span>
          </div>
          </div>
        </div>
        <div class="buttonRow">
          <div class=mvtiwrap>
          <div class="btn" :class="{selected:tClicked}" @click="tClick">
            <span class="type">C</span>
            <span>코미디</span>
          </div>
          </div>
          <div class=mvtiwrap>
          <div class="btn" :class="{selected:fClicked}" @click="fClick">
            <span class="type">T</span>
            <span>스릴러</span>
          </div>
          </div>
        </div>
        <div class="buttonRow">
          <div class=mvtiwrap>
          <div class="btn" :class="{selected:jClicked}" @click="jClick">
            <span class="type">H</span>
            <span>공포</span>
          </div>
          </div>
          <div class=mvtiwrap>
          <div class="btn" :class="{selected:pClicked}" @click="pClick">
            <span class="type">N</span>
            <span>애니메이션</span>
          </div>
          </div>
        </div>
      </section>
      <div id='btnwrap'>
      <div class="light-button button-wrapper" @click="test">
            <div class="result">
              <span>
                가입하기
              </span>
            </div>  
          </div>
      </div>
    </div>
  </div>
</template>


<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: "SurveyView",

// const app = new Vue({
  //       el: '#app',
  data() {
    return{

    extrovertOrIntrovert : '',
    sensingOrIntuition: '',
    thinkingOrFeeling: '',
    judgingOrPerceiving: '',
    eClicked: false,
    iClicked: false,
    sClicked: false,
    nClicked: false,
    tClicked: false,
    fClicked: false,
    jClicked: false,
    pClicked: false,
    }},

  methods: {
    eClick () {
      this.extrovertOrIntrovert = 'd'
      this.eClicked = true
      this.iClicked = false
    },
    iClick () {
      this.extrovertOrIntrovert = 'f'
      this.iClicked = true
      this.eClicked = false
    },
    sClick () {
      this.sensingOrIntuition = 'a'
      this.sClicked = true
      this.nClicked = false
    },
    nClick () {
      this.sensingOrIntuition = 'r'
      this.nClicked = true
      this.sClicked = false
    },
    tClick () {
      this.thinkingOrFeeling = 'c'
      this.tClicked = true
      this.fClicked = false
    },
    fClick () {
      this.thinkingOrFeeling = 't'
      this.fClicked = true
      this.tClicked = false
    },
    jClick () {
      this.judgingOrPerceiving = 'h'
      this.jClicked = true
      this.pClicked = false
    },
    pClick () {
      this.judgingOrPerceiving = 'n'
      this.pClicked = true
      this.jClicked = false
    },
    test () {
      console.log(this.mbti)
      console.log(this.$store.state.token)
      const mbtiType = this.mbti
      if (mbtiType.length < 4 ) {
        alert('4개의 장르를 선택해 주세요!')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/api/mbti/`,
        headers:{
          Authorization: `Token ${this.$store.state.token}`
        },
        data: {
          mbtiType
        }
      })
        .then(res => {
          this.$store.dispatch('getUserProfile', this.$store.state.userName)
          console.log(res)
        })
        .catch(err => console.log(err))
      // window.location.href = `https://www.16personalities.com/ko/성격유형-${mbtiType}`

    }
  },
  computed: {
    mbti : function () {
      return this.extrovertOrIntrovert + this.sensingOrIntuition + this.thinkingOrFeeling + this.judgingOrPerceiving
    }
  }
}


</script>

<style lang="scss">
@import "SurveyView"
</style>