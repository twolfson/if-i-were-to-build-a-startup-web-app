import { Outlet } from "react-router-dom";

// DEV: We use a component instead of a `loader`, because otherwise React Router tries to render content regardless
export const MessagesContainer = () => {
  // TODO: Load messages
  return <Outlet />;
};
