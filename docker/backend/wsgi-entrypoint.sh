#!/bin/sh

python manage.py makemigrations

until python manage.py migrate
do
    echo "Waiting for db to be ready..."
    sleep 2
done

python manage.py compilemessages
python manage.py collectstatic --noinput

python manage.py runserver 0.0.0.0:8000
