from django import forms
from django.contrib.auth import forms as auth_forms
from django.forms.widgets import PasswordInput, TextInput
from django.utils.translation import gettext_lazy as _


# TODO: Build me out
# https://github.com/django/django/blob/4.2.1/django/forms/widgets.py#L358-L369
# class BootstrapPasswordInput(PasswordInput):
#     template_name = "forms/widgets/password.html"


# https://github.com/django/django/blob/4.2.1/django/forms/widgets.py#L338-L340
class BootstrapTextInput(TextInput):
    template_name = "forms/widgets/text.html"


# https://github.com/django/django/blob/4.2.1/django/contrib/auth/forms.py#L199-L210
class LoginForm(auth_forms.AuthenticationForm):
    username = auth_forms.UsernameField(widget=BootstrapTextInput(attrs={"autofocus": True}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        # TODO: Swap to Bootstrap
        widget=PasswordInput(attrs={"autocomplete": "current-password"}),
    )
