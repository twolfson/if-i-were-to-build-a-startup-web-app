import assert from "assert";
import cx from "classnames";

// TODO: Handle input-specific errors like https://github.com/twolfson/if-i-were-to-build-a-startup-web-app/blob/acf34e2f52204084300383ba029b68b0c838af99/explorations/2-django-allauth/app/templates/widgets/input.html#L18-L20
export const Input = ({ className, label, name, type = "text", ...props }) => {
  assert(name, "No `name` prop provided");
  assert(label, "No `label` prop provided");
  return (
    <>
      <label className="form-label" htmlFor={name}>
        {label}
      </label>
      <input
        className={cx("form-control", className)}
        // DEV: `id` used to name `for`
        id={name}
        name={name}
        type={type}
        {...props}
      />
    </>
  );
};
