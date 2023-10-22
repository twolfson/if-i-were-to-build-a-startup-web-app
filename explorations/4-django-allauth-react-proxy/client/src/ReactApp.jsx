// Import our dependencies
import { useState } from "react";
import {
  createBrowserRouter,
  RouterProvider,
  redirect,
} from "react-router-dom";
import { useEffectOnce } from "react-use";

import { Index } from "./pages/Index";

const LOGGED_IN_KEY = "logged_in";
const LOGGED_IN_SUCCESS_VALUE = "1";

// DEV: We use a component instead of a `loader`, because otherwise React Router tries to render content regardless
const AuthRequired = ({ children }) => {
  // DEV: Use `useState` so we cache initial value (assumes always logged in) and doesn't touch `localStorage` until later
  //   Caching as `false` doesn't matter because the page will redirect to login
  const [isLoggedIn, ] = useState(
    window.localStorage[LOGGED_IN_KEY] === LOGGED_IN_SUCCESS_VALUE
  );

  if (!isLoggedIn) {
    // TODO: Note in README about missing URL redirect support on login
    // DEV: We can't use `redirect` since that uses `history.pushState`
    window.location = "/auth/login/";
    return null;
  }
  return children;
};


// TODO: Relocate to proper place
const LogoutPage = () => {
  // Only unset localStorage once at load
  useEffectOnce(() => {
    delete window.localStorage[LOGGED_IN_KEY];
  });

  // DEV: We can't use `redirect` since that uses `history.pushState`
  window.location = "/auth/logout/";
  return null;
}

const router = createBrowserRouter([
  {
    path: "/auth-success",
    loader: () => {
      // DEV: If we ever need to put this back into a component, then use `useEffectOnce`
      window.localStorage[LOGGED_IN_KEY] = LOGGED_IN_SUCCESS_VALUE;

      // TODO: Note in README about missing URL redirect support on login
      return redirect("/");
    },
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
