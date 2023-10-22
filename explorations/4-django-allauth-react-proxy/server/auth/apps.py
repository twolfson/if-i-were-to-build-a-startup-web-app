from django.apps import AppConfig as DjangoAppConfig


class AuthenticationConfig(DjangoAppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "authentication"
