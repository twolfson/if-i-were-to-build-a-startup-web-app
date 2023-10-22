// Import our dependencies
import { useState } from "react";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { useEffectOnce } from "react-use";

import { Index } from "./pages/Index";

const LOGGED_IN_KEY = "logged_in";
const LOGGED_IN_SUCCESS_VALUE = "1";

const AuthRequired = ({ children }) => {
  // DEV: Use `useState` so we cache initial value (assumes always logged in) and doesn't touch `localStorage` until later
  //   Caching as `false` doesn't matter because the page will redirect to login
  // TODO: Handle actually changing state on auth success
  const [isLoggedIn, setIsLoggedIn] = useState(
    window.localStorage[LOGGED_IN_KEY] === LOGGED_IN_SUCCESS_VALUE
  );

  if (!isLoggedIn) {
    return "TODO: Redirect to auth URL with current URL as query param";
  }
  return children;
};

// TODO: Relocate to proper place
const AuthSuccessPage = () => {
  // Only set localStorage once at load
  // DEV: Due to this being separate/before `AuthRequired`, we won't have hit the cache there yet
  useEffectOnce(() => {
    window.localStorage[LOGGED_IN_KEY] = LOGGED_IN_SUCCESS_VALUE;
  });

  return "TODO: Redirect to provided URL or /"
  // TODO: Handle redirect
}

const router = createBrowserRouter([
  {
    path: "/auth-success",
    element: <AuthSuccessPage />,
  },
  {
    path: "/",
    element: (
      <AuthRequired>
        <Index />
      </AuthRequired>
    ),
  },
]);

// Define our component
export const ReactApp = () => {
  return <RouterProvider router={router} />;
};
