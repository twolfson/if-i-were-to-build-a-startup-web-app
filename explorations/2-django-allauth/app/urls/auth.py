from django.urls import path, re_path

from allauth.account import views as allauth_views

urlpatterns = [
    # Only expose URLs we want to at the beginning, https://github.com/pennersr/django-allauth/blob/0.54.0/allauth/account/urls.py  # noqa:E501
    path("signup/", allauth_views.signup, name="account_signup"),
    path("login/", allauth_views.login, name="account_login"),
    path("logout/", allauth_views.logout, name="account_logout"),
    # path(
    #     "password/change/",
    #     allauth_views.password_change,
    #     name="account_change_password",
    # ),
    # path("password/set/", allauth_views.password_set, name="account_set_password"),
    # path("inactive/", allauth_views.account_inactive, name="account_inactive"),
    # # E-mail
    # path("email/", allauth_views.email, name="account_email"),
    path(
        "confirm-email/",
        allauth_views.email_verification_sent,
        name="account_email_verification_sent",
    ),
    re_path(
        r"^confirm-email/(?P<key>[-:\w]+)/$",
        allauth_views.confirm_email,
        name="account_confirm_email",
    ),
    # # password reset
    # path("password/reset/", allauth_views.password_reset, name="account_reset_password"),
    # path(
    #     "password/reset/done/",
    #     allauth_views.password_reset_done,
    #     name="account_reset_password_done",
    # ),
    # re_path(
    #     r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
    #     allauth_views.password_reset_from_key,
    #     name="account_reset_password_from_key",
    # ),
    # path(
    #     "password/reset/key/done/",
    #     allauth_views.password_reset_from_key_done,
    #     name="account_reset_password_from_key_done",
    # ),

    # Add social via different means, https://github.com/pennersr/django-allauth/blob/0.54.0/allauth/urls.py#L12-L25
]
