#!/usr/bin/env bash
# Exit on error, unset variable, or pipe failure
set -euo pipefail

# Run our tests
flake8
black --check .
./manage.py test

if ! $(./manage.py makemigrations --check &> /dev/null); then
  echo 'Missing migration changes, please run `./manage.py makemigrations`' 1>&2
  exit 1
else
  echo 'All migrations created' 1>&2
fi
