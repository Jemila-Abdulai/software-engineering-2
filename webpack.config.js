const HtmlWebpackPlugin = require('html-webpack-plugin');
const path = require("path");

// Webpack compiles our React code
// We use webpack-dev-server to hot-reaload our code so we don't have to
// reload our webpack-dev-server every time we make code changes

module.exports = {
  entry: "./src/frontend/index.jsx",

  // This controls the output of "webpack build"
  output: {
    path: path.resolve(__dirname, "dist"),
    filename: "bundle.[hash].js"
  },

  // This controls the "webpack serve" or "webpack-dev-server" (they're the same thing)
  devServer: {
    compress: true,
    port: 8080,
    // This is important if you want a backend for your frontend to talk to
    // It proxies all HTTP requests matching "/api/**" to a different HTTP server
    // i.e our backend, which serves the request with our desires data and the 
    // frontend uses it to render stuff
    proxy: {
        '/api/**': 'http://localhost:8081'
    },
    hot: true,
    static: './dist',
    historyApiFallback: true,
    open: true
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      },
      {
        test:/\.css$/,
        exclude: /node_modules/,
        use: {
          loader: 'css-loader'
        }
      },
      {
        test: /\.png$/,
        exclude: /node_modules/,
        use: {
          loader: 'file-loader'
        }
      }
    ]
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: __dirname + "/public/index.html",
      filename: "index.html"
    }),
  ],
  mode: "development",
  devtool: 'inline-source-map',
};