from allauth.account import forms as allauth_forms
from django import forms


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

        # Override silly defaults (e.g. trailing colons, placeholder same as label)
        self.fields["email"].label = "Email"
        # Guidance on setup via, https://stackoverflow.com/a/23983577/1960509
        self.fields["email"].widget.attrs["placeholder"] = "your@email.com"

        self.fields["password1"].widget.attrs["placeholder"] = ""

        self.fields["password2"].label = "Confirm Password"
        self.fields["password2"].widget.attrs["placeholder"] = ""

        return ret_val

    def signup(self, request, user):
        # Ensure email and username are both the same, as well as lowercase
        # `username` will be `first_name` if we don't override
        # TODO: This override isn't working as expected, let's go TDD
        user.email = self.cleaned_data["email"].lower()
        user.username = self.cleaned_data["email"].lower()
        # TODO: How does login with with casing change

        # Add our other data
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.save()
        return user
