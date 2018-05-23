import os
import sys

os.environ.sefdefault('DJANGO_SETTINGS_MODULE','website.settings')

from django.core.handlers.wsgi import WSGIHandler
application=WSGIHandler()
