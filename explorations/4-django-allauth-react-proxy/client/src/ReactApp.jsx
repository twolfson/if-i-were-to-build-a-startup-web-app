// Import our dependencies
import { createBrowserRouter, RouterProvider } from "react-router-dom";

import { AuthRequiredContainer } from "./containers/AuthRequiredContainer";
import { MessagesContainer } from "./containers/MessagesContainer";
import { AuthSuccessLoader } from "./loaders/AuthSuccessLoader";
import { Index } from "./pages/Index";

const router = createBrowserRouter([
  {
    path: "/auth-success",
    loader: AuthSuccessLoader,
  },
  {
    path: "/",
    element: <AuthRequiredContainer />,
    children: [
      {
        index: true,
        // DEV: Required as part of Django auth process, to avoid weird messages at logout
        element: <MessagesContainer />,
        children: [
          {
            index: true,
            element: <Index />,
          },
        ],
      },
    ],
  },
]);

// Define our component
export const ReactApp = () => {
  return <RouterProvider router={router} />;
};
