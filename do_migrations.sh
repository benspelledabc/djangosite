#!/bin/bash

echo "Making migrations and stuff..."
docker exec benspelledabc_unicorn_web_1 ./imrunicorn/manage.py makemigrations
docker exec benspelledabc_unicorn_web_1 ./imrunicorn/manage.py migrate
docker exec benspelledabc_unicorn_web_1 ./imrunicorn/manage.py collectstatic --no-input
docker exec -it benspelledabc_unicorn_web_1 ./imrunicorn/manage.py createsuperuser

