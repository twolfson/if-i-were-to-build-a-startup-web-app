from django.urls import include, path

urlpatterns = [
    # Auth pages
    # Technically everything is configured to serve at `/accounts/` (e.g. `/accounts/login`))
    #   but UX-wise, stating `/accounts/` in URL just feels confusing =/ (esp if we introduce a model named Account)
    path("", include("auth.urls.account")),
    # Social login disabled currently
    # path("social/", include("auth.urls.socialaccount")),
]
