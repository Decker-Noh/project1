<template>
  <div class="container p-0">
    <h5 class="mt-4" style="font-weight:bold;">로그인</h5>
    <form>
      <div class="form-group d-flex justify-content-center mt-4">
        <input
          type="id"
          class="form-control"
          id="exampleInputID1"
          aria-describedby="IDHelp"
          placeholder="아이디"
          v-model="loginData.username"
        />
      </div>
      <div class="form-group d-flex justify-content-center">
        <input
          type="password"
          class="form-control"
          id="exampleInputPassword1"
          placeholder="비밀번호"
          v-model="loginData.password"
        />
      </div>
      <button class="btn btn-primary loginBtn" @click="login">로그인</button>
    </form>
    <br />
  </div>
</template>

<script>
import axios from "@/util/axios";
import { mapActions, mapMutations } from "vuex";

export default {
  data() {
    return {
      loginData: {
        username: null,
        password: null
      }
    };
  },
  computed: {},
  methods: {
    ...mapMutations(["setCookie"]),
    ...mapActions(["getUserInfo"]),
    login() {
      axios
        .post("/api/rest-auth/login/", this.loginData)
        .then(res => {
          console.log(res);
          // Swal.fire({
          //     title: "성공",
          //     text: "로그인이 완료되었습니다.",
          //     icon: 'success',
          //     //confirmButtonText: '확인',
          // });
          console.log(res.headers);
          this.setCookie(res.data.key);
          alert("성공");

          this.$router.push("/");
          window.location.reload();
        })
        .catch(error => {
          console.log(error.response);
          // Swal.fire({
          //     // title: "실패",
          //     text: "아이디 및 비밀번호를 확인 해주세요.",
          //     icon: 'error',
          //     confirmButtonText: '확인',
          // });
          alert("이메일 및 비밀번호를 확인해주세요.");
          // console.log(err.response.data.message);
        });
    }
  }
};
</script>

<style scoped>
/* h1 {
  font-size:3rem
  
} */
input {
  background-color: #f5f5f5;
  width: 80%;
}
.PWQues {
  color: #3498db;
}
.loginBtn {
  background-color: #3498db;
  width: 80%;
}
.loginBtn:hover {
  background-color: #3498db;
}
.divider {
  width: 1px;
  opacity: 0.8;
  background-color: #858f96;
  margin: 0 71px;
  height: 257px;
}
.socialLogin {
  position: relative;
  color: black;
  text-align: center;
  height: 1.5em;
  border: 0px;
  outline: 0px;
  margin: 24px 0px;
}
.socialLogin::before {
  content: "";
  position: absolute;
  top: 50%;
  left: 0px;
  width: 100%;
  border-top: 1px solid rgb(216, 216, 216);
}
.socialLogin::after {
  content: "OR";
  display: inline-block;
  position: relative;
  top: -2px;
  background-color: rgb(255, 255, 255);
  color: rgb(160, 160, 160);
  font-size: 14px;
  font-weight: 400;
  letter-spacing: -0.3px;
  line-height: 19px;
  vertical-align: middle;
  padding: 0px 14px;
}
</style>
