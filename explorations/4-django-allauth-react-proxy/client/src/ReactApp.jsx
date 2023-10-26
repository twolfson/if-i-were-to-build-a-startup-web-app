// Import our dependencies
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { useCookie } from "react-use";
import { ToastContainer } from "react-toastify";

import { AuthSuccessLoader } from "./loaders/AuthSuccessLoader";
import { IndexPage } from "./pages/IndexPage";
import { LOGGED_IN_COOKIE_NAME } from "./utils/constants";
import { LogoutPage } from "./pages/LogoutPage";
import { NotificationContainer } from "./containers/NotificationContainer";

const queryClient = new QueryClient();
const router = createBrowserRouter([
  {
    // This handles the completion side of auth login (acts as a callback)
    path: "/auth-success",
    loader: AuthSuccessLoader,
  },
  {
    path: "/",
    element: <IndexPage />,
  },
  {
    path: "/logout",
    element: <LogoutPage />,
  },
]);

// Define our component
const InnerApp = () => {
  // Determine our login status
  // DEV: Use `useState` so we cache initial value (assumes always logged in) and doesn't touch `localStorage` until later
  //   Caching as `false` doesn't matter because the page will redirect to login
  const [loggedInStr] = useCookie(LOGGED_IN_COOKIE_NAME);
  const isLoggedIn = !!loggedInStr;

  // If we're not logged in, navigate to Django's auth pages
  if (!isLoggedIn) {
    // DEV: We can't use `redirect` since that uses `history.pushState`
    window.location = "/auth/login/";
    return null;
  }

  // Otherwise, perform routing as per normal
  return (
    <>
      <NotificationContainer />
      <RouterProvider router={router} />
    </>
  );
};

export const ReactApp = () => {
  return (
    <>
      {/* DEV: We place `ToastContainer` at top level, to avoid re-renders which clear existing Toast (see */}
      <ToastContainer position="top-center" />
      <QueryClientProvider client={queryClient}>
        <InnerApp />
      </QueryClientProvider>
    </>
  );
};
