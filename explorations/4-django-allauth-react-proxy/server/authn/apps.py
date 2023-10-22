from django.apps import AppConfig as DjangoAppConfig


class AuthNConfig(DjangoAppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "authn"

    def ready(self):
        # https://docs.djangoproject.com/en/4.2/topics/signals/#connecting-receiver-functions
        # Implicitly connect signal handlers decorated with @receiver.
        from . import signals  # noqa:F401
