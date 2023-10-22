# django-allauth / React proxy exploration

# TODO: See TODOs

TODO: Django doesn't have a session set up on login page... so unsure session fixation/rotation applies -- prob review/update plan once done

TODO: Update references in README regarding `api` + `ui` -> `django` + `react`

TODO: Walk through django-allauth more thoroughly, https://docs.allauth.org/en/latest/account/configuration.html

TODO: Provide a safeguard that checks `Host` header in development to deter :8000 access
This is an exploration for [if-i-were-to-build-a-startup-web-app](https://github.com/twolfson/if-i-were-to-build-a-startup-web-app)

TODO: Update after security exploration

A common setup in the wild is a JWT-based API and a React development server (e.g. `create-react-app`) as 2 separate servers talking over CORS.

I'd like to explore consolidating these 2 on the same server with a proxy, and seeing the benefits that fall out (potentially cookies, no annoying JWT tracking/handoffs, no CORS + preflight `OPTIONS` requests, immediate standup of `django-allauth` with ability for full customization, and ability to fully integrate UI in the future).

## How to proxy
In the Django case, it might be possible to have Django proxy the React development server, but those servers typically use Websockets, which is quite the headache.

NGINX would be another alternative but it's abnormal to have that run in development.

We could do a Node.js proxy server as well, but instead of 2 separate Node.js servers (proxy + React development server), we can just repurpose the React development one as well =)

In production, the setup would be an NGINX server with the same proxy routing pointing towards Django

## What's missing from this implementation
- `fetch` usages don't handle errors like API giving a 404 and trying JSON parsing
- Handling redirects on login or sign-up isn't built out
    - TODO: Link back to architectural layout

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

- Started walking through specification we laid out
- Had a weird state where I was logged in but no cookie - so thought Django somehow had no sessions by default, but nope =)
- and that won't be the case in practice =P
- Aaah, it was an allauth setting for cookie duration =)

- Huuuh, the CSRF piece is accessible as a cookie, https://docs.djangoproject.com/en/4.2/ref/settings/#csrf-cookie-httponly
    - which breaks my brain on some levels but also makes a lot of sense
    - and almost warrants another security detour .\_.

- Back from a walk/break
- CSRF is not so bad tbh, and changes nothing here
- TODO: Update nuance in the security detour and #3 to talk through CSRF tweaks (i.e. no field needed, but still need to touch a Django page)
- I also did a sanity check video watch of a demo of Auth0 to verify the URL scheme is roughly where we're at with nothing unexpected, https://www.youtube.com/watch?v=RpfEk6drhPc
- TODO: Room for improvement based on video + CSRF realization, instead of `localStorage.loggedIn`, we could do a JSON non-HttpOnly cookie with user info that the browser can consume ASAP (though it comes with all the same issues as JWT)
    - Yea, it's tricky because it's valid at login but then becomes junk if they change mid-session =/ So need to wire in to all those points .\_. YAGNI + KISS
- Actually... yea, going with a basic replacement of `localStorage` because it simplifies the React side greatly =)

- Cookies were a bit of a hassle, but it's done
- and the end result does feel a lot simpler (e.g. no mismatched expiration concerns)

- `django-loginas` has also been added, and works very quickly and easily =D

- Fixed up permissions for DRF endpoints we made

- Exploring messages and Toast libraries
- This one has put effort into accessibility apparently =D
    - https://fkhadra.github.io/react-toastify/introduction/
    - https://github.com/fkhadra/react-toastify/issues/121

- Toast is working great
- `drf-messges` doesn't work out of the box
- I started to consider a fetch/similar for `react-query`, but then started looping on trying to understand logic behind `actions`
    - Def some mixed feelings since there's been aggressive rewrites
    - and the structure isn't easily alleviated
    - and we had a pretty good patter from before with `_layout` JSX + statuses
    - https://reactrouter.com/en/main/guides/data-libs

- Next day
- Deciding to keep pushing on messages, otherwise it's an incomplete experience
- Also realized there's prob AJAX Django messages support out there
- Sadly, all seems out of date =(
- TODO: Create one-off gist for messages endpoint
