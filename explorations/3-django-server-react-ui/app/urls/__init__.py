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

    # Match anything page-like to React
    # DEV: We could get clever and use a common router JSON config between apps, but YAGNI for now
    # DEV: Do not match *everything*, as this includes `main.*.hot-update.json` which breaks LiveReload in dev
    re_path(r"^[A-Za-z0-9/]*$", views.index, name="index"),
]
