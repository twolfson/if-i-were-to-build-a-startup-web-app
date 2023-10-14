// Based on: https://github.com/pennersr/django-allauth/blob/0.54.0/allauth/templates/account/login.html
// Based on: explorations/2-django-allauth/app/templates/account/login.html
// TODO: It'd be nice to use `head_title: Login`
// TODO: Handle form errors
import { AuthLayout } from "./_layouts/AuthLayout";
import { Checkbox } from "../components/Checkbox";
import { CsrfToken } from "../components/CsrfToken";
import { Input } from "../components/Input";

export const Login = () => {
  return (
    <AuthLayout>
      <h1 className="mb-3">Login</h1>
      {/* Fields enumerated here: https://github.com/pennersr/django-allauth/blob/0.54.0/allauth/account/forms.py#L90 */}
      {/* DEV: `form` submits as an HTML form, not an XHR submission */}
      <form action="/login" method="post" className="mb-4">
        <CsrfToken />
        <div className="mb-3">
          <Input name="login" label="Email" />
        </div>
        <div className="mb-3">
          <Input name="password" label="Password" type="password" />
        </div>
        <div className="mb-3">
          <Checkbox name="remember" label="Remember me" />
        </div>
        <div className="d-grid">
          <button className="btn btn-primary btn-block" type="submit">
            Login
          </button>
        </div>
        {/* DEV: django-allauth supports form redirect but we didn't implement it yet */}
      </form>
      <p>
        {/* eslint-disable-next-line jsx-a11y/anchor-is-valid,no-script-url */}
        <a href="#" onClick={() => window.alert("Disabled for now")}>
          Forgot password?
        </a>
      </p>
      <p>
        {/* Nice touch would be linking this whole row, but keeping styling at end */}
        Don't have an account? <a href="/sign-up">Sign up</a>
      </p>
    </AuthLayout>
  );
};
