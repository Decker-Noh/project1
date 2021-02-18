<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="./img/tiger.png"
          transition="scale-transition"
          width="60"
        />
        <v-text class="white--text" style="font-size:2em;"
          >호랑이는 멍멍</v-text
        >
      </div>

      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-heart</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>

      <v-menu left bottom>
        <template v-slot:activator="{ on, attrs }">
          <v-btn icon v-bind="attrs" v-on="on">
            <v-icon>mdi-dots-vertical</v-icon>
          </v-btn>
        </template>

        <v-list>
          <v-list-item v-for="n in 5" :key="n" @click="() => {}">
            <v-list-item-title>Option {{ n }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-app-bar>

    <v-main class="d-flex justify-center align-center">
      <router-view :key="$route.fullPath" />
    </v-main>

    <BottomNav class="pt-2" />
  </v-app>
</template>

<script>
import BottomNav from "@/components/BottomNav.vue";

export default {
  name: "App",
  components: {
    BottomNav
  }
};
</script>
<style>
a {
  text-decoration: none !important;
  color: black !important;
}
</style>
