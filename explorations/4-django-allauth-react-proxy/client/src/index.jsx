import React from "react";
import ReactDOM from "react-dom/client";
import { ReactApp } from "./ReactApp";

const uiRoot = ReactDOM.createRoot(document.getElementById("ui"));
uiRoot.render(
  <React.StrictMode>
    <AuthProvider>
      <ReactApp />
    </AuthProvider>
  </React.StrictMode>,
);
