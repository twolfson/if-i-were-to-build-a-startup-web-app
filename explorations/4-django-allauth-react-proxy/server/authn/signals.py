from django.dispatch import receiver
from allauth.account.signals import user_logged_in


@receiver(user_logged_in)
def handle_user_logged_in(request, user, **kwargs):
    # DEV: This fires at both sign up and login when email verification is optional
    print(request

# TODO: Handle logout
# allauth.account.signals.user_logged_out(request, user)

# TODO: Make note we need might need this for social logins
