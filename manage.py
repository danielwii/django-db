#!/usr/bin/env python
import os
import sys

from django.apps import apps
from django.conf import settings

conf = {
    'INSTALLED_APPS': [
        # add apps here
    ],
    'DATABASES': {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join('.', 'db.sqlite3'),
        }
    }
}

if __name__ == "__main__":
    settings.configure(**conf)
    apps.populate(settings.INSTALLED_APPS)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
