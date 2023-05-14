# Django Contrib Auth Forms exploration
This is an exploration for [if-i-were-to-build-a-startup-web-app](https://github.com/twolfson/if-i-were-to-build-a-startup-web-app)

Initially I planned on writing it as a full setup, but as I built basic authentication in Django, I realized I'd never fully done that end-to-end with their built-ins (previous setup had legacy).

This is now just an exploration for setting up Django with its `django.contrib.auth` forms

## Getting Started
To set up this repo, install the following dependencies:

- Python 3, https://wiki.python.org/moin/BeginnersGuide/Download
- Poetry, https://python-poetry.org/docs/#installation
  - Explanation and comparison vs `pip` as well as `venv` and `virtualenvwrapper` coming soon! (TODO)

then run the following:

```bash
# Open Poetry shell
poetry shell
# Should see "(1-django-contrib-auth-forms-py3.8)" now

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
```bash
# Create basic files
poetry init
# Also specified Django dependency in here

# Creating our Django project
# https://docs.djangoproject.com/en/4.2/intro/tutorial01/#creating-a-project
django-admin startproject mysite

# Relocate mysite to top level, since nesting seems annoying/unnecessary
mv mysite mysite-tmp # Renamed due to `mysite/mysite` to `mysite` conflict
mv mysite-tmp/* .
rm -r mysite-tmp

# Adjusted `settings.py` secret to not include any random data

# Run our migratons and server
./manage.py migrate
./manage.py runserver

# Ignore our DB
git ignore db.sqlite3  # Possibly via `git-extras`

# Verify server running locally
xdg-open http://127.0.0.1:8000/

# Create a proper Django app for ourselves
./manage.py startapp myapp
```

- See multiple folders now, and realize we have knowledge gap around ideal setups
- Research purpose of "mysite" normally
    - https://dev.to/jackdlinke/modern-django-project-examples-58mm
    - https://github.com/mozilla/kitsune
        - Lots of folders in its `kitsune` folder but each of those is a Django app it seems
        - settings.py is at top-level of folder and wsgi.py is its own thing
        - Maybe all tied to being around for a long time?
    - https://github.com/project-koku/koku
        - Similar setup to kitsune but `settings.py` is in a `koku/koku` folder, along with `wsgi.py`
        - More confident that's serving as Django and app core (e.g. users, worker queue)
        - whereas other folders are extensions to that
- Was about to restart with renaming `mysite` to `myproject` but it's the same outcome. Leaving as-is

- Following https://docs.djangoproject.com/en/4.2/intro/tutorial01/ quite closely to remind self of basic setup (so different when working on an existing repo)
- We def need to reconsider things around `myapp` since the naming isn't great for URLs =/
- Read through all of intro, never touches on root pages nor auth
- Finding https://docs.djangoproject.com/en/4.2/topics/auth/

- Setting up login page + redirects

- Realizing no sign up page is built in
- Finding https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html

- Stopped note taking, getting too much in the way. Commits and code comments should capture history well from here

- Performed rename of project
    - `mysite` -> `project`
    - `myapp` -> `app`
    - `git grep -i mysite`
    - `git grep -i myapp`

- Introducing Bootstrap to take this more seriously
- TIL MDN also has their own Django tutorial, https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django

- Learning about Django forms
    - They seem to be quite opinionated and not friendly to custom designs/setups
    - I have a feeling this is for the same reasons Django doesn't have full login pages outside of Django Admin. It was built for serving content outside of admin (newspaper sites), and less of a web app for users to interface with
- Regarding handling widgets and styles
    - A lot of articles say to add CSS to the widget, https://stackoverflow.com/a/5827669/1960509, which imo distributes the CSS around too much + doesn't handle scenarios like a little extra margin
    - Better options are an `addclass` filter, https://stackoverflow.com/a/18962676/1960509
    - But now I'm wondering if I can build some utility to render this common input pattern without copy/pasting the 3 lines for an input every time

- Keep on spining circles around myself, going to document things in a top-level file
