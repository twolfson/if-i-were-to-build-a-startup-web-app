// Based on: https://github.com/pennersr/django-allauth/blob/0.54.0/allauth/templates/account/login.html
// Based on: explorations/2-django-allauth/app/templates/account/login.html
import { AuthLayout } from "./_layouts/AuthLayout";
import { Checkbox } from "../components/Checkbox";
import { CsrfToken } from "../components/CsrfToken";
import { Input } from "../components/Input";

export const Login = () => {
  // DEV: It'd be nice to use `head_title: Login`
  // DEV: It'd prob be more efficient to define a context which looks for form errors

  // Process our form errors into a common array for top of form
  // DEV: We always render a `json_script` for each of these in this exploration, even on page load
  // DEV: We're using `_` to avoid confusing with `combinedFormErrors`
  const _formErrors = JSON.parse(document.querySelector("head > #form__errors").innerText);
  const _formNonFieldErrors = JSON.parse(document.querySelector("head > #form__non_field_errors").innerText);
  // __all__ appears as `_formNonFieldErrors` as well (e.g. email+password incorrect)
  delete _formErrors["__all__"];
  const formErrorsAsArray = Object.entries(_formErrors).map(([key, val]) =>
    `${key}: ${val}`
  )
  const combinedFormErrors = formErrorsAsArray.concat(_formNonFieldErrors);

  return (
    <AuthLayout>
      <h1 className="mb-3">Login</h1>
      { combinedFormErrors.length ? <p class="text-danger">{combinedFormErrors.join(" ")}</p> : null }
      {/* Fields enumerated here: https://github.com/pennersr/django-allauth/blob/0.54.0/allauth/account/forms.py#L90 */}
      {/* DEV: `form` submits as an HTML form, not an XHR submission */}
      <form action="/login/" method="post" className="mb-4">
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
