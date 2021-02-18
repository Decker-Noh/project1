<template>
  <v-container>
    <h1 style="text-align: center">📓 도감 📓</h1>
    <br/>
    <v-parallax
        src="https://i.imgur.com/OKlSmBt.png"
        height="100px"
        v-for="animal in capturedAnimalList"
        v-bind:key="animal"
        class="mt-1 rounded-lg"
        @click="moveDetailView(animal)"
    >
      <v-row align="center">
        <v-col cols="4">
          <v-avatar size="80">
            <img src="https://i.imgur.com/qUgHbuI.png" alt=""/>
          </v-avatar>
        </v-col>
        <v-col cols="12">
          <v-row>
            <v-col cols="4">
              <span style="color: black; ">종류</span>
            </v-col>
            <v-col cols="8">
              <span style="color: black; ">{{ animal.name }}</span>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="4"><span style="color: black; ">포획일</span></v-col>
            <v-col cols="8"><span style="color: black; ">{{ animal.created_at }}</span></v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-parallax>
  </v-container>
</template>

<script>
import axios from "@/util/axios";

export default {
  name: "IllustratedBook",
  mounted() {
    this.loadAnimalList();
  },
  data() {
    return {
      capturedAnimalList: []
    };
  },
  methods: {
    loadAnimalList() {
      axios
          .get('api/animals/post_list?id=' + this.$route.params.id)
          .then((response) => {
            this.capturedAnimalList = response.data;
            console.dir(this.capturedAnimalList);
          })
          .catch((error) => {
            alert(error);
          })
    },
    moveDetailView(animal) {
      this.$router.push({name: "Captured", params:animal});
    }
  }
};
</script>

<style scoped>
</style>