// The root of the web application

import React, { StrictMode } from "react";
import ReactDOM from "react-dom";
import 'regenerator-runtime'

import App from './components/App/App.jsx'

// The only bit of vanilla JS we need
// Uses ReactDOM to render some JSX
// public/index.html must have a div with the class "root" in it for this to work
// ReactDOM.render takes the div and uses all the react magic to render
// your React application inside the div
const rootElement = document.getElementById("root");
ReactDOM.render(
  <StrictMode>
    <App />
  </StrictMode>,
  rootElement
);