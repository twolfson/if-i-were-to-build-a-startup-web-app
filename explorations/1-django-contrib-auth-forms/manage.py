#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import warnings


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

    # If we're running our tests, fallback our appropriate environment variable
    # sys.argv = ['manage.py', 'test']  # python manage.py test
    # sys.argv = ['./manage.py', 'test']  # ./manage.py test
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        os.environ["ENV"] = "test"

        # Additionally, enable warnings to catch issues early (instead of at Django upgrade)
        #   https://docs.djangoproject.com/en/4.2/howto/upgrade-version/#resolving-deprecation-warnings
        #   https://docs.python.org/3.8/library/warnings.html#overriding-the-default-filter
        #   We'd put this outside of `main()` but it gets noisy with `runserver_plus`
        if not sys.warnoptions:
            warnings.simplefilter("default")  # Change the filter in this process
            os.environ["PYTHONWARNINGS"] = "default"  # Also affect subprocesses


if __name__ == "__main__":
    main()
