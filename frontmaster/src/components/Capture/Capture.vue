<template>
  <v-container>
    <v-row>
      <v-col cols="12" class="d-flex justify-center">
        <input
          hidden
          ref="imageInput"
          @change="onChangeImage"
          type="file"
          accept="image/*"
          capture="camera"
        />
        <v-img v-if="previewImage" :src="previewImage"></v-img>
      </v-col>
      <v-col cols="12" class="d-flex justify-center">
        <div v-if="previewImage">
          <v-btn @click="sendImage" color="success" class="mx-2 px-6">
            <v-icon>
              mdi-cloud-upload
            </v-icon>
            업로드
          </v-btn>
          <v-btn @click="refreshPage" color="warning" class="mx-2">
            <v-icon>
              mdi-refresh
            </v-icon>
            다시찍기
          </v-btn>
        </div>
      </v-col>
      <v-overlay :value="overlay">
        <v-progress-circular indeterminate size="64"></v-progress-circular>
      </v-overlay>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      previewImage: null,
      imageFile: null,
      overlay: false,
      currentUserId: null
    };
  },
  methods: {
    onChangeImage(e) {
      this.imageFile = e.target.files[0];
      this.previewImage = URL.createObjectURL(this.imageFile);
      console.log(this.imageFile);
    },
    sendImage() {
      this.overlay = !this.overlay;
      const formData = new FormData();
      formData.append("image", this.imageFile);
      formData.append("userId", this.currentUserId);
      console.log(this.currentUserId);
      const config = {
        headers: {
          "Content-Type": "multipart/form-data"
        }
      };
      this.$axios
        .post("/api/animals/upload/", formData, config)
        .then(res => {
          alert("성공");
          console.log(res.data);
          this.$emit("success-signal", res.data);
        })
        .catch(err => console.log(err));
    },
    refreshPage() {
      this.$refs.imageInput.click();
    },
    loadCurrentUserId(token) {
      this.$axios
        .get("api/return/id?authToken=" + token)
        .then(response => {
          this.currentUserId = response.data.id;
          console.log(this.currentUserId);
        })
        .catch(error => {
          console.log(error);
        });
    }
  },
  mounted() {
    this.$refs.imageInput.click();
    this.loadCurrentUserId(this.$store.state.authToken);
  },

  watch: {
    overlay(val) {
      val &&
        setTimeout(() => {
          this.overlay = false;
        }, 4000);
    }
  }
};
</script>

<style></style>
