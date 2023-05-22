export const CsrfToken = () => (
    <input type="hidden" name="csrf_token" value={window.csrf_token} />
);
