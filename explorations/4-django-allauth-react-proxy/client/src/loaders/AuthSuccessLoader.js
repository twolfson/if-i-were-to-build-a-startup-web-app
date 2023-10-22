import {
  redirect,
} from "react-router-dom";

export const AuthSuccessLoader = () => {
  // DEV: We could be paranoid and check `document.cookie` (can't use `useCookie` but simple enough), but YAGNI

  return redirect("/");
};
