<template>
  <Capture v-if="!show" @success-signal="success" />
  <Result v-else :results="results" />
</template>

<script>
import Capture from "@/components/Capture/Capture.vue";
import Result from "@/components/Capture/Result.vue";
export default {
  name: "CaptureView",
  components: {
    Capture,
    Result
  },
  data() {
    return {
      show: false,
      results: []
    };
  },
  methods: {
    success(e) {
      this.results = e;
      this.show = !this.show;
      console.log(this.results);
      console.log(this.show);
    }
  }
};
</script>

<style></style>
