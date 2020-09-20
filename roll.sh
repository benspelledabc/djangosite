#!/bin/bash

docker pull benspelledabc/djangosite:3.14.16
docker-compose down
docker-compose up -d

# docker exec -it imrunicorn_unicorn_web_1 imrunicorn/manage.py makemigrations
# docker exec -it imrunicorn_unicorn_web_1 imrunicorn/manage.py migrate
docker exec -it imrunicorn_unicorn_web_1 imrunicorn/manage.py collectstatic --no-input
