<template>
  <v-container>
    <v-parallax
        src="https://i.imgur.com/E8qonfe.png"
        class="rounded-lg"
        height="100%"
    >
      <v-row align="center">
        <v-col cols="4">
          <v-avatar size="100">
            <img src="https://i.imgur.com/PWuj14A.png" alt=""/>
          </v-avatar>
        </v-col>
        <v-col cols="8">
          <v-row>
            <v-col cols="3" class="ma-0 pa-1"
            ><span style="color: black; ">아이디</span></v-col
            >
            <v-col cols="9" class="ma-0 pa-1"
            ><span style="color: black; ">{{
                userInfo.username
              }}</span></v-col
            >
          </v-row>
          <v-row>
            <v-col cols="3" class="ma-0 pa-1">
              <span style="color: black; ">이름</span>
            </v-col>
            <v-col cols="9" class="ma-0 pa-1">
              <span style="color: black; ">{{ userInfo.last_name }}&nbsp;</span>
              <span style="color: black; ">{{ userInfo.first_name }}</span>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="3" class="ma-0 pa-1">
              <span style="color: black; ">이메일</span>
            </v-col>
            <v-col cols="9" class="ma-0 pa-1">
              <span style="color: black; ">{{ userInfo.email }}</span>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="3" class="ma-0 pa-1">
              <span style="color: black; ">레벨</span>
            </v-col>
            <v-col cols="9" class="ma-0 pa-1">
              <span style="color: black; ">{{ userInfo.level }}</span>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="3" class="ma-0 pa-1">
              <span style="color: black; ">가입일</span>
            </v-col>
            <v-col cols="9" class="ma-0 pa-1">
              <span style="color: black; ">{{ userInfo.date_joined }}</span>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="3" class="ma-0 pa-1">
              <span style="color: black; ">소개</span>
            </v-col>
            <v-col cols="9" class="ma-0 pa-1">
              <span style="color: black; ">{{ userInfo.introduction }}</span>
            </v-col>
          </v-row>
          <v-row>
            <v-spacer></v-spacer>
            <v-btn right small color="error" class="ma-4" @click="moveModify"
                   v-if="userInfo.id == this.currentUserId">수정하기
            </v-btn
            >
          </v-row>
        </v-col>
      </v-row>
    </v-parallax>
  </v-container>
</template>

<script>
import axios from "@/util/axios";

export default {
  name: "MyPage",
  data() {
    return {
      userInfo: {},
      currentUserId: ""
    };
  },

  mounted() {
    this.loadUserInfo();
    this.loadCurrentUserId(this.$store.state.authToken)
  },
  methods: {
    loadUserInfo() {
      axios
          .get('api/return/userinfo?id=' + this.$route.params.id)
          .then((response) => {
            this.userInfo = response.data.userInfo;
          })
          .catch((error) => {
            alert(error);
          });
    },
    moveModify() {
      this.$router.push("/modify");
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
    }
  }
};
</script>
<style scoped></style>
