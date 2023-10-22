import {
  redirect,
} from "react-router-dom";

export const AuthSuccessLoader = () => {
  // DEV: We could be paranoid and check `document.cookie` (can't use `useCookie` but simple enough), but YAGNI

  // TODO: Note in README about missing URL redirect support on login
  return redirect("/");
};
