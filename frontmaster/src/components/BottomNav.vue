<template>
  <v-bottom-navigation :value="value" color="teal" grow>
    <router-link :to="{ name: 'Home' }">
      <v-btn>
        <span>Home</span>
        <v-icon>mdi-home</v-icon>
      </v-btn>
    </router-link>

    <router-link :to="{ name: 'CaptureView' }">
      <v-btn>
        <span>Capture</span>
        <v-icon>mdi-camera</v-icon>
      </v-btn>
    </router-link>

    <span v-if="!isLogIn" class="d-flex">
      <router-link :to="{ name: 'Login' }">
        <v-btn>
          <span>Login</span>
          <v-icon>mdi-human</v-icon>
        </v-btn>
      </router-link>
      <router-link :to="{ name: 'Signup' }">
        <v-btn>
          <span>Signup</span>
          <v-icon>mdi-human</v-icon>
        </v-btn>
      </router-link>
    </span>
    <span v-if="isLogIn" class="d-flex">
        <v-btn @click="moveMyPage(currentUserId)">
          <span>My</span>
          <v-icon>mdi-human</v-icon>
        </v-btn>
      <router-link :to="{ name: 'Logout' }">
        <v-btn>
          <span>logout</span>
          <v-icon>mdi-human</v-icon>
        </v-btn>
      </router-link>
        <v-btn @click="moveIllustratedBook(currentUserId)">
          <span>mybook</span>
          <v-icon>mdi-human</v-icon>
        </v-btn>
      <v-btn @click="moveRanking">
        <span>rank</span>
        <v-icon>mdi-format-list-bulleted</v-icon>
      </v-btn>
    </span>
  </v-bottom-navigation>
</template>
<script>
import { mapGetters } from "vuex";
import Login from "@/views/accounts/Login.vue";
import Signup from "@/views/accounts/Signup.vue";
import axios from "@/util/axios";

export default {
  componants: {
    Login,
    Signup
  },
  data() {
    return {
      value: 0,
      currentUserId: ""
    };
  },
  methods: {
    goPhoto() {},

    MoveToLogout() {
      this.$router.push("/logout");
    },
    loadCurrentUserId(token) {
      axios
          .get('api/return/id?authToken=' + token)
          .then((response) => {
            this.currentUserId = response.data.id;
            console.log(this.currentUserId)
          })
          .catch((error) => {
            console.log(error);
          });
    },
    moveMyPage(id){
      this.$router.push('/mypage/' + id);
    },
    moveIllustratedBook(id){
      this.$router.push('/illustratedbook/'+id);
    },
    moveRanking() {
      this.$router.push('/ranking')
    }
  },
  computed: {
    ...mapGetters(["isLogIn"])
  },
  mounted() {
    this.loadCurrentUserId(this.$store.state.authToken);
  }
};
</script>
