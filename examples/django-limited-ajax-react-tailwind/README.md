# Django + Limited AJAX + React/Tailwind example
This is an example implementation in [if-i-were-to-build-a-startup-web-app](https://github.com/twolfson/if-i-were-to-build-a-startup-web-app)

At the time of writing, it's strictly a test to sanity check some setup elements for how the latest Tailwind framework interfaces with a Django setup, since it our existing interactions have required build step to filter unwanted content.

Additionally, it should serve as an explanation and example of the "limited AJAX" example we discussed in [UI <> Server Interface Analysis](../../docs/ui-server-interface.md).

## Getting Started
To set up this repo, install the following dependencies:

- Python 3, https://wiki.python.org/moin/BeginnersGuide/Download
- Poetry, https://python-poetry.org/docs/#installation
  - Explanation and comparison vs `pip` as well as `venv` and `virtualenvwrapper` coming soon! (TODO)

then run the following:

```bash
# Open Poetry shell
poetry shell
# Should see "(django-limited-ajax-react-tailwind-py3.8)" now

# Install our dependencies
poetry install

# Run our migrations (we're using SQLite for simplest setup)
./manage.py migrate

# Run our server
./manage.py runserver
```

We can now see our server running locally at <http://127.0.0.1:8000/>

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
