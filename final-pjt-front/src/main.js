import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import GAuth from 'vue-google-oauth2'
import AOS from 'aos';
import "aos/dist/aos.css";

Vue.use(GAuth, {clientId: '217723291634-suk3i1a3n53vn686uiaseags57j1mn6t.apps.googleusercontent.com', scope: 'profile email https://www.googleapis.com/auth/plus.login'})

Vue.use(BootstrapVue)

Vue.config.productionTip = false

new Vue({
  created() {
    AOS.init();
},
  el: '#app',
  router,
  store,
  render: h => h(App)
}).$mount('#app')
