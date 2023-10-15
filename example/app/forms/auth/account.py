from allauth.account import forms as allauth_account_forms
from django import forms

# Enumeration and extension all forms for easy extension in the future
# https://github.com/pennersr/django-allauth/blob/0.54.0/allauth/account/forms.py


def customize_email_field(field):
    # Override silly defaults (e.g. trailing colons, placeholder same as label)
    field.label = "Email"
    # Guidance on setup via https://stackoverflow.com/a/23983577/1960509
    field.widget.attrs["placeholder"] = "your@email.com"


def remove_field_placeholder(field):
    field.widget.attrs["placeholder"] = ""


class LoginForm(allauth_account_forms.LoginForm):
    # Fields:
    # login # Might be email or username
    # password
    # remember

    def __init__(self, *args, **kwargs):
        ret_val = super().__init__(*args, **kwargs)
        customize_email_field(self.fields["login"])
        remove_field_placeholder(self.fields["password"])
        return ret_val


# Initial guidance via https://dev.to/gajesh/the-complete-django-allauth-guide-la3
class SignupForm(allauth_account_forms.SignupForm):
    # https://github.com/pennersr/django-allauth/blob/0.54.0/allauth/account/forms.py#L267
    # BaseSignUpForm fields:
    # username  # Removed via `USERNAME_REQUIRED`
    # email
    # email2  # Only when `SIGNUP_EMAIL_ENTER_TWICE`

    # SignUpForm fields:
    # password1
    # password2

    # Our custom/additional fields
    first_name = forms.CharField(max_length=30, label="First Name")
    last_name = forms.CharField(max_length=30, label="Last Name")

    def __init__(self, *args, **kwargs):
        ret_val = super().__init__(*args, **kwargs)
        customize_email_field(self.fields["email"])
        remove_field_placeholder(self.fields["password1"])

        self.fields["password2"].label = "Confirm Password"
        remove_field_placeholder(self.fields["password2"])

        return ret_val


class AddEmailForm(allauth_account_forms.AddEmailForm):
    # Fields:
    # email
    pass


class ChangePasswordForm(allauth_account_forms.ChangePasswordForm):
    # Fields:
    # oldpassword
    # password1
    # password2
    pass


class SetPasswordForm(allauth_account_forms.SetPasswordForm):
    # Fields:
    # password1
    # password2
    pass


class ResetPasswordForm(allauth_account_forms.ResetPasswordForm):
    # Fields:
    # email
    pass


class ResetPasswordKeyForm(allauth_account_forms.ResetPasswordKeyForm):
    # Fields:
    # password1
    # password2
    pass


class UserTokenForm(allauth_account_forms.UserTokenForm):
    # Fields:
    # uidb36
    # key
    pass
