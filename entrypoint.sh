#!/usr/bin/env bash
python manage.py collectstatic --noinput
python manage.py migrate --noinput
gunicorn -b :8000 core.wsgi