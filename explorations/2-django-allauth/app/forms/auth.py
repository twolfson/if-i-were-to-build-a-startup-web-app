from allauth.account import forms as allauth_forms
from django import forms


def monkeypatch_email_field(field):
    # Override silly defaults (e.g. trailing colons, placeholder same as label)
    field.label = "Email"
    # Guidance on setup via https://stackoverflow.com/a/23983577/1960509
    field.widget.attrs["placeholder"] = "your@email.com"


def monkeypatch_password_field(field):
    field.widget.attrs["placeholder"] = ""


# Guidance via https://dev.to/gajesh/the-complete-django-allauth-guide-la3
# Username hidden via `ACCOUNT_USERNAME_REQUIRED = False` in `settings.py`
class SignupForm(allauth_forms.SignupForm):
    # https://github.com/pennersr/django-allauth/blob/0.54.0/allauth/account/forms.py#L267
    # Additional fields: username, email, email2, password1, password2
    # Username removed via: https://github.com/pennersr/django-allauth/blob/0.54.0/allauth/account/forms.py#L339-L340
    first_name = forms.CharField(max_length=30, label="First Name")
    last_name = forms.CharField(max_length=30, label="Last Name")

    def __init__(self, *args, **kwargs):
        ret_val = super().__init__(*args, **kwargs)
        monkeypatch_email_field(self.fields["email"])
        monkeypatch_password_field(self.fields["password1"])

        self.fields["password2"].label = "Confirm Password"
        self.fields["password2"].widget.attrs["placeholder"] = ""

        return ret_val

    # DEV: `signup` method timing is too late for adjustments like username, email, and name (double saving at best)
    #   https://github.com/pennersr/django-allauth/blob/0.54.0/allauth/account/forms.py#L437-L449
    def clean(self):
        # Ensure email and username are both the same, as well as lowercase
        # `username` will be `first_name` if we don't override
        if "email" in self.cleaned_data:
            self.cleaned_data["email"] = self.cleaned_data["email"].lower()
            self.cleaned_data["username"] = self.cleaned_data["email"]
        elif "username" in self.cleaned_data:
            # Clean our `username` if it's somehow around when `email` isn't
            del self.cleaned_data["username"]

        return super().clean()


class LoginForm(allauth_forms.LoginForm):
    def __init__(self, *args, **kwargs):
        ret_val = super().__init__(*args, **kwargs)
        monkeypatch_email_field(self.fields["login"])
        monkeypatch_password_field(self.fields["password"])
        return ret_val