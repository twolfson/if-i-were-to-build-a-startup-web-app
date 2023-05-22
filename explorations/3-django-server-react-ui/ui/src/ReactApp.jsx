// Import our dependencies
import { Login } from "./pages/Login";

// Define our component
export const ReactApp = () => {
  const user = window.user;
  const isLoggedIn = !user.is_anonymous;

  // TODO: Handle routing (sign up) and 404 pages
  return <>{isLoggedIn ? `Hello ${user.full_name}` : <Login />}</>;
};
