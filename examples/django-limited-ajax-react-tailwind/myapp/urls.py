from django.urls import include, path

from . import views

urlpatterns = [
    # Provide multiple auth login by default, https://docs.djangoproject.com/en/4.2/topics/auth/default/#using-the-views
    # DEV: Technically auth isn't required for demo purposes, but we think this highlights Django's strengths
    path("", include("django.contrib.auth.urls")),
    # Django doesn't have a sign up view despite a form, so use this guide: https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
    path("sign-up/", views.SignUpFormView.as_view(), name="sign_up"),

    path("", views.index, name="index"),
]
