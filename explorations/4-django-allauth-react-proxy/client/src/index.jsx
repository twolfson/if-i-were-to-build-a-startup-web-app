import React from "react";
import ReactDOM from "react-dom/client";
import { ReactApp } from "./ReactApp";

// DEV: This handles the HTML side of loading our app
const uiRoot = ReactDOM.createRoot(document.getElementById("ui"));
uiRoot.render(
  <React.StrictMode>
    <ReactApp />
  </React.StrictMode>,
);
