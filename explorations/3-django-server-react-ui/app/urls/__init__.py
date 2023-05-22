from django.urls import include, path, re_path

from app import views

urlpatterns = [
    # Auth pages
    # Technically everything is configured to serve at `/accounts/` (e.g. `/accounts/login`))
    #   but UX-wise, stating `/accounts/` in URL just feels confusing =/ (esp if we introduce a model named Account)
    path("", include("app.urls.auth.account")),
    # Social login disabled currently
    # path("socialaccount/", include("app.urls.auth.socialaccount")),

    # Test pages
    path("message-test/", views.message_test, name="message_test"),

    # Any remaining pages are handled by React
    # DEV: We could get clever and use a common router JSON config between apps, but YAGNI for now
    re_path(r".*", views.index, name="index"),
]
