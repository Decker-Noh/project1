import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";

// 잡기
import CaptureView from "@/views/Capture/CaptureView";

import Signup from "../views/accounts/Signup.vue";
import Login from "../views/accounts/Login.vue";
import Logout from '../views/accounts/Logout.vue';
// 내 정보 페이지
import MyPage from "@/views/MyPage/MyPage";
import Captured from "@/views/IllustratedBook/Captured";
import Modify from "@/views/MyPage/Modify";

// 도감 페이지
import IllustratedBook from "@/views/IllustratedBook/IllustratedBook";

//랭킹
import Ranking from "@/views/Ranking";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue")
  },
  {
    path: "/mypage/:id",
    name: "MyPage",
    component: MyPage
  },
  {
    path: "/modify",
    name: "Modify",
    component: Modify
  },
  {
    path: "/captured",
    name: "Captured",
    component: Captured,
    props: true
  },
  // 사진찍기
  {
    path: "/capture",
    name: "CaptureView",
    component: CaptureView
  },
  {
    path: "/illustratedbook/:id",
    name: "IllustratedBook",
    component: IllustratedBook
  },
  {
    path: "/accounts/signup",
    name: "Signup",
    component: Signup
  },
  {
    path: "/accounts/login",
    name: "Login",
    component: Login
  },
  {
    path: "/logout",
    name: "Logout",
    component: Logout
  },
  {
    path: "/ranking",
    name: "Ranking",
    component: Ranking
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
