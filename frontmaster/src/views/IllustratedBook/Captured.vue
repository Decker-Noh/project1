<template>
  <v-container>
    <v-parallax
      src="https://i.imgur.com/E8qonfe.png"
      class="rounded-lg"
      height="100%"
    >
      <v-row class="mt-1">
        <v-col align="center">
          <v-img
            class="rounded-lg"
            src="https://i.imgur.com/O6JUzra.jpg"
            width="160"
          />
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="2" class="ma-0 pa-1" align="center">
          <span style="color: black">이름</span>
        </v-col>
        <v-col cols="10" class="ma-0 pa-1" align="center">
          <span style="color: black">{{ captured.name }}</span>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="2" class="ma-0 pa-1" align="center">
          <span style="color: black">포획일</span>
        </v-col>
        <v-col cols="10" class="ma-0 pa-1" align="center">
          <span style="color: black">{{ captured.created_at }}</span>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="2" class="ma-0 pa-1" align="center">
          <span style="color: black">설명</span>
        </v-col>
        <v-col cols="10" class="ma-0 pa-1" align="center">
          <span style="color: black">{{ captured.info }}</span>
        </v-col>
      </v-row>
      <v-row>
        <v-btn left small color="primary" class="ma-4" @click="goBack"
          >뒤로가기</v-btn
        >
        <v-spacer></v-spacer>
        <!--        추후에 본인일 때만 버튼 활성화할 수 있게 해야함.-->
        <v-btn
          right
          small
          color="error"
          class="ma-4"
          @click="letFree(captured.id)"
          >놓아주기</v-btn
        >
      </v-row>
    </v-parallax>
  </v-container>
</template>

<script>
import axios from "@/util/axios";

export default {
  name: "Captured",
  data() {
    return {
      captured: {},
      animalInfo: {}
    };
  },
  mounted() {
    this.loadCaptured();
  },
  methods: {
    loadCaptured() {
      this.captured = this.$route.params;
    },
    goBack() {
      this.$router.go(-1);
    },
    letFree(id) {
      axios
        .delete("animals/post_list/" + id)
        .then(() => {
          alert("풀어주었습니다!");
          this.$router.go(-1);
        })
        .catch(error => {
          alert(error);
        });
    }
  }
};
</script>

<style scoped></style>
