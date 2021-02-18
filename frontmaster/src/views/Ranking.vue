<template>
  <v-container>
    <h1 style="text-align: center">👑 랭킹 👑</h1>
    <br>
    <v-card>
      <v-card-title>
        <v-spacer></v-spacer>
        <v-text-field
            v-model="search"
            append-icon="mdi-magnify"
            label="검색"
            single-line
        ></v-text-field>
      </v-card-title>
      <v-data-table
          :headers="headers"
          :items="rankingData"
          :search="search"
      >
        <template v-slot:item.rank="{ item }">
          <v-chip v-if="item.rank === 1">🥇</v-chip>
          <v-chip v-else-if="item.rank === 2">🥈</v-chip>
          <v-chip v-else-if="item.rank === 3">🥉</v-chip>
          <v-chip v-else>{{ item.rank }}</v-chip>
        </template>
        <template v-slot:item.username="{ item }">
          <a @click="moveIllustrateBook(item.id)">{{ item.username }}</a>
        </template>
      </v-data-table>
    </v-card>
  </v-container>
</template>

<script>
import axios from "@/util/axios";

export default {
  name: "Ranking",
  data() {
    return {
      search: "",
      headers: [
        {
          text: "순위",
          value: "rank"
        },
        {
          text: "아이디",
          value: "username"
        },
        {
          text: "레벨",
          value: "level"
        },
        {
          text: "포획한 동물 수",
          value: "captured"
        }
      ],
      rankingData: [],
      currentUserRank: {}
    };
  },
  mounted() {
    this.loadRankingData();
  },
  methods: {
    loadRankingData() {
      axios
          .get('api/rank')
          .then((response) => {
            this.rankingData = response.data.data;
          })
          .catch((error) => {
            console.log(error);
            alert("랭킹 정보를 읽어오는데 실패했습니다.");
          })
    },
    moveIllustrateBook(id) {
      this.$router.push("/illustratedbook/" + id);
    }
  }
};
</script>

<style scoped>

</style>