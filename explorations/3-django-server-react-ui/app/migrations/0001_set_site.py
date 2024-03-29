# Generated by Django 4.2.1 on 2023-05-14 22:58

from django.db import migrations
from project.settings import ENV, PRODUCTION, TEST


# DEV: Use `shell_plus --print-sql` to test for `n+1` queries locally before deploying to `production`
def _backfill(apps, schema_editor, dry_run=True):
    # Tests don't have sites set up, so exit early
    if ENV == TEST:
        return

    # Load our models
    # "sites" resolves django.contrib.sites, as expected
    Site = apps.get_model("sites", "Site")

    # Retrieve our only site (will error out if not exactly 1)
    site = Site.objects.get()
    assert site.id == 1
    assert ENV != PRODUCTION, "domain_name not configured properly for production"
    site.domain = "twolfson.com"
    site.name = "twolfson.com"
    site.save()


def assert_for_backfill(*args, **kwargs):
    return _backfill(*args, **kwargs, dry_run=True)


def backfill(*args, **kwargs):
    return _backfill(*args, **kwargs, dry_run=False)


class Migration(migrations.Migration):
    dependencies = []

    operations = [
        # Nothing to assert since jumping into backfill immediately
        # migrations.RunPython(assert_for_backfill),

        # Normally we might include a column migration here

        migrations.RunPython(backfill),
    ]
