import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from "@/views/HomeView";
import SignUpView from "@/views/SignUpView";
import LogInView from "@/views/LogInView";
import SocialLogIn from "@/views/SocialLogInView";
import CreateView from "@/views/CreateView";
import SurveyView from "@/views/SurveyView";
import MovieDetailView from "@/views/MovieDetailView";
import ReviewView from "@/views/ReviewView";
import ReviewDetailView from "@/views/ReviewDetailView";
import ProfileView from "@/views/ProfileView";
// import MyPageView from "@/views/MyPageView";
import MyPageSettingsView from "@/views/MyPageSettingsView";
import NotFound from "@/views/NotFound";
import TempMembersView from "@/views/TempMembersView";
import UpdateView from "@/views/UpdateView";


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
    meta: {
      title: "Home",
      authorized: false,
    },
  },
  {
    path: "/signup",
    name: "SignUpView",
    component: SignUpView,
    meta: {
      title: "SignUp",
      authorized: false,
    },
  },
  {
    path: "/login",
    name: "login",
    component: LogInView,
    meta: {
      title: "LogIn",
      authorized: false,
    },
  },
  {
    path: "/sociallogin",
    name: "sociallogin",
    component: SocialLogIn,
    meta: {
      title: "SocialLogIn",
      authorized: false,
    },
  },
  {
    path: "/survey",
    name: "survey",
    component: SurveyView,
    meta: {
      title: "Survey",
      authorized: true,
    },
  },
  {
    path: "/reviews",
    name: "review",
    component: ReviewView,
    meta: {
      title: "Review",
      authorized: true,
    },
  },
  {
    path: "/reviews/:reviewId",
    name: "reviewdetail",
    component: ReviewDetailView,
    meta: {
      title: "ReviewDetail",
      authorized: true,
    },
  },
  {
    path: "/profile/:userId",
    name: "mypage",
    component: ProfileView,
    meta: {
      title: "MyPage",
      authorized: true,
    },
  },
  {
    path: "/mypage/settings",
    name: "settings",
    component: MyPageSettingsView,
    meta: {
      title: "Settings",
      authorized: true,
    },
  },
  {
    path: "/profile/:userId",
    name: "profile",
    component: ProfileView,
    meta: {
      title: "Profile",
      authorized: true,
    },
  },
  {
    path: "/create",
    name: "create",
    component: CreateView,
    meta: {
      title: "Create",
      authorized: true,
    },
  },
  {
    path: "/update/:reviewId",
    name: "update",
    component: UpdateView,
    meta: {
      title: "Update",
      authorized: true,
    },
  },
  {
    path: "/movies/:movieId",
    name: "movieDetail",
    component: MovieDetailView,
    meta: {
      title: "MovieDetail",
      authorized: true,
    },
  },
  {
    path: "/users",
    name: "TempMembersView",
    component: TempMembersView,
    meta: {
      title: "TempMembers",
      authorized: true,
    },
  },
  {
    path: "/404",
    name: "notFound",
    component: NotFound,
  },
  {
    path: "*",
    redirect: "/404",
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
