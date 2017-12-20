#!/usr/bin/env python
import os
import sys
from os.path import join

from django.apps import apps
from django.conf import settings
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), verbose=True)

conf = {
    'INSTALLED_APPS': [
        'app',
    ],
}

if os.environ.get('ENV') == 'local':
    conf['DATABASES'] = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': join('.', 'db.sqlite3'),
        },
    }
elif os.environ.get('ENV') == 'development':
    conf['DATABASES'] = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            # 'OPTIONS': {'charset': 'utf8mb4'},
            'NAME': os.environ.get('DB_NAME'),
            'USER': os.environ.get('DB_USER'),
            'PASSWORD': os.environ.get('DB_PASSWORD'),
            'HOST': os.environ.get('DB_HOST'),
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
