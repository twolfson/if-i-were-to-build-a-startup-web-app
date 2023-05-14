from allauth.account.adapter import DefaultAccountAdapter
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site

from project.settings import DEBUG


# https://github.com/pennersr/django-allauth/blob/0.54.0/allauth/account/adapter.py#L43
class AccountAdapter(DefaultAccountAdapter):
    # Extend the normal `send_confirmation_mail` to include `request`, https://github.com/pennersr/django-allauth/blob/0.54.0/allauth/account/adapter.py#L536-L549  # noqa:E501
    #   This is required by our `send_mail`
    def send_confirmation_mail(self, request, emailconfirmation, signup):
        current_site = get_current_site(request)
        activate_url = self.get_email_confirmation_url(request, emailconfirmation)
        ctx = {
            "user": emailconfirmation.email_address.user,
            "activate_url": activate_url,
            "current_site": current_site,
            "key": emailconfirmation.key,
            "request": request,
        }
        if signup:
            email_template = "account/email/email_confirmation_signup"
        else:
            email_template = "account/email/email_confirmation"
        self.send_mail(email_template, emailconfirmation.email_address.email, ctx)

    # Override email sending, https://github.com/pennersr/django-allauth/blob/0.54.0/allauth/account/adapter.py#L138-L140  # noqa:E501
    # DEV: Technically we can log to console, but let's treat ourselves with messages in the UI
    def send_mail(self, template_prefix, email, context):
        assert DEBUG is True, "Conditional for production case not handled"
        message = f'Email "sent": "{template_prefix}" to "{email}" with {context}'
        print(message)
        messages.info(context["request"], message)
