export const LogoutPage = () => {
  // Avoid `redirect` (and I assume `Navigate` too) since that will use `pushState`
  window.location = "/auth/logout";

  // Return nothing to show progress
  return null;
};
