import os, sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'Chimera.settings'

# Google App Engine imports.
from google.appengine.ext.webapp import util

# Force Django to reload its settings.
from django.conf import settings

settings._target = None

import MySQLdb

print MySQLdb.apilevel

import django.core.handlers.wsgi
import django.core.signals
import django.dispatch.dispatcher

app = django.core.handlers.wsgi.WSGIHandler()


def main():
    util.run_wsgi_app(app)


if __name__ == '__main__':
    main()
