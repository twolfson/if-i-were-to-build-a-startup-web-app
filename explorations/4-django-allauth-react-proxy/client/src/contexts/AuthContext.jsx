import { createContext } from 'react';

const LOGGED_IN_KEY = "logged_in";

export const ThemeContext = createContext('light');

export const AuthProvider = ({ children }) => {
  const [isLoggedIn, setIsLoggedIn] = window.localStorage[LOGGED_IN_KEY] === "1";

  if (!isLoggedIn) {
    return "TODO: Redirect";
  }
  return children;
};
