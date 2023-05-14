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

## Screenshots
Sign up:
![Sign up screenshot](docs/screenshots/sign-up.png)

Confirm email:
![Confirm email screenshot](docs/screenshots/confirm-email.png)

Confirm email (via email link):
![Confirm email (via email link) screenshot](docs/screenshots/confirm-email-confirm.png)

Dashboard:
![Dashboard screenshot](docs/screenshots/dashboard.png)

Logout:
![Logout screenshot](docs/screenshots/logout.png)

## Development
### File structure
We break from the Django recommendations and store almost everything for our application in `app/`.

Why: Django app fragrmentation are from a time when Python modules weren't as robust, [StackOverflow discussion](https://stackoverflow.com/a/64463620/1960509) and [good sides/perspectives](https://stackoverflow.com/a/53735156/1960509).

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
./manage.py test
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
- Copy from `1-django-contrib-auth-forms`
- Clean up `1-django-contrib-auth-forms` mentions + screenshots + setup log
    - `git grep -i "django-contrib"`
    - `git grep -i "django contrib"`
- `git grep -i "django.contrib"`
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

- Seeing "ConnectionRefusedError: [Errno 111] Connection refused" for email sending (as expected)
    - Fix should be to log to console + surface message to user somehow (maybe flash message support now that we have it 🤩), https://django-allauth.readthedocs.io/en/latest/advanced.html#sending-email
<br /><br />

- Getting django-allauth setup rather quickly, a lot less fighting =D Though still relatively involved =/
- I do still feel this is equal to or better than other solutions I've seen. Very robust solution including email verification
<br /><br />

- Having trouble signing in after doing a password reset
- Time to use `./manage.py createsuperuser` and Django Admin finally ✨
- After logging in, I quickly see the email is unverified and easily verify it
    - Sadly no button to resend an email verification =/
<br /><br />

- DONE: Extend messages to the rest of the application
- DONE: Ensure the messages backend is session
<br /><br />

- Ahh, it wasn't verification issues =/
- I was auto-signed in as my superuser into the app, how confusing x_x
<br /><br />

- Using Firefox Container tabs to split out the different cookies =D :galaxy_brain:
    - DONE: Record a note about this in guidance
<br /><br />

- Hmm, we reset the password in Django Admin, and it's still broken?
<br /><br />

- Ohhh, the sign up utility was using the first name as the username -_-;;
- DONE: Fix sign up form to use email as username
- DONE: Add email == username enforcement/validation
- DONE: Add email verification requirement test
<br /><br />

- TODO: Oh, if we have Site(1) in the DB always via migration, then update it via migration ;D
    - Confirmed via fresh `./manage.py migrate` + `./manage.py dbshell`
<br /><br />

- Seeing response in tests in a whole new light =D
    - `context["form"].errors` seems so awesome =o
<br /><br />

- SKIP: Talk about low-level hook for ENV=test
<br /><br />

- DONE: @email_verified decorator
<br /><br />

- DONE: Any lingering TODOs in code?
<br /><br />

- Continued to carrythrough styles from previous pages
- Stuck briefly on mandatory email verification meaning there is no identified user
<br /><br />

- DONE: Talk about {% debug %}
<br /><br />

- DONE: Prob pause efforts on additional pages? Allauth seems to be friendly with incremental, so that's good
<br /><br />

- DONE: Talk through using same app for everything
https://stackoverflow.com/questions/64237/when-to-create-a-new-app-with-startapp-in-django
Nice reassurance from DoorDash philosophy
<br /><br />

- DONE: Pull more notes from exploration recommendations
    - Did all except "template <> views or URL mappings". Clicking through files felt faster .\_.
<br /><br />

- `$ cp -r . ~/github/if-i-were-to-build-a-startup-web-app/explorations/2-django-allauth` + manual relocation
