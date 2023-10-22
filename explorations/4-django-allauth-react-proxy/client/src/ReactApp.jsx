// Import our dependencies
import { useQuery, QueryClient, QueryClientProvider } from "react-query";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { useCookie } from "react-use";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

import { AuthSuccessLoader } from "./loaders/AuthSuccessLoader";
import { Index } from "./pages/Index";
import { LOGGED_IN_COOKIE_NAME } from "./utils/constants";

const queryClient = new QueryClient();
const router = createBrowserRouter([
  {
    // This handles the completion side of auth login (acts as a callback)
    path: "/auth-success",
    loader: AuthSuccessLoader,
  },
  {
    path: "/",
    element: <Index />,
  },
]);

// Define our component
export const ReactApp = () => {
  // Determine our login status
  // DEV: Use `useState` so we cache initial value (assumes always logged in) and doesn't touch `localStorage` until later
  //   Caching as `false` doesn't matter because the page will redirect to login
  const [loggedInStr] = useCookie(LOGGED_IN_COOKIE_NAME);
  const isLoggedIn = !!loggedInStr;

  // If we're not logged in, navigate to Django's auth pages
  if (!isLoggedIn) {
    // TODO: Note in README about missing URL redirect support on login
    // DEV: We can't use `redirect` since that uses `history.pushState`
    window.location = "/auth/login/";
    return null;
  }

  // Otherwise, perform routing as per normal
  return (
    <QueryClientProvider client={queryClient}>
      <ToastContainer position="top-center" />
      <RouterProvider router={router} />
    </QueryClientProvider>
  );
};
