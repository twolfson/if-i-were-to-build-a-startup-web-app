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
```
