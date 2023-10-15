# if-i-were-to-build-a-startup-web-app Example
This is a repo demonstrating all the concepts concluded in the parent folder

TODO: See TODOs

## Getting Started
To set up this repo, install the following dependencies:

- Python 3, https://wiki.python.org/moin/BeginnersGuide/Download
- Poetry, https://python-poetry.org/docs/#installation

then run the following:

```bash
# Open Poetry shell
poetry shell
# Should see "(if-i-were-example-py3.8)" now

# Install our dependencies
poetry install

# Run our migrations (we're using SQLite for simplest setup)
./manage.py migrate

# Run our server
./manage.py runserver
```

## Screenshots
TODO: Add screenshots

## Development
### File structure
We break from the Django recommendations and store almost everything for our application in `app/`.

Why: Django app fragmentation are from a time when Python modules weren't as robust, [StackOverflow discussion](https://stackoverflow.com/a/64463620/1960509) and [good sides/perspectives](https://stackoverflow.com/a/53735156/1960509).

We believe that abstraction without a use case is busy work, and our `auth` setup is strictly a customization of `django-allauth` (not worth abstracting). Thus, we lean into Python modules instead.

- `.venv/` - Virtual environment for our Python dependencies
- `app/` - Container for almost everything in our app
    - Normal Django folders you expect (e.g. `forms`, `migrations`, `templates`)
- `docs/` - Container for documentation (strictly screenshots for now)
- `project/` - Settings for project and web server utilities
- `manage.py` - Wonderful CLI utility for Django. `./manage.py` all the things!
- `poetry.*`, `pyproject.toml`, `setup.cfg` - Poetry, `flake8`, and more tooling configuration
- `README.md` - Documentation you're reading
- `test.sh` - Test runner utility (`ENV=test` is setup via `manage.py` modifications)

### Django Admin
Django Admin can be set up via the following:

```bash
./manage.py createsuperuser
# Username (leave blank to use '$USER'):
# Email address: my@email.com
# Password:
# Password (again):
# Superuser created successfully.
```

Alternatively, you can promote the user via `./manage.py shell_plus`

```python
# Inside ./manage.py shell_plus (auto-imports User)
user = User.objects.first()
user.is_superuser = True
user.is_staff = True
user.save()
```

You can now log in to Django Admin to view things like user and email verification:

http://127.0.0.1:8000/admin/

**We strongly recommend using a separate [browser profile](https://support.google.com/chrome/answer/2364824) (Chrome) or [container tab](https://support.mozilla.org/en-US/kb/containers) (Firefox). Otherwise, Django Admin shares the same session with the app, and this complicates debugging.**

![Django Admin screenshot](docs/screenshots/django-admin.png)

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
./test.sh
```

## Debugging
We install `django-extensions` to get access to `runserver_plus`. This has the following amazing features:

- Better tracebacks (Django's default screen feels lacking/less easy to follow)
- `--print-sql` support to catch `n+1` errors (not an issue in this exploration)
- Interactive debugging console in the middle of a request error, https://django-extensions.readthedocs.io/en/latest/runserver_plus.html
    - You'll be able to find the debugging PIN in your console

Additionally, we get `shell_plus` which gives us the same `--print-sql` support and automatic imports in an IPython shell

Additionally, inside templates, a handy utility is `{% debug %}` which dumps all available context variables

## Setup Log
- Copy from `explorations/2-django-allauth`
- Clean up `2-django-allauth` mentions + screenshots + setup log
    - `git grep -i "2-django-allauth"`
- `rm -r .venv` (to reset `poetry shell` naming)
