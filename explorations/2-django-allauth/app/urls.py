from django.urls import include, path

from . import views

urlpatterns = [
    # Provide multiple auth login by default, https://docs.djangoproject.com/en/4.2/topics/auth/default/#using-the-views
    # https://github.com/django/django/blob/4.2.1/django/contrib/auth/urls.py
    path("", include("allauth.urls")),
    path("", views.index, name="index"),
]
