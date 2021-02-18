<template>
  <v-carousel
    class="caroo"
    hide-delimiters
    :show-arrows="false"
    height="1000px"
  >
    <v-carousel-item v-for="(item, i) in results" :key="i">
      <v-card class="mx-0 mx-auto" max-width="415px" scroll>
        <v-img
          :src="'http://j3c106.p.ssafy.io/' + item.image"
          min-height="500px"
          max-height="700px"
          aspect-ratio="16/9"
        ></v-img>
        <!-- <v-img
          :src="'http://localhost:8000' + item.image"
          min-height="500px"
          max-height="700px"
          aspect-ratio="16/9"
        ></v-img> -->

        <v-card-title>
          {{ item.name }}
        </v-card-title>

        <!-- <v-card-subtitle>
          더 추가할 말 있나
        </v-card-subtitle> -->

        <v-card-actions>
          <v-btn color="orange lighten-2" text>
            설명
          </v-btn>

          <v-spacer></v-spacer>
        </v-card-actions>

        <v-expand-transition>
          <div v-show="show">
            <v-divider></v-divider>

            <v-card-text>
              {{ item.info }}
            </v-card-text>
          </div>
        </v-expand-transition>
      </v-card>
    </v-carousel-item>
  </v-carousel>
</template>

<script>
export default {
  name: "Result",
  props: {
    results: Array
  },
  data() {
    return {
      show: true,
      items: [
        {
          name: "다람쥐",
          src: "https://cdn.vuetifyjs.com/images/carousel/squirrel.jpg",
          description:
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
        },
        {
          name: "하늘",
          src: "https://cdn.vuetifyjs.com/images/carousel/sky.jpg",
          description:
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
        },
        {
          name: "독수리",
          src: "https://cdn.vuetifyjs.com/images/carousel/bird.jpg",
          description:
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
        },
        {
          name: "우주",
          src: "https://cdn.vuetifyjs.com/images/carousel/planet.jpg",
          description:
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
        }
      ]
    };
  }
};
</script>

<style>
.caroo {
  background-color: #1e1e1e;
}
</style>
