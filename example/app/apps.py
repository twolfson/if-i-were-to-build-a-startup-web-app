from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app"

    def ready(self):
        # Import our signals once everything else loaded
        # https://docs.djangoproject.com/en/4.2/topics/signals/#:~:text=Where%20should%20this%20code%20live%3F
        import app.signals  # noqa:F401
