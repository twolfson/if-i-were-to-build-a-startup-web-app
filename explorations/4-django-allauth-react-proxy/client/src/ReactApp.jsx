// Import our dependencies
import {
  createBrowserRouter,
  RouterProvider,
  redirect,
} from "react-router-dom";
import { useCookie } from "react-use";

import { Index } from "./pages/Index";

const LOGGED_IN_COOKIE_NAME = "logged_in";

// DEV: We use a component instead of a `loader`, because otherwise React Router tries to render content regardless
const AuthRequired = ({ children }) => {
  // DEV: Use `useState` so we cache initial value (assumes always logged in) and doesn't touch `localStorage` until later
  //   Caching as `false` doesn't matter because the page will redirect to login
  const [isLoggedIn] = useCookie(LOGGED_IN_COOKIE_NAME);

  if (!isLoggedIn) {
    // TODO: Note in README about missing URL redirect support on login
    // DEV: We can't use `redirect` since that uses `history.pushState`
    window.location = "/auth/login/";
    return null;
  }
  return children;
};

const AuthSuccessLoader = () => {
  // DEV: We could be paranoid and check `document.cookie` (can't use `useCookie` but simple enough), but YAGNI

  // TODO: Note in README about missing URL redirect support on login
  return redirect("/");
};

// TODO: Put all this logic into an `AuthRouter`?
const router = createBrowserRouter([
  {
    path: "/auth-success",
    loader: AuthSuccessLoader,
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
