// Import our dependencies
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import { ErrorPage } from "./pages/ErrorPage";
import { Index } from "./pages/Index";

const router = createBrowserRouter([
  {
    path: "/",
    element: < Index />,
    errorElement: <ErrorPage />,
  },
]);

// Define our component
export const ReactApp = () => {
  return <RouterProvider router={router} />;
};
