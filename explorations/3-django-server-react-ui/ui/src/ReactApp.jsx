// Import our dependencies
import { Login } from "./pages/Login";

// Define our component
export const ReactApp = () => {
  const user = window.user;
  const isLoggedIn = !user.is_anonymous;

  // DEV: This is missing routing (e.g. sign up, 404 pages)
  return <>{isLoggedIn ? `Hello ${user.full_name}` : <Login />}</>;
};
