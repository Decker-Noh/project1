import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import axios from "axios";
import VueCookies from "vue-cookies";

Vue.config.productionTip = true;
Vue.use(VueCookies);
Vue.prototype.$axios = axios;

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount("#app");
