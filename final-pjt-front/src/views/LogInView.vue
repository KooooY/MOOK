<template>
  <div class="container">
    <div class = "row">
        <div id="logindiv" class="col" @submit.prevent="logIn">
          <div id="loginwrap">
            <p class="title">LOGIN</p>
            <label for="username">username</label>
            <input type="text" id="username" v-model="username">
            <label for="password">password</label>
            <input type="password" id="passwor1" v-model="password">
            <div class="light-button button-wrapper" @click="logIn">
                <div class="button">
                  <span>
                    LOGIN
                  </span>
                </div>  
              </div>
          </div>
          <hr>
          <div id="another">
            <p>아이디가 없으신가요?</p>
            <!-- <a class="social" @click="GoogleLoginBtn">구글 계정으로 계속하기</a>
            <div id="my-signin2" style="display: none"></div> -->
            <!-- <div class="g-signin2" data-onsuccess="onSignIn"></div> -->
            <!-- <br> -->
            <router-link to="/signup">
              <div class="light-button button-wrapper">
                <div class="button">
                  <span>
                    일반회원 가입하기
                  </span>
                </div>  
              </div>
            </router-link>
            <br>
          </div>
        </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LogInView",
  data() {
    return {
      username: null,
      password: null,
      googleUser: null,
    }
  },
  methods: {
    logIn() {
      const username = this.username
      const password = this.password

      const payload = {
        username, password,
      }
      this.$store.dispatch('logIn', payload)
      // this.$store.dispatch('getUserProfile', payload)
    },
    GoogleLoginBtn() {
      // var self = this;
      window.gapi.signin2.render('my-signin2', {
        scope: 'profile email',
        width: 240,
        height: 50,
        longtitle: true,
        theme: 'dark',
        // onsuccess: this.GoogleLoginSuccess,
        // onfailure: this.GoogleLoginFailure,
        onsuccess: this.onSuccess,
        onfailure: this.onFailure,
      });
    },
  
    onSuccess(googleUser) {
      console.log(googleUser)
      this.googleUser = googleUser.getBasicProfile();
    },
    onFailure(error) {
      // eslint-disable-next-line
      console.log(error);
    },

  //     setTimeout(function () {
  //       if (!self.googleLoginCheck) {
  //         const auth = window.gapi.auth2.getAuthInstance();
  //         auth.isSignedIn.get();
  //         document.querySelector('.abcRioButton').click();
  //       }
  //     }, 1500)

  //   },
  //   async GoogleLoginSuccess(googleUser) {
  //     const googleEmail = googleUser.getBasicProfile().getEmail();
  //     if (googleEmail !== 'undefined') {
  //       console.log(googleEmail);
  //     }
  //   },
  //   //구글 로그인 콜백함수 (실패)
  //   GoogleLoginFailure(error) {
  //     console.log(error);
  //   },
  },
}
</script>

<style lang="scss">
@import "LogInView";
</style>