"use static";

module.exports = {
  entry: {
    ui_main: "./ui_main.py",
  },
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
