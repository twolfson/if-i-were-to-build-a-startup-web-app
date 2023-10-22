import { Outlet } from "react-router-dom";
import { useCookie } from "react-use";

import { LOGGED_IN_COOKIE_NAME } from "../utils/constants";

// DEV: We use a component instead of a `loader`, because otherwise React Router tries to render content regardless
export const AuthRequiredContainer = () => {
  // DEV: Use `useState` so we cache initial value (assumes always logged in) and doesn't touch `localStorage` until later
  //   Caching as `false` doesn't matter because the page will redirect to login
  const [isLoggedIn] = useCookie(LOGGED_IN_COOKIE_NAME);

  // If we're not logged in, navigate to Django's auth pages
  if (!isLoggedIn) {
    // TODO: Note in README about missing URL redirect support on login
    // DEV: We can't use `redirect` since that uses `history.pushState`
    window.location = "/auth/login/";
    return null;
  }

  return <Outlet />;
};
