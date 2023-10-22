// Import our dependencies
import { useState } from "react";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { Index } from "./pages/Index";

const LOGGED_IN_KEY = "logged_in";

const AuthRequired = ({ children }) => {
  const [isLoggedIn, setIsLoggedIn] = useState(
    window.localStorage[LOGGED_IN_KEY] === "1",
  );

  if (!isLoggedIn) {
    return "TODO: Redirect";
  }
  return children;
};

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
