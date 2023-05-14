# Django Allauth exploration
This is an exploration for [if-i-were-to-build-a-startup-web-app](https://github.com/twolfson/if-i-were-to-build-a-startup-web-app)

After getting "far enough" with our [Django Contrib Auth Forms exploration](../1-django-contrib-auth-forms), we still wanted to find a good solution to capture Django's first class User strengths.

## Getting Started
To set up this repo, install the following dependencies:

- Python 3, https://wiki.python.org/moin/BeginnersGuide/Download
- Poetry, https://python-poetry.org/docs/#installation

then run the following:

```bash
# Open Poetry shell
poetry shell
# Should see "(2-django-allauth-py3.8)" now

# Install our dependencies
poetry install

# Run our migrations (we're using SQLite for simplest setup)
./manage.py migrate

# Run our server
./manage.py runserver
```

We can now see our server running locally at <http://127.0.0.1:8000/>

## Development
### Linting
We've configured development with the following:

- `flake8`
- `black`

They should automatically be installed via Poetry and able to be used in your IDE or CLI

### LiveReload
We're using https://github.com/lepture/python-livereload for now. It's not required but it helps with page autorefresh on edit

## Testing
We provide a convenience wrapper for all our test utilities via:

```bash
./manage.py test
```

## Debugging
We install `django-extensions` to get access to `runserver_plus`. This has the following amazing features:

- Better tracebacks (Django's default screen feels lacking/less easy to follow)
- `--print-sql` support to catch `n+1` errors (not an issue in this exploration)
- Interactive debugging console in the middle of a request error, https://django-extensions.readthedocs.io/en/latest/runserver_plus.html
    - You'll be able to find the debugging PIN in your console

## Setup Log
- Copy from `1-django-contrib-auth-forms`
- Clean up `1-django-contrib-auth-forms` mentions + screenshots + setup log
    - `git grep -i "django-contrib"`
    - `git grep -i "django contrib"`
- `git grep -i "django.contrib"`
    - TODO: Update `urls.py`
    - TODO: Update `views.py`
    - TODO: Update `templates/registration/*`
- `rm -r .venv` (to reset `poetry shell` naming)
- Removed `LOGIN_*` and `LOGOUT_*` from `settings.py` to explore defaults
