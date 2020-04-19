"use static";

module.exports = {
  devtool: "inline-source-map",
  entry: {
    ui_main: "./ui_main.py",
  },
  mode: "production",
  module: {
    rules: [
      {
        test: /\.py$/,
        loader: "transcrypt-loader",
        options: {},
      },
    ],
  },
  target: "web",
};
