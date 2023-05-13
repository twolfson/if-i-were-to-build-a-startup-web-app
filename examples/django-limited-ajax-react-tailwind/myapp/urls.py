from django.urls import include, path

from . import views

urlpatterns = [
    # Provide multiple auth login by default, https://docs.djangoproject.com/en/4.2/topics/auth/default/#using-the-views
    # DEV: Technically auth isn't required for demo purposes, but we think this highlights Django's strengths
    path("", include("django.contrib.auth.urls")),

    path("", views.index, name="index"),
]
