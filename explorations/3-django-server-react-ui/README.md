TODO: See TODOs

# Django Server / React UI exploration
This is an exploration for [if-i-were-to-build-a-startup-web-app](https://github.com/twolfson/if-i-were-to-build-a-startup-web-app)

After building plenty in our [Django Allauth exploration](../2-django-allauth), we wanted to explore having a UI fully built on React with Django handling endpoints only.

After setting this roughly up, I can say that it is possible, but it was quite painful and I'd be concerned around long-term maintenance.

TODO: Why is this painful maintenance?

## Getting Started
To set up this repo, install the following dependencies:

- Python 3, https://wiki.python.org/moin/BeginnersGuide/Download
- Poetry, https://python-poetry.org/docs/#installation
- Node.js, https://nodejs.org/en/download

then run the following:

```bash
# Open Poetry shell
poetry shell
# Should see "(2-django-allauth-py3.8)" now

# Install our dependencies
poetry install

# Run our migrations (we're using SQLite for simplest setup)
./manage.py migrate

# Run our Django server
./manage.py runserver

# In a separate tab, navigate to our UI folder
cd ui/

# Install our Node.js dependencies
npm install

# Run our React server
npm start
```

We can now see our server running locally at <http://127.0.0.1:8000/>

## Screenshots
TODO: Add screenshots

## Development
### File structure
TODO: Write me out

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
<br /><br />

- Finagled and finagled some more, but finally got everything loading as desired
- Saw an SVG non-inline loading issue, but honestly I think that's part of growth for an app (e.g. inlining SVGs should be a thing)
    - All other images normally would just be served from a Django folder (like HTML)
<br /><br />

- Slowly trying to get Django serving React content, but struggling hard to get LiveReload working
- https://stackoverflow.com/a/58040422/1960509 might be promising for proxying??
- Ah, I found the issue -- the `main.*.hot-update.json` is loading at `/`, not specifying host, so it's confused when on :8000, not :3000 as expected
- Fixing our `urls.py` to not be so aggressive fixed the issue =D
<br /><br />

- Got up to HTML form submission working =D
- And then we realized that the UX of submitting an HTML form to have a React loading screen afterwards, is even more janky, than a minor one-off text field being overridden for better suggestion support .\_.

- TODO: If we resume this, here's some notes from earlier:
    - Validation errors. Don't need per field. Top of form good enough start
    - Email suggest. Nothing robust needed. Just "email suggestion goes here" if not matching current ones (e.g. todd@twolfson.com)
    - Large drawback of split is rework pain
        - If underlying API changes but page doesn't. Lots of work for serializer
- TODO: The infighting with setups like this is also part of a reason to not adopt such an architecture. It's quite finnicky at setup, and prob similar to maintain
    - Full React also has similar drawbacks though =/ (e.g. juggling JWT is a pain)
        - but maybe that's where split Django auth + split React post-auth shines
