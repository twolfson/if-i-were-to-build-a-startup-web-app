# TODO: See TODOs

# django-allauth / React proxy exploration
This is an exploration for [if-i-were-to-build-a-startup-web-app](https://github.com/twolfson/if-i-were-to-build-a-startup-web-app)

A common setup in the wild is a JWT-based API and a React development server (e.g. `create-react-app`) as 2 separate servers talking over CORS.

I'd like to explore consolidating these 2 on the same server with a proxy, and seeing the benefits that fall out (potentially cookies, no annoying JWT tracking/handoffs, no CORS + preflight `OPTIONS` requests, immediate standup of `django-allauth` with ability for full customization, and ability to fully integrate UI in the future).

## How to proxy
In the Django case, it might be possible to have Django proxy the React development server, but those servers typically use Websockets, which is quite the headache.

NGINX would be another alternative but it's abnormal to have that run in development.

We could do a Node.js proxy server as well, but instead of 2 separate Node.js servers (proxy + React development server), we can just repurpose the React development one as well =)

In production, the setup would be an NGINX server with the same proxy routing pointing towards Django

## Getting Started
To set up this repo, install the following dependencies:

- Python 3, https://wiki.python.org/moin/BeginnersGuide/Download
- Poetry, https://python-poetry.org/docs/#installation
- Node.js, https://nodejs.org/en/download

then run the following:

```bash
# Navigate to our API folder
cd api/

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
- Roughly same as `2-django-allauth` exploration
- New addition: `ui/`, container for all React files

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
- `eslint`
- `prettier`

They should automatically be installed via Poetry and able to be used in your IDE or CLI

### LiveReload
https://github.com/lepture/python-livereload can be used for refreshing pages on Django HTML edit.

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
### Django setup
- Starting fresh without other explorations (though will copy/paste)

```bash
mkdir api/
poetry shell
# No pyproject.toml yet
# Copy over relevant files poetry.lock, poetry.toml, pyproject.toml
# With some motifications
$ cp ../../3-django-server-react-ui/pyproject.toml .
$ cp ../../3-django-server-react-ui/poetry.lock .
$ cp ../../3-django-server-react-ui/poetry.toml
$ cp ../../3-django-server-react-ui/poetry.toml .
$ cp ../../3-django-server-react-ui/test.sh .
$ cp ../../3-django-server-react-ui/.gitignore .
$ cp ../../3-django-server-react-ui/setup.cfg .
```

- Continued to copy files, this time from `1-django-contrib-auth-forms` + deleting unneeded content

- All good and page loading =)

### React setup
- Now moving on to React as proxy work
- Looking at `3-django-server-react-ui` setup log
- Easiest path is prob `npx create-react-app ui`, https://create-react-app.dev/docs/getting-started
- so doing that

- Transferred `package.json`
- And realizing all of `3-django-server-react-ui/ui` was prob good off the shelf
- Grabbed that + modified/reduced down pages
    - TODO: Delete `AuthLayout.jsx` if unused
- Finding ourselves missing UI + styles
- Using part of `index.html` from exploration 3

### Proxy setup
- Finally ready to dig into proxy exploration, https://create-react-app.dev/docs/proxying-api-requests-in-development/
- No luck so far =/
- I think I see the problem: "The development server will only attempt to send requests without text/html in its Accept header to the proxy."

### django-allauth setup
- Going to now explore `django-allauth` (again...?)
- https://docs.allauth.org/en/latest/installation/quickstart.html
