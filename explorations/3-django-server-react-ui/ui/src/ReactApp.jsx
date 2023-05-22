// Define our component
const ReactApp = () => {
  const user = window.user;
  const isLoggedIn = !user.is_anonymous;

  return <>{isLoggedIn ? `Hello ${user.full_name}` : "Show login page"}</>;
};

export { ReactApp };
