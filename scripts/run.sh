#!/bin/sh

set -e

python manage.py wait_for_db
python manage.py collectstatic --noinput
python manage.py migrate

#gunicorn app.wsgi:application --workers 4 --bind localhost:8000
#uwsgi --socket :9000 --workers 10 --master --enable-threads --module qnode0_app.wsgi