export const CsrfToken = () => (
  // Name resolved via: `{% csrf_token %}`
  <input type="hidden" name="csrfmiddlewaretoken" value={window.csrf_token} />
);
