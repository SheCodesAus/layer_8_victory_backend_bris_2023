#!/usr/bin/env bash
python manage.py migrate --run-syncdb
python manage.py createsuperuser --no-input
gunicorn --bind :8000 --workers 1 mentorship.wsgi