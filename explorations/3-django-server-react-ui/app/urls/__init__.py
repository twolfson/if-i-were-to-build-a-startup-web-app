from django.urls import re_path

from app import views

urlpatterns = [
    # Match anything page-like to React
    # DEV: We could get clever and use a common router JSON config between apps, but YAGNI for now
    # DEV: Do not match *everything*, as this includes `main.*.hot-update.json` which breaks LiveReload in dev
    re_path(r"^[A-Za-z0-9\-/]*$", views.index, name="index"),
]
