from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from allauth.account.views import EmailVerificationSentView


# https://docs.djangoproject.com/en/4.2/topics/class-based-views/intro/#decorating-the-class
@method_decorator(login_required, name="dispatch")
class CustomEmailVerificationSentView(EmailVerificationSentView):
    pass


email_verification_sent = CustomEmailVerificationSentView.as_view()
