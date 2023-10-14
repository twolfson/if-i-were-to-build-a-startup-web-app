import assert from "assert";
import cx from "classnames";

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
