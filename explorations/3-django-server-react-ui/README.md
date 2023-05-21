# Django Server / React UI exploration
This is an exploration for [if-i-were-to-build-a-startup-web-app](https://github.com/twolfson/if-i-were-to-build-a-startup-web-app)

After building plenty in our [Django Allauth exploration](../2-django-allauth), we realized that .

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

## Screenshots
TODO: Add screenshots

## Development
### File structure
TODO:

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
- TODO: Add new ones?

They should automatically be installed via Poetry and able to be used in your IDE or CLI

### LiveReload
- TODO: Updates for this?
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
- Copy from `2-django-allauth`
- Clean up `2-django-allauth` mentions + screenshots + setup log
    - `git grep -i "django-allauth"`
    - `git grep -i "django allauth"`
- `git grep -i "django.allauth"`
- `rm -r .venv` (to reset `poetry shell` naming)
- Removed `LOGIN_*` and `LOGOUT_*` from `settings.py` to explore defaults
- Following https://django-allauth.readthedocs.io/en/latest/overview.html guidance
- Installed great and nudged around `urls.py` to my comfort
    - Added back `LOGIN_URL`
- "Site" instruction wasn't required it seemed (didn't run, no errors) https://django-allauth.readthedocs.io/en/latest/installation.html#post-installation
    - "Add a Site for your domain, matching settings.SITE_ID (django.contrib.sites app)".
    - My concern with it would be ensuring all new clones get that set up (which is kind of non-trivial from a shell)
    - Note: The "Site" piece came up via "example.com" in the DB
- Docs seem lacking around customization but https://dev.to/gajesh/the-complete-django-allauth-guide-la3 mentioned in FAQ looks solid =D
- It was good for some info, but finding I just need to read between the lines a little on all pages
<br /><br />

