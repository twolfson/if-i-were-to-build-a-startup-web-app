# if-i-were-to-build-a-startup-web-app Example
This is a repo demonstrating all the concepts concluded in the parent folder

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

## Setup Log
- Copy from `explorations/2-django-allauth`
- Clean up `2-django-allauth` mentions + screenshots + setup log
    - `git grep -i "django-allauth"`
    - `git grep -i "django allauth"`
- `rm -r .venv` (to reset `poetry shell` naming)
