#!/bin/sh

echo "Collect static files"
python manage.py collectstatic --noinput


echo "Apply database migrations"
python manage.py makemigrations app
python manage.py migrate

echo "Starting server"
python manage.py runserver 0.0.0.0:8000