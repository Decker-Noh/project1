module.exports = {
  transpileDependencies: ["vuetify"],
  devServer: {
    proxy: {
      "/api": {
        // target: "http://localhost:8000",
        target: "http://j3c106.p.ssafy.io/",
        ws: true,
        changeOrigin: true
      }
    }
  }
};
