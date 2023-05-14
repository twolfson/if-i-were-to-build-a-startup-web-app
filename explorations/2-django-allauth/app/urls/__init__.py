from django.urls import include, path

from app import views

urlpatterns = [
    # Technically everything is configured to serve at `/accounts/` (e.g. `/accounts/login`))
    #   but UX-wise, stating `/accounts/` in URL just feels confusing =/ (esp if we introduce a model named Account)
    path("", include("app.urls.auth.account")),
    # Social login disabled currently
    # path("socialaccount/", include("app.urls.auth.socialaccount")),
    path("", views.index, name="index"),
]
