<template>
  <div>
    난 MyPageView
    <div v-if="isLogin">
      <router-link to="/mypage/settings">프로필 수정하기</router-link>
      <router-view></router-view>
      <div class="container">
        <div class="row">
          <section id="personalinfo" class="col-3">
            여기 프사랑 개인정보 넣을거야
          </section>
          <aside id="personalarticle" class="col-9">
            여기는 감상평 넣을거야
          </aside>
        </div>
      </div>
    </div>
    <div v-else>
      <p>로그인하세요</p>
      <router-link to="/login">LogIn</router-link>
    </div>
  </div>
</template>

<script>
import { authComputed } from '@/store/helpers.js'

export default {
  name: "MyPageView",
  computed: {
    ...authComputed
  },
  data() {
    return{
      user: null
    }
  },
  created() {
  }

}

</script>

<style>
#personalinfo {
  outline: 1px solid black;
}
#personalarticle {
  outline: 1px solid black;
}

</style>