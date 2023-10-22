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


const router = createBrowserRouter([
  {
    path: "/auth-success",
    action: () => {
      // DEV: If we ever need to put this back into a component, then use `useEffectOnce`
      window.localStorage[LOGGED_IN_KEY] = LOGGED_IN_SUCCESS_VALUE;

      // TODO: Note in README about missing URL redirect support on login
      return redirect("/");
    },
  },
  {
    path: "/logout",
    action: () => {
      // DEV: If we ever need to put this back into a component, then use `useEffectOnce`
      delete window.localStorage[LOGGED_IN_KEY];
      return redirect("/auth/logout/");
    },
    element: null,
  },
  {
    path: "/",
    loader: () => {
      // DEV: If we ever need to put this back into a component, then use `useState` to cache
      const isLoggedIn = window.localStorage[LOGGED_IN_KEY] === LOGGED_IN_SUCCESS_VALUE;
      if (!isLoggedIn) {
        // TODO: Note in README about missing URL redirect support on login
        return redirect("/auth/login/");
      }
    },
    element: (
      <Index />
    ),
  },
]);

// Define our component
export const ReactApp = () => {
  return <RouterProvider router={router} />;
};
