// Import our dependencies
import { useState } from "react";
import { createBrowserRouter, RouterProvider, redirect } from "react-router-dom";
import { useEffectOnce } from "react-use";

import { Index } from "./pages/Index";

const LOGGED_IN_KEY = "logged_in";
const LOGGED_IN_SUCCESS_VALUE = "1";

const AuthRequired = ({ children }) => {
  // DEV: Use `useState` so we cache initial value (assumes always logged in) and doesn't touch `localStorage` until later
  //   Caching as `false` doesn't matter because the page will redirect to login
  const [isLoggedIn, ] = useState(
    window.localStorage[LOGGED_IN_KEY] === LOGGED_IN_SUCCESS_VALUE
  );

  if (!isLoggedIn) {
    // TODO: Note in README about missing URL redirect support on login
    return redirect("/auth/login/")
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

  // TODO: Note in README about missing URL redirect support on login
  return redirect("/")
}

// TODO: Relocate to proper place
const LogoutPage = () => {
  // Only unset localStorage once at load
  useEffectOnce(() => {
    delete window.localStorage[LOGGED_IN_KEY];
  });

  return redirect("/auth/logout/")
}

const router = createBrowserRouter([
  {
    path: "/auth-success",
    element: <AuthSuccessPage />,
  },
  {
    path: "/logout",
    element: <LogoutPage />,
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
