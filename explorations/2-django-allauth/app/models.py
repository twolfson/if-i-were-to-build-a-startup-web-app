from django.contrib.auth.models import User
from django.db import models  # noqa:F401
from django.core.exceptions import ValidationError

# Override User.clean with custom validation
# DEV: Ideally we use AbstractBaseUser (sp?), but this is a monkey patch solution to stop-gap issues
# fmt: off
_user_clean = User.clean
def user_clean(self, *args, **kwargs):  # noqa:E302
    print('hi')
    if self.username != self.email:
        raise ValidationError("Username is different from email")
    return _user_clean(self, *args, **kwargs)
User.clean = user_clean  # noqa:E305
# fmt: on
