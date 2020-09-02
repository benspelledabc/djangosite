#!/bin/bash

# echo "Starting up the containers."
# docker-compose up -d
# docker-compose -f /data/django/imrunicorn/docker-compose.yml up -d

echo "Making migrations and stuff..."
docker exec imrunicorn_unicorn_web_1 ./imrunicorn/manage.py makemigrations
docker exec imrunicorn_unicorn_web_1 ./imrunicorn/manage.py migrate
docker exec imrunicorn_unicorn_web_1 ./imrunicorn/manage.py collectstatic --no-input
# docker exec -it imrunicorn_unicorn_web_1 ./imrunicorn/manage.py createsuperuser

echo "Making directories needed for image storage."
docker exec -it imrunicorn_unicorn_web_1 mkdir -p /opt/app/imrunicorn/media/uploads/announcements/what_is_new
docker exec -it imrunicorn_unicorn_web_1 mkdir -p /opt/app/imrunicorn/media/uploads/deer_shots
docker exec -it imrunicorn_unicorn_web_1 mkdir -p /opt/app/imrunicorn/media/uploads/groundhog_kill_shots

echo "Setting Permissions"
docker exec -it imrunicorn_unicorn_web_1 chown -R www-data:www-data /opt/app/imrunicorn

echo "Happy dockering!"
