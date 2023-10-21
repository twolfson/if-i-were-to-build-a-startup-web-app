from django.apps import AppConfig as DjangoAppConfig


class AuthConfig(DjangoAppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app"
