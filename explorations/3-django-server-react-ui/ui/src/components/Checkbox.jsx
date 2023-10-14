import assert from "assert";
import cx from "classnames";

export const Checkbox = ({ className, label, name, ...props }) => {
  assert(name, "No `name` prop provided");
  assert(label, "No `label` prop provided");
  return (
    // https://getbootstrap.com/docs/5.2/forms/checks-radios/#checks
    <div className="form-check">
      <input
        id={name}
        name={name}
        type="checkbox"
        className={cx("form-check-input", className)}
        {...props}
      />
      <label className="form-label" htmlFor={name}>
        {label}
      </label>
    </div>
  );
};
