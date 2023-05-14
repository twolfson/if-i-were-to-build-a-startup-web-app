from django.urls import include, path

from . import views

urlpatterns = [
    # Provide multiple auth login by default, https://docs.djangoproject.com/en/4.2/topics/auth/default/#using-the-views
    # https://github.com/django/django/blob/4.2.1/django/contrib/auth/urls.py
    path("accounts/", include("allauth.urls")),

    # Django doesn't have a sign up view, so use this guide: https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html  # noqa:E501
    path("sign-up/", views.SignUpFormView.as_view(), name="sign_up"),
    path("", views.index, name="index"),
]
