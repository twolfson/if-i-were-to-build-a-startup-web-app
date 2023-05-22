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
    - `git grep -i "django\.allauth"`
- `rm -r .venv` (to reset `poetry shell` naming)
<br /><br />

- `poetry shell` to enter new virtual env
- `poetry install` to refresh dependencies
- First priority: Shedding Django Template UI mostly + integrating React
    - Prob will keep Bootstrap styling for development velocity
    - with none of its JS (to avoid React <> jQuery headaches)
- `npx create-react-app ui`, https://create-react-app.dev/docs/getting-started
    - TODO: Show logged in state or not
    - TODO: Handle auth or not, including logout
    - TODO: Handle dashboard page (to push limits of React Query)
        - Counts + recent tasks + notifications
    - TODO: Handle notifications dismissable (loading state UI)
- Looking for docs around hosting running server vs built JS
    - Red herring: CORS (multi-domain) focused setup, https://www.digitalocean.com/community/tutorials/build-a-to-do-application-using-django-and-react
    - This seems to do it well, following this: https://www.saaspegasus.com/guides/modern-javascript-for-django-developers/integrating-django-react/
        - All good except for the webpack build piece, but I think we can work around that with dev/production toggling
- Realizing we should start with the build version first
- Learning that `create-react-app` has sane defaults with hashed filenames, https://github.com/facebook/create-react-app/issues/821
    - https://github.com/rykener/django-manifest-loader seems like a promising solution
