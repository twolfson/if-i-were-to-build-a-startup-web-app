import assert from "assert";
import cx from "classnames";

// TODO: Handle input-specific errors like https://github.com/twolfson/if-i-were-to-build-a-startup-web-app/blob/acf34e2f52204084300383ba029b68b0c838af99/explorations/2-django-allauth/app/templates/widgets/input.html#L18-L20
export const Checkbox = ({ className, label, name, ...props }) => {
    assert(name, "No `name` prop provided");
    assert(label, "No `label` prop provided");
    return (
        // https://getbootstrap.com/docs/5.2/forms/checks-radios/#checks
        <div class="form-check">
            <input
                type="checkbox"
                className={cx("form-check-input", className)}
            />
            <label class="form-label" for={name}>
                {label}
            </label>
        </div>
    );
};
