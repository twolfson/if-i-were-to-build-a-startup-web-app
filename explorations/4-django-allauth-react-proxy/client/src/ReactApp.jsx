// Import our dependencies
import { useState } from "react";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { Index } from "./pages/Index";

const LOGGED_IN_KEY = "logged_in";
const LOGGED_IN_SUCCESS_VALUE = "1";

const AuthRequired = ({ children }) => {
  // DEV: Use `useState` so we cache initial value (assumes always logged in) and doesn't touch `localStorage` until later
  // TODO: Handle actually changing state on auth success
  const [isLoggedIn, setIsLoggedIn] = useState(
    window.localStorage[LOGGED_IN_KEY] === LOGGED_IN_SUCCESS_VALUE
  );

  if (!isLoggedIn) {
    return "TODO: Redirect";
  }
  return children;
};

const AuthSuccessPage = () => {
  // TODO: Handle redirect
  useEffectOnce(() => {

  })
}

const router = createBrowserRouter([
  {
    path: "/auth-success",
    element: <div>TODO</div>,
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
