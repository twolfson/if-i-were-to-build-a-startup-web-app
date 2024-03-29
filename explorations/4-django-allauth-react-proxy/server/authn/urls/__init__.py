from django.urls import include, path

from authn import views

urlpatterns = [
    # django-allauth pages
    # Technically everything is configured to serve at `/accounts/` (e.g. `/accounts/login`))
    #   but UX-wise, stating `/accounts/` in URL just feels confusing =/ (esp if we introduce a model named Account)
    path("", include("authn.urls.account")),
    path("social/", include("authn.urls.socialaccount")),
    # Auxiliary support for messages generated by django-allauth (e.g. logged in, email confirmation sent)
    path("messages/", views.messages),
]
