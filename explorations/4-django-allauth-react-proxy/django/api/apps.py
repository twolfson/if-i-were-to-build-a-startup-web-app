from django.apps import AppConfig as DjangoAppConfig


class ApiConfig(DjangoAppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "api"
