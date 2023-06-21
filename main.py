#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import sys

from django.urls import path
from django.http import HttpResponse
from django.conf import settings
from django.core.wsgi import get_wsgi_application


settings.configure(
    DEBUG=True,
    ROOT_URLCONF=__name__,
    SECRET_KEY="secret"
)

application = get_wsgi_application()


def hello_world(request):
    return HttpResponse("Hello World")


urlpatterns = [
    path('', hello_world),
]


def main():
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
