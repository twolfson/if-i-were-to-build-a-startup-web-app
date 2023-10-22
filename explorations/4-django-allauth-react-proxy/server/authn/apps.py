from django.apps import AppConfig as DjangoAppConfig


class AuthNConfig(DjangoAppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "authn"
