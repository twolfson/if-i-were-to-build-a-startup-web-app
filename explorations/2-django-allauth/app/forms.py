from allauth.account import forms as allauth_forms
from django import forms


# Guidance via https://dev.to/gajesh/the-complete-django-allauth-guide-la3
# Username hidden via `ACCOUNT_USERNAME_REQUIRED = False` in `settings.py`
class SignupForm(allauth_forms.SignupForm):
    # https://github.com/pennersr/django-allauth/blob/0.54.0/allauth/account/forms.py#L267
    # Additional fields: username, email, email2, password1, password2
    # Username removed via: https://github.com/pennersr/django-allauth/blob/0.54.0/allauth/account/forms.py#L339-L340
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user