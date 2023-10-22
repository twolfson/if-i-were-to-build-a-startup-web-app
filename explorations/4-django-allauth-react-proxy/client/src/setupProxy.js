const { createProxyMiddleware } = require("http-proxy-middleware");

// Configuration via https://create-react-app.dev/docs/proxying-api-requests-in-development/
// DEV: We cannot use the default `proxy` setting since it disallows `Allow: text/html` (e.g. browser navigation)
module.exports = function (app) {
  app.use(
    // Route multiple paths to Django, https://stackoverflow.com/a/26058349/1960509
    [
      "/admin",
      "/api",
      "/auth",
    ],
    createProxyMiddleware({
      target: "http://localhost:8000",
      // DEV: We keep the host the same as the original, such that DRF documentation still works
      changeOrigin: false,
    }),
  );
};
