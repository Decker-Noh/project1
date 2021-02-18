<template>
  <v-parallax
      src="https://i.imgur.com/E8qonfe.png"
      class="rounded-lg ma-3 pa-1"
      height="100%"
  >
    <v-row align="center">
      <v-col cols="4">
        <v-avatar size="100">
          <img src="https://i.imgur.com/PWuj14A.png" alt=""/>
        </v-avatar>
      </v-col>
      <v-col cols="8">
        <v-row class="ma-0 pa-0">
          <v-text-field label="ID" :value="userInfo.username" readonly filled dense></v-text-field>
        </v-row>
        <v-row class="ma-0 pa-0">
          <v-text-field label="이메일" :value="userInfo.email" clearable dense></v-text-field>
        </v-row>
        <v-row class="ma-0 pa-0">
          <v-col cols="5" class="my-0 pa-0 ml-0 mr-2">
            <v-text-field v-model="userInfo.last_name" label="성" dense></v-text-field>
          </v-col>
          <v-col cols="6" class="ma-0 pa-0">
            <v-text-field v-model="userInfo.first_name" label="이름" dense></v-text-field>
          </v-col>
        </v-row>
        <v-row>
          <v-col class="py-0">
            <v-text-field
                v-model="password"
                :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                :type="show1 ? 'text': 'password'"
                label="비밀번호"
                @click:append="show1 = !show1" dense></v-text-field>
          </v-col>
        </v-row>
        <v-row>
          <v-col class="py-0">
            <v-text-field
                v-model="newPassword"
                :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
                :type="show2 ? 'text': 'password'"
                label="새로운 비밀번호"
                @click:append="show2 = !show2" dense></v-text-field>
          </v-col>
        </v-row>
        <v-row>
          <v-col class="py-0">
            <v-text-field
                :append-icon="show3 ? 'mdi-eye' : 'mdi-eye-off'"
                :rules="[rules.newPasswordRule]"
                :type="show3 ? 'text': 'password'"
                label="새로운 비밀번호 확인"
                value=""
                @click:append="show3 = !show3" dense></v-text-field>
          </v-col>
        </v-row>
        <v-row class="">
          <v-textarea
              label="소개"
              v-model="userInfo.introduction"
              background-color="transparent"
              auto-grow
          ></v-textarea>
        </v-row>
        <v-row>
          <v-btn left small color="primary" class="ma-4" @click="goBack">뒤로가기</v-btn>
          <v-spacer></v-spacer>
          <v-btn right small color="error" class="ma-4" @click="modify">수정하기</v-btn>
        </v-row>
      </v-col>
    </v-row>
  </v-parallax>
</template>

<script>
// import axios from "@/util/axios";

let dummyUserInfo = {
  id: "1",
  password: "12",
  last_login: "",
  is_superuser: true,
  username: "admin",
  first_name: "SSAFY",
  last_name: "KIM",
  email: "ssafy@ssafy.com",
  is_staff: true,
  date_joined: "2020년 9월 14일",
  level: 5,
  introduction: "안녕하세요. 간단한 소개를 남길 수 있는 공간입니다."
};

export default {
  name: "Modify",
  data() {
    return {
      userInfo: {},
      password: "",
      newPassword: "",
      show1: false,
      show2: false,
      show3: false,
      rules: {
        newPasswordRule: value => value == this.newPassword || ('새 비밀번호가 일치하지 않습니다.')
      }
    }
  },
  mounted() {
    this.loadUserInfo();
  },
  methods: {
    loadUserInfo() {
      this.userInfo = dummyUserInfo;
      //  추후 api가 나오면 axios를 통한 비동기 통신으로 교체.
    },
    goBack() {
      this.$router.go(-1);
    },
    modify() {
      // 비밀번호가 일치하는지 확인
      if (this.userInfo.password == this.password) {
        // 새 비밀번호가 있다면
        if (this.newPassword != '') {
          this.userInfo.password = this.password;
        }
        // 비밀번호가 일치하고 정보 수정이 완료되면, mypage로
        this.$router.push("/mypage");
      } else {
        alert("비밀번호가 일치하지 않습니다.");
      }
    }
  },
}
</script>

<style scoped>

</style>