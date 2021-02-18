<template>
  <div>
    <div class="container p-0">
      <!-- <img src="../../assets/title.jpg" alt style="width:70%; height:70%;" /> -->
      <h5 class="mt-4" style="font-weight:bold;">회원가입</h5>
      <!-- <form class="col-6 mx-auto">
      <div class="form-group">
          <v-text-field label="이메일" hide-details="auto" v-model="signupData.email" type="email"></v-text-field>
      </div>
      <div class="form-group">
        <v-text-field v-model="signupData.username" label="아이디" hide-details="auto" type="text" />
      </div>
      <div class="form-group">
        <v-text-field
          v-model="signupData.password1"
          label="비밀번호"
          hide-details="auto"
          type="password"
        />
      </div>
      <div class="form-group">
        <v-text-field
          v-model="signupData.password2"
          label="비밀번호 확인"
          hide-details="auto"
          type="password"
        />
      </div>
      <div class="d-flex justify-content-between">
        <div class="d-flex align-items-center">
          <b-form-checkbox id="checkbox-1" v-model="isTerm" name="checkbox-1" value="accepted">약관동의</b-form-checkbox>
        </div>
        <v-btn rounded outlined color="indigo" @click="check">가입하기</v-btn>
      </div>
      </form>-->
      <form>
        <div class="form-group d-flex justify-content-center mt-4">
          <input
            type="id"
            class="form-control"
            id="exampleInputID1"
            aria-describedby="IDHelp"
            placeholder="아이디"
            v-model="signupData.username"
          />
        </div>
        <div class="form-group d-flex justify-content-center">
          <input
            type="password"
            class="form-control"
            id="exampleInputPassword1"
            placeholder="비밀번호(영문과 숫자 조합으로 8자리이상)"
            v-model="signupData.password1"
          />
        </div>
        <div class="form-group d-flex justify-content-center">
          <input
            type="password"
            class="form-control"
            id="exampleInputPassword2"
            placeholder="비밀번호 확인"
            v-model="signupData.password2"
          />
        </div>
        <button type="button" class="btn btn-primary signupBtn" @click="signup">
          회원가입
        </button>
      </form>
      <br />
    </div>
  </div>
</template>

<script>
import axios from "@/util/axios";
// import SERVER from "@/api/drf"

export default {
  data: () => {
    return {
      signupData: {
        username: "",
        password1: "",
        password2: ""
      }
    };
  },
  methods: {
    check() {
      let checkList = [
        this.signupData.username == "",
        this.signupData.password1 == "",
        this.signupData.password1 != this.signupData.password2
      ];
      let checkMessage = [
        "닉네임을 입력",
        "비밀번호를 입력",
        "비밀번호를 확인",
        "약관에 동의"
      ];

      for (let i = 0; i < 4; i++) {
        if (checkList[i]) {
          alert(checkMessage[i] + "해주세요.");
          return;
        }
      }
      this.signup(this.signupData);
    },
    signup() {
      axios
        .post("/api/rest-auth/signup/", this.signupData)
        .then(() => {
          alert("회원가입이 완료되었습니다.");
          // Swal.fire({
          //     title: "성공",
          //     text: "회원가입이 완료되었습니다.",
          //     icon: 'success',
          //     //confirmButtonText: '확인',
          // });
          this.$router.push("/");
          window.location.reload();
        })
        .catch(err => {
          console.log(err);
          alert("회원가입이 실패하였습니다.");
          // Swal.fire({
          //     // title: "실패",
          //     text: "회원 가입 아이디와 비밀번호를 다시 확인하세요",
          //     icon: 'error',
          //     confirmButtonText: '확인',
          // });
        });
    }
  }
};
</script>

<style scoped>
input {
  background-color: #f5f5f5;
  width: 80%;
}
.PWQues {
  color: #3498db;
}
.signupBtn {
  background-color: #3498db;
  width: 80%;
}
.signupBtn:hover {
  background-color: #3498db;
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
