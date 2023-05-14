from django.urls import include, path

from app import views

urlpatterns = [
    path("account/", include("app.urls.auth.account")),
    # Social login disabled currently
    # path("socialaccount/", include("app.urls.auth.socialaccount")),
    path("", views.index, name="index"),
]
