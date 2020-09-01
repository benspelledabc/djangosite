#!/bin/bash


echo "Making migrations and stuff..."
docker exec $1_unicorn_web_1 ./imrunicorn/manage.py makemigrations
docker exec $1_unicorn_web_1 ./imrunicorn/manage.py migrate
docker exec $1_unicorn_web_1 ./imrunicorn/manage.py collectstatic --no-input
docker exec -it $1_unicorn_web_1 ./imrunicorn/manage.py createsuperuser

