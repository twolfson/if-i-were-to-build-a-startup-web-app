from allauth.socialaccount import forms as allauth_socialaccount_forms

# Enumeration and extension all forms for easy extension in the future
# https://github.com/pennersr/django-allauth/blob/0.54.0/allauth/socialaccount/forms.py


class SignupForm(allauth_socialaccount_forms.SignupForm):
    # BaseSignUpForm fields:
    # https://github.com/pennersr/django-allauth/blob/0.54.0/allauth/account/forms.py#L267
    # username
    # email
    # email2
    pass


class DisconnectForm(allauth_socialaccount_forms.DisconnectForm):
    # Fields
    # account
    pass
