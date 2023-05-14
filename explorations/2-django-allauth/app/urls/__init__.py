from django.urls import include, path

from app import views

urlpatterns = [
    path("", include("app.urls.auth")),
    path("", views.index, name="index"),
]
