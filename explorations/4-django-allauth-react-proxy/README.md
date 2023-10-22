# TODO: See TODOs

- [x] Complete rough django-allauth
- [x] Set up DRF
- [ ] Finish implementing spec we discussed in the explorations file
- [ ] Polish django-allauth (e.g. `messages` handling)

"""
##### Initial auth
- User visits https://app.example.com/foo/bar
    - React SPA loads and looks for `localStorage.loggedIn`
    - It doesn't see it so it redirect to https://app.example.com/auth/login?redirect_uri=/foo/bar
- Browser loads https://app.example.com/auth/login?redirect_uri=/foo/bar
    - Django establishes cookie-based session, with `HttpOnly` and `SameSite=strict` set (should double check on implementation)
        - `HttpOnly` is required to prevent third party scripts from stealing `document.cookie`
        - `SameSite` is required for API piece, will explain there
    - Django presents HTML form with CSRF field
- User logs in
    - Django rotates session id (to prevent session fixation attack)
    - Django saves user ID to session in DB
    - Django redirects user to https://app.example.com/auth-success?redirect_uri=/foo/bar (Auth0 calls this [`/callback`](https://developer.auth0.com/resources/guides/spa/react/basic-authentication), but I like these semantics more)
- Browser loads https://app.example.com/auth-success?redirect_uri=/foo/bar
    - React SPA loads and sets `localStorage.loggedIn = true`
        - We use `true` instead of an expiration because cookies typically self-refresh expiration upon usage
        - Without this `/auth-success` page, React would still think the user is logged out
        - We could use a query parameter as well, but that means handling it on every page and a possible flash of content while it's sorted (this is why Auth0 pushes for it)
        - This page also gives us a common location to capture any relevant events
    - React SPA pushes browser to https://app.example.com/foo/bar

##### API usage
- React SPA makes XHR to https://app.example.com/api/baz
    - Browser uses current cookie, including our session one
    - Django DRF sees the cookie and uses that
    - To mitigate CSRF risk, we need to use `SameSite=strict` when setting the cookie
        - Otherwise, someone could manufacture an HTML form to submit to our API as elaborated above

##### Session expiration
- If the user hasn't interfaced with the app in a while, then their cookie will expire but they'll have `localStorage.loggedIn` still
- User visits https://app.example.com/foo/bar
    - React SPA loads and makes request to Django DRF (our API)
    - (Double check implementation) Django DRF responds with "401 Unauthorized" (we'd use "403 Forbidden" for permission issues)
    - React SPA identifies 401 and unset `localStorage.loggedIn`
    - React SPA continues by redirecting to https://app.example.com/auth/login

##### Logout
- When a user navigates to https://app.example.com/logout
    - React SPA loads and routes to logout page
    - React SPA unsets `localStorage.loggedIn`
    - React SPA redirects to https://app.example.com/auth/logout
- Browser navigates to https://app.example.com/auth/logout
    - (Double check implementation) Django loads, unsets the cookie, and removes the session from the DB
        - Session removal from DB is to prevent session fixation

##### Admin "Login as"
- `django-loginas` is a Django extension which allows logging in as a user via Django Admin
- This is very useful for supporting your team internally
- Intended implementation for us: When the button is pressed
    - It will update the session and cookie to the relevant user
    - Navigate to the redirect URL, which we'll set to our `/auth-success` one
    - `/auth-success` interacts as per usual, treating user as logged in and such
"""

TODO: Update references in README regarding `api` + `ui` -> `django` + `react`

TODO: Walk through django-allauth more thoroughly, https://docs.allauth.org/en/latest/account/configuration.html

TODO: Provide a safeguard that checks `Host` header in development to deter :8000 access

# django-allauth / React proxy exploration
This is an exploration for [if-i-were-to-build-a-startup-web-app](https://github.com/twolfson/if-i-were-to-build-a-startup-web-app)

TODO: Update after security exploration

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
- Generally smooth, then a `ModuleNotFoundError: No module named 'allauth.account.middleware'` hiccup due to docs being in front of released version
    - https://stackoverflow.com/a/77013205/1960509
- It was caused by copying the old `pyproject.toml`
- Going to just upgrade to 0.57.0 =) https://pypi.org/project/django-allauth/#history

- Got the `:8000` (Django version) working
- but then `:3000` has some CSRF origin complaints (as it should)
- `    Origin checking failed - http://localhost:3000 does not match any trusted origins.`
- Fixing that... (notes in commits)
- But out of time for now
- Generally seem to be in the right spot though
- Also seeing a path forward with just building right tools for disconnected apps + setup (tradeoffs for each)
    - e.g. Should be able to get `django-loginas` working properly in both if we build the right handoff chain for JWT callbacks

### Security detour
- After some time away from the repo, we realized there were security considerations we needed to cover, so moving those into `docs/explorations.md` in the main repo

### Continuing setup
- Back from security detour
- Informed/confirms that proxy + cookie is the simplest and easiest choice to move forward
- Switched to `django-allauth-ui` for some prestyled pages =D
- Tweaking and processing settings

- Rename folders due to realizing we want to break up `api` from `auth` routes and `api/auth` + `api/api` feels weird
    - Renamed from `api` -> `django` + `ui` -> `react` -- more fitting anyway =)
    - If we ever change stack, changing folders would be a likely outcome as-is
- Removed `.venv` + reinstalled Poetry packages
- Relocated `django/app` to `django/auth`
- Created `django/api` via `./manage.py startapp api`
- Started Django REST Framework setup
- Performed another rename due to fearing `django` import possibly getting messed up by top level folder
- Renamed `AppConfig` for `auth` to `server-auth` due to conflict with Django's `auth` package
- Then to `authn` when it wanted the name for the containing folder
