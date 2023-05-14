from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from django.dispatch import receiver


# https://docs.djangoproject.com/en/4.2/ref/signals/#pre-save
@receiver(pre_save, sender=User)
def user_validate_username_email_same(sender, instance, **kwargs):
    if instance.username.lower() != instance.username:
        raise ValidationError("Username is not lowercased")
    if instance.username != instance.email:
        raise ValidationError("Username is different from email")
