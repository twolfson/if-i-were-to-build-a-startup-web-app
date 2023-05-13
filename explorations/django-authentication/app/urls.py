from django.urls import include, path

from . import views

urlpatterns = [
    # Provide multiple auth login by default, https://docs.djangoproject.com/en/4.2/topics/auth/default/#using-the-views
    # https://github.com/django/django/blob/4.2.1/django/contrib/auth/urls.py
    # TODO: Update to login explicitly, https://github.com/django/django/blob/4.2.1/django/contrib/auth/forms.py#L199-L210
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("password_change/", views.PasswordChangeView.as_view(), name="password_change"),
    path(
        "password_change/done/",
        views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
    path(
        "password_reset/done/",
        views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    # Django doesn't have a sign up view, so use this guide: https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
    path("sign-up/", views.SignUpFormView.as_view(), name="sign_up"),
    path("", views.index, name="index"),
]
