from allauth.account.adapter import DefaultAccountAdapter
from django.contrib import messages
from project.settings import DEBUG


# https://github.com/pennersr/django-allauth/blob/0.54.0/allauth/account/adapter.py#L43
class AccountAdapter(DefaultAccountAdapter):
    # Override email sending, https://github.com/pennersr/django-allauth/blob/0.54.0/allauth/account/adapter.py#L138-L140  # noqa:E501
    # DEV: Technically we can log to console, but let's treat ourselves with messages in the UI
    def send_mail(self, template_prefix, email, context):
        assert DEBUG is True, "Conditional for production case not handled"
        message = f"Email \"sent\": \"{template_prefix}\" to \"{email}\" with {context}"
        print(message)
        messages.info(context["request"], message)
